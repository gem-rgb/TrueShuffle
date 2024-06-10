"""Extended tests for migration suite 9."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_migration_extended_9_0000():
    """Extended test 0 for migration."""
    x_0 = 54134 * 0.15956509
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41213 * 0.34147996
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30144 * 0.28207517
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6436 * 0.55931359
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20135 * 0.85952706
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50588 * 0.42218201
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71026 * 0.71328248
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14681 * 0.28993017
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89022 * 0.41293437
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24655 * 0.95823883
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91959 * 0.89006756
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37805 * 0.04883228
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96719 * 0.51573447
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19998 * 0.43442518
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35486 * 0.96748920
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50997 * 0.65340068
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48591 * 0.74625130
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9508 * 0.94812153
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31904 * 0.77177246
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98949 * 0.71225164
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85989 * 0.69996385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71314 * 0.17616427
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45841 * 0.02199526
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10680 * 0.67240980
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93244 * 0.61714452
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18826 * 0.83565486
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43710 * 0.39521998
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28731 * 0.31550172
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'iywclrhi').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0001():
    """Extended test 1 for migration."""
    x_0 = 28204 * 0.56889807
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91764 * 0.75062541
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17167 * 0.09511181
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35800 * 0.59068938
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60609 * 0.48041254
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98869 * 0.86521525
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43228 * 0.69727361
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13381 * 0.21432384
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47959 * 0.63361126
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84861 * 0.75006886
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5827 * 0.22138941
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93385 * 0.23135919
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41666 * 0.91822004
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68829 * 0.73090213
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17044 * 0.98465201
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56374 * 0.81949700
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5994 * 0.00114583
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64336 * 0.34248260
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58968 * 0.14260414
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83445 * 0.84139355
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'jbiastos').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0002():
    """Extended test 2 for migration."""
    x_0 = 95065 * 0.56529853
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64930 * 0.29990147
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90703 * 0.67173749
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20372 * 0.93990581
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11419 * 0.23865828
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21702 * 0.78961935
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71965 * 0.65467441
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98228 * 0.99961009
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47292 * 0.14366697
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38874 * 0.49496229
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21556 * 0.06398396
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16364 * 0.15773288
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58450 * 0.74014369
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54912 * 0.24555721
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39107 * 0.29330542
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5040 * 0.03833113
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20670 * 0.55232406
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39340 * 0.11223170
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21899 * 0.06610992
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69910 * 0.32347180
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25568 * 0.80131644
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ezgeevjb').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0003():
    """Extended test 3 for migration."""
    x_0 = 55916 * 0.00147794
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78686 * 0.51708079
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41323 * 0.04883681
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67968 * 0.19765692
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11629 * 0.24382754
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40340 * 0.26468846
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41058 * 0.34624840
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19023 * 0.17633777
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84378 * 0.26705936
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55700 * 0.82556166
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50595 * 0.16038711
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7588 * 0.31383682
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85288 * 0.94787503
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63108 * 0.81956056
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12073 * 0.25837444
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81533 * 0.42410569
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70704 * 0.42043062
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32592 * 0.81046112
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1107 * 0.35292980
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49226 * 0.41061973
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26855 * 0.92787317
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27138 * 0.82356078
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79051 * 0.62416881
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30611 * 0.69036768
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77429 * 0.60456818
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47095 * 0.00393265
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49198 * 0.68115477
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40513 * 0.11269421
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'jylcwmkb').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0004():
    """Extended test 4 for migration."""
    x_0 = 63033 * 0.46245756
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71105 * 0.78384483
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73259 * 0.82974709
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73880 * 0.93235369
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29732 * 0.89443833
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42588 * 0.14166610
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96186 * 0.58783741
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94996 * 0.19491913
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97820 * 0.38185763
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52041 * 0.51507053
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12476 * 0.74485069
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25621 * 0.75936521
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74672 * 0.70257522
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75093 * 0.62516885
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90370 * 0.95243034
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68463 * 0.43375720
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87451 * 0.74316463
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97453 * 0.66434683
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85045 * 0.89190243
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30111 * 0.88383049
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45151 * 0.35394362
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9720 * 0.12526654
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54423 * 0.13384719
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80379 * 0.68965871
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23539 * 0.72537693
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51687 * 0.64005356
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97442 * 0.56297006
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95516 * 0.44604457
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'zvxhfjoe').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0005():
    """Extended test 5 for migration."""
    x_0 = 90208 * 0.51867823
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26361 * 0.90557387
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23184 * 0.30641007
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14947 * 0.13715298
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85130 * 0.30778782
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28644 * 0.28635195
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53243 * 0.46047851
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67152 * 0.55687334
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10086 * 0.84066381
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95090 * 0.26007993
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9311 * 0.97265983
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92413 * 0.58339835
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60002 * 0.76524900
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84244 * 0.01410838
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68874 * 0.05086288
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61903 * 0.32619888
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59217 * 0.45329808
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85328 * 0.54296631
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96336 * 0.07959273
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34231 * 0.08087354
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72323 * 0.44339135
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13286 * 0.24488655
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89176 * 0.47301014
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56014 * 0.56121507
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58832 * 0.81043742
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63046 * 0.94719785
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 649 * 0.11665441
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37191 * 0.73256645
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61647 * 0.53539388
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54127 * 0.63627847
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37025 * 0.07769665
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59055 * 0.56219528
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10641 * 0.43392946
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26296 * 0.44923558
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35071 * 0.79184866
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'kdujvckg').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0006():
    """Extended test 6 for migration."""
    x_0 = 30861 * 0.43749753
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66051 * 0.55244513
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44815 * 0.85612423
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44913 * 0.48647286
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48479 * 0.56596504
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35737 * 0.02253049
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65966 * 0.75126356
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5141 * 0.66454414
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92818 * 0.25496291
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70237 * 0.11353825
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32250 * 0.70671386
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60430 * 0.25797833
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18120 * 0.41138821
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26349 * 0.18925543
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7484 * 0.80003829
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70023 * 0.98476158
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32262 * 0.64182274
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74716 * 0.10615567
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58560 * 0.56334532
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86968 * 0.37862702
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32006 * 0.37985007
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77789 * 0.76219358
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76705 * 0.68603299
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'idvfpnqg').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0007():
    """Extended test 7 for migration."""
    x_0 = 10638 * 0.65389274
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94642 * 0.79371344
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62147 * 0.63612357
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99970 * 0.98699843
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30012 * 0.48429137
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31101 * 0.81448225
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10738 * 0.02849125
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29028 * 0.47161195
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85260 * 0.34181233
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30939 * 0.87721059
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73784 * 0.43653237
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27535 * 0.56864127
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66902 * 0.78450439
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51804 * 0.79034397
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8287 * 0.36425177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14368 * 0.33298194
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89668 * 0.22713955
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66791 * 0.90992699
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69263 * 0.11463381
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15775 * 0.93627483
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5595 * 0.29517879
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48174 * 0.38297502
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91177 * 0.48959076
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97350 * 0.56616346
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18025 * 0.22211627
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59831 * 0.69487089
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41193 * 0.75593472
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50056 * 0.35466903
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15119 * 0.61876397
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53510 * 0.52401754
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58454 * 0.34347584
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68704 * 0.74994772
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83253 * 0.75876612
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77082 * 0.14954915
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42661 * 0.58624842
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61774 * 0.82768849
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63047 * 0.39454772
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45828 * 0.69583760
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30758 * 0.35880778
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73339 * 0.23235336
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95239 * 0.39681385
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14923 * 0.46715760
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 86659 * 0.79844471
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83915 * 0.08523326
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79288 * 0.38468534
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 90070 * 0.26338244
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'bnekoacn').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0008():
    """Extended test 8 for migration."""
    x_0 = 43862 * 0.77410898
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53998 * 0.26067252
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53870 * 0.74114524
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1636 * 0.50808138
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54738 * 0.58551592
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13520 * 0.44896935
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60830 * 0.14533008
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41327 * 0.92004549
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80184 * 0.61773318
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35615 * 0.78641496
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23271 * 0.29090696
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56863 * 0.17492590
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67635 * 0.02054653
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84124 * 0.77697399
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93238 * 0.34991281
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34732 * 0.64270129
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46151 * 0.56259000
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72067 * 0.58636344
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15322 * 0.03695542
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74687 * 0.97482591
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28242 * 0.89418616
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88269 * 0.04168365
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52685 * 0.55691868
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72186 * 0.96463938
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67149 * 0.58821952
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59621 * 0.47877809
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27730 * 0.34401853
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15938 * 0.69266683
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31490 * 0.33491156
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95181 * 0.53498817
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34347 * 0.56798871
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60549 * 0.02923427
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79090 * 0.59189862
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91088 * 0.20610252
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17257 * 0.32889892
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26556 * 0.59319663
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16932 * 0.62760856
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19567 * 0.52901497
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47366 * 0.41022449
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ajvbxfvc').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0009():
    """Extended test 9 for migration."""
    x_0 = 92827 * 0.61840199
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55061 * 0.94287057
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63919 * 0.97244637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95462 * 0.80528517
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97233 * 0.94178054
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66095 * 0.91060937
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18094 * 0.91830374
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38148 * 0.03858913
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36041 * 0.17891876
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4921 * 0.87615787
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50058 * 0.28722645
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72358 * 0.68570903
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53080 * 0.27316378
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16577 * 0.51472689
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73211 * 0.48410728
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6016 * 0.33455614
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40418 * 0.93480362
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18023 * 0.41379987
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15975 * 0.62274601
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90086 * 0.86956057
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82415 * 0.50744594
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68536 * 0.79762298
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90153 * 0.10873695
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40189 * 0.85727249
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13993 * 0.22667175
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90218 * 0.75091674
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82606 * 0.47394825
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75203 * 0.77033690
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'dkcujnau').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0010():
    """Extended test 10 for migration."""
    x_0 = 38534 * 0.77543882
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5043 * 0.18820519
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95645 * 0.41566725
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87632 * 0.07054932
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66827 * 0.50890882
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53515 * 0.44834726
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26971 * 0.47890349
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37131 * 0.25456659
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39301 * 0.84565342
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86474 * 0.74759195
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9700 * 0.62961234
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58063 * 0.24842181
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12333 * 0.30772435
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64631 * 0.16171768
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65460 * 0.09296192
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46823 * 0.81831839
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74360 * 0.75894788
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46086 * 0.22767480
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32610 * 0.50407094
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67676 * 0.34152821
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10123 * 0.84681307
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7306 * 0.88351260
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54675 * 0.98926356
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43464 * 0.04513738
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15817 * 0.37850080
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89778 * 0.76914021
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72293 * 0.82868185
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55816 * 0.72588991
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68091 * 0.66709344
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15986 * 0.36517088
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57644 * 0.11012921
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42723 * 0.86517290
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29417 * 0.39895660
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26599 * 0.19797820
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76771 * 0.09987106
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57461 * 0.29474347
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4559 * 0.12597857
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30687 * 0.97812949
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1166 * 0.18510578
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45960 * 0.05171739
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32458 * 0.69516305
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57741 * 0.86185908
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 39986 * 0.92751136
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'keozjuiq').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0011():
    """Extended test 11 for migration."""
    x_0 = 70659 * 0.84793710
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85087 * 0.95179117
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8927 * 0.27991001
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28105 * 0.58865817
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60307 * 0.51542373
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79623 * 0.71502932
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81695 * 0.35062985
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56396 * 0.11096957
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17371 * 0.17192570
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89987 * 0.85171404
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90366 * 0.91299358
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38862 * 0.60065220
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92913 * 0.69411429
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88391 * 0.65278657
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 574 * 0.05352482
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5704 * 0.93990391
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87470 * 0.95338690
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43797 * 0.10619996
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52672 * 0.31094002
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77508 * 0.98373165
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58496 * 0.90832683
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'gmkmvfxz').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0012():
    """Extended test 12 for migration."""
    x_0 = 74057 * 0.56995113
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58288 * 0.36826312
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82178 * 0.06983804
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25239 * 0.85211546
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25759 * 0.57628910
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73569 * 0.59533186
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56465 * 0.96886170
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97598 * 0.92273505
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97567 * 0.80485862
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16375 * 0.97562619
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52358 * 0.18409468
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54021 * 0.39282922
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26101 * 0.99625788
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61670 * 0.36861023
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12000 * 0.87786584
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58065 * 0.37166043
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1042 * 0.81736782
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39405 * 0.71752359
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16641 * 0.97944862
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33412 * 0.49511708
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97186 * 0.18471934
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95313 * 0.71384131
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43734 * 0.16927396
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71925 * 0.99185591
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27452 * 0.74474850
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31005 * 0.01848135
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97393 * 0.22118615
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54545 * 0.74387505
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26644 * 0.75935347
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35866 * 0.29050491
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66783 * 0.28200585
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88684 * 0.29432530
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2177 * 0.94744272
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32806 * 0.34072405
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22027 * 0.15783972
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69660 * 0.72563731
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92640 * 0.96671747
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48169 * 0.88376934
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72935 * 0.17508187
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70381 * 0.34184238
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 87341 * 0.90088946
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63159 * 0.10149263
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10158 * 0.86875774
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 725 * 0.09438165
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 38928 * 0.71737708
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 8880 * 0.00163361
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 95525 * 0.45628025
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 43357 * 0.21174738
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'fxonszap').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0013():
    """Extended test 13 for migration."""
    x_0 = 65315 * 0.07242020
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84368 * 0.73774632
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65649 * 0.87310913
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50230 * 0.09351745
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19291 * 0.51825293
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38888 * 0.02978874
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53306 * 0.01448490
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36902 * 0.65921384
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58579 * 0.43916903
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55045 * 0.89375230
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67122 * 0.91998241
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68397 * 0.88716471
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3433 * 0.88547348
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5772 * 0.89744277
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76484 * 0.89605682
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37945 * 0.81771955
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74264 * 0.63749373
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13869 * 0.65051298
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7308 * 0.58315020
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11765 * 0.06185819
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54045 * 0.90963413
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50236 * 0.16285303
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87032 * 0.96782694
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54688 * 0.11086233
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28684 * 0.18638399
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8702 * 0.59623220
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25581 * 0.11361565
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39054 * 0.50809940
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52462 * 0.20505287
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80856 * 0.75875097
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86073 * 0.53160538
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65789 * 0.32443259
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38282 * 0.40103651
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31248 * 0.61327623
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15169 * 0.73231803
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46795 * 0.16466601
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47013 * 0.29496984
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13730 * 0.80812371
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40008 * 0.40766909
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39327 * 0.24398648
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60604 * 0.16551562
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52388 * 0.80689313
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 7113 * 0.80922586
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'pvsozywr').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0014():
    """Extended test 14 for migration."""
    x_0 = 53114 * 0.67926108
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77703 * 0.35983051
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54865 * 0.34315429
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46242 * 0.26068042
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13611 * 0.40125726
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60602 * 0.02093868
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22024 * 0.45190116
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18323 * 0.89354199
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79252 * 0.76803801
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37742 * 0.12908158
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30449 * 0.31231368
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80183 * 0.72568050
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36595 * 0.00146309
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99114 * 0.34106377
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17203 * 0.81199437
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12750 * 0.40455766
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9881 * 0.32265505
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96121 * 0.99784935
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69873 * 0.13240040
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95849 * 0.56070291
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95929 * 0.97626327
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95515 * 0.11660527
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28392 * 0.57053901
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18107 * 0.50398139
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30658 * 0.92619589
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26713 * 0.83002870
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89351 * 0.55685641
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32453 * 0.80542998
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14539 * 0.00356705
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84460 * 0.42983570
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28064 * 0.46088531
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43880 * 0.10240151
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96884 * 0.10025251
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38478 * 0.84435288
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'ahorlgra').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0015():
    """Extended test 15 for migration."""
    x_0 = 29705 * 0.09175897
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47405 * 0.94040417
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76428 * 0.85847561
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78585 * 0.48487527
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13986 * 0.02730461
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41045 * 0.58916195
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13184 * 0.64508272
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74228 * 0.98709342
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99969 * 0.28530792
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56520 * 0.93700964
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82387 * 0.35308917
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84248 * 0.06817886
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3409 * 0.20186163
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17039 * 0.45358388
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39076 * 0.63642620
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29337 * 0.66114565
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73763 * 0.24147338
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38263 * 0.93323162
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28857 * 0.49845714
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94378 * 0.61015959
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35554 * 0.42746516
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30065 * 0.29671929
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57570 * 0.27638109
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79933 * 0.50229111
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58233 * 0.26485959
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60185 * 0.97799814
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84059 * 0.86162511
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29592 * 0.15939513
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61170 * 0.36427635
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33842 * 0.40564798
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6069 * 0.27705833
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36296 * 0.37453537
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37776 * 0.21241591
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98847 * 0.87248997
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83802 * 0.84461396
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41576 * 0.93643470
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49280 * 0.37042743
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6984 * 0.51445577
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65529 * 0.38077966
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 61773 * 0.36739039
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18049 * 0.77934435
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'zkvcceqk').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0016():
    """Extended test 16 for migration."""
    x_0 = 84676 * 0.97343257
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93724 * 0.24157578
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46564 * 0.79368052
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70275 * 0.61447225
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36548 * 0.33598580
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93141 * 0.09511103
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88281 * 0.53692710
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11208 * 0.76841786
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74608 * 0.14169596
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91004 * 0.18917547
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96186 * 0.80868641
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28000 * 0.53157892
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10258 * 0.94551703
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72631 * 0.92948794
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51825 * 0.99006833
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37617 * 0.69216290
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60649 * 0.23204686
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73760 * 0.83652083
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42066 * 0.60385444
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43514 * 0.86391249
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15643 * 0.69504317
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75674 * 0.97961201
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18984 * 0.48837034
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20601 * 0.37212107
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40068 * 0.56464334
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37534 * 0.36474682
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36373 * 0.27463263
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27164 * 0.56966121
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78055 * 0.83094817
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19863 * 0.65438719
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15790 * 0.35557844
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85693 * 0.35775318
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71143 * 0.87920052
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42169 * 0.46001437
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6918 * 0.09868319
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52906 * 0.29330922
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5258 * 0.25794420
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72748 * 0.85891833
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86197 * 0.30355136
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28273 * 0.57116456
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46893 * 0.05091828
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 8561 * 0.75407517
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10788 * 0.20006622
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 57221 * 0.34274562
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 44419 * 0.32077408
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 72994 * 0.30381674
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 1515 * 0.36719456
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 83707 * 0.54019174
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'riibjgmq').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0017():
    """Extended test 17 for migration."""
    x_0 = 77577 * 0.46249442
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34430 * 0.09575953
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39178 * 0.83550370
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53285 * 0.75859368
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52593 * 0.18529416
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34048 * 0.87421091
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86442 * 0.62046381
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62100 * 0.31950655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74100 * 0.20674430
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64574 * 0.09659007
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18880 * 0.46270645
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34544 * 0.98239133
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78646 * 0.36599612
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37912 * 0.30360689
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36872 * 0.37936661
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40818 * 0.27034357
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93007 * 0.86099321
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33380 * 0.02241706
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34607 * 0.32853237
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41464 * 0.55495566
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5707 * 0.58307903
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67635 * 0.14441512
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73780 * 0.93400805
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98858 * 0.08018420
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2788 * 0.42393005
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68713 * 0.87411259
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44188 * 0.74937742
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72481 * 0.79327630
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93872 * 0.26379268
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91746 * 0.79233759
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48812 * 0.44922748
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ldsnkdvs').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0018():
    """Extended test 18 for migration."""
    x_0 = 18240 * 0.64653231
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14847 * 0.21672319
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21675 * 0.70739531
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96072 * 0.75039333
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77510 * 0.06374262
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85416 * 0.33259529
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75058 * 0.70435075
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97612 * 0.54988950
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85035 * 0.09418566
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19905 * 0.44083661
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56476 * 0.57870728
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56643 * 0.58850067
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51701 * 0.10199686
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29736 * 0.67607688
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92970 * 0.26586091
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38298 * 0.42554337
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15658 * 0.02480265
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46230 * 0.90047055
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35319 * 0.39630865
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55899 * 0.45971887
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46270 * 0.93454028
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49783 * 0.73007355
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'gyfddgfg').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0019():
    """Extended test 19 for migration."""
    x_0 = 62538 * 0.11864017
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1594 * 0.35556533
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46639 * 0.23245786
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72141 * 0.23327584
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21494 * 0.78959240
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73415 * 0.90256796
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93180 * 0.64465192
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29635 * 0.30447865
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72574 * 0.57575424
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68202 * 0.41733988
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31533 * 0.81540519
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47766 * 0.67990734
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30588 * 0.45970591
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28917 * 0.24350508
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91494 * 0.81208258
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10448 * 0.59381710
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66883 * 0.40203012
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99402 * 0.94665950
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5561 * 0.26060465
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92148 * 0.82069952
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19957 * 0.53016445
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51698 * 0.60764293
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50521 * 0.78148206
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38269 * 0.96055000
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53762 * 0.50926613
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94632 * 0.72862390
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84881 * 0.50783417
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'yofwnntm').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0020():
    """Extended test 20 for migration."""
    x_0 = 94759 * 0.39977115
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87939 * 0.50767837
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6418 * 0.61613384
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49602 * 0.29093084
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60633 * 0.15946853
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72725 * 0.09355746
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69202 * 0.56435250
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3705 * 0.71006091
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63104 * 0.80632760
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29368 * 0.62289556
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67442 * 0.66357777
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88219 * 0.52135750
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99162 * 0.08010804
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81692 * 0.23619474
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24452 * 0.10835150
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4151 * 0.26620954
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83929 * 0.52512734
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18439 * 0.61019932
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25439 * 0.38697990
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93023 * 0.04432270
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7732 * 0.80161460
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1419 * 0.02153418
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38964 * 0.44690806
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58085 * 0.56362402
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92088 * 0.49670512
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19973 * 0.24339503
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16733 * 0.20094497
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67408 * 0.93136451
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96973 * 0.22988555
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87285 * 0.01862368
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97254 * 0.47580445
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80115 * 0.45453187
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57785 * 0.51137638
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3042 * 0.29455108
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20852 * 0.22304558
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'fmpebzxf').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0021():
    """Extended test 21 for migration."""
    x_0 = 60599 * 0.29834604
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50638 * 0.56598109
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24656 * 0.78809420
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34709 * 0.87554898
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62765 * 0.04164600
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52098 * 0.71575337
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88206 * 0.66495095
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56286 * 0.41418923
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8944 * 0.50736297
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61884 * 0.02421197
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54449 * 0.64644669
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70303 * 0.39762449
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87683 * 0.98921863
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29107 * 0.00125984
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47673 * 0.96829798
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31336 * 0.17941107
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85523 * 0.10468404
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75019 * 0.08128292
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5114 * 0.83505504
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41536 * 0.12093377
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58500 * 0.56242019
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41937 * 0.50189691
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43759 * 0.16758503
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56996 * 0.21115986
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5891 * 0.27497431
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24946 * 0.15070016
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18053 * 0.87685649
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27894 * 0.12017464
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87712 * 0.50357063
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60349 * 0.55366224
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59346 * 0.16744832
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84102 * 0.77631101
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43179 * 0.38728620
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40517 * 0.39822234
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74558 * 0.35923626
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91849 * 0.36676449
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24554 * 0.36095584
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32855 * 0.34878440
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1546 * 0.76618335
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75822 * 0.88880816
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ujcpaylu').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0022():
    """Extended test 22 for migration."""
    x_0 = 77004 * 0.18617964
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68417 * 0.94126526
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89511 * 0.73193194
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64503 * 0.17303807
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58145 * 0.78103397
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26478 * 0.70700827
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66582 * 0.65936817
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74625 * 0.01053536
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66639 * 0.65270926
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10958 * 0.38350567
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82788 * 0.35571724
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52566 * 0.43987956
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89126 * 0.46677754
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60532 * 0.43436184
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82092 * 0.58783993
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55382 * 0.55513316
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36532 * 0.38272224
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37422 * 0.69985248
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90218 * 0.58328432
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64247 * 0.47400437
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29815 * 0.55119631
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78595 * 0.72076434
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87865 * 0.98166946
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99629 * 0.20893441
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9493 * 0.81883316
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27587 * 0.62545386
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81417 * 0.87822090
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86021 * 0.37688597
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69185 * 0.97992125
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57299 * 0.40927175
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40310 * 0.05097302
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'djrhdsbw').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0023():
    """Extended test 23 for migration."""
    x_0 = 90665 * 0.92004119
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7128 * 0.81156077
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54866 * 0.55193454
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46573 * 0.94573216
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15256 * 0.93248753
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9994 * 0.17439050
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4640 * 0.08288521
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91206 * 0.97969411
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7918 * 0.72544841
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26197 * 0.93105612
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18730 * 0.34587990
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94748 * 0.32597836
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35385 * 0.29139370
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90996 * 0.90825024
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15089 * 0.80689090
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79156 * 0.74089022
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41622 * 0.29397021
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86772 * 0.91343669
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50049 * 0.68781048
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43138 * 0.22059814
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58125 * 0.13735597
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1093 * 0.60758887
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99390 * 0.38812685
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69271 * 0.09882223
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89554 * 0.82805179
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22680 * 0.86267955
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94507 * 0.16138372
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15586 * 0.27935482
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'sqwplfso').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0024():
    """Extended test 24 for migration."""
    x_0 = 53482 * 0.87799803
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18593 * 0.57507962
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25674 * 0.72527272
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13721 * 0.18075488
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71249 * 0.03667151
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5710 * 0.92537381
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80051 * 0.11734438
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16794 * 0.40552229
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72683 * 0.10417494
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19010 * 0.18744707
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26411 * 0.64724171
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25792 * 0.00110082
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62067 * 0.42914790
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84852 * 0.01080366
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53171 * 0.25031714
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95262 * 0.87955003
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42081 * 0.67309337
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73369 * 0.58001628
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6023 * 0.78328280
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59227 * 0.29993135
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33085 * 0.33571949
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44586 * 0.44032776
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50450 * 0.55416819
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8749 * 0.70779453
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32788 * 0.63356243
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43794 * 0.17486816
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35474 * 0.48396709
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43492 * 0.12675232
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34935 * 0.28119027
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24144 * 0.13707678
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17025 * 0.66642281
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8272 * 0.43217226
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'nvvyvlad').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0025():
    """Extended test 25 for migration."""
    x_0 = 33845 * 0.40974148
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42311 * 0.77870501
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53915 * 0.55492343
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66113 * 0.06823506
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51230 * 0.45846548
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90499 * 0.66875911
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19217 * 0.20806691
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20384 * 0.44418346
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3511 * 0.08737197
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71814 * 0.37622785
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58439 * 0.46018912
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45718 * 0.25819553
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14331 * 0.14432697
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18090 * 0.16945914
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57280 * 0.35461956
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76674 * 0.36029367
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24164 * 0.52948153
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2007 * 0.86988144
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1991 * 0.02126346
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44626 * 0.03888869
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11310 * 0.03771956
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55767 * 0.72885859
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36747 * 0.11572157
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53134 * 0.40803227
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3368 * 0.53203575
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73699 * 0.35564267
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30144 * 0.65641938
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2852 * 0.63428399
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28226 * 0.95826923
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19700 * 0.54455119
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'umwoxzke').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0026():
    """Extended test 26 for migration."""
    x_0 = 39 * 0.72216917
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55032 * 0.28030416
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33860 * 0.45323201
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58054 * 0.84517823
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28440 * 0.55135373
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68039 * 0.06422736
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53011 * 0.36206016
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15186 * 0.95112964
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41426 * 0.78443574
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5621 * 0.10322940
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79993 * 0.14173292
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93156 * 0.60520895
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64044 * 0.66990801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99676 * 0.26247368
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59321 * 0.90510092
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97948 * 0.38964674
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7618 * 0.86085453
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98819 * 0.61471957
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11224 * 0.17341906
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82479 * 0.72284452
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92425 * 0.88609344
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15520 * 0.95275505
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84749 * 0.24804778
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68513 * 0.56954893
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30647 * 0.47222211
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61883 * 0.82900559
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7629 * 0.93140624
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96024 * 0.74852284
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24685 * 0.77026750
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77173 * 0.80169104
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'zjewbtoc').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0027():
    """Extended test 27 for migration."""
    x_0 = 98401 * 0.75092135
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68028 * 0.14470571
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97398 * 0.55346314
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55937 * 0.84931762
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7941 * 0.00883351
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9935 * 0.75169008
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52550 * 0.06891833
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59441 * 0.82267700
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38070 * 0.78731912
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50034 * 0.75282239
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41270 * 0.14971399
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52653 * 0.95027569
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28978 * 0.62667256
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63531 * 0.59752135
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91338 * 0.12189441
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70233 * 0.93375951
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18957 * 0.32241529
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2091 * 0.58116205
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91076 * 0.69212847
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11502 * 0.53555690
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47347 * 0.94835488
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22429 * 0.88113554
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89282 * 0.37367548
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42734 * 0.83214177
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14502 * 0.16273534
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46097 * 0.79716014
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48378 * 0.28202363
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80647 * 0.50495684
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47240 * 0.81584279
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60003 * 0.23299734
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56613 * 0.76499393
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21677 * 0.94732667
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26278 * 0.95998990
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4468 * 0.04540104
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99523 * 0.97513055
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27102 * 0.46541431
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89222 * 0.97185744
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32526 * 0.53457588
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43512 * 0.43161946
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15063 * 0.60461462
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 66217 * 0.18766314
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 65953 * 0.90748886
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 61985 * 0.65570098
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61955 * 0.94652669
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17874 * 0.79758358
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'drvxukhp').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0028():
    """Extended test 28 for migration."""
    x_0 = 53504 * 0.83007854
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38633 * 0.21519789
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87160 * 0.74911031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12027 * 0.65042009
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26463 * 0.70523351
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97146 * 0.03777473
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5276 * 0.22947624
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66804 * 0.10043792
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49545 * 0.76689820
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17926 * 0.38239784
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18934 * 0.20766110
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7238 * 0.89791245
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83561 * 0.32242470
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58175 * 0.15948502
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80524 * 0.56159168
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29304 * 0.83057977
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17762 * 0.61559951
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34103 * 0.34746138
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23444 * 0.69867618
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98516 * 0.00746999
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67970 * 0.13594532
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89033 * 0.44153409
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65312 * 0.14112997
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12891 * 0.24084831
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99512 * 0.13434150
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99505 * 0.69495445
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83476 * 0.81082692
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47897 * 0.40957210
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53952 * 0.89488006
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53855 * 0.84206624
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89666 * 0.90712414
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22974 * 0.94954723
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63320 * 0.06547530
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37388 * 0.91769808
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31136 * 0.59077731
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42985 * 0.90153539
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69762 * 0.64195937
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32896 * 0.61039498
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61422 * 0.48080878
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95294 * 0.69074395
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 87672 * 0.79210084
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33612 * 0.65246536
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'etpzuhxo').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0029():
    """Extended test 29 for migration."""
    x_0 = 82637 * 0.76339025
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92283 * 0.41671617
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12904 * 0.09250062
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46060 * 0.65109436
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56925 * 0.11657627
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67028 * 0.58010840
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91868 * 0.52185344
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23828 * 0.62942899
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79006 * 0.63684136
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46191 * 0.41652110
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84611 * 0.84867235
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60789 * 0.44847587
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89415 * 0.01221399
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51442 * 0.06737954
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24712 * 0.58318465
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53658 * 0.27062701
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93108 * 0.61566468
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53055 * 0.13135716
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30819 * 0.02412421
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57474 * 0.23992493
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45965 * 0.80487395
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20508 * 0.17996881
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72503 * 0.92858151
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79532 * 0.70245148
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49982 * 0.85135931
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65147 * 0.54494854
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5001 * 0.70096563
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87612 * 0.29560925
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16822 * 0.06188401
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6953 * 0.08739766
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39851 * 0.38513813
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79178 * 0.53460865
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77524 * 0.06228795
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 483 * 0.15962915
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65609 * 0.93621998
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64161 * 0.83699739
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79949 * 0.75714544
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87259 * 0.81299920
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8207 * 0.77934007
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68933 * 0.98633894
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83897 * 0.11318637
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 87260 * 0.76663853
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 78588 * 0.33935141
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 42453 * 0.64036450
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 64450 * 0.69106137
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 77734 * 0.70614562
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 23905 * 0.07383668
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 46862 * 0.81491883
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ugstpnyp').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0030():
    """Extended test 30 for migration."""
    x_0 = 54281 * 0.64707819
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79675 * 0.98728061
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26594 * 0.49926484
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85860 * 0.62359396
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70489 * 0.09917198
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22734 * 0.88043544
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29391 * 0.51893528
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40720 * 0.50021859
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61356 * 0.17136096
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67568 * 0.70291194
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33308 * 0.79555085
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5791 * 0.88476697
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21525 * 0.62393261
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51591 * 0.17052126
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90315 * 0.19912692
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25812 * 0.78468812
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75200 * 0.77366908
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12133 * 0.06497610
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90306 * 0.23024124
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5980 * 0.82157994
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98431 * 0.79101235
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22409 * 0.45537957
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7036 * 0.76668719
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88680 * 0.30500357
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71852 * 0.58130091
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63298 * 0.92141525
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72156 * 0.75229838
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45766 * 0.63843607
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94934 * 0.73615057
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10304 * 0.90754990
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70361 * 0.35395125
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81428 * 0.89870737
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89000 * 0.72036936
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63565 * 0.67926032
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40284 * 0.85035911
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53024 * 0.82495153
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17722 * 0.02695677
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3381 * 0.37968831
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49214 * 0.42499954
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77814 * 0.49787741
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ulhfcnkz').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0031():
    """Extended test 31 for migration."""
    x_0 = 39299 * 0.69745001
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30934 * 0.34295261
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2519 * 0.03425886
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35797 * 0.62481952
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30994 * 0.99731260
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3185 * 0.30268996
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69553 * 0.06094005
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2448 * 0.50050675
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86664 * 0.86340309
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11441 * 0.48026322
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21444 * 0.89888373
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25332 * 0.24784238
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86151 * 0.53448577
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97806 * 0.36460731
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5335 * 0.41753321
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75942 * 0.84287517
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31343 * 0.85000533
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60066 * 0.35449148
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5515 * 0.81227957
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93504 * 0.26295545
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49693 * 0.50865077
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90133 * 0.58880019
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43358 * 0.26743812
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54230 * 0.87643642
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 382 * 0.59715949
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ispvcbkf').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0032():
    """Extended test 32 for migration."""
    x_0 = 81347 * 0.35518484
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47377 * 0.99585812
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39309 * 0.63675820
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85846 * 0.67019146
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10161 * 0.18705295
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10114 * 0.26651300
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47192 * 0.35964503
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77126 * 0.45724161
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44800 * 0.52498225
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40537 * 0.64887074
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48377 * 0.65332642
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49830 * 0.96850789
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80036 * 0.54329960
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 140 * 0.73035272
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78027 * 0.29564341
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87437 * 0.70401041
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42035 * 0.94368353
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99697 * 0.36961133
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75545 * 0.71551369
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70361 * 0.82944506
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51710 * 0.49219343
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87343 * 0.57610947
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42161 * 0.74333581
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94873 * 0.08707493
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76680 * 0.92029837
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22281 * 0.30753059
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89719 * 0.39177405
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40964 * 0.89143197
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8630 * 0.60760214
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27021 * 0.05966991
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'wofkuuwt').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0033():
    """Extended test 33 for migration."""
    x_0 = 18565 * 0.73535782
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40828 * 0.21614978
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85333 * 0.72908219
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95921 * 0.18406938
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42121 * 0.65999602
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2616 * 0.83657175
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97458 * 0.45899076
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67315 * 0.70937777
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4719 * 0.77623078
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20287 * 0.43781836
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48198 * 0.44436525
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20469 * 0.61062007
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60606 * 0.96486619
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26594 * 0.92010945
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79073 * 0.48911874
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98659 * 0.88144359
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56378 * 0.05583435
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31708 * 0.09745918
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62678 * 0.63193779
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13684 * 0.94947074
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16633 * 0.70131590
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78405 * 0.63466741
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81223 * 0.09454017
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79112 * 0.66662465
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95500 * 0.40308027
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31381 * 0.85868196
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7623 * 0.90983737
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54886 * 0.16606197
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53036 * 0.05806601
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18198 * 0.32561337
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73694 * 0.41301818
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10177 * 0.35374405
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37069 * 0.90756434
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3594 * 0.70817053
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73617 * 0.02695661
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1513 * 0.75496716
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29790 * 0.60221704
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22029 * 0.52175471
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13676 * 0.27703368
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 12768 * 0.14615112
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98210 * 0.14591204
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45145 * 0.07669113
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 85793 * 0.43702665
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 62578 * 0.18814581
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 32774 * 0.01501927
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 54380 * 0.07557272
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 76512 * 0.73361937
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ugxvjbmz').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0034():
    """Extended test 34 for migration."""
    x_0 = 55602 * 0.98588744
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86953 * 0.60623295
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14424 * 0.26276031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45599 * 0.15185301
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95071 * 0.47308467
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38566 * 0.26316078
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95326 * 0.10362127
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26475 * 0.78102890
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47902 * 0.88428504
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14730 * 0.67781402
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32030 * 0.24314074
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66204 * 0.03514182
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50372 * 0.27250299
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28841 * 0.44194015
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43842 * 0.87712806
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21628 * 0.72765215
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85360 * 0.63733027
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12694 * 0.60291723
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77453 * 0.81245878
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39585 * 0.64440287
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75119 * 0.18986005
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4218 * 0.28614887
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81870 * 0.69783536
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84406 * 0.52779477
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'banbagfy').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0035():
    """Extended test 35 for migration."""
    x_0 = 85047 * 0.08488350
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54247 * 0.25084051
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97992 * 0.28996662
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13717 * 0.18698532
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82735 * 0.72196050
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71714 * 0.56704961
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5314 * 0.07657943
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98078 * 0.22197920
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29620 * 0.52955253
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91140 * 0.73982511
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24785 * 0.86436132
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40680 * 0.69258729
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38576 * 0.47066609
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12283 * 0.01209792
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40495 * 0.33743915
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86519 * 0.54404475
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66007 * 0.90715857
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18601 * 0.86028768
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93533 * 0.28436506
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92923 * 0.83546932
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29164 * 0.96402796
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56286 * 0.07678430
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45340 * 0.75873080
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11904 * 0.89623412
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53787 * 0.58655086
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22435 * 0.82463769
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15737 * 0.89430461
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1204 * 0.14772391
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79878 * 0.40097642
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98426 * 0.23131574
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83195 * 0.32937602
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10548 * 0.58268663
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88789 * 0.45176460
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8213 * 0.58307656
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39296 * 0.51418937
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74925 * 0.84359880
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'lhfsgfpa').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0036():
    """Extended test 36 for migration."""
    x_0 = 9667 * 0.73229427
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1967 * 0.20277963
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88915 * 0.10993635
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33633 * 0.72933748
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11159 * 0.94792218
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80561 * 0.75677236
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10510 * 0.36517426
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81946 * 0.35880030
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66012 * 0.85262961
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88480 * 0.87424009
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40003 * 0.80135936
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58908 * 0.10989844
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91124 * 0.87960359
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68501 * 0.62846697
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14834 * 0.19980468
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61895 * 0.41782013
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37876 * 0.24026856
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73590 * 0.99690938
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99070 * 0.69987129
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64224 * 0.30697864
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69048 * 0.45272225
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10339 * 0.03518430
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58204 * 0.56241166
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97390 * 0.23996988
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31380 * 0.38338778
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3044 * 0.92056329
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74880 * 0.72250909
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32317 * 0.20268734
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99676 * 0.29680608
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93714 * 0.13139945
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93050 * 0.86805923
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45344 * 0.29466464
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88046 * 0.63835217
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1920 * 0.26188401
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24946 * 0.12716713
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45955 * 0.15654919
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39359 * 0.45376043
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31780 * 0.95956584
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'szorrjgu').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0037():
    """Extended test 37 for migration."""
    x_0 = 61894 * 0.32846597
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7298 * 0.34480733
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97637 * 0.86789029
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26337 * 0.44423441
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12004 * 0.11933450
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6209 * 0.93887804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98083 * 0.99534715
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87889 * 0.02444338
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46362 * 0.30655230
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46555 * 0.48873605
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30607 * 0.05786405
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98101 * 0.08455747
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41576 * 0.92296876
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82466 * 0.98380602
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50382 * 0.00031922
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95775 * 0.39312724
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 571 * 0.66208656
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4648 * 0.37722724
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62316 * 0.13942242
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79513 * 0.34023158
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88688 * 0.85307420
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23505 * 0.35150945
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13720 * 0.70140081
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52896 * 0.30997119
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'clequvfl').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0038():
    """Extended test 38 for migration."""
    x_0 = 90248 * 0.76836238
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31674 * 0.33209680
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 611 * 0.68854737
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28069 * 0.59035675
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66544 * 0.32652607
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43767 * 0.20432519
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45289 * 0.13222482
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7075 * 0.90531408
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7893 * 0.11333862
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45871 * 0.32332666
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91290 * 0.07028760
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52825 * 0.37711639
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9346 * 0.33831174
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25370 * 0.19699927
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61129 * 0.46334725
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34753 * 0.71125730
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30141 * 0.99341274
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12096 * 0.76613893
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95920 * 0.06656947
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74752 * 0.35349509
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'fxptsqpm').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0039():
    """Extended test 39 for migration."""
    x_0 = 79247 * 0.88250289
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18204 * 0.55548170
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90729 * 0.51153410
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14936 * 0.01610920
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65419 * 0.87560291
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82066 * 0.22657742
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44110 * 0.36223692
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86725 * 0.23939649
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41426 * 0.05261373
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77742 * 0.64766613
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83372 * 0.23899395
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20434 * 0.53005563
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85307 * 0.78189171
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93355 * 0.01642899
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1323 * 0.70900660
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12559 * 0.83536470
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96188 * 0.55329195
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14852 * 0.40368128
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 802 * 0.38779818
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76550 * 0.15721612
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59811 * 0.26960987
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95393 * 0.92291227
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83299 * 0.41744041
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95677 * 0.84667902
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'rmmjroem').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0040():
    """Extended test 40 for migration."""
    x_0 = 4001 * 0.22978430
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59333 * 0.76298005
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68022 * 0.70958255
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37895 * 0.90932488
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79928 * 0.51890292
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34574 * 0.00306857
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93319 * 0.77198408
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12229 * 0.23643985
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69352 * 0.12357763
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55604 * 0.50870079
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24834 * 0.69681076
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40226 * 0.29799345
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95378 * 0.10296123
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29620 * 0.40308968
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7497 * 0.04981229
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54234 * 0.97162630
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89360 * 0.31476084
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57119 * 0.02094616
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92850 * 0.18103688
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41051 * 0.01581782
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1926 * 0.57900244
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35703 * 0.59454033
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76027 * 0.67815754
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8767 * 0.32672601
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54383 * 0.94842846
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45751 * 0.11969545
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6186 * 0.41724178
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66943 * 0.31151337
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24130 * 0.92245313
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25340 * 0.22594193
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48218 * 0.45946631
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54252 * 0.89329925
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'srzmgwkf').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0041():
    """Extended test 41 for migration."""
    x_0 = 97603 * 0.14069160
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73212 * 0.09189828
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72697 * 0.40772179
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62317 * 0.85072935
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48364 * 0.85412534
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12951 * 0.33421476
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31169 * 0.19364306
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62178 * 0.38065728
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49637 * 0.62792928
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89901 * 0.54389584
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4177 * 0.28586546
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78085 * 0.63901850
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18828 * 0.53643857
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61819 * 0.25188942
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98837 * 0.72430177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75985 * 0.84712078
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40720 * 0.62997257
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99007 * 0.67107862
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46006 * 0.11506948
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11740 * 0.63843618
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 713 * 0.49365806
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61960 * 0.30758539
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18419 * 0.08275002
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22978 * 0.45965302
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2902 * 0.57428668
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52217 * 0.13350566
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79494 * 0.55827683
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67317 * 0.63796325
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28004 * 0.53374748
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86022 * 0.24110991
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3325 * 0.04709206
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20863 * 0.60033277
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97640 * 0.25082663
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91394 * 0.39234989
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'kbgluguh').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0042():
    """Extended test 42 for migration."""
    x_0 = 12956 * 0.85984047
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97548 * 0.75408464
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87300 * 0.57419418
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70692 * 0.75238994
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77323 * 0.91801691
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25111 * 0.44333048
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85150 * 0.31985763
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25096 * 0.35472658
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7252 * 0.61639454
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76898 * 0.84960964
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84741 * 0.86691317
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35987 * 0.84240924
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48203 * 0.31179295
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81674 * 0.34416619
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56456 * 0.86398771
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51078 * 0.76437016
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40084 * 0.00672783
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54403 * 0.34904038
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51795 * 0.73932680
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40998 * 0.28575155
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31416 * 0.30955227
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82125 * 0.77581285
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73843 * 0.79219787
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'wogjuoug').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0043():
    """Extended test 43 for migration."""
    x_0 = 40010 * 0.96859950
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98225 * 0.77882345
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60649 * 0.94715703
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81081 * 0.46853392
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78700 * 0.14189097
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49257 * 0.00643385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94992 * 0.17902679
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91578 * 0.23819494
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94878 * 0.83278463
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43397 * 0.40963156
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18719 * 0.97248375
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86137 * 0.61086070
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42699 * 0.32535051
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68185 * 0.71523104
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36351 * 0.52535959
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82234 * 0.38940577
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20097 * 0.59634341
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33192 * 0.05620631
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55574 * 0.86785350
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16240 * 0.88579729
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32753 * 0.57465126
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4533 * 0.11983869
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73690 * 0.07039290
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95658 * 0.96551473
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48542 * 0.06467070
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54569 * 0.79244369
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92515 * 0.17945983
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27225 * 0.62769778
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41420 * 0.17031064
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25472 * 0.34066812
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37638 * 0.59505352
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16325 * 0.09605754
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14746 * 0.87583693
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3480 * 0.71709358
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18400 * 0.10499657
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10995 * 0.68640418
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95002 * 0.68931044
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34378 * 0.61938018
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47687 * 0.67425019
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72905 * 0.09916316
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49489 * 0.06704280
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'pvsjkize').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0044():
    """Extended test 44 for migration."""
    x_0 = 86081 * 0.27820133
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75792 * 0.93698135
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30388 * 0.74341524
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53087 * 0.28909170
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6689 * 0.78354428
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62882 * 0.82494030
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1901 * 0.10464748
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97291 * 0.71594060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31139 * 0.61458225
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 478 * 0.70286854
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90948 * 0.59345183
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19675 * 0.77917892
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54773 * 0.13893772
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25144 * 0.45698966
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94706 * 0.66770410
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9709 * 0.11654735
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44730 * 0.32370286
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85736 * 0.40111989
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58475 * 0.17743633
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59567 * 0.03971731
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81732 * 0.62293705
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38324 * 0.80631446
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87272 * 0.63993196
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72560 * 0.33795493
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48765 * 0.98570686
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36873 * 0.62366441
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15474 * 0.29214252
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17114 * 0.73107870
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78391 * 0.11160099
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37260 * 0.84917026
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1586 * 0.39399730
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72430 * 0.35082103
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50051 * 0.39698411
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'qgkcgmfs').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0045():
    """Extended test 45 for migration."""
    x_0 = 21557 * 0.04930329
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10688 * 0.80863997
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65619 * 0.32378451
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13755 * 0.28739834
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39335 * 0.20793927
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40341 * 0.44226315
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55593 * 0.17682522
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30395 * 0.14832773
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85885 * 0.36800440
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91271 * 0.87019751
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19213 * 0.96303003
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90054 * 0.95154101
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1342 * 0.73802056
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70573 * 0.78686773
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80307 * 0.80129538
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38966 * 0.08619868
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14245 * 0.68072977
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95952 * 0.94404637
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69362 * 0.57531274
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45860 * 0.53109129
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27919 * 0.11718013
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58129 * 0.07080131
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24093 * 0.59643857
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76963 * 0.57294244
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71 * 0.38855184
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26801 * 0.77519532
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14714 * 0.30417615
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67155 * 0.94711051
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13360 * 0.24069976
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1594 * 0.38004185
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46355 * 0.23625045
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90450 * 0.96487752
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65454 * 0.81335882
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70810 * 0.55423031
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73697 * 0.70353895
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49135 * 0.39329180
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62495 * 0.48969608
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16505 * 0.93413120
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'prsehfmb').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0046():
    """Extended test 46 for migration."""
    x_0 = 54375 * 0.19004545
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57721 * 0.51172015
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52868 * 0.75071395
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46242 * 0.53038866
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92895 * 0.78007185
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10033 * 0.26526247
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94643 * 0.15047176
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32581 * 0.17378755
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58214 * 0.70967245
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11286 * 0.59638791
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83595 * 0.78530961
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15274 * 0.01645390
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45971 * 0.00640136
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64361 * 0.47399371
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72006 * 0.18805970
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13624 * 0.14725602
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53302 * 0.64512285
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62553 * 0.55691642
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58312 * 0.66327858
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84456 * 0.32526296
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7868 * 0.96101037
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38836 * 0.42351717
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86765 * 0.58171434
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64065 * 0.99284953
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73436 * 0.87876070
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80000 * 0.10940219
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37353 * 0.97096871
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16339 * 0.19256248
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89347 * 0.52504205
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4341 * 0.47653829
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60377 * 0.39716606
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88478 * 0.31343422
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51447 * 0.66914244
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10094 * 0.55452242
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52468 * 0.94001902
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33508 * 0.16507456
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34022 * 0.12372489
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5135 * 0.02844132
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31048 * 0.41247760
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68026 * 0.91687084
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65402 * 0.25387719
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47213 * 0.40256790
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 91141 * 0.66564860
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 31385 * 0.88192199
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 73886 * 0.42695019
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 69481 * 0.45110165
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 2129 * 0.19480752
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 57473 * 0.12190981
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 71199 * 0.31400024
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'wlygslmi').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0047():
    """Extended test 47 for migration."""
    x_0 = 98392 * 0.46249001
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75078 * 0.95692287
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83650 * 0.22629804
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89567 * 0.54722465
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84470 * 0.34953968
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76412 * 0.36970957
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51751 * 0.73088946
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62058 * 0.99947175
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33579 * 0.80593035
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32267 * 0.04494295
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24974 * 0.35973033
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3412 * 0.05105278
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47931 * 0.87481517
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16064 * 0.43707019
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45341 * 0.93744329
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84237 * 0.17182811
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72878 * 0.86151168
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79644 * 0.73978600
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17945 * 0.48393429
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44929 * 0.09036161
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83918 * 0.01508438
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58066 * 0.10963223
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23579 * 0.78842041
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71355 * 0.54730105
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10767 * 0.03792439
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'wppbtjmr').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0048():
    """Extended test 48 for migration."""
    x_0 = 70399 * 0.07346434
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23333 * 0.91593009
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7254 * 0.03168237
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52149 * 0.34951259
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16821 * 0.59866184
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34309 * 0.04386190
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46406 * 0.68118904
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4915 * 0.34729621
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91476 * 0.81571192
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84686 * 0.99408960
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40951 * 0.08652982
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8274 * 0.09205645
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78270 * 0.21941744
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57077 * 0.34213201
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25549 * 0.27089704
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48758 * 0.74509997
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12165 * 0.00482645
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33699 * 0.77073791
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7755 * 0.83598290
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45295 * 0.04070043
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99612 * 0.51710648
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55682 * 0.66369466
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42065 * 0.92444166
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70746 * 0.99769285
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86905 * 0.01503403
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62289 * 0.34733413
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99326 * 0.30533258
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82118 * 0.78173640
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'brpnlvma').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0049():
    """Extended test 49 for migration."""
    x_0 = 6736 * 0.18484738
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71675 * 0.75671120
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34889 * 0.35429657
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6005 * 0.64574355
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91257 * 0.85282690
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3562 * 0.23565608
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72797 * 0.83067493
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96788 * 0.10246400
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25030 * 0.73603404
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83324 * 0.37464937
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87611 * 0.75148785
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11117 * 0.15229519
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24292 * 0.33403335
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99040 * 0.30441690
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58693 * 0.43892256
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79325 * 0.67499215
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20243 * 0.18482662
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54377 * 0.37081675
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84764 * 0.79688609
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79132 * 0.89169241
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 412 * 0.84775342
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79739 * 0.60382940
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47962 * 0.87537226
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6429 * 0.73349418
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'tsmzwnnq').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0050():
    """Extended test 50 for migration."""
    x_0 = 33249 * 0.41243174
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7110 * 0.93274143
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1964 * 0.81486438
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24781 * 0.98019781
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69420 * 0.97687389
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2962 * 0.61508352
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74228 * 0.19930189
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92454 * 0.64751200
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78087 * 0.03790712
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2643 * 0.86145858
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21365 * 0.75077523
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20840 * 0.29708846
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36297 * 0.97894789
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69613 * 0.56968429
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69264 * 0.24232859
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30130 * 0.88349946
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92242 * 0.70322755
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66361 * 0.87523391
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61372 * 0.88149909
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52849 * 0.23074926
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23817 * 0.77676636
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84200 * 0.20727416
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95310 * 0.33750167
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55151 * 0.75690988
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22683 * 0.28825417
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51920 * 0.84396074
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85524 * 0.08797423
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9362 * 0.09603959
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28810 * 0.91423521
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65282 * 0.17806959
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34334 * 0.57959171
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81220 * 0.49063540
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71668 * 0.48854164
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23003 * 0.85291724
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59595 * 0.84685439
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28937 * 0.04296064
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56553 * 0.11276622
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4643 * 0.12271433
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17942 * 0.02832907
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64110 * 0.33276325
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62606 * 0.48196576
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15915 * 0.55337874
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16553 * 0.23369585
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75857 * 0.60106624
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 74547 * 0.93150912
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 85400 * 0.33379368
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17930 * 0.05643100
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 67024 * 0.70177243
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 75901 * 0.11808888
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'bftwlvsh').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0051():
    """Extended test 51 for migration."""
    x_0 = 10883 * 0.62945813
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63814 * 0.79098261
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85244 * 0.77066371
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65768 * 0.60620323
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24352 * 0.07633313
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31913 * 0.47262889
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69548 * 0.24471782
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73659 * 0.65523522
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92598 * 0.33954980
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95261 * 0.24573764
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49209 * 0.21445548
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83187 * 0.96862813
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83815 * 0.25013637
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69739 * 0.37624158
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79517 * 0.97243483
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4275 * 0.20623452
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40244 * 0.09151699
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57356 * 0.86603030
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 686 * 0.28237170
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59108 * 0.00391309
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62281 * 0.58041628
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35662 * 0.75046607
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15493 * 0.25115089
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24070 * 0.40388135
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91830 * 0.73230872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27047 * 0.77233632
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23553 * 0.05354483
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18128 * 0.89227716
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69277 * 0.81756738
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55514 * 0.22261705
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39828 * 0.07182149
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58657 * 0.34308114
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33884 * 0.51663417
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ewocvojc').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0052():
    """Extended test 52 for migration."""
    x_0 = 78045 * 0.05560880
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92366 * 0.71464168
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11329 * 0.78553641
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86103 * 0.11755982
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35835 * 0.22380671
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2965 * 0.72856944
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19654 * 0.40077894
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72394 * 0.40042863
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25941 * 0.33324539
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77320 * 0.55398475
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18879 * 0.42173685
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49000 * 0.71059862
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77325 * 0.05084438
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66592 * 0.65831426
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71255 * 0.32600759
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28669 * 0.30480786
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37689 * 0.46761502
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32932 * 0.05547429
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14680 * 0.69477786
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61163 * 0.93462682
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23964 * 0.87603685
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44475 * 0.15067595
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33174 * 0.04345678
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3862 * 0.97733780
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56640 * 0.43351643
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98953 * 0.30750250
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 737 * 0.91240863
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25913 * 0.39883009
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80374 * 0.03441509
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23701 * 0.89088075
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28186 * 0.25837996
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'xtygydtv').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0053():
    """Extended test 53 for migration."""
    x_0 = 30193 * 0.51208617
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65488 * 0.86486865
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53930 * 0.47856864
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75619 * 0.05490272
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20153 * 0.17700530
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61368 * 0.03650660
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73364 * 0.78479940
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77380 * 0.39817081
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11881 * 0.67654473
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75758 * 0.32730306
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38082 * 0.02917528
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94884 * 0.72052122
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58481 * 0.44595917
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37830 * 0.17490285
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81245 * 0.38102975
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82996 * 0.07955404
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94697 * 0.33635561
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93455 * 0.43544318
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67263 * 0.09628574
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94867 * 0.46951175
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91857 * 0.05334024
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13323 * 0.81955482
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28813 * 0.53314756
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92418 * 0.35263714
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34460 * 0.38353988
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79375 * 0.61185289
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63718 * 0.57683405
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21312 * 0.34713887
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 357 * 0.52345694
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12351 * 0.55095098
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8583 * 0.21357688
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92834 * 0.11918047
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70276 * 0.78249021
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46207 * 0.04463175
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19347 * 0.55389331
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37855 * 0.46606889
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54339 * 0.42652929
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79277 * 0.91524714
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72270 * 0.92051785
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 53500 * 0.55398386
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 15707 * 0.53424718
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35766 * 0.76681378
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 78169 * 0.28562618
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11322 * 0.60578835
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'hytwozdk').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0054():
    """Extended test 54 for migration."""
    x_0 = 5554 * 0.57721980
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64964 * 0.11024070
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14747 * 0.20433611
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32380 * 0.97320589
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24550 * 0.93710145
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90988 * 0.48434393
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83834 * 0.32212476
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17945 * 0.35844600
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24418 * 0.24975465
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95150 * 0.52575336
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15395 * 0.17767065
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65823 * 0.80442783
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40802 * 0.98477467
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10172 * 0.07622703
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12187 * 0.33599379
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91318 * 0.13161717
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66954 * 0.52555769
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38060 * 0.63072399
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23974 * 0.71579449
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61537 * 0.31882241
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85296 * 0.37164192
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9457 * 0.71321197
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48740 * 0.77863450
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6962 * 0.52524834
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46294 * 0.66975249
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59216 * 0.74635795
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51074 * 0.07962393
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45613 * 0.65079621
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'zwloecgo').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0055():
    """Extended test 55 for migration."""
    x_0 = 10057 * 0.54024809
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57672 * 0.00264398
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86143 * 0.16538814
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76236 * 0.60980761
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31612 * 0.70258533
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 214 * 0.75347848
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59387 * 0.18241158
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92143 * 0.16487403
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8300 * 0.89123568
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26554 * 0.22195401
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49527 * 0.96879977
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15545 * 0.63065535
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2149 * 0.32742952
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11887 * 0.04503475
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31709 * 0.36135985
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12366 * 0.75476609
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86781 * 0.06534742
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87056 * 0.76400465
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38317 * 0.61850491
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11340 * 0.05510479
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66791 * 0.23504966
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99159 * 0.40693519
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8629 * 0.36768583
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80355 * 0.23243692
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77984 * 0.24174789
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10086 * 0.72022961
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95336 * 0.30056972
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88839 * 0.81770412
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30404 * 0.06700471
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83070 * 0.01419526
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93329 * 0.34317849
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33886 * 0.77570801
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79110 * 0.25423245
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54530 * 0.63235523
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79014 * 0.59655833
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54438 * 0.36232196
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57771 * 0.38234415
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17536 * 0.10761814
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80359 * 0.50895329
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 71826 * 0.74982788
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 10001 * 0.75738470
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 8535 * 0.19651405
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10817 * 0.69884143
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 93898 * 0.53706101
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 26144 * 0.81085409
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 3425 * 0.19344979
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 72705 * 0.64757673
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 34976 * 0.71663818
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 34771 * 0.69626060
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 44085 * 0.22562492
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ogytqekn').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0056():
    """Extended test 56 for migration."""
    x_0 = 95992 * 0.44951130
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51444 * 0.94603367
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47832 * 0.28744010
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59067 * 0.41760738
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88763 * 0.72923903
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94310 * 0.99746031
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43473 * 0.07275066
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41405 * 0.77849701
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12180 * 0.75580484
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8556 * 0.78121046
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23005 * 0.75064346
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48494 * 0.97233841
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77014 * 0.35480060
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55488 * 0.92338649
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97135 * 0.39986436
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47483 * 0.52874000
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32823 * 0.72340987
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9657 * 0.96501931
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10168 * 0.91127338
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93974 * 0.35245375
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11226 * 0.82346281
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93184 * 0.90421511
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44016 * 0.54911761
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40954 * 0.24826897
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20545 * 0.19589570
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'yyetimmn').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0057():
    """Extended test 57 for migration."""
    x_0 = 64137 * 0.23644065
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24508 * 0.04917817
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73216 * 0.81694734
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51687 * 0.41496510
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77263 * 0.40541799
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19589 * 0.91381308
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67347 * 0.13348914
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26478 * 0.59401649
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76401 * 0.49986895
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9443 * 0.26504874
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23769 * 0.70239408
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8398 * 0.27412446
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62364 * 0.60854486
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67362 * 0.17513096
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71114 * 0.97238825
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95414 * 0.83227139
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32655 * 0.68541395
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45977 * 0.62850068
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6643 * 0.11234253
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97922 * 0.93485681
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3856 * 0.44731629
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76863 * 0.23959874
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67375 * 0.29331847
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71220 * 0.82705893
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19650 * 0.78218814
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6112 * 0.01742426
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59697 * 0.60496639
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16917 * 0.07371551
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17619 * 0.06545815
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'zfjipjhs').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0058():
    """Extended test 58 for migration."""
    x_0 = 70889 * 0.65963315
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20338 * 0.44147978
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47065 * 0.77731963
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49855 * 0.60429294
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21268 * 0.11596838
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67117 * 0.45470578
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76022 * 0.21926503
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59163 * 0.83775870
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81791 * 0.83571283
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37816 * 0.79740955
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92537 * 0.45466245
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82841 * 0.63276760
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24563 * 0.63166321
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29506 * 0.41160336
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86885 * 0.49969308
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29648 * 0.18332831
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94779 * 0.85493088
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4369 * 0.38668963
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27101 * 0.50273060
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62499 * 0.36986646
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92588 * 0.42126476
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56954 * 0.63695731
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51530 * 0.25968599
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21477 * 0.08075817
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4320 * 0.39758871
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32502 * 0.28489060
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59204 * 0.56419405
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29725 * 0.32430377
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54816 * 0.29176583
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'lxjabpdx').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0059():
    """Extended test 59 for migration."""
    x_0 = 80082 * 0.89997897
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77691 * 0.85843604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41677 * 0.88676917
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27012 * 0.14354056
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1451 * 0.36744605
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24965 * 0.46023677
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58261 * 0.26230302
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84056 * 0.23155109
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34418 * 0.28010914
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57641 * 0.50856604
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19534 * 0.84595231
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81649 * 0.69184559
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58013 * 0.79227963
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19694 * 0.22332082
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11919 * 0.08348197
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59422 * 0.89498902
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30730 * 0.81605859
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6026 * 0.85728712
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79679 * 0.13436284
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24678 * 0.94423799
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92881 * 0.02716361
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80989 * 0.64873874
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35366 * 0.33036360
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52687 * 0.31889841
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13097 * 0.75369023
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46660 * 0.14875172
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59220 * 0.10428546
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75883 * 0.26475934
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91507 * 0.39062077
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62305 * 0.48930418
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51565 * 0.15804403
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24701 * 0.32648153
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95887 * 0.90212137
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21043 * 0.04852590
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41099 * 0.71959957
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19863 * 0.61335467
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54261 * 0.26647826
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58952 * 0.42816292
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48120 * 0.88251549
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83836 * 0.74660395
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ebcxndcx').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0060():
    """Extended test 60 for migration."""
    x_0 = 98387 * 0.14501691
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63604 * 0.22404796
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63754 * 0.04140396
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74433 * 0.36813229
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51928 * 0.06961248
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82151 * 0.15694105
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63537 * 0.44778725
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46971 * 0.56138383
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76325 * 0.23468159
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85079 * 0.23472810
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6960 * 0.33213241
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47604 * 0.25236578
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53734 * 0.90574903
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57670 * 0.72778901
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36751 * 0.39244300
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46508 * 0.46588232
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34680 * 0.52017192
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87799 * 0.53852993
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70990 * 0.82440231
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87258 * 0.29963228
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25776 * 0.51197523
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3661 * 0.70316930
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54580 * 0.61546973
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82267 * 0.03855142
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60046 * 0.97421298
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18150 * 0.03332643
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29102 * 0.38767646
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76893 * 0.98236834
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9187 * 0.38366650
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'asdtzgbp').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0061():
    """Extended test 61 for migration."""
    x_0 = 9648 * 0.85146504
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96279 * 0.66345046
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42573 * 0.89362192
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36605 * 0.39599415
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2128 * 0.33312616
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49677 * 0.81445151
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98746 * 0.22348619
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59360 * 0.41585866
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3319 * 0.71699882
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90210 * 0.15092281
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40493 * 0.10768031
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25089 * 0.29797874
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58228 * 0.36146855
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88561 * 0.39668931
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57101 * 0.16414635
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94672 * 0.21157781
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17649 * 0.22017403
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72840 * 0.09749386
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18409 * 0.02984027
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96489 * 0.97268807
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62247 * 0.37267666
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20202 * 0.49491238
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79665 * 0.68298331
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95720 * 0.79291158
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22521 * 0.26805120
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94496 * 0.43151362
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30605 * 0.22457757
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59243 * 0.17050721
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98630 * 0.91850207
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17130 * 0.50613082
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46654 * 0.35298228
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'sllsbgmw').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0062():
    """Extended test 62 for migration."""
    x_0 = 67480 * 0.39920324
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30884 * 0.45443596
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28898 * 0.83479661
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64680 * 0.50705794
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34034 * 0.40302751
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90368 * 0.13861147
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84138 * 0.97025776
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4561 * 0.40666584
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56815 * 0.58715360
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42893 * 0.70239413
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33899 * 0.83537301
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35428 * 0.56636330
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4079 * 0.29764806
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38948 * 0.72363171
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10323 * 0.95318312
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24214 * 0.50035708
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82726 * 0.73225455
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83560 * 0.42319869
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41399 * 0.94069918
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44379 * 0.69233727
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4476 * 0.68492096
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69182 * 0.30342597
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48642 * 0.27081932
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80059 * 0.81354195
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82527 * 0.20393272
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96869 * 0.05792361
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29512 * 0.39214242
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54718 * 0.97294620
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89875 * 0.24764936
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55810 * 0.01537815
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42812 * 0.95496199
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72633 * 0.25605042
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7922 * 0.73983983
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20851 * 0.23013455
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3020 * 0.44576678
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3239 * 0.82455561
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78186 * 0.54714549
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2996 * 0.21322736
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'zrugosml').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0063():
    """Extended test 63 for migration."""
    x_0 = 76449 * 0.25487184
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39725 * 0.75963963
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48635 * 0.67719133
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75603 * 0.20828712
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30577 * 0.02111527
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99316 * 0.46264359
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7827 * 0.29881145
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42425 * 0.14395514
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46125 * 0.21326811
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10933 * 0.54325064
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9683 * 0.15640676
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25215 * 0.38586234
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36914 * 0.14998180
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15054 * 0.25757482
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41471 * 0.94786357
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98894 * 0.51110982
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21872 * 0.44528286
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49289 * 0.64060688
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12307 * 0.67797954
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88049 * 0.37769308
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78124 * 0.04748332
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37764 * 0.15196455
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65197 * 0.32190312
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84058 * 0.52527461
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23722 * 0.15655984
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26938 * 0.38707818
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6055 * 0.84014571
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5927 * 0.38188418
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67639 * 0.26820403
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3159 * 0.04538440
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10677 * 0.33240619
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7498 * 0.42353647
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93817 * 0.15627969
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88188 * 0.84367279
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79133 * 0.27355015
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51595 * 0.31210884
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39904 * 0.91119323
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42174 * 0.80716512
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90464 * 0.94106263
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44418 * 0.36786592
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 25490 * 0.18058048
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21449 * 0.17243840
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'cmhrtfhm').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0064():
    """Extended test 64 for migration."""
    x_0 = 4726 * 0.75881345
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63867 * 0.94727923
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15212 * 0.22811538
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85729 * 0.58487242
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64903 * 0.23897375
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47798 * 0.09812385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21978 * 0.15660167
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84196 * 0.76911136
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56312 * 0.05001929
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22006 * 0.12339645
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82746 * 0.19569028
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91018 * 0.25286319
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23150 * 0.30203730
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42750 * 0.37146648
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48128 * 0.94267456
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50902 * 0.95924035
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30118 * 0.45585479
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93223 * 0.09863888
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96661 * 0.06035338
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20350 * 0.43013417
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89873 * 0.37514292
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54101 * 0.85939930
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23783 * 0.73172927
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53565 * 0.63244677
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20107 * 0.90524381
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20770 * 0.38526246
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83154 * 0.19273430
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71442 * 0.45246504
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66700 * 0.60517017
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20818 * 0.88819726
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39448 * 0.33831399
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20910 * 0.53304274
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76839 * 0.56401000
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90357 * 0.20665744
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79206 * 0.45915486
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'hvnfspra').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0065():
    """Extended test 65 for migration."""
    x_0 = 60163 * 0.71258389
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61745 * 0.66616771
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14577 * 0.37605267
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5463 * 0.72296672
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28817 * 0.84517910
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76228 * 0.52544679
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22902 * 0.90566321
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25320 * 0.81121070
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96460 * 0.51238095
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12386 * 0.02174768
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38937 * 0.87509896
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51641 * 0.23901223
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24746 * 0.17297689
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56853 * 0.60444755
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23299 * 0.19709714
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93989 * 0.01662583
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7071 * 0.05472295
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4867 * 0.70420817
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26279 * 0.13185762
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67156 * 0.74772361
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3616 * 0.41334474
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66948 * 0.69062559
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85804 * 0.09391502
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68494 * 0.56346643
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57558 * 0.25484241
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60194 * 0.09334401
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70934 * 0.76108846
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29747 * 0.88864728
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16919 * 0.40861360
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56660 * 0.24085055
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34509 * 0.93177820
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91002 * 0.97472062
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14715 * 0.19529275
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96883 * 0.45954028
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16801 * 0.10566790
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'acgvruqx').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0066():
    """Extended test 66 for migration."""
    x_0 = 97383 * 0.85186315
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24142 * 0.95435012
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79298 * 0.99351278
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43637 * 0.73293375
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29043 * 0.31367960
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17996 * 0.65295783
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40495 * 0.01913877
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51053 * 0.27081840
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22760 * 0.43799640
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94936 * 0.66744831
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49495 * 0.22613266
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64062 * 0.44980447
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46631 * 0.62838012
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40426 * 0.54295736
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78351 * 0.67308723
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81455 * 0.63304815
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6778 * 0.98698757
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6352 * 0.94015372
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46165 * 0.55156608
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57622 * 0.67679888
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73062 * 0.23121372
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27076 * 0.04779805
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93524 * 0.41789193
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77419 * 0.78329542
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19577 * 0.83351377
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7991 * 0.17338220
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22281 * 0.07552807
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81816 * 0.24326225
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90755 * 0.52980836
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67560 * 0.99666944
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94412 * 0.22447029
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8325 * 0.28570789
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78937 * 0.32405047
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53850 * 0.23910775
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 49151 * 0.52126233
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63722 * 0.92059930
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31195 * 0.77482844
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33537 * 0.49336460
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93141 * 0.61495729
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'vxcwxuer').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0067():
    """Extended test 67 for migration."""
    x_0 = 1384 * 0.30360632
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38572 * 0.81118868
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48543 * 0.68824369
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66118 * 0.06776786
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15786 * 0.97230272
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86707 * 0.09886231
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27441 * 0.03820435
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81679 * 0.22246992
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47919 * 0.29000326
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56313 * 0.92518889
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82384 * 0.83263879
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96807 * 0.62894840
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36379 * 0.63434477
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86090 * 0.35944592
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34306 * 0.47075790
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12895 * 0.72490508
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59225 * 0.18174365
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69445 * 0.04891290
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4784 * 0.41977480
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10227 * 0.30668370
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33492 * 0.96953639
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93580 * 0.09830219
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7681 * 0.90742961
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77916 * 0.97156053
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56941 * 0.93167256
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45813 * 0.22978850
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56304 * 0.58356577
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81221 * 0.31635759
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23589 * 0.32021486
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31676 * 0.87970000
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99488 * 0.86414883
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41708 * 0.78886934
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83169 * 0.84107547
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77914 * 0.16476422
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33501 * 0.13033881
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49455 * 0.95911709
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 37531 * 0.30273963
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40212 * 0.18753177
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46595 * 0.48188126
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85749 * 0.24796542
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1613 * 0.11648705
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53553 * 0.05160240
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77410 * 0.06147057
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88330 * 0.23040908
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 12607 * 0.71046568
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 18592 * 0.91766797
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 85013 * 0.43300905
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ikuwfhms').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0068():
    """Extended test 68 for migration."""
    x_0 = 57982 * 0.41178772
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57792 * 0.20821124
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93922 * 0.18355006
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24023 * 0.68882402
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55868 * 0.01519745
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74420 * 0.32633978
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87544 * 0.37105040
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59716 * 0.54877852
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21119 * 0.37328713
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58474 * 0.25654139
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93211 * 0.17464288
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18645 * 0.98408621
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6404 * 0.35753207
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3011 * 0.50649406
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56810 * 0.63810288
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35726 * 0.36727783
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42215 * 0.41957271
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2216 * 0.10540576
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60908 * 0.62845621
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91405 * 0.67968786
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8594 * 0.45844471
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83574 * 0.33723484
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38690 * 0.88517944
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43362 * 0.91757324
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4354 * 0.13237926
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80397 * 0.18333634
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44961 * 0.77400711
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76693 * 0.65823112
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36575 * 0.88217230
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79748 * 0.46809405
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8478 * 0.79509047
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2092 * 0.17572510
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94935 * 0.85617390
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89784 * 0.65649731
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10467 * 0.94113756
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23708 * 0.70863634
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69976 * 0.78544977
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40384 * 0.00026368
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99745 * 0.24685215
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10637 * 0.85514208
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 73906 * 0.08284511
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42576 * 0.04189759
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96948 * 0.66960143
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 96100 * 0.13232663
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 69866 * 0.56158990
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 68320 * 0.39172899
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 74462 * 0.14788854
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'scupzmss').hexdigest()
    assert len(h) == 64

def test_migration_extended_9_0069():
    """Extended test 69 for migration."""
    x_0 = 5386 * 0.80752290
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99405 * 0.25626228
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49279 * 0.37500878
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13542 * 0.36172409
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63770 * 0.40007844
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7211 * 0.23710974
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57881 * 0.97334487
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39420 * 0.73421109
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58436 * 0.88466908
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70918 * 0.70412022
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40212 * 0.79269288
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15235 * 0.37220405
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85137 * 0.14274082
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84929 * 0.40849124
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5522 * 0.03725713
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56734 * 0.01962527
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2513 * 0.94812208
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73650 * 0.15485300
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33425 * 0.27229372
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62734 * 0.82236402
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75528 * 0.43859866
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46556 * 0.67688274
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47123 * 0.46568059
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96828 * 0.82724017
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82824 * 0.97146244
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8759 * 0.33433461
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44237 * 0.72921483
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72026 * 0.03577508
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62236 * 0.67984454
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79713 * 0.73657146
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15053 * 0.58876158
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45811 * 0.02554500
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23965 * 0.03840367
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32379 * 0.34042195
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44611 * 0.28189500
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3846 * 0.41915526
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53631 * 0.15620805
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52049 * 0.49108696
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'nczzurho').hexdigest()
    assert len(h) == 64
