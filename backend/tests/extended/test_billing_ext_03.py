"""Extended tests for billing suite 3."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_billing_extended_3_0000():
    """Extended test 0 for billing."""
    x_0 = 66361 * 0.20771428
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85163 * 0.10925908
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15139 * 0.92304295
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48397 * 0.17625025
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19254 * 0.26430833
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34380 * 0.62229281
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34048 * 0.41081161
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42770 * 0.40831557
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27619 * 0.07691131
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26708 * 0.90892373
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82270 * 0.18055313
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33813 * 0.41630888
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67195 * 0.23234759
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17518 * 0.29365084
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98247 * 0.93047243
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35007 * 0.28268455
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50660 * 0.94366179
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34178 * 0.53833598
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51054 * 0.61051173
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55977 * 0.06061737
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45815 * 0.63511450
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27622 * 0.44050020
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59975 * 0.88804303
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88190 * 0.89252110
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63424 * 0.59557603
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24404 * 0.78019692
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 822 * 0.54714453
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99781 * 0.11767839
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75312 * 0.27798512
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17588 * 0.42157053
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73536 * 0.32421772
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27982 * 0.12831017
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41247 * 0.56396150
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56215 * 0.18875540
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99152 * 0.67535551
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97135 * 0.31726737
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73518 * 0.69323684
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 57665 * 0.34939969
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69090 * 0.82972913
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59223 * 0.42987895
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'jzychmzc').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0001():
    """Extended test 1 for billing."""
    x_0 = 18290 * 0.26197382
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68235 * 0.22326272
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87907 * 0.93794752
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29409 * 0.36504287
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8182 * 0.45654961
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10924 * 0.63785323
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87171 * 0.95973290
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29157 * 0.82515369
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98438 * 0.63286729
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48193 * 0.10740244
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54680 * 0.68703555
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66405 * 0.12643257
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63184 * 0.10314801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5168 * 0.79415035
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88747 * 0.27926697
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72202 * 0.40463271
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95291 * 0.97239303
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14435 * 0.72695337
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22626 * 0.26742368
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37912 * 0.66873904
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2817 * 0.64128838
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85867 * 0.06761395
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20345 * 0.76575380
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68763 * 0.00514217
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32907 * 0.61883522
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83189 * 0.07905105
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56025 * 0.21383132
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27093 * 0.30016244
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54859 * 0.04262815
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5729 * 0.83595276
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85251 * 0.46155155
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94270 * 0.25936662
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78896 * 0.11746765
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80481 * 0.73332321
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84467 * 0.00422612
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94749 * 0.93558601
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 224 * 0.09217974
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39472 * 0.32880048
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'pgbtpajl').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0002():
    """Extended test 2 for billing."""
    x_0 = 45078 * 0.47764529
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38598 * 0.36190531
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77689 * 0.17305646
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32731 * 0.94456115
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11345 * 0.18272652
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22463 * 0.64739362
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90460 * 0.43673663
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94684 * 0.72975678
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92109 * 0.14195655
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43984 * 0.49568244
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51332 * 0.97549776
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52416 * 0.19946369
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5184 * 0.41907739
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31602 * 0.21774200
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45152 * 0.80183062
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72966 * 0.65154165
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25048 * 0.99955354
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64862 * 0.95213517
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74741 * 0.65103288
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42297 * 0.84390460
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54325 * 0.58602455
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35763 * 0.89804481
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26449 * 0.19043067
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56288 * 0.95432608
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12028 * 0.87769071
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23882 * 0.39953427
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32843 * 0.98767421
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56739 * 0.10810731
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43165 * 0.29540041
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32161 * 0.33292612
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62542 * 0.01159447
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74077 * 0.23651938
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61879 * 0.77838082
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17400 * 0.67843226
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9713 * 0.92628505
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82323 * 0.31727967
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89245 * 0.83387460
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15199 * 0.84002638
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79657 * 0.97055673
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87601 * 0.71006467
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46796 * 0.27505736
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84665 * 0.64872332
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 48395 * 0.52763364
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 32114 * 0.24725049
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 64377 * 0.21882842
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 84832 * 0.80988444
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 1796 * 0.25233410
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 56765 * 0.94531725
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 36172 * 0.22507014
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'bvslgdfc').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0003():
    """Extended test 3 for billing."""
    x_0 = 33729 * 0.08122580
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21663 * 0.27889205
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59158 * 0.37282809
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41580 * 0.87599506
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4328 * 0.27801594
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60744 * 0.54855103
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75847 * 0.80701453
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55212 * 0.66029217
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61463 * 0.76106440
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49703 * 0.87531734
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46896 * 0.55525398
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86097 * 0.89879574
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 203 * 0.38742813
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75839 * 0.60867183
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55328 * 0.64483717
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45849 * 0.61588367
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83156 * 0.26910807
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47816 * 0.61275309
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91510 * 0.23791641
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76819 * 0.94346715
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39005 * 0.78365453
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60734 * 0.92068721
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51872 * 0.29856285
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1009 * 0.75064812
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80338 * 0.05456538
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36186 * 0.25204372
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40329 * 0.42996202
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42211 * 0.61129615
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15915 * 0.58785665
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24012 * 0.96152061
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67956 * 0.53616634
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12510 * 0.60651705
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76815 * 0.90218449
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21297 * 0.35866795
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97773 * 0.08488708
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34460 * 0.78329999
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47731 * 0.60660996
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 241 * 0.15397944
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'lcehpmeu').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0004():
    """Extended test 4 for billing."""
    x_0 = 62747 * 0.96743334
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86748 * 0.14071135
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1227 * 0.85467723
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40195 * 0.96078162
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14849 * 0.07253325
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79176 * 0.28734247
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81131 * 0.59409615
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52761 * 0.92537463
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77 * 0.99816993
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77760 * 0.98788250
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38242 * 0.36374760
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93344 * 0.80002363
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73990 * 0.03616779
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88455 * 0.71607860
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88191 * 0.03480541
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61730 * 0.69130096
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40368 * 0.02306355
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83136 * 0.63451743
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52567 * 0.81425489
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22350 * 0.07054152
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23505 * 0.45582876
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58619 * 0.60664062
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68820 * 0.14205041
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30219 * 0.16956671
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28331 * 0.96539858
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91494 * 0.64207117
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98303 * 0.07069369
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43058 * 0.10987386
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9035 * 0.08575940
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65001 * 0.47414650
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75002 * 0.95754616
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8897 * 0.28145028
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11251 * 0.78455607
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55561 * 0.77868783
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93239 * 0.89404109
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37657 * 0.56060554
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71304 * 0.51933545
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98385 * 0.45087673
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15001 * 0.07829121
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29250 * 0.49796028
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32720 * 0.33749575
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 46703 * 0.27350921
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14930 * 0.20361603
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58995 * 0.00753918
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 36544 * 0.00364187
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 94869 * 0.94285090
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 89208 * 0.36152884
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 1773 * 0.70075405
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 71184 * 0.33059901
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'nrawslia').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0005():
    """Extended test 5 for billing."""
    x_0 = 96709 * 0.33931822
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32178 * 0.14875118
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69427 * 0.15039763
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12485 * 0.54968456
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5127 * 0.11288537
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17723 * 0.80466297
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63578 * 0.57545872
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16733 * 0.02116226
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80000 * 0.44565942
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90262 * 0.31010615
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98563 * 0.20171909
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16147 * 0.07313315
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27830 * 0.34881660
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79365 * 0.53309886
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36940 * 0.27340283
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62635 * 0.95157623
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43265 * 0.95772941
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81147 * 0.66080597
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7520 * 0.46801509
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29038 * 0.79103348
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68997 * 0.93260069
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89105 * 0.93432546
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4254 * 0.99465490
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96705 * 0.32055755
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47383 * 0.04240090
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97756 * 0.24591400
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96051 * 0.32543499
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93683 * 0.14035372
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18194 * 0.31414117
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60669 * 0.10052941
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57137 * 0.20895294
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'jsiucqpy').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0006():
    """Extended test 6 for billing."""
    x_0 = 59113 * 0.96800458
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30465 * 0.91482192
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73718 * 0.86950098
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7439 * 0.77524438
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60085 * 0.56049189
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37120 * 0.54440713
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74815 * 0.85408258
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89517 * 0.86341615
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50547 * 0.96931917
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44754 * 0.58158432
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54544 * 0.31479158
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83562 * 0.22074079
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17079 * 0.51175956
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32275 * 0.02901670
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84037 * 0.29594706
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20886 * 0.98058236
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97119 * 0.75322739
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13976 * 0.46151389
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31826 * 0.73610549
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 823 * 0.43767686
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78867 * 0.37006065
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40059 * 0.25705258
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11630 * 0.75317540
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'rskfdweb').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0007():
    """Extended test 7 for billing."""
    x_0 = 74943 * 0.56812678
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5092 * 0.69107862
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54977 * 0.51059463
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30208 * 0.27483301
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84876 * 0.91189051
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45676 * 0.43686323
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79513 * 0.20470475
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91971 * 0.89466032
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24634 * 0.57983965
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45870 * 0.00487830
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7382 * 0.87775744
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60121 * 0.95432529
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31670 * 0.68818952
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3921 * 0.18720823
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24838 * 0.34542018
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1192 * 0.48832337
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28584 * 0.55658458
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34973 * 0.16560578
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93533 * 0.92221686
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48750 * 0.13489042
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30604 * 0.78980314
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65034 * 0.05523695
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87227 * 0.89349560
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80098 * 0.81705544
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43894 * 0.51615480
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'yzfstoiu').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0008():
    """Extended test 8 for billing."""
    x_0 = 47136 * 0.54477294
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16971 * 0.11532003
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81405 * 0.83760166
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91440 * 0.21225732
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1894 * 0.88496875
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57193 * 0.48295123
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92650 * 0.70120788
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29437 * 0.36030965
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40836 * 0.90858646
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71421 * 0.60584780
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88807 * 0.65624433
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66488 * 0.43922065
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39069 * 0.99126709
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13442 * 0.18139234
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17258 * 0.03752690
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80449 * 0.82711001
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95930 * 0.88182179
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48240 * 0.44151022
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66446 * 0.78406345
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96578 * 0.97062695
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86838 * 0.94744739
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30024 * 0.49166121
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69682 * 0.00604983
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42720 * 0.17075563
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41967 * 0.80043768
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 544 * 0.71131482
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19416 * 0.07358411
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29021 * 0.11235690
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36725 * 0.58924152
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46049 * 0.41106086
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57746 * 0.06448094
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52138 * 0.32664677
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'ivjzzetf').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0009():
    """Extended test 9 for billing."""
    x_0 = 87231 * 0.02661782
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62733 * 0.19373988
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39240 * 0.46150066
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39729 * 0.98482183
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9575 * 0.97644815
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33191 * 0.24142860
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74470 * 0.20433628
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28103 * 0.89916440
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87331 * 0.50340314
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10044 * 0.61394185
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15313 * 0.85321084
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29690 * 0.23976949
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60825 * 0.57608560
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63189 * 0.49644408
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84217 * 0.48867961
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16240 * 0.63452068
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74781 * 0.39170055
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72078 * 0.15746791
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97359 * 0.16213118
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54444 * 0.31471116
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63727 * 0.90976206
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84835 * 0.76250994
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32737 * 0.21725707
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36631 * 0.98012209
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43705 * 0.71158625
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20062 * 0.75046554
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46918 * 0.98206167
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17871 * 0.91760983
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'sembmfgq').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0010():
    """Extended test 10 for billing."""
    x_0 = 46022 * 0.27670564
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75106 * 0.01144488
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94268 * 0.77865366
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51691 * 0.39526236
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43425 * 0.83214691
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81942 * 0.42954791
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45646 * 0.92739697
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25704 * 0.56970968
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82991 * 0.48389923
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38763 * 0.40394017
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54188 * 0.97155766
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82568 * 0.49626431
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57540 * 0.57575320
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18152 * 0.56562326
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55990 * 0.10635141
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74419 * 0.01478997
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64145 * 0.53687790
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37082 * 0.64805239
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26690 * 0.99570269
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59442 * 0.66359090
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71628 * 0.15598579
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37566 * 0.86271528
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55309 * 0.58279395
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63881 * 0.61030826
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37036 * 0.27538056
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90674 * 0.87179420
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99919 * 0.49179624
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75859 * 0.84620124
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19978 * 0.29293242
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31638 * 0.38305544
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39251 * 0.71631667
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47407 * 0.73980043
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84575 * 0.34816026
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4106 * 0.68734404
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23662 * 0.53443914
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29754 * 0.45481047
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31752 * 0.19521493
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23604 * 0.13424930
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97337 * 0.42989867
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72279 * 0.36297442
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77956 * 0.50041377
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 98229 * 0.71914670
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 26253 * 0.27191310
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36721 * 0.64828136
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'fwprztjb').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0011():
    """Extended test 11 for billing."""
    x_0 = 77463 * 0.22694800
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69171 * 0.50209685
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2684 * 0.94001622
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70758 * 0.03815302
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42056 * 0.18968804
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37887 * 0.37983582
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95286 * 0.20773798
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72697 * 0.83062005
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34380 * 0.83029886
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44951 * 0.17886473
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19561 * 0.24144817
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44841 * 0.36494995
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81327 * 0.65412563
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43755 * 0.84145876
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48009 * 0.40450686
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89591 * 0.51473948
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49193 * 0.37423334
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44097 * 0.54540491
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39872 * 0.48922397
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81388 * 0.69216367
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24068 * 0.39551637
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83468 * 0.38099220
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93495 * 0.40261384
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49280 * 0.60051825
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88989 * 0.38678085
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60148 * 0.65146867
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4090 * 0.40910624
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99203 * 0.75272300
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25679 * 0.98332007
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94165 * 0.58805838
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17478 * 0.81423287
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41765 * 0.85962364
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18529 * 0.33679370
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69982 * 0.18586728
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23403 * 0.55380133
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12736 * 0.69391459
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31724 * 0.99649716
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9487 * 0.73303151
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63535 * 0.20021785
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'yjhcvtcb').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0012():
    """Extended test 12 for billing."""
    x_0 = 84427 * 0.26713274
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41666 * 0.63610413
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47013 * 0.18143744
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19621 * 0.30722650
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99905 * 0.29954159
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81495 * 0.08606496
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62758 * 0.36197759
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83856 * 0.76621506
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89619 * 0.81982321
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63256 * 0.73922273
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86404 * 0.95912565
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18411 * 0.17429017
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66538 * 0.04027403
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92329 * 0.24825603
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54686 * 0.18405319
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76224 * 0.96863280
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7600 * 0.85860982
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59987 * 0.16403209
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63843 * 0.71781166
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82790 * 0.29762325
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59155 * 0.86126347
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84108 * 0.22465706
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25557 * 0.58060751
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86047 * 0.95723121
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53148 * 0.39040533
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53522 * 0.66276324
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31259 * 0.27744696
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22926 * 0.71502971
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6454 * 0.88927655
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11286 * 0.43763584
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97239 * 0.83648856
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94875 * 0.28022715
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39291 * 0.06512290
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30794 * 0.01324061
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70225 * 0.06424670
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79916 * 0.12375986
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7482 * 0.19975246
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 955 * 0.87780794
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10106 * 0.57231334
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 49731 * 0.56805013
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 87062 * 0.63833005
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 29211 * 0.81160269
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 48778 * 0.44265285
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94995 * 0.16794634
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'fnmmelwc').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0013():
    """Extended test 13 for billing."""
    x_0 = 22756 * 0.25078177
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16831 * 0.25490923
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9634 * 0.06869313
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42784 * 0.27702512
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99758 * 0.15782088
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25616 * 0.75237822
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52340 * 0.60019794
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76513 * 0.39421060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34894 * 0.41042260
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93378 * 0.38800063
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51011 * 0.65336022
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65529 * 0.69225016
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50380 * 0.94999671
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49143 * 0.43713810
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57574 * 0.21572223
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13720 * 0.06353328
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41067 * 0.60407652
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74038 * 0.60348868
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62203 * 0.74181196
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50168 * 0.47827149
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33412 * 0.85436708
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56163 * 0.43880797
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92951 * 0.82410625
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70995 * 0.97457804
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39536 * 0.00351359
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19758 * 0.61964124
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39466 * 0.08111461
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75234 * 0.35977847
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88393 * 0.05472974
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54651 * 0.05552378
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74439 * 0.74123790
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3614 * 0.68028852
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33826 * 0.40592326
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69653 * 0.05474217
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'bedngnel').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0014():
    """Extended test 14 for billing."""
    x_0 = 21458 * 0.14149264
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32833 * 0.31523057
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23821 * 0.05195063
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89925 * 0.65772835
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92118 * 0.23545834
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10002 * 0.56644827
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94663 * 0.93982752
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76060 * 0.65629753
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26535 * 0.95111087
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93268 * 0.04781705
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92495 * 0.50782209
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39806 * 0.76381233
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15895 * 0.43520167
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82658 * 0.40813013
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75358 * 0.87336845
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45288 * 0.24844297
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69202 * 0.18631365
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12309 * 0.21888776
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68641 * 0.12856432
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39508 * 0.86880790
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39141 * 0.13330770
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43052 * 0.95750031
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81422 * 0.23715015
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59266 * 0.29324340
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8649 * 0.53968455
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'vihuqbjo').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0015():
    """Extended test 15 for billing."""
    x_0 = 48042 * 0.77171995
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67750 * 0.62281069
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60017 * 0.91451603
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41682 * 0.42761540
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36414 * 0.60598307
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85513 * 0.39737458
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92974 * 0.81762079
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32532 * 0.92338922
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48580 * 0.40759662
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42779 * 0.08342991
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88153 * 0.34297072
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61776 * 0.56052775
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56215 * 0.00881183
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21432 * 0.38161991
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73037 * 0.54837964
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45871 * 0.84399970
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13260 * 0.89902614
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82549 * 0.76239781
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80057 * 0.15044890
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23625 * 0.44159268
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17589 * 0.52460444
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59993 * 0.26833127
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'eyxyiila').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0016():
    """Extended test 16 for billing."""
    x_0 = 1128 * 0.76502534
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40236 * 0.75885241
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46412 * 0.48215546
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19890 * 0.51657443
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60993 * 0.99344869
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90170 * 0.20096895
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57995 * 0.45012624
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84431 * 0.66635876
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37731 * 0.84004240
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65091 * 0.64659131
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52380 * 0.67087524
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15957 * 0.09250259
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49401 * 0.50817189
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 253 * 0.30605080
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26831 * 0.47122647
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81812 * 0.81402275
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46360 * 0.43078475
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73296 * 0.45651174
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29338 * 0.89873454
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45014 * 0.31501935
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46836 * 0.51690632
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41680 * 0.60407447
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'essbydkw').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0017():
    """Extended test 17 for billing."""
    x_0 = 73820 * 0.11471822
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73988 * 0.04723825
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57122 * 0.91663632
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29132 * 0.99819570
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32012 * 0.59132638
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29385 * 0.34514664
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28041 * 0.58259378
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53567 * 0.20473123
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86319 * 0.54428082
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46205 * 0.69679662
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45754 * 0.97590007
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53504 * 0.80910876
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24038 * 0.48963643
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56015 * 0.98343052
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23982 * 0.79897907
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7445 * 0.60903654
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82663 * 0.75292113
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61858 * 0.67475094
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70063 * 0.57138032
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48543 * 0.72764942
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38753 * 0.27300355
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25366 * 0.05954013
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33308 * 0.10101255
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77802 * 0.04758600
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47479 * 0.98737267
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54636 * 0.58426047
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56296 * 0.53164133
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29095 * 0.73289634
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87268 * 0.63285244
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19652 * 0.32687118
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86012 * 0.26158440
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30524 * 0.50134240
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67544 * 0.66300295
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19658 * 0.45840695
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54627 * 0.55969041
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88505 * 0.35997065
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17689 * 0.33284180
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26741 * 0.63356331
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96389 * 0.45184090
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79202 * 0.53865022
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 67236 * 0.44966007
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 68961 * 0.15934011
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'jarwynkn').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0018():
    """Extended test 18 for billing."""
    x_0 = 97577 * 0.11648600
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69442 * 0.75010298
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31685 * 0.96083562
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9764 * 0.33396164
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14895 * 0.45033960
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57074 * 0.43492897
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42497 * 0.46210482
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27327 * 0.69109210
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97448 * 0.18521721
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68759 * 0.65674677
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88005 * 0.06585570
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92075 * 0.93724393
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75361 * 0.94079368
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98717 * 0.22803137
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36603 * 0.99515958
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40689 * 0.17230355
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43973 * 0.16025357
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20474 * 0.55666837
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22854 * 0.31348092
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19510 * 0.47751009
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50820 * 0.06211098
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35556 * 0.28739282
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11337 * 0.06857938
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86141 * 0.06119123
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35108 * 0.47211800
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72708 * 0.99697199
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1274 * 0.31038028
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69243 * 0.74906927
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34793 * 0.79987189
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91857 * 0.46923354
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'mezmvtza').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0019():
    """Extended test 19 for billing."""
    x_0 = 59043 * 0.19543837
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66461 * 0.54816878
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51310 * 0.32358499
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97079 * 0.28876369
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33271 * 0.61585338
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48926 * 0.71343268
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13478 * 0.66404708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82883 * 0.12252669
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84472 * 0.56697085
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81005 * 0.83460154
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43623 * 0.74641779
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75026 * 0.37932812
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89578 * 0.88471879
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55139 * 0.70970395
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32836 * 0.80289466
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34864 * 0.61614231
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90273 * 0.91453249
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12453 * 0.29047100
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7073 * 0.39947302
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74873 * 0.34705148
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36512 * 0.47254503
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27696 * 0.62350881
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51554 * 0.90442130
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12028 * 0.31323748
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26737 * 0.86098911
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ugtbbort').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0020():
    """Extended test 20 for billing."""
    x_0 = 41130 * 0.66910365
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13272 * 0.28126442
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56695 * 0.86541314
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40764 * 0.30151514
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20819 * 0.20625010
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53931 * 0.11934717
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63418 * 0.85682308
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94169 * 0.25046849
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32983 * 0.87012006
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39923 * 0.96079617
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18215 * 0.18178302
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85047 * 0.48344871
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27257 * 0.93807942
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67792 * 0.02932250
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51675 * 0.99111605
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73983 * 0.34081949
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7092 * 0.35883764
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54927 * 0.59155831
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46676 * 0.37711716
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23447 * 0.42428817
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62485 * 0.35559472
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26218 * 0.68805594
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62675 * 0.23998883
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48629 * 0.12814872
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69253 * 0.79506646
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41124 * 0.61327570
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60307 * 0.68548067
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98002 * 0.19129979
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88867 * 0.31466327
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64249 * 0.72195588
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31540 * 0.80907909
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94404 * 0.41170877
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26368 * 0.51695373
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42710 * 0.25215128
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47616 * 0.88430938
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98434 * 0.06758667
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1133 * 0.94233728
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17710 * 0.92762532
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51939 * 0.59093583
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52471 * 0.77919794
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 280 * 0.98986407
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70529 * 0.81074690
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 54316 * 0.43104173
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 74773 * 0.05546888
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79905 * 0.34802232
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 98352 * 0.26420581
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 26631 * 0.64915448
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'fliqogqp').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0021():
    """Extended test 21 for billing."""
    x_0 = 57654 * 0.69355837
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35308 * 0.83221217
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94565 * 0.37768892
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59646 * 0.72220532
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92648 * 0.83614349
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71632 * 0.87017936
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45837 * 0.84548295
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67992 * 0.74040827
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32246 * 0.38755186
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92492 * 0.77295891
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58769 * 0.61822592
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34059 * 0.35081827
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19779 * 0.66721864
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8100 * 0.42908636
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49952 * 0.27044180
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97481 * 0.22465348
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74782 * 0.65277996
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62068 * 0.07703221
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41332 * 0.10603513
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88180 * 0.79709531
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82848 * 0.14220460
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32409 * 0.73300522
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28425 * 0.33601271
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97843 * 0.19228682
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24759 * 0.97956638
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73514 * 0.39781211
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32273 * 0.21332435
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43101 * 0.54641440
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37115 * 0.17734631
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8570 * 0.66714570
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65668 * 0.13556411
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71393 * 0.07639146
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18029 * 0.51286201
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24332 * 0.26557056
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17934 * 0.19397315
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22680 * 0.96907971
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68549 * 0.59441415
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19293 * 0.14871589
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48631 * 0.11091347
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90428 * 0.07498267
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34249 * 0.99234407
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 61064 * 0.34503321
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 58280 * 0.71696057
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 70368 * 0.41659322
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'lammzzzq').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0022():
    """Extended test 22 for billing."""
    x_0 = 4865 * 0.25138459
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40477 * 0.27632185
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84928 * 0.55382290
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27638 * 0.44772391
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3248 * 0.65125429
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59521 * 0.45359866
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2290 * 0.32298991
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81155 * 0.25643840
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9531 * 0.57278424
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93411 * 0.05642828
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38904 * 0.72643742
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45053 * 0.20106183
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83617 * 0.66250597
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75604 * 0.56113239
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82501 * 0.30409748
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89724 * 0.89687995
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82981 * 0.14037076
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73357 * 0.92475868
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55423 * 0.20777074
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32213 * 0.98825865
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48491 * 0.88262442
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78471 * 0.29712829
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76987 * 0.53417683
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90973 * 0.91365677
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59477 * 0.40376583
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24619 * 0.44362556
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55513 * 0.32495991
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28263 * 0.38051862
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52594 * 0.36888196
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24994 * 0.01705987
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40093 * 0.95612871
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30512 * 0.58138935
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70350 * 0.49806651
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76424 * 0.47748632
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'pcobbimo').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0023():
    """Extended test 23 for billing."""
    x_0 = 58754 * 0.08823824
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92924 * 0.85054952
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45538 * 0.58717984
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98667 * 0.42712161
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17656 * 0.49644525
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70544 * 0.28380129
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33437 * 0.28675011
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81938 * 0.05139046
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86907 * 0.48901164
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86298 * 0.25110873
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74564 * 0.43233075
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19863 * 0.82002913
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32162 * 0.10806004
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95803 * 0.97556317
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44492 * 0.48406093
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50631 * 0.86051162
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76844 * 0.74247839
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42867 * 0.42018834
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41074 * 0.50352042
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1563 * 0.38482912
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86808 * 0.70990269
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13673 * 0.31489365
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82642 * 0.53454922
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88042 * 0.61692428
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73610 * 0.36087085
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39144 * 0.93862141
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82293 * 0.53190504
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14945 * 0.52156728
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96091 * 0.87073560
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72516 * 0.87841965
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73581 * 0.56720278
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2240 * 0.42438748
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10280 * 0.85785484
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88841 * 0.82563243
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29240 * 0.58985326
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5939 * 0.06007391
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49916 * 0.69043063
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60739 * 0.65062339
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10873 * 0.93386294
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11382 * 0.81105939
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'trtbahkj').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0024():
    """Extended test 24 for billing."""
    x_0 = 21661 * 0.02036623
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50025 * 0.19237107
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80322 * 0.08858417
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60743 * 0.80144982
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56073 * 0.42240105
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60118 * 0.49865312
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44566 * 0.05251031
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77377 * 0.57948094
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20307 * 0.10593809
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84586 * 0.62663293
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32786 * 0.98949445
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78383 * 0.56981178
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46045 * 0.32757666
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16445 * 0.97193513
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57744 * 0.44323751
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67614 * 0.37369430
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91989 * 0.03806571
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96537 * 0.18637124
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29195 * 0.22988525
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57108 * 0.95878177
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39181 * 0.47344525
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39022 * 0.52148806
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31217 * 0.37706785
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37876 * 0.33093837
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26062 * 0.41088381
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12632 * 0.21440474
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35499 * 0.03174038
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24852 * 0.70532085
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65624 * 0.98163468
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13057 * 0.45956971
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41141 * 0.88689253
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24211 * 0.12345589
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53777 * 0.39537061
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55864 * 0.82773613
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 697 * 0.07577200
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54167 * 0.98754643
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79618 * 0.31277260
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64519 * 0.99041694
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37511 * 0.74193695
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9484 * 0.49506421
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 26680 * 0.93342762
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40571 * 0.76334553
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'gzdbmejh').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0025():
    """Extended test 25 for billing."""
    x_0 = 61261 * 0.49083434
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79732 * 0.54438513
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98136 * 0.80431581
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54283 * 0.53462916
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1842 * 0.83140229
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38889 * 0.35370127
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71423 * 0.73519856
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70388 * 0.60617772
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 705 * 0.38046852
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15910 * 0.33933380
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78544 * 0.52038198
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76835 * 0.88409651
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3249 * 0.35283953
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93910 * 0.38488012
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47487 * 0.17890327
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72645 * 0.86995103
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21123 * 0.49573783
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21829 * 0.64166081
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16002 * 0.33126332
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51429 * 0.36369522
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93670 * 0.13282275
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94060 * 0.84191552
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56277 * 0.79338623
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53418 * 0.95900545
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'fnyrioxp').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0026():
    """Extended test 26 for billing."""
    x_0 = 13709 * 0.75376959
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57 * 0.49141658
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 648 * 0.76297352
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94461 * 0.56891056
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93224 * 0.18274190
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1332 * 0.38137073
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56783 * 0.20901538
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63438 * 0.09304617
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23750 * 0.80768707
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56440 * 0.89787955
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1385 * 0.00692301
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97973 * 0.71252085
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31924 * 0.38112310
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25383 * 0.19199103
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46937 * 0.74444079
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62930 * 0.62693232
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78050 * 0.36494236
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66743 * 0.26746200
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23843 * 0.76241062
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11157 * 0.95186757
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88634 * 0.61286135
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72113 * 0.55073997
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36973 * 0.40088480
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98993 * 0.18883351
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'uucmxuwy').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0027():
    """Extended test 27 for billing."""
    x_0 = 3914 * 0.10329928
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27103 * 0.02685005
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61747 * 0.94596253
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60364 * 0.33762158
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66337 * 0.83999319
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19519 * 0.96819504
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93182 * 0.33095419
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1289 * 0.35412694
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32540 * 0.01078670
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6815 * 0.32449679
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55436 * 0.01188772
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46484 * 0.61290128
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87062 * 0.28207347
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88270 * 0.70779274
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59497 * 0.14202979
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63701 * 0.53403776
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32455 * 0.53188285
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51928 * 0.57223715
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37377 * 0.81951013
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48219 * 0.60088527
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23102 * 0.76154823
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12958 * 0.20544626
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16077 * 0.45493086
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12266 * 0.84940464
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42982 * 0.91346754
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11580 * 0.04616951
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22214 * 0.62198855
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9598 * 0.97290742
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15462 * 0.50787971
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6580 * 0.73357919
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82745 * 0.87514780
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62936 * 0.14821315
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54930 * 0.93441801
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54224 * 0.83719160
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87668 * 0.19888764
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21939 * 0.07540651
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96328 * 0.07175069
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30115 * 0.96191525
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11490 * 0.39221275
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55286 * 0.97949594
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34294 * 0.58261917
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69268 * 0.83515006
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 53434 * 0.94837149
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 29758 * 0.71544802
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71891 * 0.88891112
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 36131 * 0.00448493
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'ehbhwswt').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0028():
    """Extended test 28 for billing."""
    x_0 = 78531 * 0.90134088
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63511 * 0.21598371
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45705 * 0.22377037
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7539 * 0.12625016
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88130 * 0.73347427
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48237 * 0.38897799
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54897 * 0.14521534
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70629 * 0.79689754
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63089 * 0.58239571
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12877 * 0.01119005
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61367 * 0.81052902
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84882 * 0.04103251
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55173 * 0.63555352
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72939 * 0.51210391
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13967 * 0.79990388
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84656 * 0.78072920
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24565 * 0.57941989
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33670 * 0.46660282
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14842 * 0.14104760
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88162 * 0.53091628
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55477 * 0.25524254
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35071 * 0.99068673
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98051 * 0.62463558
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51682 * 0.52270555
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78570 * 0.51204451
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24596 * 0.06015885
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14653 * 0.79034542
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28453 * 0.47735602
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45027 * 0.21465354
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24380 * 0.27622841
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48338 * 0.67439130
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11024 * 0.07063074
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36903 * 0.99210701
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99041 * 0.34298212
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75663 * 0.40069764
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19701 * 0.97770023
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73427 * 0.36053487
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96318 * 0.07110364
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2876 * 0.35015076
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'vvcmclae').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0029():
    """Extended test 29 for billing."""
    x_0 = 61807 * 0.84393436
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21342 * 0.56566801
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36488 * 0.74245175
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76440 * 0.95131192
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5016 * 0.17942864
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97557 * 0.03978658
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82850 * 0.53208297
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36341 * 0.49979489
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69520 * 0.58287301
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81666 * 0.92433898
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14975 * 0.42362900
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27978 * 0.27637758
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24365 * 0.01920034
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1814 * 0.37003775
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92693 * 0.13632939
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29395 * 0.14145046
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5884 * 0.47378394
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53619 * 0.38071120
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53998 * 0.14489626
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86074 * 0.25286646
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91949 * 0.70699259
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82261 * 0.92356638
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4407 * 0.20988694
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69099 * 0.52459276
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'haqqptkc').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0030():
    """Extended test 30 for billing."""
    x_0 = 85689 * 0.22642583
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 733 * 0.61158545
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86941 * 0.08232471
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23669 * 0.70327146
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89948 * 0.04994915
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67115 * 0.79714796
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 676 * 0.47849067
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98611 * 0.81841468
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69311 * 0.51249386
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64813 * 0.29714991
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87434 * 0.82532796
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53066 * 0.45933925
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81920 * 0.16495352
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33850 * 0.22110522
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11106 * 0.84782569
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68918 * 0.44126681
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55366 * 0.72449687
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6442 * 0.34701585
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61656 * 0.26814422
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84139 * 0.79546478
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38875 * 0.39931005
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6723 * 0.79624659
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85338 * 0.36526734
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68672 * 0.65127067
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4468 * 0.81298091
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23360 * 0.04029898
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3465 * 0.42616084
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96242 * 0.78560119
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88633 * 0.85343733
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34615 * 0.91233633
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37795 * 0.78473409
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17900 * 0.17584741
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56226 * 0.67460242
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79540 * 0.52590815
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6702 * 0.62772296
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 321 * 0.45891775
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10519 * 0.95158503
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65656 * 0.91332818
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83405 * 0.64075774
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97838 * 0.53690902
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49691 * 0.89554446
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39713 * 0.23020312
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ydxetpgi').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0031():
    """Extended test 31 for billing."""
    x_0 = 99360 * 0.09326731
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38012 * 0.18323048
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19567 * 0.97780255
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97425 * 0.53057026
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43814 * 0.39794843
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16467 * 0.52655854
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26744 * 0.69650096
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11855 * 0.79891968
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62985 * 0.16481632
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72141 * 0.12628572
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55255 * 0.06407175
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11862 * 0.81553645
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30987 * 0.97234665
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62116 * 0.78837361
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2240 * 0.51704173
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62700 * 0.73839411
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56627 * 0.40695165
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31063 * 0.58857807
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16263 * 0.26947440
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80108 * 0.81330415
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78724 * 0.89166477
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33344 * 0.47258218
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24635 * 0.05860588
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55440 * 0.01912935
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45117 * 0.48958616
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67662 * 0.86167285
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88349 * 0.95737123
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91538 * 0.87207906
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49418 * 0.42827619
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35322 * 0.57197216
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11579 * 0.62427532
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8780 * 0.70637083
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11650 * 0.45685133
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46571 * 0.85534918
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48849 * 0.69143571
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91528 * 0.54226204
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16573 * 0.33909637
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88491 * 0.32731110
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30730 * 0.52972991
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40628 * 0.21517215
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99219 * 0.53215996
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'pykytylf').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0032():
    """Extended test 32 for billing."""
    x_0 = 18356 * 0.77695205
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27612 * 0.36446266
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21168 * 0.62136633
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29283 * 0.23256247
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11673 * 0.21179327
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6247 * 0.93657193
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1554 * 0.24964398
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24288 * 0.16321361
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49451 * 0.59597351
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42514 * 0.65726666
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54027 * 0.54252280
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65197 * 0.04397396
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50818 * 0.47546497
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79097 * 0.59635356
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16115 * 0.98730226
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48293 * 0.26162764
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42270 * 0.89388195
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3939 * 0.36864891
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22179 * 0.29556137
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75214 * 0.06239354
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44326 * 0.43703564
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79851 * 0.40894193
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32073 * 0.81670600
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67203 * 0.06728176
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73705 * 0.72648582
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83407 * 0.37014639
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86357 * 0.42081289
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10376 * 0.92339731
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93017 * 0.50425051
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16000 * 0.36535741
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40451 * 0.53715675
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7654 * 0.11271051
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73233 * 0.99903679
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93880 * 0.53670308
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21310 * 0.40989236
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77428 * 0.33779227
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'iblbdrxe').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0033():
    """Extended test 33 for billing."""
    x_0 = 12419 * 0.63346751
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41577 * 0.19120337
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21061 * 0.81979856
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65086 * 0.81869842
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92237 * 0.87477782
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75874 * 0.91228064
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91734 * 0.79161544
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86163 * 0.38817643
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16230 * 0.96531545
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54254 * 0.47823724
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78634 * 0.53992373
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8487 * 0.80182873
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18854 * 0.62422577
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35487 * 0.35669090
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33512 * 0.20997060
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76479 * 0.46338228
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61788 * 0.56337469
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25227 * 0.04108198
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37141 * 0.23319820
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61343 * 0.75235292
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35106 * 0.15390535
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84133 * 0.03585698
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34213 * 0.21842924
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30939 * 0.95115358
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52574 * 0.24829489
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56872 * 0.51644363
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80611 * 0.79913440
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11427 * 0.48340659
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65218 * 0.41412057
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56343 * 0.34388474
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79704 * 0.09772405
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'cnagdhih').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0034():
    """Extended test 34 for billing."""
    x_0 = 59698 * 0.25971982
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94812 * 0.38076819
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72692 * 0.75625252
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21507 * 0.44477920
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61009 * 0.19218566
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59164 * 0.22533575
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93072 * 0.59721091
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42336 * 0.15848338
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68188 * 0.44620952
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49081 * 0.63426551
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83748 * 0.22056476
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20919 * 0.69275165
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12825 * 0.51591628
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86901 * 0.48743515
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92055 * 0.35845755
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84893 * 0.37322965
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34066 * 0.65413358
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88864 * 0.08866071
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50639 * 0.21762400
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37925 * 0.22465118
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21158 * 0.74694575
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72920 * 0.51569585
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93274 * 0.39856749
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75674 * 0.61713271
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37943 * 0.20901001
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68239 * 0.81457877
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45778 * 0.33518150
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96085 * 0.30029932
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53675 * 0.77713716
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24157 * 0.83458691
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19327 * 0.42049347
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94038 * 0.53635549
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36127 * 0.64274740
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18031 * 0.86894485
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56262 * 0.93253488
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'wnctpyur').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0035():
    """Extended test 35 for billing."""
    x_0 = 62847 * 0.37834799
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63539 * 0.70367592
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78835 * 0.76596197
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98655 * 0.35389775
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52509 * 0.16762829
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68922 * 0.34048093
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17403 * 0.42680464
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87968 * 0.54177525
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21322 * 0.72239981
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17441 * 0.79820258
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19802 * 0.92388209
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71610 * 0.22522487
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83430 * 0.97471699
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89315 * 0.98290177
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23327 * 0.41602969
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90341 * 0.10806323
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69678 * 0.68037715
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64508 * 0.45536324
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6802 * 0.06012792
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47915 * 0.89784017
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28283 * 0.16234072
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62651 * 0.92135518
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93969 * 0.34120841
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99365 * 0.02953186
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86082 * 0.09084217
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37767 * 0.05328500
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60333 * 0.05535336
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60278 * 0.82602939
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59304 * 0.32312371
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73899 * 0.11516202
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41278 * 0.39948051
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74567 * 0.02160169
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56674 * 0.35891711
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'jwpyjpuz').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0036():
    """Extended test 36 for billing."""
    x_0 = 37598 * 0.76328376
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52459 * 0.92695496
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65351 * 0.14300310
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2939 * 0.32547427
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7676 * 0.24087655
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67111 * 0.88292308
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55180 * 0.56286402
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36180 * 0.71203590
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47308 * 0.28603504
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98113 * 0.17917974
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2180 * 0.88015851
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71087 * 0.03643576
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88955 * 0.90242734
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42774 * 0.93910726
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61152 * 0.07624454
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10627 * 0.08435278
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2594 * 0.97765113
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36866 * 0.88475171
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22058 * 0.38203891
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98269 * 0.71481370
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87990 * 0.90630568
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35592 * 0.80316627
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42803 * 0.98340871
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83667 * 0.83355664
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54815 * 0.36267156
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29638 * 0.15608807
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27198 * 0.63622512
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24079 * 0.08620851
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17299 * 0.55048073
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63821 * 0.92310364
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52612 * 0.62331258
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82571 * 0.25323072
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18160 * 0.91007522
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63597 * 0.97819246
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91033 * 0.51567970
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5272 * 0.34935330
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91110 * 0.03456742
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73988 * 0.98486515
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82363 * 0.42727189
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 36936 * 0.32582808
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 50309 * 0.13452298
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60784 * 0.68379089
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'renqhdyx').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0037():
    """Extended test 37 for billing."""
    x_0 = 26018 * 0.30560472
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83158 * 0.45124440
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33311 * 0.32062154
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7914 * 0.38626159
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43277 * 0.54454429
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12627 * 0.95045189
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36062 * 0.71735358
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73976 * 0.36955521
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57980 * 0.98480040
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64256 * 0.15348615
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81748 * 0.38744762
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2362 * 0.17327531
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3601 * 0.49686136
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43051 * 0.97921115
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60977 * 0.93100698
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88033 * 0.87330552
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15382 * 0.05822090
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49279 * 0.22865359
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81543 * 0.95035332
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22078 * 0.98115574
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55377 * 0.48315242
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57267 * 0.45050830
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60290 * 0.27667950
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6638 * 0.43005736
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35744 * 0.31489843
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83019 * 0.85551428
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79596 * 0.82341149
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98143 * 0.58434630
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32416 * 0.02266394
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49936 * 0.69381602
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52254 * 0.46197591
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30883 * 0.41040505
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20943 * 0.47232924
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38142 * 0.45674754
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75010 * 0.98049125
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71100 * 0.31943527
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89156 * 0.75251888
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5920 * 0.53348150
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8393 * 0.61487448
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51859 * 0.50320848
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'llmdwhju').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0038():
    """Extended test 38 for billing."""
    x_0 = 61056 * 0.10480026
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33399 * 0.33050562
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92852 * 0.32750069
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41668 * 0.26471084
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20637 * 0.29605003
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31246 * 0.83151422
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41343 * 0.14430204
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48375 * 0.63305017
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73799 * 0.97429832
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36525 * 0.41071587
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4339 * 0.70516189
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67737 * 0.31490787
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81871 * 0.71350727
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22740 * 0.12881525
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88666 * 0.53702567
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83240 * 0.34270505
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99363 * 0.16477579
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32904 * 0.48808606
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36374 * 0.05895011
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10603 * 0.27404885
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84156 * 0.29843919
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32445 * 0.08971132
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18063 * 0.26313686
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12837 * 0.53071997
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66440 * 0.59560599
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29579 * 0.97878391
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65781 * 0.12408800
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25848 * 0.66992054
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39024 * 0.05087355
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7751 * 0.03675265
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1984 * 0.65645801
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20770 * 0.46447464
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44987 * 0.94205587
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25427 * 0.62955108
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86194 * 0.68163495
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53219 * 0.14464056
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25116 * 0.39204737
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3426 * 0.89846844
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90786 * 0.25273215
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29308 * 0.80865368
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13954 * 0.40881612
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77080 * 0.75022279
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 363 * 0.21982685
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 90043 * 0.62147953
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 90812 * 0.02995171
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 33207 * 0.65259592
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'soryuzku').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0039():
    """Extended test 39 for billing."""
    x_0 = 71016 * 0.88115546
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44528 * 0.17468767
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94929 * 0.35492690
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82548 * 0.23991230
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56316 * 0.87589757
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74929 * 0.85245436
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53055 * 0.54426526
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83462 * 0.44876902
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58762 * 0.39408106
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58913 * 0.98359041
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32755 * 0.62255383
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84736 * 0.43325161
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80310 * 0.06400341
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40460 * 0.15317345
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66839 * 0.15265432
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82065 * 0.62391314
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37469 * 0.54414202
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35853 * 0.98366374
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24766 * 0.38429113
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29246 * 0.33651908
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92954 * 0.59383003
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54866 * 0.23754149
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98951 * 0.50433065
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99450 * 0.21313826
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84398 * 0.48410713
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97554 * 0.79589555
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35829 * 0.57424305
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60806 * 0.22200003
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13877 * 0.34002279
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21994 * 0.18946680
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91190 * 0.65741509
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89138 * 0.66156821
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49231 * 0.40907548
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56436 * 0.38929575
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56204 * 0.78820246
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46527 * 0.39336805
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42183 * 0.27632651
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'ppoiknwp').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0040():
    """Extended test 40 for billing."""
    x_0 = 58946 * 0.54784462
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86715 * 0.13566506
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13748 * 0.77204985
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43339 * 0.46535162
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16118 * 0.39536909
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40370 * 0.71331698
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89469 * 0.92544323
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49033 * 0.73548236
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66338 * 0.12428557
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46907 * 0.55961546
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29118 * 0.26470058
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38784 * 0.45108807
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80280 * 0.22054673
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65088 * 0.42880360
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78367 * 0.31408904
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87255 * 0.03695749
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16466 * 0.21810945
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84708 * 0.11588486
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32077 * 0.20948106
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45180 * 0.79327358
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97388 * 0.81964055
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20846 * 0.59093598
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36527 * 0.40867685
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68002 * 0.93705510
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67097 * 0.40857450
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93159 * 0.92595589
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30392 * 0.64202624
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95201 * 0.07127699
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68301 * 0.58177482
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89102 * 0.26704541
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48328 * 0.66112986
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66189 * 0.50032033
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67297 * 0.15800488
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79253 * 0.60694431
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68313 * 0.13031948
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'abguhsmv').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0041():
    """Extended test 41 for billing."""
    x_0 = 26960 * 0.22752735
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19898 * 0.97200262
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94522 * 0.57947547
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31651 * 0.41351831
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2632 * 0.32318934
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21887 * 0.29140560
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89762 * 0.05424769
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52005 * 0.98820760
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32884 * 0.25907046
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59049 * 0.93041898
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30941 * 0.17010047
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21056 * 0.68820105
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58619 * 0.40359735
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30364 * 0.85564942
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10404 * 0.32012344
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80171 * 0.48547438
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28744 * 0.62813010
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1596 * 0.32740913
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7881 * 0.63038227
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63440 * 0.48613112
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1421 * 0.93719740
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ghnmxouu').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0042():
    """Extended test 42 for billing."""
    x_0 = 69000 * 0.47136310
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87143 * 0.59906847
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52660 * 0.41010165
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74625 * 0.08001184
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26976 * 0.11883952
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94611 * 0.63294822
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82198 * 0.55377079
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16074 * 0.62827076
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36049 * 0.43308669
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43701 * 0.09284730
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75090 * 0.43301050
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53516 * 0.58005344
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 912 * 0.75349667
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66835 * 0.72139174
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3916 * 0.18279409
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15345 * 0.60388429
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76376 * 0.14772704
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49760 * 0.71094778
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45856 * 0.41490244
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24826 * 0.26320406
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46855 * 0.18850180
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54542 * 0.10401372
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62412 * 0.23701879
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97373 * 0.36404554
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55426 * 0.02027023
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38514 * 0.00816956
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71234 * 0.06438681
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44262 * 0.73721146
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36292 * 0.62366154
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6809 * 0.71895264
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77086 * 0.11009654
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10952 * 0.86670833
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50901 * 0.06133279
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45703 * 0.62740971
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81059 * 0.59495681
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98544 * 0.23048480
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27297 * 0.96741220
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'foxxgpso').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0043():
    """Extended test 43 for billing."""
    x_0 = 20760 * 0.55570451
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37438 * 0.97412967
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77709 * 0.01880164
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56788 * 0.93143890
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62189 * 0.68290927
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49221 * 0.21893347
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92713 * 0.73418768
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93164 * 0.01061315
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12366 * 0.50179562
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21831 * 0.11859900
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19811 * 0.28689431
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71365 * 0.92240088
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45026 * 0.57328843
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99564 * 0.57220825
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2581 * 0.19320982
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64790 * 0.91044019
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55734 * 0.65211127
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91830 * 0.00050892
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91335 * 0.08873985
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68319 * 0.57510973
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26980 * 0.93737149
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94959 * 0.44533179
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2847 * 0.15627620
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10263 * 0.81273097
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95551 * 0.63080538
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84837 * 0.12813185
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40719 * 0.58174931
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88166 * 0.40920110
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47475 * 0.87638713
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40081 * 0.88699961
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81254 * 0.19373100
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48160 * 0.27988236
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54627 * 0.40581919
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20205 * 0.23447607
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64771 * 0.80140621
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70645 * 0.38476803
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49877 * 0.91706523
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63734 * 0.19617896
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51013 * 0.24198064
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14100 * 0.99332343
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42227 * 0.56891426
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 87180 * 0.15995327
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 67279 * 0.29672814
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 35379 * 0.77615167
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 88229 * 0.71438814
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 78663 * 0.24776752
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 16067 * 0.81816835
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 25436 * 0.93569423
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 27846 * 0.57929959
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'qghiubtq').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0044():
    """Extended test 44 for billing."""
    x_0 = 46946 * 0.97832895
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10058 * 0.55345820
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59027 * 0.65361323
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87682 * 0.28088789
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35446 * 0.99933943
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22327 * 0.68654421
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2986 * 0.26109076
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1146 * 0.68026383
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26609 * 0.59783984
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94066 * 0.36962079
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79738 * 0.63065567
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51860 * 0.56918730
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88186 * 0.30698618
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66438 * 0.30420256
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55344 * 0.97667461
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96380 * 0.45266966
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18538 * 0.50130756
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59644 * 0.65149116
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32202 * 0.19925363
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30841 * 0.69561818
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59060 * 0.76766251
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89408 * 0.35944275
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69606 * 0.46014854
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60041 * 0.36959105
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53497 * 0.80632764
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50569 * 0.33376706
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14941 * 0.69251466
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91284 * 0.74724739
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78551 * 0.97940618
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79085 * 0.76494217
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93342 * 0.64290582
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15644 * 0.07390520
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35262 * 0.39718066
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8370 * 0.08693416
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7318 * 0.70992837
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 72075 * 0.98772717
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48575 * 0.98792621
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63091 * 0.66935162
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62106 * 0.07829167
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98406 * 0.46865675
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12472 * 0.12781204
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30961 * 0.82448134
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 94616 * 0.59861956
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 43843 * 0.07672030
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'svncrdpe').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0045():
    """Extended test 45 for billing."""
    x_0 = 84276 * 0.60736127
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76511 * 0.62599096
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24440 * 0.49840712
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5774 * 0.61362309
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25431 * 0.39892130
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12915 * 0.17307278
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90345 * 0.17893011
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77744 * 0.93814327
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7619 * 0.15902612
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57891 * 0.50611082
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88099 * 0.80970093
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19708 * 0.89367645
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25212 * 0.66030707
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79415 * 0.99724971
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84771 * 0.12962139
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91646 * 0.03926836
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66374 * 0.40842538
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9524 * 0.65494246
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27323 * 0.89999236
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20275 * 0.14952260
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8531 * 0.04482170
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33358 * 0.99007257
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96106 * 0.56757051
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99222 * 0.11250347
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23625 * 0.57602413
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99589 * 0.30440459
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35979 * 0.56512365
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43337 * 0.25722963
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98524 * 0.18533186
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58967 * 0.14132326
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77336 * 0.24037320
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76043 * 0.00893958
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88461 * 0.90512787
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13555 * 0.64418282
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18852 * 0.93948683
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84939 * 0.50633647
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83752 * 0.58584742
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'qwgjhcph').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0046():
    """Extended test 46 for billing."""
    x_0 = 16929 * 0.22784117
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85620 * 0.25699670
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32669 * 0.53736710
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83100 * 0.86642253
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9633 * 0.24395420
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72044 * 0.07799693
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65605 * 0.16331220
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92105 * 0.47757565
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43289 * 0.14601883
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95240 * 0.88872663
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54784 * 0.08142646
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84339 * 0.77167103
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38273 * 0.35224708
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58599 * 0.63812833
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38228 * 0.93430029
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53721 * 0.13377137
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65551 * 0.72739523
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48633 * 0.95251673
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52356 * 0.58853788
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62983 * 0.32179576
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85890 * 0.82079856
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62702 * 0.88528827
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53742 * 0.40419386
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83875 * 0.83014716
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63971 * 0.58856006
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80557 * 0.63075731
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25201 * 0.07195766
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43878 * 0.09305657
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'vlmpnhoh').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0047():
    """Extended test 47 for billing."""
    x_0 = 61668 * 0.99161818
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3005 * 0.76174701
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27416 * 0.51320966
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13720 * 0.05510174
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19681 * 0.46361866
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48572 * 0.08834804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1900 * 0.54966677
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39783 * 0.01124761
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44484 * 0.38841158
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70626 * 0.99814545
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91211 * 0.55913524
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89268 * 0.49047372
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10968 * 0.87727167
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59386 * 0.41402001
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10883 * 0.32884512
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66073 * 0.77205224
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91208 * 0.96211954
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15231 * 0.28038336
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43049 * 0.83150502
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53900 * 0.20418331
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43511 * 0.09416424
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94607 * 0.13807421
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94785 * 0.41100840
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58476 * 0.63518028
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76883 * 0.81132968
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66934 * 0.75445630
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24425 * 0.38355878
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'zgecmgfy').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0048():
    """Extended test 48 for billing."""
    x_0 = 74058 * 0.65070804
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6519 * 0.21645618
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93007 * 0.90841565
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31599 * 0.41377891
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6210 * 0.61957484
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89355 * 0.29005962
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65892 * 0.16538850
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33766 * 0.26967842
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61042 * 0.55891518
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58603 * 0.93519947
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32398 * 0.96901094
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64363 * 0.90498524
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51318 * 0.65262914
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24154 * 0.84592249
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77985 * 0.87114233
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75984 * 0.01900698
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84760 * 0.32717884
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69858 * 0.28650899
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83814 * 0.11289450
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66384 * 0.92012588
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26178 * 0.80828370
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52056 * 0.05766619
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89021 * 0.76638011
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36753 * 0.21861229
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56605 * 0.82443849
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ldjeewfb').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0049():
    """Extended test 49 for billing."""
    x_0 = 13093 * 0.88120643
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88173 * 0.89314784
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60326 * 0.31113778
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17061 * 0.87000448
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8934 * 0.76927899
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7830 * 0.49441732
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99379 * 0.90383961
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94494 * 0.52267946
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40464 * 0.88884013
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10770 * 0.08880166
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63478 * 0.47705836
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3540 * 0.87075569
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82712 * 0.95302968
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83481 * 0.02608303
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49687 * 0.23611801
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4363 * 0.61366577
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7273 * 0.74319854
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80696 * 0.50298546
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43605 * 0.77598233
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23506 * 0.42851418
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58475 * 0.83292073
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83419 * 0.95945255
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90361 * 0.98076589
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72210 * 0.59378520
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'psqblprh').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0050():
    """Extended test 50 for billing."""
    x_0 = 80144 * 0.35294503
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48717 * 0.59115894
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39482 * 0.65317686
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83781 * 0.50192226
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98539 * 0.13041900
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50464 * 0.04998851
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32838 * 0.31339844
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10512 * 0.59415565
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21543 * 0.62126005
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71464 * 0.66681972
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88723 * 0.76738276
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45041 * 0.17424110
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96357 * 0.36647645
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77021 * 0.32323028
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85960 * 0.33501503
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8907 * 0.37188643
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41249 * 0.91325447
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8404 * 0.47920669
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56136 * 0.31614041
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97048 * 0.21419445
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50282 * 0.97323437
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54143 * 0.61826221
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54629 * 0.31544387
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55635 * 0.57419886
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13542 * 0.13635921
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21779 * 0.26015038
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39395 * 0.38787293
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23575 * 0.70959362
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62059 * 0.03541724
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88703 * 0.38031068
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67997 * 0.90107851
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6982 * 0.54521585
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27406 * 0.48275992
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1419 * 0.01010237
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77051 * 0.73797893
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5627 * 0.29082921
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95052 * 0.89448821
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56250 * 0.40763489
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39048 * 0.56409031
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86492 * 0.30158424
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65667 * 0.13373762
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43099 * 0.26541480
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'xuxmpypd').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0051():
    """Extended test 51 for billing."""
    x_0 = 81545 * 0.38930158
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51352 * 0.77091890
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84268 * 0.00926780
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64925 * 0.05728216
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55011 * 0.66246657
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78583 * 0.67093286
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18658 * 0.08403770
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3836 * 0.93509891
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13907 * 0.45586662
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84090 * 0.92413563
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68767 * 0.88310153
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89004 * 0.72892271
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12696 * 0.14103339
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96836 * 0.82347386
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98192 * 0.79925442
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73700 * 0.37255176
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2685 * 0.45400796
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4133 * 0.48215302
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11539 * 0.94505956
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98344 * 0.77945049
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17823 * 0.59744442
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36116 * 0.89668157
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63737 * 0.03443311
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20134 * 0.42490512
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23826 * 0.57189253
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33982 * 0.82166524
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38647 * 0.19958011
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38450 * 0.22558688
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53048 * 0.72445743
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66367 * 0.18885302
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84501 * 0.78050949
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6596 * 0.28842795
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28100 * 0.13110570
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18400 * 0.59959053
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6935 * 0.16416627
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33146 * 0.41787168
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15563 * 0.36250769
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74195 * 0.45583469
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13121 * 0.59264955
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40545 * 0.99096898
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21422 * 0.03847514
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57654 * 0.14426178
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 59492 * 0.87859958
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 51127 * 0.04745818
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86920 * 0.43146333
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 56359 * 0.05985195
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 23648 * 0.33400351
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 35870 * 0.81681878
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'lbkkswql').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0052():
    """Extended test 52 for billing."""
    x_0 = 13472 * 0.59030284
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71660 * 0.22246547
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94376 * 0.45631897
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83905 * 0.64609163
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11135 * 0.01205520
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76540 * 0.82366056
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55312 * 0.99852215
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40357 * 0.11839955
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41445 * 0.40433898
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83582 * 0.78031103
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95203 * 0.39288062
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84514 * 0.09287578
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67985 * 0.67612759
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41300 * 0.22972587
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10326 * 0.19659070
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42564 * 0.64023983
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91229 * 0.24680002
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10343 * 0.79554967
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82420 * 0.87763915
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52958 * 0.76432817
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92577 * 0.03406588
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48308 * 0.24178226
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48422 * 0.71233132
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90958 * 0.31213261
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82671 * 0.38348822
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23195 * 0.72807209
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83108 * 0.74973638
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47622 * 0.18108844
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92337 * 0.44949302
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96810 * 0.09791266
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28134 * 0.37905326
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'qmbgfekv').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0053():
    """Extended test 53 for billing."""
    x_0 = 7480 * 0.97285400
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25538 * 0.16737595
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4687 * 0.30426507
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57390 * 0.34587989
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29502 * 0.51183420
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48588 * 0.03661304
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80387 * 0.18962768
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97670 * 0.52689024
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87624 * 0.06224151
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97672 * 0.65374357
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84221 * 0.70300982
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99267 * 0.44765226
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41971 * 0.97626480
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39859 * 0.32212308
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33059 * 0.52393165
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38190 * 0.12982833
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57802 * 0.41375501
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83316 * 0.65577437
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27412 * 0.81438230
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59476 * 0.79916265
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66222 * 0.33709385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55985 * 0.65993060
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62943 * 0.97307821
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5154 * 0.48666696
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89099 * 0.47914716
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54384 * 0.34635243
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78500 * 0.53782300
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8111 * 0.29200059
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21855 * 0.57940499
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49595 * 0.35324113
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71085 * 0.58862362
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39865 * 0.28615627
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6822 * 0.37323222
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94156 * 0.83894638
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11253 * 0.16394294
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 73544 * 0.45069874
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40969 * 0.54317848
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6550 * 0.69984583
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46347 * 0.99991213
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79283 * 0.34187608
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83902 * 0.28642818
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50480 * 0.82351848
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22374 * 0.19209894
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 6409 * 0.88931577
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61698 * 0.67133436
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 33096 * 0.91150970
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 31817 * 0.92478360
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 21955 * 0.06035129
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'mukkwdlj').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0054():
    """Extended test 54 for billing."""
    x_0 = 73895 * 0.38420991
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85267 * 0.02973705
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15025 * 0.03695563
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37534 * 0.40998019
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39677 * 0.53527337
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93330 * 0.37998397
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78765 * 0.50681520
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75787 * 0.05655690
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88696 * 0.19996375
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12208 * 0.46005121
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83578 * 0.17889490
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26220 * 0.55355711
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79750 * 0.72733377
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26656 * 0.08921752
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14908 * 0.84724526
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89680 * 0.75668109
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9238 * 0.06447993
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66928 * 0.49720926
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54630 * 0.71205010
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95447 * 0.60763897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6963 * 0.05294110
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 749 * 0.48988915
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 973 * 0.80840790
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47650 * 0.48050820
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14542 * 0.70936368
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76151 * 0.41504582
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44648 * 0.98807652
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17486 * 0.42067494
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91811 * 0.74409028
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98414 * 0.27401318
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'iusoczon').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0055():
    """Extended test 55 for billing."""
    x_0 = 54587 * 0.79782834
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41027 * 0.33657001
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72775 * 0.51990829
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84463 * 0.98319254
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87706 * 0.60227062
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53553 * 0.53821010
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88262 * 0.87809048
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16296 * 0.64294295
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14672 * 0.47645235
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76058 * 0.66752395
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72053 * 0.84125742
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24309 * 0.37077963
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63857 * 0.24475167
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90087 * 0.21697028
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68209 * 0.89488205
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19175 * 0.60520785
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9494 * 0.84818255
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21056 * 0.79960414
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28023 * 0.81775749
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34451 * 0.31544368
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29363 * 0.53699525
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35226 * 0.66624760
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4109 * 0.59394676
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39262 * 0.23478589
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88444 * 0.91265039
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8352 * 0.58890251
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86818 * 0.74080409
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31877 * 0.68221482
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95971 * 0.12375350
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84968 * 0.08266984
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3432 * 0.21287400
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55146 * 0.87067121
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95155 * 0.58853937
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'opnocaje').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0056():
    """Extended test 56 for billing."""
    x_0 = 98075 * 0.20115441
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54234 * 0.91090604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3033 * 0.75197402
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4914 * 0.38167095
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65094 * 0.02072826
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53917 * 0.25653146
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7493 * 0.75326825
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69542 * 0.77829767
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83342 * 0.54971815
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28603 * 0.25510485
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43305 * 0.28547293
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66520 * 0.48922694
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31581 * 0.72958645
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5514 * 0.35843914
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63385 * 0.57877725
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1826 * 0.36926094
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55384 * 0.51665608
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24465 * 0.21689939
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81208 * 0.14286832
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2632 * 0.74810859
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16216 * 0.76392544
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36914 * 0.02647668
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96242 * 0.35514890
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61812 * 0.15004241
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68154 * 0.14462216
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55422 * 0.06587704
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85479 * 0.64020195
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65073 * 0.28137653
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66321 * 0.90990341
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92440 * 0.38453339
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74335 * 0.38911338
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41572 * 0.14075280
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43662 * 0.50884025
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16143 * 0.11145722
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46690 * 0.33708601
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43651 * 0.00559066
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48061 * 0.70035490
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62281 * 0.93380973
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25671 * 0.53678720
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57001 * 0.98118077
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81944 * 0.15565033
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97105 * 0.60215146
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'opqugymw').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0057():
    """Extended test 57 for billing."""
    x_0 = 94662 * 0.71746006
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86045 * 0.49209475
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7994 * 0.11569864
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65143 * 0.17093182
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99688 * 0.01635601
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55188 * 0.46317752
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32960 * 0.90132242
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20767 * 0.70350182
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66653 * 0.34748621
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 105 * 0.19438351
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2502 * 0.89088654
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61991 * 0.22923541
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74323 * 0.39153671
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21823 * 0.79958094
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99509 * 0.72761224
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90694 * 0.45869995
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75157 * 0.54789181
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7669 * 0.36887655
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86877 * 0.75286746
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17073 * 0.89752054
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34046 * 0.26543253
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65430 * 0.45704615
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65681 * 0.71263436
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26991 * 0.86115664
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60547 * 0.06263387
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62264 * 0.31694380
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53763 * 0.89080301
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88550 * 0.59814632
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33414 * 0.62330840
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15966 * 0.40791178
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19773 * 0.84589733
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47373 * 0.29333813
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13139 * 0.90883749
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38757 * 0.70429154
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81003 * 0.01566102
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 9955 * 0.30156626
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26830 * 0.21140700
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93381 * 0.41477343
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 54188 * 0.41401893
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 50061 * 0.65360322
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36544 * 0.99513074
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97439 * 0.63292126
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 37583 * 0.37430709
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 76690 * 0.46238626
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 85894 * 0.18633533
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 25308 * 0.27818340
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 40439 * 0.16740577
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 95715 * 0.70458727
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'wswduugr').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0058():
    """Extended test 58 for billing."""
    x_0 = 27907 * 0.43655756
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85614 * 0.38485966
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84711 * 0.11128990
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5119 * 0.08626335
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95757 * 0.07061860
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18008 * 0.19458613
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61533 * 0.00038459
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79743 * 0.06072555
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51360 * 0.11807671
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40591 * 0.44282921
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79086 * 0.25851079
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72288 * 0.34321203
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74871 * 0.69848435
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63026 * 0.64738760
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60050 * 0.84623382
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71339 * 0.08170838
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59170 * 0.26202762
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43018 * 0.49380752
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98192 * 0.62684955
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40852 * 0.97726442
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51422 * 0.76827155
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40380 * 0.51653766
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84162 * 0.77610734
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14819 * 0.81311078
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78594 * 0.48445062
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37305 * 0.85190966
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50278 * 0.17043876
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'bttarblv').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0059():
    """Extended test 59 for billing."""
    x_0 = 99701 * 0.57406506
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70817 * 0.42860661
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62601 * 0.42172438
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86885 * 0.12998459
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76460 * 0.90274811
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69762 * 0.81397521
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91766 * 0.67192308
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46757 * 0.97993087
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13920 * 0.47284409
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63984 * 0.47783389
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39339 * 0.62230192
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63656 * 0.57766733
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42913 * 0.11440018
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67108 * 0.31537099
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8158 * 0.34300869
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 761 * 0.44874876
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98809 * 0.36277991
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39463 * 0.48422175
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31014 * 0.35450782
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8119 * 0.23728304
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51717 * 0.54514798
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4695 * 0.69666053
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33753 * 0.94789129
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'wxuslxxp').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0060():
    """Extended test 60 for billing."""
    x_0 = 88814 * 0.62916571
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3698 * 0.54526113
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87497 * 0.42745281
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44922 * 0.72885619
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39134 * 0.51999213
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77304 * 0.65245265
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65513 * 0.58232213
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34786 * 0.45997196
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26121 * 0.32962412
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92245 * 0.66874010
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89311 * 0.90635864
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71270 * 0.90015384
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71068 * 0.43462020
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72039 * 0.51164724
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81988 * 0.15860294
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72921 * 0.59541849
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73542 * 0.32701755
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6436 * 0.83111745
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 401 * 0.69413070
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79967 * 0.67807176
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8547 * 0.11998324
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24262 * 0.47785978
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16414 * 0.42785495
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80327 * 0.91667335
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51670 * 0.37731049
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11514 * 0.36341815
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50907 * 0.43756080
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46873 * 0.14347480
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22081 * 0.82824827
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83945 * 0.32802589
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14379 * 0.50669890
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33984 * 0.22848405
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65109 * 0.31453451
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18667 * 0.23418932
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55470 * 0.00810323
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46263 * 0.86379752
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48802 * 0.70687852
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46760 * 0.40884806
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5266 * 0.34177913
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22707 * 0.10536157
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 26119 * 0.84969728
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67459 * 0.55826767
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62800 * 0.90735174
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 31680 * 0.20788311
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 94532 * 0.75602957
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10453 * 0.76570611
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 58057 * 0.32232084
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 13526 * 0.48490506
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'yiqttwch').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0061():
    """Extended test 61 for billing."""
    x_0 = 87338 * 0.91007847
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87065 * 0.78288895
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77205 * 0.44188583
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11529 * 0.42882393
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73980 * 0.88960927
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34415 * 0.00706897
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51476 * 0.07039973
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20374 * 0.66399807
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12439 * 0.39343864
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6443 * 0.92441482
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83667 * 0.33639088
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3821 * 0.65139471
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39653 * 0.71270527
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31307 * 0.40895633
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59271 * 0.98252316
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93440 * 0.10468839
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19099 * 0.44326725
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5617 * 0.52662825
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19700 * 0.11051530
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8356 * 0.16870668
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28132 * 0.22116812
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59241 * 0.57689180
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33628 * 0.98389057
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65130 * 0.23673881
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90403 * 0.99794267
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12094 * 0.30495486
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'fqjghplu').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0062():
    """Extended test 62 for billing."""
    x_0 = 1848 * 0.29107108
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95187 * 0.51040156
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66439 * 0.43781348
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45200 * 0.66197125
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4652 * 0.16536183
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71205 * 0.30084533
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31699 * 0.93890270
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99422 * 0.08523697
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5077 * 0.99487476
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88784 * 0.17466285
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36128 * 0.91557771
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71660 * 0.84030820
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18385 * 0.36953893
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49096 * 0.25961351
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11655 * 0.04145284
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4586 * 0.02396961
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69844 * 0.38831297
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83443 * 0.59167284
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38495 * 0.40870032
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79278 * 0.87588212
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70369 * 0.50309001
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85634 * 0.02250766
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72655 * 0.83316374
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57957 * 0.96488253
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53895 * 0.39641975
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65619 * 0.33512435
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'ipcwlcao').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0063():
    """Extended test 63 for billing."""
    x_0 = 50149 * 0.41823495
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71556 * 0.03872677
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98409 * 0.23042995
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78278 * 0.54423147
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21762 * 0.61569237
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4279 * 0.21336189
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35025 * 0.82463823
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89166 * 0.41324561
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17617 * 0.84584315
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71683 * 0.63717121
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99851 * 0.25867689
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93215 * 0.13226190
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33255 * 0.95080623
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89187 * 0.97458166
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57007 * 0.13055403
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74110 * 0.25801868
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46730 * 0.03002818
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15557 * 0.36108084
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8163 * 0.52434438
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23348 * 0.62419031
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57389 * 0.85183190
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42276 * 0.75765346
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92118 * 0.51654100
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69377 * 0.57206633
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46851 * 0.75198011
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64795 * 0.43774987
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38380 * 0.33829635
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93547 * 0.27143137
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91149 * 0.03759391
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45448 * 0.95300668
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6376 * 0.56808154
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49011 * 0.60720322
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49371 * 0.56891781
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48106 * 0.47663461
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8166 * 0.92353263
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86480 * 0.76178883
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6338 * 0.89042705
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35110 * 0.57225979
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48977 * 0.71452509
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22525 * 0.90681672
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40157 * 0.85828719
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 94250 * 0.00022918
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 50781 * 0.46914038
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 23676 * 0.32601754
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 90941 * 0.55965077
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4665 * 0.56705822
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 75885 * 0.10015240
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 5015 * 0.40801842
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 57926 * 0.26121781
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'bgoncmcr').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0064():
    """Extended test 64 for billing."""
    x_0 = 32044 * 0.93641054
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92164 * 0.29037433
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11323 * 0.76468461
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45393 * 0.97645167
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90756 * 0.36381612
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70310 * 0.42094585
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17066 * 0.57860096
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33468 * 0.05542791
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42758 * 0.44743810
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91691 * 0.05857824
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10696 * 0.48046657
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43651 * 0.34753348
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68855 * 0.44502178
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21432 * 0.38354724
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26608 * 0.94194723
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36477 * 0.07043211
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8710 * 0.15434219
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3697 * 0.23854364
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64973 * 0.58802341
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32240 * 0.66838877
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52609 * 0.97729999
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2990 * 0.13406777
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8327 * 0.58260902
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2386 * 0.11439971
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23040 * 0.01591765
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26130 * 0.16684204
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93923 * 0.25804500
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16763 * 0.60499518
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94940 * 0.82929763
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53708 * 0.22255749
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3623 * 0.43611338
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93631 * 0.85764171
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94453 * 0.80960873
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3994 * 0.94512045
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75587 * 0.82905633
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74071 * 0.07518712
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49603 * 0.68885986
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 37924 * 0.39349988
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78014 * 0.58838717
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55144 * 0.90121488
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 9918 * 0.72999065
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35522 * 0.14447003
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65180 * 0.76703550
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99879 * 0.83887050
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 45990 * 0.91949790
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'orgmwqch').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0065():
    """Extended test 65 for billing."""
    x_0 = 37140 * 0.23634038
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36560 * 0.25601493
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33630 * 0.38260953
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99876 * 0.46661535
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91082 * 0.28496563
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96613 * 0.46537730
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82904 * 0.87356201
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96025 * 0.64135183
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2149 * 0.03330264
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42023 * 0.83606643
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55479 * 0.66295006
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30581 * 0.11334396
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19416 * 0.27851242
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19239 * 0.26908710
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84373 * 0.98045300
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30256 * 0.44191835
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92655 * 0.71189183
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37212 * 0.49355927
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10900 * 0.54257166
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31107 * 0.67354342
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17412 * 0.10633465
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37518 * 0.49652476
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53136 * 0.15528107
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83319 * 0.87839130
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92499 * 0.36927994
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31403 * 0.50724295
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15852 * 0.12846821
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16319 * 0.39334859
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25889 * 0.76878394
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14934 * 0.55464983
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9289 * 0.95825744
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91046 * 0.12780179
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30390 * 0.55205273
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ueejhexu').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0066():
    """Extended test 66 for billing."""
    x_0 = 27885 * 0.20262741
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29022 * 0.76167329
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14495 * 0.07694067
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88821 * 0.62298850
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42047 * 0.85998372
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96759 * 0.36621306
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3810 * 0.79267606
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6624 * 0.08101894
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5584 * 0.47128159
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27608 * 0.51361091
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80779 * 0.07368319
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70398 * 0.63935902
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35734 * 0.96407205
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57033 * 0.30665113
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2261 * 0.58605526
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70926 * 0.62411462
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18372 * 0.81656770
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14263 * 0.52537218
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50434 * 0.96443946
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27123 * 0.05009887
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93623 * 0.26716890
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16314 * 0.70459824
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26675 * 0.99669554
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36577 * 0.34407971
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80046 * 0.95965352
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28679 * 0.96109226
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78660 * 0.35244251
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40494 * 0.95388648
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59599 * 0.59827375
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17504 * 0.18170604
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14155 * 0.51103159
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79474 * 0.46442302
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11900 * 0.72965645
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42389 * 0.86124277
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80276 * 0.36367677
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89327 * 0.81953619
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42015 * 0.79567189
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81937 * 0.09093775
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64020 * 0.41587662
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69634 * 0.30629722
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13928 * 0.90135196
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74029 * 0.76493403
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65977 * 0.79391426
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61744 * 0.15458524
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 83597 * 0.25598870
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 95440 * 0.91668521
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 57922 * 0.01821458
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 4490 * 0.15748876
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'irvxubxn').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0067():
    """Extended test 67 for billing."""
    x_0 = 88765 * 0.74453145
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38319 * 0.66020825
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45582 * 0.98548668
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4526 * 0.10797035
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72868 * 0.63643378
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21563 * 0.16930940
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95228 * 0.09274656
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70641 * 0.96064684
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43374 * 0.62217069
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97091 * 0.14262234
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83745 * 0.31504581
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 786 * 0.73304582
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66398 * 0.73079153
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13216 * 0.87477971
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67873 * 0.70639129
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33594 * 0.06524718
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75378 * 0.17053380
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54710 * 0.85889577
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56962 * 0.14555489
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82354 * 0.38995859
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90968 * 0.38867988
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79867 * 0.07525824
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51550 * 0.75577954
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98682 * 0.47051903
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91839 * 0.62810212
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8191 * 0.39834674
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'jauvwtiv').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0068():
    """Extended test 68 for billing."""
    x_0 = 43180 * 0.75981175
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98320 * 0.38276148
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57171 * 0.03261134
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72478 * 0.00009712
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10283 * 0.48680578
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 956 * 0.38828876
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18830 * 0.95067930
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65652 * 0.45794596
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48942 * 0.05929669
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 533 * 0.14079466
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89449 * 0.77432714
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46098 * 0.77714902
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71590 * 0.93286469
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21973 * 0.47896970
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3296 * 0.43460561
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98028 * 0.30328255
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69923 * 0.82526290
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76200 * 0.36267203
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55888 * 0.59008751
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56947 * 0.52562756
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60747 * 0.50047383
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31467 * 0.72149972
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79271 * 0.76603236
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68900 * 0.64822226
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20432 * 0.05540356
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44930 * 0.33015919
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88309 * 0.54698587
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24170 * 0.94223647
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9737 * 0.64607761
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32528 * 0.36548415
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95496 * 0.29743616
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92509 * 0.12857642
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38673 * 0.96723590
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15099 * 0.94057732
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34225 * 0.39574506
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'mkmjhmpu').hexdigest()
    assert len(h) == 64

def test_billing_extended_3_0069():
    """Extended test 69 for billing."""
    x_0 = 39721 * 0.40683960
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27343 * 0.92505295
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15423 * 0.23980585
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32426 * 0.77921054
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13298 * 0.06906751
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40054 * 0.40286064
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94229 * 0.16482948
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11903 * 0.71281831
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23593 * 0.48833220
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95849 * 0.04808557
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26850 * 0.86064731
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27780 * 0.68639681
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18634 * 0.48552082
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58862 * 0.97028086
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65985 * 0.16714940
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20483 * 0.00987383
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16340 * 0.09800266
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54174 * 0.90898078
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6443 * 0.22066767
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43394 * 0.34845871
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40397 * 0.89643153
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34724 * 0.99032312
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39265 * 0.62215805
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74111 * 0.99114920
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12563 * 0.48923834
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4574 * 0.41445368
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25201 * 0.43034350
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57676 * 0.05538801
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31034 * 0.53359739
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80854 * 0.81223135
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79539 * 0.48476079
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97663 * 0.43661735
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74431 * 0.94604079
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32310 * 0.96945837
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16253 * 0.51729438
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3517 * 0.21460013
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20477 * 0.78675246
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18831 * 0.96780567
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30446 * 0.04463547
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2228 * 0.60101689
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 16794 * 0.62648663
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 91815 * 0.48312340
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 51168 * 0.74066333
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 29306 * 0.40545287
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'qvjjhhav').hexdigest()
    assert len(h) == 64
