"""Extended tests for aggregation suite 3."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_aggregation_extended_3_0000():
    """Extended test 0 for aggregation."""
    x_0 = 28690 * 0.07458548
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11003 * 0.71700701
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37932 * 0.10417214
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48964 * 0.09271446
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35024 * 0.38114409
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48649 * 0.91915451
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15319 * 0.09707316
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80164 * 0.99885096
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75439 * 0.32172285
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18062 * 0.19491476
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21496 * 0.12069581
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19304 * 0.83991409
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60831 * 0.72816110
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56710 * 0.93643980
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10850 * 0.38686392
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39148 * 0.05989750
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9769 * 0.49416235
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43582 * 0.85690453
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37886 * 0.19611220
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81800 * 0.54367242
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45811 * 0.49142391
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62389 * 0.13028750
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66892 * 0.76604261
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24694 * 0.36804789
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44967 * 0.28847533
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75880 * 0.50754379
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29417 * 0.14335834
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98739 * 0.49661248
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61099 * 0.74088963
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38924 * 0.84659608
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71109 * 0.88617628
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ljmevrfd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0001():
    """Extended test 1 for aggregation."""
    x_0 = 22899 * 0.76676864
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39818 * 0.48301604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98905 * 0.82671440
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61062 * 0.54656426
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5959 * 0.21521724
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57266 * 0.01247993
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46811 * 0.90669637
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41307 * 0.37693522
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60123 * 0.96871885
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63766 * 0.53977348
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18376 * 0.39221748
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26639 * 0.36574402
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69567 * 0.35947199
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78818 * 0.18085874
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5343 * 0.59901911
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17946 * 0.01487274
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88764 * 0.22747551
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56396 * 0.23912537
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20713 * 0.34035276
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23450 * 0.40390826
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71544 * 0.19321511
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41606 * 0.35051887
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86763 * 0.88998366
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6992 * 0.67730544
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50550 * 0.09473076
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78256 * 0.88112592
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61590 * 0.96036309
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21007 * 0.55408866
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45537 * 0.58331443
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67201 * 0.19744379
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8794 * 0.43859828
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'crlilxpj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0002():
    """Extended test 2 for aggregation."""
    x_0 = 16559 * 0.38525492
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58954 * 0.20451634
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32926 * 0.99146368
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62915 * 0.76076705
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11109 * 0.54874029
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61027 * 0.03388710
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2973 * 0.76786991
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84537 * 0.18392188
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40346 * 0.55487696
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72130 * 0.05902475
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30916 * 0.56194332
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57122 * 0.94921518
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3995 * 0.29724288
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12154 * 0.14116075
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98532 * 0.32572969
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70853 * 0.25978783
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65010 * 0.44416250
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68101 * 0.52476862
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54844 * 0.72372441
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99637 * 0.50610752
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81957 * 0.71628287
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26710 * 0.50228963
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27135 * 0.50128123
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97884 * 0.31579021
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53062 * 0.72343150
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48183 * 0.18722353
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77080 * 0.62177436
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9478 * 0.56206847
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53826 * 0.08159854
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47781 * 0.41162710
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89530 * 0.80526600
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23509 * 0.36172886
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51267 * 0.49663533
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43135 * 0.26533251
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56596 * 0.05494825
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84062 * 0.96667710
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3020 * 0.43279104
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19598 * 0.97624550
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49076 * 0.25317554
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29769 * 0.96668149
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40648 * 0.27935456
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 7355 * 0.96872059
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10609 * 0.20298894
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 26006 * 0.76852547
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4482 * 0.53802310
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 633 * 0.88607599
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 66714 * 0.23681488
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 66206 * 0.25736064
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 69901 * 0.53700564
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'ddthxxzr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0003():
    """Extended test 3 for aggregation."""
    x_0 = 6338 * 0.87630592
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23372 * 0.60053641
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48479 * 0.82052482
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45309 * 0.76565847
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5996 * 0.11390707
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20254 * 0.38994775
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24492 * 0.02736413
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43338 * 0.82482498
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95066 * 0.45891305
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76418 * 0.97613992
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65686 * 0.13123098
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87675 * 0.78753228
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74987 * 0.53265510
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61357 * 0.19792802
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41742 * 0.12037378
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34176 * 0.84506668
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13791 * 0.37066317
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4366 * 0.59196567
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81808 * 0.15267803
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44941 * 0.42037154
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23462 * 0.08375071
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64303 * 0.68239732
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7239 * 0.55716058
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67924 * 0.05089818
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8092 * 0.96956302
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87290 * 0.54810558
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4931 * 0.32414245
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19046 * 0.70596423
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23953 * 0.32904179
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37392 * 0.23422759
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 930 * 0.02792202
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46146 * 0.22662531
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78137 * 0.92809630
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48541 * 0.10059673
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77079 * 0.20756414
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22169 * 0.28980771
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64672 * 0.59432343
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69128 * 0.79721630
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13953 * 0.33105063
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96348 * 0.35496230
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2514 * 0.23746908
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33928 * 0.28591605
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 26263 * 0.94865203
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22498 * 0.79795143
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 73982 * 0.48993468
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 65620 * 0.30846886
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'idobehef').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0004():
    """Extended test 4 for aggregation."""
    x_0 = 40251 * 0.12194540
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86306 * 0.17334222
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69612 * 0.38577525
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38639 * 0.78866889
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20908 * 0.14797258
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65986 * 0.85508927
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78738 * 0.59294463
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 375 * 0.61751912
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72266 * 0.27275877
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89221 * 0.08235434
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93100 * 0.15575496
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51469 * 0.25978746
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56898 * 0.76826684
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65228 * 0.25879945
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18734 * 0.53619828
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93369 * 0.58869639
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87908 * 0.59802204
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18648 * 0.00159698
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56915 * 0.85026021
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33201 * 0.52001393
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'hfukuuzn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0005():
    """Extended test 5 for aggregation."""
    x_0 = 8833 * 0.93667293
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29315 * 0.75150273
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64401 * 0.41257478
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77820 * 0.92476312
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47506 * 0.90761336
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78589 * 0.10737673
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62979 * 0.09566069
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34299 * 0.29230764
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9723 * 0.47023529
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94766 * 0.03792165
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11835 * 0.56374039
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95140 * 0.29685995
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38357 * 0.14372566
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16450 * 0.75691127
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18992 * 0.80117986
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66898 * 0.29730354
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1072 * 0.43739742
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79776 * 0.15363820
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91079 * 0.67791910
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44148 * 0.25758874
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41895 * 0.31317457
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18109 * 0.57253141
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98246 * 0.36032175
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54779 * 0.45515793
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21839 * 0.63972808
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96303 * 0.64873732
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17125 * 0.63181793
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16738 * 0.97138866
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92112 * 0.40189966
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7723 * 0.81915976
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69637 * 0.38106468
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84659 * 0.78661659
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6820 * 0.58538203
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35828 * 0.55941490
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14802 * 0.91105836
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75703 * 0.50279095
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98094 * 0.55476662
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47601 * 0.39807441
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9514 * 0.91398683
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74100 * 0.21123512
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17724 * 0.56184198
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12696 * 0.15736807
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 43680 * 0.08861314
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 73355 * 0.82281700
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10137 * 0.02134464
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 27832 * 0.75346979
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 56234 * 0.55395743
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'whjytmqx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0006():
    """Extended test 6 for aggregation."""
    x_0 = 58320 * 0.52651387
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57682 * 0.58089496
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54252 * 0.66723600
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8708 * 0.09167792
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23902 * 0.06618821
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38702 * 0.56277343
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30690 * 0.34951248
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76290 * 0.61891105
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51417 * 0.60452898
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10966 * 0.82265561
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96535 * 0.52863292
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95807 * 0.32004329
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87682 * 0.34862423
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17479 * 0.35002428
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24491 * 0.19015781
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37166 * 0.16192918
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27713 * 0.91578555
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55963 * 0.06812503
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42745 * 0.86344365
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91001 * 0.43749779
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37680 * 0.97233132
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59528 * 0.04557931
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28580 * 0.66501595
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89927 * 0.59873289
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38330 * 0.39978030
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59513 * 0.07820822
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79401 * 0.21914911
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'eeqilqqb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0007():
    """Extended test 7 for aggregation."""
    x_0 = 7802 * 0.71368412
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84870 * 0.75438145
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24213 * 0.48227158
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18956 * 0.46994316
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44068 * 0.01872430
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56045 * 0.39902825
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19542 * 0.67605180
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67646 * 0.95086027
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77259 * 0.34176981
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87486 * 0.63267020
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1415 * 0.29595619
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78206 * 0.36442375
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86308 * 0.11585536
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90631 * 0.03479680
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30121 * 0.10326173
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30985 * 0.18714051
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89526 * 0.48328204
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63565 * 0.45863001
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1146 * 0.29262628
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1799 * 0.04782570
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50577 * 0.85285863
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81507 * 0.08386960
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19967 * 0.53486756
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'yguzhkdf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0008():
    """Extended test 8 for aggregation."""
    x_0 = 96854 * 0.52562881
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49622 * 0.55629149
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49332 * 0.24834557
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40861 * 0.33100603
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81614 * 0.18667919
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26718 * 0.40541587
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91104 * 0.56759727
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63503 * 0.01725945
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91152 * 0.09454922
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56503 * 0.37926973
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47113 * 0.44181053
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14403 * 0.97278156
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8377 * 0.15433781
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25644 * 0.69355805
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58268 * 0.13674371
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41446 * 0.68393633
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83164 * 0.67426563
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32995 * 0.72633174
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7160 * 0.44262738
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81657 * 0.22542470
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82367 * 0.90819113
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'yelkmpig').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0009():
    """Extended test 9 for aggregation."""
    x_0 = 37756 * 0.79335278
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75332 * 0.52181486
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58362 * 0.02855199
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8227 * 0.65570857
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54521 * 0.69632046
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56156 * 0.21730409
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34029 * 0.61313210
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96799 * 0.61017269
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60097 * 0.06552126
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27120 * 0.69094304
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18337 * 0.99406768
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89839 * 0.04987548
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84958 * 0.71356403
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92987 * 0.14212838
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82631 * 0.91262533
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38498 * 0.44719013
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52790 * 0.41243937
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59268 * 0.22810532
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82558 * 0.02729547
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38847 * 0.82825698
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8210 * 0.99351044
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28693 * 0.42095370
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24903 * 0.22826563
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92824 * 0.35842528
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30872 * 0.71432681
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52727 * 0.37375713
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'sznsovfh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0010():
    """Extended test 10 for aggregation."""
    x_0 = 4912 * 0.87317826
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38424 * 0.81318629
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42233 * 0.39824542
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65015 * 0.03845278
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73256 * 0.60491712
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89619 * 0.88614203
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28803 * 0.43201188
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70893 * 0.12959291
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35479 * 0.47232528
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86360 * 0.47550939
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41909 * 0.27329611
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 937 * 0.97700523
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5003 * 0.68767473
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95992 * 0.88469543
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57650 * 0.80695710
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90523 * 0.51967784
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42703 * 0.80897870
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65099 * 0.19565956
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88569 * 0.36139854
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1100 * 0.27415989
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18323 * 0.70757207
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22596 * 0.57866293
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84727 * 0.33821805
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87967 * 0.77595512
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14592 * 0.99658668
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20636 * 0.71264555
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55650 * 0.41870494
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35472 * 0.67946673
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75225 * 0.06471121
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38606 * 0.53304493
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66975 * 0.84514154
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73456 * 0.34429716
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40332 * 0.58959811
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13858 * 0.85416033
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56287 * 0.95766777
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'kcbuvmwm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0011():
    """Extended test 11 for aggregation."""
    x_0 = 10323 * 0.53513154
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46608 * 0.81905361
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98515 * 0.58504250
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92730 * 0.22573883
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1043 * 0.44971442
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62331 * 0.68846151
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74531 * 0.26807189
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59573 * 0.63669937
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48221 * 0.79930463
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79307 * 0.75405073
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39482 * 0.52856854
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76305 * 0.94458325
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48962 * 0.77451925
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75085 * 0.64650471
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8708 * 0.79629765
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52889 * 0.40268028
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69240 * 0.27488341
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40679 * 0.07975437
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 692 * 0.27323014
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69228 * 0.00962505
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70814 * 0.59890319
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1827 * 0.53567067
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63555 * 0.25370168
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58698 * 0.62381479
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32880 * 0.57084444
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48764 * 0.21391105
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43330 * 0.79443313
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32707 * 0.76763582
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20000 * 0.65180598
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'lihxglbg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0012():
    """Extended test 12 for aggregation."""
    x_0 = 77946 * 0.72312406
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3173 * 0.46168905
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18596 * 0.73064953
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 497 * 0.49398730
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51441 * 0.44714697
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96270 * 0.04719911
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3367 * 0.11292549
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86794 * 0.69273294
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73129 * 0.56144280
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69834 * 0.24704098
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51617 * 0.77949290
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93363 * 0.72207786
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14605 * 0.62281618
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36991 * 0.10478490
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47941 * 0.68334332
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5110 * 0.20418579
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14942 * 0.72716309
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16983 * 0.66104413
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64532 * 0.07990387
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52623 * 0.80320255
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17306 * 0.03232482
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97114 * 0.24408059
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21095 * 0.49911416
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47774 * 0.83296155
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45163 * 0.01752130
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10026 * 0.89275883
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11240 * 0.67714176
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90429 * 0.86457898
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32833 * 0.37178962
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85210 * 0.24667870
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50148 * 0.69939861
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11556 * 0.99768053
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11155 * 0.16023070
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17838 * 0.35385802
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98918 * 0.72993475
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30117 * 0.31683821
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89144 * 0.20831853
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42974 * 0.97649015
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92554 * 0.06332142
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57528 * 0.86962179
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'vjsioymk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0013():
    """Extended test 13 for aggregation."""
    x_0 = 44534 * 0.74974970
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19354 * 0.59892521
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16490 * 0.67773985
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43690 * 0.94317099
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19175 * 0.32137977
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76157 * 0.78622763
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47739 * 0.33552789
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33290 * 0.36360455
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19834 * 0.76539621
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92121 * 0.14596195
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17519 * 0.50433787
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42404 * 0.56424574
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85034 * 0.54825751
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60392 * 0.13493806
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89877 * 0.23183056
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12246 * 0.57642634
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52229 * 0.70820706
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91584 * 0.70347657
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68472 * 0.46069541
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85401 * 0.56804567
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78847 * 0.41148435
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87636 * 0.72795237
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29848 * 0.51474028
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66987 * 0.23293073
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32944 * 0.24537103
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53171 * 0.17622220
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43099 * 0.24146657
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89531 * 0.37067292
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78337 * 0.91004301
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59960 * 0.75717514
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54311 * 0.49507124
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87243 * 0.57345670
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83610 * 0.72848169
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'xbveunlk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0014():
    """Extended test 14 for aggregation."""
    x_0 = 29543 * 0.66363094
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86465 * 0.93637138
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99304 * 0.78206938
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59100 * 0.56772385
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22352 * 0.60264300
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70236 * 0.48746240
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66980 * 0.42330732
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93960 * 0.19695566
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15789 * 0.01574408
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34841 * 0.02320571
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35751 * 0.73233788
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8424 * 0.45230733
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7128 * 0.67225808
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68003 * 0.71769451
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78305 * 0.21083903
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15387 * 0.36582215
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67473 * 0.45275457
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9632 * 0.62955962
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17199 * 0.31113496
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98136 * 0.43407504
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58535 * 0.60320511
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88576 * 0.64141828
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4461 * 0.99690395
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2228 * 0.09785284
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20996 * 0.10279525
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46035 * 0.00170150
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'fomcsnhl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0015():
    """Extended test 15 for aggregation."""
    x_0 = 27787 * 0.22614401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21252 * 0.76722306
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17036 * 0.54464404
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30380 * 0.95638194
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28231 * 0.11570406
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39743 * 0.92676960
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63127 * 0.72885096
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20159 * 0.26555810
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16406 * 0.62463154
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2423 * 0.65925762
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29821 * 0.64518289
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13347 * 0.49349643
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19492 * 0.55909878
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99502 * 0.09383083
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68821 * 0.79016923
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97630 * 0.35106669
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83456 * 0.69501966
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35064 * 0.09563049
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78250 * 0.49391531
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56121 * 0.39306825
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96356 * 0.99526963
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51146 * 0.28304464
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30227 * 0.84209544
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3858 * 0.67831421
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11723 * 0.83389295
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98651 * 0.36056967
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32958 * 0.74319750
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93529 * 0.83045251
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27148 * 0.71041228
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50307 * 0.87368552
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71759 * 0.29087212
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1732 * 0.47892211
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81893 * 0.01920812
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55194 * 0.99004195
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50192 * 0.31503186
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37257 * 0.81341233
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69218 * 0.11885151
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15528 * 0.29012281
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40559 * 0.36342007
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79732 * 0.16993089
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40231 * 0.07010457
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43175 * 0.89574832
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'vgbvcbpm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0016():
    """Extended test 16 for aggregation."""
    x_0 = 72130 * 0.37045610
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12092 * 0.15940606
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7243 * 0.71479823
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23899 * 0.79082503
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75411 * 0.27756248
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7475 * 0.80391801
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61249 * 0.24856062
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35755 * 0.38864069
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46538 * 0.72928462
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30434 * 0.16575563
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77032 * 0.36969307
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72733 * 0.16630010
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27987 * 0.22164358
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31734 * 0.26811825
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71436 * 0.38501552
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3654 * 0.49520243
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28841 * 0.09281478
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53711 * 0.61884185
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64555 * 0.06922919
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93540 * 0.05212945
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89680 * 0.60179730
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43187 * 0.83414694
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24437 * 0.33884733
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40171 * 0.95335638
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93354 * 0.18563182
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25921 * 0.29436491
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78159 * 0.05383377
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15479 * 0.00262910
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23061 * 0.91885221
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85945 * 0.71671464
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69306 * 0.36543186
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60637 * 0.53697363
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9659 * 0.43526788
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43089 * 0.08612702
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66262 * 0.04093839
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 756 * 0.73897248
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46362 * 0.93535535
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49019 * 0.64385999
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37632 * 0.51461378
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15665 * 0.83867556
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 7327 * 0.62976073
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58641 * 0.72127198
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83622 * 0.04662398
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 54871 * 0.11065042
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 88619 * 0.13092206
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 40600 * 0.27505038
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 79417 * 0.91599015
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 40566 * 0.68121713
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 96543 * 0.68258750
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'xmyqjklr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0017():
    """Extended test 17 for aggregation."""
    x_0 = 28739 * 0.47037163
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2638 * 0.96845798
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79293 * 0.95259608
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86130 * 0.43878436
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92747 * 0.84949110
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19270 * 0.57833160
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30481 * 0.91878269
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95781 * 0.05031885
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94194 * 0.33636124
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16396 * 0.69692121
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58579 * 0.21568614
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32456 * 0.20823703
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26500 * 0.39944945
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8159 * 0.63911805
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90260 * 0.76970841
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5510 * 0.61073542
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15618 * 0.29687947
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12291 * 0.83793437
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93020 * 0.67525350
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59288 * 0.76664899
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33804 * 0.84493692
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52809 * 0.14856062
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83076 * 0.22106475
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'xpebjmez').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0018():
    """Extended test 18 for aggregation."""
    x_0 = 70592 * 0.20596925
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14159 * 0.97594264
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99481 * 0.10420181
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89335 * 0.79710325
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91135 * 0.20553442
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38338 * 0.63215381
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57202 * 0.24135798
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27311 * 0.32177102
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7706 * 0.86954691
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51758 * 0.17812808
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16794 * 0.33942600
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87487 * 0.28299780
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52137 * 0.38089160
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90189 * 0.34419938
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77544 * 0.20780495
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68560 * 0.96205269
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64888 * 0.72963383
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96243 * 0.62089243
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45206 * 0.62640221
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8701 * 0.28012941
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48805 * 0.54740680
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68097 * 0.55148799
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 674 * 0.03184677
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38990 * 0.19371422
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13504 * 0.45631087
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92349 * 0.65970883
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99953 * 0.82208896
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34726 * 0.70007116
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75868 * 0.08125563
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52281 * 0.95831963
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40759 * 0.00084492
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16057 * 0.21469717
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22793 * 0.14152815
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8102 * 0.81303741
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26861 * 0.38238068
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27487 * 0.19962100
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59719 * 0.24915497
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93865 * 0.08650333
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'gipwxbyd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0019():
    """Extended test 19 for aggregation."""
    x_0 = 25891 * 0.00493520
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72512 * 0.88837370
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47935 * 0.22842523
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13318 * 0.94836554
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86973 * 0.23429312
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5262 * 0.53726920
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40392 * 0.48804077
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35249 * 0.59919573
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77932 * 0.07227208
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46662 * 0.70331463
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77520 * 0.19279936
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97090 * 0.82294775
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41106 * 0.50332367
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87541 * 0.55801068
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72766 * 0.85544681
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48967 * 0.06290410
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23112 * 0.84199030
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9461 * 0.42037345
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21814 * 0.57678400
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39687 * 0.68523746
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51858 * 0.96318769
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97308 * 0.78837090
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95554 * 0.43372814
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7269 * 0.35162086
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65788 * 0.24966570
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97343 * 0.08515181
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86693 * 0.92090377
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44800 * 0.80107543
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50525 * 0.50454292
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9739 * 0.17207649
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3284 * 0.93026916
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70838 * 0.62902916
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9609 * 0.51985990
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6913 * 0.19037973
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75474 * 0.90459145
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94900 * 0.76285549
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12620 * 0.74928045
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27592 * 0.33846771
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30885 * 0.05965925
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 53705 * 0.74166957
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65780 * 0.90466248
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'emdabwmo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0020():
    """Extended test 20 for aggregation."""
    x_0 = 45233 * 0.38003591
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36582 * 0.93613733
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4507 * 0.57259340
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 513 * 0.38607818
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65935 * 0.34242584
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90677 * 0.48766436
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61763 * 0.13961617
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98800 * 0.24393765
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64111 * 0.95146561
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48304 * 0.92932293
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44946 * 0.00802818
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77226 * 0.57221077
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69075 * 0.14286860
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58946 * 0.49790938
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6939 * 0.88999040
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65275 * 0.77391788
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72853 * 0.54689560
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59121 * 0.12117966
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52816 * 0.88209885
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42537 * 0.55460509
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30685 * 0.67310855
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40223 * 0.89085533
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2510 * 0.88055600
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12453 * 0.17578479
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33208 * 0.79907365
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66151 * 0.23488745
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49281 * 0.12375892
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81532 * 0.38896802
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26524 * 0.51325973
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18476 * 0.41163501
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85779 * 0.40921825
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89862 * 0.69805868
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30899 * 0.54207974
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46697 * 0.05255890
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60222 * 0.06370666
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82630 * 0.27893274
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71728 * 0.01696102
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19533 * 0.01637073
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 7505 * 0.10421456
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16408 * 0.74794776
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84136 * 0.70973939
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 8147 * 0.63687579
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 39570 * 0.31951928
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 71050 * 0.08821752
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 44926 * 0.23725664
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 95147 * 0.92289871
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 84256 * 0.71450360
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 49556 * 0.51875036
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 9075 * 0.42256231
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'xyzijyit').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0021():
    """Extended test 21 for aggregation."""
    x_0 = 62690 * 0.99643435
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34781 * 0.09679163
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94604 * 0.18700646
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57017 * 0.15033328
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81296 * 0.77683106
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82072 * 0.23572388
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16890 * 0.78252500
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8773 * 0.70705132
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91300 * 0.46060161
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57296 * 0.55465475
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30412 * 0.37954374
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98715 * 0.94799411
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13165 * 0.05002965
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20655 * 0.49884809
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13506 * 0.15988995
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22760 * 0.93248958
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35222 * 0.99300641
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29570 * 0.47665219
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2711 * 0.27835453
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89215 * 0.98464429
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77213 * 0.52244233
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2463 * 0.45841223
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81972 * 0.77761017
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27462 * 0.12101186
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 696 * 0.66341643
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27799 * 0.30956308
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25173 * 0.31635945
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ehfkeozn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0022():
    """Extended test 22 for aggregation."""
    x_0 = 24754 * 0.91593311
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9688 * 0.47369424
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39481 * 0.66569058
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34915 * 0.03104189
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11471 * 0.03350777
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14767 * 0.79755991
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64432 * 0.78168950
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3491 * 0.93849654
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57511 * 0.43229119
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7215 * 0.14326528
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42621 * 0.03232353
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43487 * 0.82289825
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13117 * 0.98711831
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29119 * 0.15498444
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61297 * 0.67560511
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78748 * 0.95552895
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6096 * 0.67997063
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50133 * 0.36115335
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42638 * 0.34135858
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10347 * 0.64878481
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51805 * 0.42131694
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5006 * 0.39609669
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40588 * 0.68608940
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39441 * 0.88285157
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14316 * 0.01077930
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76976 * 0.42195998
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7044 * 0.02664400
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58918 * 0.15761200
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49089 * 0.09842387
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7358 * 0.91387021
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95147 * 0.50525017
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89818 * 0.74974848
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66007 * 0.60334839
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79517 * 0.98780095
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19793 * 0.23846328
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51542 * 0.48180455
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17278 * 0.94638395
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39216 * 0.89005669
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82889 * 0.57834691
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30263 * 0.85121597
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'rhnaqbtg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0023():
    """Extended test 23 for aggregation."""
    x_0 = 9044 * 0.41357119
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87310 * 0.70228183
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99168 * 0.45862650
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18813 * 0.81795512
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85101 * 0.34497281
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16175 * 0.45076193
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47321 * 0.39378536
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56360 * 0.81357011
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28668 * 0.15157723
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54921 * 0.87245193
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97769 * 0.47416961
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27155 * 0.80433560
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6867 * 0.39917658
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26563 * 0.48213409
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38765 * 0.75606000
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80844 * 0.65034376
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46687 * 0.24987295
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70782 * 0.85028676
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35231 * 0.37429467
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4338 * 0.88971683
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14779 * 0.02312159
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27162 * 0.97876722
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62424 * 0.34635509
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69968 * 0.35290470
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11229 * 0.56069807
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27742 * 0.80816546
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51248 * 0.20989541
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63282 * 0.18704045
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1734 * 0.32169266
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75288 * 0.29110528
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60301 * 0.42225886
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9689 * 0.24347001
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76550 * 0.55057348
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52679 * 0.79066386
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70117 * 0.26967949
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66723 * 0.90915115
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54476 * 0.13344844
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21633 * 0.57781573
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48668 * 0.71487177
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33346 * 0.98191246
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'yrjmlvin').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0024():
    """Extended test 24 for aggregation."""
    x_0 = 4926 * 0.94623754
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80169 * 0.10879467
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50370 * 0.14779059
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77627 * 0.84292277
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71518 * 0.95606137
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20938 * 0.15856542
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59002 * 0.63685304
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54024 * 0.26819794
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91362 * 0.05403512
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69206 * 0.38397736
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9425 * 0.16044557
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23193 * 0.16287424
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43177 * 0.87789711
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63634 * 0.16076618
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75853 * 0.59154130
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60257 * 0.10709875
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69347 * 0.42249005
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2153 * 0.15132724
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66888 * 0.10575680
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94803 * 0.71864368
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60565 * 0.62176891
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47524 * 0.97068323
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69178 * 0.61793074
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97060 * 0.74728794
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49648 * 0.04547677
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44544 * 0.81678311
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18662 * 0.77281465
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10599 * 0.13032711
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64619 * 0.58338655
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42920 * 0.72172741
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46954 * 0.66478098
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77446 * 0.57688721
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77151 * 0.21252507
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6490 * 0.82811739
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56026 * 0.63953660
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6254 * 0.40115122
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49853 * 0.73381726
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79433 * 0.54229477
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97918 * 0.25565193
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29604 * 0.99997723
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13367 * 0.01141691
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30539 * 0.45520038
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11352 * 0.14163341
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 946 * 0.65964630
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 85762 * 0.38419848
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 28858 * 0.01481402
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'csouyeyq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0025():
    """Extended test 25 for aggregation."""
    x_0 = 89509 * 0.50963229
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34767 * 0.55659827
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82254 * 0.35414970
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31118 * 0.47096580
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14776 * 0.95165456
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75970 * 0.02482153
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51623 * 0.23660042
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73099 * 0.49265242
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75594 * 0.44544488
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19003 * 0.87534404
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4008 * 0.66808440
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49037 * 0.02053709
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98797 * 0.87644704
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51189 * 0.82854018
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96088 * 0.19481501
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2682 * 0.66625705
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6205 * 0.00975884
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76619 * 0.68295962
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39356 * 0.80367113
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43348 * 0.60851311
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27162 * 0.51178014
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29495 * 0.33696429
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26338 * 0.60154093
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39220 * 0.18482187
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'tffomdhf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0026():
    """Extended test 26 for aggregation."""
    x_0 = 68435 * 0.81953685
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67490 * 0.62703609
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77528 * 0.97585397
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71720 * 0.45792896
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46257 * 0.17546610
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17834 * 0.01995349
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79846 * 0.29674465
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49154 * 0.19278523
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73787 * 0.65679768
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63790 * 0.79550120
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74333 * 0.04400253
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91144 * 0.91313410
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42974 * 0.35205717
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86958 * 0.90017453
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5767 * 0.47112952
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66002 * 0.76289072
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55090 * 0.56355212
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72664 * 0.68093190
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4782 * 0.73077993
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48502 * 0.57209659
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73968 * 0.03035213
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13265 * 0.03476359
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63701 * 0.25144421
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72567 * 0.13206109
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87648 * 0.15279280
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53489 * 0.26068555
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83602 * 0.97150400
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15082 * 0.35022369
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12687 * 0.08041694
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32564 * 0.34688536
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49035 * 0.56767806
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63624 * 0.91772495
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8767 * 0.87867851
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80261 * 0.20618234
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56056 * 0.61579908
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78131 * 0.47970498
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21530 * 0.99417520
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69813 * 0.92293021
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36290 * 0.62013471
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41208 * 0.58549731
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2183 * 0.18929914
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3814 * 0.74827026
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46985 * 0.19007127
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83736 * 0.41371309
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86138 * 0.87848561
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 37421 * 0.31314924
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 10908 * 0.64517612
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 62624 * 0.39512487
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'qplivvjt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0027():
    """Extended test 27 for aggregation."""
    x_0 = 42381 * 0.66388484
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38033 * 0.82713755
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94423 * 0.62227350
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32711 * 0.39258528
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4886 * 0.71141329
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64474 * 0.75012490
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80129 * 0.60775590
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29084 * 0.08518774
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49357 * 0.36083134
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55605 * 0.67057259
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66937 * 0.69999020
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73516 * 0.72643993
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43585 * 0.75617210
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41229 * 0.07065692
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2114 * 0.04723894
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85222 * 0.04537851
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26390 * 0.91087559
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7614 * 0.04700757
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6680 * 0.54551841
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77003 * 0.03916788
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52154 * 0.52495861
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 428 * 0.46004200
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89679 * 0.19654022
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70410 * 0.70554005
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5109 * 0.14466186
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74633 * 0.11468055
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93128 * 0.41635928
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84935 * 0.53298685
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12189 * 0.11663806
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88817 * 0.14003555
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73977 * 0.16116024
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ijbafvqm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0028():
    """Extended test 28 for aggregation."""
    x_0 = 8969 * 0.06839731
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81695 * 0.95237787
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76949 * 0.46532993
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17803 * 0.23562158
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52626 * 0.35940186
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92319 * 0.63200187
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83888 * 0.13071322
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70709 * 0.12068658
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27153 * 0.43023717
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75491 * 0.71774543
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7044 * 0.00597512
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4185 * 0.65141845
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3717 * 0.87883399
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39138 * 0.35546434
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13013 * 0.21558456
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25381 * 0.60893039
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77809 * 0.27660860
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1794 * 0.10455004
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52458 * 0.53132393
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77290 * 0.20360584
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70020 * 0.99701827
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54729 * 0.46084165
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42605 * 0.38225523
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11234 * 0.02299931
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4388 * 0.31661942
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96252 * 0.80815953
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78966 * 0.22526080
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75611 * 0.56750492
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92083 * 0.01545537
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30954 * 0.62225701
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60495 * 0.12081844
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53525 * 0.50723462
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72044 * 0.09325454
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6168 * 0.32280664
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92311 * 0.91754224
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45279 * 0.79304334
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9840 * 0.56258342
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 57940 * 0.91054552
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61985 * 0.66592075
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 78777 * 0.19521416
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94381 * 0.73688500
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66906 * 0.60534770
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 40895 * 0.83551623
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 68111 * 0.16056384
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 38440 * 0.39788213
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 96943 * 0.88213932
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 28424 * 0.30988554
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'purtrkyj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0029():
    """Extended test 29 for aggregation."""
    x_0 = 80186 * 0.70101779
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12535 * 0.79045288
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49237 * 0.99341847
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60244 * 0.43951997
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91173 * 0.88065195
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74821 * 0.28288888
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36502 * 0.02861508
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66073 * 0.17352837
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41558 * 0.02860427
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26727 * 0.14053987
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75191 * 0.46385622
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66011 * 0.73137335
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6290 * 0.89687525
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32216 * 0.51013111
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 764 * 0.59726418
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72281 * 0.78423629
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70124 * 0.48804762
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12187 * 0.72892379
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63451 * 0.44958085
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21519 * 0.41575611
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41856 * 0.31683098
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60725 * 0.43906570
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77607 * 0.89456863
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29892 * 0.13218791
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99738 * 0.29974182
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64379 * 0.45064591
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23561 * 0.84605945
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31751 * 0.16527296
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47684 * 0.58807148
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83082 * 0.64323949
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73752 * 0.47786092
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6956 * 0.23320620
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13465 * 0.60316671
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5702 * 0.70993967
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7446 * 0.41462835
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89464 * 0.42332340
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29846 * 0.51351813
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39820 * 0.67726673
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72716 * 0.33175634
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30119 * 0.71229913
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84446 * 0.69801211
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71057 * 0.99772062
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46983 * 0.24404431
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88018 * 0.89216342
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 88833 * 0.93966579
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 51828 * 0.14274746
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'hplizsdh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0030():
    """Extended test 30 for aggregation."""
    x_0 = 87801 * 0.51310035
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77747 * 0.17926683
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29620 * 0.78867552
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11619 * 0.67909964
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10157 * 0.79569444
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38997 * 0.08217035
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26223 * 0.91574324
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68712 * 0.24972248
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35786 * 0.99525891
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11604 * 0.04033023
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95592 * 0.82048000
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35248 * 0.47169111
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15905 * 0.86318757
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50595 * 0.62596586
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13354 * 0.67384470
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61634 * 0.77069318
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19236 * 0.57922345
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49977 * 0.31514549
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2285 * 0.30687664
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80045 * 0.12865575
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86929 * 0.46783558
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49190 * 0.02770907
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2109 * 0.26939211
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18478 * 0.64382336
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60346 * 0.25031865
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72923 * 0.22736953
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41100 * 0.66615942
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83500 * 0.55596361
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36601 * 0.66673305
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53895 * 0.82607789
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89931 * 0.28580795
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40418 * 0.74455857
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17762 * 0.29816972
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58518 * 0.41265673
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83445 * 0.29316218
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86259 * 0.29376947
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47670 * 0.97339064
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45972 * 0.64443580
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30484 * 0.95810945
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 35568 * 0.08857290
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 63345 * 0.26241982
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'wccqvpbn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0031():
    """Extended test 31 for aggregation."""
    x_0 = 33941 * 0.81427258
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59852 * 0.09236733
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93063 * 0.91781816
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55440 * 0.54890315
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27 * 0.65472764
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8952 * 0.63842339
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83450 * 0.95897420
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86402 * 0.26497397
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12286 * 0.44486016
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27609 * 0.77170968
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64100 * 0.14265526
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4013 * 0.60442981
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21543 * 0.81742843
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51499 * 0.40689128
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63513 * 0.80456469
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68419 * 0.64453283
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69111 * 0.53189129
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51992 * 0.73041766
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94633 * 0.35814943
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46868 * 0.09479445
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25887 * 0.73656806
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84134 * 0.35787931
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36465 * 0.14795420
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17221 * 0.45076279
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75613 * 0.36676138
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38706 * 0.44652828
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53395 * 0.50617456
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95185 * 0.13959693
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'kpuwrxwt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0032():
    """Extended test 32 for aggregation."""
    x_0 = 20888 * 0.98346361
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52046 * 0.49601861
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31279 * 0.12618368
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58938 * 0.29680458
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51748 * 0.37454722
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30250 * 0.00082194
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16635 * 0.60593972
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63419 * 0.61121168
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73410 * 0.15870335
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 821 * 0.43438575
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70130 * 0.77303943
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75098 * 0.13807174
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7813 * 0.11980916
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32109 * 0.75963524
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82148 * 0.37807357
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4398 * 0.30734917
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81142 * 0.91567089
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40657 * 0.92914970
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81569 * 0.66620044
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6867 * 0.48495926
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21409 * 0.96379316
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19854 * 0.57029522
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20054 * 0.03928152
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29340 * 0.93119338
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26617 * 0.35780765
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59381 * 0.34541716
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48633 * 0.55257929
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96440 * 0.60497109
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89511 * 0.96004846
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64479 * 0.69916088
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54950 * 0.21055994
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44944 * 0.77368826
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88719 * 0.83502291
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82349 * 0.15490421
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8025 * 0.15741552
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35480 * 0.16740400
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15778 * 0.72867177
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97038 * 0.92879548
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56444 * 0.61019411
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69821 * 0.92311504
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 61455 * 0.95862878
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13696 * 0.77508332
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24573 * 0.74544444
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27188 * 0.22033933
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 63197 * 0.30103003
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 71129 * 0.94957908
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 22739 * 0.18263771
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 92117 * 0.45676461
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'lcttotrb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0033():
    """Extended test 33 for aggregation."""
    x_0 = 36089 * 0.69266682
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26299 * 0.24162514
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85777 * 0.39596335
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48500 * 0.98552140
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77598 * 0.89413388
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32005 * 0.38332234
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1367 * 0.79206969
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66126 * 0.38865005
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21765 * 0.60956248
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45908 * 0.16063771
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98994 * 0.90984425
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98323 * 0.78181311
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9186 * 0.31884921
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3962 * 0.42941262
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38043 * 0.86478719
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43912 * 0.96551184
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34354 * 0.81656470
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30985 * 0.94206273
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18528 * 0.85046129
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17857 * 0.14743469
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71217 * 0.98168527
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51359 * 0.03749340
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4096 * 0.53872158
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93794 * 0.29173285
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75168 * 0.52927422
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41621 * 0.06692583
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64661 * 0.22488467
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40913 * 0.40501066
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4142 * 0.24452977
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38781 * 0.11917808
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ricojojz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0034():
    """Extended test 34 for aggregation."""
    x_0 = 62172 * 0.87019041
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12057 * 0.76202374
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40860 * 0.11043288
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67111 * 0.44265364
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95034 * 0.74382575
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87673 * 0.83446670
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28697 * 0.66493101
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19543 * 0.28414841
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66466 * 0.10488747
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99636 * 0.99469908
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12054 * 0.98785272
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63273 * 0.08011997
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37826 * 0.54152305
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65792 * 0.56989074
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90616 * 0.80053026
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5682 * 0.21195655
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98955 * 0.56204887
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69588 * 0.38062574
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1791 * 0.73367516
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29897 * 0.00896471
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44311 * 0.89597779
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60382 * 0.11085613
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66441 * 0.33480722
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96772 * 0.27538050
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85787 * 0.71256093
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94927 * 0.62636922
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86272 * 0.43777006
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 605 * 0.47408957
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28505 * 0.02651661
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8770 * 0.04552205
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24074 * 0.70570134
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'rmgzbpce').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0035():
    """Extended test 35 for aggregation."""
    x_0 = 33973 * 0.33249478
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12934 * 0.66992371
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8120 * 0.86089912
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65371 * 0.78237407
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11005 * 0.96864876
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75795 * 0.54070659
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74007 * 0.27531251
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19264 * 0.46937442
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86290 * 0.06224606
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36082 * 0.04862945
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31533 * 0.74527333
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90161 * 0.92267798
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87724 * 0.81142963
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97182 * 0.83107782
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39344 * 0.23206009
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72238 * 0.09584427
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77045 * 0.44347800
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61861 * 0.56642935
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73557 * 0.33228703
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18252 * 0.31296691
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40984 * 0.38804071
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20577 * 0.07873223
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91232 * 0.04658543
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25780 * 0.10215022
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40381 * 0.90403489
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82236 * 0.98008667
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44201 * 0.05396102
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70276 * 0.83724569
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58051 * 0.34020580
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66 * 0.70105806
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 514 * 0.47442194
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91146 * 0.13797934
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72015 * 0.87650351
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84260 * 0.38439214
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78032 * 0.21191793
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50443 * 0.05448576
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45575 * 0.86492549
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78032 * 0.56262301
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93451 * 0.92939871
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'zpkydrio').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0036():
    """Extended test 36 for aggregation."""
    x_0 = 4708 * 0.00704081
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64838 * 0.53469867
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26597 * 0.25580743
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73987 * 0.16576127
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53371 * 0.56355155
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43488 * 0.66029128
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94440 * 0.21860188
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4315 * 0.96666500
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53813 * 0.35720039
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29717 * 0.18904232
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32198 * 0.26743060
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5274 * 0.55355688
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69919 * 0.18404270
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59876 * 0.33004231
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67922 * 0.50507661
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52613 * 0.64862522
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12841 * 0.80319838
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72196 * 0.84250711
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93372 * 0.90144974
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58223 * 0.08734854
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83332 * 0.53721969
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14552 * 0.53282352
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54297 * 0.44714482
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37019 * 0.34283331
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28298 * 0.04798667
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96696 * 0.51393454
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2914 * 0.72728138
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68922 * 0.20528961
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10281 * 0.54907200
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49817 * 0.41376258
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'lnshpbcd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0037():
    """Extended test 37 for aggregation."""
    x_0 = 68846 * 0.70821697
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98405 * 0.07772506
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49882 * 0.32522996
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67866 * 0.29052416
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84817 * 0.81636949
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72922 * 0.31690797
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23385 * 0.85189087
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90284 * 0.64657854
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31215 * 0.49972107
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94344 * 0.18959602
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87239 * 0.87958555
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88235 * 0.82325573
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57154 * 0.53369585
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86481 * 0.79596455
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76666 * 0.34300446
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10783 * 0.06093007
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3660 * 0.81018782
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75816 * 0.88057265
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93560 * 0.95815000
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48287 * 0.94662950
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6722 * 0.59357937
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50197 * 0.33518819
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50107 * 0.31851672
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42471 * 0.25317125
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42839 * 0.83177808
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1808 * 0.61399971
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29824 * 0.82309465
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44706 * 0.70526758
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72585 * 0.23123930
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60698 * 0.39955646
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21318 * 0.50330976
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58899 * 0.10669087
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28432 * 0.76470435
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25085 * 0.95211080
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'omvxngvm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0038():
    """Extended test 38 for aggregation."""
    x_0 = 86531 * 0.94230255
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50224 * 0.03929780
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37134 * 0.22634205
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34998 * 0.58609321
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91920 * 0.88836432
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96848 * 0.16265764
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2884 * 0.60749111
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33412 * 0.08837849
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87768 * 0.74051962
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10532 * 0.16055453
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58809 * 0.53161565
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90635 * 0.84617951
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72230 * 0.60961711
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38308 * 0.34458899
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60108 * 0.78920150
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89903 * 0.41995144
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61753 * 0.12951497
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84826 * 0.27243993
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74982 * 0.19600146
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33092 * 0.95636185
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14842 * 0.15817053
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87942 * 0.47115794
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35157 * 0.74530018
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4087 * 0.68450049
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91328 * 0.92963181
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57117 * 0.27552192
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13103 * 0.22667813
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5188 * 0.25237173
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34371 * 0.01004662
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18967 * 0.66125203
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38705 * 0.04319194
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27083 * 0.20406804
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70631 * 0.81001184
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19465 * 0.21261802
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79096 * 0.04024530
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74856 * 0.36030983
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72175 * 0.08192090
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40493 * 0.53242798
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24008 * 0.10287103
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76659 * 0.22576776
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 72602 * 0.00653216
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 2318 * 0.74181327
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71708 * 0.87010917
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'fzfvzdck').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0039():
    """Extended test 39 for aggregation."""
    x_0 = 70343 * 0.22461747
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92126 * 0.34746144
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15744 * 0.23760525
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62629 * 0.67393443
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55650 * 0.12364873
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75180 * 0.69368646
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92122 * 0.98225869
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6037 * 0.24410421
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69356 * 0.81603136
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43027 * 0.56368964
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32646 * 0.72389619
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22442 * 0.51486597
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64771 * 0.18012505
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42464 * 0.83822351
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18061 * 0.40467187
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50079 * 0.88176826
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46239 * 0.12561050
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20254 * 0.37889266
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18844 * 0.79259648
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50390 * 0.56422640
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11270 * 0.37792072
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9651 * 0.16204208
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79020 * 0.58593175
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2175 * 0.80715736
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76342 * 0.69561732
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15679 * 0.14267621
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41099 * 0.20277886
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12788 * 0.63398297
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20433 * 0.10471282
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94944 * 0.13147020
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94210 * 0.95481644
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60949 * 0.92242879
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11637 * 0.81674764
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2429 * 0.23868145
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78547 * 0.18953913
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'sscekohx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0040():
    """Extended test 40 for aggregation."""
    x_0 = 17179 * 0.18154344
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11840 * 0.02829566
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83967 * 0.32766332
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60259 * 0.51724342
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76911 * 0.94316657
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50725 * 0.76651171
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33322 * 0.70554250
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62493 * 0.22925506
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32097 * 0.57110463
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59845 * 0.29853873
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33487 * 0.72623774
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64591 * 0.76297148
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93041 * 0.45409302
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30648 * 0.98903484
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33695 * 0.44788200
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 809 * 0.77880426
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47856 * 0.70535977
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20934 * 0.32601105
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65410 * 0.35345908
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58561 * 0.28536113
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3186 * 0.03233905
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58166 * 0.08998057
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41015 * 0.08441189
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52290 * 0.98020800
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13423 * 0.58635735
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53764 * 0.45883973
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9688 * 0.83422254
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11971 * 0.57804838
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53198 * 0.01554558
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93141 * 0.07126253
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44970 * 0.92290309
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'evuahyyq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0041():
    """Extended test 41 for aggregation."""
    x_0 = 43398 * 0.48242212
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84867 * 0.86685511
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12358 * 0.17696363
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81900 * 0.90714721
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12092 * 0.16758728
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40486 * 0.35232621
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60997 * 0.54836716
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16320 * 0.67052716
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59151 * 0.37835908
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39473 * 0.35861820
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90611 * 0.19197991
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85749 * 0.16298296
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78584 * 0.45709844
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94477 * 0.98074805
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99671 * 0.80654074
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90311 * 0.56218616
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56681 * 0.78270268
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93751 * 0.23312936
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53016 * 0.43130130
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8009 * 0.00391156
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4840 * 0.51040760
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81192 * 0.11565855
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99358 * 0.29165901
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99452 * 0.41172488
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86467 * 0.81080831
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41874 * 0.08439774
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55057 * 0.69589669
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85928 * 0.14152184
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28519 * 0.42638349
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 527 * 0.32512804
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76571 * 0.76545909
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22967 * 0.30378660
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59702 * 0.26348840
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4597 * 0.52190033
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79155 * 0.32136376
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71038 * 0.75846867
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78213 * 0.98151104
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62082 * 0.40234807
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'shiesvzr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0042():
    """Extended test 42 for aggregation."""
    x_0 = 68483 * 0.38709407
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41612 * 0.51874979
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91020 * 0.84715629
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69906 * 0.86242000
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77815 * 0.85338427
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17567 * 0.03943944
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99862 * 0.89461761
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63963 * 0.98917819
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65886 * 0.67850866
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82811 * 0.07668394
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96875 * 0.09612504
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38745 * 0.74153002
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65817 * 0.76050356
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86463 * 0.86619678
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42528 * 0.30034671
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49826 * 0.58249511
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92504 * 0.31816491
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39361 * 0.16175089
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5724 * 0.10617097
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98754 * 0.85843543
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83003 * 0.96772621
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54317 * 0.54260369
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73964 * 0.43204976
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50125 * 0.27150090
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94549 * 0.50730824
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68098 * 0.34251379
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48206 * 0.83092756
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22102 * 0.64563031
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65031 * 0.69908541
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11358 * 0.40160602
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50261 * 0.97297241
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93731 * 0.39044534
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76525 * 0.28724450
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16783 * 0.79891256
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90135 * 0.20757486
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80731 * 0.78573344
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84426 * 0.50019340
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'sawulstx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0043():
    """Extended test 43 for aggregation."""
    x_0 = 30723 * 0.84598668
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90102 * 0.25394569
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76468 * 0.34704830
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96506 * 0.74130040
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40718 * 0.19586122
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39791 * 0.14016160
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36569 * 0.59627965
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28689 * 0.76353269
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99355 * 0.79758874
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64078 * 0.78201569
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28698 * 0.40184668
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60960 * 0.47455130
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 998 * 0.60893210
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8383 * 0.72629459
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69743 * 0.63204393
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95187 * 0.61978812
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5503 * 0.89252510
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4308 * 0.29630717
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33667 * 0.12073669
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6095 * 0.24646364
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57384 * 0.54559302
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22466 * 0.19276219
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2206 * 0.48215527
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32517 * 0.57848775
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4301 * 0.31785651
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70630 * 0.89417933
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36672 * 0.95175332
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70564 * 0.50181683
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58022 * 0.97628251
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70179 * 0.59263263
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20622 * 0.69395034
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62569 * 0.64519246
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27099 * 0.05797771
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'neuajnuw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0044():
    """Extended test 44 for aggregation."""
    x_0 = 37720 * 0.48067703
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29940 * 0.42643472
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25846 * 0.10969122
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86813 * 0.60503469
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74767 * 0.39726288
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23633 * 0.38554917
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92415 * 0.48058368
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96694 * 0.18126029
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16448 * 0.08444248
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22933 * 0.45987693
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54717 * 0.64795170
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89799 * 0.16831666
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8323 * 0.04944439
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25203 * 0.63377620
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55418 * 0.28977667
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78062 * 0.50290907
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70545 * 0.49503306
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8202 * 0.29330643
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49173 * 0.07696200
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60319 * 0.29720303
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2795 * 0.56232254
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43076 * 0.63511431
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61793 * 0.80893111
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38020 * 0.35922514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1632 * 0.98062318
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33274 * 0.18092494
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70761 * 0.74030108
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23260 * 0.65469933
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2858 * 0.71405188
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37270 * 0.16697955
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'mxncvzhl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0045():
    """Extended test 45 for aggregation."""
    x_0 = 46640 * 0.08745081
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25453 * 0.50342612
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85487 * 0.25432197
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13898 * 0.47835419
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4552 * 0.52030937
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92117 * 0.55707204
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92004 * 0.13590068
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59364 * 0.07829622
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67077 * 0.33235448
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36872 * 0.93520504
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22471 * 0.30111437
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37582 * 0.55345611
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56816 * 0.72664627
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14739 * 0.36494539
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55344 * 0.26137278
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76861 * 0.31119060
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86977 * 0.13854486
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53468 * 0.54559286
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86734 * 0.68703410
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68105 * 0.66844135
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 380 * 0.28551946
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69098 * 0.85365499
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59238 * 0.82599444
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8786 * 0.35092997
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97382 * 0.95278980
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77362 * 0.10330550
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97828 * 0.46140811
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60204 * 0.44069175
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17993 * 0.74194455
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82717 * 0.07865910
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ahdffwgh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0046():
    """Extended test 46 for aggregation."""
    x_0 = 16390 * 0.16491667
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29862 * 0.29016889
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39787 * 0.71523369
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47892 * 0.15863418
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6191 * 0.14347114
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40780 * 0.75402762
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10927 * 0.58710463
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20828 * 0.83606456
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37589 * 0.01974883
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64105 * 0.01879318
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65383 * 0.24428278
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84491 * 0.58500521
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27958 * 0.77633831
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88240 * 0.05551196
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42447 * 0.42088049
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83706 * 0.25435055
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87807 * 0.10444647
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20466 * 0.74245254
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51485 * 0.18947535
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18975 * 0.91667687
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74012 * 0.22659353
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80866 * 0.11147196
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95831 * 0.94289673
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69411 * 0.98861133
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34 * 0.81526607
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55151 * 0.75875760
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68937 * 0.48010141
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39884 * 0.92183618
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70519 * 0.61125010
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82264 * 0.77532581
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32582 * 0.74227908
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6528 * 0.23524823
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74531 * 0.80637619
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1021 * 0.89067754
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19989 * 0.02359714
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83456 * 0.04247163
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42520 * 0.69882167
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'wfmcwvbl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0047():
    """Extended test 47 for aggregation."""
    x_0 = 4792 * 0.02787854
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76918 * 0.78384662
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93762 * 0.79187118
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49330 * 0.91998333
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15852 * 0.87890163
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75893 * 0.84294338
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97364 * 0.28031554
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32915 * 0.86133797
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42368 * 0.33940569
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43895 * 0.05893708
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27341 * 0.61032201
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88936 * 0.98579384
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27445 * 0.04429580
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96035 * 0.05514363
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30913 * 0.17434842
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5645 * 0.55235552
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99235 * 0.90923307
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88053 * 0.36552858
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12494 * 0.61066781
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64171 * 0.26692425
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33190 * 0.00333616
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1389 * 0.66407579
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19970 * 0.54244527
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32528 * 0.57147706
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96417 * 0.08910843
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67786 * 0.65498473
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34981 * 0.71675799
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60712 * 0.22052714
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12189 * 0.18542715
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30786 * 0.50700455
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98636 * 0.96939929
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62611 * 0.26042948
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6814 * 0.82213217
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91455 * 0.71337363
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42176 * 0.47732958
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28128 * 0.65482418
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24195 * 0.98297861
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36241 * 0.05660511
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74029 * 0.47905736
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44419 * 0.27809801
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11411 * 0.32075543
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4331 * 0.77018005
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 37104 * 0.27177231
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 67726 * 0.04496489
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 3203 * 0.81418977
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 5937 * 0.05716137
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 40564 * 0.46167467
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 24324 * 0.03760500
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'epqcsnhg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0048():
    """Extended test 48 for aggregation."""
    x_0 = 64474 * 0.57713631
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51476 * 0.51471933
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53470 * 0.02033357
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25539 * 0.10757574
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99983 * 0.97561192
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96418 * 0.76811798
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76786 * 0.24464315
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91577 * 0.35608220
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85344 * 0.39582342
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30898 * 0.13589804
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17657 * 0.04106501
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50416 * 0.54217948
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29200 * 0.93989530
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46525 * 0.89872479
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34822 * 0.66786570
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74735 * 0.81940874
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75528 * 0.96955706
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32068 * 0.04966330
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96015 * 0.81874235
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85072 * 0.04346037
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 689 * 0.52142494
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42109 * 0.53456722
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50727 * 0.85321435
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78596 * 0.65373502
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77214 * 0.56585312
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33161 * 0.36476779
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5729 * 0.43606897
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71448 * 0.76743240
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6745 * 0.14641055
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10804 * 0.03505934
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57591 * 0.18265048
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19797 * 0.63775996
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84967 * 0.80415190
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52981 * 0.97668561
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 968 * 0.14379529
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40977 * 0.50167477
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28276 * 0.95579665
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52882 * 0.04073686
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43905 * 0.05505669
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54532 * 0.12809162
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38981 * 0.33849685
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 19666 * 0.45945052
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93736 * 0.34211098
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 74144 * 0.39384593
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 85887 * 0.98196761
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 62709 * 0.55750653
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'hhypsgpl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0049():
    """Extended test 49 for aggregation."""
    x_0 = 66672 * 0.68724011
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52462 * 0.29301798
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28020 * 0.86293712
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53019 * 0.71925958
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42903 * 0.03646658
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18624 * 0.78445932
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32523 * 0.74505482
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5779 * 0.74490540
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95992 * 0.37337870
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39251 * 0.83966794
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76264 * 0.97783554
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3151 * 0.83689475
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20072 * 0.90741062
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17071 * 0.35720551
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70789 * 0.61982713
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82922 * 0.91863449
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34259 * 0.14309257
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3722 * 0.50079660
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13612 * 0.82575724
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45591 * 0.04409339
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59226 * 0.99794580
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'uynigvey').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0050():
    """Extended test 50 for aggregation."""
    x_0 = 47985 * 0.45712296
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12985 * 0.88003233
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86702 * 0.54401488
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72243 * 0.55293513
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25312 * 0.22252241
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36022 * 0.81849883
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65822 * 0.54114375
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 940 * 0.91877414
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74489 * 0.73732604
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78701 * 0.31347945
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91050 * 0.30470943
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40648 * 0.86630508
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65989 * 0.22934393
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69984 * 0.41154277
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37189 * 0.50993792
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43597 * 0.55491390
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37715 * 0.69889438
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11821 * 0.80039868
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68681 * 0.03038749
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3662 * 0.85329481
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35417 * 0.23963615
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23048 * 0.91234865
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77330 * 0.99077679
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42218 * 0.22578581
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ltkhylte').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0051():
    """Extended test 51 for aggregation."""
    x_0 = 9176 * 0.20497159
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19010 * 0.23093673
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96609 * 0.55823518
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39911 * 0.20010868
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33117 * 0.34470653
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30116 * 0.22033598
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47433 * 0.96785165
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74654 * 0.42092914
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3739 * 0.78053411
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56989 * 0.58844786
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67046 * 0.40169419
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74797 * 0.05597671
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28352 * 0.26799748
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1074 * 0.87307469
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53548 * 0.77850901
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41250 * 0.35230863
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9532 * 0.35218015
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40341 * 0.54713225
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19025 * 0.39694632
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2670 * 0.04449112
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72351 * 0.14957121
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61836 * 0.79057159
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20622 * 0.89613787
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78174 * 0.94011100
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99880 * 0.41484188
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35889 * 0.63839330
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96842 * 0.90848087
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'srkgxvmk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0052():
    """Extended test 52 for aggregation."""
    x_0 = 80852 * 0.56480325
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98303 * 0.93682523
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93138 * 0.27978161
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72180 * 0.82813119
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45589 * 0.87504947
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42486 * 0.15800628
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73104 * 0.64308478
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48862 * 0.98728655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50741 * 0.30488903
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11894 * 0.33116441
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22679 * 0.41569942
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8885 * 0.74866227
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17385 * 0.72418003
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65723 * 0.48535925
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5802 * 0.13192454
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26393 * 0.99135855
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11288 * 0.87332460
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56800 * 0.55405781
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86843 * 0.91806612
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17115 * 0.03225001
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22281 * 0.23265481
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37051 * 0.68334115
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41717 * 0.51814679
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23511 * 0.51112313
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85000 * 0.01833748
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74528 * 0.64885101
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11742 * 0.62130754
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22115 * 0.73897123
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'bjpiydca').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0053():
    """Extended test 53 for aggregation."""
    x_0 = 74942 * 0.14596243
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47920 * 0.10558680
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15283 * 0.06136811
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47124 * 0.97980654
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20046 * 0.80826483
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64524 * 0.11853152
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11313 * 0.44330832
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35729 * 0.54019901
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4826 * 0.40171335
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88514 * 0.89304724
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3620 * 0.16810444
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84178 * 0.58318385
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80537 * 0.89737482
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2488 * 0.67588818
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83335 * 0.75602363
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54374 * 0.60765459
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89007 * 0.24915162
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96322 * 0.07278328
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37259 * 0.36988538
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57949 * 0.60342290
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8113 * 0.36754707
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95953 * 0.60805285
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78838 * 0.35556871
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7095 * 0.16994705
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20681 * 0.37731961
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12795 * 0.15309958
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64547 * 0.72973752
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95160 * 0.32244248
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80797 * 0.73437500
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83541 * 0.49669433
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91509 * 0.33962137
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15608 * 0.28271541
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17686 * 0.36894358
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72859 * 0.51369038
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63006 * 0.57157397
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28644 * 0.00754628
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51387 * 0.59553751
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45152 * 0.25344577
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65778 * 0.66959079
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 50156 * 0.75034425
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80867 * 0.79913238
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60828 * 0.04748435
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'khmnvmil').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0054():
    """Extended test 54 for aggregation."""
    x_0 = 38832 * 0.78563012
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10679 * 0.96403061
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45067 * 0.70912933
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68081 * 0.41992189
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63558 * 0.16966992
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98248 * 0.19398416
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57952 * 0.10170303
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54768 * 0.40625454
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69599 * 0.31989839
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26082 * 0.67247727
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40643 * 0.42043658
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54146 * 0.51829913
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59955 * 0.16388449
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54490 * 0.79017512
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7398 * 0.24320099
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22969 * 0.64269696
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45242 * 0.60336282
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14316 * 0.58226313
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17874 * 0.58307477
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48791 * 0.41504143
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87237 * 0.51952995
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10514 * 0.85737239
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3874 * 0.34610376
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'lzgjwpng').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0055():
    """Extended test 55 for aggregation."""
    x_0 = 32354 * 0.84546692
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67780 * 0.33341080
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56230 * 0.84906221
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71890 * 0.55813959
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61653 * 0.92025058
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57482 * 0.06392048
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69774 * 0.76417443
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47882 * 0.75810494
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92013 * 0.19241365
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82837 * 0.65260487
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66842 * 0.82649318
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 726 * 0.59739590
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74461 * 0.30965274
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27441 * 0.44096438
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88087 * 0.98582581
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64965 * 0.92571138
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89580 * 0.59998441
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67682 * 0.30775187
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24930 * 0.34319462
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62717 * 0.97023895
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30500 * 0.15120058
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11841 * 0.06344229
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23778 * 0.94099193
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80439 * 0.12922230
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52870 * 0.92838852
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89804 * 0.02329190
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39179 * 0.72826191
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61072 * 0.83452359
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2718 * 0.71104874
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86775 * 0.78696407
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98310 * 0.74276688
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15397 * 0.52250004
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61477 * 0.43931780
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6434 * 0.93334401
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42161 * 0.75378258
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10797 * 0.67794919
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57763 * 0.09857032
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16877 * 0.72089841
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ujimlytm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0056():
    """Extended test 56 for aggregation."""
    x_0 = 94798 * 0.07143558
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87117 * 0.91047186
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67426 * 0.57475610
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76190 * 0.39381419
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 768 * 0.31754285
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70582 * 0.36031116
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68479 * 0.14097869
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3417 * 0.85444465
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27428 * 0.83322434
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62002 * 0.43469149
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95526 * 0.14070497
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93206 * 0.69759456
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50933 * 0.61248364
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84238 * 0.24626992
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30639 * 0.90784425
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30912 * 0.04529987
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82187 * 0.16430390
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39984 * 0.17978402
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63600 * 0.48193777
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75119 * 0.18564800
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93724 * 0.57734819
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42676 * 0.81265934
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69790 * 0.81200245
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52549 * 0.70413352
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59007 * 0.11058202
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25519 * 0.35315275
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97164 * 0.93718152
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4676 * 0.01059973
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64062 * 0.81671034
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9337 * 0.75292098
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26788 * 0.89169123
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98520 * 0.04470968
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85234 * 0.29670166
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15272 * 0.11008521
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11900 * 0.97203800
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43263 * 0.94946727
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34033 * 0.59631872
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21171 * 0.46040300
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58042 * 0.61216025
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23658 * 0.80920520
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18340 * 0.40334996
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 2328 * 0.43509998
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'prabihbm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0057():
    """Extended test 57 for aggregation."""
    x_0 = 7847 * 0.48206884
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81175 * 0.55005987
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4407 * 0.75618716
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37106 * 0.36863674
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18065 * 0.29904840
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46466 * 0.58382021
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1465 * 0.43369870
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85318 * 0.40817542
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23781 * 0.48275334
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50406 * 0.43310246
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31412 * 0.35855896
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61346 * 0.80351373
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8886 * 0.93419691
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1610 * 0.11553483
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53348 * 0.56875106
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91509 * 0.16240953
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88541 * 0.82564325
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41787 * 0.90999370
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31001 * 0.13045855
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24840 * 0.81339572
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41639 * 0.97870763
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30851 * 0.22811043
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51907 * 0.15214339
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16544 * 0.73827415
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62429 * 0.74495427
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25604 * 0.10153101
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83511 * 0.47055503
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38969 * 0.78238846
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2042 * 0.45097386
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54171 * 0.01082029
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28351 * 0.80439278
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62612 * 0.10892546
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'zggzuozv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0058():
    """Extended test 58 for aggregation."""
    x_0 = 18580 * 0.34154920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77039 * 0.09188144
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16035 * 0.22942423
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65868 * 0.58742989
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48349 * 0.97871227
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51429 * 0.05702900
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33076 * 0.74383070
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7910 * 0.50559839
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91862 * 0.53908144
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94249 * 0.26614809
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38956 * 0.07566909
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7664 * 0.36036281
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38614 * 0.67320714
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94701 * 0.47812869
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91633 * 0.73125908
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82781 * 0.24703920
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33674 * 0.84108720
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57284 * 0.66009171
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42719 * 0.52599444
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11986 * 0.14954573
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29690 * 0.06963896
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60779 * 0.75575772
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34289 * 0.75829992
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23134 * 0.97646190
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18566 * 0.48210931
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75941 * 0.84941538
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25665 * 0.30392970
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87553 * 0.83583467
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12522 * 0.36642274
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58635 * 0.43866444
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80593 * 0.67090670
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'smslupvy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0059():
    """Extended test 59 for aggregation."""
    x_0 = 35356 * 0.09213758
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71717 * 0.10605792
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8297 * 0.79741122
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67801 * 0.93838790
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6411 * 0.30580528
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50154 * 0.68330416
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31540 * 0.15040404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18028 * 0.73220688
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2729 * 0.57207244
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81237 * 0.23648325
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30476 * 0.82595531
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83012 * 0.47604410
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17865 * 0.79950382
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24877 * 0.98014962
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13217 * 0.19365111
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70991 * 0.32296802
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 128 * 0.53646106
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44383 * 0.00352884
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35152 * 0.34459123
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50353 * 0.06984744
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43663 * 0.29762829
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16592 * 0.62933125
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20796 * 0.25350062
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67098 * 0.35013660
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6550 * 0.07627712
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52857 * 0.14470601
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'qnoanybd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0060():
    """Extended test 60 for aggregation."""
    x_0 = 71333 * 0.47036171
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64443 * 0.78360867
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84530 * 0.60908197
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3434 * 0.32197417
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53158 * 0.40231893
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82939 * 0.40104764
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49466 * 0.95194791
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25443 * 0.54632840
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90389 * 0.88710636
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30293 * 0.26249356
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72999 * 0.91324681
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3521 * 0.08040807
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7972 * 0.47563006
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59761 * 0.60447345
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26908 * 0.67855995
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18388 * 0.81494742
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51617 * 0.28028129
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85071 * 0.63538632
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15435 * 0.56708938
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51839 * 0.55030633
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83511 * 0.60584242
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48701 * 0.89529520
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21440 * 0.05427123
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42434 * 0.80410499
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98933 * 0.82936426
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19885 * 0.97877051
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87890 * 0.44139029
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72697 * 0.16416756
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78906 * 0.75633963
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47618 * 0.09541082
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35691 * 0.15177844
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84438 * 0.39526228
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27866 * 0.41643084
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15457 * 0.97172418
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21394 * 0.48116022
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3714 * 0.42881887
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'hyckdnub').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0061():
    """Extended test 61 for aggregation."""
    x_0 = 64173 * 0.00857100
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32 * 0.69469863
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76738 * 0.54653246
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74848 * 0.99212905
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87684 * 0.60396491
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61489 * 0.63273720
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77007 * 0.46773550
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15818 * 0.33225108
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97675 * 0.28578381
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 140 * 0.76549744
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7928 * 0.64127382
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59616 * 0.08828159
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54432 * 0.69818261
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3276 * 0.60086567
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7431 * 0.71520932
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67575 * 0.72086357
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68996 * 0.33635468
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36133 * 0.55995944
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11988 * 0.28429729
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57180 * 0.57815616
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79234 * 0.09044082
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58768 * 0.37381532
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89661 * 0.09010925
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29875 * 0.75321875
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72175 * 0.98611574
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70597 * 0.24454024
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97758 * 0.20364698
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94369 * 0.54394516
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58113 * 0.68215896
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3297 * 0.27973278
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40884 * 0.89506612
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3745 * 0.38980435
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32334 * 0.71192892
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25257 * 0.32709441
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3510 * 0.83429571
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47563 * 0.06898009
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35972 * 0.20152395
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33669 * 0.88568071
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74279 * 0.94360061
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1393 * 0.97089864
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 92192 * 0.72976670
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'pwhglxrs').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0062():
    """Extended test 62 for aggregation."""
    x_0 = 78723 * 0.67939250
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44234 * 0.58713918
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8361 * 0.46376626
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70304 * 0.60882089
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54374 * 0.82108120
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25879 * 0.32766247
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2220 * 0.54287358
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73906 * 0.11805275
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77661 * 0.29765540
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60887 * 0.14068157
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94665 * 0.90325837
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93829 * 0.06437117
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 301 * 0.98038252
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50718 * 0.05191686
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78353 * 0.44323050
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72303 * 0.00264817
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6143 * 0.23995776
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63544 * 0.77621527
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27059 * 0.40857538
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53129 * 0.31087782
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81046 * 0.28744195
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91115 * 0.39896394
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98492 * 0.42077016
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59842 * 0.53277659
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70867 * 0.26227368
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84902 * 0.21527207
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13789 * 0.35797875
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54158 * 0.72741121
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49378 * 0.36295498
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31519 * 0.67638051
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67996 * 0.98641237
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'vzywdfzo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0063():
    """Extended test 63 for aggregation."""
    x_0 = 87903 * 0.28312451
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54501 * 0.21530589
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5167 * 0.37189035
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7515 * 0.85364123
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96408 * 0.92386494
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99057 * 0.68236071
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62186 * 0.07983167
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51484 * 0.28727237
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66693 * 0.25955735
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25995 * 0.61287784
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17412 * 0.50316955
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4044 * 0.54366329
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42027 * 0.22391798
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9462 * 0.62448524
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62530 * 0.13210132
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22224 * 0.74382746
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56901 * 0.26379045
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74811 * 0.12354585
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85485 * 0.51407201
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67542 * 0.07690821
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34428 * 0.33935223
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57882 * 0.65288080
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91407 * 0.12104283
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23969 * 0.44136753
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99384 * 0.66076250
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89084 * 0.24013753
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52158 * 0.17618703
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'dcpgvgep').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0064():
    """Extended test 64 for aggregation."""
    x_0 = 83850 * 0.34290657
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7759 * 0.38399742
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81733 * 0.86766064
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57128 * 0.25893698
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63149 * 0.50354131
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23472 * 0.07472387
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1624 * 0.10348545
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78656 * 0.32058433
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59729 * 0.71418549
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1821 * 0.77194105
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35752 * 0.61819439
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36246 * 0.87416252
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11871 * 0.49255381
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36208 * 0.10253360
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49976 * 0.71718993
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25783 * 0.85411262
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13580 * 0.66920065
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92439 * 0.42113518
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69469 * 0.58496724
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50568 * 0.59519347
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9583 * 0.22128314
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9894 * 0.63501124
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11439 * 0.90563626
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15552 * 0.51815717
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8371 * 0.68416619
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73235 * 0.48850875
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35747 * 0.67039873
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17591 * 0.98865850
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2397 * 0.18219585
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70931 * 0.18140862
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12160 * 0.29609238
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87949 * 0.73298701
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82860 * 0.82243048
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23087 * 0.55183569
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78471 * 0.01467020
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53270 * 0.62955640
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45776 * 0.84786945
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45459 * 0.49179001
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72564 * 0.55055597
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43985 * 0.87128663
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74467 * 0.40033610
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18515 * 0.21612047
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 69827 * 0.96759166
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40576 * 0.09761456
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 88920 * 0.13850330
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'kcxsuunh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0065():
    """Extended test 65 for aggregation."""
    x_0 = 79806 * 0.12388281
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51655 * 0.52642294
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62217 * 0.99781364
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19171 * 0.12709022
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52306 * 0.90865993
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35483 * 0.09947332
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87308 * 0.88255801
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93439 * 0.86388744
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44179 * 0.98958809
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34813 * 0.60206862
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46737 * 0.82774501
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62365 * 0.08538817
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17169 * 0.77549584
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47907 * 0.80702320
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15815 * 0.12167253
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12227 * 0.88798116
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35093 * 0.87269795
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22201 * 0.72065779
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86807 * 0.69366003
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43171 * 0.06221694
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33155 * 0.21560292
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91031 * 0.43670314
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24873 * 0.60003461
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36143 * 0.47465289
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21540 * 0.63790446
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73171 * 0.89891675
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74769 * 0.95573693
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5642 * 0.35581798
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65890 * 0.77574846
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72019 * 0.72196229
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91602 * 0.84779127
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8642 * 0.00737168
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1940 * 0.78579183
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92883 * 0.32247297
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95758 * 0.02203768
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4594 * 0.41060664
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12168 * 0.77030130
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66926 * 0.16480979
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34124 * 0.39203245
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64573 * 0.01018087
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 72188 * 0.76100070
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4703 * 0.92373860
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'vsfwwbap').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0066():
    """Extended test 66 for aggregation."""
    x_0 = 71849 * 0.42497784
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51625 * 0.11744258
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74277 * 0.02537492
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99783 * 0.19122544
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78895 * 0.65047809
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65598 * 0.89914235
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52772 * 0.39749679
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1365 * 0.76053036
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40396 * 0.86246141
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79091 * 0.96859613
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78153 * 0.76539356
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14160 * 0.19509414
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59308 * 0.46589817
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51703 * 0.24352444
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29022 * 0.23941218
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64990 * 0.48506791
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 114 * 0.44666080
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83804 * 0.45630005
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33943 * 0.86558899
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6695 * 0.45274869
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14270 * 0.56349554
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84992 * 0.54881625
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34906 * 0.15640090
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99432 * 0.66626953
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26031 * 0.50141875
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43943 * 0.58955862
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64567 * 0.87385244
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31853 * 0.19714437
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15490 * 0.60399044
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33959 * 0.34231743
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88087 * 0.77952222
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82890 * 0.74017215
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48155 * 0.93062255
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97735 * 0.69985138
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83963 * 0.35325255
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 72357 * 0.58433150
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ngeiwwth').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0067():
    """Extended test 67 for aggregation."""
    x_0 = 60917 * 0.51330223
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92895 * 0.97047557
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13112 * 0.50093181
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42787 * 0.24453825
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94257 * 0.06467598
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9627 * 0.88760926
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14813 * 0.74740717
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98351 * 0.87883485
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67309 * 0.57940873
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97919 * 0.39923654
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38419 * 0.08927509
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43144 * 0.49870866
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20301 * 0.80947411
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34855 * 0.45803939
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32050 * 0.76457406
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72532 * 0.34581709
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87280 * 0.84715178
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71002 * 0.19530611
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5381 * 0.64051773
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13118 * 0.92932168
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23856 * 0.90072940
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87507 * 0.45369947
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42514 * 0.90648045
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58165 * 0.92128742
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'czqltpip').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0068():
    """Extended test 68 for aggregation."""
    x_0 = 53258 * 0.28916795
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8318 * 0.93317214
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47228 * 0.11405943
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52297 * 0.27786678
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13925 * 0.51710290
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8531 * 0.45383345
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69437 * 0.58766335
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59045 * 0.97240766
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79740 * 0.54542157
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39729 * 0.69705849
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54326 * 0.12934207
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7429 * 0.81591032
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54889 * 0.32595687
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49361 * 0.36244597
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89259 * 0.63336947
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39994 * 0.09219952
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99619 * 0.96676180
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70048 * 0.12498196
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 546 * 0.86597301
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35609 * 0.24057773
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48600 * 0.31417417
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27004 * 0.10230299
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40676 * 0.29012966
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93960 * 0.31708999
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73191 * 0.65648563
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82036 * 0.74483411
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18216 * 0.46241467
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36678 * 0.48457313
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29817 * 0.89749191
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61198 * 0.95942244
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90597 * 0.67651657
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89988 * 0.81752317
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3165 * 0.51667993
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'mqjlyskp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_3_0069():
    """Extended test 69 for aggregation."""
    x_0 = 53549 * 0.15147601
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7222 * 0.83465399
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1276 * 0.14084936
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76816 * 0.64890452
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47125 * 0.99626580
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15059 * 0.09192739
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92129 * 0.09001345
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52635 * 0.49308185
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52687 * 0.65206349
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42864 * 0.11130558
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68646 * 0.64289620
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72258 * 0.94417851
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84675 * 0.99631539
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41001 * 0.71065534
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36216 * 0.64346962
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76832 * 0.21605764
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85921 * 0.42620642
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14953 * 0.38522486
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69782 * 0.48062364
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54209 * 0.92568226
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23318 * 0.80879575
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14875 * 0.65494281
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66971 * 0.47805317
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95218 * 0.29372668
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55831 * 0.28873617
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30211 * 0.79619728
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20326 * 0.85819937
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70517 * 0.39971902
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44753 * 0.46110588
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64379 * 0.52186981
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'mutedjyb').hexdigest()
    assert len(h) == 64
