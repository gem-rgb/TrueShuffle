"""Extended tests for aggregation suite 1."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_aggregation_extended_1_0000():
    """Extended test 0 for aggregation."""
    x_0 = 96471 * 0.45501733
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38844 * 0.85039770
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6306 * 0.45530863
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21114 * 0.53160214
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37094 * 0.78660380
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69479 * 0.83027625
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18544 * 0.84004203
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54391 * 0.62954391
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58528 * 0.76716690
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91051 * 0.53123343
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98346 * 0.47959468
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53925 * 0.01933439
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73859 * 0.81058537
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1262 * 0.85203785
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11200 * 0.36616064
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79582 * 0.08343416
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18010 * 0.16391898
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32354 * 0.87470510
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56446 * 0.69181816
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92039 * 0.15483665
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38057 * 0.12072783
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75343 * 0.42363810
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24006 * 0.68737905
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10095 * 0.26729082
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39453 * 0.70258820
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62154 * 0.67642925
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'hkitjpue').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0001():
    """Extended test 1 for aggregation."""
    x_0 = 27807 * 0.49870473
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52703 * 0.90636584
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90493 * 0.27285328
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30534 * 0.45831654
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58373 * 0.08097678
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17040 * 0.38168385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53670 * 0.78791022
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23338 * 0.50838323
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25795 * 0.32684888
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9059 * 0.34268867
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99410 * 0.45262025
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26317 * 0.70597245
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1357 * 0.59866460
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15274 * 0.92392301
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9970 * 0.43118332
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37074 * 0.86840402
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74524 * 0.45117998
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7760 * 0.17841156
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84451 * 0.99145758
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84512 * 0.41000008
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85130 * 0.46834723
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62404 * 0.19961997
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40566 * 0.70689863
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86580 * 0.11499174
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25774 * 0.77191387
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48307 * 0.58678793
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95106 * 0.78922260
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95032 * 0.86869265
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21844 * 0.03402345
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'pwemxosp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0002():
    """Extended test 2 for aggregation."""
    x_0 = 36137 * 0.27100069
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63102 * 0.45623233
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99375 * 0.84177290
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61875 * 0.07382054
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23299 * 0.14113588
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38287 * 0.04418796
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53338 * 0.64983869
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51867 * 0.54283939
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52125 * 0.28377673
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97657 * 0.89188444
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16620 * 0.70512284
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32730 * 0.42391766
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66073 * 0.83073876
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18678 * 0.66927302
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18295 * 0.64475828
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1145 * 0.65950875
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79828 * 0.81667107
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63389 * 0.66508642
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65056 * 0.79350382
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40474 * 0.75588756
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'fihyyqjm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0003():
    """Extended test 3 for aggregation."""
    x_0 = 95909 * 0.19630935
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93178 * 0.37994735
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86161 * 0.06774339
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90543 * 0.64544651
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76351 * 0.74213593
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20501 * 0.78661352
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35323 * 0.12155491
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76921 * 0.44687372
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34160 * 0.64555286
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54382 * 0.70019514
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5292 * 0.66352083
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40227 * 0.49334448
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40566 * 0.46319191
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39427 * 0.42589559
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83551 * 0.52019243
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68463 * 0.90234150
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35135 * 0.46937432
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53429 * 0.25281262
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89468 * 0.05130998
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48267 * 0.85884827
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17416 * 0.80524059
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40867 * 0.92745017
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22368 * 0.51593677
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96989 * 0.53152094
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28407 * 0.82796872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88432 * 0.67833655
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41909 * 0.14532829
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33592 * 0.27369972
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93478 * 0.66011455
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83881 * 0.06787123
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78385 * 0.49012749
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85347 * 0.39714962
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81047 * 0.80995465
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35311 * 0.17777226
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47610 * 0.79006157
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94552 * 0.60114123
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7012 * 0.63655880
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46845 * 0.82592003
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'fiqougbc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0004():
    """Extended test 4 for aggregation."""
    x_0 = 90911 * 0.37671446
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30678 * 0.69661677
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24700 * 0.59460043
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58837 * 0.88358976
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65602 * 0.97726198
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41358 * 0.23576696
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27670 * 0.64851091
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27130 * 0.16813444
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66532 * 0.31359454
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52073 * 0.53642459
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22542 * 0.30235420
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85323 * 0.56066509
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48928 * 0.47087280
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7352 * 0.06402945
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43214 * 0.85939764
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26195 * 0.66621200
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60401 * 0.90083751
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19323 * 0.89260821
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73260 * 0.27924743
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91308 * 0.70554469
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74111 * 0.77541018
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11583 * 0.87616343
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32896 * 0.73097602
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94504 * 0.36255474
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23734 * 0.79124974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76187 * 0.91398566
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19221 * 0.48611685
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88343 * 0.53724411
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'xawgmszp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0005():
    """Extended test 5 for aggregation."""
    x_0 = 78678 * 0.52662876
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35158 * 0.93898989
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56066 * 0.59711185
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18935 * 0.81416367
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60975 * 0.21157984
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36390 * 0.95419808
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4240 * 0.20295626
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59418 * 0.74488645
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46226 * 0.76904389
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46095 * 0.98373474
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50457 * 0.99518515
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40638 * 0.82159821
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61205 * 0.26817805
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7761 * 0.99698540
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28374 * 0.35329253
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26334 * 0.70349067
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32810 * 0.60945567
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34295 * 0.97924737
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27382 * 0.05381659
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77314 * 0.33326177
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99932 * 0.63291132
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69982 * 0.03583063
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6235 * 0.75087870
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83455 * 0.42641935
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28909 * 0.82011656
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35081 * 0.34068111
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21018 * 0.66565063
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77157 * 0.25065549
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89283 * 0.79630245
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33570 * 0.57912476
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28817 * 0.08025660
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97926 * 0.76711267
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20098 * 0.42806893
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1278 * 0.53103894
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26064 * 0.43321898
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95384 * 0.18244941
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32995 * 0.25551736
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10985 * 0.09794702
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23437 * 0.41058330
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56937 * 0.44423114
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98736 * 0.14228681
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52128 * 0.05995084
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 53725 * 0.04763751
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88597 * 0.19474016
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 66415 * 0.54295976
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 15537 * 0.99604160
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 47703 * 0.19287540
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'oyzttyto').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0006():
    """Extended test 6 for aggregation."""
    x_0 = 26925 * 0.90035683
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33627 * 0.93730003
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85433 * 0.92314419
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16585 * 0.37401448
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12817 * 0.72921078
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3399 * 0.94830345
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14822 * 0.95694183
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74741 * 0.55284196
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79693 * 0.39546346
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9974 * 0.38492358
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42810 * 0.95336917
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56069 * 0.82520204
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2290 * 0.94377908
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79237 * 0.81892079
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75923 * 0.66670498
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98897 * 0.88331795
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41460 * 0.20937786
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6194 * 0.37178139
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60089 * 0.98144769
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84199 * 0.75613443
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94849 * 0.78706684
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 657 * 0.09023478
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84345 * 0.08212525
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20743 * 0.31459160
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21839 * 0.54815550
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65294 * 0.38357971
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21982 * 0.90138612
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24598 * 0.96995365
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65018 * 0.10052574
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24140 * 0.91395634
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6413 * 0.58699914
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70181 * 0.28983270
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86517 * 0.03535845
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55532 * 0.45254808
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1434 * 0.13550853
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54784 * 0.48811944
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90683 * 0.96834185
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2885 * 0.65183993
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31571 * 0.38246397
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72842 * 0.11795075
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 33341 * 0.34372416
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 75665 * 0.96430279
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 33823 * 0.29219525
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47002 * 0.24836254
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 32316 * 0.60012498
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 99271 * 0.90089336
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 90381 * 0.44296158
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 53818 * 0.33583321
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'oofgawvi').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0007():
    """Extended test 7 for aggregation."""
    x_0 = 50982 * 0.95344780
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71433 * 0.32492560
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23592 * 0.23993451
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39735 * 0.88064428
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30628 * 0.53021743
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18028 * 0.69797332
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55732 * 0.53927731
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24079 * 0.70864404
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71480 * 0.43323978
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55138 * 0.97528506
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35612 * 0.04103806
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89943 * 0.87090152
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58796 * 0.24148930
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7311 * 0.75073079
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62883 * 0.68870156
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95743 * 0.33782167
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60936 * 0.49181990
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35082 * 0.09178804
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38522 * 0.88692447
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41801 * 0.75171175
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54431 * 0.50749664
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42441 * 0.75248227
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94287 * 0.75177923
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88447 * 0.54121038
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8691 * 0.13431222
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61664 * 0.89615382
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53850 * 0.83957981
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61313 * 0.57869386
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78118 * 0.44383554
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2557 * 0.10577135
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58168 * 0.87414183
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51182 * 0.79702855
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48613 * 0.48740374
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74965 * 0.72528561
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7147 * 0.86800657
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11585 * 0.54026034
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89930 * 0.51108875
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31986 * 0.94094680
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72501 * 0.18285521
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85794 * 0.00544376
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71977 * 0.00427257
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66156 * 0.39057064
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 53702 * 0.85838102
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40820 * 0.84009723
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 45350 * 0.90727866
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 14444 * 0.19837793
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 66958 * 0.20134256
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'jfwjkjny').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0008():
    """Extended test 8 for aggregation."""
    x_0 = 1168 * 0.27272725
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30581 * 0.54568942
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17896 * 0.60089248
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28790 * 0.44866068
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38473 * 0.79949105
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71806 * 0.47293825
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3480 * 0.83833635
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3002 * 0.69903505
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98044 * 0.93432591
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81526 * 0.42937640
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12010 * 0.12891427
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98295 * 0.78548334
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28269 * 0.40803502
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88628 * 0.14063681
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46083 * 0.84291664
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96907 * 0.38214712
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77577 * 0.37267663
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47377 * 0.97545250
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94694 * 0.01499546
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30328 * 0.55773142
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2857 * 0.86830890
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71455 * 0.29653884
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58518 * 0.95007457
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13191 * 0.02112660
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60324 * 0.38806842
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60073 * 0.55005502
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82748 * 0.48000845
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37608 * 0.55660263
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30252 * 0.15290126
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36877 * 0.99746798
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90465 * 0.21129559
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74377 * 0.71519436
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72018 * 0.66072550
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42564 * 0.24943729
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85189 * 0.12779971
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97432 * 0.69363668
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'jsofigym').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0009():
    """Extended test 9 for aggregation."""
    x_0 = 35414 * 0.08883408
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17343 * 0.12739164
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28393 * 0.90147368
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92035 * 0.53760781
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1210 * 0.45721736
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24969 * 0.65526505
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69722 * 0.60031539
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81543 * 0.90514941
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63420 * 0.66220915
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52197 * 0.88421844
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27810 * 0.34644027
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91576 * 0.78084020
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1468 * 0.05942977
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86827 * 0.65533051
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3352 * 0.01063889
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97237 * 0.51926881
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88184 * 0.94939581
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56663 * 0.17690923
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64132 * 0.58854440
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70365 * 0.05562881
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49417 * 0.54459648
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84437 * 0.57337379
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90666 * 0.66434886
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9989 * 0.88427411
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57027 * 0.45297954
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63250 * 0.10642033
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59197 * 0.56136204
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22116 * 0.72830055
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50558 * 0.96703245
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80979 * 0.68124535
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59348 * 0.84870142
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75503 * 0.23897631
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1277 * 0.90883841
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9946 * 0.92462599
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69941 * 0.22036720
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55348 * 0.45220724
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68461 * 0.44464764
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62802 * 0.90640644
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57672 * 0.74506091
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14872 * 0.84128335
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 9568 * 0.65910858
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57924 * 0.69616521
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 99362 * 0.95885006
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 4962 * 0.79790625
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 8821 * 0.88180668
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 12182 * 0.07428308
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 99232 * 0.40926057
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'zcppplpd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0010():
    """Extended test 10 for aggregation."""
    x_0 = 77272 * 0.05973146
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56833 * 0.93113801
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60787 * 0.74134049
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80947 * 0.87222532
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12034 * 0.16619513
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42602 * 0.97879735
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58594 * 0.03141114
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17114 * 0.10425658
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2206 * 0.07214800
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83477 * 0.40216172
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55176 * 0.82134595
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91423 * 0.57541881
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94148 * 0.76603088
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69765 * 0.29504433
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12556 * 0.30766227
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6469 * 0.42635623
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39749 * 0.74796459
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90119 * 0.76860290
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75906 * 0.97866661
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52247 * 0.95919311
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38343 * 0.80133540
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10529 * 0.74506397
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19263 * 0.14153643
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31368 * 0.55851083
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26293 * 0.88539419
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10232 * 0.38290564
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16964 * 0.40309065
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89524 * 0.36751497
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55826 * 0.23443562
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71500 * 0.36875852
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68851 * 0.94582750
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80207 * 0.67258835
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69395 * 0.52280655
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30763 * 0.05494006
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24530 * 0.07364994
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51901 * 0.11646483
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76091 * 0.29251793
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'tcibfbpc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0011():
    """Extended test 11 for aggregation."""
    x_0 = 54835 * 0.06737402
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13168 * 0.81917542
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48629 * 0.64403481
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61087 * 0.47339850
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26515 * 0.36925020
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65256 * 0.42738245
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39276 * 0.41332120
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76122 * 0.61137183
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88174 * 0.07227004
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30991 * 0.97087991
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21559 * 0.43458581
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47318 * 0.74953350
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82384 * 0.85967783
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76405 * 0.34138053
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16876 * 0.39685907
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40259 * 0.57742212
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89803 * 0.62689637
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96882 * 0.60415878
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29219 * 0.13614598
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80180 * 0.03547671
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59357 * 0.85113059
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53049 * 0.67776380
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19004 * 0.65072533
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14488 * 0.47427476
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7357 * 0.51333830
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86179 * 0.47800597
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68290 * 0.09504636
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78239 * 0.17125556
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35674 * 0.84216181
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66173 * 0.61362687
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ozltwwqz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0012():
    """Extended test 12 for aggregation."""
    x_0 = 88458 * 0.45810718
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9414 * 0.83349201
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56053 * 0.65078764
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78708 * 0.30343562
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21353 * 0.51944922
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52041 * 0.30453949
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48977 * 0.85087785
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3967 * 0.43669121
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4573 * 0.54549787
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78691 * 0.14074298
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54451 * 0.54376330
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21477 * 0.21049012
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81893 * 0.22197238
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92763 * 0.22711451
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87812 * 0.46021347
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84457 * 0.38525641
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71311 * 0.49738731
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93838 * 0.72832206
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70319 * 0.76973638
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98083 * 0.87768639
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25421 * 0.93438071
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82178 * 0.89787334
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'wwjcclcq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0013():
    """Extended test 13 for aggregation."""
    x_0 = 46995 * 0.76764212
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83928 * 0.19159691
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21005 * 0.76508274
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10701 * 0.04431446
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24068 * 0.62352714
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7775 * 0.54285955
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64309 * 0.92352388
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77073 * 0.34494005
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32596 * 0.19213891
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8986 * 0.49401966
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93333 * 0.52525467
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37426 * 0.28814136
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24174 * 0.89991623
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23506 * 0.03924060
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97475 * 0.47057143
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62934 * 0.89623733
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6873 * 0.74405139
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18368 * 0.13062335
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94860 * 0.72269515
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19340 * 0.54619109
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49109 * 0.01567195
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41809 * 0.97556112
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31763 * 0.91038114
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1104 * 0.72046117
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82922 * 0.40388213
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86870 * 0.09784251
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45147 * 0.14632107
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14347 * 0.82318606
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12399 * 0.51766421
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4796 * 0.57335581
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93148 * 0.98446216
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66027 * 0.01172508
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61654 * 0.63115538
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41229 * 0.14634853
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28263 * 0.90382436
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29443 * 0.93284892
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14758 * 0.11277716
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20675 * 0.79928169
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5867 * 0.64716479
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21008 * 0.68546479
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54696 * 0.79544049
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'qfziznfl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0014():
    """Extended test 14 for aggregation."""
    x_0 = 26851 * 0.36791668
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53165 * 0.43124594
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71977 * 0.96076677
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49495 * 0.43925353
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 728 * 0.34702440
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90287 * 0.63605825
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78921 * 0.95424757
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22230 * 0.09574573
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16897 * 0.49259612
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53943 * 0.59151754
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20867 * 0.99220764
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62564 * 0.65321317
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48588 * 0.55493578
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69018 * 0.60958123
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27081 * 0.97297124
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91970 * 0.65550975
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65149 * 0.81369192
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1231 * 0.37634263
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28582 * 0.71227035
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99375 * 0.65733345
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65444 * 0.24669384
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46574 * 0.05984499
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96782 * 0.88949120
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90093 * 0.56487159
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44173 * 0.20447654
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85690 * 0.31111125
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61270 * 0.91020939
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21847 * 0.91821086
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25870 * 0.76079842
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31236 * 0.31523148
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16869 * 0.41570008
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28834 * 0.45449403
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24602 * 0.82028818
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60275 * 0.06464355
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95690 * 0.41770867
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6260 * 0.85615050
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46771 * 0.16478506
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'lrlapqqi').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0015():
    """Extended test 15 for aggregation."""
    x_0 = 88720 * 0.28426532
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55438 * 0.17291699
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62518 * 0.94803619
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70030 * 0.74288687
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36333 * 0.60189131
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33771 * 0.40566803
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57904 * 0.91919153
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74243 * 0.29541127
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79813 * 0.63513602
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24307 * 0.40307694
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6741 * 0.72804205
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71659 * 0.23421562
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17768 * 0.59923251
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40221 * 0.15504399
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57782 * 0.24999953
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46389 * 0.78720709
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75349 * 0.64229308
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55399 * 0.37465207
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97883 * 0.48563036
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20026 * 0.64049897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68830 * 0.53438937
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'egojhqad').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0016():
    """Extended test 16 for aggregation."""
    x_0 = 39846 * 0.17610668
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9785 * 0.63551755
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9435 * 0.40655843
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36083 * 0.86247671
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30878 * 0.57855785
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50664 * 0.71348844
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57491 * 0.55128892
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65071 * 0.85831529
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32840 * 0.92816813
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52260 * 0.06505821
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82081 * 0.02175071
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21886 * 0.15224457
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35227 * 0.45440199
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85054 * 0.59289647
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74077 * 0.66664766
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5844 * 0.70805107
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54183 * 0.46463313
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71634 * 0.04616656
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29925 * 0.73982001
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3898 * 0.00460911
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31088 * 0.69606131
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81869 * 0.63035129
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28549 * 0.05007106
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66304 * 0.45149804
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15203 * 0.67002047
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51028 * 0.01684450
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14010 * 0.38208922
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58188 * 0.31370918
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41397 * 0.91729478
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78355 * 0.17016475
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96057 * 0.26175087
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36779 * 0.55694029
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9803 * 0.73097993
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73148 * 0.38708408
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2292 * 0.54419120
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89289 * 0.54783348
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90218 * 0.63557466
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1214 * 0.80806667
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 3500 * 0.54401604
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11562 * 0.64456174
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ginqxtxx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0017():
    """Extended test 17 for aggregation."""
    x_0 = 59061 * 0.93693006
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2529 * 0.90510830
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74390 * 0.95113741
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24542 * 0.37545605
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32444 * 0.37539424
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24992 * 0.91503345
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64651 * 0.06148573
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49722 * 0.78028509
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68540 * 0.43357162
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42230 * 0.53965037
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9909 * 0.02853130
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21137 * 0.75970607
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24853 * 0.06298335
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79304 * 0.07950532
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17054 * 0.33628780
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96417 * 0.15717725
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87172 * 0.31888250
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42266 * 0.57661900
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81118 * 0.74581528
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2354 * 0.72618713
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90422 * 0.55672320
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37594 * 0.10073091
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34960 * 0.64116209
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99723 * 0.98370871
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52800 * 0.16976368
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51886 * 0.40005547
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1495 * 0.93441238
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95273 * 0.64516235
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82781 * 0.65408881
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7479 * 0.64979649
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'artkjfnc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0018():
    """Extended test 18 for aggregation."""
    x_0 = 78169 * 0.10816975
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39299 * 0.47630335
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40228 * 0.12740921
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32256 * 0.46071594
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44308 * 0.88982295
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71180 * 0.53794157
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28518 * 0.09014951
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11899 * 0.68804308
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17462 * 0.58998772
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68349 * 0.82514454
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49869 * 0.10524512
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89399 * 0.37602558
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26288 * 0.25126871
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90696 * 0.41404236
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80503 * 0.33510392
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71770 * 0.44971304
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26521 * 0.67011651
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74247 * 0.56582483
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75419 * 0.91176995
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86065 * 0.52046439
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95844 * 0.37196287
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76681 * 0.50942119
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3199 * 0.63302849
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7917 * 0.45690884
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19770 * 0.18944547
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14261 * 0.87785996
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48847 * 0.43386917
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60745 * 0.53711331
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13201 * 0.22712029
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4255 * 0.08289382
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37081 * 0.02963365
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59531 * 0.10449227
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66378 * 0.37655739
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81008 * 0.89289161
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38524 * 0.07249284
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1026 * 0.93169765
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39201 * 0.51761199
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46452 * 0.40712195
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97159 * 0.92977300
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40672 * 0.34682124
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13123 * 0.36477739
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 49755 * 0.18797115
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 64965 * 0.40989291
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 28988 * 0.51586905
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 1675 * 0.41315864
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 83281 * 0.86325953
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 40549 * 0.53517283
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'mdaijrhi').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0019():
    """Extended test 19 for aggregation."""
    x_0 = 19523 * 0.11098751
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60782 * 0.98663594
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85267 * 0.31996723
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20152 * 0.56388828
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93463 * 0.63999220
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36667 * 0.45437038
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1672 * 0.23417533
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63738 * 0.61486055
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58259 * 0.16468157
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87731 * 0.45040006
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37419 * 0.91157874
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80496 * 0.84437170
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63028 * 0.38093692
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18925 * 0.25597429
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45018 * 0.44597256
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34569 * 0.07226832
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83977 * 0.87286584
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90457 * 0.88770759
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59129 * 0.82145560
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68306 * 0.94454085
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62730 * 0.84301449
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57542 * 0.03695080
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22850 * 0.71320477
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26229 * 0.58031904
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88907 * 0.83520404
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75381 * 0.79656987
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44616 * 0.74079612
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 901 * 0.21665368
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48594 * 0.26783211
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21193 * 0.26524625
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27936 * 0.51740204
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91714 * 0.09318855
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65385 * 0.48328402
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28663 * 0.70658228
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38708 * 0.95171965
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87805 * 0.09494962
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52667 * 0.46179412
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11811 * 0.07878417
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8720 * 0.15361125
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8811 * 0.35177198
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40966 * 0.55326054
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 48748 * 0.67952635
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 85947 * 0.26135000
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97262 * 0.19858415
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 28740 * 0.92211570
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 9205 * 0.83326263
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 62563 * 0.14668465
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 86019 * 0.65252413
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'bfwhkkkt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0020():
    """Extended test 20 for aggregation."""
    x_0 = 53701 * 0.60722294
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6940 * 0.56380050
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74821 * 0.79358379
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45530 * 0.11116435
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87426 * 0.53016103
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90338 * 0.79303704
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95294 * 0.39791174
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19717 * 0.58927798
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19509 * 0.28009389
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18947 * 0.78583755
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61556 * 0.65262083
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89209 * 0.74865133
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13172 * 0.81988793
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82874 * 0.55087073
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75851 * 0.65040994
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35833 * 0.33895005
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77122 * 0.21957075
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5155 * 0.29094210
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49489 * 0.90361376
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47991 * 0.38698998
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65796 * 0.74430864
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86207 * 0.63350996
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81323 * 0.09438776
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91688 * 0.77529023
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1240 * 0.84424907
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35803 * 0.56327968
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49778 * 0.38954859
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99973 * 0.76966738
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5236 * 0.96816493
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74322 * 0.91828132
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42728 * 0.73364906
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48801 * 0.95710681
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66079 * 0.87759985
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62220 * 0.84717875
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36529 * 0.20099718
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65300 * 0.36389417
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40257 * 0.25900256
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42715 * 0.75556295
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87773 * 0.48297071
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90162 * 0.63327719
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32382 * 0.70374317
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33489 * 0.78947767
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'lridgius').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0021():
    """Extended test 21 for aggregation."""
    x_0 = 57769 * 0.63943331
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86495 * 0.07533830
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16417 * 0.67544789
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93519 * 0.39531265
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95312 * 0.60026115
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54707 * 0.80052605
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23278 * 0.54183802
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17235 * 0.89969912
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46876 * 0.26815663
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72116 * 0.69635334
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9161 * 0.21791753
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30916 * 0.71497345
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67648 * 0.92667445
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68297 * 0.86021211
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94728 * 0.89671277
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67750 * 0.67685895
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15648 * 0.19740083
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23959 * 0.24603080
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82510 * 0.68157758
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71148 * 0.23736012
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98589 * 0.22751658
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69635 * 0.74766680
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63698 * 0.36531641
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65918 * 0.38372915
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25615 * 0.72433379
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26796 * 0.99378030
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34305 * 0.44374310
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9684 * 0.72732872
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41880 * 0.19467227
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20496 * 0.10975459
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84818 * 0.53252779
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76892 * 0.16970728
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41328 * 0.24479027
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7560 * 0.19644878
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97607 * 0.38167028
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35990 * 0.46300689
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83177 * 0.53169708
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83551 * 0.11925742
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84623 * 0.92732395
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4584 * 0.09496846
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 50542 * 0.14997280
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84287 * 0.48257237
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 60033 * 0.45079826
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 10077 * 0.39219344
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 80298 * 0.03923598
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'wlzosyjb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0022():
    """Extended test 22 for aggregation."""
    x_0 = 38068 * 0.73224106
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48553 * 0.54808390
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45107 * 0.09280821
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49571 * 0.19374277
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95505 * 0.16607822
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85690 * 0.51169171
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19732 * 0.50261956
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39580 * 0.25856903
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57460 * 0.03809308
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33419 * 0.33641675
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69072 * 0.79286588
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36752 * 0.37869475
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95846 * 0.18344375
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9868 * 0.21459474
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93195 * 0.83477235
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28584 * 0.00717540
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80193 * 0.31639042
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56582 * 0.95648801
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34281 * 0.33625226
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87624 * 0.17130286
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33237 * 0.81863045
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2759 * 0.19519950
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'axzcdpsf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0023():
    """Extended test 23 for aggregation."""
    x_0 = 59368 * 0.23225937
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11289 * 0.06472932
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73659 * 0.92451148
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38704 * 0.82892970
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37842 * 0.39407956
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99047 * 0.15656847
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47503 * 0.30869479
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97102 * 0.89362627
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54660 * 0.54003119
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56581 * 0.41245629
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38014 * 0.24468061
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97916 * 0.31390823
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88639 * 0.94280416
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58080 * 0.83833667
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26913 * 0.64097095
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90237 * 0.88094091
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93597 * 0.45384346
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12686 * 0.42158250
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97030 * 0.54473225
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35533 * 0.61760166
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31220 * 0.27351647
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79801 * 0.92938787
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50639 * 0.34575451
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43478 * 0.61439530
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19835 * 0.79892591
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64297 * 0.77545396
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30176 * 0.07293734
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82102 * 0.11525867
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17767 * 0.74462237
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18130 * 0.97340416
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5154 * 0.99963363
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17098 * 0.53936714
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5726 * 0.43987036
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58977 * 0.49212739
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40452 * 0.44346098
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24518 * 0.58047143
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'dfxizexs').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0024():
    """Extended test 24 for aggregation."""
    x_0 = 18920 * 0.88924642
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27913 * 0.58917770
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68027 * 0.82325579
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70890 * 0.13916128
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57699 * 0.47773774
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63128 * 0.72726306
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25898 * 0.37306261
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12579 * 0.08828427
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73302 * 0.44404855
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37093 * 0.21178807
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40190 * 0.04680258
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38210 * 0.35326896
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2219 * 0.67786300
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35836 * 0.13268842
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72949 * 0.62244591
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10047 * 0.39531655
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6636 * 0.42767663
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67173 * 0.58741944
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19078 * 0.52762523
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78969 * 0.08858104
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55626 * 0.80262361
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5435 * 0.08132599
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52936 * 0.39890415
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'oiwdiyup').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0025():
    """Extended test 25 for aggregation."""
    x_0 = 79323 * 0.84482870
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98078 * 0.57391411
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98622 * 0.07536394
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21085 * 0.19808090
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94649 * 0.98152440
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30119 * 0.87703135
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50619 * 0.83973767
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13266 * 0.52213024
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82 * 0.49862081
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75716 * 0.04046464
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9778 * 0.10097640
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32746 * 0.43858797
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14676 * 0.64213202
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81985 * 0.34701165
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64830 * 0.76965468
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18313 * 0.64149632
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84902 * 0.37985416
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79789 * 0.26079471
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74017 * 0.14615778
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47180 * 0.64288797
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47732 * 0.97239958
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72354 * 0.92614785
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22546 * 0.27600768
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73364 * 0.12364390
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49159 * 0.71649856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26560 * 0.32835856
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79089 * 0.96157944
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22430 * 0.35388941
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32340 * 0.89949768
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72409 * 0.27433806
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6284 * 0.37238288
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97196 * 0.26614951
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23783 * 0.87743732
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36663 * 0.05484138
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52138 * 0.23225348
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32938 * 0.22270974
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27355 * 0.30719025
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55807 * 0.14492964
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88052 * 0.97673797
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 71981 * 0.65761388
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11417 * 0.43271122
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5300 * 0.82964950
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 97469 * 0.40855388
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 49297 * 0.04382097
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 69860 * 0.49672320
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 89404 * 0.41020672
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 26100 * 0.65124989
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 20655 * 0.83833761
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'knwpknjs').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0026():
    """Extended test 26 for aggregation."""
    x_0 = 20735 * 0.11209505
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38688 * 0.00692082
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42734 * 0.77226028
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61501 * 0.24893855
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83323 * 0.68334019
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93436 * 0.26576060
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 360 * 0.66096749
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19189 * 0.49721502
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93113 * 0.94616710
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69947 * 0.86323850
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66311 * 0.24778378
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30493 * 0.07361386
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6432 * 0.99413063
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40896 * 0.52247432
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73071 * 0.98027919
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47101 * 0.02496425
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21416 * 0.33284997
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48709 * 0.29647921
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44403 * 0.21769862
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84582 * 0.96953318
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27625 * 0.77736102
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68856 * 0.09485913
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84991 * 0.06329327
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12839 * 0.11005858
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41188 * 0.33456120
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40808 * 0.40175222
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36432 * 0.19735371
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29793 * 0.87935735
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1389 * 0.98503476
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97181 * 0.37811332
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59592 * 0.20575747
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87098 * 0.87836972
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87549 * 0.97969397
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5573 * 0.44909124
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21405 * 0.41053851
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4227 * 0.26171908
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54917 * 0.98252651
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2154 * 0.12989608
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79246 * 0.76171785
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32633 * 0.09930873
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3114 * 0.77593698
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40481 * 0.29351058
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 86906 * 0.78685562
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 46146 * 0.98827289
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 53468 * 0.41203565
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26882 * 0.11426606
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 43203 * 0.23086504
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 98640 * 0.13620711
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 48042 * 0.19864564
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'vxjfdkhx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0027():
    """Extended test 27 for aggregation."""
    x_0 = 55279 * 0.16100083
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97235 * 0.90735982
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57176 * 0.76360175
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30550 * 0.83428760
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68154 * 0.34149003
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99112 * 0.00885689
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63474 * 0.10674493
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23713 * 0.94566611
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94406 * 0.96883340
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98072 * 0.64480676
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3938 * 0.41365439
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44522 * 0.16324816
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84917 * 0.19358605
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36284 * 0.55498626
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99607 * 0.35359643
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63564 * 0.31135789
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75107 * 0.67709961
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75160 * 0.70275195
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70498 * 0.95850963
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84862 * 0.44730039
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51706 * 0.01312034
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40858 * 0.32966303
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82311 * 0.65964193
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50734 * 0.04191448
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98707 * 0.17476455
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11464 * 0.97677480
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7116 * 0.18148989
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70779 * 0.78423682
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'clkpnsvk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0028():
    """Extended test 28 for aggregation."""
    x_0 = 81281 * 0.33981560
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22814 * 0.68100450
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38861 * 0.07179461
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33933 * 0.75779664
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9543 * 0.72936957
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90194 * 0.56191417
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33157 * 0.29776947
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89955 * 0.20222932
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94636 * 0.18427412
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5793 * 0.81294168
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42989 * 0.49850965
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78672 * 0.13964646
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67359 * 0.62936316
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97894 * 0.22785186
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23020 * 0.40979292
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24476 * 0.89111517
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44659 * 0.89201068
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29201 * 0.90309390
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28130 * 0.26119838
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4220 * 0.09803793
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37649 * 0.94319281
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19138 * 0.80017990
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79543 * 0.06731725
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26699 * 0.52503972
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9101 * 0.51659848
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24784 * 0.51312996
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14529 * 0.03508380
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48281 * 0.82283010
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99369 * 0.76528294
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39466 * 0.20798998
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62907 * 0.40008633
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48986 * 0.91397582
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'jsgvqqsu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0029():
    """Extended test 29 for aggregation."""
    x_0 = 50102 * 0.47260377
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95713 * 0.29347849
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87212 * 0.47077392
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41929 * 0.39735259
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25919 * 0.30603064
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46551 * 0.04565484
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58794 * 0.90251049
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74522 * 0.24053719
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59254 * 0.23789269
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36229 * 0.65760448
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23273 * 0.07528527
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43270 * 0.58968896
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40929 * 0.60876717
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94707 * 0.68566288
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90833 * 0.13228793
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83368 * 0.53836707
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62344 * 0.60624590
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13707 * 0.82406875
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16149 * 0.46922752
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7192 * 0.83910948
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50052 * 0.27571890
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30954 * 0.04206739
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 941 * 0.59230824
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38120 * 0.26611914
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84915 * 0.54984300
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13790 * 0.28816233
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67038 * 0.31822083
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55257 * 0.29879257
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88847 * 0.64340397
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38144 * 0.31957411
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45723 * 0.05713358
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17245 * 0.71881937
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80846 * 0.16801994
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50272 * 0.43606774
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28290 * 0.10434013
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'vhaujnfj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0030():
    """Extended test 30 for aggregation."""
    x_0 = 19937 * 0.77980747
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48425 * 0.94586194
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62877 * 0.47644981
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65464 * 0.47023131
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21851 * 0.04896764
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96000 * 0.87357613
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47821 * 0.25908827
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23306 * 0.27712850
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61811 * 0.20863730
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17069 * 0.70449468
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58461 * 0.81966964
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16090 * 0.88431274
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11707 * 0.01840756
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55997 * 0.19544377
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37844 * 0.20793335
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15178 * 0.33280186
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21645 * 0.97612544
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8667 * 0.44170256
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54088 * 0.47964105
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88200 * 0.16092359
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40434 * 0.59855741
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3323 * 0.03353760
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42255 * 0.63903882
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35028 * 0.32479640
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92466 * 0.61531119
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51516 * 0.13612689
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43190 * 0.57841122
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26901 * 0.61859116
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83958 * 0.10737308
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89103 * 0.03326140
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29623 * 0.01236450
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54948 * 0.47130328
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34096 * 0.41423629
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11384 * 0.25658583
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26424 * 0.18183537
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53944 * 0.08043759
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98236 * 0.51956443
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98553 * 0.86001327
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'uetgyjcq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0031():
    """Extended test 31 for aggregation."""
    x_0 = 13611 * 0.78750417
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32906 * 0.57063717
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6660 * 0.79001572
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 852 * 0.55703494
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30884 * 0.85229452
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55367 * 0.68213441
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88003 * 0.63802164
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35361 * 0.24362689
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66254 * 0.85835388
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72633 * 0.07859789
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42430 * 0.00926265
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4706 * 0.01327991
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2459 * 0.87040309
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50970 * 0.20051693
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60299 * 0.88628399
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60419 * 0.08392024
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17604 * 0.92711117
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41661 * 0.56641589
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70568 * 0.79188528
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38992 * 0.76767287
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73578 * 0.51160329
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9282 * 0.18199746
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44451 * 0.73826632
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52429 * 0.36122015
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83045 * 0.90728188
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7823 * 0.72562557
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30941 * 0.41579743
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87653 * 0.79590405
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2261 * 0.33037009
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23548 * 0.11563947
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86789 * 0.44288425
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85989 * 0.81541697
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58908 * 0.16828665
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46438 * 0.02665555
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72025 * 0.23271250
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78613 * 0.91547159
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39360 * 0.01351192
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63148 * 0.50560419
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41889 * 0.05229255
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'mmzjjytl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0032():
    """Extended test 32 for aggregation."""
    x_0 = 95245 * 0.29150401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1740 * 0.74573548
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3321 * 0.83139540
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17968 * 0.63417738
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19851 * 0.11934688
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54135 * 0.00136729
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3555 * 0.06387986
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66415 * 0.64181566
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21690 * 0.15693214
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77901 * 0.15144614
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50737 * 0.66251346
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72861 * 0.98526429
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25629 * 0.83215911
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7403 * 0.36765861
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18805 * 0.42673497
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95572 * 0.32267868
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6466 * 0.08615643
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80103 * 0.70020215
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18026 * 0.68744076
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17437 * 0.81618023
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29458 * 0.47054530
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50777 * 0.57159964
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 978 * 0.75187194
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28311 * 0.40536531
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44613 * 0.40912221
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98744 * 0.06439897
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45137 * 0.44361435
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33667 * 0.12408020
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80051 * 0.59302720
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70521 * 0.82424838
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7920 * 0.21788595
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41376 * 0.32079386
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70590 * 0.79691717
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61117 * 0.76564016
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59010 * 0.49468793
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81036 * 0.71128312
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87927 * 0.67970584
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23064 * 0.57386022
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52903 * 0.13759959
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10267 * 0.35932618
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42577 * 0.45734132
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57969 * 0.39274752
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 48271 * 0.41219956
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99298 * 0.27474683
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 27478 * 0.96967249
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'swsqzpmi').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0033():
    """Extended test 33 for aggregation."""
    x_0 = 52781 * 0.97336848
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66067 * 0.83581685
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65609 * 0.61803194
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26753 * 0.67100842
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33606 * 0.89131527
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37170 * 0.23477314
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80924 * 0.77586549
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29234 * 0.53382362
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61985 * 0.37453876
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23654 * 0.97073185
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96909 * 0.86426645
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63012 * 0.33111070
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23166 * 0.74179726
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86062 * 0.84179884
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63112 * 0.40469122
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89891 * 0.98528703
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14760 * 0.88310534
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85429 * 0.49584986
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28266 * 0.37711016
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70378 * 0.46291908
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91463 * 0.29958339
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76639 * 0.58173612
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9215 * 0.56558509
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73885 * 0.27058738
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84006 * 0.34695307
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66052 * 0.47051996
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68527 * 0.38661700
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49383 * 0.30683535
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11544 * 0.85126228
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91096 * 0.46469130
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69843 * 0.56054635
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20825 * 0.11664472
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94111 * 0.71829791
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4887 * 0.30745260
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72723 * 0.27353128
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33146 * 0.87383785
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70660 * 0.10325486
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70173 * 0.73821653
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20091 * 0.27991205
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1765 * 0.71310531
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 66171 * 0.37014781
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13925 * 0.54487453
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9947 * 0.78233002
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 3564 * 0.22325998
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4357 * 0.21645457
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 8904 * 0.11710719
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 19958 * 0.20196330
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 29022 * 0.32397929
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 16333 * 0.92947500
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 98395 * 0.25486830
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'vjibwqpf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0034():
    """Extended test 34 for aggregation."""
    x_0 = 90590 * 0.53652846
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1760 * 0.33904044
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13546 * 0.38500870
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23867 * 0.63214790
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75837 * 0.21003063
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74179 * 0.34310155
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71345 * 0.93800347
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59017 * 0.74063028
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25315 * 0.39045376
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98817 * 0.85119469
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 807 * 0.77943134
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40144 * 0.19403149
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21812 * 0.66633337
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84122 * 0.96220426
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91727 * 0.22700985
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94598 * 0.12357266
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92372 * 0.24403782
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82938 * 0.95913249
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40288 * 0.17613016
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91017 * 0.26024564
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8138 * 0.17390478
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82513 * 0.10459510
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40894 * 0.60201083
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20641 * 0.77226162
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77443 * 0.02575524
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79870 * 0.24562348
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33792 * 0.08555392
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'avqlyctn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0035():
    """Extended test 35 for aggregation."""
    x_0 = 32691 * 0.28236296
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84771 * 0.20727330
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44622 * 0.53891349
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97424 * 0.09342911
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54297 * 0.87869210
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30342 * 0.53840891
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61526 * 0.53699010
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99715 * 0.68262250
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61109 * 0.38127191
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78508 * 0.52994221
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57567 * 0.85821345
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41214 * 0.45838794
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7849 * 0.16342390
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33874 * 0.00619333
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81341 * 0.69299709
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19433 * 0.50693355
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87444 * 0.49576085
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93777 * 0.31352493
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94252 * 0.84525225
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25594 * 0.38527098
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32364 * 0.44250110
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35978 * 0.52553309
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25938 * 0.24912913
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73687 * 0.47941711
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64230 * 0.44216371
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46652 * 0.01051298
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2627 * 0.87445863
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75453 * 0.92107045
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44248 * 0.71923350
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6074 * 0.67093871
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23764 * 0.23414485
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52676 * 0.69463991
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30248 * 0.36653576
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50714 * 0.92847464
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74327 * 0.35760862
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16437 * 0.93258188
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17573 * 0.93731466
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39062 * 0.42494299
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39031 * 0.30224195
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31811 * 0.06642408
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'wyynooyc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0036():
    """Extended test 36 for aggregation."""
    x_0 = 43585 * 0.01035482
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41785 * 0.67929343
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96674 * 0.75806683
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89762 * 0.93620997
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48344 * 0.25266497
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36353 * 0.56200353
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87207 * 0.71801184
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23860 * 0.54644167
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70550 * 0.35559976
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48008 * 0.70483975
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92691 * 0.66875953
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72175 * 0.33337969
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71502 * 0.01631718
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71027 * 0.34436621
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25114 * 0.53819735
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35744 * 0.36382066
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95956 * 0.32014930
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91913 * 0.15691298
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6706 * 0.94500771
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69020 * 0.97340612
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13379 * 0.70960560
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1945 * 0.40539336
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59174 * 0.76601449
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40593 * 0.95012896
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60744 * 0.85917059
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84343 * 0.60230287
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10725 * 0.85959813
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50002 * 0.05333890
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90225 * 0.56320815
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11199 * 0.93815014
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41982 * 0.69483103
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81469 * 0.53990320
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28521 * 0.95457879
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31856 * 0.74700539
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19607 * 0.44058629
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85458 * 0.08125224
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 77088 * 0.62716247
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44320 * 0.10456178
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19581 * 0.20692752
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76712 * 0.42439253
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46344 * 0.00860578
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6560 * 0.14011463
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 43075 * 0.10784312
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 29639 * 0.57785694
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50095 * 0.99769800
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 506 * 0.15232670
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'fsomlxrt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0037():
    """Extended test 37 for aggregation."""
    x_0 = 21596 * 0.64631489
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30532 * 0.95674402
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95319 * 0.87333023
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69972 * 0.17648822
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81213 * 0.03558685
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73998 * 0.41828191
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93902 * 0.34723899
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33666 * 0.61364476
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6470 * 0.82090320
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44928 * 0.83962220
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21008 * 0.99077383
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62559 * 0.02161975
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88164 * 0.58707065
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84154 * 0.12812588
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26461 * 0.17787723
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2251 * 0.84735548
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18859 * 0.73606179
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19690 * 0.16595110
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95001 * 0.05855297
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41116 * 0.02396641
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54229 * 0.80584496
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37258 * 0.53038680
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93244 * 0.96950905
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75309 * 0.08425316
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34766 * 0.05753018
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91876 * 0.72385847
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40703 * 0.71399969
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7654 * 0.38332576
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81084 * 0.32079944
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84127 * 0.08234170
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31750 * 0.39242879
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38817 * 0.83209207
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35836 * 0.06740775
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47458 * 0.76357199
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79458 * 0.91304214
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37113 * 0.07590900
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46723 * 0.04200762
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58073 * 0.60149169
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26974 * 0.40389911
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31135 * 0.93798283
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82830 * 0.78428052
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 23886 * 0.33350848
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 32047 * 0.68775306
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 70860 * 0.03034300
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'stotueen').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0038():
    """Extended test 38 for aggregation."""
    x_0 = 58588 * 0.57890886
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38310 * 0.19009654
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18824 * 0.51111271
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2179 * 0.93569093
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74226 * 0.19823031
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50486 * 0.61203606
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14898 * 0.72095980
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57797 * 0.99760927
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72812 * 0.92285583
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20829 * 0.11222681
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66448 * 0.89901769
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31723 * 0.40027306
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33928 * 0.02255596
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56480 * 0.22733547
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62807 * 0.76900210
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12803 * 0.27550580
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85911 * 0.31873351
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2051 * 0.37854196
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31394 * 0.93931955
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62169 * 0.29436988
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57032 * 0.16563148
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15613 * 0.16703420
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38633 * 0.74918555
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4595 * 0.62681821
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96151 * 0.11733619
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13133 * 0.91799757
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'fqyjjggu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0039():
    """Extended test 39 for aggregation."""
    x_0 = 29470 * 0.47575626
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5340 * 0.26698077
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39679 * 0.30083036
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 552 * 0.58768135
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47184 * 0.39414497
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65740 * 0.14051683
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30760 * 0.05368197
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88644 * 0.06069729
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98636 * 0.05628159
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26206 * 0.48791217
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62552 * 0.39179250
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97102 * 0.91311446
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40487 * 0.58652301
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64733 * 0.67718484
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70413 * 0.67996486
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42866 * 0.97998226
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9137 * 0.53671279
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65169 * 0.60351398
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22720 * 0.48646527
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35074 * 0.48618887
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9993 * 0.17464539
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45634 * 0.05954068
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65099 * 0.80146577
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46695 * 0.23595134
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17160 * 0.62257312
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40918 * 0.57674071
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45773 * 0.97572136
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99481 * 0.01504003
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1947 * 0.91628379
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59021 * 0.72360120
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79451 * 0.14676597
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37205 * 0.19055195
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68305 * 0.91467760
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82991 * 0.32298807
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13261 * 0.36014653
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60999 * 0.53446378
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31824 * 0.08054687
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13048 * 0.23276240
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81627 * 0.80725168
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94561 * 0.95131334
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'tmwynupe').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0040():
    """Extended test 40 for aggregation."""
    x_0 = 83645 * 0.51200808
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56104 * 0.80884813
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67029 * 0.56536299
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52602 * 0.07059256
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48106 * 0.31540469
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9435 * 0.79645833
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38497 * 0.34893674
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62506 * 0.43085436
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22311 * 0.32954138
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76283 * 0.11481215
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92375 * 0.20877294
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31909 * 0.67533754
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84448 * 0.61724102
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41422 * 0.72358472
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9984 * 0.13655243
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8289 * 0.06455072
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21757 * 0.01351604
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79176 * 0.17164990
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5765 * 0.24908919
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94446 * 0.24700262
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'jujajnqi').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0041():
    """Extended test 41 for aggregation."""
    x_0 = 88329 * 0.88393668
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39032 * 0.94282409
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95438 * 0.06131717
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84031 * 0.65515531
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16779 * 0.16977057
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51340 * 0.14184547
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89961 * 0.76837728
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66553 * 0.43548702
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63226 * 0.45960602
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78302 * 0.20198930
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15673 * 0.28854325
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1900 * 0.68972815
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81786 * 0.45567298
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3033 * 0.31573838
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89934 * 0.73419356
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71703 * 0.80201843
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64849 * 0.15685355
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83716 * 0.47502938
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95445 * 0.90684782
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9871 * 0.42048252
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90961 * 0.08450994
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21486 * 0.79566210
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3718 * 0.34365263
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40687 * 0.61180676
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8923 * 0.27487574
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'frijokvy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0042():
    """Extended test 42 for aggregation."""
    x_0 = 18563 * 0.43351249
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55182 * 0.64464489
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31368 * 0.41676388
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1744 * 0.41981036
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43555 * 0.57951342
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14637 * 0.47755687
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6911 * 0.50552332
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99589 * 0.56971394
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49415 * 0.41886268
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43214 * 0.46150971
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69613 * 0.09856622
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8590 * 0.61023387
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8174 * 0.20367148
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53603 * 0.76416542
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38093 * 0.74222548
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5472 * 0.01920065
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17552 * 0.72502651
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16241 * 0.81467409
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68103 * 0.97070683
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52732 * 0.66225177
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94247 * 0.21478420
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25909 * 0.32558728
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73231 * 0.42507888
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37352 * 0.69113712
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39672 * 0.88257860
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92118 * 0.36327733
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53689 * 0.60880893
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67676 * 0.32338181
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81075 * 0.14963920
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'avivbbgh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0043():
    """Extended test 43 for aggregation."""
    x_0 = 4382 * 0.20057781
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19502 * 0.27134174
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13891 * 0.28975229
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30879 * 0.60857224
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57636 * 0.94319246
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84816 * 0.26935413
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75849 * 0.84151483
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70266 * 0.96375775
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63911 * 0.10402318
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40085 * 0.09957745
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26811 * 0.17009832
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62756 * 0.75148135
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72047 * 0.25587626
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62652 * 0.76390536
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71486 * 0.56748197
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30651 * 0.96649502
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72932 * 0.24357994
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81144 * 0.43762804
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9360 * 0.59582994
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70604 * 0.22030719
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97454 * 0.14933478
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55259 * 0.45628433
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9095 * 0.34192186
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16197 * 0.97847273
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68053 * 0.71070753
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37601 * 0.00710840
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56766 * 0.84811773
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9127 * 0.37455838
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97826 * 0.12244880
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75887 * 0.85105458
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55733 * 0.78335419
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80683 * 0.01306056
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47317 * 0.84787498
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ycmtsysz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0044():
    """Extended test 44 for aggregation."""
    x_0 = 91394 * 0.87149206
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41184 * 0.49059385
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36334 * 0.42218399
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20660 * 0.21703986
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92442 * 0.15305187
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27692 * 0.22344318
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41241 * 0.33529277
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47447 * 0.55604081
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44499 * 0.52183580
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10730 * 0.31300201
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87040 * 0.04012377
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12680 * 0.80390948
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32095 * 0.04643470
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63090 * 0.74065387
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79117 * 0.23270365
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51848 * 0.88635211
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75131 * 0.56256898
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7306 * 0.10029560
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13354 * 0.14809128
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90521 * 0.12562628
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43476 * 0.91996692
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4524 * 0.87738748
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44493 * 0.52547698
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'opoelmyv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0045():
    """Extended test 45 for aggregation."""
    x_0 = 89309 * 0.95011644
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 670 * 0.92957241
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48999 * 0.34136724
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79953 * 0.02925859
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18233 * 0.57341491
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90155 * 0.24813983
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10419 * 0.98760665
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23756 * 0.46593201
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39227 * 0.05697484
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46261 * 0.62533502
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20427 * 0.50045488
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58176 * 0.82275839
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53218 * 0.98789256
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42939 * 0.04773127
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57994 * 0.29892172
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19495 * 0.92850005
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58536 * 0.31845268
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7448 * 0.29694161
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58720 * 0.65612423
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27983 * 0.26233364
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73017 * 0.67217217
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10457 * 0.38893366
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74348 * 0.58322283
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5015 * 0.59817552
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2085 * 0.67773040
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78621 * 0.59440152
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7374 * 0.24246188
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41603 * 0.77403111
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6694 * 0.81064943
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59328 * 0.18525198
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66655 * 0.13638408
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29933 * 0.34185616
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96176 * 0.67752950
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62270 * 0.82192424
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95805 * 0.14132409
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'isbwadic').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0046():
    """Extended test 46 for aggregation."""
    x_0 = 24139 * 0.57075938
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37221 * 0.72671554
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35342 * 0.74137919
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84480 * 0.59765785
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37156 * 0.19475927
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2808 * 0.37336611
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88649 * 0.27319057
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32797 * 0.87670150
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20871 * 0.87108316
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87027 * 0.10443361
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62866 * 0.84561039
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19247 * 0.45505607
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51941 * 0.34808847
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21177 * 0.43052977
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5535 * 0.10609369
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60433 * 0.74106636
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97257 * 0.87830654
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20637 * 0.75547707
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81430 * 0.32745279
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83330 * 0.68620882
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59279 * 0.74637223
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60280 * 0.83214056
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93796 * 0.72620716
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60476 * 0.74325019
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20178 * 0.78326870
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35374 * 0.10887735
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36340 * 0.09259545
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46743 * 0.66930466
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98757 * 0.56392464
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12663 * 0.83659074
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14360 * 0.65982138
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21494 * 0.96320403
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58513 * 0.78921810
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53207 * 0.41993043
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53731 * 0.48193507
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60598 * 0.18819898
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95019 * 0.24223978
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98587 * 0.65259123
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19823 * 0.32147971
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81469 * 0.55797558
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91304 * 0.48366470
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 76588 * 0.35563764
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83229 * 0.63557391
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 67208 * 0.96776260
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 49844 * 0.66343260
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26382 * 0.87206509
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 1602 * 0.66725755
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 76642 * 0.03114130
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 69688 * 0.30426034
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 74587 * 0.82577313
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'fymdaxnq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0047():
    """Extended test 47 for aggregation."""
    x_0 = 60497 * 0.00036119
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67456 * 0.40603383
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41338 * 0.63950188
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18079 * 0.22389987
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10820 * 0.45496084
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13166 * 0.17669605
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24219 * 0.27394531
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36389 * 0.71493366
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28691 * 0.71299621
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85995 * 0.41453151
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15384 * 0.66704985
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70152 * 0.39294408
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88018 * 0.65680199
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64449 * 0.44788385
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12985 * 0.13304200
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95651 * 0.12335469
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33268 * 0.00324381
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27806 * 0.01866432
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13616 * 0.61838077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31456 * 0.67851652
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14990 * 0.95625468
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50244 * 0.26646381
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7574 * 0.66129250
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77838 * 0.42217024
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 107 * 0.04279357
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27072 * 0.22877005
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6823 * 0.94737090
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80646 * 0.63086461
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73304 * 0.79586807
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96044 * 0.29190074
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64072 * 0.39635603
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70134 * 0.67697155
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'rguurvkg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0048():
    """Extended test 48 for aggregation."""
    x_0 = 40654 * 0.28589100
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20269 * 0.91606010
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89805 * 0.95514351
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68984 * 0.68086339
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88573 * 0.05815270
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90141 * 0.36477365
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56290 * 0.29769876
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94007 * 0.89048436
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48535 * 0.30468620
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43252 * 0.49930764
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36549 * 0.23043428
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65062 * 0.71010587
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55246 * 0.86698151
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13917 * 0.66095053
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6476 * 0.99859355
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48978 * 0.76577287
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7811 * 0.82356425
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93095 * 0.58389292
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52661 * 0.70924001
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49810 * 0.82889393
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3687 * 0.63508974
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13405 * 0.45286611
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15929 * 0.57793519
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66729 * 0.20779117
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76093 * 0.25042174
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29297 * 0.10681190
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41663 * 0.16353762
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75265 * 0.79795783
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44634 * 0.51764677
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26945 * 0.13033605
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39153 * 0.83796986
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65658 * 0.08773953
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96304 * 0.98882024
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 189 * 0.91918421
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76821 * 0.94756945
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98864 * 0.80133660
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51323 * 0.41397579
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'vadvcquw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0049():
    """Extended test 49 for aggregation."""
    x_0 = 87463 * 0.12703407
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88432 * 0.46868737
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92792 * 0.51644089
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45245 * 0.94991326
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79492 * 0.46965826
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68117 * 0.49428945
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65974 * 0.33591641
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37429 * 0.30541268
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71161 * 0.22569556
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22744 * 0.86879714
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46924 * 0.25425760
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4950 * 0.86554126
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86386 * 0.75118963
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30245 * 0.16345305
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84527 * 0.26302048
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52431 * 0.74667783
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61335 * 0.26870185
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8019 * 0.09397383
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92614 * 0.79454777
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57291 * 0.15507027
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45628 * 0.47833203
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86066 * 0.36217513
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6622 * 0.28610094
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3574 * 0.61981027
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51248 * 0.00667501
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19596 * 0.86529010
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86366 * 0.54126598
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89363 * 0.58830918
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65090 * 0.65691524
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15210 * 0.55989631
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2645 * 0.95696086
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22767 * 0.31477005
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99588 * 0.97339728
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10209 * 0.98242997
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65745 * 0.88171552
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32678 * 0.74259576
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18619 * 0.74576658
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'cnokqcnw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0050():
    """Extended test 50 for aggregation."""
    x_0 = 89905 * 0.46929042
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77978 * 0.67524646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58624 * 0.95988889
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22396 * 0.70487180
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46651 * 0.38486683
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76793 * 0.96056846
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49535 * 0.62000208
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90808 * 0.39431486
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87190 * 0.68961260
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24687 * 0.59030976
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23000 * 0.98025860
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51279 * 0.12445327
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89044 * 0.61873597
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53319 * 0.25716756
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58007 * 0.42207508
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16234 * 0.26182151
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35116 * 0.83586347
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60466 * 0.93702801
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76513 * 0.69327665
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38797 * 0.87936112
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42675 * 0.80186965
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74688 * 0.37044516
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17248 * 0.90938758
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21372 * 0.61527136
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3753 * 0.74476216
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23731 * 0.11508478
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86532 * 0.21290943
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66118 * 0.26739953
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6054 * 0.14420954
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59202 * 0.47928072
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93074 * 0.10010362
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42105 * 0.44579406
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49030 * 0.60692704
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90328 * 0.18177311
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60727 * 0.00986098
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21468 * 0.12211393
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81853 * 0.13096281
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'iovonsio').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0051():
    """Extended test 51 for aggregation."""
    x_0 = 71110 * 0.65464547
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34933 * 0.03199366
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14483 * 0.03518996
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11867 * 0.45300316
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22817 * 0.12215318
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65954 * 0.98516163
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57462 * 0.83131760
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70054 * 0.57972198
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87216 * 0.30277278
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23637 * 0.64300602
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79254 * 0.59664472
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27917 * 0.02696870
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44665 * 0.79525281
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37637 * 0.94783470
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93466 * 0.55231339
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62181 * 0.75805148
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43880 * 0.54656057
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14581 * 0.81186966
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48909 * 0.94708703
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78026 * 0.92104465
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86436 * 0.34276385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20538 * 0.86214327
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61582 * 0.37233686
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99997 * 0.49106748
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5368 * 0.22989498
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15935 * 0.25532430
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73706 * 0.98059724
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10707 * 0.65939306
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26141 * 0.80137732
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7191 * 0.73240663
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6852 * 0.58245433
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42287 * 0.95290280
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'kqiaania').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0052():
    """Extended test 52 for aggregation."""
    x_0 = 46756 * 0.10325339
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51761 * 0.47269821
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31221 * 0.40461617
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32300 * 0.77680223
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41542 * 0.12178039
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97526 * 0.96191246
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73555 * 0.82219157
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29522 * 0.36784200
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74049 * 0.68306858
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95803 * 0.05662148
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19430 * 0.46055694
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94317 * 0.60283124
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3325 * 0.06732840
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28384 * 0.54357666
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73756 * 0.15761133
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12471 * 0.03556106
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9652 * 0.13845342
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5066 * 0.21643985
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77143 * 0.64627217
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6936 * 0.36500248
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17412 * 0.78284044
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43127 * 0.81442746
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20918 * 0.98184027
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80658 * 0.37695494
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71956 * 0.81967036
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18431 * 0.30278013
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93350 * 0.08926960
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93411 * 0.14468287
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35129 * 0.11635497
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76187 * 0.31319030
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45415 * 0.96668854
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75651 * 0.30861425
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58895 * 0.78500561
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20083 * 0.01446165
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72015 * 0.63341884
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83070 * 0.85189174
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51638 * 0.89528058
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30786 * 0.97594058
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77313 * 0.17367841
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2704 * 0.39210621
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'sqfnsfft').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0053():
    """Extended test 53 for aggregation."""
    x_0 = 52397 * 0.81125557
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8088 * 0.66985143
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45549 * 0.79893388
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29659 * 0.64052870
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92108 * 0.04176623
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26496 * 0.66750918
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40314 * 0.04606787
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26330 * 0.29235970
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19007 * 0.64250396
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54188 * 0.42291118
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84262 * 0.89101662
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10325 * 0.48766109
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21524 * 0.24174563
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88246 * 0.99178574
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42405 * 0.59124500
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1139 * 0.57510466
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28578 * 0.20021858
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67677 * 0.74773428
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62296 * 0.57535346
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96360 * 0.81582291
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53972 * 0.16087862
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7323 * 0.59205961
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83541 * 0.15539188
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98601 * 0.81730198
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98834 * 0.78202397
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13833 * 0.76175804
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10735 * 0.08576772
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93565 * 0.88593074
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64457 * 0.78776231
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98751 * 0.39368528
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11948 * 0.10791369
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7916 * 0.94851212
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94347 * 0.33497697
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11467 * 0.44139991
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11025 * 0.45573474
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54512 * 0.15256235
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42619 * 0.18457117
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60530 * 0.32681601
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96817 * 0.91797340
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19505 * 0.06821576
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32326 * 0.01331075
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 75499 * 0.59752561
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6634 * 0.35539113
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'oqubgsjc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0054():
    """Extended test 54 for aggregation."""
    x_0 = 7547 * 0.69182629
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84584 * 0.44194057
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20999 * 0.74396808
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79413 * 0.39302396
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35394 * 0.23375237
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50669 * 0.83137737
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42355 * 0.20880205
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10864 * 0.51809170
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53564 * 0.46293136
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26096 * 0.23680911
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78027 * 0.34934774
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 678 * 0.44362279
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45455 * 0.53178397
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1178 * 0.02523478
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44514 * 0.88796467
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81442 * 0.74793919
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48755 * 0.30572510
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85748 * 0.30061236
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98447 * 0.88729262
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58272 * 0.19419132
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17046 * 0.75480775
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86418 * 0.56842330
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25064 * 0.13884464
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58508 * 0.69407574
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53908 * 0.62016309
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76689 * 0.73745363
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90953 * 0.89826895
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80763 * 0.94059365
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61145 * 0.31629529
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17308 * 0.80321043
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67996 * 0.71129943
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8990 * 0.59993492
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67961 * 0.21060363
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96620 * 0.44493660
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85787 * 0.41288292
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 9123 * 0.18288481
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22272 * 0.98036152
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73224 * 0.05704815
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31532 * 0.77581471
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19804 * 0.76631965
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 24120 * 0.01916918
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16710 * 0.67028392
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24506 * 0.92576310
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'chvnijtn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0055():
    """Extended test 55 for aggregation."""
    x_0 = 34614 * 0.97137994
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88401 * 0.46778508
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20637 * 0.47005449
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72385 * 0.12782390
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36308 * 0.20663035
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49669 * 0.66826516
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9816 * 0.04317802
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3145 * 0.15375414
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30559 * 0.74830756
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81470 * 0.03161259
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77658 * 0.10360735
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29759 * 0.38693212
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22966 * 0.50235448
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80962 * 0.08405748
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98411 * 0.10029023
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25783 * 0.90289576
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45156 * 0.19608918
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25616 * 0.64430272
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53710 * 0.44373382
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42056 * 0.95596145
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68122 * 0.43923545
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4113 * 0.29205797
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3024 * 0.47340846
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48833 * 0.71549166
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57695 * 0.17912795
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29887 * 0.48294354
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15343 * 0.62746983
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57233 * 0.65263473
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74064 * 0.04178891
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29062 * 0.25577145
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88158 * 0.47464518
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56243 * 0.98450146
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'jrvwcxcb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0056():
    """Extended test 56 for aggregation."""
    x_0 = 65225 * 0.47698871
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93608 * 0.44704417
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64834 * 0.83293974
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92269 * 0.96912233
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11596 * 0.15208666
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74011 * 0.09864529
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90809 * 0.49892190
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12850 * 0.03445071
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97933 * 0.33887637
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95626 * 0.74421061
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58409 * 0.87602921
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57231 * 0.87948971
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17983 * 0.91620241
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79226 * 0.84512526
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48847 * 0.97636050
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88082 * 0.45278317
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29744 * 0.23621707
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15211 * 0.95537506
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97426 * 0.21805168
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16635 * 0.21048249
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67436 * 0.50665252
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50698 * 0.35875259
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22099 * 0.14108437
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78072 * 0.61371112
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61573 * 0.94100974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6773 * 0.71369277
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33781 * 0.85761697
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13616 * 0.35060054
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40187 * 0.56272152
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28233 * 0.43306572
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1558 * 0.42631911
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26993 * 0.16344186
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10994 * 0.94930177
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57766 * 0.46610994
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76368 * 0.68647517
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24017 * 0.89222115
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'njblfsyy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0057():
    """Extended test 57 for aggregation."""
    x_0 = 43752 * 0.07284266
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32833 * 0.13949167
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60822 * 0.57240813
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41401 * 0.68818053
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31144 * 0.23143470
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14293 * 0.23605469
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3150 * 0.32184397
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40735 * 0.10403609
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56468 * 0.41134082
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35544 * 0.70880915
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38046 * 0.14278677
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14636 * 0.03310623
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63595 * 0.20288243
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61488 * 0.75749778
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43890 * 0.72387941
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32441 * 0.91065375
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60471 * 0.39746494
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83743 * 0.12681979
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89110 * 0.59627719
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38833 * 0.82163844
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15760 * 0.39376223
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47061 * 0.58424076
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37820 * 0.27364208
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37679 * 0.35521079
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53182 * 0.69494029
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20115 * 0.67739415
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48607 * 0.42331993
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80219 * 0.84172520
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58842 * 0.30141687
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32167 * 0.96364800
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67262 * 0.54008482
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15943 * 0.29977789
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58761 * 0.43649269
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22548 * 0.15807997
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76895 * 0.28727204
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16641 * 0.61834255
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27988 * 0.78834047
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47069 * 0.56106662
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30024 * 0.78927212
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65055 * 0.46587361
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95063 * 0.06890469
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63035 * 0.49226765
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 34628 * 0.58922938
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 48731 * 0.17153585
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 69327 * 0.41900002
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 81655 * 0.53561104
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'cbqafqzg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0058():
    """Extended test 58 for aggregation."""
    x_0 = 41468 * 0.73574253
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18338 * 0.20403759
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8388 * 0.04680498
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22661 * 0.18473901
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62742 * 0.63453206
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63254 * 0.19601795
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60120 * 0.06540209
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64677 * 0.91932985
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22300 * 0.71053712
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91760 * 0.23679907
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7765 * 0.45036599
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15691 * 0.42633188
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18128 * 0.71838659
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96460 * 0.77978267
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65903 * 0.58547748
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59790 * 0.16097988
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87332 * 0.17995011
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52794 * 0.27197585
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98876 * 0.89647937
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48947 * 0.17860667
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16778 * 0.43452129
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89276 * 0.21665012
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56425 * 0.74308322
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74776 * 0.21133156
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81517 * 0.15204634
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11322 * 0.31104290
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40422 * 0.35115875
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14015 * 0.78620516
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93538 * 0.50892709
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14399 * 0.95861118
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90520 * 0.57041194
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90222 * 0.85297361
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75028 * 0.45237793
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52910 * 0.96438091
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 105 * 0.06726327
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28829 * 0.36004819
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66510 * 0.49204217
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52372 * 0.04099466
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5758 * 0.00933579
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65618 * 0.71342007
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75114 * 0.59041251
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67878 * 0.88201631
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16016 * 0.17262696
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94054 * 0.28429026
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71967 * 0.73021602
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'guuctymz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0059():
    """Extended test 59 for aggregation."""
    x_0 = 48889 * 0.66721824
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61460 * 0.75425224
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33346 * 0.67872582
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49141 * 0.17101351
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37066 * 0.10196766
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68974 * 0.35489174
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47364 * 0.92938023
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56944 * 0.86449533
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52537 * 0.75420093
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8188 * 0.49369022
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53514 * 0.10406158
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13627 * 0.57985188
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97264 * 0.45641996
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85613 * 0.23892585
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41688 * 0.48288007
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88439 * 0.67493607
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34297 * 0.88684521
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1308 * 0.95784923
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91704 * 0.62445398
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92926 * 0.24939481
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81547 * 0.13666102
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56831 * 0.11400774
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79359 * 0.81095940
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58073 * 0.47150116
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72407 * 0.04226626
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41108 * 0.55535136
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11161 * 0.06365007
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5993 * 0.14586615
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43204 * 0.18214954
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74661 * 0.60816381
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34581 * 0.09502955
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59650 * 0.94377925
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80720 * 0.35834985
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32615 * 0.79916781
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94037 * 0.44008343
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95707 * 0.45752724
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'otjwoqqt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0060():
    """Extended test 60 for aggregation."""
    x_0 = 78933 * 0.38751765
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8706 * 0.43588351
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78175 * 0.57609673
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31551 * 0.65835822
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37545 * 0.15683421
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48262 * 0.74429700
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93991 * 0.17257134
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98121 * 0.97519269
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15892 * 0.87638267
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20248 * 0.14337981
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52964 * 0.12417463
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82201 * 0.03335863
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23292 * 0.50997933
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79617 * 0.04461072
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15457 * 0.65611208
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50108 * 0.00905503
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75562 * 0.86045875
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42561 * 0.32844352
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94604 * 0.09095690
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46526 * 0.88342997
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69768 * 0.03843092
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81347 * 0.66027737
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20509 * 0.76428537
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99062 * 0.59631624
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21406 * 0.30707117
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53959 * 0.38989288
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43837 * 0.68452814
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38633 * 0.99035741
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55312 * 0.02390589
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71252 * 0.71174478
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12394 * 0.79193056
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94932 * 0.53982867
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71875 * 0.74473846
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60597 * 0.82714090
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30130 * 0.62899144
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'intglcso').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0061():
    """Extended test 61 for aggregation."""
    x_0 = 37981 * 0.73998929
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15543 * 0.67959017
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85798 * 0.71776634
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71467 * 0.00032639
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21572 * 0.55900570
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95182 * 0.67695162
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24144 * 0.21734288
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78587 * 0.60950774
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54651 * 0.66444617
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71292 * 0.40086835
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70322 * 0.07806744
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90225 * 0.58756816
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35325 * 0.67619150
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15294 * 0.57421174
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81278 * 0.48943386
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97419 * 0.92520389
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79093 * 0.63645467
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76560 * 0.02504031
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14213 * 0.89832380
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8911 * 0.42341865
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62989 * 0.05324670
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98074 * 0.93527550
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19752 * 0.79437936
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36602 * 0.04622828
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89299 * 0.34245160
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20430 * 0.89380605
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43680 * 0.27365090
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15186 * 0.64032188
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96278 * 0.73599260
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73283 * 0.52778016
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62192 * 0.97272473
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89846 * 0.26050715
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70938 * 0.07460238
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31086 * 0.50909262
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'yjsfdolf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0062():
    """Extended test 62 for aggregation."""
    x_0 = 97284 * 0.07512172
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47210 * 0.28426734
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50263 * 0.89174249
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55034 * 0.35706078
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63874 * 0.76134738
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42600 * 0.69758333
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99861 * 0.01153516
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53720 * 0.08710526
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53217 * 0.74756002
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55287 * 0.26129456
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61765 * 0.24470304
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86992 * 0.21273460
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6998 * 0.63012418
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81731 * 0.65096970
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31674 * 0.67231126
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83501 * 0.07524251
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88578 * 0.40478335
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70775 * 0.09695535
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81558 * 0.88424539
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93605 * 0.78955332
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49981 * 0.63757139
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53762 * 0.95300556
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10689 * 0.57137390
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35844 * 0.70529783
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92288 * 0.58259165
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13949 * 0.96126849
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58638 * 0.43928141
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9590 * 0.79684606
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52391 * 0.36564621
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47666 * 0.12662418
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78246 * 0.03370185
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33898 * 0.14321843
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36473 * 0.82874791
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68974 * 0.04953816
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1750 * 0.11430144
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91159 * 0.46354092
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57734 * 0.36959119
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42412 * 0.98424073
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66831 * 0.62544538
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76972 * 0.58293677
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'drvzysmo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0063():
    """Extended test 63 for aggregation."""
    x_0 = 69300 * 0.22118914
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63366 * 0.69950180
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31714 * 0.21923611
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34615 * 0.77703134
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59817 * 0.49921683
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4735 * 0.99887990
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81963 * 0.12650584
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4078 * 0.30580727
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84737 * 0.23935243
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22444 * 0.58139818
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23143 * 0.75484886
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61413 * 0.31992909
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52208 * 0.35597450
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41218 * 0.33032374
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83737 * 0.83298578
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97593 * 0.80011240
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27124 * 0.56710742
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89770 * 0.31648099
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35020 * 0.69168712
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82772 * 0.87393256
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50594 * 0.89465223
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30957 * 0.52472081
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82845 * 0.40516196
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2859 * 0.86794390
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2053 * 0.51258856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31732 * 0.79041213
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 328 * 0.19749305
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'knzqefib').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0064():
    """Extended test 64 for aggregation."""
    x_0 = 27530 * 0.51678442
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43423 * 0.36022008
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61339 * 0.77011155
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67625 * 0.45332182
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4913 * 0.59286034
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92865 * 0.83593199
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28332 * 0.43630533
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83710 * 0.02723898
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79255 * 0.12058684
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89516 * 0.78820955
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69905 * 0.62688246
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86333 * 0.91017236
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98655 * 0.56276043
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15322 * 0.58546123
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46865 * 0.71549010
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34242 * 0.54295120
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68374 * 0.69226067
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9083 * 0.86846666
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68235 * 0.77702002
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47582 * 0.50119213
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57554 * 0.53093797
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23005 * 0.00608974
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93472 * 0.64904039
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90398 * 0.83546442
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36376 * 0.37419574
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36202 * 0.97275235
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49164 * 0.19130007
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49622 * 0.08533139
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14113 * 0.83599888
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78298 * 0.34703298
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84323 * 0.37631240
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49267 * 0.15230030
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17146 * 0.73257002
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70037 * 0.73420725
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82470 * 0.15130265
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'fqpvmduu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0065():
    """Extended test 65 for aggregation."""
    x_0 = 54595 * 0.99812428
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5879 * 0.78011084
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17664 * 0.66367827
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80119 * 0.06114129
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67651 * 0.69203184
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27926 * 0.55436818
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98886 * 0.94914156
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19070 * 0.83542858
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93103 * 0.23804802
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34767 * 0.29646557
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47280 * 0.19778400
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73353 * 0.03835960
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73853 * 0.45359245
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17173 * 0.01332408
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52302 * 0.64424213
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86033 * 0.50163262
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34367 * 0.69624449
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42577 * 0.74637568
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32450 * 0.78804922
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80007 * 0.74161793
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28043 * 0.98414528
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84144 * 0.34483039
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87977 * 0.37642584
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10792 * 0.30442652
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35132 * 0.10113833
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5831 * 0.90237978
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9080 * 0.77205979
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82693 * 0.18891571
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68205 * 0.97354001
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'yajsbvoj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0066():
    """Extended test 66 for aggregation."""
    x_0 = 5892 * 0.97542830
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69107 * 0.64157777
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71332 * 0.05414329
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66750 * 0.42803191
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97307 * 0.30905677
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59513 * 0.97669066
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50753 * 0.98842045
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39461 * 0.44245551
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7920 * 0.88776210
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83301 * 0.79023981
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8343 * 0.47381223
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36299 * 0.07590957
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75159 * 0.78229576
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3940 * 0.68191476
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39893 * 0.51867581
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9426 * 0.92902110
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17932 * 0.97483202
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78375 * 0.18370212
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98129 * 0.06284816
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74729 * 0.54429400
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97704 * 0.79921530
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98030 * 0.66576963
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8581 * 0.59119842
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46207 * 0.97016745
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42434 * 0.74709982
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20529 * 0.50392832
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66429 * 0.90127271
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ogprmlvt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0067():
    """Extended test 67 for aggregation."""
    x_0 = 18738 * 0.03516168
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19397 * 0.77391089
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41482 * 0.02540658
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46615 * 0.42673168
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43597 * 0.91360141
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81048 * 0.08457545
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45832 * 0.83353409
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84892 * 0.78212251
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55351 * 0.50238014
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51349 * 0.51461178
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26794 * 0.20698439
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28722 * 0.14770451
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18397 * 0.21867568
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45420 * 0.25524076
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38484 * 0.53454032
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96529 * 0.29587077
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1735 * 0.73708433
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63901 * 0.61611682
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62321 * 0.96042045
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99303 * 0.23790953
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'tfncirqp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0068():
    """Extended test 68 for aggregation."""
    x_0 = 51645 * 0.64182702
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43815 * 0.18457802
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42432 * 0.53251403
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92108 * 0.11543292
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1013 * 0.29032068
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39619 * 0.42875118
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77758 * 0.26976020
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17595 * 0.44595858
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92076 * 0.40812198
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95962 * 0.24024232
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22774 * 0.15011420
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14650 * 0.87097188
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25332 * 0.14201072
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9052 * 0.56568226
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21387 * 0.11419899
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64157 * 0.48616722
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21046 * 0.79359582
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89262 * 0.18653585
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29356 * 0.05261073
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19697 * 0.26200664
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3872 * 0.48563982
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17888 * 0.53025338
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1308 * 0.80067887
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62892 * 0.66044513
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56827 * 0.11941799
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43015 * 0.96485050
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79986 * 0.03801660
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1783 * 0.00409753
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5106 * 0.64029598
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85939 * 0.93985935
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55689 * 0.51220819
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92399 * 0.28901024
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64133 * 0.67126732
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55009 * 0.14283846
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45688 * 0.18334518
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95633 * 0.68404833
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20326 * 0.24275360
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91160 * 0.98987355
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76902 * 0.34390805
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81793 * 0.16746963
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'dsubpcgs').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_1_0069():
    """Extended test 69 for aggregation."""
    x_0 = 12793 * 0.89224375
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70669 * 0.61163275
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66599 * 0.70127783
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75093 * 0.91120886
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33922 * 0.27078129
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64885 * 0.62429120
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23090 * 0.88897115
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51738 * 0.02184792
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18296 * 0.35531301
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31565 * 0.44246135
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18314 * 0.33557395
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62917 * 0.78596358
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86796 * 0.23284702
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53168 * 0.63084885
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72163 * 0.12483006
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91556 * 0.97996157
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61821 * 0.82750556
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5269 * 0.38576125
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60891 * 0.51918982
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74732 * 0.70866007
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78348 * 0.37983696
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55734 * 0.22848182
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47722 * 0.82355472
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2258 * 0.62605131
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48685 * 0.22554272
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63149 * 0.45245834
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3750 * 0.06757629
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59473 * 0.02009032
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31192 * 0.81081463
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'sdnkedbm').hexdigest()
    assert len(h) == 64
