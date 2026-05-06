"""Extended tests for transcoding suite 0."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_transcoding_extended_0_0000():
    """Extended test 0 for transcoding."""
    x_0 = 60118 * 0.08182448
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98762 * 0.37207752
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62903 * 0.15608533
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39209 * 0.01998325
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54188 * 0.21847118
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5771 * 0.77824314
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47100 * 0.84227340
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9365 * 0.74160084
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52562 * 0.54078459
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90908 * 0.17653695
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15443 * 0.89280916
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85863 * 0.07620731
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66681 * 0.32651819
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56725 * 0.04620962
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10477 * 0.79601798
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83406 * 0.54414301
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89966 * 0.91338699
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38471 * 0.58422812
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27733 * 0.39922804
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50950 * 0.82630656
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74206 * 0.33865100
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'bzhjazxj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0001():
    """Extended test 1 for transcoding."""
    x_0 = 23999 * 0.20284941
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14886 * 0.50330684
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65896 * 0.29760248
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46744 * 0.41699487
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15033 * 0.27785380
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8592 * 0.95740077
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75365 * 0.12008468
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91052 * 0.71411626
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97196 * 0.85164391
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 663 * 0.85909667
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64259 * 0.66975739
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24086 * 0.99353574
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17513 * 0.88370992
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58357 * 0.93205204
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96734 * 0.82834305
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61728 * 0.91626270
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47746 * 0.06232000
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2418 * 0.93430568
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89298 * 0.47561560
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13033 * 0.87161945
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48940 * 0.03905751
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28387 * 0.10233381
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58037 * 0.94031536
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74369 * 0.74505260
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85674 * 0.05824510
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42126 * 0.24269040
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76850 * 0.95398481
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70842 * 0.15414307
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'hudfjcgb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0002():
    """Extended test 2 for transcoding."""
    x_0 = 11252 * 0.43940755
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20642 * 0.66029170
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72785 * 0.75253148
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92348 * 0.58416524
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9589 * 0.09222021
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40253 * 0.89164917
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10759 * 0.31717604
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36717 * 0.60306253
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73025 * 0.17523409
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81770 * 0.02615971
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11298 * 0.23358797
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69438 * 0.63172540
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90714 * 0.03489701
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25386 * 0.33980777
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46339 * 0.46594881
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3914 * 0.70356445
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86271 * 0.71373705
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16320 * 0.25888618
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66527 * 0.15117109
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8627 * 0.62251269
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25842 * 0.51433856
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32899 * 0.59052978
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21469 * 0.35186821
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25698 * 0.76999012
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86471 * 0.80513714
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21982 * 0.79489027
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13887 * 0.01492419
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61926 * 0.32963540
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49755 * 0.06378200
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36076 * 0.33621256
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1474 * 0.41870746
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37488 * 0.50738569
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68912 * 0.48813582
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47491 * 0.50374414
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31076 * 0.56944756
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8280 * 0.43685940
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49415 * 0.66072223
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6332 * 0.36630954
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63993 * 0.58670315
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24700 * 0.93519613
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'trseqheo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0003():
    """Extended test 3 for transcoding."""
    x_0 = 10430 * 0.47936585
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78657 * 0.15914173
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52157 * 0.79744941
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96524 * 0.49622470
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62927 * 0.62623637
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19285 * 0.51291136
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12235 * 0.10707408
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29988 * 0.58284210
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94092 * 0.56438290
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87720 * 0.68826968
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83995 * 0.94688040
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32856 * 0.45805765
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79109 * 0.80130139
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39401 * 0.75672772
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79971 * 0.08992008
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17093 * 0.69375110
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54948 * 0.17863053
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52617 * 0.05675362
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10809 * 0.15732405
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44891 * 0.43550860
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62643 * 0.72187429
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91917 * 0.89916715
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63469 * 0.35046873
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27200 * 0.89990418
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23099 * 0.98973978
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61515 * 0.60132736
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98690 * 0.73989514
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71459 * 0.83299194
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21798 * 0.46693966
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87025 * 0.02590781
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3635 * 0.68300668
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51670 * 0.18208675
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87456 * 0.08481443
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43338 * 0.01734955
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 658 * 0.37973435
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52374 * 0.27454499
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95354 * 0.94835217
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39209 * 0.73867780
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'xylasont').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0004():
    """Extended test 4 for transcoding."""
    x_0 = 79006 * 0.47130232
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71364 * 0.08127622
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62688 * 0.68486305
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89664 * 0.27589204
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3496 * 0.81451409
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49718 * 0.22521860
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24203 * 0.22087445
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17010 * 0.69835248
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43894 * 0.66169284
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47859 * 0.19839135
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11844 * 0.53187583
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61200 * 0.74205274
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29418 * 0.61304104
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90898 * 0.17550104
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20584 * 0.44593181
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12905 * 0.25730565
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85383 * 0.67744090
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81131 * 0.69750920
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74997 * 0.23307984
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78563 * 0.37860935
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84999 * 0.70633353
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30218 * 0.88470135
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31413 * 0.39298725
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89107 * 0.89758534
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'lgzxcado').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0005():
    """Extended test 5 for transcoding."""
    x_0 = 48716 * 0.64395102
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23069 * 0.89845952
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80707 * 0.46343257
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58853 * 0.34190754
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1762 * 0.57851004
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2217 * 0.22231922
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21953 * 0.44816187
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96461 * 0.60737656
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19596 * 0.76016475
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60714 * 0.82954522
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54162 * 0.38537925
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98842 * 0.38400495
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13771 * 0.77779502
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30029 * 0.06688610
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92483 * 0.47823154
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18555 * 0.13739612
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81365 * 0.91786442
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98520 * 0.80630816
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44713 * 0.78790058
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91059 * 0.65754272
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41046 * 0.66716286
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22991 * 0.20141063
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20626 * 0.33107999
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79658 * 0.08198505
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58185 * 0.06796118
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31542 * 0.06891973
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62580 * 0.54819271
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5935 * 0.88245250
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'hycllnqf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0006():
    """Extended test 6 for transcoding."""
    x_0 = 29963 * 0.81315853
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 270 * 0.86236218
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98806 * 0.79013421
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65054 * 0.88195377
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73949 * 0.54453768
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97591 * 0.93621892
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73832 * 0.82294471
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55800 * 0.54800819
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10951 * 0.74561681
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89915 * 0.48921329
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57319 * 0.26189475
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19376 * 0.18823507
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73882 * 0.92890845
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55422 * 0.67099845
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57581 * 0.17364454
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28276 * 0.72663604
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17013 * 0.83543384
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73906 * 0.19270177
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88436 * 0.08908797
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49822 * 0.87300403
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50526 * 0.30831475
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71637 * 0.87495748
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24995 * 0.20487103
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25145 * 0.68770583
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71815 * 0.57578039
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46104 * 0.04796569
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57220 * 0.91112993
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64306 * 0.31688106
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45117 * 0.03272895
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14450 * 0.54508038
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74806 * 0.23586753
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27511 * 0.94377915
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62325 * 0.04699351
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72790 * 0.99083923
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50581 * 0.96806989
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22415 * 0.82551990
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17590 * 0.58132520
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43349 * 0.50185544
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23390 * 0.27915661
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59181 * 0.98838164
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18302 * 0.10825327
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53264 * 0.88362474
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 21334 * 0.77442083
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 31727 * 0.86237097
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 65440 * 0.78174285
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 33802 * 0.18395788
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 35980 * 0.15736310
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 33287 * 0.95538464
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 32410 * 0.64389275
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 81725 * 0.80341409
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'vyaowekx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0007():
    """Extended test 7 for transcoding."""
    x_0 = 53826 * 0.61817029
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40470 * 0.47347860
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45935 * 0.47399995
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5523 * 0.16889784
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65472 * 0.00899462
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79650 * 0.74264714
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80782 * 0.87369451
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84431 * 0.41125180
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84678 * 0.09124669
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50968 * 0.97972000
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96703 * 0.88714178
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68211 * 0.22117854
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16432 * 0.73525200
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64544 * 0.93274650
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 750 * 0.21497525
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48881 * 0.34426744
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7277 * 0.18062698
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38466 * 0.27808821
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7544 * 0.18198301
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18360 * 0.73085040
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40465 * 0.47759786
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18280 * 0.91905300
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9265 * 0.05061263
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29088 * 0.41496853
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34277 * 0.27765307
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23723 * 0.11924452
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4924 * 0.52617211
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58404 * 0.77727621
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84329 * 0.90506656
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51218 * 0.68540196
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82547 * 0.60435728
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9492 * 0.46220922
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76047 * 0.14830947
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7271 * 0.55057370
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73743 * 0.53348490
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75991 * 0.16648850
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64799 * 0.96565476
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82064 * 0.36784051
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67296 * 0.07732089
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18679 * 0.85514292
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62003 * 0.69563853
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74997 * 0.44249969
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 21311 * 0.03855079
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 43715 * 0.71752636
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17764 * 0.08269556
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 78245 * 0.60675350
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'lrreogbj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0008():
    """Extended test 8 for transcoding."""
    x_0 = 21679 * 0.92615675
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65497 * 0.50889340
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9612 * 0.26040580
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73124 * 0.66235201
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49585 * 0.96787830
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92043 * 0.76237579
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38639 * 0.09633425
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92705 * 0.66269661
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27682 * 0.98631524
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84427 * 0.23002468
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31050 * 0.70463847
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79907 * 0.17086387
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81249 * 0.69390581
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89295 * 0.52513777
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99615 * 0.72710681
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17343 * 0.25322585
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88053 * 0.23901533
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81812 * 0.21894993
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11863 * 0.50010043
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73513 * 0.26983574
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95243 * 0.69847916
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81773 * 0.26875012
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43741 * 0.34645919
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61453 * 0.54160271
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76757 * 0.04074772
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55976 * 0.58870847
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45775 * 0.89751954
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2920 * 0.77761474
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92558 * 0.41888041
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32010 * 0.17355240
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ljpmtdfd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0009():
    """Extended test 9 for transcoding."""
    x_0 = 19470 * 0.03466463
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65109 * 0.84311436
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94459 * 0.95344290
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22447 * 0.88688309
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49697 * 0.50874140
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83962 * 0.52260314
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76845 * 0.94833249
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7283 * 0.57720386
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64328 * 0.08670973
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12025 * 0.58551440
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35518 * 0.95762094
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84499 * 0.79384074
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91128 * 0.11734624
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85588 * 0.65671855
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70484 * 0.52446628
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74712 * 0.93864995
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39677 * 0.39170333
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24821 * 0.90979327
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77948 * 0.89695823
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83320 * 0.42185122
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33066 * 0.24100592
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93854 * 0.50130010
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'hlhfbzrs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0010():
    """Extended test 10 for transcoding."""
    x_0 = 18733 * 0.90550334
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99057 * 0.24497697
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8831 * 0.60600400
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10129 * 0.20816155
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71385 * 0.61806004
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98775 * 0.07916668
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72894 * 0.03242621
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32124 * 0.07600980
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12087 * 0.04480339
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99802 * 0.55449446
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3297 * 0.01284996
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45147 * 0.75266614
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27146 * 0.24896768
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71625 * 0.79794228
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32911 * 0.24261500
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89900 * 0.60006634
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92480 * 0.27725597
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73622 * 0.71910266
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20267 * 0.49489186
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23383 * 0.27242603
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75302 * 0.03428420
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99596 * 0.13712279
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73627 * 0.87175155
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55861 * 0.56527358
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47794 * 0.84956926
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36511 * 0.87606520
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4663 * 0.36846201
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32667 * 0.30374906
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86140 * 0.80355512
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1261 * 0.70431719
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20400 * 0.89700193
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52851 * 0.81218130
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28079 * 0.92247683
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83995 * 0.03155141
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lcquzdcd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0011():
    """Extended test 11 for transcoding."""
    x_0 = 7492 * 0.27837857
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63316 * 0.80084271
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2454 * 0.11318499
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70846 * 0.20247937
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71037 * 0.97427262
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31851 * 0.55218880
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85033 * 0.86147035
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94862 * 0.62518183
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81953 * 0.71836420
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39945 * 0.12752864
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8301 * 0.39188795
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65661 * 0.61575284
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40136 * 0.95173304
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71696 * 0.13336407
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10017 * 0.07427259
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90305 * 0.59041193
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23034 * 0.40540432
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45161 * 0.25938553
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22183 * 0.58554789
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52427 * 0.15054472
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20346 * 0.66559276
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51762 * 0.45895203
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50335 * 0.80287165
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54155 * 0.34658424
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49773 * 0.49898256
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36266 * 0.70030026
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96212 * 0.83715158
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83561 * 0.59551227
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38641 * 0.95693018
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23296 * 0.78864617
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16216 * 0.81498430
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61576 * 0.01230714
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54452 * 0.62843397
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21841 * 0.91544084
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44568 * 0.28740324
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85596 * 0.41471761
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94531 * 0.57519789
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13908 * 0.30032556
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35542 * 0.27761892
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47303 * 0.55835414
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 50258 * 0.09371555
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71456 * 0.61577175
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74825 * 0.59915201
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 37374 * 0.74917104
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92775 * 0.03784522
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 19248 * 0.39905742
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'dlbagqbh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0012():
    """Extended test 12 for transcoding."""
    x_0 = 71649 * 0.06230402
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59769 * 0.08855369
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84700 * 0.63269935
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60044 * 0.30463213
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6658 * 0.64274510
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18642 * 0.23747291
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74418 * 0.78813358
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72061 * 0.04418455
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9562 * 0.60129712
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27483 * 0.73170790
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13065 * 0.96476366
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17585 * 0.32263624
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73743 * 0.78845038
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 490 * 0.32471985
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85668 * 0.20294524
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63831 * 0.89630917
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73376 * 0.89586637
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29404 * 0.35401849
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43399 * 0.00034552
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2753 * 0.28940855
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63254 * 0.44991644
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40151 * 0.73103939
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92048 * 0.96437338
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7755 * 0.76072946
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46754 * 0.22234082
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20439 * 0.95258546
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78690 * 0.34972799
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24249 * 0.59214263
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73062 * 0.60463612
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78702 * 0.32219328
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57642 * 0.33270971
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57694 * 0.28556106
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11345 * 0.45301441
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58950 * 0.86541327
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35835 * 0.40695968
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66377 * 0.49649790
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'uupsicyn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0013():
    """Extended test 13 for transcoding."""
    x_0 = 53130 * 0.93044052
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33623 * 0.71743799
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18306 * 0.18271815
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49118 * 0.91215236
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35196 * 0.07606963
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92299 * 0.59101947
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42254 * 0.78048229
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61427 * 0.29900031
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37039 * 0.29065056
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86429 * 0.20966966
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43619 * 0.27691567
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36991 * 0.08340686
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38229 * 0.54016614
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81389 * 0.68205650
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75731 * 0.44417028
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44150 * 0.32257633
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54640 * 0.36578163
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13032 * 0.31929537
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73463 * 0.71617116
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82234 * 0.24474768
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90592 * 0.73299595
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93110 * 0.47228031
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1656 * 0.44087692
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48424 * 0.33136174
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53683 * 0.37515610
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60830 * 0.18537958
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43573 * 0.70571982
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42569 * 0.06797768
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94365 * 0.60861504
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16064 * 0.15687611
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82436 * 0.20677905
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15301 * 0.97655998
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26410 * 0.65175169
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57603 * 0.91839478
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71831 * 0.27517953
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49408 * 0.85722874
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32834 * 0.44576510
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 14435 * 0.96909930
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29180 * 0.05368217
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88665 * 0.65625478
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 96279 * 0.86961936
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 94416 * 0.45139504
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18049 * 0.66704417
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 62792 * 0.93542658
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 74795 * 0.71138136
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'qerrbuzh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0014():
    """Extended test 14 for transcoding."""
    x_0 = 31844 * 0.59636995
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55079 * 0.84148341
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78592 * 0.27183451
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65827 * 0.41580531
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79657 * 0.86528906
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36457 * 0.94426140
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44555 * 0.45606094
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71815 * 0.47684553
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32808 * 0.68530854
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80593 * 0.48005056
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79728 * 0.40665420
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3292 * 0.67935895
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20428 * 0.16166500
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68329 * 0.47614932
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22507 * 0.35630079
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14361 * 0.30362575
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49276 * 0.57299927
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63731 * 0.23114399
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16375 * 0.46029273
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18094 * 0.35205389
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58503 * 0.85054979
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46286 * 0.75256032
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2054 * 0.93721877
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62144 * 0.81980760
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6612 * 0.15357535
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'kjkbhrjw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0015():
    """Extended test 15 for transcoding."""
    x_0 = 93882 * 0.42088589
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96023 * 0.54307968
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56414 * 0.68253311
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93795 * 0.74254585
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83897 * 0.55366191
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56411 * 0.29486581
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71297 * 0.90178491
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4538 * 0.77550531
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1195 * 0.36114713
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99727 * 0.99091627
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27451 * 0.22610103
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37832 * 0.69069690
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25752 * 0.27844261
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11866 * 0.72878116
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23147 * 0.78830149
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79149 * 0.23159521
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17683 * 0.64508982
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65232 * 0.58428183
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69966 * 0.47086054
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50117 * 0.98629824
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39755 * 0.24965115
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'mclmyshb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0016():
    """Extended test 16 for transcoding."""
    x_0 = 84929 * 0.52734401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69042 * 0.83785438
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80996 * 0.57652056
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64756 * 0.81882884
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23682 * 0.28055102
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56380 * 0.59282885
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43182 * 0.83954183
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38848 * 0.11643543
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51637 * 0.89855230
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40374 * 0.94594799
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53116 * 0.43048839
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57299 * 0.56070821
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40889 * 0.51623887
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86928 * 0.20824029
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28080 * 0.26208767
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74065 * 0.63937493
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17527 * 0.96641018
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36599 * 0.81141064
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86380 * 0.77903498
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29346 * 0.09744584
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59495 * 0.94902453
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29413 * 0.10655461
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91468 * 0.41352714
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45705 * 0.93647674
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8698 * 0.52212605
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54229 * 0.89484846
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52028 * 0.67829583
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36468 * 0.71780147
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3708 * 0.96178019
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30087 * 0.08390065
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20241 * 0.61041640
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40857 * 0.70841875
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33492 * 0.16303122
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42552 * 0.05967014
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36017 * 0.45469065
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65560 * 0.72211646
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47696 * 0.88400916
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30899 * 0.89851007
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23082 * 0.70489024
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43611 * 0.66150546
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62397 * 0.70857267
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 90806 * 0.86883029
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'yehhhdsg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0017():
    """Extended test 17 for transcoding."""
    x_0 = 31589 * 0.96489417
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31234 * 0.23298106
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39377 * 0.62443640
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47197 * 0.41501710
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48843 * 0.37251972
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13811 * 0.06305554
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74347 * 0.43959656
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47445 * 0.53775704
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93393 * 0.76976757
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43597 * 0.30222887
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9821 * 0.33955337
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48023 * 0.67141999
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39619 * 0.46332968
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4330 * 0.36323915
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10200 * 0.23841977
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85958 * 0.16454205
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83385 * 0.71449440
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90932 * 0.92774961
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78651 * 0.71694467
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96205 * 0.77948976
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21569 * 0.56188330
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38271 * 0.27261256
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45937 * 0.32168494
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27893 * 0.90757007
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89954 * 0.16074690
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'uqamrjhx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0018():
    """Extended test 18 for transcoding."""
    x_0 = 65811 * 0.63951893
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1110 * 0.92668642
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21650 * 0.84642318
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20696 * 0.43446808
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33467 * 0.52411120
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68620 * 0.37050240
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39618 * 0.42109214
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66036 * 0.81696712
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40814 * 0.82081701
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63595 * 0.71185492
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9636 * 0.62957387
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35892 * 0.28334080
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64920 * 0.87312339
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47242 * 0.87111343
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27720 * 0.36377923
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47785 * 0.96651856
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50629 * 0.76216577
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79120 * 0.55818672
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84140 * 0.10812291
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11548 * 0.23008383
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11340 * 0.98401891
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51420 * 0.98738489
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35901 * 0.44989971
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56954 * 0.69474746
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45687 * 0.57225214
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'feqbvfvb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0019():
    """Extended test 19 for transcoding."""
    x_0 = 13707 * 0.70086272
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11231 * 0.04065802
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7376 * 0.78402191
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88834 * 0.89111098
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25297 * 0.27202823
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32687 * 0.32666520
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43121 * 0.03770676
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53347 * 0.47897659
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64001 * 0.95567319
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5705 * 0.02224576
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23697 * 0.74795562
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33186 * 0.55805505
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40079 * 0.66508040
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52739 * 0.16153615
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92469 * 0.45039732
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65450 * 0.61791186
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27408 * 0.83900270
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16363 * 0.84175807
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4004 * 0.79891413
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50361 * 0.38109908
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52155 * 0.70329587
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4948 * 0.37862114
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27371 * 0.07858911
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74489 * 0.50834911
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35416 * 0.80547382
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67909 * 0.79172072
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54141 * 0.94851306
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58730 * 0.62614965
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21500 * 0.15216536
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10154 * 0.94197172
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99923 * 0.50597464
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81002 * 0.36060669
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51915 * 0.56466076
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77909 * 0.14942399
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18977 * 0.52079935
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5228 * 0.12874819
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29120 * 0.53992719
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77912 * 0.16406997
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77596 * 0.97250326
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 60940 * 0.85542393
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82505 * 0.57580881
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47604 * 0.05731390
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36077 * 0.91823009
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39331 * 0.81045943
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'gwkqbuex').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0020():
    """Extended test 20 for transcoding."""
    x_0 = 76104 * 0.67689070
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79446 * 0.31687168
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59969 * 0.66262210
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91710 * 0.34203596
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56591 * 0.45993691
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43934 * 0.34564680
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60085 * 0.47713607
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78724 * 0.49848822
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40853 * 0.42405454
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36667 * 0.30102738
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29079 * 0.24522143
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5311 * 0.32566666
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66287 * 0.77657405
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86824 * 0.04015782
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20650 * 0.31694776
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83728 * 0.24148040
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72788 * 0.70998855
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74476 * 0.24064904
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34546 * 0.78163303
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20828 * 0.03180598
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47933 * 0.92230737
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7735 * 0.28107410
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92598 * 0.15282775
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35158 * 0.31690786
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29256 * 0.02940765
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79715 * 0.74339596
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77013 * 0.69112893
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41082 * 0.82202002
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96720 * 0.30609112
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6123 * 0.49232869
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88608 * 0.76855579
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78014 * 0.52601522
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89395 * 0.43825777
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83041 * 0.64704111
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90467 * 0.81500235
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4588 * 0.31388258
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74000 * 0.54160304
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81695 * 0.20822634
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69830 * 0.30987187
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73147 * 0.81097581
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69495 * 0.16136703
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96543 * 0.28099628
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77301 * 0.57204689
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'jopaydsl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0021():
    """Extended test 21 for transcoding."""
    x_0 = 65075 * 0.86041532
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49796 * 0.47248626
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86649 * 0.48014745
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38333 * 0.98429328
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27389 * 0.87962043
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84468 * 0.21309463
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28269 * 0.70762843
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57054 * 0.41208375
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81305 * 0.35720318
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69207 * 0.62367955
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87697 * 0.45569187
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32246 * 0.06055105
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45466 * 0.60172490
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20213 * 0.73928891
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18967 * 0.37291121
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64685 * 0.38338052
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67003 * 0.39049135
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41253 * 0.06924894
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86205 * 0.32425434
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45467 * 0.16731550
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72961 * 0.67954538
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76439 * 0.49561941
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36485 * 0.77127561
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24920 * 0.50397504
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44745 * 0.24238850
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9930 * 0.52529002
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92705 * 0.66681450
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29862 * 0.30953379
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43756 * 0.99013794
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44693 * 0.01024281
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34587 * 0.32294726
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3960 * 0.23744715
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11033 * 0.95892992
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32349 * 0.94832122
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9147 * 0.28290406
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58967 * 0.36490501
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61304 * 0.31285171
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'cbeuaabd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0022():
    """Extended test 22 for transcoding."""
    x_0 = 4000 * 0.80983392
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52207 * 0.92065357
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7850 * 0.71124558
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42777 * 0.60985228
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2331 * 0.84681439
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54208 * 0.39332849
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33487 * 0.34762775
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21674 * 0.10555623
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24404 * 0.34880371
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78435 * 0.48938168
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74065 * 0.07512149
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31474 * 0.69947932
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76765 * 0.97705061
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43538 * 0.50781060
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14926 * 0.46515897
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28906 * 0.36398838
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79500 * 0.68807478
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73969 * 0.64605671
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80350 * 0.19804445
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25488 * 0.76879513
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46938 * 0.55675964
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79015 * 0.18866754
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97904 * 0.83677661
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41148 * 0.01936155
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25470 * 0.08335162
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46484 * 0.49237965
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97231 * 0.79010426
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67906 * 0.67482747
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19688 * 0.17367357
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7407 * 0.22434805
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'iuioaggb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0023():
    """Extended test 23 for transcoding."""
    x_0 = 75337 * 0.49079169
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86839 * 0.52563275
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98349 * 0.89083018
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3429 * 0.31326158
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56735 * 0.75603637
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30188 * 0.58081030
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47978 * 0.73752710
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30144 * 0.04270031
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2586 * 0.21209622
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85495 * 0.02254465
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59829 * 0.73878959
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67959 * 0.59140917
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65008 * 0.85549912
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19145 * 0.67153609
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5166 * 0.94527012
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45258 * 0.43311622
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75625 * 0.18715292
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13126 * 0.60975823
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36960 * 0.06210263
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88319 * 0.24061914
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30436 * 0.31532561
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24404 * 0.35099160
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48508 * 0.02041751
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23808 * 0.86677543
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19838 * 0.75553927
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16957 * 0.09081102
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93605 * 0.93702705
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4381 * 0.76625078
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1373 * 0.39908472
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99533 * 0.39157073
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19890 * 0.59676676
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97037 * 0.89342432
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37188 * 0.90048361
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49710 * 0.27183410
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71336 * 0.46621209
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14844 * 0.95369368
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73698 * 0.88452411
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'broamrgv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0024():
    """Extended test 24 for transcoding."""
    x_0 = 12453 * 0.46907623
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88893 * 0.81029955
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38928 * 0.05878716
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55038 * 0.64705453
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41709 * 0.84325412
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51946 * 0.53631207
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9314 * 0.64685431
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95018 * 0.82552705
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43820 * 0.91072051
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41914 * 0.85544396
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66454 * 0.41083054
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76130 * 0.20113197
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39230 * 0.68796397
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33773 * 0.18640052
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92255 * 0.88165645
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52147 * 0.29282653
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63508 * 0.87656699
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16627 * 0.88433866
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17613 * 0.08190901
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36895 * 0.43364031
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8166 * 0.13959430
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64054 * 0.60361010
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17935 * 0.58382740
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12743 * 0.68706625
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90646 * 0.56695098
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89045 * 0.21211469
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50187 * 0.82815748
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97561 * 0.88676288
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78168 * 0.66566062
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'mezblpaf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0025():
    """Extended test 25 for transcoding."""
    x_0 = 588 * 0.79620971
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21396 * 0.42531683
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1995 * 0.89310242
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66909 * 0.52632940
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31517 * 0.43055514
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41590 * 0.58263585
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42896 * 0.38012108
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91060 * 0.52458991
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35516 * 0.44120800
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72041 * 0.57332164
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37817 * 0.94530439
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22662 * 0.07853843
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16782 * 0.46675935
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20257 * 0.17028310
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79009 * 0.33252391
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39916 * 0.29597852
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50779 * 0.60255471
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26072 * 0.25971768
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81097 * 0.86184770
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11467 * 0.45327059
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12369 * 0.07600650
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80207 * 0.26247537
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72336 * 0.71945222
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55789 * 0.99409658
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14495 * 0.44483333
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90952 * 0.00997426
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20788 * 0.10498147
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37724 * 0.76959701
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13666 * 0.95117316
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90572 * 0.31886931
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'teqqmxox').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0026():
    """Extended test 26 for transcoding."""
    x_0 = 39614 * 0.67592479
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16346 * 0.42933987
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6339 * 0.50385633
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83292 * 0.09825607
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36670 * 0.63557327
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83492 * 0.02009973
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90866 * 0.36911883
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94408 * 0.19268977
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71022 * 0.58511829
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81553 * 0.41450531
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7830 * 0.10400086
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61589 * 0.34317242
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31368 * 0.86161315
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95476 * 0.05351939
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31880 * 0.28474292
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11560 * 0.82101908
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93374 * 0.25928003
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21127 * 0.05209604
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66917 * 0.20609090
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20945 * 0.80827936
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24265 * 0.73203873
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89157 * 0.61175999
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26748 * 0.46023538
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'sunagvbw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0027():
    """Extended test 27 for transcoding."""
    x_0 = 3958 * 0.71532306
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5277 * 0.55828789
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79434 * 0.57774835
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5225 * 0.24721076
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89803 * 0.57737402
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31545 * 0.46760712
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56315 * 0.63506476
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78484 * 0.13437833
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67970 * 0.16954930
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3010 * 0.63461657
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49246 * 0.11507349
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80564 * 0.97202590
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6833 * 0.23938037
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54804 * 0.73532550
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43769 * 0.54173279
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86841 * 0.25511785
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11857 * 0.48492373
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64797 * 0.02341893
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98975 * 0.30234872
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59184 * 0.02788676
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19348 * 0.94310381
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68124 * 0.52243495
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47017 * 0.16283234
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61810 * 0.71609647
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44970 * 0.57646964
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30393 * 0.16755096
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83440 * 0.17430127
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62778 * 0.02880223
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15349 * 0.90504467
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14763 * 0.30763084
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37810 * 0.89270987
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4271 * 0.05629387
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51267 * 0.50593759
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83994 * 0.21153897
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25232 * 0.05346898
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21880 * 0.41640412
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'cgbuhjkp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0028():
    """Extended test 28 for transcoding."""
    x_0 = 11904 * 0.69521621
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85586 * 0.56802262
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70765 * 0.70404952
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22538 * 0.33386370
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7707 * 0.43012253
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52203 * 0.90834457
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22582 * 0.74218404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81613 * 0.04463139
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13832 * 0.52647785
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81588 * 0.68386520
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3255 * 0.02022725
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37213 * 0.08275946
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53851 * 0.75937035
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38912 * 0.47648008
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56651 * 0.44581606
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83051 * 0.78433152
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49893 * 0.53100110
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60112 * 0.31632624
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54596 * 0.61027247
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15835 * 0.25064818
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42989 * 0.36686975
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35534 * 0.93441242
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59308 * 0.59036811
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44909 * 0.59268628
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37759 * 0.02784363
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89572 * 0.62304606
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'zfnqovth').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0029():
    """Extended test 29 for transcoding."""
    x_0 = 58272 * 0.91439034
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1502 * 0.01349098
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54808 * 0.28650743
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87291 * 0.33383120
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11090 * 0.80070299
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64461 * 0.57488917
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54336 * 0.13506222
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58557 * 0.22966516
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12459 * 0.67055327
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31656 * 0.69151585
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15000 * 0.98478925
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12949 * 0.82453621
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5811 * 0.95712488
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92475 * 0.07566063
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70205 * 0.33495562
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71914 * 0.51873967
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42839 * 0.55151547
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19671 * 0.60080763
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72641 * 0.67654606
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78353 * 0.43506009
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64233 * 0.42898583
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52301 * 0.05413978
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59655 * 0.69250619
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40164 * 0.84746783
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19725 * 0.16541197
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20924 * 0.97406679
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12855 * 0.63202651
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77529 * 0.24627161
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86688 * 0.60538129
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66794 * 0.91675031
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48220 * 0.82107548
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38817 * 0.26421552
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37893 * 0.89346735
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64163 * 0.60902900
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36832 * 0.80477458
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46896 * 0.52575955
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'srcrbgyn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0030():
    """Extended test 30 for transcoding."""
    x_0 = 14821 * 0.95232699
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92193 * 0.62785124
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17348 * 0.67883698
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6717 * 0.34444842
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32149 * 0.70395332
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34851 * 0.40760442
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69707 * 0.44469535
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5397 * 0.48402456
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67305 * 0.05478412
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94410 * 0.68069964
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81472 * 0.50683526
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 444 * 0.50947362
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41719 * 0.39142006
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81086 * 0.19372211
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20807 * 0.31597689
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37627 * 0.65402739
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62373 * 0.62606239
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68789 * 0.33255899
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1833 * 0.44282885
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22232 * 0.08241443
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 772 * 0.48239905
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12456 * 0.71854216
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39549 * 0.86544182
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65713 * 0.94486548
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25381 * 0.82367045
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29530 * 0.42030587
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99125 * 0.20684829
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92858 * 0.05757585
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51014 * 0.55970234
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'mrevrkzm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0031():
    """Extended test 31 for transcoding."""
    x_0 = 63244 * 0.48368183
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42421 * 0.82181570
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64337 * 0.13152518
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19116 * 0.40453957
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53357 * 0.89840143
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54331 * 0.39246378
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27460 * 0.13861651
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55362 * 0.50584886
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57747 * 0.70241964
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21128 * 0.95965458
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14904 * 0.38340328
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46175 * 0.00380290
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22773 * 0.12074509
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42450 * 0.26601530
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74367 * 0.81252598
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48402 * 0.44985389
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89794 * 0.26919660
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51201 * 0.14909976
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6990 * 0.50227178
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14046 * 0.96250314
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88028 * 0.68671965
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65083 * 0.02580103
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78110 * 0.03656734
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9207 * 0.91809655
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45887 * 0.15100889
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16615 * 0.31728715
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24081 * 0.31654289
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41879 * 0.71510101
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43562 * 0.26147410
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72332 * 0.77903190
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82358 * 0.84818067
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72287 * 0.72762185
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85014 * 0.39236432
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53393 * 0.78001396
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88187 * 0.07670441
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83232 * 0.66888495
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28842 * 0.21416075
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82551 * 0.35392484
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46324 * 0.33101435
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56519 * 0.96058419
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17166 * 0.36799547
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47895 * 0.41657765
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 4543 * 0.57274635
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 6085 * 0.23317231
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xwbfvekq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0032():
    """Extended test 32 for transcoding."""
    x_0 = 81722 * 0.24355169
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26721 * 0.70172652
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72143 * 0.30103566
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49565 * 0.73488936
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68440 * 0.15938840
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59186 * 0.16975163
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50017 * 0.82414462
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11182 * 0.55426760
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42624 * 0.21059117
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46426 * 0.84733204
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47326 * 0.79158892
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97158 * 0.64771504
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51361 * 0.00306122
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76860 * 0.33915486
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60583 * 0.27714706
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5696 * 0.17870564
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64338 * 0.47380963
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48877 * 0.57561641
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5060 * 0.86428365
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7149 * 0.09255456
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7881 * 0.06833802
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52723 * 0.09570619
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35902 * 0.13013495
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44408 * 0.35243339
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44980 * 0.56043069
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86259 * 0.40398906
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13657 * 0.86268148
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21272 * 0.37402793
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79433 * 0.17029236
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43555 * 0.43664490
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84713 * 0.92124277
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'bpzndeva').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0033():
    """Extended test 33 for transcoding."""
    x_0 = 40484 * 0.37920954
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54235 * 0.17668109
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35762 * 0.47478510
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37841 * 0.17197220
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39377 * 0.72660627
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56285 * 0.11382426
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98262 * 0.36615200
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87245 * 0.89932964
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50424 * 0.45175652
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26791 * 0.81689640
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71807 * 0.67453503
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69804 * 0.84565651
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4339 * 0.63597086
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48114 * 0.22071204
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3059 * 0.45342705
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22389 * 0.77254093
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76306 * 0.42114968
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31043 * 0.25127465
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12485 * 0.33316287
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14681 * 0.99736409
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80323 * 0.74047146
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88966 * 0.43733228
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87639 * 0.80244405
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80659 * 0.07532576
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40541 * 0.38129569
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63127 * 0.24811130
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94258 * 0.71208931
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81025 * 0.38468693
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75965 * 0.57187674
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32553 * 0.49246098
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52661 * 0.22128843
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18556 * 0.14022028
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 110 * 0.57657148
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54319 * 0.17217983
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68620 * 0.33571605
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24553 * 0.11473088
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22534 * 0.05711383
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8420 * 0.95172982
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56615 * 0.45864918
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57338 * 0.93620333
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64120 * 0.57393635
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88412 * 0.97703723
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 49169 * 0.04828913
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 18606 * 0.24846657
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17147 * 0.93342501
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 6152 * 0.94561863
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 24267 * 0.20696277
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 99060 * 0.29281338
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 12009 * 0.30113691
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 20689 * 0.47653378
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'peogihnr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0034():
    """Extended test 34 for transcoding."""
    x_0 = 92594 * 0.24670352
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59847 * 0.28875524
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94219 * 0.07158155
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55437 * 0.03031447
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20140 * 0.12353808
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50485 * 0.56859459
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 795 * 0.57435379
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91547 * 0.22650921
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38736 * 0.98526519
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83799 * 0.93980721
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9081 * 0.26551125
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24103 * 0.50890849
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53196 * 0.74819508
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70881 * 0.06598986
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40639 * 0.13394026
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55341 * 0.74214352
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35070 * 0.86430636
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99157 * 0.52623605
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37795 * 0.55289624
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57047 * 0.17521894
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50558 * 0.86980540
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99689 * 0.35636096
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94868 * 0.44739662
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48416 * 0.61849481
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86483 * 0.84209934
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97433 * 0.04835445
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33365 * 0.53471199
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37344 * 0.94947573
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1730 * 0.70169978
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44935 * 0.04001245
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47842 * 0.90430510
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52896 * 0.58128246
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80204 * 0.86409294
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21435 * 0.52977528
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62926 * 0.32767867
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90760 * 0.51715185
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'mexovyeb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0035():
    """Extended test 35 for transcoding."""
    x_0 = 15289 * 0.31028264
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9517 * 0.04062139
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97081 * 0.29918797
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31063 * 0.60135507
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55092 * 0.09823254
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16108 * 0.56273853
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27834 * 0.82215716
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39099 * 0.25041448
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99391 * 0.31133632
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43253 * 0.82864741
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17183 * 0.09853598
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80141 * 0.64517962
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60539 * 0.27975428
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99289 * 0.51252874
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32461 * 0.98174389
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81771 * 0.71188100
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83930 * 0.72432815
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19837 * 0.99938069
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28682 * 0.25860115
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57135 * 0.55986714
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65365 * 0.95997123
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81417 * 0.46616564
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83925 * 0.90071200
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78600 * 0.27201823
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62854 * 0.40959605
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52258 * 0.29603324
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37013 * 0.30264467
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67960 * 0.42803841
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70983 * 0.12644982
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7429 * 0.67292745
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57527 * 0.03446455
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 855 * 0.52404361
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55756 * 0.47900327
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28366 * 0.39185178
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14313 * 0.74602120
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38490 * 0.91032882
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21842 * 0.66083766
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28260 * 0.59205923
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51861 * 0.79794896
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85182 * 0.06644704
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 14400 * 0.47405790
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47828 * 0.87778398
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11790 * 0.82550615
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 66910 * 0.17812021
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 53810 * 0.54147429
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 61633 * 0.00819993
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 74599 * 0.11807709
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 14029 * 0.28388811
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'qkyyfkqd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0036():
    """Extended test 36 for transcoding."""
    x_0 = 24962 * 0.87883856
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97205 * 0.92907927
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31064 * 0.98194434
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73370 * 0.77918724
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53592 * 0.42135859
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45921 * 0.64434760
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25558 * 0.80898238
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54798 * 0.66742294
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92720 * 0.48292712
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49851 * 0.06396128
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73572 * 0.63360496
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39753 * 0.82396984
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69723 * 0.59004120
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10900 * 0.37747806
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8473 * 0.59347418
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91824 * 0.03636237
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23369 * 0.04094200
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22970 * 0.34739555
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55247 * 0.65842337
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93745 * 0.68415002
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68729 * 0.89283357
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28892 * 0.02220824
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'bxyxbqxh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0037():
    """Extended test 37 for transcoding."""
    x_0 = 52190 * 0.23333858
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62779 * 0.61507551
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21205 * 0.09781808
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12505 * 0.36370244
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92348 * 0.51791670
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86344 * 0.33843558
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89470 * 0.42290077
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38599 * 0.69627289
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22730 * 0.65839916
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64612 * 0.49247544
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25120 * 0.39538501
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51917 * 0.08097041
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71744 * 0.35031729
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67705 * 0.11558434
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36081 * 0.28571307
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30276 * 0.22631843
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45292 * 0.28077684
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53689 * 0.92679765
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38542 * 0.49873646
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42008 * 0.55257735
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66140 * 0.64185393
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26930 * 0.76297473
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52449 * 0.26817457
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15241 * 0.19447145
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'wlkmqzem').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0038():
    """Extended test 38 for transcoding."""
    x_0 = 56235 * 0.38937642
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70121 * 0.86942011
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57357 * 0.64209045
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8184 * 0.97352278
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27039 * 0.68999246
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8420 * 0.91906537
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11123 * 0.92608556
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53299 * 0.81881289
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99860 * 0.81193145
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23160 * 0.33391833
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80087 * 0.52353453
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9407 * 0.08307658
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67982 * 0.43339647
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81735 * 0.00333136
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13475 * 0.65498821
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30528 * 0.07775197
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30335 * 0.36358014
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74757 * 0.12929025
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91080 * 0.49166755
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45228 * 0.98971672
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55042 * 0.35533638
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25069 * 0.39285407
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5645 * 0.66956456
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15568 * 0.31754987
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75584 * 0.56632956
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14928 * 0.37793581
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87541 * 0.09573269
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76200 * 0.96097464
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42176 * 0.44597833
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83701 * 0.44703164
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24555 * 0.31039789
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78112 * 0.96308369
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49683 * 0.17242326
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5904 * 0.23335405
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22388 * 0.09259535
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8894 * 0.16732906
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76309 * 0.22469717
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24411 * 0.49788383
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63759 * 0.49644788
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69772 * 0.02798174
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34358 * 0.94085588
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70650 * 0.84970308
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 86015 * 0.50913824
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 16034 * 0.22239605
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'vrrqowei').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0039():
    """Extended test 39 for transcoding."""
    x_0 = 58603 * 0.68673966
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5005 * 0.30186607
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47216 * 0.03430492
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40233 * 0.45988477
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95454 * 0.74535139
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20811 * 0.11010675
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51683 * 0.97594383
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66548 * 0.82509704
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45836 * 0.50286806
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34258 * 0.94797023
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65773 * 0.08652781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66259 * 0.37246667
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85098 * 0.04265888
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27549 * 0.64954693
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68844 * 0.44479985
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5115 * 0.58470516
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99841 * 0.69660211
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72211 * 0.00414367
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55544 * 0.44869886
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84409 * 0.43251021
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58834 * 0.91372849
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88389 * 0.85745543
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41627 * 0.37803241
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24394 * 0.59261919
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71325 * 0.85537253
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94723 * 0.12446849
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49817 * 0.05415067
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72548 * 0.36363793
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61976 * 0.12896472
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23685 * 0.75022363
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53669 * 0.35125991
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21549 * 0.92768520
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70368 * 0.05314968
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85527 * 0.29427166
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95310 * 0.24059483
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11257 * 0.50812673
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4082 * 0.53873121
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6477 * 0.81659271
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66135 * 0.15388919
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4216 * 0.04624039
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ibxcfvqj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0040():
    """Extended test 40 for transcoding."""
    x_0 = 97023 * 0.81628092
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44528 * 0.44018734
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42497 * 0.62200491
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87953 * 0.12977877
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83297 * 0.74778992
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32206 * 0.72023517
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91939 * 0.03195685
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16677 * 0.58352391
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94982 * 0.76748777
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9478 * 0.92005764
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92174 * 0.05859227
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99928 * 0.81782146
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5952 * 0.69506305
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41983 * 0.17517424
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91426 * 0.43095789
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73527 * 0.37043119
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44570 * 0.17876080
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63715 * 0.68000365
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25836 * 0.78781257
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93258 * 0.61514852
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91689 * 0.53347314
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33083 * 0.51363296
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56381 * 0.79274645
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20785 * 0.48542146
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17078 * 0.87382399
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23540 * 0.44069025
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20060 * 0.38991601
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71916 * 0.61398774
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71415 * 0.03723179
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47383 * 0.60632284
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85682 * 0.22851465
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86152 * 0.40288594
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25467 * 0.34431461
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19603 * 0.74852272
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43718 * 0.67554771
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46164 * 0.66683541
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64600 * 0.32903092
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20526 * 0.52743343
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16833 * 0.75845400
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74340 * 0.61716632
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 517 * 0.17314369
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22488 * 0.62466720
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16831 * 0.74888035
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 90099 * 0.38625874
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 97978 * 0.64686931
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 87243 * 0.65655080
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'nkldavkq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0041():
    """Extended test 41 for transcoding."""
    x_0 = 53905 * 0.24773689
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54088 * 0.00274383
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2212 * 0.51873270
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70191 * 0.60275524
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86785 * 0.60853424
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58693 * 0.15799077
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95190 * 0.37909720
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46678 * 0.73987183
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55660 * 0.71793888
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23458 * 0.72034694
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98586 * 0.72427289
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64863 * 0.15393802
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98894 * 0.30092808
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67310 * 0.03662280
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14872 * 0.15991574
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37558 * 0.49961643
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50936 * 0.78358645
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42481 * 0.66314948
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80905 * 0.81534497
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35780 * 0.27837866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12053 * 0.97692531
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27895 * 0.14027320
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12854 * 0.73267208
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31989 * 0.28694468
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10332 * 0.54294286
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12743 * 0.25188736
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26533 * 0.64269330
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44128 * 0.00797643
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25053 * 0.12257032
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76499 * 0.43137201
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51597 * 0.86627250
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99189 * 0.19863744
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89085 * 0.77363419
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23736 * 0.46625658
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35441 * 0.51757112
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7534 * 0.67154793
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8695 * 0.87519140
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'cxroojjn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0042():
    """Extended test 42 for transcoding."""
    x_0 = 87230 * 0.18416833
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45754 * 0.34956927
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9844 * 0.22177466
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90993 * 0.43480492
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61278 * 0.78558312
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83244 * 0.90360758
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54922 * 0.24108721
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42933 * 0.37361366
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26478 * 0.61758303
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66805 * 0.01226771
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87206 * 0.73074341
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30761 * 0.32096176
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48542 * 0.18968109
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65420 * 0.20575187
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74576 * 0.63984486
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23599 * 0.23122213
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2256 * 0.61351877
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99087 * 0.68469650
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50918 * 0.78448125
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75521 * 0.74297724
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92901 * 0.82617270
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 525 * 0.39924975
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'nirglyyv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0043():
    """Extended test 43 for transcoding."""
    x_0 = 71599 * 0.51452565
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64013 * 0.09686470
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28521 * 0.19831620
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31849 * 0.08167795
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8102 * 0.71441565
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52062 * 0.37324061
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77968 * 0.67007748
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9170 * 0.93634960
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70376 * 0.58311989
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43992 * 0.19129665
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79048 * 0.32837599
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85741 * 0.52575868
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76722 * 0.16028391
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54277 * 0.92572530
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79099 * 0.85381952
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98859 * 0.65513983
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48088 * 0.07016013
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76802 * 0.12297457
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3942 * 0.19651277
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77263 * 0.43068347
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7281 * 0.65997534
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'kuchirmn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0044():
    """Extended test 44 for transcoding."""
    x_0 = 33409 * 0.74800176
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58775 * 0.81371222
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90351 * 0.06040877
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99802 * 0.29912893
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66948 * 0.56020719
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76135 * 0.04868706
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20514 * 0.27750462
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6581 * 0.40014777
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93721 * 0.52721640
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47550 * 0.59037576
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59387 * 0.55448586
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63785 * 0.16072890
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31908 * 0.27499434
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64288 * 0.14706041
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91485 * 0.79372507
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11737 * 0.75991159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59663 * 0.51035391
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84185 * 0.50249854
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21900 * 0.42317405
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1381 * 0.61801944
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76776 * 0.57634101
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44029 * 0.31396053
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53674 * 0.80500494
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82912 * 0.02666793
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41135 * 0.78088356
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17779 * 0.44612882
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89085 * 0.14322900
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23423 * 0.46974678
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51818 * 0.38978231
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3323 * 0.63263582
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27214 * 0.45142159
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49952 * 0.34050497
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13739 * 0.29441311
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36560 * 0.37798140
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71252 * 0.72303631
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78568 * 0.20300314
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3876 * 0.95687768
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79178 * 0.52682707
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27711 * 0.53981021
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62650 * 0.76724819
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'vdrnkuhw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0045():
    """Extended test 45 for transcoding."""
    x_0 = 25544 * 0.60680816
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57435 * 0.32411679
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49649 * 0.80158171
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71640 * 0.87403901
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47386 * 0.56557550
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5138 * 0.67139060
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84401 * 0.32914016
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43581 * 0.34652372
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33306 * 0.88612238
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67101 * 0.24421924
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46687 * 0.74539008
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32549 * 0.42730979
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93814 * 0.23068642
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38660 * 0.04693051
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4465 * 0.16313585
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12155 * 0.84588767
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40825 * 0.94973036
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42277 * 0.82929333
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30168 * 0.49266266
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62960 * 0.18347197
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12594 * 0.89143194
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40269 * 0.51092065
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73743 * 0.34452255
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74307 * 0.53256696
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94815 * 0.15111178
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39248 * 0.45104530
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73456 * 0.51340007
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87278 * 0.03255885
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87426 * 0.10380185
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40727 * 0.29920039
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15538 * 0.23696559
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67023 * 0.24867808
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20397 * 0.23373223
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50695 * 0.59592685
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80840 * 0.74242153
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45576 * 0.33283342
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11659 * 0.21101354
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74325 * 0.70680905
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76158 * 0.40970684
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ktucjlua').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0046():
    """Extended test 46 for transcoding."""
    x_0 = 57069 * 0.76333405
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71621 * 0.10250143
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14701 * 0.15965513
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40222 * 0.44290476
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92751 * 0.07791914
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93280 * 0.75852412
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27190 * 0.12990095
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5896 * 0.65492772
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67601 * 0.10979317
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95028 * 0.76730931
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76601 * 0.85969555
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47531 * 0.95973933
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32163 * 0.27096011
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26547 * 0.43600388
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70147 * 0.44859540
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69689 * 0.49791356
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45155 * 0.18735943
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39631 * 0.21973393
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81224 * 0.44062777
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81855 * 0.07435969
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4034 * 0.77535278
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46320 * 0.67352842
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90164 * 0.34361040
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77837 * 0.22598828
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59075 * 0.15421655
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13156 * 0.41244992
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47699 * 0.45196293
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2524 * 0.39204162
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68524 * 0.31543868
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69849 * 0.26778010
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54817 * 0.95483611
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56420 * 0.76153724
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7880 * 0.82748627
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83945 * 0.94873297
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72336 * 0.12369519
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'cfhysmvs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0047():
    """Extended test 47 for transcoding."""
    x_0 = 71939 * 0.40524691
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90652 * 0.38721481
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31121 * 0.77850626
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82317 * 0.81005702
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4795 * 0.20937217
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44220 * 0.74388425
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33568 * 0.90046501
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92907 * 0.50271413
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7558 * 0.75191306
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89777 * 0.49861905
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68048 * 0.92405668
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28314 * 0.31670515
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32140 * 0.36561451
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8023 * 0.59930481
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75258 * 0.08890684
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16496 * 0.30024878
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63783 * 0.31794937
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56144 * 0.78538369
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22593 * 0.41781440
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18995 * 0.31981118
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74118 * 0.23313815
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35922 * 0.16348941
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68278 * 0.13162305
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11300 * 0.54859994
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58223 * 0.51738239
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2946 * 0.57773899
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65756 * 0.55234964
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61011 * 0.93442248
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84029 * 0.71650148
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58574 * 0.45673170
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67765 * 0.03665521
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20277 * 0.47454047
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26939 * 0.65608631
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'zwqubtas').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0048():
    """Extended test 48 for transcoding."""
    x_0 = 86383 * 0.43146083
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6003 * 0.33692547
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69642 * 0.26842027
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32205 * 0.55706435
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51968 * 0.28514191
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9072 * 0.01830406
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29624 * 0.37741720
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95653 * 0.10050621
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11602 * 0.84282664
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5789 * 0.10470606
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79210 * 0.20191418
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98574 * 0.64150431
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40610 * 0.49790090
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24748 * 0.64099300
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95230 * 0.93922613
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36450 * 0.41067969
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35367 * 0.60381902
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17545 * 0.54481649
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51786 * 0.07868460
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3874 * 0.13099539
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59209 * 0.71548359
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89317 * 0.97360640
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41880 * 0.81939209
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95407 * 0.74967351
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13571 * 0.78186130
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2935 * 0.11960650
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53660 * 0.53588713
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60795 * 0.46248753
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80387 * 0.76782687
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85017 * 0.44533477
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61452 * 0.97863017
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17706 * 0.83763416
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4425 * 0.84996932
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96278 * 0.00889952
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50794 * 0.71919517
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19473 * 0.19971865
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57063 * 0.20323183
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83830 * 0.35826690
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58959 * 0.27306772
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 26494 * 0.97795162
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75364 * 0.49910912
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 87816 * 0.35128084
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29385 * 0.95490508
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 44500 * 0.11957181
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 74232 * 0.95765513
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'wyaeeutz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0049():
    """Extended test 49 for transcoding."""
    x_0 = 60551 * 0.77097650
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51965 * 0.15416378
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41768 * 0.89490875
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54974 * 0.13613577
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12922 * 0.96170044
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45711 * 0.52386309
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29099 * 0.92223139
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48346 * 0.84642018
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81708 * 0.29830810
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76572 * 0.83525564
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98231 * 0.08339511
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31895 * 0.74271936
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72369 * 0.34773723
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95885 * 0.07534943
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13486 * 0.85746248
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93190 * 0.18969603
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26545 * 0.65889384
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19307 * 0.00369022
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47852 * 0.28777763
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94663 * 0.23559595
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30532 * 0.93662203
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54176 * 0.32670759
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85540 * 0.82325212
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92103 * 0.07009826
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51346 * 0.46631557
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64745 * 0.45416132
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24650 * 0.89074057
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60137 * 0.90166179
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7286 * 0.33731178
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48032 * 0.94859953
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64507 * 0.65393538
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97037 * 0.92865990
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32704 * 0.14719366
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53902 * 0.14483918
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'tpqygdbt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0050():
    """Extended test 50 for transcoding."""
    x_0 = 4409 * 0.10656598
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39491 * 0.18444395
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4104 * 0.15016052
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77494 * 0.03448118
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70443 * 0.34609233
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68445 * 0.93374414
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42175 * 0.82976233
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96595 * 0.10901174
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46233 * 0.38680683
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70765 * 0.60967687
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67298 * 0.97850027
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11771 * 0.32182532
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22039 * 0.96455168
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50669 * 0.64495494
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99683 * 0.16061721
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23695 * 0.41561385
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4112 * 0.30006244
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49705 * 0.40865577
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18899 * 0.98128246
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51180 * 0.50023018
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27107 * 0.36424120
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56709 * 0.31863975
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92005 * 0.20853835
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68162 * 0.35098380
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2139 * 0.82247588
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17382 * 0.38075736
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74288 * 0.79297595
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42808 * 0.40002549
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63600 * 0.27802565
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96699 * 0.48129646
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66755 * 0.43931401
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31972 * 0.84909452
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1406 * 0.52537665
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87756 * 0.08476368
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46739 * 0.17894773
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58299 * 0.40075643
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1224 * 0.07198064
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83269 * 0.20576536
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44000 * 0.26245082
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63937 * 0.55011555
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'dccxdgiu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0051():
    """Extended test 51 for transcoding."""
    x_0 = 8445 * 0.16029342
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34694 * 0.39842018
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49574 * 0.26153893
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75368 * 0.31245812
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61847 * 0.71643501
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98751 * 0.98666509
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42170 * 0.90015804
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18390 * 0.05671195
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46261 * 0.27921009
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95212 * 0.51458880
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22059 * 0.51605599
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18763 * 0.65875280
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61664 * 0.85077451
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43453 * 0.51817554
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15896 * 0.82838050
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74818 * 0.96166089
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59406 * 0.32839594
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83435 * 0.29758154
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32205 * 0.60100969
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66511 * 0.26547678
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68693 * 0.78312379
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87657 * 0.75301228
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17664 * 0.19379845
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24770 * 0.03095177
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41923 * 0.90451051
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89368 * 0.93897432
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61368 * 0.08125493
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52139 * 0.05326217
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72511 * 0.46067976
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8094 * 0.42629982
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88821 * 0.27471063
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90734 * 0.60272912
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85783 * 0.51439712
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86214 * 0.36207458
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85007 * 0.55998187
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86444 * 0.48191393
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19065 * 0.70349310
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27947 * 0.60497487
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 22857 * 0.79843387
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17578 * 0.78554285
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6762 * 0.25419305
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 2625 * 0.84120048
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46158 * 0.23626881
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 13219 * 0.27656376
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 22355 * 0.17302375
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 25804 * 0.98601148
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 72701 * 0.97364825
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 68152 * 0.42375360
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'qzmdtwub').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0052():
    """Extended test 52 for transcoding."""
    x_0 = 89363 * 0.27107798
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91781 * 0.47784026
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37024 * 0.21516511
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16382 * 0.24743596
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52823 * 0.11119318
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86956 * 0.49239993
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60452 * 0.43205884
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10558 * 0.56356834
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49334 * 0.99194545
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90417 * 0.79282229
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81918 * 0.88366468
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20978 * 0.16186405
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78154 * 0.32342064
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75985 * 0.33459992
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4642 * 0.41020814
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98432 * 0.96055132
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5221 * 0.44542971
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93503 * 0.07441800
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23273 * 0.07439392
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48923 * 0.32252774
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28368 * 0.64655033
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35062 * 0.06813529
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'togdxaaw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0053():
    """Extended test 53 for transcoding."""
    x_0 = 67852 * 0.79867807
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86645 * 0.45082009
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27244 * 0.30242622
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60373 * 0.74231065
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35208 * 0.20601596
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66359 * 0.62901905
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51449 * 0.12973036
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98472 * 0.31523445
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60535 * 0.80090931
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85754 * 0.19563621
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94645 * 0.79663036
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91605 * 0.72697060
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82162 * 0.15716617
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45058 * 0.98314530
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35526 * 0.72764998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45017 * 0.11237597
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41035 * 0.55590886
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57028 * 0.46480147
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58901 * 0.66405501
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98307 * 0.61983974
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 568 * 0.71330138
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43512 * 0.67629028
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56802 * 0.20160519
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61955 * 0.16662751
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68395 * 0.45905821
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7534 * 0.34686408
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75850 * 0.92261667
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32597 * 0.06011438
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9449 * 0.56997718
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5880 * 0.13001149
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13494 * 0.86419538
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2624 * 0.24974839
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46010 * 0.98414041
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58931 * 0.76292286
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54987 * 0.09334090
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'secouvec').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0054():
    """Extended test 54 for transcoding."""
    x_0 = 21412 * 0.81737420
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80955 * 0.96246704
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28065 * 0.96859215
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52570 * 0.31514859
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90935 * 0.44923484
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55341 * 0.06340721
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93509 * 0.32574704
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79854 * 0.89662170
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18306 * 0.02334137
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86783 * 0.82614159
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63262 * 0.33113471
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11139 * 0.53739359
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62417 * 0.01616680
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64580 * 0.48988112
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50410 * 0.08169972
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61300 * 0.00381587
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14928 * 0.04217827
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1945 * 0.22107491
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58694 * 0.00973761
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78163 * 0.03808282
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16486 * 0.62951124
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35887 * 0.92902877
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61697 * 0.48601011
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4552 * 0.47331303
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43844 * 0.87788350
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35206 * 0.16148553
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33862 * 0.55791759
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42384 * 0.08401013
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8221 * 0.73102757
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21149 * 0.72511048
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82750 * 0.46784174
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29901 * 0.09147259
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3650 * 0.10544412
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58368 * 0.62796459
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18320 * 0.47752746
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45036 * 0.86498417
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29275 * 0.39115302
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11472 * 0.82019020
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93370 * 0.80303989
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65282 * 0.27478745
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 59551 * 0.08853789
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21904 * 0.40583559
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 90908 * 0.99921796
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 70780 * 0.29443508
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50184 * 0.06430434
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 62810 * 0.17448473
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'aouhouit').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0055():
    """Extended test 55 for transcoding."""
    x_0 = 92758 * 0.48885052
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99514 * 0.92371855
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90283 * 0.04048708
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89007 * 0.39368424
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43746 * 0.52142241
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56335 * 0.22630580
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95064 * 0.08727524
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65953 * 0.01150757
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9923 * 0.10230079
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61738 * 0.44192070
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2188 * 0.59575964
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60684 * 0.24890164
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92361 * 0.42518493
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37138 * 0.81222987
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62611 * 0.53408279
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3300 * 0.61126969
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46316 * 0.71638786
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78543 * 0.48695014
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4226 * 0.69198633
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48983 * 0.32957065
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13841 * 0.96778989
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82547 * 0.02314050
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95477 * 0.98423524
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89932 * 0.39327291
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18134 * 0.00900188
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67085 * 0.59527152
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59013 * 0.83152475
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56856 * 0.94581511
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 643 * 0.91463948
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73622 * 0.91146011
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68810 * 0.52179515
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52979 * 0.17813088
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36591 * 0.44300843
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19508 * 0.20943632
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88668 * 0.76931496
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65439 * 0.35527798
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80347 * 0.13065640
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48723 * 0.60540096
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 962 * 0.82227885
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95127 * 0.50004337
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20389 * 0.40256544
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 62087 * 0.67678578
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 50998 * 0.40152997
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 90909 * 0.12376622
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 57036 * 0.27129532
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 58922 * 0.82669237
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 24896 * 0.13108663
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'giugxfkn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0056():
    """Extended test 56 for transcoding."""
    x_0 = 87818 * 0.70319759
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15029 * 0.19484646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56705 * 0.47787189
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60942 * 0.21613536
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84967 * 0.80456350
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69143 * 0.61189144
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68933 * 0.95061903
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66456 * 0.26079442
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20702 * 0.85336698
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4778 * 0.40531309
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17701 * 0.46428460
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6560 * 0.59805314
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76515 * 0.12827451
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99782 * 0.67417481
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53703 * 0.30999290
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98591 * 0.06764911
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36485 * 0.07247584
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21520 * 0.39166639
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61931 * 0.34945205
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11275 * 0.39347088
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1425 * 0.39458878
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95478 * 0.79503488
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70983 * 0.63461925
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'nvioudqf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0057():
    """Extended test 57 for transcoding."""
    x_0 = 44687 * 0.18060068
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7940 * 0.07990542
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23322 * 0.67564943
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20679 * 0.05915683
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84781 * 0.29380248
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62859 * 0.63172493
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97736 * 0.38117602
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4202 * 0.99338222
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63221 * 0.41656706
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6413 * 0.10493303
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75282 * 0.06837191
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71292 * 0.33094648
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70702 * 0.21565294
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77741 * 0.10838162
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30850 * 0.88802268
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12420 * 0.16151893
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65962 * 0.06036738
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85462 * 0.11596465
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54587 * 0.78339849
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84455 * 0.89558919
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'oikgqedb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0058():
    """Extended test 58 for transcoding."""
    x_0 = 23533 * 0.77698407
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41996 * 0.10202505
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83599 * 0.24063008
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79896 * 0.97181383
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44764 * 0.06876696
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76283 * 0.65266354
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99365 * 0.21039126
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30381 * 0.87212578
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 703 * 0.54363490
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13387 * 0.25151530
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51719 * 0.39563211
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80441 * 0.35577765
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94587 * 0.01722529
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67738 * 0.65216564
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49212 * 0.83820157
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8093 * 0.19892575
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43673 * 0.98912361
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54799 * 0.28629212
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26037 * 0.21347402
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37279 * 0.26089568
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78677 * 0.34783410
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87654 * 0.77881196
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84886 * 0.22873927
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61122 * 0.98369700
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15254 * 0.38982129
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81068 * 0.45913447
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50357 * 0.37720923
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47872 * 0.09532930
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39276 * 0.67207703
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49961 * 0.13244633
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42197 * 0.77139514
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43902 * 0.11939864
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12883 * 0.12934742
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15289 * 0.87859978
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26276 * 0.31783269
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8435 * 0.38587400
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15956 * 0.21711284
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20221 * 0.01866773
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44213 * 0.01765867
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74985 * 0.76634867
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88555 * 0.22787377
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 55676 * 0.30112660
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77396 * 0.19513890
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 50219 * 0.93066088
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 8334 * 0.64112778
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 97829 * 0.06317060
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 69459 * 0.35406436
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 90263 * 0.30698145
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'nqlrykxf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0059():
    """Extended test 59 for transcoding."""
    x_0 = 43843 * 0.66093123
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15811 * 0.23346416
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82205 * 0.39806867
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39498 * 0.68818689
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74449 * 0.53752821
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27540 * 0.77567443
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68474 * 0.30903027
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18150 * 0.44573178
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78369 * 0.94909004
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61385 * 0.15311273
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86773 * 0.24485680
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58998 * 0.51032549
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16760 * 0.45881592
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28047 * 0.40486749
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64324 * 0.89086553
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26751 * 0.04478512
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6596 * 0.73518185
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95572 * 0.81836481
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66557 * 0.05868437
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29183 * 0.90788160
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85157 * 0.85685205
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68687 * 0.59627326
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74538 * 0.04433782
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15110 * 0.65601918
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56256 * 0.07327834
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62974 * 0.85942845
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48078 * 0.32987325
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92274 * 0.67963881
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7973 * 0.54902073
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83560 * 0.17163334
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70152 * 0.20811584
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92299 * 0.17350949
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13527 * 0.40884994
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56658 * 0.79978302
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84253 * 0.29726402
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86963 * 0.75100871
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60734 * 0.24236217
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42980 * 0.22650326
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35669 * 0.16219887
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31521 * 0.58279114
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1399 * 0.05236721
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57457 * 0.93703986
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24623 * 0.69209586
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 18632 * 0.02627020
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 45314 * 0.98887507
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 64774 * 0.79340814
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 21606 * 0.52153143
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 91163 * 0.40029103
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'apdazcpc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0060():
    """Extended test 60 for transcoding."""
    x_0 = 61869 * 0.90895811
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42517 * 0.54847436
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33090 * 0.78325647
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35812 * 0.00757879
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29855 * 0.65737598
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98472 * 0.92645070
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79564 * 0.67877785
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50067 * 0.84639350
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48026 * 0.28567904
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58288 * 0.40614786
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62257 * 0.57430102
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50117 * 0.30988888
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90698 * 0.64754882
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22536 * 0.34807782
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51402 * 0.16536664
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69013 * 0.52825210
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87232 * 0.13534530
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31681 * 0.37445406
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18896 * 0.82979127
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27909 * 0.98747369
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'cjcvnbqp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0061():
    """Extended test 61 for transcoding."""
    x_0 = 20497 * 0.61997118
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50694 * 0.26119327
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76489 * 0.91604478
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93848 * 0.56380032
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24024 * 0.39419756
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1977 * 0.94788836
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3366 * 0.79123059
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7134 * 0.14830253
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32989 * 0.80079453
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31727 * 0.68562851
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12766 * 0.40005326
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82261 * 0.28291218
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28670 * 0.62825345
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14539 * 0.19354806
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67624 * 0.95223925
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70072 * 0.86536201
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50266 * 0.00834827
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23103 * 0.17229315
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60618 * 0.61788545
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62807 * 0.46325012
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35656 * 0.36417976
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9204 * 0.43130266
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45300 * 0.23665803
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62409 * 0.55349902
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73507 * 0.66053131
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7101 * 0.59545502
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86317 * 0.44579989
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8908 * 0.12729726
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32440 * 0.15043845
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29441 * 0.71791069
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'weboordg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0062():
    """Extended test 62 for transcoding."""
    x_0 = 59291 * 0.16753016
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43550 * 0.09686611
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54374 * 0.11914883
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54145 * 0.61434057
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71451 * 0.31339927
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40906 * 0.90360798
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53819 * 0.07370876
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2767 * 0.54030645
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63221 * 0.07907578
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30987 * 0.19579008
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44335 * 0.12546979
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75711 * 0.92665561
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61360 * 0.79644118
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82618 * 0.76782557
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85398 * 0.77650193
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9006 * 0.62851653
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25092 * 0.19489117
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93447 * 0.30039905
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65813 * 0.66300399
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36109 * 0.87097835
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13818 * 0.25036288
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58658 * 0.46398669
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15231 * 0.44449109
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39671 * 0.10482655
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36279 * 0.03957238
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12882 * 0.04317951
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50955 * 0.56817659
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49813 * 0.44613078
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62433 * 0.26859946
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51198 * 0.72132737
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'mcdjxcxd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0063():
    """Extended test 63 for transcoding."""
    x_0 = 69988 * 0.08235978
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59204 * 0.43033226
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84462 * 0.93613378
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36216 * 0.73286240
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22281 * 0.55214397
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14448 * 0.30895338
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9012 * 0.42933801
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57780 * 0.52197127
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30095 * 0.38976270
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42627 * 0.85447276
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66995 * 0.78714031
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42486 * 0.78881103
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69917 * 0.41867617
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81692 * 0.11531962
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8906 * 0.10064782
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5058 * 0.94250814
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63161 * 0.61633958
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24392 * 0.43640566
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47550 * 0.17649850
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7476 * 0.04290776
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57949 * 0.43398470
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53099 * 0.15103268
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99776 * 0.98168363
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36162 * 0.86557500
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92682 * 0.04155477
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8948 * 0.09142405
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47229 * 0.64891939
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32965 * 0.60074133
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18666 * 0.48325495
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60302 * 0.12079224
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63311 * 0.96675960
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40240 * 0.50677114
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32736 * 0.38662829
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84242 * 0.09668359
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12220 * 0.18039039
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39440 * 0.54650502
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33551 * 0.62483400
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90332 * 0.90761523
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88676 * 0.15323267
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84542 * 0.63538172
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32558 * 0.43167738
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89094 * 0.84950634
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ugucrkla').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0064():
    """Extended test 64 for transcoding."""
    x_0 = 54954 * 0.66231608
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14159 * 0.17075929
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26476 * 0.35013783
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47224 * 0.32900008
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43194 * 0.38593760
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97132 * 0.51461153
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24236 * 0.77561637
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72909 * 0.71137002
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21576 * 0.36165945
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52201 * 0.86207273
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44543 * 0.04550239
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39484 * 0.41259487
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76348 * 0.97658128
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85730 * 0.42668346
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61275 * 0.59607032
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44878 * 0.33877972
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88693 * 0.04764785
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52497 * 0.07397554
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87839 * 0.61536993
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55656 * 0.42949646
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52720 * 0.35102469
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79033 * 0.24775185
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21363 * 0.44774448
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38809 * 0.67312483
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24622 * 0.45835743
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46912 * 0.24364454
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63643 * 0.18577934
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49956 * 0.76571857
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85038 * 0.02632628
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53682 * 0.52809040
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62973 * 0.00142171
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70883 * 0.13799591
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65937 * 0.11199395
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1294 * 0.89601155
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8970 * 0.16530863
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93218 * 0.97820237
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72814 * 0.16415955
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30429 * 0.59114447
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70580 * 0.60686547
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 48972 * 0.70326265
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32725 * 0.97725933
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80248 * 0.23942735
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'bnygxysh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0065():
    """Extended test 65 for transcoding."""
    x_0 = 75432 * 0.02590568
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50213 * 0.50177851
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64645 * 0.93232584
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19237 * 0.49715414
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86816 * 0.16175514
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9626 * 0.94114320
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33699 * 0.40626404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76221 * 0.11240478
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78922 * 0.34810670
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9791 * 0.54784111
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5133 * 0.91213018
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53165 * 0.08605555
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77609 * 0.09917602
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14247 * 0.66817266
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19079 * 0.75557066
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48428 * 0.17380097
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41210 * 0.33441367
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87253 * 0.68079817
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60892 * 0.59560789
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91475 * 0.60397624
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24886 * 0.07129776
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7460 * 0.67778295
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92366 * 0.13248955
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75289 * 0.72349359
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7534 * 0.90259827
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6290 * 0.56797645
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67067 * 0.84464801
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83617 * 0.92988125
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48274 * 0.72792645
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22181 * 0.34609411
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5177 * 0.29057556
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98612 * 0.91180059
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83948 * 0.74356268
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79977 * 0.60526544
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27773 * 0.14185819
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27053 * 0.04752594
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68671 * 0.05512528
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43230 * 0.66397498
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83229 * 0.95749684
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16797 * 0.13976348
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51852 * 0.93564808
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60719 * 0.91752258
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 51047 * 0.89925849
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 24326 * 0.80243197
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4907 * 0.56612242
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 56573 * 0.26058547
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 98594 * 0.90764575
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 79218 * 0.23740961
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 10547 * 0.81876247
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 64260 * 0.00281680
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'mlglpkrl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0066():
    """Extended test 66 for transcoding."""
    x_0 = 90254 * 0.24777597
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25681 * 0.78129503
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18530 * 0.01126637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57270 * 0.95797126
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5237 * 0.22667115
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59693 * 0.13057473
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72674 * 0.10987505
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68593 * 0.14374205
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76602 * 0.83771596
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87883 * 0.99391169
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2595 * 0.14323982
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76865 * 0.02688427
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14913 * 0.97208874
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86935 * 0.96064217
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96855 * 0.90060756
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45246 * 0.20728696
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59219 * 0.81914269
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16894 * 0.33699104
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76791 * 0.25816515
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18868 * 0.39069717
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6384 * 0.09436577
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45572 * 0.25654473
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77846 * 0.93048469
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14465 * 0.87738625
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'cjkwpvrl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0067():
    """Extended test 67 for transcoding."""
    x_0 = 54859 * 0.63837290
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22841 * 0.17005737
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1646 * 0.17809779
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65645 * 0.57879060
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74728 * 0.32063488
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19397 * 0.44617531
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34061 * 0.12751450
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39539 * 0.02060074
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41149 * 0.72053848
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28191 * 0.99571244
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92667 * 0.03389254
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72690 * 0.46475866
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99076 * 0.41005914
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9774 * 0.02899078
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57646 * 0.41370330
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76661 * 0.23377262
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63623 * 0.96990165
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1381 * 0.20123206
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90614 * 0.09759821
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33642 * 0.17253255
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88702 * 0.10169424
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48105 * 0.07168801
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23211 * 0.33907559
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96775 * 0.93613025
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63809 * 0.11000952
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59250 * 0.81048100
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6635 * 0.00387322
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39142 * 0.68253765
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1926 * 0.30702924
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55584 * 0.57179266
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14506 * 0.93519260
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47522 * 0.36658584
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76568 * 0.33727922
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69256 * 0.50549160
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81130 * 0.24906341
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4667 * 0.52790100
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48228 * 0.60859699
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47095 * 0.33874300
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12499 * 0.75248899
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3762 * 0.07609694
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71638 * 0.66274963
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'xzfapjvp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0068():
    """Extended test 68 for transcoding."""
    x_0 = 33023 * 0.36183984
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95119 * 0.59808409
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60765 * 0.69992181
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11248 * 0.81342157
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51146 * 0.93337238
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66154 * 0.39105407
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44347 * 0.94152411
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96009 * 0.86144568
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36987 * 0.72743107
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88920 * 0.40478060
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38708 * 0.40942289
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65150 * 0.74186054
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35570 * 0.97139063
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93978 * 0.56411745
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79136 * 0.88566796
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34147 * 0.33731042
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26867 * 0.52013514
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81938 * 0.59043440
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74307 * 0.31070489
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56724 * 0.27129884
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'nqfhmymn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_0_0069():
    """Extended test 69 for transcoding."""
    x_0 = 49969 * 0.53561722
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24754 * 0.29973250
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87313 * 0.67931165
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84907 * 0.37095042
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54403 * 0.45185072
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27188 * 0.09251884
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34328 * 0.03886154
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88296 * 0.24091034
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13724 * 0.46084200
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99921 * 0.95068388
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63531 * 0.13313638
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50750 * 0.39072536
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85231 * 0.45695060
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50962 * 0.46863825
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74581 * 0.09514160
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48884 * 0.07026709
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88323 * 0.07246874
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26298 * 0.54138767
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45164 * 0.89982323
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16687 * 0.67341405
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57527 * 0.18731061
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90443 * 0.58237435
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77300 * 0.64591682
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19522 * 0.69399434
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46122 * 0.32512807
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63339 * 0.71398818
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41556 * 0.16101678
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23624 * 0.54775540
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70560 * 0.92799270
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86455 * 0.90476489
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91306 * 0.71288623
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2451 * 0.63455087
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55218 * 0.89667920
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'eqyzrxcw').hexdigest()
    assert len(h) == 64
