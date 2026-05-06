"""Extended tests for federation suite 0."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_federation_extended_0_0000():
    """Extended test 0 for federation."""
    x_0 = 67791 * 0.70918942
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71939 * 0.30848612
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84207 * 0.48501277
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35035 * 0.46862925
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55154 * 0.63138333
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46118 * 0.59735654
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83529 * 0.88730881
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32744 * 0.13984060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37568 * 0.29482152
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37240 * 0.09584498
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77630 * 0.89982293
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97070 * 0.65497812
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86621 * 0.84032870
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3207 * 0.73891476
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51669 * 0.03727978
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54064 * 0.33789673
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96386 * 0.66304070
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54194 * 0.21531333
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47909 * 0.35040013
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93123 * 0.31611122
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76021 * 0.47206643
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43113 * 0.24495394
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26111 * 0.27898691
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'xdppqzmr').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0001():
    """Extended test 1 for federation."""
    x_0 = 99641 * 0.82742043
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51042 * 0.38998762
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85657 * 0.22050031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80079 * 0.73580342
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53878 * 0.18943649
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84768 * 0.35314515
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92607 * 0.68438367
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75764 * 0.88990112
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46400 * 0.83421477
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66292 * 0.55752704
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51323 * 0.51168608
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58212 * 0.63489910
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22466 * 0.60637795
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19592 * 0.52930919
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45685 * 0.51125492
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11178 * 0.20965755
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81388 * 0.44227199
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57423 * 0.08576864
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76264 * 0.29189877
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32976 * 0.96399328
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6226 * 0.80053587
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28280 * 0.09324091
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62262 * 0.27714402
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50310 * 0.83848653
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8531 * 0.05369969
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7429 * 0.48965174
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99081 * 0.11632559
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75174 * 0.42966237
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25939 * 0.64600444
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45805 * 0.40248317
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 499 * 0.44963856
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97933 * 0.09712875
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41263 * 0.70087782
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80689 * 0.40470248
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71297 * 0.04220473
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21604 * 0.57148682
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30311 * 0.48349474
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69312 * 0.82820665
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 3535 * 0.60317645
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57965 * 0.31573255
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71046 * 0.17632854
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21666 * 0.22651159
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74080 * 0.68170381
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 41198 * 0.62100545
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 51939 * 0.84031906
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 43831 * 0.79472017
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 41815 * 0.22912411
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 76870 * 0.70263586
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 95765 * 0.43512166
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'lkpgrgax').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0002():
    """Extended test 2 for federation."""
    x_0 = 18679 * 0.68475077
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52883 * 0.64255484
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50655 * 0.92098131
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53754 * 0.64368405
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13790 * 0.65459459
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86638 * 0.54351709
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1016 * 0.30044555
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77105 * 0.18039786
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48936 * 0.06777065
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80328 * 0.82699634
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52056 * 0.43534709
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61377 * 0.74551160
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12985 * 0.91494772
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13903 * 0.38789278
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65230 * 0.62930522
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6612 * 0.51437373
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44219 * 0.11140002
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34169 * 0.79819118
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17046 * 0.71034330
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4033 * 0.52977748
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57849 * 0.30388723
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72534 * 0.94676010
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32862 * 0.94035220
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'aeakdhnz').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0003():
    """Extended test 3 for federation."""
    x_0 = 44013 * 0.77873977
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98803 * 0.59401273
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78880 * 0.35827546
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79567 * 0.05289118
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44208 * 0.92528725
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18450 * 0.66316909
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78202 * 0.32994406
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44321 * 0.89454378
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97193 * 0.21196093
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22414 * 0.63057264
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7313 * 0.83907887
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44333 * 0.89851810
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86080 * 0.46004119
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60804 * 0.34886225
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97066 * 0.67761253
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97200 * 0.49315336
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42167 * 0.03794703
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87188 * 0.21514289
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72442 * 0.62922115
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4518 * 0.94393844
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'rdympymn').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0004():
    """Extended test 4 for federation."""
    x_0 = 82060 * 0.91055624
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41067 * 0.44647436
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37624 * 0.72489892
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20022 * 0.25132182
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44835 * 0.59543639
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10524 * 0.14297084
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67497 * 0.77029107
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44395 * 0.03684321
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94175 * 0.96413523
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70360 * 0.59182172
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69402 * 0.52378633
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7869 * 0.30454793
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56744 * 0.23995214
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95643 * 0.44937408
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 441 * 0.57312805
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94163 * 0.15825660
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36151 * 0.52832288
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82565 * 0.60399087
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2587 * 0.21989750
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57650 * 0.31193804
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26162 * 0.16575959
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5725 * 0.22670719
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'roerocfh').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0005():
    """Extended test 5 for federation."""
    x_0 = 33235 * 0.73267060
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7252 * 0.25949528
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9537 * 0.25261471
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18046 * 0.91782064
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22159 * 0.54315473
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7923 * 0.52098933
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66598 * 0.09413837
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23290 * 0.95424348
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89995 * 0.89345055
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9909 * 0.08004922
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13918 * 0.96368716
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91929 * 0.02350677
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58092 * 0.38322543
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16173 * 0.84684395
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60274 * 0.64878173
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5627 * 0.49200358
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27566 * 0.87052245
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75529 * 0.86430410
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25062 * 0.02653978
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90673 * 0.16683058
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48866 * 0.55110347
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85092 * 0.14707932
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83140 * 0.50972984
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36345 * 0.94746092
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94646 * 0.16262270
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75920 * 0.69170864
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'xjiazwbg').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0006():
    """Extended test 6 for federation."""
    x_0 = 40171 * 0.57224309
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42936 * 0.79368475
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14701 * 0.10956988
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72388 * 0.39337449
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90984 * 0.10207208
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58675 * 0.50239263
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99312 * 0.62496110
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89354 * 0.31854896
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31314 * 0.69373152
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70170 * 0.80317929
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90481 * 0.46000722
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87543 * 0.40577319
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98695 * 0.65430203
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61640 * 0.83877895
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19841 * 0.83145318
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60351 * 0.75950186
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89286 * 0.50339578
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63797 * 0.00543395
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23352 * 0.09248101
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99746 * 0.82925867
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82730 * 0.83550460
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21272 * 0.73388007
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5567 * 0.52529860
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30586 * 0.57828929
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73952 * 0.32591835
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41242 * 0.68048315
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91107 * 0.85015764
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77003 * 0.60675055
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62979 * 0.01355550
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65147 * 0.35273510
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12961 * 0.23664485
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22617 * 0.72626512
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58275 * 0.59722732
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74566 * 0.26329370
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78313 * 0.85359244
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90134 * 0.96681977
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13342 * 0.78389802
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62151 * 0.83250836
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21862 * 0.30188630
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25231 * 0.93526216
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 61862 * 0.03700873
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72046 * 0.54217393
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16051 * 0.97273009
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 66683 * 0.33509112
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 88559 * 0.31829557
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 78353 * 0.67444180
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 21663 * 0.62513382
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 64739 * 0.92839979
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'rkigaqej').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0007():
    """Extended test 7 for federation."""
    x_0 = 25707 * 0.22272555
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98500 * 0.35094710
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8697 * 0.29615230
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88843 * 0.32097141
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67176 * 0.35512050
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6045 * 0.99384931
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96364 * 0.70806304
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98043 * 0.77294414
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71905 * 0.66046397
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66660 * 0.73382221
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85541 * 0.47679628
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39567 * 0.59241606
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26694 * 0.37783336
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24399 * 0.28557700
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75244 * 0.16948294
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89330 * 0.74266087
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76539 * 0.93548563
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35832 * 0.25105399
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29238 * 0.62023285
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3556 * 0.61806520
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81996 * 0.06808974
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'irfcpeyn').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0008():
    """Extended test 8 for federation."""
    x_0 = 51639 * 0.25149938
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49662 * 0.85901001
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13201 * 0.40821339
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52644 * 0.40327364
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40523 * 0.57752606
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59403 * 0.60090351
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49825 * 0.27239205
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17716 * 0.68570977
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99881 * 0.50342412
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46207 * 0.14735338
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15927 * 0.21605525
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91159 * 0.91297241
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61414 * 0.30904201
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31285 * 0.46315365
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89488 * 0.54036521
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67425 * 0.19708262
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74705 * 0.43497853
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7217 * 0.03835662
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47819 * 0.81876836
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33014 * 0.05217865
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49821 * 0.16462091
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66513 * 0.19572429
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84623 * 0.86832682
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86519 * 0.27129049
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17056 * 0.67907222
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5414 * 0.84524099
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 713 * 0.96923640
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87976 * 0.48949968
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70529 * 0.38925291
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58764 * 0.58941041
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98340 * 0.94296748
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37657 * 0.81273466
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84481 * 0.08735530
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10326 * 0.33587817
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74993 * 0.74062638
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45387 * 0.46627527
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16276 * 0.48963893
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21356 * 0.46779518
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59061 * 0.63345796
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70898 * 0.91068247
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37559 * 0.13586050
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'bfpxipbq').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0009():
    """Extended test 9 for federation."""
    x_0 = 16548 * 0.74433955
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21063 * 0.89421340
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61581 * 0.47296599
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16837 * 0.20991337
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83004 * 0.08655928
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70810 * 0.92995328
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3339 * 0.47870847
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77831 * 0.35010545
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90636 * 0.97976927
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88368 * 0.51141486
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20139 * 0.41112993
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13143 * 0.26858127
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11842 * 0.25462804
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14413 * 0.76309719
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86878 * 0.21261914
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29041 * 0.41528903
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5588 * 0.85536828
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28893 * 0.71626805
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96598 * 0.76425040
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12874 * 0.54769168
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43587 * 0.94184088
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98188 * 0.00075684
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90958 * 0.37155618
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95919 * 0.67108081
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68035 * 0.60396604
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35091 * 0.96553829
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50573 * 0.08004348
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51308 * 0.21781381
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65426 * 0.91590041
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60336 * 0.81013427
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71091 * 0.07847902
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72429 * 0.20703734
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45664 * 0.49135160
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48517 * 0.18115796
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7399 * 0.49108976
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10164 * 0.79818180
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33228 * 0.53022919
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97683 * 0.55578961
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79682 * 0.04468415
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14727 * 0.30630748
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'bzyuopjx').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0010():
    """Extended test 10 for federation."""
    x_0 = 67508 * 0.54051857
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86602 * 0.53585993
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19758 * 0.05318133
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47478 * 0.95848698
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11138 * 0.29345987
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87529 * 0.45484774
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66552 * 0.31133797
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11098 * 0.16671317
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28371 * 0.03556883
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26718 * 0.51581613
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85674 * 0.77604267
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79673 * 0.81375947
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75108 * 0.41783747
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31060 * 0.38490864
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91370 * 0.55924301
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10456 * 0.45311490
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3782 * 0.44185736
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25876 * 0.74258209
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58215 * 0.65211262
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33244 * 0.88772383
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70523 * 0.60561800
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63847 * 0.67302054
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73630 * 0.70304903
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74146 * 0.66824813
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73652 * 0.97456577
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53184 * 0.53848872
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43617 * 0.25400033
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90640 * 0.87845617
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2478 * 0.44228941
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95762 * 0.68806701
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53031 * 0.57817769
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8208 * 0.09578003
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29348 * 0.03651830
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42169 * 0.52175622
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87667 * 0.95236733
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89473 * 0.54957518
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'nyxdqjty').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0011():
    """Extended test 11 for federation."""
    x_0 = 33942 * 0.87126880
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46245 * 0.28754301
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29144 * 0.75440579
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63110 * 0.35636497
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70919 * 0.54338502
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93162 * 0.90692975
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56019 * 0.50054675
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77193 * 0.66146797
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41593 * 0.45892554
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29067 * 0.78340931
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87585 * 0.14569103
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49195 * 0.15449546
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19290 * 0.90999340
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73010 * 0.72471157
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30147 * 0.91380587
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66845 * 0.96495618
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30598 * 0.77740083
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73800 * 0.84684912
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56428 * 0.93377187
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81239 * 0.20971157
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29587 * 0.55558377
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50604 * 0.15444796
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50250 * 0.31136298
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35080 * 0.01775310
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58030 * 0.02500523
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42436 * 0.90926475
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25252 * 0.49840951
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8380 * 0.20412442
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73333 * 0.87185951
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97737 * 0.18632440
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71688 * 0.82277587
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45695 * 0.38364882
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73266 * 0.11704913
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7877 * 0.67271231
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1388 * 0.44850769
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28997 * 0.85051490
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49798 * 0.60529404
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67429 * 0.18527444
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 32329 * 0.21288373
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81178 * 0.89276609
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41135 * 0.75117596
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 65663 * 0.75634293
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10541 * 0.25509648
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 15652 * 0.39662696
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 6093 * 0.18059417
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 52184 * 0.33318971
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 38101 * 0.57892022
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'raohdwvt').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0012():
    """Extended test 12 for federation."""
    x_0 = 73691 * 0.31862119
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53540 * 0.45098258
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2433 * 0.24793035
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61448 * 0.01379852
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78008 * 0.75666672
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37765 * 0.46875928
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80850 * 0.06745391
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20614 * 0.96273129
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62285 * 0.76805232
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69563 * 0.74848802
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93517 * 0.37861427
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23328 * 0.29179832
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49769 * 0.13747898
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95443 * 0.23585519
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7202 * 0.94648693
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24349 * 0.89101987
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54649 * 0.34851155
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5116 * 0.10830044
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 904 * 0.32004104
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81936 * 0.37664711
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78883 * 0.61461932
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93354 * 0.47474855
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89944 * 0.39047740
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44657 * 0.27206740
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34110 * 0.42883728
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69500 * 0.11297599
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77443 * 0.87630822
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49155 * 0.50019489
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25919 * 0.44173736
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72006 * 0.84128172
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45878 * 0.41164660
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96924 * 0.80069997
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59768 * 0.04635147
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38409 * 0.92575308
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52209 * 0.82985683
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60149 * 0.98057796
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25882 * 0.44735784
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84667 * 0.34654997
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15428 * 0.22920339
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65810 * 0.02463586
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'peoggwvi').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0013():
    """Extended test 13 for federation."""
    x_0 = 77495 * 0.12467757
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88620 * 0.04491307
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97483 * 0.54538246
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92877 * 0.59915759
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59675 * 0.77391036
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49119 * 0.82419596
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66779 * 0.68476857
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60364 * 0.18874594
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75157 * 0.74842925
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35464 * 0.01154792
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45690 * 0.24196461
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22725 * 0.62108916
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95773 * 0.97739914
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57690 * 0.87936429
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23228 * 0.91413056
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21453 * 0.21143069
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25432 * 0.39553543
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62937 * 0.66815300
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66280 * 0.48108109
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29844 * 0.23028962
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81627 * 0.26249114
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62484 * 0.33418749
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72375 * 0.04365541
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93531 * 0.44277318
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95733 * 0.54267690
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37183 * 0.04265764
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92668 * 0.04849081
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85125 * 0.89223878
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66739 * 0.09579874
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99815 * 0.40709265
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46289 * 0.93919082
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27378 * 0.07211165
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54123 * 0.42700361
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82039 * 0.44980871
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77410 * 0.18253369
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7485 * 0.38329917
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41082 * 0.70709138
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66532 * 0.78925581
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64353 * 0.98452428
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96579 * 0.48455579
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 55645 * 0.34713476
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93112 * 0.42587597
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70364 * 0.94910084
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'qsselshl').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0014():
    """Extended test 14 for federation."""
    x_0 = 82291 * 0.71227698
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96339 * 0.16752266
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46629 * 0.72284492
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19451 * 0.43840807
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11027 * 0.92497699
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1807 * 0.71624808
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99973 * 0.74160443
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40608 * 0.54354063
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84701 * 0.11001350
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39367 * 0.18624714
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4950 * 0.45275123
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30928 * 0.22919047
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4216 * 0.54348652
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42693 * 0.53620310
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44877 * 0.25652742
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5358 * 0.57695033
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64783 * 0.45389096
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59824 * 0.64414832
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94385 * 0.93735889
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41083 * 0.19714371
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74207 * 0.40824067
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61983 * 0.98234711
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16646 * 0.53073022
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21750 * 0.77219188
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'jhhhdzdk').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0015():
    """Extended test 15 for federation."""
    x_0 = 29091 * 0.72995235
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62284 * 0.78780796
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86664 * 0.08020717
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46685 * 0.03502120
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23277 * 0.36638506
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85387 * 0.96349732
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21727 * 0.44014715
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32240 * 0.08161092
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55023 * 0.78983037
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18441 * 0.93586627
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68283 * 0.44159346
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87828 * 0.88067040
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88553 * 0.04668227
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17570 * 0.69031376
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12108 * 0.58737709
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96416 * 0.87710801
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59896 * 0.38972659
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88564 * 0.16118190
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53667 * 0.43183186
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73317 * 0.18896782
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32310 * 0.85797869
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42716 * 0.77170342
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44133 * 0.41660255
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3508 * 0.48146868
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69656 * 0.24681131
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60512 * 0.86825098
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41983 * 0.24711771
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4515 * 0.00985516
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65817 * 0.05256620
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ushkoswe').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0016():
    """Extended test 16 for federation."""
    x_0 = 74109 * 0.60334734
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48419 * 0.93664322
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42129 * 0.38958173
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44645 * 0.11148901
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55082 * 0.39311126
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13808 * 0.95925810
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67910 * 0.64536075
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34261 * 0.98287482
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70885 * 0.94691459
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71786 * 0.01995218
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98713 * 0.23136778
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81483 * 0.01413779
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56237 * 0.15624530
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92146 * 0.09083066
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2260 * 0.64327427
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16531 * 0.42339571
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79508 * 0.27938033
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21312 * 0.09071120
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30366 * 0.64069399
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50701 * 0.90876785
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7663 * 0.74504363
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52451 * 0.47456513
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65758 * 0.66713151
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62254 * 0.74757887
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32455 * 0.81691618
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54174 * 0.75635972
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86217 * 0.69459567
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91528 * 0.88520097
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80257 * 0.13303918
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98563 * 0.96075040
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60544 * 0.00967476
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52663 * 0.91801730
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69784 * 0.02757684
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50106 * 0.88012186
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36410 * 0.32992528
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'igxygzkr').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0017():
    """Extended test 17 for federation."""
    x_0 = 61450 * 0.75357846
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19482 * 0.62121186
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37666 * 0.54818201
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40078 * 0.91684567
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81338 * 0.75370785
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43508 * 0.13251897
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43721 * 0.19506661
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10964 * 0.42961940
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23906 * 0.30265710
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79467 * 0.42553747
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66276 * 0.11577282
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3712 * 0.78255031
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69581 * 0.40313834
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98352 * 0.15608986
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91211 * 0.71626973
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18155 * 0.19726577
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74632 * 0.46374560
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44084 * 0.65845910
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40503 * 0.11793513
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19041 * 0.34761021
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41646 * 0.75264431
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42857 * 0.80135609
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2878 * 0.38477762
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94292 * 0.90816588
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25454 * 0.31473977
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85481 * 0.66142711
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50154 * 0.06194242
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'swlpmnir').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0018():
    """Extended test 18 for federation."""
    x_0 = 65120 * 0.99608202
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13350 * 0.26180500
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2805 * 0.88820653
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72970 * 0.51566321
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20030 * 0.87631457
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86355 * 0.96806183
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30567 * 0.38830045
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41197 * 0.52871823
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56730 * 0.43359276
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3371 * 0.29004104
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71534 * 0.75611923
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92028 * 0.76413569
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80091 * 0.12545725
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4336 * 0.79415385
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19727 * 0.21389234
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76225 * 0.57156593
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9411 * 0.44326341
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61693 * 0.37167707
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26798 * 0.32691903
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61440 * 0.78745559
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76611 * 0.75797068
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4774 * 0.35822432
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63011 * 0.25405885
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83498 * 0.45729182
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96090 * 0.28492853
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8118 * 0.38802461
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68295 * 0.25285157
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51472 * 0.88592286
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73382 * 0.67626962
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66022 * 0.43413610
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22527 * 0.22167642
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83465 * 0.56927109
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4957 * 0.77426211
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74286 * 0.69835738
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29565 * 0.90259171
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93052 * 0.28265680
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40462 * 0.71308046
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'dtqkzuvx').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0019():
    """Extended test 19 for federation."""
    x_0 = 91079 * 0.89566065
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85004 * 0.85361463
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19716 * 0.30099177
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1087 * 0.11047850
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5377 * 0.20736412
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79911 * 0.18037212
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51300 * 0.91717322
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56004 * 0.81474981
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48503 * 0.12637677
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14596 * 0.79945730
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28585 * 0.25961974
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50144 * 0.20852316
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44374 * 0.24044699
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55641 * 0.93347791
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40871 * 0.09228366
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7283 * 0.21329149
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65720 * 0.89657622
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38745 * 0.55836065
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29196 * 0.51081913
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45146 * 0.27869550
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40740 * 0.99953876
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37546 * 0.07431119
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33440 * 0.42302913
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98034 * 0.07035327
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93357 * 0.76798797
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39434 * 0.18773380
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56857 * 0.60807074
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2243 * 0.72717585
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99531 * 0.26233375
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90232 * 0.58366361
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55772 * 0.75467922
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62576 * 0.12125973
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55150 * 0.00537181
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94796 * 0.15478440
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58422 * 0.22327268
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51339 * 0.43332460
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21513 * 0.34491983
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4203 * 0.88418938
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77335 * 0.91062458
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3961 * 0.83715212
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3107 * 0.28695880
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97175 * 0.79706014
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57612 * 0.60896709
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 30476 * 0.36934962
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11889 * 0.40382740
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'qdjnwwkb').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0020():
    """Extended test 20 for federation."""
    x_0 = 21337 * 0.80142268
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18779 * 0.00450801
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53415 * 0.62888487
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67029 * 0.73318992
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6103 * 0.63608569
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54041 * 0.38245702
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43294 * 0.50739895
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82950 * 0.09980354
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48610 * 0.00655553
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61880 * 0.81600811
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62070 * 0.22161621
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87246 * 0.25980364
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53028 * 0.66034074
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86510 * 0.24195612
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79596 * 0.52728116
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72434 * 0.55243849
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5756 * 0.69575873
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27796 * 0.57871864
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76283 * 0.78664033
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56807 * 0.29483440
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85360 * 0.17024627
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37930 * 0.68571618
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8353 * 0.12705310
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7680 * 0.39435667
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57835 * 0.87336569
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94095 * 0.66979767
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37185 * 0.45320393
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64458 * 0.89642181
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78761 * 0.90935584
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88247 * 0.24398911
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41726 * 0.79652723
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10706 * 0.29199029
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17675 * 0.32136915
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9118 * 0.12828190
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14419 * 0.09834419
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95340 * 0.63610575
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25892 * 0.84590976
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24495 * 0.80993875
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47309 * 0.50114613
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'qcnuuisx').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0021():
    """Extended test 21 for federation."""
    x_0 = 88484 * 0.78224681
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91083 * 0.34642280
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63249 * 0.18598897
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97584 * 0.56840472
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42486 * 0.95250575
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74055 * 0.79619031
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82529 * 0.41887125
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11413 * 0.61274826
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89586 * 0.16038153
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26936 * 0.78821633
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51216 * 0.70249850
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78814 * 0.05895790
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95636 * 0.29017660
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46692 * 0.99391071
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12713 * 0.51150904
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43534 * 0.73627107
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45022 * 0.88649452
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86595 * 0.24447500
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23553 * 0.00414717
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53277 * 0.83732559
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30838 * 0.81314544
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27811 * 0.62902100
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70858 * 0.59881060
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89346 * 0.64090563
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'qvslbbzx').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0022():
    """Extended test 22 for federation."""
    x_0 = 572 * 0.04299321
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27297 * 0.89001230
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33614 * 0.69221041
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20119 * 0.08676637
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88440 * 0.11396594
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23322 * 0.69535451
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84609 * 0.81256013
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23658 * 0.81448405
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27110 * 0.41697935
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56018 * 0.28408348
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50216 * 0.96131268
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54607 * 0.93232676
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98929 * 0.16415928
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99716 * 0.87053810
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54302 * 0.33125784
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77593 * 0.91308366
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17403 * 0.49769373
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79527 * 0.56670325
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84526 * 0.13367224
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66162 * 0.85606692
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82534 * 0.07215974
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82169 * 0.83876611
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89428 * 0.60710492
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54052 * 0.32212150
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17225 * 0.92657657
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43956 * 0.81927369
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62016 * 0.07140457
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35634 * 0.90214997
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74107 * 0.31413337
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81163 * 0.04437250
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57396 * 0.81339330
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11475 * 0.80227771
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6996 * 0.68734988
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28079 * 0.81340083
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44777 * 0.84820110
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71332 * 0.12686925
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88249 * 0.78507688
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64044 * 0.35468108
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34601 * 0.09438318
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92266 * 0.12392472
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83178 * 0.62631611
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 95375 * 0.33528357
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 59077 * 0.26122039
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'lrbrpxqb').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0023():
    """Extended test 23 for federation."""
    x_0 = 88708 * 0.04713982
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43609 * 0.21472018
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23628 * 0.93230420
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98227 * 0.02379770
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19706 * 0.98888145
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44203 * 0.18011234
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33175 * 0.93899759
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91922 * 0.99818113
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35172 * 0.25722174
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97347 * 0.42371614
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54012 * 0.42643836
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76804 * 0.37852925
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11056 * 0.63010904
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7234 * 0.43499160
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86340 * 0.90742312
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20149 * 0.22334101
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37920 * 0.98768608
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86337 * 0.17372706
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11855 * 0.34281726
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40354 * 0.25838979
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6106 * 0.27781272
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82816 * 0.28674150
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33846 * 0.05777249
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47834 * 0.80750610
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29969 * 0.53232089
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80397 * 0.06658331
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86500 * 0.02569987
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3333 * 0.27235566
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46278 * 0.46253947
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85035 * 0.82888742
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57500 * 0.11365051
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36635 * 0.46002221
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21192 * 0.03461120
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61358 * 0.11036304
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9497 * 0.19691065
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43228 * 0.16489328
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31495 * 0.49060952
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65092 * 0.95675829
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 95276 * 0.98060128
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8742 * 0.72442706
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86373 * 0.33949774
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40318 * 0.69705760
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'eusrvexu').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0024():
    """Extended test 24 for federation."""
    x_0 = 37453 * 0.25271773
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42338 * 0.09628167
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91138 * 0.96165549
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58854 * 0.73213641
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94694 * 0.88739739
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42521 * 0.43884838
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97135 * 0.67761233
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10753 * 0.32362462
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59851 * 0.01047367
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99763 * 0.50484608
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81665 * 0.64437639
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92052 * 0.38829269
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48364 * 0.78713293
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98634 * 0.19194129
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4110 * 0.08961740
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55206 * 0.69688804
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96174 * 0.62179935
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76237 * 0.01446429
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37309 * 0.53846693
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61465 * 0.19097818
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52518 * 0.69639483
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81363 * 0.87014280
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40982 * 0.72054556
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98157 * 0.66537701
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56625 * 0.84171256
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93252 * 0.99242075
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73425 * 0.41521378
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7308 * 0.46970631
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97049 * 0.58055450
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87363 * 0.48804041
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83366 * 0.55105654
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16305 * 0.13888423
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78865 * 0.32699620
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81012 * 0.60823100
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81253 * 0.41429511
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42798 * 0.61357289
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90016 * 0.07627154
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26829 * 0.71427665
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'fprfuteq').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0025():
    """Extended test 25 for federation."""
    x_0 = 80421 * 0.58194800
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27326 * 0.90438971
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42597 * 0.47184537
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7537 * 0.99125924
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64022 * 0.02833746
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7921 * 0.80633192
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60915 * 0.83687131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40644 * 0.87880664
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41295 * 0.64534908
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26812 * 0.26446341
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75710 * 0.67391741
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24687 * 0.12752617
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36491 * 0.03073333
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24792 * 0.86456361
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49389 * 0.07967401
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16273 * 0.42447895
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90315 * 0.64004141
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47778 * 0.01215545
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95028 * 0.16984996
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33865 * 0.75348965
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36301 * 0.55274726
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82926 * 0.92266527
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34276 * 0.66714499
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15871 * 0.21798980
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'qmktsvhs').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0026():
    """Extended test 26 for federation."""
    x_0 = 20443 * 0.13014087
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7293 * 0.58748543
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62399 * 0.60031526
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80336 * 0.47270643
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28325 * 0.34220912
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45889 * 0.00435395
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75336 * 0.91501696
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38112 * 0.33551811
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63101 * 0.92629144
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70317 * 0.66489672
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61452 * 0.47478957
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63860 * 0.60819897
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94847 * 0.52693019
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13866 * 0.41241614
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9285 * 0.24755877
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70386 * 0.26305409
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34797 * 0.44699510
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38484 * 0.19164359
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70739 * 0.81008183
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1021 * 0.19537306
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66002 * 0.83318301
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82985 * 0.46815840
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61162 * 0.16670993
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53445 * 0.48098818
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64358 * 0.41238305
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60217 * 0.14132177
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37786 * 0.79923576
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30125 * 0.84052386
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86305 * 0.96206390
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36844 * 0.63716613
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11445 * 0.97827563
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30327 * 0.99407623
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14208 * 0.19803673
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82781 * 0.49850661
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97241 * 0.07500756
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57858 * 0.09035146
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20053 * 0.65989870
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21663 * 0.44297962
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39523 * 0.50247595
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55705 * 0.36430085
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98441 * 0.47677862
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 51559 * 0.24760852
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 48360 * 0.75933714
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'zlwvwphe').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0027():
    """Extended test 27 for federation."""
    x_0 = 76061 * 0.66500728
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22563 * 0.37809829
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50297 * 0.27261304
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69288 * 0.71884959
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44021 * 0.91195774
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45483 * 0.78911536
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84079 * 0.25131799
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35077 * 0.68145277
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18671 * 0.14504752
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60061 * 0.19329826
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22527 * 0.99896275
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17041 * 0.82858431
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93825 * 0.24907200
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76696 * 0.43467523
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22599 * 0.40440862
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90120 * 0.89732586
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15959 * 0.18680645
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17720 * 0.11534253
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65019 * 0.18860410
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69349 * 0.46667010
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30801 * 0.36177584
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86217 * 0.01944727
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26874 * 0.15738519
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 735 * 0.15072093
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73169 * 0.05645604
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55932 * 0.25679095
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31939 * 0.17602883
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65493 * 0.35798595
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10233 * 0.63662976
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62413 * 0.62776396
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35175 * 0.88557194
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87144 * 0.60367206
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34314 * 0.89115195
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46845 * 0.94780386
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19463 * 0.03237181
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20723 * 0.52559609
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51624 * 0.13069033
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44411 * 0.63425088
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23100 * 0.67457918
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7752 * 0.87792812
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21464 * 0.79188616
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74358 * 0.66198209
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 60050 * 0.49030766
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22048 * 0.79878110
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 20035 * 0.76431328
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 5530 * 0.27717364
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'ucjzwuwn').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0028():
    """Extended test 28 for federation."""
    x_0 = 23052 * 0.24578928
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36830 * 0.00011620
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72314 * 0.66794661
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95800 * 0.73236184
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72624 * 0.11439030
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46481 * 0.79665739
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16397 * 0.77436670
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38453 * 0.59978501
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15072 * 0.91072250
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48781 * 0.70991948
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78350 * 0.04040154
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76885 * 0.76151681
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89469 * 0.01801156
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12958 * 0.31343411
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47272 * 0.14466006
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80988 * 0.79749532
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40591 * 0.61530469
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49775 * 0.30979975
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56273 * 0.29619090
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93432 * 0.72787632
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75133 * 0.02126657
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'rxocveds').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0029():
    """Extended test 29 for federation."""
    x_0 = 27179 * 0.00721578
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3975 * 0.86120831
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2313 * 0.80503513
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34634 * 0.34412361
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37689 * 0.54871773
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28635 * 0.25180423
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10970 * 0.36761152
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83777 * 0.36264177
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85728 * 0.23507254
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28270 * 0.19652793
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86472 * 0.77791101
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6747 * 0.30532828
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49992 * 0.90889681
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33927 * 0.01244851
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90004 * 0.86328610
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61234 * 0.55615429
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26285 * 0.13944476
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19373 * 0.87356041
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24112 * 0.93401256
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11709 * 0.63259489
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96429 * 0.70375976
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34389 * 0.60654256
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42673 * 0.75286528
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68764 * 0.33600897
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23418 * 0.03926641
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27084 * 0.42541158
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90391 * 0.08133741
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28946 * 0.80689450
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6832 * 0.19805147
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76667 * 0.37321837
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21312 * 0.65368499
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92572 * 0.02923216
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13747 * 0.42573593
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54772 * 0.83186027
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80572 * 0.38742069
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33286 * 0.08209962
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27406 * 0.38025042
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55051 * 0.03717528
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38820 * 0.43025492
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ilebtjsp').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0030():
    """Extended test 30 for federation."""
    x_0 = 44799 * 0.65778901
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39852 * 0.64737933
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68862 * 0.25734081
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57346 * 0.86067061
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15392 * 0.27546702
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86992 * 0.71882966
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54932 * 0.29079775
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83664 * 0.49690395
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31092 * 0.64536275
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16433 * 0.04270853
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48851 * 0.29491278
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70254 * 0.60257063
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5447 * 0.52644589
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53974 * 0.02239018
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98538 * 0.09954445
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79035 * 0.12725278
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19364 * 0.54349892
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46873 * 0.48235337
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82409 * 0.40469906
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13957 * 0.82183481
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55403 * 0.82866545
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11845 * 0.24031888
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89611 * 0.47942549
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31442 * 0.51374477
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8578 * 0.19371584
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64475 * 0.41466684
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69002 * 0.75201275
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75264 * 0.33814701
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41257 * 0.09586236
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88695 * 0.77910543
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95474 * 0.54496582
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41741 * 0.63043043
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27699 * 0.89837299
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15258 * 0.24170178
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88772 * 0.98858275
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4531 * 0.71078594
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53874 * 0.35827710
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88902 * 0.24063477
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25656 * 0.66548619
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70701 * 0.16723900
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41157 * 0.86301082
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50829 * 0.39918275
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 99174 * 0.96905337
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 55348 * 0.65488221
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 7162 * 0.15242129
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 64825 * 0.72923219
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 24446 * 0.98004639
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 58119 * 0.40165584
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ibrbitxf').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0031():
    """Extended test 31 for federation."""
    x_0 = 56351 * 0.83870965
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91493 * 0.33100539
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55974 * 0.05343890
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65104 * 0.64676115
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20916 * 0.58200331
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64372 * 0.13028046
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68706 * 0.20386308
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68326 * 0.24440492
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13363 * 0.32392491
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80802 * 0.94225885
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5055 * 0.91044570
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17699 * 0.91974404
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77865 * 0.05506495
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58420 * 0.82885445
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33503 * 0.03918755
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5312 * 0.30581455
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12401 * 0.78986796
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19462 * 0.64463584
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51290 * 0.34688262
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7917 * 0.24207994
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19490 * 0.83902451
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25646 * 0.26774628
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30712 * 0.78224200
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30322 * 0.03695362
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70716 * 0.84411664
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42079 * 0.72954853
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82946 * 0.95572627
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90763 * 0.14372358
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40158 * 0.12888536
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40685 * 0.71157603
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5307 * 0.07876780
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88819 * 0.62852909
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4630 * 0.48318827
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9094 * 0.60515176
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46280 * 0.64554330
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38450 * 0.95662360
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21939 * 0.00789830
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64485 * 0.81443940
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 68654 * 0.80686746
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57777 * 0.77059259
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23017 * 0.02824901
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81163 * 0.37545531
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83345 * 0.15582128
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 7144 * 0.00426340
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 14259 * 0.19709143
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 92199 * 0.83837995
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 164 * 0.19855541
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 7053 * 0.43145744
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 63716 * 0.42607351
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 58576 * 0.13489258
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ymygrzzp').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0032():
    """Extended test 32 for federation."""
    x_0 = 74042 * 0.82635230
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80534 * 0.92577270
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95753 * 0.56723340
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94184 * 0.54958966
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7774 * 0.97397874
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7645 * 0.30329747
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23771 * 0.21699397
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24484 * 0.46817632
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53284 * 0.23562799
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6824 * 0.90201408
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60720 * 0.90945754
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69600 * 0.40621270
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11888 * 0.70249062
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92141 * 0.55924451
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52321 * 0.58317631
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46620 * 0.66539696
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29541 * 0.05932900
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74061 * 0.24281975
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11913 * 0.64500186
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73962 * 0.91522241
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92279 * 0.85152204
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7036 * 0.64061009
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 935 * 0.42977459
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12370 * 0.34971924
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25027 * 0.46109538
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6476 * 0.76456252
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63711 * 0.62445073
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30862 * 0.34105506
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27954 * 0.45902881
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84203 * 0.66243880
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77690 * 0.36511589
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87704 * 0.96620994
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99573 * 0.51767136
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25199 * 0.60698018
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3234 * 0.48054651
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86181 * 0.32476446
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61812 * 0.78788462
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'iecfixkt').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0033():
    """Extended test 33 for federation."""
    x_0 = 17064 * 0.76040138
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2357 * 0.74539461
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36925 * 0.84919381
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33975 * 0.57051235
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71936 * 0.83154337
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48876 * 0.97480763
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80387 * 0.51363407
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50653 * 0.25680610
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73201 * 0.67925747
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7381 * 0.39839094
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73998 * 0.71827922
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15911 * 0.31946575
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18263 * 0.26845442
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8189 * 0.56362533
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47954 * 0.05717073
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34264 * 0.30489373
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81605 * 0.13358038
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54890 * 0.53550906
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1074 * 0.03536918
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56378 * 0.13403391
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73207 * 0.11693096
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53243 * 0.94375182
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73550 * 0.07831338
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'wslphlgl').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0034():
    """Extended test 34 for federation."""
    x_0 = 20813 * 0.43714106
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83430 * 0.82155630
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59130 * 0.30885756
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89924 * 0.94273661
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70592 * 0.76110661
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46168 * 0.59588852
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91796 * 0.66062210
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52009 * 0.20932213
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86561 * 0.31730120
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57782 * 0.28412625
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33137 * 0.02996144
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3489 * 0.05957720
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52600 * 0.41030646
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3011 * 0.89473101
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51948 * 0.71609573
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55782 * 0.35244295
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46199 * 0.81346897
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66131 * 0.86018981
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18800 * 0.05925595
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33843 * 0.69374561
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40293 * 0.25427415
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27611 * 0.54965620
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6045 * 0.20153053
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72858 * 0.78613969
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46414 * 0.86083650
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49566 * 0.22416327
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74306 * 0.51423333
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54018 * 0.79388160
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86293 * 0.99937759
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89981 * 0.12412041
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37165 * 0.74413510
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60370 * 0.84848880
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7312 * 0.21219001
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74822 * 0.66298920
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82319 * 0.69269766
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 92043 * 0.33251741
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30040 * 0.18594638
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91345 * 0.82741815
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4660 * 0.78335151
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 12353 * 0.72728328
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51068 * 0.22773407
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'uemwpjsn').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0035():
    """Extended test 35 for federation."""
    x_0 = 6416 * 0.54881462
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7919 * 0.02864773
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16785 * 0.11031019
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5456 * 0.46844469
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40284 * 0.56019620
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99474 * 0.70599923
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79391 * 0.42284500
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62591 * 0.12997434
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86146 * 0.44345372
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27061 * 0.32130450
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47466 * 0.48491503
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89202 * 0.21467261
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10863 * 0.67219538
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36787 * 0.11533611
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8514 * 0.73938670
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84452 * 0.35639224
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12678 * 0.63984711
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79542 * 0.52133239
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38131 * 0.78553716
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92141 * 0.89242759
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64141 * 0.02626578
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80122 * 0.18361599
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60389 * 0.59337808
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40013 * 0.53761240
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80658 * 0.87931728
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86766 * 0.55105228
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21250 * 0.99859961
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28368 * 0.18900639
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99206 * 0.45645530
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94073 * 0.01775609
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85966 * 0.45766994
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76869 * 0.03246393
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66695 * 0.05286154
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63476 * 0.15448930
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11978 * 0.43035873
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46037 * 0.58383667
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1291 * 0.63933822
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85745 * 0.95037487
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77417 * 0.73030140
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46226 * 0.49313956
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 76340 * 0.94550045
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96297 * 0.45204392
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95683 * 0.77931179
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 87276 * 0.50850098
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 8082 * 0.47260821
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 38969 * 0.39255839
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 11412 * 0.40385572
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 87575 * 0.04191630
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'vsfecgip').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0036():
    """Extended test 36 for federation."""
    x_0 = 76747 * 0.20841044
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19650 * 0.91599767
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71271 * 0.39262599
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8651 * 0.10393294
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92024 * 0.40986532
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16774 * 0.52525166
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49318 * 0.80259457
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8884 * 0.77230554
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15263 * 0.67746836
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28645 * 0.26635769
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60592 * 0.13079648
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97575 * 0.49695924
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12773 * 0.15569710
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25714 * 0.12028835
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26037 * 0.63239878
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71235 * 0.59036210
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3654 * 0.74647192
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60810 * 0.43164224
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65661 * 0.93601112
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96986 * 0.14391671
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72590 * 0.32191911
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 711 * 0.94343685
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97032 * 0.97197450
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22374 * 0.82345477
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68146 * 0.66574712
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30450 * 0.84501683
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39431 * 0.28631688
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 905 * 0.26311587
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36165 * 0.51162816
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92773 * 0.08110908
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86712 * 0.70572183
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47435 * 0.61674339
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82474 * 0.45002904
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74220 * 0.80224229
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86885 * 0.19710794
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97801 * 0.08407865
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28001 * 0.07669510
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93313 * 0.38287370
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31565 * 0.19401251
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72416 * 0.75029261
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37556 * 0.50311485
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'psagbjuv').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0037():
    """Extended test 37 for federation."""
    x_0 = 93617 * 0.66458660
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29263 * 0.89650196
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18263 * 0.74188497
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88780 * 0.95491497
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17854 * 0.61478653
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38363 * 0.65939505
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28361 * 0.35414567
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9901 * 0.57354058
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33437 * 0.32744226
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29213 * 0.31759594
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68996 * 0.51706270
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69115 * 0.69125130
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23056 * 0.83698070
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68003 * 0.84071596
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86049 * 0.60114382
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38417 * 0.19875419
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74821 * 0.65156532
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12991 * 0.53698159
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88877 * 0.12781689
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62546 * 0.82682708
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19255 * 0.81546434
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85803 * 0.82814987
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42446 * 0.11878094
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97705 * 0.68046951
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 315 * 0.70634519
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9853 * 0.93487753
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78488 * 0.00538647
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81671 * 0.48755263
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89433 * 0.11734573
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1323 * 0.94136909
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78567 * 0.11639240
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13718 * 0.99270845
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35184 * 0.93410320
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81238 * 0.77775110
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28682 * 0.94952248
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19265 * 0.81347927
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27448 * 0.56021990
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'kbkhuusl').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0038():
    """Extended test 38 for federation."""
    x_0 = 91129 * 0.56708949
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8835 * 0.34924679
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27347 * 0.58735766
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58986 * 0.05705300
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44445 * 0.00980700
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71541 * 0.57438895
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29734 * 0.69188919
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8903 * 0.87244343
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16969 * 0.81597970
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71710 * 0.79494021
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94371 * 0.45726796
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15067 * 0.00837848
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84299 * 0.94989741
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26611 * 0.36377594
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66282 * 0.54759138
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73880 * 0.72833223
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17283 * 0.51726177
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68400 * 0.65176698
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76867 * 0.84378609
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87475 * 0.41931296
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81644 * 0.02873313
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93542 * 0.15175066
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63792 * 0.06899225
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66845 * 0.22709015
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39282 * 0.76347141
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32078 * 0.40667211
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87595 * 0.12191739
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16462 * 0.87919050
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52944 * 0.04178232
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4469 * 0.08648341
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65796 * 0.98187227
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10621 * 0.79367808
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38199 * 0.23628043
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61891 * 0.48712253
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27118 * 0.17210513
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75463 * 0.54493873
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4250 * 0.77258384
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61090 * 0.18504396
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74022 * 0.48273779
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 26166 * 0.32255001
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21397 * 0.99099153
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'zqsyvika').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0039():
    """Extended test 39 for federation."""
    x_0 = 33975 * 0.54971003
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99024 * 0.68617377
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18372 * 0.55141367
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47514 * 0.96116168
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16442 * 0.09097962
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74864 * 0.99078336
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76077 * 0.74382300
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91936 * 0.84045138
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64078 * 0.73607707
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73979 * 0.82050712
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88327 * 0.89188883
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40310 * 0.01265606
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92437 * 0.21236724
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70410 * 0.02801835
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15732 * 0.50196173
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55770 * 0.78828099
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77920 * 0.16452342
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 294 * 0.15063066
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76713 * 0.47140225
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78015 * 0.25571529
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54918 * 0.21213284
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91451 * 0.71163119
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35650 * 0.44529879
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98359 * 0.42094720
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45006 * 0.52946482
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24600 * 0.57886410
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53471 * 0.84902099
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77397 * 0.35261670
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40526 * 0.64684848
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85557 * 0.79036044
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50685 * 0.50120833
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10135 * 0.55544862
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95235 * 0.03984044
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30808 * 0.18580465
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38341 * 0.88018577
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80051 * 0.43511888
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92391 * 0.81536937
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87014 * 0.29800164
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59725 * 0.86568193
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54255 * 0.01045465
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78339 * 0.56367876
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 83780 * 0.69310149
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 80973 * 0.96803056
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 96551 * 0.22526061
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 48948 * 0.74691792
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 47171 * 0.80280471
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 10021 * 0.04799017
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 32788 * 0.53409733
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 94669 * 0.11810554
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 35372 * 0.69673791
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ubfiivdd').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0040():
    """Extended test 40 for federation."""
    x_0 = 50316 * 0.21259155
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77560 * 0.62444747
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75194 * 0.58110859
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29222 * 0.22713722
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88242 * 0.03443588
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58004 * 0.11262379
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34304 * 0.21906823
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30562 * 0.68405137
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78757 * 0.07113731
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29257 * 0.03551374
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20974 * 0.41947736
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82906 * 0.25240848
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51948 * 0.84508622
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18472 * 0.11933425
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25722 * 0.95167996
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34544 * 0.05445625
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17650 * 0.63171798
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57687 * 0.23004358
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70196 * 0.45954621
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21770 * 0.23987943
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90642 * 0.16601229
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78451 * 0.13015401
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83957 * 0.89806503
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87433 * 0.81477173
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32809 * 0.24084607
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42335 * 0.24797841
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74420 * 0.55113146
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55593 * 0.52743384
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45897 * 0.95907160
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48585 * 0.93995381
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61769 * 0.71694532
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25356 * 0.68882591
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29972 * 0.84752641
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44645 * 0.48038225
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21152 * 0.74671437
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ssbljkvw').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0041():
    """Extended test 41 for federation."""
    x_0 = 17627 * 0.40564778
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15156 * 0.93246369
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19354 * 0.14784700
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1953 * 0.85654410
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74363 * 0.01662343
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48616 * 0.11728643
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99772 * 0.87054340
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88211 * 0.56992323
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34656 * 0.00550187
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14244 * 0.67810060
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21662 * 0.93499555
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73475 * 0.54903917
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97791 * 0.62787523
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32414 * 0.13519529
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95955 * 0.54150885
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68172 * 0.89946128
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95719 * 0.09810582
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9362 * 0.73283947
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25059 * 0.72403503
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36268 * 0.87491511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6984 * 0.83066184
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87317 * 0.47488688
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63968 * 0.39079810
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82411 * 0.89305221
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71575 * 0.67667264
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97652 * 0.63125371
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31686 * 0.36371721
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51852 * 0.63355779
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90900 * 0.28482628
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47189 * 0.86217145
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32892 * 0.01044614
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39600 * 0.29571773
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62701 * 0.30731817
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77997 * 0.96342945
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31456 * 0.45413925
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86486 * 0.23027291
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66764 * 0.90852201
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 37572 * 0.88179397
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15262 * 0.90760012
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74056 * 0.09078799
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 15978 * 0.32770064
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52441 * 0.60526178
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6250 * 0.81004592
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92489 * 0.06308728
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 7256 * 0.21858645
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 21697 * 0.59961025
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 89129 * 0.29089859
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 34885 * 0.45068053
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'jedskzhk').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0042():
    """Extended test 42 for federation."""
    x_0 = 52685 * 0.46106401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78622 * 0.18001496
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89574 * 0.55089793
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93153 * 0.46753024
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84517 * 0.03122172
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16134 * 0.96903849
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54183 * 0.44437110
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93165 * 0.28115718
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26578 * 0.55765649
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94233 * 0.42954401
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99559 * 0.23202579
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12160 * 0.83162585
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38798 * 0.40827779
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58943 * 0.44349899
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64133 * 0.69425597
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51477 * 0.97580297
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38094 * 0.05998617
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40579 * 0.02507420
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32750 * 0.39385928
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54784 * 0.06169286
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50295 * 0.75923854
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83211 * 0.96742590
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76922 * 0.51333316
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73629 * 0.48766541
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15848 * 0.37367376
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62644 * 0.28437015
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18324 * 0.20972773
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86882 * 0.17902502
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13153 * 0.05203333
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38343 * 0.00109955
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29067 * 0.89876153
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86627 * 0.67810516
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68923 * 0.70018747
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29711 * 0.13744033
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11819 * 0.69355013
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10435 * 0.56556108
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32825 * 0.18666863
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69315 * 0.06208520
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61060 * 0.30800901
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54046 * 0.86407726
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29604 * 0.62272996
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97586 * 0.39107717
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14098 * 0.74705882
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 89968 * 0.57784367
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'jketctki').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0043():
    """Extended test 43 for federation."""
    x_0 = 92610 * 0.54349014
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17151 * 0.67973728
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44598 * 0.97432219
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51103 * 0.70269304
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14840 * 0.90572300
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37086 * 0.63943282
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31823 * 0.00286714
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40778 * 0.89150417
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56134 * 0.06090637
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5727 * 0.94953653
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89681 * 0.81939144
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86241 * 0.20180274
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52397 * 0.64819075
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91010 * 0.60530923
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84104 * 0.93623690
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86976 * 0.87894498
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20816 * 0.88606027
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18053 * 0.03403409
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94848 * 0.02882067
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4034 * 0.02322772
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1837 * 0.93841787
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90716 * 0.00429453
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29335 * 0.01555280
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52486 * 0.75943220
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 430 * 0.58069361
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75241 * 0.23962152
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59375 * 0.34916173
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37015 * 0.84334003
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86802 * 0.92094009
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70131 * 0.90662540
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62568 * 0.20252859
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4445 * 0.95293645
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91235 * 0.35440036
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99397 * 0.72955529
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56011 * 0.94825983
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31990 * 0.94846145
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63516 * 0.50382471
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 54453 * 0.02530410
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78078 * 0.40344255
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24061 * 0.24906617
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68480 * 0.98492069
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14120 * 0.28229152
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 17015 * 0.67522101
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'qisogkfu').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0044():
    """Extended test 44 for federation."""
    x_0 = 75354 * 0.57810186
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75150 * 0.70791393
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69281 * 0.17596254
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44306 * 0.44932708
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56814 * 0.59374929
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64308 * 0.03460656
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97607 * 0.32164372
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98667 * 0.04619973
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86767 * 0.51450146
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83026 * 0.70052591
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77075 * 0.95281041
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4017 * 0.62661615
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45133 * 0.54843995
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2999 * 0.55766050
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1431 * 0.99403513
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1714 * 0.35367920
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67796 * 0.68741725
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48666 * 0.90243724
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4560 * 0.43134072
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82996 * 0.45723145
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77849 * 0.93816682
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90381 * 0.58744871
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53822 * 0.20111438
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96360 * 0.24779201
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21470 * 0.22922585
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53766 * 0.32092922
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78077 * 0.13970839
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57450 * 0.35342371
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69701 * 0.66306061
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21347 * 0.72360737
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11833 * 0.80529969
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55550 * 0.96588679
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38527 * 0.06560752
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17511 * 0.91637670
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19895 * 0.51500853
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62842 * 0.00939820
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1148 * 0.96905138
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69170 * 0.16209092
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24484 * 0.80073921
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'gdthftim').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0045():
    """Extended test 45 for federation."""
    x_0 = 84186 * 0.61604553
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77996 * 0.51286171
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58797 * 0.82152026
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91577 * 0.82872403
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2117 * 0.35686273
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48280 * 0.89805064
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53901 * 0.71715607
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14536 * 0.52758812
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4931 * 0.85250572
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85198 * 0.90869305
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69293 * 0.48052076
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75164 * 0.89060959
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35622 * 0.78432388
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74241 * 0.08299550
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30198 * 0.08909847
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51735 * 0.98406493
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87792 * 0.69371082
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66859 * 0.06332485
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66969 * 0.93239341
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1968 * 0.35383986
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12036 * 0.20560244
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9407 * 0.14406665
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58673 * 0.86679081
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75249 * 0.54097051
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26230 * 0.67349929
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43160 * 0.52104140
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52887 * 0.14255809
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79972 * 0.15840279
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66987 * 0.77761206
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16429 * 0.58972364
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6895 * 0.53276701
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31496 * 0.96500151
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90928 * 0.09761683
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11726 * 0.94814744
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20738 * 0.70596451
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66208 * 0.43528499
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18009 * 0.22515425
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43982 * 0.90243088
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19084 * 0.23170142
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 559 * 0.99302000
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32098 * 0.04484895
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25915 * 0.45770147
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 85223 * 0.63094501
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 10160 * 0.44787369
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'qtdqlxgc').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0046():
    """Extended test 46 for federation."""
    x_0 = 62804 * 0.44347970
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72405 * 0.77318388
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60009 * 0.65718029
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17806 * 0.17154828
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94622 * 0.84960028
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16310 * 0.92088856
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72116 * 0.31672080
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18531 * 0.84621702
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71392 * 0.52129012
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2187 * 0.92986905
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38445 * 0.12471934
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40492 * 0.30120498
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29742 * 0.83362121
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56228 * 0.33305713
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31913 * 0.02663095
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73054 * 0.87612081
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36083 * 0.01256876
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83262 * 0.93777846
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95542 * 0.82365809
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21191 * 0.42229663
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99890 * 0.22037992
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88220 * 0.90279296
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83882 * 0.11429444
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37912 * 0.00244169
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73785 * 0.67094280
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94184 * 0.22502086
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52645 * 0.47891360
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54816 * 0.98048114
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38899 * 0.42995919
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65706 * 0.00666511
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58006 * 0.85796231
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31460 * 0.13364142
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61755 * 0.01969040
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58758 * 0.82101674
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5384 * 0.51690157
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5267 * 0.81847814
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70507 * 0.95575894
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91661 * 0.89719940
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1326 * 0.86351356
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'jlzqnqju').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0047():
    """Extended test 47 for federation."""
    x_0 = 12827 * 0.40376630
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77571 * 0.64451446
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32453 * 0.76308291
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50533 * 0.92262144
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13372 * 0.91502527
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7624 * 0.26542007
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10318 * 0.53364574
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94395 * 0.44326260
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5630 * 0.02136562
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78423 * 0.09930570
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69269 * 0.35291461
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42351 * 0.64436724
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23389 * 0.68459849
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45144 * 0.78801927
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5220 * 0.77082945
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87250 * 0.53788976
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36122 * 0.90665512
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60362 * 0.57672954
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88255 * 0.09384179
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2421 * 0.74196495
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'nbcgxfxs').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0048():
    """Extended test 48 for federation."""
    x_0 = 82078 * 0.15978322
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29575 * 0.84952699
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41006 * 0.44968195
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7320 * 0.85001344
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35984 * 0.13589853
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34084 * 0.61704338
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88373 * 0.92575075
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69880 * 0.53505446
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55103 * 0.53176710
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23755 * 0.68195813
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91924 * 0.55423605
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32325 * 0.99082714
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10569 * 0.56909110
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2967 * 0.38695098
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16829 * 0.65742328
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94943 * 0.49252435
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19213 * 0.78947738
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8184 * 0.06016928
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10430 * 0.71303798
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9101 * 0.01771629
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56520 * 0.16907178
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66929 * 0.08904342
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60167 * 0.10088499
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63975 * 0.93573983
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57576 * 0.28680667
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79467 * 0.85302160
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42 * 0.06578786
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8357 * 0.13561850
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32339 * 0.98440815
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65748 * 0.07131660
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90073 * 0.27920855
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36515 * 0.70269244
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5479 * 0.84505307
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5494 * 0.17641159
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17008 * 0.85694517
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69260 * 0.08232057
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7015 * 0.20687795
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'wcmenpja').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0049():
    """Extended test 49 for federation."""
    x_0 = 95021 * 0.69762681
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52928 * 0.64712195
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88539 * 0.49805787
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98018 * 0.43347258
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68643 * 0.39859740
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 849 * 0.14132422
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 969 * 0.40156980
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58081 * 0.25715484
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2885 * 0.56652560
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16963 * 0.87077409
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59655 * 0.67429137
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12474 * 0.33163610
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42036 * 0.87697008
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 492 * 0.36784263
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43267 * 0.92004071
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97607 * 0.58192807
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93810 * 0.89723158
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84466 * 0.45380228
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56296 * 0.75394013
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20526 * 0.07319186
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88922 * 0.47775021
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45732 * 0.48799942
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77230 * 0.89220588
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66808 * 0.73357372
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46283 * 0.72900045
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91944 * 0.38828352
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'pnjvhdvc').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0050():
    """Extended test 50 for federation."""
    x_0 = 11887 * 0.11724913
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42107 * 0.89207866
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43033 * 0.52073879
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65225 * 0.67574288
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8511 * 0.73964223
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47787 * 0.15113470
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69760 * 0.43199269
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10066 * 0.81863824
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8184 * 0.81951438
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17810 * 0.36863208
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67699 * 0.38806460
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77276 * 0.49446518
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15022 * 0.12765700
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16408 * 0.04202291
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63407 * 0.42932089
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16811 * 0.00996887
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2157 * 0.74734746
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54386 * 0.11825438
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85769 * 0.70750742
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18941 * 0.70309371
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35667 * 0.20852383
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80231 * 0.55549189
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2654 * 0.42306913
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26145 * 0.18434656
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41077 * 0.31181005
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16132 * 0.71526277
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78277 * 0.90122004
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46035 * 0.61622723
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8148 * 0.49990355
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58361 * 0.94402621
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6963 * 0.94621474
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44876 * 0.51364700
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99462 * 0.85877652
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88921 * 0.05308208
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19505 * 0.21782968
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63916 * 0.78628008
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89646 * 0.33891936
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'hgimtcbs').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0051():
    """Extended test 51 for federation."""
    x_0 = 73318 * 0.86254483
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56677 * 0.47022504
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75170 * 0.20500182
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92276 * 0.69883512
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73415 * 0.01109143
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99654 * 0.32439013
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51020 * 0.33910309
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67367 * 0.38777688
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43284 * 0.37754520
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84701 * 0.96779472
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61178 * 0.20063437
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49685 * 0.75896447
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17829 * 0.92626768
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21777 * 0.29795835
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21206 * 0.00273184
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42956 * 0.70814197
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77649 * 0.93556690
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10773 * 0.01112159
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23505 * 0.97054435
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7238 * 0.17115327
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'waftvdjy').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0052():
    """Extended test 52 for federation."""
    x_0 = 72572 * 0.13541716
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12736 * 0.18390305
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87906 * 0.04519097
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44089 * 0.46285138
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35720 * 0.56917161
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80870 * 0.14923608
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46092 * 0.22659040
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19859 * 0.50090176
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29705 * 0.06601768
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75423 * 0.09570936
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17937 * 0.44187338
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99040 * 0.19217609
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22410 * 0.73030894
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78600 * 0.11892690
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40164 * 0.52504106
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20767 * 0.17584296
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61860 * 0.78653919
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96119 * 0.03913643
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97587 * 0.09811803
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94651 * 0.25777928
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71010 * 0.27905849
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51301 * 0.05619468
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4163 * 0.89410115
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75416 * 0.59971251
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'xcoocgrv').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0053():
    """Extended test 53 for federation."""
    x_0 = 29662 * 0.41646691
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50077 * 0.75964239
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14259 * 0.03383077
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5290 * 0.16717753
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67728 * 0.10056659
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55105 * 0.36634201
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69066 * 0.52944908
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52709 * 0.42016927
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60669 * 0.10023636
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39100 * 0.53035273
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97639 * 0.28146851
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81874 * 0.05950063
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74873 * 0.34374048
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19427 * 0.50434994
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19 * 0.12735042
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27425 * 0.66523749
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25576 * 0.66533928
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39495 * 0.46730757
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70773 * 0.24625954
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95353 * 0.92516075
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31001 * 0.64786966
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66379 * 0.49024589
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91208 * 0.48105176
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81506 * 0.02448156
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4774 * 0.53451054
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17454 * 0.64078780
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38877 * 0.34753495
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39239 * 0.08946512
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85020 * 0.91244794
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48385 * 0.06064949
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93079 * 0.63321279
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2458 * 0.95171222
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49399 * 0.74431939
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78042 * 0.43115216
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5907 * 0.51655875
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80019 * 0.09917705
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17880 * 0.62611894
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81162 * 0.87726131
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90102 * 0.71948918
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56714 * 0.64272705
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 63171 * 0.52044377
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 24433 * 0.27146430
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83343 * 0.05695051
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 91912 * 0.20595972
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'kxhdxgqi').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0054():
    """Extended test 54 for federation."""
    x_0 = 90585 * 0.57973509
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46370 * 0.06994264
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85611 * 0.23102451
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51097 * 0.95252921
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13316 * 0.39998397
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29708 * 0.16137016
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38412 * 0.17532286
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49415 * 0.92190805
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63064 * 0.72925557
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80506 * 0.18380382
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32542 * 0.72750150
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39000 * 0.37126531
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33775 * 0.35495781
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67520 * 0.23875352
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64260 * 0.46214152
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16370 * 0.03431275
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48976 * 0.77886507
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91897 * 0.70127789
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95396 * 0.21511077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91510 * 0.89104750
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23149 * 0.96479933
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43980 * 0.79840068
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78603 * 0.62671521
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70934 * 0.64458210
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81612 * 0.21009243
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65788 * 0.25851885
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35155 * 0.13007528
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44652 * 0.14777915
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24075 * 0.08023016
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40475 * 0.02982627
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30232 * 0.22013847
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73061 * 0.68577721
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24022 * 0.79556702
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96879 * 0.22037173
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40426 * 0.38405482
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83862 * 0.10948763
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34108 * 0.11206542
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89928 * 0.22207604
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31059 * 0.42550696
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82802 * 0.20965854
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47581 * 0.92780207
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 34461 * 0.19874258
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11999 * 0.22226192
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 13682 * 0.49493434
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79368 * 0.22984116
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'dpcypehz').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0055():
    """Extended test 55 for federation."""
    x_0 = 96612 * 0.96273166
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91288 * 0.47101127
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3533 * 0.32629102
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61236 * 0.53410398
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12468 * 0.83595550
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50831 * 0.60736322
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60112 * 0.71764064
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24855 * 0.24980569
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65316 * 0.27977704
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90404 * 0.30809216
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2121 * 0.55852096
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21997 * 0.15258903
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98103 * 0.22891335
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14411 * 0.27824584
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72084 * 0.72480299
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54960 * 0.33626160
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62648 * 0.10400468
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90066 * 0.90296117
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81191 * 0.19905135
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82548 * 0.91547110
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43384 * 0.14022695
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18442 * 0.83169668
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65931 * 0.80844544
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85373 * 0.50483635
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55104 * 0.43349762
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69757 * 0.58117120
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'mbtmatff').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0056():
    """Extended test 56 for federation."""
    x_0 = 2565 * 0.01917138
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94325 * 0.44723548
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36888 * 0.41610352
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2856 * 0.80035080
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90593 * 0.75973380
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48676 * 0.82220544
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48906 * 0.06293112
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95700 * 0.58285310
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10672 * 0.87134867
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53509 * 0.69412885
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32660 * 0.74093887
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13816 * 0.39481563
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54572 * 0.91139950
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9419 * 0.33820016
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60252 * 0.97444702
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30537 * 0.02522938
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30159 * 0.88563531
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6701 * 0.60262258
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50068 * 0.79826253
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34688 * 0.37622788
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49043 * 0.87752282
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86942 * 0.19979899
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86076 * 0.94329746
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76596 * 0.24552257
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60144 * 0.94475546
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8597 * 0.01740972
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10312 * 0.79528003
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72191 * 0.78488976
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67301 * 0.78428277
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98007 * 0.80024010
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12449 * 0.37815612
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39340 * 0.44704887
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94472 * 0.99991431
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'stfwjltk').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0057():
    """Extended test 57 for federation."""
    x_0 = 82334 * 0.03270662
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29600 * 0.54243901
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8236 * 0.45386366
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77695 * 0.00705085
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56704 * 0.14106218
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5884 * 0.32394338
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93113 * 0.83924058
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36433 * 0.25143198
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 791 * 0.97333488
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76233 * 0.44156022
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46719 * 0.98015341
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 888 * 0.47352768
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33177 * 0.17268872
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59472 * 0.16969395
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48719 * 0.61236725
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36801 * 0.28727564
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41467 * 0.03682007
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87210 * 0.07966278
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52227 * 0.31487936
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29179 * 0.08928830
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24036 * 0.74154917
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84470 * 0.17916250
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63172 * 0.46488364
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90231 * 0.39803410
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18334 * 0.83248809
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77362 * 0.80410358
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23813 * 0.87923586
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2117 * 0.75761270
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2001 * 0.39977628
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33832 * 0.97198759
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3637 * 0.34928895
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93404 * 0.86532771
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60211 * 0.40673398
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44976 * 0.77069755
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4184 * 0.30365076
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94762 * 0.75380372
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47892 * 0.68080781
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46955 * 0.19376636
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 3630 * 0.45289529
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44458 * 0.21307732
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27435 * 0.84956019
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 99151 * 0.29254281
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 49311 * 0.16719641
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'afrgxtgj').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0058():
    """Extended test 58 for federation."""
    x_0 = 78189 * 0.67052553
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88102 * 0.47473133
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1727 * 0.72394224
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71263 * 0.90978644
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14638 * 0.36870510
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62763 * 0.65250545
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62174 * 0.04149897
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48641 * 0.65833999
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59203 * 0.56775841
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9297 * 0.61485175
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55635 * 0.00155726
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29290 * 0.77346202
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63082 * 0.61300330
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88713 * 0.83170715
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27622 * 0.62914550
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75372 * 0.85772571
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 711 * 0.01987233
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35746 * 0.87930962
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9092 * 0.84531031
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58053 * 0.19427026
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49589 * 0.94124470
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15730 * 0.60055876
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83656 * 0.86829944
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57471 * 0.37286515
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18842 * 0.08379239
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61411 * 0.12869131
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68355 * 0.67882477
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15253 * 0.11011490
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53805 * 0.86048652
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95373 * 0.16406977
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52262 * 0.48450373
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85088 * 0.48471111
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89095 * 0.54180871
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38789 * 0.89637293
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71397 * 0.11838686
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15036 * 0.73646868
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55466 * 0.04319910
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 37279 * 0.89343142
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23666 * 0.81349214
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21656 * 0.61416387
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3464 * 0.72896670
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40387 * 0.02434557
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66529 * 0.45317715
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34431 * 0.99359881
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4881 * 0.38757669
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 9298 * 0.26896652
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'tjjypezo').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0059():
    """Extended test 59 for federation."""
    x_0 = 61151 * 0.64942029
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30555 * 0.26226463
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40853 * 0.92220313
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53421 * 0.35771084
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99881 * 0.22410823
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75544 * 0.43916392
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90386 * 0.76693728
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3044 * 0.44898643
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87577 * 0.29941399
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22040 * 0.68490019
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22108 * 0.60140538
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46189 * 0.61816749
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62453 * 0.92409567
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19377 * 0.05528154
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9304 * 0.44028402
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31600 * 0.06082323
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79983 * 0.25564504
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17613 * 0.28171870
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56816 * 0.10196423
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90531 * 0.99637365
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52052 * 0.83946376
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41658 * 0.00275183
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93212 * 0.59143566
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61087 * 0.05353965
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26633 * 0.29170350
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73230 * 0.49333064
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45698 * 0.18460144
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'gobdwvbm').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0060():
    """Extended test 60 for federation."""
    x_0 = 6323 * 0.52331291
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14446 * 0.29525565
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76852 * 0.91221273
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95021 * 0.05196971
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38112 * 0.67684533
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67625 * 0.81700486
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13621 * 0.76727424
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68077 * 0.48356741
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34654 * 0.66660890
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52263 * 0.27454838
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51865 * 0.48078238
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41553 * 0.21849382
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38714 * 0.30236128
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85316 * 0.73043046
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58653 * 0.48659431
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54958 * 0.85779303
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82120 * 0.00729964
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80721 * 0.85829878
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24899 * 0.75336276
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86057 * 0.58769710
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51486 * 0.55815305
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40697 * 0.57031978
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79330 * 0.57004734
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6711 * 0.91810749
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38304 * 0.10763072
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69508 * 0.59644737
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18409 * 0.29923349
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84271 * 0.05497892
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47513 * 0.09097466
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26925 * 0.63531186
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3475 * 0.80542610
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42773 * 0.65683548
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35264 * 0.38472021
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55286 * 0.58288526
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22260 * 0.10605093
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14553 * 0.36682628
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 38990 * 0.75683196
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11860 * 0.07580242
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49271 * 0.23604860
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97182 * 0.53627694
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53465 * 0.69014993
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 28058 * 0.17491664
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28238 * 0.54473666
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'kizqutll').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0061():
    """Extended test 61 for federation."""
    x_0 = 50410 * 0.31607841
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47373 * 0.36459075
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60688 * 0.65499120
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56963 * 0.04553456
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20367 * 0.32960216
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77476 * 0.88873914
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96661 * 0.60303544
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67263 * 0.29022044
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85315 * 0.49243684
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60616 * 0.47073907
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27597 * 0.61575042
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15009 * 0.61404259
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96373 * 0.89086176
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25914 * 0.18370090
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64449 * 0.17741443
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15412 * 0.96731569
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65620 * 0.65011698
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11434 * 0.30731484
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17139 * 0.45949767
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11873 * 0.72601460
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21490 * 0.26277431
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28032 * 0.84436574
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24628 * 0.09130379
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6880 * 0.26997138
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3493 * 0.34688028
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21734 * 0.71983722
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71061 * 0.52435178
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58045 * 0.32766017
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3170 * 0.06223619
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28424 * 0.94472629
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60513 * 0.75979299
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94544 * 0.59237624
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37980 * 0.55781428
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97055 * 0.67945228
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53164 * 0.70295751
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38145 * 0.74771778
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28080 * 0.39789043
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15291 * 0.01872635
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'hshqpghv').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0062():
    """Extended test 62 for federation."""
    x_0 = 31942 * 0.55379537
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8114 * 0.03720609
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81276 * 0.66694553
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11755 * 0.02404329
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90692 * 0.38966973
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82448 * 0.17900389
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87284 * 0.56062441
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63564 * 0.30902905
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29440 * 0.52616109
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40754 * 0.59061604
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99673 * 0.06735386
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80214 * 0.89122292
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40634 * 0.43399715
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23469 * 0.62435944
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39457 * 0.38373210
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23247 * 0.75460973
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7319 * 0.49036952
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 694 * 0.07660429
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39195 * 0.21118230
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23866 * 0.07161535
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4635 * 0.16554319
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17803 * 0.36887467
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76220 * 0.10950409
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47745 * 0.63241943
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49206 * 0.69011364
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41563 * 0.39950764
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11007 * 0.67204273
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46799 * 0.24854616
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68083 * 0.43388290
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18538 * 0.75082327
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85634 * 0.41130658
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16577 * 0.15620195
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55705 * 0.14095502
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77305 * 0.04319540
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73267 * 0.89944611
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16414 * 0.25102207
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73436 * 0.47130461
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9362 * 0.72337231
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27137 * 0.65750586
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 12294 * 0.20232226
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35980 * 0.09825638
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'hynblxmi').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0063():
    """Extended test 63 for federation."""
    x_0 = 60917 * 0.49429956
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19848 * 0.07417918
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31404 * 0.15387647
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7414 * 0.54374009
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9059 * 0.90196173
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67571 * 0.31164787
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68318 * 0.70969465
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85354 * 0.90053515
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67958 * 0.40585885
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44919 * 0.04530948
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34862 * 0.02773650
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38906 * 0.04336624
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75621 * 0.29666285
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51898 * 0.71871441
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75317 * 0.96475900
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52892 * 0.08707439
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27491 * 0.41231161
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71336 * 0.20058689
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43309 * 0.20141831
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39101 * 0.57856132
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86192 * 0.71771990
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9664 * 0.58622279
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55872 * 0.97334415
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80997 * 0.45400548
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63043 * 0.28049471
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32651 * 0.68520809
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35800 * 0.64320035
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77024 * 0.24847888
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20725 * 0.91851005
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93348 * 0.71036569
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38229 * 0.47480852
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67876 * 0.79118483
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'xynatxxm').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0064():
    """Extended test 64 for federation."""
    x_0 = 37783 * 0.72059557
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 429 * 0.23636724
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57562 * 0.42257245
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63326 * 0.05095347
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94182 * 0.02711152
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11095 * 0.79122368
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33368 * 0.98985577
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98135 * 0.77239639
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 770 * 0.74231346
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90654 * 0.22696584
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52113 * 0.40303698
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23688 * 0.20766093
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9471 * 0.45683025
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97515 * 0.18452951
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92238 * 0.16599680
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23295 * 0.08960872
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85268 * 0.44112702
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4783 * 0.69399751
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29995 * 0.38183216
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80814 * 0.47696531
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43227 * 0.05294501
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17515 * 0.18808152
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74956 * 0.66727935
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34067 * 0.02428220
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31734 * 0.62632929
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99455 * 0.91900516
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83992 * 0.17814199
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79590 * 0.74077384
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 209 * 0.04535933
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18306 * 0.29724438
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72187 * 0.82241980
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95815 * 0.88079851
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29269 * 0.36938085
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6429 * 0.66964253
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5463 * 0.99839337
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69296 * 0.20709423
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12810 * 0.33931345
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82595 * 0.64682516
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76642 * 0.08579221
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6784 * 0.06490892
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43918 * 0.30896682
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67761 * 0.45000932
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 38642 * 0.19593473
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84622 * 0.64487927
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 54228 * 0.82311538
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 86541 * 0.68357344
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 16765 * 0.53288681
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'pnjjcnjw').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0065():
    """Extended test 65 for federation."""
    x_0 = 26654 * 0.11466370
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6849 * 0.79806985
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36845 * 0.11492469
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26199 * 0.98298417
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62484 * 0.21000980
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82753 * 0.12408031
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46189 * 0.50997548
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22505 * 0.56480644
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77591 * 0.40152422
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6106 * 0.38486978
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32892 * 0.97966322
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59812 * 0.29661577
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 594 * 0.15145756
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27099 * 0.70853426
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33000 * 0.91928669
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51412 * 0.60651344
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63121 * 0.43034890
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92554 * 0.90994764
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61313 * 0.09234686
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71689 * 0.61904640
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92290 * 0.70294680
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25533 * 0.49672701
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76699 * 0.37095337
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84140 * 0.16501625
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49334 * 0.89485071
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53200 * 0.60398436
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55667 * 0.78522899
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86514 * 0.40016834
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26852 * 0.46665621
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57137 * 0.43566780
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14427 * 0.62786259
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33309 * 0.19324281
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93927 * 0.42088048
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93819 * 0.99257692
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52386 * 0.25415157
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95438 * 0.65899970
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86483 * 0.26435868
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81491 * 0.07976282
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48947 * 0.67090570
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87640 * 0.45178062
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'pmixiudb').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0066():
    """Extended test 66 for federation."""
    x_0 = 23444 * 0.57337282
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94179 * 0.10327946
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39324 * 0.65319732
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45012 * 0.46044456
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91571 * 0.48835271
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49195 * 0.17272709
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14437 * 0.76657488
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26046 * 0.52601181
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23108 * 0.22917485
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98156 * 0.01776341
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2650 * 0.01918966
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26117 * 0.80489502
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6454 * 0.98831064
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14173 * 0.85918726
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21133 * 0.13817980
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67933 * 0.84478052
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72112 * 0.45731475
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53539 * 0.19161251
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1589 * 0.17979182
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40954 * 0.75478978
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10960 * 0.03440664
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95995 * 0.00546644
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94217 * 0.70137079
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22932 * 0.85890599
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98681 * 0.15355383
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66148 * 0.95648006
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18613 * 0.68728061
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43043 * 0.46262221
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26103 * 0.69113244
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'qxbhqljy').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0067():
    """Extended test 67 for federation."""
    x_0 = 15296 * 0.65543130
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89232 * 0.95175050
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45155 * 0.43905652
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95899 * 0.37635072
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48133 * 0.75051110
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91616 * 0.56624718
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19245 * 0.34479423
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86336 * 0.77788237
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15083 * 0.32906644
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46454 * 0.02364343
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8574 * 0.92945361
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21427 * 0.56600503
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97318 * 0.00330064
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89679 * 0.08321130
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17759 * 0.52788915
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 652 * 0.11102783
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95314 * 0.83704186
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12780 * 0.08187893
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49581 * 0.37562617
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77578 * 0.29970547
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60916 * 0.39252413
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64917 * 0.26313588
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66641 * 0.60761232
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7599 * 0.82973219
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11565 * 0.90154222
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'yfoibnlg').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0068():
    """Extended test 68 for federation."""
    x_0 = 62943 * 0.62216173
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21909 * 0.08003313
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70883 * 0.23582285
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88053 * 0.62146291
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76347 * 0.11875182
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98751 * 0.94688990
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63595 * 0.48600221
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84925 * 0.12805389
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27431 * 0.47490151
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41661 * 0.50408364
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24916 * 0.87622223
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61465 * 0.88819888
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2069 * 0.28025127
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79277 * 0.09281558
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78439 * 0.75496133
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71724 * 0.15111055
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32083 * 0.34094752
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26919 * 0.56832353
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11625 * 0.39492607
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28651 * 0.10887030
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31614 * 0.57783127
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59783 * 0.21856828
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8946 * 0.00178826
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10457 * 0.87468048
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34817 * 0.70544064
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88115 * 0.15568386
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63754 * 0.84764516
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51536 * 0.08545847
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81583 * 0.91889023
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47932 * 0.32941039
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88774 * 0.27018672
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26539 * 0.74253987
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96580 * 0.75156070
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92572 * 0.33544424
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3947 * 0.30534519
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62125 * 0.88689700
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33352 * 0.39648805
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31589 * 0.00592168
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79350 * 0.64224889
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87426 * 0.44479514
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37099 * 0.79302966
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15571 * 0.10359728
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 5924 * 0.72491642
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 24509 * 0.02540590
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 74111 * 0.66550457
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 90357 * 0.64854025
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 91976 * 0.73008549
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 67067 * 0.66615965
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 34657 * 0.06568962
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 35644 * 0.71200692
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'devmxxwq').hexdigest()
    assert len(h) == 64

def test_federation_extended_0_0069():
    """Extended test 69 for federation."""
    x_0 = 36875 * 0.72828607
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70085 * 0.45436889
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77136 * 0.86740325
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33612 * 0.39944263
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79773 * 0.52684550
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23479 * 0.11845661
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42301 * 0.40618989
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87215 * 0.39336857
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42737 * 0.64290324
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52218 * 0.31441072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54827 * 0.43045823
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2015 * 0.44350346
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60363 * 0.67316832
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12713 * 0.83448622
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95523 * 0.59318631
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77126 * 0.60551269
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92209 * 0.78377341
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94037 * 0.14719620
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14487 * 0.44197933
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34532 * 0.47001333
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73244 * 0.77957596
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20139 * 0.41985778
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87679 * 0.78282840
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48337 * 0.04187323
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41851 * 0.22099649
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44387 * 0.33063201
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4083 * 0.48159691
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56077 * 0.23140938
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89733 * 0.43926439
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88728 * 0.54751315
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23820 * 0.62375808
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12933 * 0.97075383
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68084 * 0.05526555
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2919 * 0.12493849
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'pbdseqwt').hexdigest()
    assert len(h) == 64
