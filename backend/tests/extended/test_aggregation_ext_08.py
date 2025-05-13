"""Extended tests for aggregation suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_aggregation_extended_8_0000():
    """Extended test 0 for aggregation."""
    x_0 = 36687 * 0.13806902
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29594 * 0.78204468
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50998 * 0.18570141
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70196 * 0.22420615
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32645 * 0.80335883
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82341 * 0.04982243
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84325 * 0.15318688
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30417 * 0.98765653
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40854 * 0.79352726
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16798 * 0.45491145
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73360 * 0.62108141
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95849 * 0.55312890
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33536 * 0.50855204
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22237 * 0.77539638
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20698 * 0.34295234
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36256 * 0.90921493
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86372 * 0.95849114
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42809 * 0.28484210
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96289 * 0.81116020
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56793 * 0.43133024
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36686 * 0.47352150
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45403 * 0.22117688
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90397 * 0.81227248
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97464 * 0.97816189
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34222 * 0.29406345
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86687 * 0.62006226
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29768 * 0.50078624
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63508 * 0.63788129
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32891 * 0.55204786
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3442 * 0.37204655
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98042 * 0.40891645
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5997 * 0.22877371
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63207 * 0.91525166
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48491 * 0.24118286
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35676 * 0.00403849
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78503 * 0.57243002
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18202 * 0.43771485
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78147 * 0.96347190
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'scpdkapi').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0001():
    """Extended test 1 for aggregation."""
    x_0 = 42354 * 0.74339144
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14027 * 0.99857953
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4398 * 0.22959728
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93081 * 0.57641904
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98841 * 0.99495217
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28375 * 0.10457537
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8834 * 0.32688210
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66308 * 0.09117867
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71724 * 0.06274608
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4068 * 0.93860866
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29916 * 0.44263997
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28918 * 0.94461874
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51118 * 0.26442316
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3107 * 0.41481908
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21913 * 0.35845820
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60074 * 0.08319317
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20563 * 0.49000558
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65229 * 0.12728001
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63489 * 0.87427513
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4137 * 0.18473360
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75443 * 0.98020888
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7961 * 0.66170861
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5667 * 0.12119331
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82576 * 0.39493438
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80918 * 0.36215990
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35259 * 0.41627875
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73354 * 0.89775188
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7656 * 0.32500707
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25005 * 0.51370506
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61321 * 0.09655922
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65579 * 0.68634272
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25130 * 0.51477156
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34580 * 0.11147979
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7310 * 0.00586199
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45767 * 0.99896133
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62554 * 0.17316599
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 453 * 0.74154858
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42446 * 0.57765092
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59926 * 0.98216445
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22821 * 0.55749148
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'bddfhyvn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0002():
    """Extended test 2 for aggregation."""
    x_0 = 27953 * 0.75312901
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6961 * 0.75348046
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37369 * 0.07948514
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24094 * 0.04428576
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60846 * 0.60007733
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32635 * 0.52191330
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36114 * 0.73485151
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12074 * 0.12643482
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65693 * 0.09626003
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52459 * 0.49516958
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93050 * 0.17996721
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71224 * 0.15270162
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71599 * 0.05027455
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20450 * 0.68343287
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43613 * 0.85501338
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16475 * 0.79206772
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85833 * 0.90951808
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3929 * 0.44295650
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59620 * 0.86260867
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20860 * 0.27577814
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48045 * 0.51527112
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40066 * 0.46778243
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20702 * 0.74509412
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85418 * 0.65313987
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53541 * 0.67358400
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24603 * 0.57528446
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3416 * 0.09940783
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14187 * 0.11290020
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10686 * 0.50534146
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4616 * 0.68278322
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96642 * 0.00143285
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50019 * 0.15329123
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41613 * 0.90397131
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'nbnqejqx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0003():
    """Extended test 3 for aggregation."""
    x_0 = 86869 * 0.75233196
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68760 * 0.49429878
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37376 * 0.61395518
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70876 * 0.38776630
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50808 * 0.52978224
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66638 * 0.86272027
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99251 * 0.55521527
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87874 * 0.79397003
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29689 * 0.99177382
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68789 * 0.04125959
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81703 * 0.50908802
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62045 * 0.56825668
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83573 * 0.10327032
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17838 * 0.40598674
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12902 * 0.69157173
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48217 * 0.96908002
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61923 * 0.74968649
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4430 * 0.39080609
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4937 * 0.26858601
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43402 * 0.52679479
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15523 * 0.34748290
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22549 * 0.59748806
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23249 * 0.25530976
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79350 * 0.51256705
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25458 * 0.74698828
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92101 * 0.32113396
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26983 * 0.45166279
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38853 * 0.49465729
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97783 * 0.67525583
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48504 * 0.75434440
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93448 * 0.74682086
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76747 * 0.35996108
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34987 * 0.40362068
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5493 * 0.36016019
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65747 * 0.60428146
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33392 * 0.04643814
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80414 * 0.83581260
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 248 * 0.98039607
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64824 * 0.11895264
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40530 * 0.10802880
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 63987 * 0.71315567
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 10671 * 0.55607478
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77655 * 0.97849678
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38306 * 0.41709118
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'ansxjblo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0004():
    """Extended test 4 for aggregation."""
    x_0 = 22478 * 0.00768847
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14499 * 0.20844277
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92648 * 0.42424438
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70707 * 0.65213470
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69380 * 0.34343227
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25000 * 0.80156503
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85909 * 0.51510370
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82244 * 0.38206115
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70289 * 0.10108311
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94154 * 0.79110774
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75745 * 0.82637326
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38582 * 0.42051423
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48774 * 0.11530570
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75977 * 0.50060529
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21317 * 0.67676562
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56871 * 0.99610700
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73762 * 0.48615174
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25647 * 0.85406140
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8416 * 0.97190996
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61823 * 0.23371356
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36592 * 0.03873335
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23352 * 0.28142152
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46444 * 0.83502552
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98057 * 0.67098448
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90943 * 0.19840467
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ocuxaqte').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0005():
    """Extended test 5 for aggregation."""
    x_0 = 4328 * 0.89983841
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63586 * 0.92104150
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87430 * 0.91353222
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34909 * 0.01727097
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5957 * 0.78205038
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68946 * 0.86185255
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4348 * 0.08336990
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87084 * 0.42417136
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78811 * 0.71557613
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32172 * 0.59438547
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73643 * 0.70564866
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56792 * 0.24542576
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85737 * 0.85066116
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17399 * 0.76153719
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50889 * 0.30900416
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37965 * 0.06591994
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5441 * 0.53366230
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47723 * 0.31975479
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83753 * 0.39743259
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63985 * 0.51922688
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89435 * 0.44641810
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9950 * 0.79676797
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49516 * 0.03798035
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90816 * 0.07173518
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97218 * 0.75706622
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77700 * 0.56089598
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23958 * 0.41398495
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56411 * 0.60214342
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72331 * 0.75382326
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73206 * 0.22094084
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26966 * 0.18318515
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74717 * 0.85650734
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34569 * 0.71182213
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58516 * 0.83960819
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57561 * 0.64224146
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22353 * 0.99109643
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52996 * 0.25644514
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74476 * 0.97712253
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47820 * 0.41666957
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9268 * 0.83216754
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62215 * 0.83328596
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92798 * 0.12666768
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95698 * 0.69551319
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22264 * 0.79517942
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'wjrkvcwd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0006():
    """Extended test 6 for aggregation."""
    x_0 = 31492 * 0.18283151
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8824 * 0.22579482
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29859 * 0.52715831
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43030 * 0.96710903
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95856 * 0.24386785
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65053 * 0.72568721
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15892 * 0.50173363
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61330 * 0.06006049
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86289 * 0.96656729
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67929 * 0.25888047
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21343 * 0.04452226
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32626 * 0.78687430
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73430 * 0.28013625
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26307 * 0.03808288
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38962 * 0.15165120
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69421 * 0.80699401
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90718 * 0.03935018
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31045 * 0.92334673
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38366 * 0.95829776
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24794 * 0.85574276
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76921 * 0.81260283
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47223 * 0.81657229
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8186 * 0.31411987
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27803 * 0.83643382
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97438 * 0.90211870
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27298 * 0.94326341
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74524 * 0.60780859
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75633 * 0.78685522
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57817 * 0.82984940
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33732 * 0.34978757
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41330 * 0.22541401
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66767 * 0.65895818
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7034 * 0.27539317
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47371 * 0.06728240
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17723 * 0.97683415
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48619 * 0.57192339
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61893 * 0.62061446
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67412 * 0.70364653
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1387 * 0.19477103
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75030 * 0.42501952
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ntgtdpnp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0007():
    """Extended test 7 for aggregation."""
    x_0 = 49235 * 0.44202173
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33802 * 0.37661508
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44104 * 0.90540719
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41624 * 0.35826373
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13317 * 0.16100756
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61577 * 0.31969588
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67752 * 0.07428549
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17842 * 0.15233777
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62576 * 0.88292541
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52010 * 0.77356876
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78875 * 0.43081413
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22780 * 0.52713627
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45766 * 0.96127070
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66270 * 0.15780721
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63895 * 0.53088989
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32088 * 0.41341443
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4464 * 0.45494634
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3583 * 0.98216496
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86165 * 0.58597545
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26650 * 0.94092961
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'epupxwbt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0008():
    """Extended test 8 for aggregation."""
    x_0 = 32673 * 0.39705433
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72234 * 0.69537191
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8853 * 0.56493629
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50886 * 0.77695865
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14580 * 0.69718426
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62588 * 0.46054175
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50780 * 0.99762463
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16195 * 0.34394804
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51314 * 0.66890420
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39439 * 0.86619062
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31009 * 0.45209528
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37855 * 0.58132304
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75432 * 0.97332924
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76713 * 0.48586485
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 157 * 0.78399909
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30896 * 0.80915461
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21740 * 0.68820025
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29465 * 0.19245793
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34564 * 0.80583614
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55383 * 0.35858674
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36698 * 0.64410144
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14998 * 0.85487222
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2612 * 0.47182998
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37108 * 0.61009739
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70354 * 0.08084801
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49481 * 0.17444614
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81575 * 0.80062776
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70373 * 0.50519106
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'glfkkdxe').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0009():
    """Extended test 9 for aggregation."""
    x_0 = 42644 * 0.07887377
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58673 * 0.64876271
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48136 * 0.82920472
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67533 * 0.55349832
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50557 * 0.38119988
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75689 * 0.56482315
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31483 * 0.33808849
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7268 * 0.56253219
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7874 * 0.45706450
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2400 * 0.63777734
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88032 * 0.26140338
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64825 * 0.33908353
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90332 * 0.37876678
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40194 * 0.89885679
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45024 * 0.09048951
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96813 * 0.59154663
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48650 * 0.56938244
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54042 * 0.22867428
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24233 * 0.52805938
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80089 * 0.43480837
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34051 * 0.30188998
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28331 * 0.56823504
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6007 * 0.97785132
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58555 * 0.98100791
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46999 * 0.52944914
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93596 * 0.80447941
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24634 * 0.75581477
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7636 * 0.15536545
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20238 * 0.97362255
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92567 * 0.68159240
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10818 * 0.77816328
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40924 * 0.81135610
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32302 * 0.43188867
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16349 * 0.22199868
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70213 * 0.45704528
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29184 * 0.21918768
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24864 * 0.72238192
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 76230 * 0.28398403
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 50881 * 0.41538972
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44397 * 0.14163632
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'hihkdlhe').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0010():
    """Extended test 10 for aggregation."""
    x_0 = 57123 * 0.68413626
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46468 * 0.23388788
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4523 * 0.61575649
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42640 * 0.12468944
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79616 * 0.19907783
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35779 * 0.40782274
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88594 * 0.58839955
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68149 * 0.58869684
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87930 * 0.69787908
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56459 * 0.87616890
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14460 * 0.10047138
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11663 * 0.77468532
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10463 * 0.58185037
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82420 * 0.60678877
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61863 * 0.54589464
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26054 * 0.25446700
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42821 * 0.51504463
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54759 * 0.38977415
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86308 * 0.85806969
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94470 * 0.44802882
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58518 * 0.65424130
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43619 * 0.85261931
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78704 * 0.78719317
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92268 * 0.84220142
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12316 * 0.30557273
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21695 * 0.93498051
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20247 * 0.85062797
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ztvhdfwl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0011():
    """Extended test 11 for aggregation."""
    x_0 = 88631 * 0.05223963
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28888 * 0.01582422
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17049 * 0.62717486
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52938 * 0.89896468
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40691 * 0.53964135
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14372 * 0.91565114
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97478 * 0.73678634
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33263 * 0.47406767
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37090 * 0.20709240
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38011 * 0.65630063
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13091 * 0.87279387
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32884 * 0.61127722
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27170 * 0.62852572
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76959 * 0.82523339
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38782 * 0.09435168
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97283 * 0.28376326
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98133 * 0.08564957
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97471 * 0.52042290
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7745 * 0.61300941
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92017 * 0.55037558
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6234 * 0.35500803
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16867 * 0.46771677
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6082 * 0.20359880
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86857 * 0.54238552
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19518 * 0.62090918
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40454 * 0.55703088
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75880 * 0.76793165
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57071 * 0.12718710
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49130 * 0.68553594
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22930 * 0.00932134
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39156 * 0.64213212
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94201 * 0.93463980
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11336 * 0.59086958
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94857 * 0.34547249
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81503 * 0.69675174
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81068 * 0.15757626
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9949 * 0.24186616
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41889 * 0.85283866
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87375 * 0.69298710
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20712 * 0.21635468
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77513 * 0.17111457
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4874 * 0.27575665
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65167 * 0.57981152
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 96499 * 0.83985635
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71441 * 0.25950299
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 85710 * 0.48040982
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 73680 * 0.04919297
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 25638 * 0.03626078
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'vwifvevq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0012():
    """Extended test 12 for aggregation."""
    x_0 = 6235 * 0.49652360
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6615 * 0.59328703
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40211 * 0.23571921
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1588 * 0.88870328
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90167 * 0.02620621
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11543 * 0.68934976
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99541 * 0.00053401
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79903 * 0.31683793
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42622 * 0.05103287
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81194 * 0.44630429
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60062 * 0.55087693
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15582 * 0.40355023
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73057 * 0.14192865
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20707 * 0.02170360
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92502 * 0.05549624
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 774 * 0.50354427
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11821 * 0.85516707
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88450 * 0.18945391
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88118 * 0.77932213
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28274 * 0.26878263
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8354 * 0.49226995
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7828 * 0.50631828
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'xjhenvsx').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0013():
    """Extended test 13 for aggregation."""
    x_0 = 28714 * 0.52978554
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17149 * 0.25275958
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47128 * 0.28809592
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29050 * 0.10722229
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83514 * 0.04068768
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35536 * 0.06478698
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31943 * 0.50859550
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98959 * 0.73966521
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4167 * 0.79669798
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39333 * 0.57124558
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11553 * 0.15357173
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29705 * 0.16635184
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2678 * 0.34351472
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6033 * 0.31938308
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66297 * 0.51468074
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25562 * 0.27516805
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25069 * 0.16573823
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90548 * 0.65272388
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63699 * 0.10876256
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89127 * 0.71397568
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29915 * 0.00009454
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30751 * 0.25234635
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95135 * 0.98879534
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51033 * 0.19864184
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33932 * 0.15558500
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42632 * 0.90877984
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16708 * 0.77967628
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59151 * 0.41494691
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86255 * 0.27817296
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ycvhinuq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0014():
    """Extended test 14 for aggregation."""
    x_0 = 81875 * 0.37398836
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89226 * 0.88922991
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84525 * 0.83802893
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50609 * 0.54350099
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28736 * 0.25211060
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2223 * 0.85755638
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21314 * 0.95413954
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89383 * 0.66081982
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21552 * 0.87513192
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25635 * 0.29594894
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49205 * 0.77389807
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3989 * 0.05456449
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74478 * 0.99060325
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98865 * 0.02398299
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96630 * 0.50483101
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45731 * 0.04731014
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97913 * 0.26801348
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20103 * 0.51683088
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 154 * 0.37360735
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52759 * 0.54408101
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84120 * 0.05317886
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85976 * 0.52976132
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78125 * 0.17389563
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81646 * 0.96704100
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13544 * 0.31602648
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5039 * 0.34676472
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72173 * 0.93525219
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18630 * 0.61394949
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32893 * 0.75074812
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28693 * 0.20537645
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1844 * 0.39541393
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53830 * 0.11089389
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8776 * 0.65122332
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97727 * 0.07533022
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22716 * 0.44665590
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48629 * 0.25649640
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 37315 * 0.10318329
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71823 * 0.07575298
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6286 * 0.93210795
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62471 * 0.80316631
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34390 * 0.11508640
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58414 * 0.94037847
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28115 * 0.88350474
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58610 * 0.70451029
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'qribaswo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0015():
    """Extended test 15 for aggregation."""
    x_0 = 18722 * 0.72022650
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31007 * 0.86556421
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14178 * 0.76260298
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69036 * 0.19942189
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4704 * 0.03066594
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92347 * 0.64074291
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78940 * 0.26473990
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91114 * 0.83689480
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39197 * 0.09198718
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13251 * 0.36661083
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5064 * 0.37681583
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46883 * 0.63913021
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87053 * 0.11105694
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99094 * 0.56736879
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65527 * 0.02397354
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52238 * 0.22028534
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20829 * 0.68824994
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44170 * 0.29087103
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26578 * 0.55541204
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77225 * 0.32117226
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11397 * 0.33392014
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27085 * 0.74099231
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16213 * 0.33589717
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28680 * 0.45650557
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77564 * 0.86932570
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94986 * 0.81234625
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72572 * 0.19828189
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69751 * 0.16027136
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19269 * 0.76034694
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35392 * 0.83034294
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96442 * 0.93815619
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96949 * 0.62288683
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9648 * 0.25725893
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62554 * 0.54876296
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77974 * 0.88153724
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85099 * 0.32806222
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42005 * 0.75178624
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84690 * 0.68684409
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70733 * 0.79598969
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19457 * 0.06935467
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 10966 * 0.57407953
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67784 * 0.38754994
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'kysoortr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0016():
    """Extended test 16 for aggregation."""
    x_0 = 20446 * 0.48103909
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41722 * 0.42371607
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72293 * 0.93244491
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45321 * 0.66258002
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23285 * 0.65716841
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59030 * 0.85691591
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97185 * 0.82464274
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33055 * 0.00522301
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92028 * 0.56159425
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50792 * 0.87624738
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79992 * 0.18829339
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63649 * 0.00000416
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7785 * 0.68099092
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1631 * 0.15423165
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29713 * 0.75571579
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91827 * 0.81680338
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53033 * 0.61064922
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69298 * 0.15641895
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97468 * 0.42039029
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98999 * 0.63357806
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32629 * 0.71338229
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35481 * 0.88976312
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66598 * 0.85249256
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56321 * 0.93730998
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52379 * 0.98270884
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83770 * 0.28529905
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20089 * 0.35237213
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3090 * 0.89098801
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 366 * 0.68448578
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47663 * 0.42563809
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78892 * 0.77342890
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42821 * 0.67472617
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69784 * 0.86226856
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49286 * 0.85614352
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89692 * 0.38454725
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38588 * 0.01201283
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83229 * 0.09657223
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 398 * 0.34814244
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14753 * 0.43307051
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81373 * 0.64638803
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71117 * 0.90050812
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'bpjruhfj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0017():
    """Extended test 17 for aggregation."""
    x_0 = 59100 * 0.09352678
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6923 * 0.26004501
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96250 * 0.46306637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50675 * 0.16802453
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35805 * 0.94481554
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61269 * 0.62365218
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71986 * 0.69802313
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66737 * 0.95225986
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66673 * 0.84297399
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43529 * 0.69708941
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10623 * 0.19201592
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20761 * 0.52695760
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32029 * 0.29742603
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86860 * 0.59061115
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8836 * 0.55149544
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35201 * 0.89818964
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39707 * 0.33708439
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20987 * 0.16379512
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23786 * 0.10663348
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92467 * 0.58437704
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13955 * 0.90385488
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1305 * 0.74140928
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46057 * 0.71021734
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84022 * 0.21027936
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44664 * 0.93258772
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25359 * 0.62119048
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'hjnowndk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0018():
    """Extended test 18 for aggregation."""
    x_0 = 67290 * 0.81827384
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38120 * 0.38488897
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13920 * 0.73737516
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35378 * 0.16814812
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73375 * 0.36599852
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23637 * 0.49193684
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81258 * 0.42171486
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88666 * 0.89001485
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28276 * 0.99201591
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7876 * 0.29672420
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86659 * 0.19342141
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23252 * 0.31183384
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10743 * 0.10062839
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81495 * 0.88237666
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14345 * 0.68606703
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83735 * 0.07151582
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43640 * 0.50723452
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94154 * 0.88989483
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31543 * 0.40659470
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6133 * 0.02034798
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92231 * 0.51965725
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98528 * 0.92008136
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46709 * 0.79741734
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69890 * 0.35083126
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90884 * 0.36642713
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63894 * 0.88026321
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19822 * 0.83235808
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50491 * 0.08017558
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88522 * 0.98679016
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89753 * 0.84023138
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84680 * 0.48379225
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36038 * 0.90241059
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86488 * 0.50949703
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65465 * 0.99704609
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35721 * 0.08889945
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77957 * 0.38389468
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9687 * 0.43604202
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13027 * 0.76376313
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82961 * 0.73668173
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43230 * 0.18130230
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12760 * 0.29252700
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81663 * 0.14814147
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 32836 * 0.25454506
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 51909 * 0.40144523
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 83007 * 0.38602324
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 43755 * 0.64884407
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 46791 * 0.51693443
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 14893 * 0.04956991
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'qgyuoqpv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0019():
    """Extended test 19 for aggregation."""
    x_0 = 7420 * 0.71762929
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94714 * 0.75745473
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31360 * 0.65268791
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54874 * 0.38425681
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54145 * 0.49002649
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87037 * 0.50446219
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54319 * 0.01972017
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24606 * 0.65556749
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70570 * 0.89498565
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39541 * 0.65886463
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49118 * 0.40854907
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21104 * 0.75643966
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83941 * 0.82860517
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42750 * 0.36886217
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68188 * 0.90727720
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84812 * 0.91007494
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10589 * 0.40666126
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29828 * 0.38629615
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90457 * 0.57315268
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21518 * 0.56378291
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61943 * 0.58014690
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80638 * 0.67517465
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25382 * 0.53190480
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1070 * 0.94211186
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16944 * 0.08913038
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48306 * 0.72579255
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59761 * 0.87786092
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60573 * 0.53424362
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25684 * 0.55606726
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35744 * 0.56447746
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49836 * 0.69200520
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2941 * 0.73579073
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83213 * 0.55628362
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18198 * 0.29371696
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17226 * 0.80166661
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25913 * 0.28221147
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80414 * 0.06553934
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22085 * 0.81288511
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14147 * 0.15730948
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'hsbbwcxp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0020():
    """Extended test 20 for aggregation."""
    x_0 = 21994 * 0.10653038
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81886 * 0.20873272
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42369 * 0.56973952
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52604 * 0.51442373
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17212 * 0.56020154
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24493 * 0.22368853
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24315 * 0.64483646
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47297 * 0.11775000
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78857 * 0.72758637
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60820 * 0.10534920
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25204 * 0.24471362
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71953 * 0.82325964
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6920 * 0.34456074
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26004 * 0.31224186
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77491 * 0.58703671
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8928 * 0.32827547
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49034 * 0.35927830
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53873 * 0.17710340
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84545 * 0.01217302
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17105 * 0.72135195
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74598 * 0.44754349
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23048 * 0.94621025
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'xiwlfhit').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0021():
    """Extended test 21 for aggregation."""
    x_0 = 58279 * 0.96254313
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14058 * 0.04585504
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48360 * 0.37711443
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61285 * 0.06268224
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79528 * 0.97933323
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37980 * 0.13782522
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91451 * 0.94979263
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69668 * 0.89486429
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31196 * 0.15135638
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90062 * 0.59902562
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32251 * 0.94373778
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27308 * 0.61102188
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24778 * 0.66928652
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5374 * 0.30438469
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69211 * 0.69353612
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5571 * 0.69817383
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81515 * 0.59352457
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22487 * 0.44959970
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38945 * 0.86637848
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22238 * 0.62326563
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26772 * 0.60369714
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8755 * 0.14117771
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38546 * 0.01307777
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76675 * 0.61685086
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45425 * 0.89507923
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72703 * 0.09011000
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88986 * 0.53050759
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68019 * 0.17764232
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6346 * 0.54938146
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98314 * 0.60720905
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69969 * 0.91445314
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18828 * 0.61626333
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70862 * 0.57410911
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54042 * 0.72397207
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78577 * 0.38834587
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34231 * 0.46696031
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29231 * 0.46242086
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73714 * 0.52180504
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14836 * 0.32365304
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93662 * 0.07713210
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94702 * 0.14249376
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74939 * 0.13255297
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 99142 * 0.00207892
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 6513 * 0.92608995
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 40296 * 0.73429096
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 28800 * 0.41164979
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 88680 * 0.60372985
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 7402 * 0.03150799
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'xriszzgw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0022():
    """Extended test 22 for aggregation."""
    x_0 = 36361 * 0.52786632
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70355 * 0.08818527
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98898 * 0.16295652
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53305 * 0.78525412
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46587 * 0.50292065
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51933 * 0.41498405
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94580 * 0.27809218
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14350 * 0.75330734
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8086 * 0.72471428
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85996 * 0.93834049
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9065 * 0.81372343
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85867 * 0.11117896
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28024 * 0.67884139
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55888 * 0.44948465
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3672 * 0.54037338
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49576 * 0.04611087
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12232 * 0.72138706
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55741 * 0.53662943
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41150 * 0.32823165
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55291 * 0.99264319
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26062 * 0.65971134
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12681 * 0.34734857
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42070 * 0.61981227
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89999 * 0.16730753
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55666 * 0.86574255
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99379 * 0.06463211
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50798 * 0.22697153
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45542 * 0.40627036
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39107 * 0.15656536
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37874 * 0.48205455
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52394 * 0.27849319
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'rjrzscun').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0023():
    """Extended test 23 for aggregation."""
    x_0 = 22916 * 0.96797370
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56580 * 0.30467901
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40527 * 0.95208398
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28861 * 0.67291727
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99065 * 0.32979440
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95205 * 0.50145731
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88792 * 0.92471597
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90835 * 0.57888994
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53317 * 0.16241054
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60831 * 0.36660942
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53737 * 0.05864283
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20345 * 0.83992753
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22816 * 0.81005219
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54370 * 0.49188436
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14781 * 0.21379727
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62825 * 0.61199682
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15688 * 0.28203582
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27622 * 0.30913457
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 867 * 0.47604190
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8286 * 0.54546855
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17199 * 0.41305970
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98412 * 0.27170692
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25314 * 0.33989319
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62907 * 0.99102554
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36427 * 0.12964081
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98388 * 0.94643015
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20717 * 0.20586733
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40399 * 0.11224118
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'zmzbdfvb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0024():
    """Extended test 24 for aggregation."""
    x_0 = 79373 * 0.75667185
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68333 * 0.35469992
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73919 * 0.39501177
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24689 * 0.50137605
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94673 * 0.42802321
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78396 * 0.70658886
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38183 * 0.44440441
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74768 * 0.53671777
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78152 * 0.63537341
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61722 * 0.70602264
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95945 * 0.22711876
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36660 * 0.47838465
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90224 * 0.16365538
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17858 * 0.86082571
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58851 * 0.18799096
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31463 * 0.95824075
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51162 * 0.69260321
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57132 * 0.47785047
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33963 * 0.06902827
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60095 * 0.59506310
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1145 * 0.70716787
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 981 * 0.69896886
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50154 * 0.62476153
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 704 * 0.60627394
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42668 * 0.88061662
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6814 * 0.38703137
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98888 * 0.47921071
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44246 * 0.79077102
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61746 * 0.20064021
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60776 * 0.02003532
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19510 * 0.21517857
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2412 * 0.00041056
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20004 * 0.05656738
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'catlxxbr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0025():
    """Extended test 25 for aggregation."""
    x_0 = 99790 * 0.59945397
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27067 * 0.86514561
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33504 * 0.44011900
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76733 * 0.33851129
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21249 * 0.62163872
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54252 * 0.95205485
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11903 * 0.41710488
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58953 * 0.96684431
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37261 * 0.98795684
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11616 * 0.66232987
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34591 * 0.44149023
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96512 * 0.52623104
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18902 * 0.30763634
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58344 * 0.76917245
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5868 * 0.58576663
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50796 * 0.88873201
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95909 * 0.67434982
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39897 * 0.21916047
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34520 * 0.16920310
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70430 * 0.03387088
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1305 * 0.45827846
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97841 * 0.43369721
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95521 * 0.30301972
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95920 * 0.94169860
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41056 * 0.92781303
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20073 * 0.67248730
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21773 * 0.67802710
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22844 * 0.16756740
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55033 * 0.55322495
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'burkfsxw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0026():
    """Extended test 26 for aggregation."""
    x_0 = 32360 * 0.60363755
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41271 * 0.51404138
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46507 * 0.14778459
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89742 * 0.56063040
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93661 * 0.38258710
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18055 * 0.06788802
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86871 * 0.23383776
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10661 * 0.99960281
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8241 * 0.57147527
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92218 * 0.02219883
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50804 * 0.19165297
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6863 * 0.67121359
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32573 * 0.06757678
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30672 * 0.84305636
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75570 * 0.91819134
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95047 * 0.43871375
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98198 * 0.21581912
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30269 * 0.14410950
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23915 * 0.91007760
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15606 * 0.37886606
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42183 * 0.68244696
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16073 * 0.23435696
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16759 * 0.35955856
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68330 * 0.25946529
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26189 * 0.73769409
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50107 * 0.85812166
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13782 * 0.79001613
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3540 * 0.23662143
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90690 * 0.80851417
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95614 * 0.83000405
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57677 * 0.21152245
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36477 * 0.31995435
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9964 * 0.17352299
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35187 * 0.37444327
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58504 * 0.15246382
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33708 * 0.61036159
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94634 * 0.42595208
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66266 * 0.16769768
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10929 * 0.12046983
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25669 * 0.41607678
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4516 * 0.07726137
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'lzkydcgp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0027():
    """Extended test 27 for aggregation."""
    x_0 = 70427 * 0.33811817
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79592 * 0.30404976
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92999 * 0.45190014
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12504 * 0.68617397
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88087 * 0.40136832
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20878 * 0.25054672
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49602 * 0.03569988
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44256 * 0.28311451
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63526 * 0.68164703
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98997 * 0.99901328
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6603 * 0.23809370
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98231 * 0.39181517
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40047 * 0.72074865
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52375 * 0.02096137
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4907 * 0.32343493
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38274 * 0.04758932
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24214 * 0.67168697
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61046 * 0.98974877
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85773 * 0.53545166
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99479 * 0.05254907
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30115 * 0.99688381
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 671 * 0.29405105
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25585 * 0.55444825
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16359 * 0.67747273
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19154 * 0.52674140
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56966 * 0.30452042
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9344 * 0.82490802
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48645 * 0.05511566
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73269 * 0.87297131
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44404 * 0.32990276
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30520 * 0.57039805
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72377 * 0.17696685
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50677 * 0.91611070
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91717 * 0.35590755
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74457 * 0.21200263
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49552 * 0.91332780
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54309 * 0.72496964
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21477 * 0.40386208
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55223 * 0.42709585
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24120 * 0.47600855
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62152 * 0.69386628
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'vrgxclpj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0028():
    """Extended test 28 for aggregation."""
    x_0 = 47275 * 0.14170095
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35963 * 0.40157101
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77074 * 0.11980237
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98052 * 0.38898288
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88232 * 0.84179957
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23544 * 0.47455913
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60714 * 0.61958744
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86559 * 0.11484627
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58705 * 0.60660429
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29700 * 0.07761361
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45802 * 0.54872924
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55073 * 0.64621739
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70460 * 0.23377454
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9657 * 0.20276092
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99766 * 0.59953420
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19687 * 0.00771776
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27238 * 0.06346111
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55813 * 0.88032421
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62566 * 0.75778066
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82823 * 0.83310779
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11741 * 0.49298421
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29434 * 0.08363285
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61108 * 0.61585371
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89088 * 0.60485091
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83833 * 0.64203874
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82015 * 0.07164533
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96215 * 0.42805685
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 462 * 0.80430425
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83332 * 0.46405835
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20421 * 0.79465130
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93362 * 0.38971303
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73721 * 0.62989115
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6922 * 0.85620476
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59477 * 0.38015233
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82104 * 0.93128403
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95492 * 0.44275924
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43222 * 0.74161210
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82489 * 0.88879929
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'kcgthtyz').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0029():
    """Extended test 29 for aggregation."""
    x_0 = 57075 * 0.15983483
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70538 * 0.66488865
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64381 * 0.08960610
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98693 * 0.06306596
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60672 * 0.59509032
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14646 * 0.95553169
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66714 * 0.42457636
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61921 * 0.02489818
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71069 * 0.42601299
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28014 * 0.83077788
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59190 * 0.32701908
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1903 * 0.42399068
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7245 * 0.57137283
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90436 * 0.09078117
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98598 * 0.72030005
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88849 * 0.56823714
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2147 * 0.61744400
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50836 * 0.40103126
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94627 * 0.26640598
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82729 * 0.03733846
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89792 * 0.58217524
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31312 * 0.04429003
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93235 * 0.40202600
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1683 * 0.72614338
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25929 * 0.14408275
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25483 * 0.26741722
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10557 * 0.94658860
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71081 * 0.10742564
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26910 * 0.46972786
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96912 * 0.39077798
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85569 * 0.69370897
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9139 * 0.04009501
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7947 * 0.41472829
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'utwmvbqq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0030():
    """Extended test 30 for aggregation."""
    x_0 = 66690 * 0.70010648
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30136 * 0.52722042
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6328 * 0.48996936
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75997 * 0.86625298
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20688 * 0.98532883
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73494 * 0.18435721
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71289 * 0.49388111
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43708 * 0.25019531
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81783 * 0.33140379
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71172 * 0.81380336
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87901 * 0.83907319
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31517 * 0.63057714
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98816 * 0.79009610
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87559 * 0.02688525
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11841 * 0.74348472
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92734 * 0.66413954
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5984 * 0.99836846
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92522 * 0.52226361
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50232 * 0.50550376
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83228 * 0.04757791
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83203 * 0.53839122
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57827 * 0.68723078
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78445 * 0.90120869
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80715 * 0.65869367
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91068 * 0.59918584
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4712 * 0.65550982
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11952 * 0.02565493
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11439 * 0.46124264
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7021 * 0.58609419
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76669 * 0.12051960
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99343 * 0.31832743
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40857 * 0.23372202
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30047 * 0.43352320
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41748 * 0.92086613
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87754 * 0.37379034
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95039 * 0.92239043
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3123 * 0.82794407
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 99186 * 0.61739001
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58318 * 0.82130570
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'sjklklwb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0031():
    """Extended test 31 for aggregation."""
    x_0 = 36415 * 0.60541434
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65015 * 0.52687124
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60736 * 0.05396945
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50736 * 0.24054859
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19727 * 0.23026995
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79256 * 0.03813497
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40870 * 0.16989045
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46322 * 0.99647452
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14735 * 0.62273107
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26801 * 0.29218244
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41814 * 0.27325274
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94057 * 0.82154348
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24858 * 0.76891483
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81672 * 0.40197552
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49423 * 0.55992949
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63320 * 0.35736977
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59335 * 0.91750395
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29154 * 0.88567511
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48815 * 0.82004618
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23430 * 0.39333345
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28452 * 0.67121355
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'nxntsjgo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0032():
    """Extended test 32 for aggregation."""
    x_0 = 62363 * 0.63805441
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17837 * 0.36925802
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68351 * 0.55117297
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34588 * 0.55631484
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33659 * 0.45927670
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34481 * 0.21272551
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16917 * 0.06455103
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1801 * 0.74169115
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87924 * 0.93432308
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72506 * 0.88405614
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20253 * 0.42786956
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85405 * 0.43685151
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71528 * 0.35740937
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25540 * 0.93143204
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98994 * 0.19034230
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60978 * 0.32977310
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27577 * 0.26582305
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 209 * 0.39514357
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53801 * 0.11420866
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90949 * 0.32142923
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24721 * 0.77619427
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81015 * 0.07301744
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65917 * 0.61898078
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5136 * 0.36438655
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97493 * 0.12601573
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99558 * 0.23912583
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76892 * 0.29631988
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12519 * 0.44805339
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34593 * 0.83531493
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35374 * 0.06095651
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54440 * 0.44335326
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 34868 * 0.83800705
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62870 * 0.97502432
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21497 * 0.59175838
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59239 * 0.54950396
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20288 * 0.63459440
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41536 * 0.64997956
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70562 * 0.54626660
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92587 * 0.40902898
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'veuidkfg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0033():
    """Extended test 33 for aggregation."""
    x_0 = 12491 * 0.45591355
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40721 * 0.39447285
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45948 * 0.10448728
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71800 * 0.95854579
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66878 * 0.95133766
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54289 * 0.32297458
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38542 * 0.38209882
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13126 * 0.13740481
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4545 * 0.82024292
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37177 * 0.31338513
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 971 * 0.76020027
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27355 * 0.05174127
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87627 * 0.79630612
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36474 * 0.03238053
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30918 * 0.11330411
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92359 * 0.33761021
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93028 * 0.90433564
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17733 * 0.71277537
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10366 * 0.03884871
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75285 * 0.67007609
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5533 * 0.09181222
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43939 * 0.09529259
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58187 * 0.83569437
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20552 * 0.23437949
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19322 * 0.96951826
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60161 * 0.87566700
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94861 * 0.97350449
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33227 * 0.61785159
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90717 * 0.85065513
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39576 * 0.47446552
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45990 * 0.71538715
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2766 * 0.36539570
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94429 * 0.68154053
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39821 * 0.45510058
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53171 * 0.91608274
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95360 * 0.36358789
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90759 * 0.05244771
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39603 * 0.22804022
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2779 * 0.29523304
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34934 * 0.44233395
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 90367 * 0.87430376
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14068 * 0.93644484
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79254 * 0.72434632
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47388 * 0.55511099
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 45302 * 0.33536876
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 92100 * 0.81017296
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'eqbqpkph').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0034():
    """Extended test 34 for aggregation."""
    x_0 = 56101 * 0.82485942
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94425 * 0.87892940
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43911 * 0.94743016
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72862 * 0.07592215
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49748 * 0.81871539
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16256 * 0.71464360
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59013 * 0.72814456
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2299 * 0.70486612
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52272 * 0.64628110
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1220 * 0.04236720
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11730 * 0.54824257
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58241 * 0.50220788
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5171 * 0.05344863
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68526 * 0.85612428
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13005 * 0.96780072
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38547 * 0.44159719
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19688 * 0.92410475
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7680 * 0.49532085
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7831 * 0.29405616
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8176 * 0.39049990
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72834 * 0.92202553
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93965 * 0.45504748
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'wevgkhid').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0035():
    """Extended test 35 for aggregation."""
    x_0 = 30235 * 0.26919502
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12336 * 0.72784059
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68696 * 0.78788001
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49199 * 0.11804626
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66596 * 0.27402973
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9450 * 0.21351615
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92298 * 0.62291272
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63682 * 0.61806264
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93450 * 0.74886589
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26897 * 0.68153104
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58986 * 0.94623615
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8839 * 0.72303279
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87919 * 0.69542590
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9212 * 0.90192444
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46324 * 0.51566407
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56381 * 0.49366870
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92883 * 0.78394916
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58474 * 0.89068187
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66480 * 0.76749451
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47956 * 0.95936629
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30611 * 0.81208353
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61018 * 0.09137539
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52023 * 0.76129775
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92187 * 0.91063659
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63273 * 0.56761796
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69244 * 0.76882081
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56427 * 0.87739321
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98084 * 0.13214232
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35575 * 0.98937830
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83211 * 0.74413030
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90685 * 0.95138697
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41197 * 0.63994744
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1278 * 0.79459823
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12245 * 0.63123910
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61471 * 0.68967180
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93130 * 0.92255505
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80510 * 0.07782187
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48802 * 0.70803575
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63398 * 0.50495697
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15268 * 0.41770432
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40432 * 0.48854109
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30112 * 0.40727453
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1220 * 0.64260889
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 15010 * 0.06815788
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'dbpejavb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0036():
    """Extended test 36 for aggregation."""
    x_0 = 20356 * 0.00507020
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64691 * 0.70624760
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 796 * 0.25767998
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79878 * 0.48210082
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23392 * 0.44007673
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54187 * 0.82138563
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21028 * 0.32450855
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3409 * 0.41926994
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93045 * 0.76150711
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71021 * 0.42058482
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73002 * 0.43807599
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92158 * 0.01545767
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26127 * 0.93620800
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7052 * 0.37772103
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17797 * 0.83414276
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46083 * 0.66783128
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75179 * 0.27256541
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19091 * 0.84514653
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33952 * 0.70208388
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3361 * 0.73278073
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62437 * 0.40430322
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53116 * 0.85082647
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58114 * 0.22101437
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94480 * 0.68288075
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69768 * 0.40063816
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51979 * 0.09681108
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79085 * 0.77295307
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77344 * 0.81436386
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'ioraivok').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0037():
    """Extended test 37 for aggregation."""
    x_0 = 72111 * 0.42100946
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98513 * 0.10943467
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25900 * 0.70656768
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89867 * 0.38079005
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55086 * 0.43693751
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20856 * 0.36255455
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81136 * 0.35016342
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77467 * 0.18560835
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95568 * 0.31927878
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98149 * 0.53047732
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69721 * 0.65276212
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18494 * 0.91045620
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74510 * 0.43978458
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87090 * 0.41044524
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68535 * 0.31773163
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71528 * 0.96868712
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68486 * 0.67961214
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29646 * 0.43060065
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53142 * 0.60133201
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46919 * 0.01738906
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9374 * 0.87421539
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99883 * 0.50580205
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80601 * 0.28030712
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31577 * 0.97091817
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28089 * 0.57679880
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8916 * 0.42391594
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53764 * 0.86630113
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'yikzqjdn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0038():
    """Extended test 38 for aggregation."""
    x_0 = 26013 * 0.72425371
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42617 * 0.57049434
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28289 * 0.97967139
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16628 * 0.40294707
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4808 * 0.08341696
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40429 * 0.58661545
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87417 * 0.56514880
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63768 * 0.61389041
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27171 * 0.63259094
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40627 * 0.26440334
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52607 * 0.74707722
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65878 * 0.45306250
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22269 * 0.17148169
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41079 * 0.47240004
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85972 * 0.66617908
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61636 * 0.91084560
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72938 * 0.09162565
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59569 * 0.18509044
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87068 * 0.51498686
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18406 * 0.20165888
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60438 * 0.96369973
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3094 * 0.27932197
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32874 * 0.60157536
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80781 * 0.76339745
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62180 * 0.48267919
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46727 * 0.05735110
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59329 * 0.63368017
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57106 * 0.54879847
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12161 * 0.51733156
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4651 * 0.61823537
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89758 * 0.32306237
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43661 * 0.88952210
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2431 * 0.58532013
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23028 * 0.08021065
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9512 * 0.15607744
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68934 * 0.52708623
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95327 * 0.34791560
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38568 * 0.45271743
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86407 * 0.70040452
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95189 * 0.00814995
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'fbcnypbr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0039():
    """Extended test 39 for aggregation."""
    x_0 = 39947 * 0.25361465
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5796 * 0.87267913
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10498 * 0.72708069
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73944 * 0.79571043
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24605 * 0.07722056
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52761 * 0.60038416
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60531 * 0.03053722
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67656 * 0.91464060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7696 * 0.29205833
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36605 * 0.93798662
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13410 * 0.40749208
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99389 * 0.88826072
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94228 * 0.80869727
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81707 * 0.67173520
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4133 * 0.49677339
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63158 * 0.62252396
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55996 * 0.65720400
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84907 * 0.33011739
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44689 * 0.00108859
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18469 * 0.25981390
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6794 * 0.12789679
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44336 * 0.31826616
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 174 * 0.83765558
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'nidbqgpb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0040():
    """Extended test 40 for aggregation."""
    x_0 = 49282 * 0.54841804
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16949 * 0.79057439
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92126 * 0.33839498
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29486 * 0.98114112
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64408 * 0.55427580
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85605 * 0.98359371
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47262 * 0.33670345
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88591 * 0.22588574
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31497 * 0.16901534
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45617 * 0.90444689
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28701 * 0.14109190
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37130 * 0.00910614
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18892 * 0.08387311
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87137 * 0.64167973
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21070 * 0.64959824
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52487 * 0.40578196
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74979 * 0.59622611
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56640 * 0.86643239
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86547 * 0.81627874
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75266 * 0.30103142
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4763 * 0.24031236
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79966 * 0.25179446
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49786 * 0.60325818
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50504 * 0.24871698
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36520 * 0.24965027
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55362 * 0.92734139
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37516 * 0.90774680
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72803 * 0.13236186
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16955 * 0.52236965
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98564 * 0.75866892
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68548 * 0.99388858
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42624 * 0.65173794
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35044 * 0.69061649
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97295 * 0.42921314
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57532 * 0.26648267
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61264 * 0.14428202
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13584 * 0.77100825
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78761 * 0.47199482
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96583 * 0.09017249
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95756 * 0.09217988
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1076 * 0.30176572
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15739 * 0.16679247
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 60502 * 0.76859921
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 9170 * 0.27466520
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4783 * 0.29476412
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 88192 * 0.52553054
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17712 * 0.08597571
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 24475 * 0.66830037
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 90606 * 0.97688791
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 81909 * 0.84945868
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'mizkqxin').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0041():
    """Extended test 41 for aggregation."""
    x_0 = 62671 * 0.10849767
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32581 * 0.49191948
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74923 * 0.76111288
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16997 * 0.52629061
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91223 * 0.55175536
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57198 * 0.80480230
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50522 * 0.58658758
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54025 * 0.76171657
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34558 * 0.64085651
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72358 * 0.76658417
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71797 * 0.32333869
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14170 * 0.23614221
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30721 * 0.41201188
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20295 * 0.63479948
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14040 * 0.74441284
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 618 * 0.19391790
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72420 * 0.90969609
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32398 * 0.90923912
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23072 * 0.85686800
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34439 * 0.89445124
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3514 * 0.52183126
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10552 * 0.81132857
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18136 * 0.70253670
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67267 * 0.56046446
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84339 * 0.29184891
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43027 * 0.49784981
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80803 * 0.11368886
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40195 * 0.71063007
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1863 * 0.96993130
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17075 * 0.28164210
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58766 * 0.77561981
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11554 * 0.26277865
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5925 * 0.94905861
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24028 * 0.91167995
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9489 * 0.57799637
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56436 * 0.48216718
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34147 * 0.03068699
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15634 * 0.91014414
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92211 * 0.35475125
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86936 * 0.71399154
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79367 * 0.98951013
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82330 * 0.96041829
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36763 * 0.40735515
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 25081 * 0.22173277
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 15193 * 0.47584941
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'inmbyewt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0042():
    """Extended test 42 for aggregation."""
    x_0 = 93344 * 0.76909104
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50161 * 0.22796041
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57942 * 0.39638402
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52355 * 0.44070129
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43685 * 0.10970419
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13310 * 0.02150503
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60753 * 0.41607879
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37499 * 0.88754831
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70999 * 0.70959234
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42942 * 0.19661404
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55490 * 0.23457009
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58228 * 0.13984702
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62430 * 0.92408001
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44101 * 0.93837526
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21840 * 0.12801872
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78400 * 0.22098908
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37270 * 0.24898002
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95587 * 0.68028992
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66695 * 0.11838501
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32421 * 0.48130958
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96206 * 0.06366163
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89854 * 0.99915431
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29234 * 0.37424680
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54323 * 0.42385345
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56901 * 0.93706185
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69199 * 0.05909557
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56972 * 0.06414650
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72852 * 0.65587323
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76389 * 0.70671483
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26036 * 0.55211613
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2358 * 0.68605831
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63861 * 0.16018061
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23767 * 0.17016589
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89393 * 0.21889028
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77200 * 0.73439198
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38095 * 0.72313056
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68785 * 0.36738345
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40116 * 0.85908682
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84989 * 0.90643155
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52757 * 0.35162454
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11557 * 0.31478736
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 31885 * 0.02258173
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11451 * 0.15860381
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 95021 * 0.17332158
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 78881 * 0.55039605
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 24542 * 0.33689875
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 14362 * 0.34208732
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 65914 * 0.84274056
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 59152 * 0.70969121
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'xcwjddcn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0043():
    """Extended test 43 for aggregation."""
    x_0 = 8487 * 0.47797688
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81829 * 0.94612181
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38038 * 0.50933463
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99529 * 0.25642686
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58839 * 0.22897202
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5923 * 0.70623347
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52989 * 0.79260742
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77917 * 0.20508696
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53866 * 0.47845297
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48501 * 0.39032402
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67176 * 0.28313717
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60919 * 0.15467593
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7314 * 0.90900550
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20430 * 0.00809180
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18988 * 0.10567693
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78991 * 0.82922421
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28555 * 0.17183814
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94666 * 0.87730290
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76732 * 0.34437955
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63540 * 0.69294284
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89311 * 0.43729142
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44970 * 0.93929370
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14142 * 0.84073514
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31223 * 0.88949573
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72598 * 0.75311591
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22745 * 0.18715399
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97791 * 0.54353151
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56972 * 0.06934297
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66454 * 0.31936337
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'qokmvlrm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0044():
    """Extended test 44 for aggregation."""
    x_0 = 7402 * 0.29014992
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7819 * 0.42273219
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54657 * 0.72015905
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34687 * 0.58547840
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10780 * 0.44645185
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18040 * 0.18994172
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16657 * 0.91803679
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76795 * 0.97339008
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66368 * 0.37214398
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17872 * 0.69779267
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78966 * 0.65456704
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88267 * 0.02039889
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73600 * 0.28996696
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11187 * 0.32124258
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86304 * 0.53277549
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99302 * 0.71568069
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62981 * 0.86096762
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77309 * 0.59166308
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69107 * 0.65482920
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66722 * 0.46108837
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86784 * 0.02367338
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16858 * 0.93470390
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91974 * 0.81104392
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53849 * 0.85712053
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3632 * 0.90704995
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65391 * 0.29437427
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37711 * 0.36200415
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46592 * 0.84327668
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61166 * 0.70522166
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30273 * 0.18069336
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68253 * 0.16618250
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92551 * 0.09435520
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60778 * 0.51550600
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19255 * 0.35330326
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53969 * 0.96991289
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5455 * 0.92577860
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66213 * 0.25181032
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85409 * 0.91896003
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17537 * 0.21911121
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94574 * 0.53083549
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68648 * 0.39495162
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38080 * 0.60760872
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29084 * 0.17993598
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 50144 * 0.62629307
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 13735 * 0.91198270
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 27250 * 0.07944096
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 69450 * 0.79052187
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 9072 * 0.62902370
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 19913 * 0.56046135
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 33580 * 0.81514824
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'swcbomzk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0045():
    """Extended test 45 for aggregation."""
    x_0 = 55646 * 0.18515086
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18007 * 0.33563003
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74415 * 0.02801788
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3117 * 0.56065537
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33067 * 0.22917374
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43035 * 0.65797853
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69971 * 0.62131074
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73258 * 0.43728950
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20532 * 0.26464204
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86629 * 0.55240369
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32583 * 0.00650590
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35976 * 0.65079372
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19423 * 0.28084830
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68654 * 0.09803246
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2656 * 0.62946917
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36610 * 0.20115121
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85791 * 0.01302554
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77280 * 0.32728768
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65980 * 0.57836234
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52889 * 0.28608343
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71158 * 0.58856984
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96929 * 0.47257857
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95061 * 0.14099968
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10647 * 0.36591309
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48233 * 0.96490712
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89684 * 0.70525621
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'dizvaljl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0046():
    """Extended test 46 for aggregation."""
    x_0 = 21788 * 0.42511646
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96166 * 0.16930921
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54402 * 0.51002107
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61592 * 0.78242172
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67704 * 0.52601638
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97436 * 0.38020416
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52690 * 0.80939461
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2578 * 0.31506631
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36547 * 0.29280133
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52397 * 0.71003956
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14978 * 0.48711866
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24521 * 0.93576206
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38821 * 0.75920946
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55622 * 0.27971734
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71689 * 0.98392018
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58526 * 0.62349704
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83093 * 0.80978849
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27228 * 0.38469959
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36296 * 0.97429655
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61810 * 0.20266894
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94775 * 0.32123472
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39168 * 0.83896775
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87330 * 0.78998811
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85818 * 0.47251928
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56227 * 0.42543787
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'lddqyffm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0047():
    """Extended test 47 for aggregation."""
    x_0 = 68398 * 0.31226907
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75715 * 0.28998828
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75323 * 0.02292725
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37485 * 0.57006976
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52234 * 0.64032570
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34145 * 0.14661884
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29181 * 0.34310566
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60132 * 0.63786184
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83886 * 0.45239767
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6914 * 0.76056974
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65400 * 0.30500292
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63771 * 0.39352195
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26150 * 0.85440051
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23140 * 0.08036016
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72737 * 0.96441424
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25702 * 0.79482423
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61793 * 0.16086294
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21034 * 0.47109453
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16183 * 0.45366118
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85584 * 0.35305416
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21649 * 0.55124261
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54454 * 0.58849181
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24436 * 0.12548788
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2116 * 0.32878694
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65405 * 0.62592468
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97097 * 0.24271272
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11730 * 0.33736514
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68623 * 0.21082732
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81436 * 0.55206774
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52646 * 0.75140816
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48171 * 0.54977396
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83896 * 0.66761474
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65585 * 0.51785884
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91904 * 0.80467061
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63008 * 0.89256617
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60288 * 0.80478933
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94074 * 0.62046878
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24351 * 0.81712907
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10060 * 0.05894153
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43487 * 0.05154699
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45530 * 0.18172099
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'iaxaukvq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0048():
    """Extended test 48 for aggregation."""
    x_0 = 87034 * 0.82824925
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85964 * 0.71915945
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91967 * 0.91651157
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19949 * 0.89207422
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31929 * 0.62543540
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38629 * 0.53780203
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19910 * 0.24907955
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92560 * 0.53153941
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77455 * 0.05189517
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24234 * 0.60416784
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20130 * 0.38752772
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90102 * 0.42711748
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45985 * 0.20199615
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14444 * 0.44033422
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24023 * 0.79102580
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7933 * 0.07518940
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54501 * 0.23662819
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34381 * 0.73625215
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62245 * 0.23954513
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86241 * 0.33201591
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45256 * 0.65546180
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80171 * 0.32795850
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98221 * 0.97400933
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58719 * 0.16773562
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25912 * 0.82593642
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40112 * 0.75208699
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 347 * 0.25036754
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93770 * 0.12616561
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51506 * 0.67060507
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72720 * 0.95823595
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83585 * 0.66915440
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81989 * 0.64396086
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25819 * 0.11370809
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53108 * 0.31649049
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45248 * 0.06793924
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20300 * 0.03064752
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78122 * 0.25176454
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62644 * 0.80213750
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'izwufkpb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0049():
    """Extended test 49 for aggregation."""
    x_0 = 74854 * 0.20305450
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63890 * 0.28061812
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44272 * 0.48120800
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69587 * 0.85532935
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39339 * 0.75463318
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89120 * 0.77305682
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55794 * 0.39942219
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5280 * 0.07529680
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50460 * 0.62849875
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72904 * 0.20782685
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57222 * 0.67111634
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47950 * 0.09064451
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87097 * 0.80001943
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76784 * 0.60822337
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40112 * 0.58064734
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73919 * 0.15957997
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45068 * 0.15954388
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59784 * 0.46289792
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77558 * 0.39539728
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54454 * 0.13709004
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10187 * 0.09186717
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 791 * 0.57721806
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76113 * 0.57371957
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55106 * 0.17231048
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65296 * 0.55962126
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78358 * 0.33889489
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11582 * 0.25569922
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87875 * 0.88650756
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92685 * 0.23787725
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23865 * 0.66171581
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42754 * 0.45973319
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92170 * 0.68213685
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62439 * 0.33633715
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16497 * 0.02541386
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90169 * 0.66737302
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70779 * 0.01167899
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73314 * 0.00854827
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65609 * 0.51957843
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38165 * 0.31225119
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'cdgypbog').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0050():
    """Extended test 50 for aggregation."""
    x_0 = 61161 * 0.32727771
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92358 * 0.28805123
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11012 * 0.60707630
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91316 * 0.22839389
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45376 * 0.00584079
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41569 * 0.47520939
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56836 * 0.84291379
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7932 * 0.34078258
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63560 * 0.30643502
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67222 * 0.14739270
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35326 * 0.91991964
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19100 * 0.56365720
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28341 * 0.14434247
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11370 * 0.60022215
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80911 * 0.64737018
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36590 * 0.76638501
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96175 * 0.22103463
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92845 * 0.75102482
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85134 * 0.87226235
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74442 * 0.61218148
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74597 * 0.86253580
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37972 * 0.46357398
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43762 * 0.01031930
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42885 * 0.17628234
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59227 * 0.58238430
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63484 * 0.12643433
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5314 * 0.63240815
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85518 * 0.76839101
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30151 * 0.40559502
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99145 * 0.96530785
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37447 * 0.17369644
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87705 * 0.89320241
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28540 * 0.34160903
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12429 * 0.53295508
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'ryxncmso').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0051():
    """Extended test 51 for aggregation."""
    x_0 = 62884 * 0.66669399
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18135 * 0.79431043
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32133 * 0.23374651
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8344 * 0.99548113
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76796 * 0.26969278
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81682 * 0.47816016
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60084 * 0.36304790
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94380 * 0.66845040
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5675 * 0.17642945
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27060 * 0.85983046
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69458 * 0.66632960
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39239 * 0.82606790
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58409 * 0.14113771
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27300 * 0.56527224
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1627 * 0.49069541
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88293 * 0.86353591
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54642 * 0.01653011
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31064 * 0.28208248
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29516 * 0.37573993
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2848 * 0.36518253
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59367 * 0.50813927
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49329 * 0.10948806
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10547 * 0.62394705
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11256 * 0.00571537
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39077 * 0.11501987
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25753 * 0.45148270
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34935 * 0.06812653
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2737 * 0.57673105
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65215 * 0.08207822
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87963 * 0.66053608
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26325 * 0.57904066
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65388 * 0.83911310
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38558 * 0.11900210
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1355 * 0.63980617
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1709 * 0.41880356
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25879 * 0.88268901
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25362 * 0.32476693
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8318 * 0.99313288
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1319 * 0.93522273
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ahcajjcy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0052():
    """Extended test 52 for aggregation."""
    x_0 = 90390 * 0.60952578
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7295 * 0.79174790
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35775 * 0.90513376
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61597 * 0.37624002
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56194 * 0.14118464
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97772 * 0.81421484
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67881 * 0.95238334
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15138 * 0.75508398
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26154 * 0.95496066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84925 * 0.61260504
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17116 * 0.59669974
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48165 * 0.68632342
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44006 * 0.37917716
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14750 * 0.28016320
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68 * 0.59059064
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8534 * 0.15936559
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93473 * 0.85708573
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71051 * 0.85271820
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20515 * 0.73393197
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5898 * 0.30064352
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7824 * 0.51264493
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9625 * 0.43229727
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23398 * 0.66121118
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12501 * 0.66326811
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87791 * 0.78665174
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57108 * 0.75329130
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59822 * 0.85294706
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2508 * 0.37545199
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6060 * 0.04228786
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35555 * 0.45560315
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24769 * 0.02538379
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56894 * 0.76641911
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95007 * 0.71169338
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20368 * 0.79452052
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23668 * 0.42426033
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89077 * 0.84218027
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31325 * 0.15325469
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35740 * 0.78141643
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39922 * 0.76988859
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10124 * 0.48534674
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86395 * 0.52093928
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'bbxeftma').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0053():
    """Extended test 53 for aggregation."""
    x_0 = 96871 * 0.37235043
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16001 * 0.24509985
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60226 * 0.15678362
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15386 * 0.69687540
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50393 * 0.68754483
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80223 * 0.16731646
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4708 * 0.27673930
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76244 * 0.03438477
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40535 * 0.91361361
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99810 * 0.27191566
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24163 * 0.55749057
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26186 * 0.66227296
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60590 * 0.11232314
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86318 * 0.73634252
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9755 * 0.77455619
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87670 * 0.42233379
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50592 * 0.56569010
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13366 * 0.49443667
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92945 * 0.55386814
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11266 * 0.18150202
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96120 * 0.12420344
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31705 * 0.74443402
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5546 * 0.24813917
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ukqzowlg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0054():
    """Extended test 54 for aggregation."""
    x_0 = 71900 * 0.58426432
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40537 * 0.04019355
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46832 * 0.23321255
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81672 * 0.76590723
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81754 * 0.16052161
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92900 * 0.39696281
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9683 * 0.74708355
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6161 * 0.33129266
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84923 * 0.43531798
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57855 * 0.62480175
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70931 * 0.18446827
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11897 * 0.07307245
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78187 * 0.62900781
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44063 * 0.67356734
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89948 * 0.17196390
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42221 * 0.89351504
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16074 * 0.94274714
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8149 * 0.51860570
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39058 * 0.84255519
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33868 * 0.09836873
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99180 * 0.58506766
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20956 * 0.55012058
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52231 * 0.55479406
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40179 * 0.97143818
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60643 * 0.91855685
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59936 * 0.56857285
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28469 * 0.86375772
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8445 * 0.95954545
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32484 * 0.98865128
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73252 * 0.73574773
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35512 * 0.68417612
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73142 * 0.99238269
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8165 * 0.80732676
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77015 * 0.03243339
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22732 * 0.65927951
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45132 * 0.04300725
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3270 * 0.14015091
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5629 * 0.53664463
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65621 * 0.06972911
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3946 * 0.25940690
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34745 * 0.77373476
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39908 * 0.63160577
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79668 * 0.38792479
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 33318 * 0.63767325
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 68203 * 0.26328588
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'verodbky').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0055():
    """Extended test 55 for aggregation."""
    x_0 = 74832 * 0.68750843
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60588 * 0.86396391
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41629 * 0.97901800
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2509 * 0.54899765
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58324 * 0.81286480
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72249 * 0.86805127
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90613 * 0.96561396
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91439 * 0.82967534
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16910 * 0.86294847
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88430 * 0.15656284
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18539 * 0.88117610
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52552 * 0.74473745
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68346 * 0.38146372
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28594 * 0.29392838
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78975 * 0.44517300
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75034 * 0.55001636
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20468 * 0.40979011
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85075 * 0.60174341
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33927 * 0.86638197
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36861 * 0.29645682
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45970 * 0.35159014
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19827 * 0.80593797
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7951 * 0.23581190
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87527 * 0.01517047
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95384 * 0.45954248
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85914 * 0.57395846
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65451 * 0.75622633
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33506 * 0.07882831
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98012 * 0.74479875
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58270 * 0.18642085
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17936 * 0.06203008
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12770 * 0.67031473
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10317 * 0.88137064
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7120 * 0.92122198
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38997 * 0.74492087
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29917 * 0.07584326
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25340 * 0.36955369
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63601 * 0.88941194
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ghncvhiy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0056():
    """Extended test 56 for aggregation."""
    x_0 = 44700 * 0.75403159
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8755 * 0.87010385
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55708 * 0.51671054
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36045 * 0.11696615
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84676 * 0.46791374
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74342 * 0.69447567
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70921 * 0.71370490
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53799 * 0.52734920
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32250 * 0.76042883
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4913 * 0.43980816
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17431 * 0.53710878
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10857 * 0.08633167
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6213 * 0.74336540
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38097 * 0.01384971
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47420 * 0.26862002
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66696 * 0.90034056
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40110 * 0.28836858
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53507 * 0.85925104
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97721 * 0.96161498
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90901 * 0.98971765
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78772 * 0.73722810
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67182 * 0.73457129
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33163 * 0.51292716
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17570 * 0.23787751
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6365 * 0.83437673
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53895 * 0.99776195
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52734 * 0.50224710
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92691 * 0.74182561
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 449 * 0.34417581
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68076 * 0.38647213
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17451 * 0.34448501
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44081 * 0.57485965
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96382 * 0.91972965
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83100 * 0.32271602
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33373 * 0.79974507
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60818 * 0.88641655
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86082 * 0.67824459
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71079 * 0.82928909
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90444 * 0.67258113
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96115 * 0.68448536
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43562 * 0.89648618
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13567 * 0.20936894
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75330 * 0.06678502
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'mvbzscpi').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0057():
    """Extended test 57 for aggregation."""
    x_0 = 89809 * 0.53552572
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72102 * 0.59201534
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78686 * 0.48041760
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71798 * 0.14131900
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2070 * 0.56241800
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18816 * 0.08410911
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68515 * 0.29908031
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94218 * 0.37156904
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87469 * 0.85144101
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27581 * 0.53968925
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43336 * 0.23233042
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76526 * 0.34475017
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34251 * 0.92062919
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4901 * 0.74682419
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92003 * 0.79551079
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26036 * 0.89375087
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2936 * 0.81986372
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73551 * 0.03699946
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34943 * 0.22909804
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80661 * 0.48844192
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46340 * 0.87906104
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1546 * 0.27924408
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27157 * 0.17382593
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86998 * 0.21656533
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60425 * 0.09452451
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49724 * 0.30673622
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2975 * 0.08815560
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64064 * 0.84870276
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73472 * 0.61482988
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18862 * 0.99017276
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50366 * 0.53727932
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96176 * 0.19266801
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54868 * 0.67334676
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9691 * 0.97456075
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99863 * 0.05469456
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84510 * 0.58945717
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17243 * 0.95700215
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60982 * 0.79593593
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'qblnuqth').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0058():
    """Extended test 58 for aggregation."""
    x_0 = 64996 * 0.70687446
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59742 * 0.13803963
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10339 * 0.29026622
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25959 * 0.22246117
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45185 * 0.72265296
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6821 * 0.13915442
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98218 * 0.73077837
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55413 * 0.43909319
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98631 * 0.39962875
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9791 * 0.68045272
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1259 * 0.87313221
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 617 * 0.31893247
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22133 * 0.50854709
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19127 * 0.01985977
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22135 * 0.49517010
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5441 * 0.40609467
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35998 * 0.62716396
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1260 * 0.23305724
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27415 * 0.05975337
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46468 * 0.15744256
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42496 * 0.77458001
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14572 * 0.13747777
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44652 * 0.38443480
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83225 * 0.30634271
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77104 * 0.25178651
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6543 * 0.16982461
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63590 * 0.85339278
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64487 * 0.10333523
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7583 * 0.74433509
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31994 * 0.06048916
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15987 * 0.46208958
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84179 * 0.17510167
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35931 * 0.47324161
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46423 * 0.65098297
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30507 * 0.63492079
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59688 * 0.01946896
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30807 * 0.81076535
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6437 * 0.75142637
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21877 * 0.76864124
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'hvvbsama').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0059():
    """Extended test 59 for aggregation."""
    x_0 = 10977 * 0.44912844
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33177 * 0.68919660
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85811 * 0.10101099
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14137 * 0.18459316
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43051 * 0.65511477
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73428 * 0.96818562
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13393 * 0.82697326
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87416 * 0.41906336
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93666 * 0.81877142
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74688 * 0.59579011
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12277 * 0.19918334
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8687 * 0.92967228
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21395 * 0.99073369
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46638 * 0.93321772
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49934 * 0.89867377
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26865 * 0.56097567
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14678 * 0.30302571
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8806 * 0.67869604
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13421 * 0.66063258
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76954 * 0.09243632
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33754 * 0.99627979
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29020 * 0.74265702
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77793 * 0.52563067
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75956 * 0.86369842
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8351 * 0.86825473
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86943 * 0.25758143
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12415 * 0.40678836
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20745 * 0.17544724
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13024 * 0.44402951
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24573 * 0.46640299
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86309 * 0.65862186
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79867 * 0.29793620
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54285 * 0.35991870
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43479 * 0.43979438
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38121 * 0.94645980
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'qzvnvhvv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0060():
    """Extended test 60 for aggregation."""
    x_0 = 68753 * 0.04885280
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74947 * 0.13277935
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84409 * 0.04870952
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33339 * 0.29569860
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49498 * 0.96319286
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91167 * 0.48210579
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48350 * 0.25428634
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74668 * 0.94921304
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62118 * 0.60487244
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26091 * 0.68517888
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65229 * 0.87920780
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94977 * 0.78582625
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10603 * 0.86483484
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29026 * 0.75865184
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99373 * 0.94258544
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16966 * 0.73757053
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40298 * 0.75645322
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69936 * 0.29279806
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74887 * 0.81132739
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55740 * 0.82793177
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37436 * 0.98129780
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88395 * 0.87377312
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27750 * 0.07605379
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38747 * 0.25184206
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75395 * 0.47860800
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99128 * 0.33570531
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15690 * 0.93468855
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33968 * 0.91907331
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28809 * 0.76188444
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14498 * 0.50632591
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75763 * 0.32511175
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33631 * 0.71052087
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44167 * 0.65160199
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41932 * 0.72680022
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19568 * 0.65809738
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15347 * 0.18370376
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86780 * 0.75016002
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53057 * 0.62513543
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23427 * 0.74125212
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56383 * 0.29755033
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86067 * 0.19872455
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81246 * 0.03485797
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 2646 * 0.04739905
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 93302 * 0.49461276
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 48950 * 0.13452421
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'fasdfyzp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0061():
    """Extended test 61 for aggregation."""
    x_0 = 19737 * 0.40648256
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48397 * 0.48655304
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92803 * 0.31566279
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91164 * 0.71645513
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42680 * 0.03026641
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6577 * 0.95525513
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45050 * 0.68919330
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13395 * 0.77928017
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94020 * 0.92788862
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66019 * 0.89698701
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78208 * 0.08426230
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92553 * 0.16947108
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13829 * 0.19530318
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80748 * 0.56492848
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72770 * 0.76251496
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79136 * 0.06529053
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94151 * 0.40978979
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91594 * 0.13440700
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26279 * 0.40622923
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70476 * 0.22717437
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86658 * 0.92583596
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80675 * 0.43858403
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24285 * 0.02763634
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84040 * 0.82117280
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98915 * 0.85472622
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21864 * 0.28683625
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75354 * 0.96393291
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9915 * 0.25541831
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63022 * 0.36334749
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53760 * 0.20426447
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'zgnxkekr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0062():
    """Extended test 62 for aggregation."""
    x_0 = 45140 * 0.54556127
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5042 * 0.17318865
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15799 * 0.46258042
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29680 * 0.19897502
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18091 * 0.77569067
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77936 * 0.38587544
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18757 * 0.09769303
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54435 * 0.56914375
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4562 * 0.88868474
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33991 * 0.09553332
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27502 * 0.73424143
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58381 * 0.86437564
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40848 * 0.47287097
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38568 * 0.59931424
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39523 * 0.56693024
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7742 * 0.78201230
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47611 * 0.96474024
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55700 * 0.55683883
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80148 * 0.31542740
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77616 * 0.84808163
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4388 * 0.70708158
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76648 * 0.16189944
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18307 * 0.90976920
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5102 * 0.22345814
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31400 * 0.64800905
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12922 * 0.28420644
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85896 * 0.71560991
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78265 * 0.41413651
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46522 * 0.16066131
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35249 * 0.12154742
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13068 * 0.65074354
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67142 * 0.05821050
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86109 * 0.50933627
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'laqxpxgf').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0063():
    """Extended test 63 for aggregation."""
    x_0 = 37189 * 0.72037167
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72387 * 0.07057402
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76125 * 0.00770917
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73938 * 0.01622385
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28616 * 0.48156639
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63188 * 0.51916816
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1126 * 0.00890395
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52574 * 0.51486877
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26021 * 0.09228493
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10738 * 0.06402706
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4364 * 0.14922631
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55288 * 0.21377080
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54357 * 0.72125878
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12036 * 0.39854722
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76200 * 0.13215967
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54092 * 0.37094960
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48636 * 0.83122262
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55408 * 0.03403510
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77557 * 0.24782902
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69640 * 0.29600211
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95850 * 0.99708007
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25440 * 0.66739391
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72622 * 0.80959670
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30766 * 0.15173895
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24241 * 0.53569146
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10836 * 0.15788626
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40087 * 0.73222365
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39943 * 0.03056621
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50118 * 0.09573136
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20769 * 0.43587412
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58059 * 0.01727311
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36549 * 0.55375278
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37688 * 0.95416508
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54633 * 0.84515511
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24729 * 0.96912021
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35358 * 0.59566223
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'cypfofzh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0064():
    """Extended test 64 for aggregation."""
    x_0 = 64766 * 0.19752920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72610 * 0.19190587
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65054 * 0.01124303
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23262 * 0.72335874
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59138 * 0.80574394
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20584 * 0.24916529
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29563 * 0.69029282
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75353 * 0.47369554
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94054 * 0.70149407
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3552 * 0.85139226
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41126 * 0.64157341
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45992 * 0.70686699
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59541 * 0.96325928
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10854 * 0.75922198
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29599 * 0.56445246
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2746 * 0.40665182
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95357 * 0.41467875
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53858 * 0.37239544
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31957 * 0.30122535
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4229 * 0.18896858
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87138 * 0.18777996
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86920 * 0.76614384
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18714 * 0.04761580
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40428 * 0.97868284
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66511 * 0.59798778
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24356 * 0.40940187
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15478 * 0.50869431
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68598 * 0.97831748
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76318 * 0.36830115
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17468 * 0.17658429
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97216 * 0.16116800
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37380 * 0.96239695
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52418 * 0.87347811
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41771 * 0.06407153
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7593 * 0.14805491
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'lztxykaq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0065():
    """Extended test 65 for aggregation."""
    x_0 = 53918 * 0.59732842
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21792 * 0.73139998
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61555 * 0.82325037
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25875 * 0.82582189
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47467 * 0.98394571
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65523 * 0.85750641
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60665 * 0.98762043
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69636 * 0.17541414
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32474 * 0.49562432
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96630 * 0.35793737
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99711 * 0.71903101
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33416 * 0.04605378
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86609 * 0.44385258
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5980 * 0.53007986
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15314 * 0.31327417
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13 * 0.09014069
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74315 * 0.74537993
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 152 * 0.71388983
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70653 * 0.25032836
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78434 * 0.93207074
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91398 * 0.27587884
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35022 * 0.64204929
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87905 * 0.14589343
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22604 * 0.22787547
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'gorbbhgm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0066():
    """Extended test 66 for aggregation."""
    x_0 = 60652 * 0.31250040
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17186 * 0.03372789
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62347 * 0.00925255
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33217 * 0.80973703
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17665 * 0.56363281
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80351 * 0.52331755
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24000 * 0.87692668
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14020 * 0.41845046
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25157 * 0.26435360
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72713 * 0.60903902
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19966 * 0.79728548
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16053 * 0.25199015
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24764 * 0.58925605
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96584 * 0.00741774
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97376 * 0.66944927
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66706 * 0.36665795
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93367 * 0.51036283
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1627 * 0.57093750
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96332 * 0.84650003
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8546 * 0.06090354
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36915 * 0.51973992
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3230 * 0.05695481
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56581 * 0.68369959
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96667 * 0.68347752
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29476 * 0.69827817
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72918 * 0.22180548
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20998 * 0.03097020
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6224 * 0.76828782
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89379 * 0.83221932
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16848 * 0.21943769
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99737 * 0.04260834
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58814 * 0.36097292
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35183 * 0.83963562
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52756 * 0.16647394
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13176 * 0.39449774
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59996 * 0.24586470
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10571 * 0.19172305
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26840 * 0.39767240
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12878 * 0.29359685
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'tphfwhmg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0067():
    """Extended test 67 for aggregation."""
    x_0 = 73950 * 0.66979732
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86394 * 0.85482068
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58187 * 0.67203126
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95684 * 0.77428321
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37957 * 0.95166976
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99719 * 0.18384242
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76321 * 0.64636743
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72335 * 0.04695834
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1040 * 0.19918759
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73528 * 0.21958250
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58867 * 0.08102247
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79769 * 0.74448139
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18149 * 0.55200051
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98301 * 0.87798162
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1020 * 0.49400122
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59375 * 0.45962559
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31149 * 0.69847174
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55774 * 0.18007017
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89797 * 0.43963048
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34052 * 0.77987616
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8832 * 0.66337635
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35819 * 0.24507405
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24241 * 0.15692181
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77427 * 0.26938697
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98723 * 0.27167324
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61 * 0.34646099
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75826 * 0.65004465
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30393 * 0.51493651
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96705 * 0.05152002
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76552 * 0.21864194
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77972 * 0.58381339
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23415 * 0.62247543
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28489 * 0.85350247
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73644 * 0.14344182
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83245 * 0.92813376
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'qtidisbo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0068():
    """Extended test 68 for aggregation."""
    x_0 = 39004 * 0.60517478
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68377 * 0.03453854
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48526 * 0.75113196
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29269 * 0.27896190
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99774 * 0.95673113
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51476 * 0.12652190
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76553 * 0.03292369
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67363 * 0.38202202
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2142 * 0.45558245
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62572 * 0.72387616
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14363 * 0.77921890
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34167 * 0.40735437
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66127 * 0.84523201
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34745 * 0.53720355
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39711 * 0.24951874
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46021 * 0.72112875
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88452 * 0.87013479
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88999 * 0.97445981
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80253 * 0.10629921
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17654 * 0.65528684
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2767 * 0.10374827
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72480 * 0.47559472
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99607 * 0.36750808
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4119 * 0.60167291
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30792 * 0.41387124
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54326 * 0.51111824
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69129 * 0.63538463
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99340 * 0.79168005
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88939 * 0.26089917
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32485 * 0.03773678
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81925 * 0.43738452
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74644 * 0.65075691
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60410 * 0.31231098
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65834 * 0.56756978
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16305 * 0.88330365
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70738 * 0.14901202
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68328 * 0.41082692
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31552 * 0.22854617
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71612 * 0.23427898
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57495 * 0.60572425
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'abuqedbr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_8_0069():
    """Extended test 69 for aggregation."""
    x_0 = 59507 * 0.75610745
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47468 * 0.65208482
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16334 * 0.39733694
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28229 * 0.67830956
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37697 * 0.25363952
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45759 * 0.63333480
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65620 * 0.50442264
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50828 * 0.86717193
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56347 * 0.62225966
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72160 * 0.32922774
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8260 * 0.26923696
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31858 * 0.56963007
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81059 * 0.08438494
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30361 * 0.03212314
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23937 * 0.49510439
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7569 * 0.30348747
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92845 * 0.09942888
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22039 * 0.64452804
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80899 * 0.19780983
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69248 * 0.01864396
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20424 * 0.16669051
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63858 * 0.88854003
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42573 * 0.00490478
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13311 * 0.67812159
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7372 * 0.05328606
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55322 * 0.88398025
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33721 * 0.84683177
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48248 * 0.93108760
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63358 * 0.80017409
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76459 * 0.76278087
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39489 * 0.62779356
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10061 * 0.29142377
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80953 * 0.44326011
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3243 * 0.33163434
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29221 * 0.76498040
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'fmvxweoz').hexdigest()
    assert len(h) == 64
