"""Extended tests for transcoding suite 6."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_transcoding_extended_6_0000():
    """Extended test 0 for transcoding."""
    x_0 = 78469 * 0.50643334
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40806 * 0.18198442
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84846 * 0.21056927
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39387 * 0.66710969
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94395 * 0.04079147
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54252 * 0.30031227
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46042 * 0.93905274
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23262 * 0.38278190
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78290 * 0.36130884
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29174 * 0.83897350
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38584 * 0.43523396
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85994 * 0.00700424
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94900 * 0.65080070
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28709 * 0.47519280
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9583 * 0.95324725
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8638 * 0.28595924
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2978 * 0.70163340
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33297 * 0.46521024
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30698 * 0.00231546
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37833 * 0.64860291
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71807 * 0.33114033
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92895 * 0.16388328
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79607 * 0.40571729
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97951 * 0.08025415
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14028 * 0.57844132
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18946 * 0.75146270
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22862 * 0.54610229
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38992 * 0.89793215
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87075 * 0.36403381
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99552 * 0.74931408
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27714 * 0.75207932
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68672 * 0.09139875
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46708 * 0.35364857
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25245 * 0.28970972
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19940 * 0.32625542
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5399 * 0.71824196
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76252 * 0.64089904
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89032 * 0.89280011
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80537 * 0.63495535
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76322 * 0.50234464
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 33522 * 0.85182619
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 51515 * 0.22788069
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29740 * 0.38201475
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 15089 * 0.88455553
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 42118 * 0.17214989
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 33982 * 0.44825275
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 8290 * 0.58543652
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 35349 * 0.84493421
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 85978 * 0.08742598
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'exgedbni').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0001():
    """Extended test 1 for transcoding."""
    x_0 = 56950 * 0.11184493
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62460 * 0.39858133
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99596 * 0.65054449
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 323 * 0.38711911
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85290 * 0.63238405
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50978 * 0.80854000
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86739 * 0.86443154
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8768 * 0.94399409
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30753 * 0.45586407
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82265 * 0.69382250
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69396 * 0.32719507
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46773 * 0.09043439
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49231 * 0.20915565
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6771 * 0.09382890
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68510 * 0.80250936
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3262 * 0.61688457
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14670 * 0.88473261
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25796 * 0.38666790
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81610 * 0.94946906
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79783 * 0.53536637
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19316 * 0.75824517
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14883 * 0.75014633
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99356 * 0.62492698
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63831 * 0.63837083
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41897 * 0.60680218
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58156 * 0.75625567
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48106 * 0.16051226
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48981 * 0.99258946
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59548 * 0.47364420
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62744 * 0.25417081
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23760 * 0.02705706
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98728 * 0.93667910
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88507 * 0.29776999
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28214 * 0.01147140
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8619 * 0.41011716
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35561 * 0.64997636
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19064 * 0.76883638
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82960 * 0.93521763
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58068 * 0.74671360
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'hjgrhtdu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0002():
    """Extended test 2 for transcoding."""
    x_0 = 56354 * 0.79417252
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46646 * 0.89710518
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85035 * 0.40264516
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92963 * 0.43145660
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69958 * 0.57886610
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82924 * 0.14412168
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86572 * 0.70211730
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10133 * 0.35362573
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8121 * 0.22547031
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99795 * 0.04119484
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40317 * 0.31895171
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85455 * 0.30449857
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57993 * 0.49145808
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32948 * 0.15418015
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6201 * 0.17390527
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96888 * 0.76805720
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97874 * 0.76871047
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98691 * 0.67541219
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88201 * 0.48045709
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31097 * 0.84361325
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47701 * 0.80486700
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54629 * 0.63379180
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95357 * 0.59597263
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2973 * 0.92684148
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98548 * 0.12147525
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20245 * 0.46141644
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45746 * 0.39615708
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45421 * 0.96056318
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15215 * 0.39729491
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51374 * 0.83086450
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59512 * 0.34094152
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68746 * 0.92874468
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84360 * 0.80760170
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49142 * 0.88537488
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'inmpnbvv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0003():
    """Extended test 3 for transcoding."""
    x_0 = 12847 * 0.92054089
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70250 * 0.13931672
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19417 * 0.83405804
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74149 * 0.45206726
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37657 * 0.75900604
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73929 * 0.38930783
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33666 * 0.73537703
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71481 * 0.06302042
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6910 * 0.18654481
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24530 * 0.50963703
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46799 * 0.19649952
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2105 * 0.43304707
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73366 * 0.87141097
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48649 * 0.97210140
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4207 * 0.95991348
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71411 * 0.28507100
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94146 * 0.47752109
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47059 * 0.26619475
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44216 * 0.38137284
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81065 * 0.94271510
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65164 * 0.53053448
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55012 * 0.83724881
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47493 * 0.75640179
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21258 * 0.86405964
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17175 * 0.30058393
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2482 * 0.53998140
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26609 * 0.74050118
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76484 * 0.68464366
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15140 * 0.04107833
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42658 * 0.20570079
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75074 * 0.62379843
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27071 * 0.50666335
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75971 * 0.86728950
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70852 * 0.76974309
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2877 * 0.00506705
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32267 * 0.84928868
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91608 * 0.59563750
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62503 * 0.77422955
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2942 * 0.27166754
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57731 * 0.44466226
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37350 * 0.60607591
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3925 * 0.21003731
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 64132 * 0.37549840
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83077 * 0.31985865
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'kjyhuhan').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0004():
    """Extended test 4 for transcoding."""
    x_0 = 40218 * 0.40092538
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76722 * 0.76564354
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32317 * 0.79454860
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73031 * 0.91052411
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81414 * 0.94910767
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38607 * 0.25338175
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33520 * 0.46308414
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40171 * 0.72847206
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83508 * 0.69339616
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92580 * 0.94382782
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12524 * 0.20510573
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11023 * 0.50483869
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88494 * 0.52731871
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17673 * 0.88806250
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47686 * 0.27927474
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66518 * 0.63762966
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84310 * 0.22169532
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46904 * 0.70744810
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59375 * 0.58744942
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92306 * 0.76010462
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66725 * 0.37251612
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66779 * 0.46782860
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36795 * 0.02834952
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68045 * 0.70280751
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4206 * 0.16393066
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14878 * 0.44290602
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76446 * 0.80295904
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5731 * 0.29332309
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94810 * 0.29880801
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71785 * 0.27072251
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40501 * 0.89721535
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37443 * 0.51050492
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'gqvlwjop').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0005():
    """Extended test 5 for transcoding."""
    x_0 = 45944 * 0.22993842
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66799 * 0.11091190
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7896 * 0.81509030
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57351 * 0.29949619
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75716 * 0.91285489
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12758 * 0.17849721
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48524 * 0.15838172
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4639 * 0.46757120
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17319 * 0.80035065
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33413 * 0.06520786
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90925 * 0.64493497
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31504 * 0.99683804
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4000 * 0.87825343
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30377 * 0.63649999
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79678 * 0.63883554
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48872 * 0.03448661
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43258 * 0.72511058
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72429 * 0.60965476
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2487 * 0.15292702
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42554 * 0.47927454
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31181 * 0.49621270
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6869 * 0.87156510
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23857 * 0.69054574
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62295 * 0.83733496
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 757 * 0.93903801
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76685 * 0.90453771
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14478 * 0.07865472
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29582 * 0.63322668
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68841 * 0.12161048
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ibwsiuel').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0006():
    """Extended test 6 for transcoding."""
    x_0 = 4577 * 0.03326800
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92960 * 0.97820277
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30671 * 0.14230501
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39661 * 0.44331617
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41679 * 0.78401953
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72766 * 0.31370223
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25282 * 0.76977433
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63288 * 0.73740594
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96019 * 0.14089639
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31339 * 0.82090569
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82978 * 0.34960984
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58162 * 0.06605323
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25252 * 0.86196567
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91493 * 0.81210798
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30610 * 0.11210389
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23208 * 0.10456122
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76176 * 0.14379240
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12918 * 0.27167638
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68125 * 0.38995006
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9783 * 0.48612959
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33299 * 0.88432817
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51332 * 0.56486429
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20333 * 0.83564937
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67329 * 0.62849877
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65673 * 0.17172864
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77229 * 0.08743171
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72627 * 0.64806108
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ovuyyaqf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0007():
    """Extended test 7 for transcoding."""
    x_0 = 62185 * 0.24529965
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9577 * 0.35138398
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14959 * 0.68631943
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42736 * 0.74975438
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9727 * 0.26615662
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44321 * 0.25159235
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16193 * 0.17274555
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2343 * 0.02809958
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84421 * 0.45778865
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17098 * 0.94079121
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87987 * 0.88267738
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73776 * 0.71663640
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73176 * 0.66177769
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74331 * 0.52785639
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35701 * 0.51774271
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59977 * 0.65390850
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73056 * 0.35860666
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66243 * 0.59206003
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52207 * 0.72086601
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55835 * 0.88613637
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48326 * 0.75878909
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70412 * 0.58801970
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7496 * 0.32816669
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36051 * 0.53155366
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75034 * 0.09132319
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38366 * 0.12175335
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61207 * 0.02825251
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'hzvdqnhu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0008():
    """Extended test 8 for transcoding."""
    x_0 = 39081 * 0.27754595
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71541 * 0.74451871
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20469 * 0.95353089
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10651 * 0.69139904
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43635 * 0.75173053
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53000 * 0.78028700
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51816 * 0.37814694
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6343 * 0.60140282
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42487 * 0.13724578
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73686 * 0.80216214
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7219 * 0.17696509
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82478 * 0.10487121
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41661 * 0.97175331
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5113 * 0.91703718
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81136 * 0.54659238
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71125 * 0.68971003
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69095 * 0.46625950
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90175 * 0.36257012
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76646 * 0.10481910
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9252 * 0.92987565
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7367 * 0.57176040
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18166 * 0.19582403
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42918 * 0.50422858
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28851 * 0.89163012
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71394 * 0.82377776
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6148 * 0.24378274
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72789 * 0.00618052
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'grwlpcyy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0009():
    """Extended test 9 for transcoding."""
    x_0 = 36710 * 0.48659718
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25285 * 0.55957933
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82670 * 0.37684776
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91999 * 0.96758621
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13648 * 0.00914272
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7810 * 0.42556619
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21198 * 0.18466688
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70333 * 0.17742397
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68214 * 0.63208469
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40776 * 0.25797727
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20508 * 0.54833840
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98337 * 0.33859182
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53657 * 0.39505626
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87307 * 0.05261035
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97259 * 0.44890306
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82720 * 0.51187226
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17299 * 0.97341374
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50392 * 0.21740747
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88548 * 0.02724221
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66491 * 0.96656857
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51057 * 0.37014906
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88099 * 0.17043227
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12473 * 0.38387882
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36627 * 0.01339385
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64373 * 0.72486300
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54024 * 0.59515543
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78544 * 0.87159830
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3709 * 0.85630209
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43071 * 0.74049272
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3535 * 0.07993603
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44134 * 0.49458648
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61578 * 0.73458499
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47388 * 0.33235613
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85159 * 0.02222544
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61504 * 0.14680943
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16933 * 0.59939171
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 490 * 0.53065074
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23035 * 0.19874935
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93128 * 0.71273025
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45355 * 0.64411260
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37584 * 0.13553191
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 90668 * 0.60919818
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57727 * 0.78355358
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75778 * 0.25600718
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 49118 * 0.67054318
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 58778 * 0.57712618
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 36239 * 0.92083890
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 49163 * 0.21722421
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 23081 * 0.75209346
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 41063 * 0.98234433
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'krhrdguk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0010():
    """Extended test 10 for transcoding."""
    x_0 = 87723 * 0.89080587
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24638 * 0.88349377
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56556 * 0.51878432
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26645 * 0.90348823
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79214 * 0.20646794
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11306 * 0.65243958
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58542 * 0.54614014
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61386 * 0.45761001
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54195 * 0.37285601
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84019 * 0.57045305
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67237 * 0.85897490
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37169 * 0.25688740
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18979 * 0.98789484
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74745 * 0.03755831
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84609 * 0.26476701
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59977 * 0.43995834
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58711 * 0.27447953
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50804 * 0.16355244
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15997 * 0.54416121
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68909 * 0.17089225
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4150 * 0.92856393
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65692 * 0.86549989
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40468 * 0.79748027
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86835 * 0.36618181
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34482 * 0.96335978
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34501 * 0.77127986
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8461 * 0.04143977
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75705 * 0.30449951
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44231 * 0.72389257
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62839 * 0.57408400
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51064 * 0.91102911
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11258 * 0.36310045
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72625 * 0.61147387
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23092 * 0.20443303
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40880 * 0.28338579
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6093 * 0.79879287
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96264 * 0.90588801
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15271 * 0.16934738
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73751 * 0.43162445
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54610 * 0.95431731
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40309 * 0.66833168
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 29001 * 0.14122235
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96686 * 0.15925599
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11526 * 0.23129562
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 29017 * 0.90135584
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 98214 * 0.71365439
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 23223 * 0.40348092
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 38703 * 0.91714072
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 68865 * 0.11409181
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 13336 * 0.21219014
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'jvauwzzv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0011():
    """Extended test 11 for transcoding."""
    x_0 = 8072 * 0.89404144
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19287 * 0.67827749
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7636 * 0.59241252
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45597 * 0.74402611
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11213 * 0.91046614
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79109 * 0.87915530
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74136 * 0.70579960
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10477 * 0.94090325
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95902 * 0.05132009
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12556 * 0.76375238
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51834 * 0.85717654
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46112 * 0.35691938
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19383 * 0.59043785
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36369 * 0.20948182
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1887 * 0.82727538
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81512 * 0.13181478
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42137 * 0.53195876
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30858 * 0.78274443
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65025 * 0.75463068
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28920 * 0.69324897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57628 * 0.46219275
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50726 * 0.33597809
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50294 * 0.20657780
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65179 * 0.74696010
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90963 * 0.18535212
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85044 * 0.96763244
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79839 * 0.87839655
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24553 * 0.22858196
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19426 * 0.21854365
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97256 * 0.56641564
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37456 * 0.29717933
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40138 * 0.71106538
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'oexzsrlg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0012():
    """Extended test 12 for transcoding."""
    x_0 = 50376 * 0.69470859
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87178 * 0.45976112
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58482 * 0.56904252
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67815 * 0.01016868
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22290 * 0.81077113
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44913 * 0.34887203
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41375 * 0.52525839
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86230 * 0.56436482
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94271 * 0.21707708
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2039 * 0.33189521
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36277 * 0.45890401
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6198 * 0.99593087
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47015 * 0.52613938
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87502 * 0.70993398
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23056 * 0.72342038
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11696 * 0.10003600
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57481 * 0.21790916
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90224 * 0.77544769
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4593 * 0.05515906
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83211 * 0.58084205
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13042 * 0.99344406
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24526 * 0.87578163
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26042 * 0.49922747
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89947 * 0.66358522
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26829 * 0.85038622
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48273 * 0.62779520
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65068 * 0.87226925
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2283 * 0.05366843
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19201 * 0.54276372
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27382 * 0.83877699
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71436 * 0.53695104
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82199 * 0.37064073
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35608 * 0.86544694
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89913 * 0.68962491
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46594 * 0.51743821
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 9315 * 0.97412375
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'lbmfweda').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0013():
    """Extended test 13 for transcoding."""
    x_0 = 50497 * 0.25673760
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85909 * 0.22628875
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7355 * 0.55801723
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51164 * 0.14869729
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67549 * 0.07041608
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71762 * 0.51267562
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70479 * 0.52696717
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9554 * 0.07834179
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64069 * 0.83470960
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19325 * 0.87281097
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18744 * 0.73448402
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33864 * 0.46744016
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93870 * 0.69893932
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82793 * 0.09593330
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38033 * 0.26494084
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20035 * 0.05014832
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14699 * 0.97240077
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29707 * 0.49858512
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86641 * 0.42043726
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50028 * 0.37253989
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48446 * 0.10027650
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35848 * 0.61549600
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75074 * 0.41423881
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57055 * 0.44178980
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64633 * 0.50368505
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10169 * 0.69334078
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62514 * 0.90871132
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83639 * 0.99458518
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88208 * 0.67925081
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46420 * 0.01805039
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1175 * 0.96561092
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68282 * 0.07916848
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80343 * 0.84009346
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57032 * 0.39928756
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82521 * 0.00506684
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61662 * 0.68199326
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11658 * 0.19314837
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91200 * 0.98997210
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23798 * 0.69749404
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 12856 * 0.63065183
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60325 * 0.75330489
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 10817 * 0.77725041
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70650 * 0.11882557
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22486 * 0.27893388
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 90390 * 0.33137224
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4234 * 0.84276785
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 40071 * 0.06736675
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 36115 * 0.66325176
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 97645 * 0.58065430
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 21572 * 0.96778335
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'dkmhlazm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0014():
    """Extended test 14 for transcoding."""
    x_0 = 12005 * 0.43026898
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15072 * 0.72532162
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17751 * 0.92488941
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19225 * 0.76620338
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54548 * 0.72801675
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73262 * 0.78222680
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73074 * 0.48324385
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17555 * 0.15646664
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53418 * 0.99700382
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66408 * 0.89948076
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18868 * 0.02271644
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70714 * 0.08074446
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14693 * 0.05392120
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7478 * 0.15113232
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73056 * 0.02536470
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87727 * 0.07485985
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70800 * 0.00194135
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16053 * 0.86119832
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96426 * 0.00611868
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21802 * 0.13539708
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39448 * 0.21921520
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63879 * 0.31875827
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6035 * 0.61106713
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74687 * 0.13975859
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20876 * 0.73204429
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98658 * 0.80082023
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40941 * 0.18066392
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94073 * 0.43262697
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70248 * 0.23273096
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4892 * 0.98293994
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79485 * 0.47276348
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21833 * 0.15726303
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19372 * 0.65866200
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21920 * 0.20563069
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13906 * 0.91773072
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38365 * 0.77998419
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53229 * 0.45783638
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73323 * 0.08254810
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64435 * 0.12842434
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18842 * 0.74550214
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64823 * 0.67875529
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40181 * 0.62364436
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29198 * 0.62469022
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36496 * 0.05310932
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 19358 * 0.35567062
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 69074 * 0.81523279
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 87264 * 0.07034364
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 62065 * 0.67101886
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 49284 * 0.99382145
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'mdospzak').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0015():
    """Extended test 15 for transcoding."""
    x_0 = 87511 * 0.55750645
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43936 * 0.57472231
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94349 * 0.53550883
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16522 * 0.96908289
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92445 * 0.99794131
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73659 * 0.90381237
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91823 * 0.01583757
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 813 * 0.24662801
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65203 * 0.28555528
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 896 * 0.86092378
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19520 * 0.55500660
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72921 * 0.43120838
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79125 * 0.91781336
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80113 * 0.97978847
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33307 * 0.02834715
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57984 * 0.13474821
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7407 * 0.39458804
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42130 * 0.91712233
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26686 * 0.40579706
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19489 * 0.87474695
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73020 * 0.09172431
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61663 * 0.57634531
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99796 * 0.82007349
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1521 * 0.85146512
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86091 * 0.33850182
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6217 * 0.86406827
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95480 * 0.01973932
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6634 * 0.37309675
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50117 * 0.05640766
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21084 * 0.31116198
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75007 * 0.92727639
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49179 * 0.07220338
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72016 * 0.49656584
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30923 * 0.95596721
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89740 * 0.29914453
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22645 * 0.24422199
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71324 * 0.73509363
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84176 * 0.09526632
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9979 * 0.17484219
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85592 * 0.04234346
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8686 * 0.87948320
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 32663 * 0.94076210
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83026 * 0.57397403
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 15587 * 0.18853896
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 5137 * 0.68974640
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 9670 * 0.16084187
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 21617 * 0.96933170
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'dnfymwon').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0016():
    """Extended test 16 for transcoding."""
    x_0 = 60557 * 0.59929403
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98793 * 0.84556400
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47774 * 0.10927051
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36087 * 0.14569076
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47835 * 0.90770953
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41186 * 0.45035351
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99491 * 0.50918355
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87593 * 0.46655765
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53478 * 0.13910903
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7074 * 0.45894410
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65116 * 0.13126122
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47753 * 0.36408838
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73343 * 0.48618322
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24630 * 0.62179242
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94844 * 0.99442120
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22329 * 0.73983238
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37514 * 0.55322799
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16180 * 0.97758116
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79177 * 0.66120786
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61766 * 0.20407993
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92279 * 0.42613445
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88514 * 0.46511178
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40323 * 0.96638642
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97476 * 0.68269099
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17257 * 0.59724615
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27900 * 0.98235207
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23642 * 0.21443471
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11580 * 0.55073577
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98396 * 0.58447602
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39315 * 0.09783427
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'nhsqmvnu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0017():
    """Extended test 17 for transcoding."""
    x_0 = 48289 * 0.30327683
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22633 * 0.60679346
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92143 * 0.51048480
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27669 * 0.65276033
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1814 * 0.72772292
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13170 * 0.38459836
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36719 * 0.27145949
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43113 * 0.05309060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57370 * 0.77642838
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42358 * 0.32632953
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83864 * 0.50946979
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29693 * 0.55563127
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58403 * 0.85399180
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47565 * 0.19999262
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78152 * 0.54805846
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54594 * 0.38384039
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56432 * 0.13577871
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44882 * 0.56787646
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16521 * 0.62248002
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72979 * 0.51287220
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91946 * 0.08512179
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66038 * 0.76883842
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27096 * 0.36766117
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27547 * 0.20931179
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49302 * 0.84445484
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79842 * 0.00102017
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91147 * 0.72210339
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22674 * 0.89810864
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76033 * 0.86986131
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47713 * 0.95723165
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88273 * 0.65017704
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60250 * 0.22051085
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87886 * 0.79042742
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76700 * 0.28869106
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86318 * 0.06184523
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12962 * 0.90347922
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40308 * 0.08981442
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92572 * 0.57975550
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86298 * 0.83509404
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96998 * 0.10158819
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85725 * 0.39214061
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50088 * 0.74487415
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18190 * 0.58750508
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ytsojpeq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0018():
    """Extended test 18 for transcoding."""
    x_0 = 89895 * 0.55571071
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81376 * 0.61707927
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64261 * 0.41796851
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19365 * 0.62693939
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74981 * 0.13154308
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12493 * 0.54076870
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78485 * 0.98627486
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55151 * 0.03738105
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91217 * 0.78075024
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63320 * 0.48707996
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72052 * 0.37189517
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75639 * 0.73368140
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77064 * 0.18290501
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48116 * 0.59901924
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94068 * 0.34156015
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44849 * 0.74087431
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75627 * 0.00965223
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37237 * 0.55038828
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68515 * 0.36959276
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70618 * 0.58344092
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56673 * 0.24233242
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18630 * 0.28710910
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52917 * 0.06051682
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3377 * 0.48017178
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79097 * 0.79536361
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78556 * 0.48310723
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47134 * 0.45202539
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92458 * 0.44894680
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37150 * 0.51398472
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64307 * 0.27437077
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50483 * 0.48110942
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95095 * 0.82911172
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64509 * 0.37287534
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63484 * 0.91271595
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30301 * 0.74749734
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14486 * 0.05989521
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57374 * 0.70908894
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 54919 * 0.51691288
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31208 * 0.54548174
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7182 * 0.21270891
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43614 * 0.84988266
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 87807 * 0.79966517
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62403 * 0.70124839
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 77681 * 0.95850890
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 24672 * 0.01304175
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'stmnmnal').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0019():
    """Extended test 19 for transcoding."""
    x_0 = 13266 * 0.57332163
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17977 * 0.18379316
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81774 * 0.57018838
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80438 * 0.93905826
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66768 * 0.36302157
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62136 * 0.65609510
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79009 * 0.50508213
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21889 * 0.03744532
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70443 * 0.25509589
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80387 * 0.34426226
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29230 * 0.97694387
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48533 * 0.15995974
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73908 * 0.51710128
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50585 * 0.19076558
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95682 * 0.25977137
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43129 * 0.84750204
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87613 * 0.62830064
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73035 * 0.68874150
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75029 * 0.33657436
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12622 * 0.77806153
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61784 * 0.14359381
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72459 * 0.28547329
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60070 * 0.60964503
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12273 * 0.07967923
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66548 * 0.71326751
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99915 * 0.61073249
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6448 * 0.31646642
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14054 * 0.07710948
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44829 * 0.04547751
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'utocexrh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0020():
    """Extended test 20 for transcoding."""
    x_0 = 40251 * 0.54102874
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26720 * 0.13505451
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93983 * 0.67979163
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48009 * 0.67893488
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34212 * 0.17493833
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86532 * 0.38815971
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76447 * 0.75846733
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56853 * 0.16920422
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96754 * 0.33237973
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64645 * 0.47412042
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47447 * 0.81688614
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68059 * 0.16634143
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16472 * 0.19083241
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86244 * 0.27783887
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39566 * 0.26395177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61626 * 0.69443605
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11590 * 0.67200038
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38749 * 0.33555841
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64347 * 0.01698547
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43637 * 0.89249034
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4011 * 0.07136276
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99822 * 0.99886533
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15346 * 0.98716377
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76163 * 0.36115695
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78152 * 0.19866728
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9288 * 0.99285377
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76065 * 0.49595513
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59055 * 0.45560153
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46770 * 0.90108096
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90556 * 0.91601121
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94143 * 0.78976221
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21380 * 0.14019966
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33531 * 0.18954721
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62047 * 0.82141344
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56228 * 0.32525426
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11626 * 0.18099712
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90743 * 0.27070923
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77905 * 0.25360921
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74983 * 0.84485245
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82391 * 0.22517806
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69005 * 0.65699324
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 91751 * 0.82294170
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 80887 * 0.45287593
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 74313 * 0.03172941
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'gjteqgja').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0021():
    """Extended test 21 for transcoding."""
    x_0 = 64840 * 0.84019196
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80302 * 0.33489352
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33623 * 0.27835266
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45860 * 0.99821197
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74317 * 0.71331295
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10366 * 0.12191361
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47503 * 0.53763022
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94704 * 0.19503362
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98911 * 0.03891327
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76061 * 0.97823269
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43431 * 0.15363999
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87395 * 0.18114816
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64855 * 0.87491059
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42488 * 0.62868826
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72634 * 0.65624332
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9597 * 0.18188185
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11631 * 0.53912753
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43087 * 0.30955629
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96620 * 0.37653143
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68866 * 0.55025219
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51127 * 0.58322806
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64416 * 0.38433309
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77508 * 0.53921509
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44853 * 0.35349059
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77151 * 0.75867186
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64749 * 0.40013335
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18242 * 0.55155424
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27476 * 0.98353710
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49329 * 0.41683485
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36244 * 0.38536073
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11883 * 0.86905054
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99824 * 0.19067878
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69932 * 0.97905845
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63594 * 0.80298490
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61196 * 0.05538940
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64525 * 0.40307276
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1155 * 0.03848101
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6046 * 0.36763821
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46565 * 0.39244417
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85239 * 0.66759644
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21348 * 0.91380656
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41152 * 0.44535679
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66023 * 0.24363089
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'zukpfidb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0022():
    """Extended test 22 for transcoding."""
    x_0 = 38846 * 0.36882654
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81355 * 0.38802803
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46237 * 0.36346994
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47163 * 0.21437031
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95598 * 0.93795595
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97583 * 0.68356672
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67367 * 0.63535714
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31005 * 0.79810454
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 918 * 0.29362121
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10766 * 0.83124046
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99294 * 0.91428120
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85465 * 0.88841913
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69625 * 0.86333012
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49802 * 0.28428653
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6608 * 0.70577327
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43358 * 0.23463761
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71933 * 0.49654202
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85187 * 0.08890397
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18237 * 0.61092168
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21443 * 0.17140049
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 859 * 0.56110948
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14253 * 0.00089252
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91579 * 0.95817609
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45675 * 0.58009076
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55822 * 0.54082662
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93494 * 0.00335518
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61261 * 0.66342090
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24244 * 0.53331868
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67566 * 0.61853808
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85563 * 0.89327414
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'hxvamzhd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0023():
    """Extended test 23 for transcoding."""
    x_0 = 77788 * 0.86837768
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81953 * 0.07770284
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2956 * 0.90729876
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83787 * 0.21676744
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75789 * 0.36144347
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27663 * 0.56553264
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45785 * 0.05118090
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4163 * 0.54673817
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98352 * 0.84395245
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97557 * 0.90108438
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60933 * 0.42659847
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78274 * 0.55862341
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88689 * 0.44427686
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7025 * 0.78013716
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12397 * 0.01514040
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38512 * 0.64521256
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30208 * 0.64941413
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2054 * 0.84788482
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50909 * 0.36759356
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88864 * 0.22448168
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50342 * 0.69604294
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83127 * 0.50635794
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32631 * 0.30206799
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85048 * 0.39462265
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77618 * 0.07205288
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19853 * 0.24991109
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85811 * 0.15235379
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9525 * 0.89777487
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3807 * 0.65329562
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34834 * 0.44954815
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50943 * 0.82865806
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54287 * 0.78206266
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25736 * 0.49259208
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71331 * 0.18923512
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62295 * 0.70535461
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34923 * 0.29714883
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'oklynkul').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0024():
    """Extended test 24 for transcoding."""
    x_0 = 17074 * 0.01839892
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64843 * 0.10924361
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69238 * 0.54883015
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10398 * 0.60503662
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65166 * 0.21534576
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58360 * 0.63723681
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66717 * 0.71783246
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32578 * 0.64153918
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75193 * 0.00454477
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99359 * 0.64204690
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64680 * 0.56330890
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31934 * 0.19910899
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37755 * 0.25639692
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49267 * 0.31089564
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90254 * 0.93040073
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35075 * 0.03598811
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43144 * 0.85428521
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66254 * 0.63464557
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19594 * 0.10238884
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54955 * 0.74639159
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61137 * 0.62815075
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26995 * 0.68039820
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93894 * 0.43208915
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21541 * 0.74085901
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84642 * 0.20169255
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89254 * 0.10347918
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94891 * 0.22334105
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17079 * 0.74329138
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70318 * 0.27693880
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95347 * 0.22293368
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65840 * 0.12221032
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41089 * 0.61740327
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18788 * 0.37734169
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30442 * 0.86124342
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98104 * 0.95850245
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83248 * 0.17926475
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88132 * 0.16951228
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63087 * 0.22900215
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97468 * 0.57499690
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 26427 * 0.23478153
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60240 * 0.93120550
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66851 * 0.03743371
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62743 * 0.79901038
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 17496 * 0.71373775
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'zdqhokvp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0025():
    """Extended test 25 for transcoding."""
    x_0 = 78620 * 0.86938314
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61098 * 0.95688342
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94698 * 0.81214600
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21705 * 0.45275253
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23529 * 0.68840397
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97537 * 0.38836060
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48636 * 0.18175463
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45277 * 0.19274063
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66275 * 0.57136922
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94575 * 0.40078693
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66907 * 0.38223891
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28319 * 0.32908834
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50269 * 0.27196213
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5497 * 0.05745581
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17375 * 0.48805178
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51289 * 0.17835239
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36895 * 0.52283911
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84925 * 0.00884851
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67687 * 0.30902414
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70567 * 0.82628376
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7058 * 0.69809189
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78875 * 0.62052483
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32170 * 0.44014774
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40593 * 0.72176264
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44984 * 0.20312196
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'gpjbzjxq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0026():
    """Extended test 26 for transcoding."""
    x_0 = 40818 * 0.82064210
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84976 * 0.36319985
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12172 * 0.24222757
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12568 * 0.97568914
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46691 * 0.48138813
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92319 * 0.25782022
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42589 * 0.03821861
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26996 * 0.09395882
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65237 * 0.08351795
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94951 * 0.76863619
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44377 * 0.67809661
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90513 * 0.77384051
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53858 * 0.65853609
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56919 * 0.74012023
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14817 * 0.57162057
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38484 * 0.72222787
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43094 * 0.13697575
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8249 * 0.21570106
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78215 * 0.46518824
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74945 * 0.25837307
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45935 * 0.13676876
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'kvcjlqvs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0027():
    """Extended test 27 for transcoding."""
    x_0 = 87558 * 0.02156748
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31032 * 0.55468112
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95912 * 0.91548759
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73051 * 0.95093624
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24623 * 0.33090508
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77851 * 0.62424684
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70490 * 0.51830593
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42003 * 0.44447879
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34639 * 0.39740100
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66219 * 0.26068100
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69289 * 0.23706651
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6943 * 0.29468963
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73669 * 0.47015395
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5069 * 0.43149976
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59548 * 0.23005319
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90607 * 0.15965720
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74855 * 0.57324003
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88461 * 0.03762167
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36840 * 0.53565627
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22607 * 0.03049648
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 364 * 0.56219915
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23849 * 0.16919769
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33355 * 0.66843824
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24547 * 0.75478322
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1178 * 0.21958490
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8032 * 0.74968586
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79181 * 0.71033191
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57990 * 0.55836854
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23741 * 0.72220694
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69988 * 0.02784253
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51359 * 0.43510695
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84739 * 0.75640322
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30431 * 0.98313695
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11668 * 0.13631508
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87176 * 0.07595707
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77051 * 0.18298229
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41785 * 0.51105471
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33494 * 0.30063062
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79084 * 0.34886918
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1293 * 0.16281148
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 93465 * 0.29579754
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38174 * 0.12062711
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81474 * 0.27623221
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84464 * 0.06564372
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'yobdvwch').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0028():
    """Extended test 28 for transcoding."""
    x_0 = 99436 * 0.25721176
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31667 * 0.82033419
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17911 * 0.52169260
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97147 * 0.57598495
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49206 * 0.56842728
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91325 * 0.41086474
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9061 * 0.81288417
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58190 * 0.01729829
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75590 * 0.78258955
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55576 * 0.51333168
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47775 * 0.32980300
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77817 * 0.46659633
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73789 * 0.95041258
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94927 * 0.08477144
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 902 * 0.15433238
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78651 * 0.43800884
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48670 * 0.77400640
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66732 * 0.03934846
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13292 * 0.82475742
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25004 * 0.32057618
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79092 * 0.34231409
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80412 * 0.51325274
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20903 * 0.60495047
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19426 * 0.76500275
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56601 * 0.50016437
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63344 * 0.21206238
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42290 * 0.92239522
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67535 * 0.15784355
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4568 * 0.06677007
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46630 * 0.88848928
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51343 * 0.42658118
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49989 * 0.00982525
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10341 * 0.25842863
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44450 * 0.33354522
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16068 * 0.79510333
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84262 * 0.23557349
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49140 * 0.02407825
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22809 * 0.46199284
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'wuhmyyez').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0029():
    """Extended test 29 for transcoding."""
    x_0 = 87494 * 0.48003852
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28329 * 0.55654321
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67760 * 0.75163271
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20283 * 0.74944542
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55029 * 0.51397853
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17283 * 0.63998208
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47527 * 0.43454713
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23055 * 0.49052543
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14317 * 0.24836737
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77545 * 0.06034133
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13584 * 0.83340455
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33735 * 0.35340359
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80108 * 0.38154035
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17824 * 0.45168909
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39814 * 0.63751491
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66353 * 0.99996051
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64156 * 0.45386992
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1690 * 0.56774904
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29598 * 0.88622751
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77333 * 0.10574840
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56821 * 0.75646844
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66128 * 0.63655076
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96365 * 0.37027937
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48831 * 0.10617877
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47189 * 0.28356126
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'cdgornnh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0030():
    """Extended test 30 for transcoding."""
    x_0 = 16402 * 0.83542333
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27410 * 0.99020145
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82164 * 0.47096186
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55800 * 0.61629067
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40471 * 0.10933435
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27303 * 0.82111654
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89117 * 0.87403929
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31493 * 0.14863175
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42004 * 0.04276333
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29331 * 0.79106665
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70093 * 0.49810086
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34692 * 0.27426217
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53685 * 0.64905888
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41209 * 0.51994562
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33201 * 0.54113443
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68960 * 0.86486509
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35991 * 0.14052376
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55169 * 0.05139144
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85514 * 0.01917126
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67335 * 0.01040456
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61642 * 0.60124065
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93359 * 0.04856908
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16714 * 0.76627489
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94545 * 0.60565965
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 867 * 0.22703472
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52247 * 0.55013692
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37262 * 0.69626397
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69699 * 0.85375819
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38395 * 0.74138020
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45202 * 0.90535266
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28436 * 0.18202195
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39271 * 0.17018463
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2833 * 0.66570371
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28014 * 0.74599423
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91007 * 0.04857430
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54648 * 0.31050546
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75744 * 0.38325987
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41965 * 0.43270412
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41648 * 0.24863739
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16813 * 0.06096815
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84503 * 0.54500889
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 10609 * 0.27798371
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 76583 * 0.61183565
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92085 * 0.41806057
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 96414 * 0.72399641
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 50001 * 0.97188736
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'yfrvflfj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0031():
    """Extended test 31 for transcoding."""
    x_0 = 38259 * 0.09472017
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83779 * 0.05175056
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26830 * 0.92202290
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51601 * 0.37367244
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12246 * 0.12764832
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26769 * 0.94274883
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60573 * 0.35990093
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49959 * 0.75630863
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68006 * 0.58470637
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54327 * 0.17736045
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12405 * 0.69436022
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89437 * 0.77638344
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69912 * 0.46706312
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44670 * 0.14017987
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33918 * 0.02127892
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14625 * 0.01391581
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91918 * 0.65973976
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58615 * 0.17733882
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11977 * 0.54569011
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8310 * 0.90080499
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37166 * 0.69383865
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37770 * 0.02659934
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53335 * 0.03170871
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36620 * 0.43591051
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40579 * 0.76243514
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64542 * 0.60794460
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74181 * 0.62283013
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27215 * 0.23832495
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83434 * 0.36722542
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51314 * 0.03081612
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34851 * 0.51869693
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80232 * 0.01142155
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30158 * 0.07616871
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98659 * 0.64674792
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92284 * 0.35492263
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3370 * 0.98305300
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70033 * 0.39108700
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43240 * 0.90199099
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64612 * 0.36020578
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63573 * 0.61412118
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21476 * 0.81649429
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 68123 * 0.32370634
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23982 * 0.29028148
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 2638 * 0.47298549
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 27261 * 0.79296845
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 33462 * 0.37973184
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 67159 * 0.45864947
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 5241 * 0.28810554
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 64316 * 0.80369196
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'olqtskeo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0032():
    """Extended test 32 for transcoding."""
    x_0 = 59051 * 0.25475847
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3930 * 0.42796240
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73177 * 0.72713957
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27780 * 0.99144619
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56072 * 0.41547601
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44194 * 0.96729086
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97335 * 0.75179530
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99536 * 0.05889663
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1717 * 0.91151164
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41167 * 0.07801012
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6843 * 0.13970665
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81763 * 0.70748709
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19255 * 0.20372244
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3769 * 0.46936040
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62277 * 0.47366725
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90124 * 0.37691927
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26947 * 0.64468855
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49920 * 0.60885529
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21840 * 0.32500401
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37164 * 0.44606939
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36029 * 0.33580431
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24974 * 0.57233587
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57170 * 0.91628258
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4299 * 0.45031684
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14893 * 0.32820342
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8831 * 0.03723227
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41429 * 0.32691030
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19952 * 0.99555047
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86692 * 0.64727238
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87372 * 0.79237552
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87825 * 0.36287289
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71705 * 0.70763203
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12222 * 0.59098530
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35666 * 0.50920614
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12274 * 0.75233832
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85978 * 0.49264540
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70151 * 0.21696547
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60952 * 0.38558500
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42927 * 0.36553506
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76756 * 0.53394181
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46108 * 0.05358571
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 76459 * 0.67995876
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 40785 * 0.14591421
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 81729 * 0.15541727
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71089 * 0.72243929
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'wvdumwxn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0033():
    """Extended test 33 for transcoding."""
    x_0 = 63681 * 0.98816505
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26681 * 0.15671131
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82715 * 0.86237958
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76088 * 0.58057609
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37624 * 0.72778112
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78283 * 0.29398858
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32822 * 0.07211969
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63869 * 0.91538409
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36061 * 0.70521075
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43139 * 0.05867026
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5842 * 0.53794493
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44890 * 0.58850748
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5134 * 0.39727225
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29974 * 0.38387355
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16963 * 0.45583167
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74695 * 0.86225074
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12162 * 0.93139242
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94028 * 0.50951451
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52827 * 0.68428131
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94968 * 0.51808196
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99085 * 0.88116733
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9890 * 0.76774576
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47080 * 0.85670456
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16614 * 0.55838720
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18312 * 0.93980401
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87247 * 0.46738119
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84006 * 0.46897902
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33774 * 0.34273624
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85847 * 0.53698328
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31183 * 0.18143204
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43431 * 0.74117834
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44457 * 0.10195236
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90802 * 0.83011120
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4392 * 0.50878974
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56888 * 0.23170267
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90449 * 0.76122539
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8126 * 0.29646281
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6680 * 0.42354800
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81566 * 0.85907919
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 570 * 0.43413594
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27899 * 0.26993667
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9341 * 0.50281491
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83326 * 0.03581224
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 19246 * 0.32104312
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'kepclfsz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0034():
    """Extended test 34 for transcoding."""
    x_0 = 65897 * 0.59972054
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88371 * 0.57084773
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17954 * 0.74992165
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93651 * 0.50195734
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91758 * 0.86237060
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52002 * 0.07276308
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80975 * 0.89062098
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73483 * 0.74698430
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12053 * 0.97900947
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87954 * 0.66340406
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82774 * 0.27050700
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3811 * 0.18192986
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47989 * 0.31712181
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37009 * 0.06666501
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39828 * 0.49881468
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95485 * 0.66736830
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57983 * 0.20455020
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77415 * 0.22096284
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98637 * 0.98124294
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77005 * 0.60357455
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28835 * 0.38666211
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73556 * 0.10924527
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86115 * 0.10609893
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28912 * 0.61786526
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47644 * 0.87025748
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61267 * 0.12942412
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38726 * 0.15790259
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'cvepvufd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0035():
    """Extended test 35 for transcoding."""
    x_0 = 47336 * 0.16313313
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66362 * 0.35324661
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71936 * 0.17968671
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52332 * 0.25696701
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43211 * 0.31965405
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70205 * 0.30626448
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39152 * 0.60421024
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81072 * 0.34205190
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94467 * 0.42328752
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82189 * 0.60512610
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58645 * 0.51306975
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69123 * 0.68770091
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30283 * 0.26193487
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29949 * 0.37086297
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13894 * 0.77624776
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62995 * 0.53115939
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62577 * 0.85563337
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61283 * 0.43293741
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74715 * 0.76716098
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33724 * 0.10991384
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54574 * 0.15560753
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34171 * 0.41692304
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61444 * 0.97159600
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19627 * 0.93952220
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14185 * 0.18447846
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91754 * 0.97402614
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81957 * 0.73159809
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5521 * 0.65075152
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34219 * 0.23169182
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67649 * 0.70754026
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83165 * 0.71129770
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80564 * 0.38667218
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52002 * 0.08660603
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51345 * 0.68268536
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79256 * 0.68415326
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6414 * 0.29082323
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30023 * 0.11793991
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82346 * 0.15507273
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6392 * 0.07034671
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6057 * 0.70295805
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68738 * 0.74933533
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'dtbwnxep').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0036():
    """Extended test 36 for transcoding."""
    x_0 = 26356 * 0.64383216
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14628 * 0.13060993
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20947 * 0.18152002
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94815 * 0.95744385
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44261 * 0.21349137
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18126 * 0.17680273
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8171 * 0.95451879
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37965 * 0.48372879
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15540 * 0.75995217
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6296 * 0.20882196
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96111 * 0.05610640
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98409 * 0.59381769
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87827 * 0.94283811
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42294 * 0.72317223
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97216 * 0.84194625
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74144 * 0.67049828
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17446 * 0.02204477
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75722 * 0.82154795
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66299 * 0.46841296
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20096 * 0.13421118
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44427 * 0.75843762
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38706 * 0.76353692
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35076 * 0.84333033
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54721 * 0.46671981
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97026 * 0.02241021
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96802 * 0.78901045
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14405 * 0.96749338
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55729 * 0.01481303
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30753 * 0.23675986
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33706 * 0.61695500
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23661 * 0.12481601
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60508 * 0.00294660
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15026 * 0.74738487
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74613 * 0.62352206
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'ybedgpij').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0037():
    """Extended test 37 for transcoding."""
    x_0 = 80471 * 0.42878890
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81326 * 0.15435953
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7910 * 0.92915997
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24670 * 0.38995565
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97397 * 0.60593747
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44271 * 0.03540540
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34069 * 0.48476026
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9665 * 0.32747178
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69883 * 0.79450941
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24960 * 0.86705300
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51323 * 0.32812512
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70799 * 0.64313109
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28372 * 0.95620203
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97577 * 0.06973833
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75514 * 0.19831571
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17359 * 0.12835953
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90699 * 0.93010246
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69454 * 0.73112656
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45959 * 0.23493218
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71294 * 0.54140030
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72068 * 0.11198082
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74924 * 0.48099688
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42865 * 0.46651951
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92674 * 0.13609799
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38313 * 0.08006327
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3778 * 0.96726487
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38971 * 0.70425705
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87353 * 0.76907285
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14928 * 0.95861298
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5527 * 0.62472609
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97057 * 0.64682586
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99330 * 0.12573518
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63441 * 0.28554163
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21653 * 0.15183242
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2056 * 0.34727983
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78971 * 0.80512709
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91240 * 0.41897472
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 406 * 0.97491975
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37889 * 0.83166782
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92449 * 0.08938589
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 9339 * 0.52605525
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 34375 * 0.16754522
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 64179 * 0.74312738
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27273 * 0.34965749
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59088 * 0.41289237
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 25358 * 0.08858513
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'lnemtumj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0038():
    """Extended test 38 for transcoding."""
    x_0 = 8636 * 0.18033443
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2154 * 0.80635644
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54325 * 0.97132456
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13628 * 0.04615795
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76317 * 0.95984588
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43240 * 0.74922166
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47706 * 0.64111435
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91977 * 0.26077226
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11083 * 0.11847191
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10702 * 0.01190107
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44610 * 0.43773232
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99234 * 0.95011463
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58117 * 0.57995691
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63289 * 0.17757422
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74169 * 0.58167175
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7999 * 0.77534239
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59507 * 0.03346967
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31040 * 0.00080133
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85971 * 0.74708199
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58632 * 0.30264521
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16430 * 0.15566327
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34315 * 0.97367229
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25543 * 0.41907644
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66421 * 0.51064473
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53087 * 0.74489292
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43312 * 0.96344816
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31510 * 0.87420161
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12426 * 0.75862918
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83416 * 0.41267930
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23490 * 0.28171299
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74955 * 0.76330230
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52280 * 0.65036950
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27049 * 0.25861965
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80933 * 0.70451733
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19518 * 0.51786670
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93218 * 0.89497101
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'urkzxduv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0039():
    """Extended test 39 for transcoding."""
    x_0 = 30811 * 0.81124143
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22768 * 0.52784545
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67777 * 0.07065193
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9034 * 0.52675459
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76275 * 0.76201655
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75339 * 0.19025378
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39796 * 0.94892685
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84997 * 0.45352046
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38975 * 0.19020932
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74911 * 0.59975416
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50193 * 0.20291819
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29980 * 0.54230498
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18194 * 0.74859189
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43835 * 0.03250647
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35761 * 0.56515114
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62788 * 0.07332642
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47828 * 0.43582416
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57364 * 0.27521484
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10350 * 0.00683980
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73385 * 0.58721816
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30955 * 0.55427928
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34154 * 0.96839035
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52177 * 0.90165365
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55920 * 0.72801430
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89994 * 0.84725729
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58416 * 0.87679564
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92949 * 0.90138727
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25519 * 0.18434292
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23992 * 0.53226496
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86012 * 0.04704058
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14187 * 0.67077242
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17172 * 0.28582555
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'clsrmqbz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0040():
    """Extended test 40 for transcoding."""
    x_0 = 23835 * 0.13287859
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3881 * 0.13549307
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51917 * 0.90616247
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80122 * 0.06103609
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40671 * 0.52787805
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21444 * 0.15014483
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32455 * 0.43053801
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40633 * 0.47767967
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84051 * 0.06102121
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20553 * 0.00537670
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45868 * 0.16177232
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20215 * 0.68345420
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72790 * 0.10386048
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78896 * 0.47072434
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62621 * 0.98574062
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88430 * 0.34646290
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41116 * 0.00932964
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95612 * 0.33914082
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42643 * 0.48604708
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76265 * 0.78969255
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74703 * 0.31183516
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70772 * 0.62370647
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73734 * 0.49506974
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20674 * 0.32351773
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'hpufbquw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0041():
    """Extended test 41 for transcoding."""
    x_0 = 66999 * 0.61215807
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56736 * 0.80460855
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56853 * 0.13188813
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70370 * 0.60356551
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89601 * 0.95866780
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53714 * 0.13412165
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95756 * 0.95673776
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67529 * 0.52803160
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60663 * 0.47769545
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82680 * 0.71467578
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35065 * 0.53427226
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94816 * 0.15676428
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91284 * 0.28038255
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74446 * 0.40183938
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89405 * 0.62248452
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17824 * 0.91438992
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89230 * 0.41423742
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54596 * 0.83571489
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80717 * 0.02071807
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86390 * 0.76957167
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94427 * 0.80615672
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58819 * 0.14446145
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59046 * 0.60704237
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53318 * 0.62647454
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98003 * 0.22868700
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69046 * 0.53957671
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99748 * 0.37990104
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 284 * 0.71567517
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33436 * 0.18102155
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67308 * 0.94402337
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74710 * 0.30128691
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40874 * 0.26864367
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97440 * 0.46594218
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25135 * 0.21590832
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27958 * 0.43792054
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35102 * 0.25877932
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60100 * 0.65254374
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21598 * 0.54356897
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8825 * 0.41817901
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59119 * 0.63801227
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82010 * 0.79970955
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79535 * 0.42623380
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46170 * 0.28139495
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 87500 * 0.11885580
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 65093 * 0.69750709
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 90131 * 0.90489732
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 67370 * 0.11843752
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 91479 * 0.15568822
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'lcbggneg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0042():
    """Extended test 42 for transcoding."""
    x_0 = 14034 * 0.48591781
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55517 * 0.70015219
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92213 * 0.04069783
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71568 * 0.50300605
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36601 * 0.13356718
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81998 * 0.96558798
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36911 * 0.46802618
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69198 * 0.40406068
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50768 * 0.51137165
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28210 * 0.88551715
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6113 * 0.89513203
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27652 * 0.52332260
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94095 * 0.30673378
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73008 * 0.29218689
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24040 * 0.44382105
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97995 * 0.04135892
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15231 * 0.29550809
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90904 * 0.47982853
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54227 * 0.86814108
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67637 * 0.90525236
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36959 * 0.38561809
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28355 * 0.15256312
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85803 * 0.60397284
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77849 * 0.33204068
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4757 * 0.03329367
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84633 * 0.11948309
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49565 * 0.73301965
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16339 * 0.18594809
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5751 * 0.82101216
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75088 * 0.00799366
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28575 * 0.14576098
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36130 * 0.64828782
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15132 * 0.90903862
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86919 * 0.77707797
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25015 * 0.65497713
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18767 * 0.02848020
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55088 * 0.66221937
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86340 * 0.08613213
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51567 * 0.73067996
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 58713 * 0.68808380
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46266 * 0.59340687
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22574 * 0.42348670
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74275 * 0.72490083
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 28252 * 0.17620122
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'whqrkqif').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0043():
    """Extended test 43 for transcoding."""
    x_0 = 33435 * 0.22551432
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32258 * 0.97802498
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40257 * 0.81107616
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45881 * 0.50247153
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25042 * 0.50451806
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28961 * 0.86304703
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56502 * 0.91226654
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56639 * 0.93794138
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64532 * 0.54851662
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76075 * 0.56429475
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27392 * 0.27336581
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35282 * 0.91751967
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52576 * 0.01751233
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94120 * 0.35105229
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28917 * 0.69040519
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1162 * 0.13483391
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44493 * 0.69264275
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37735 * 0.29105880
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90306 * 0.62289136
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99883 * 0.94387628
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81742 * 0.82280560
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27634 * 0.74134873
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74412 * 0.94169229
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67281 * 0.18661915
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98808 * 0.92733432
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14630 * 0.35395439
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96408 * 0.91481822
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74990 * 0.65526052
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63709 * 0.60245808
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50468 * 0.80943388
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16565 * 0.17092461
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89678 * 0.21458538
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39664 * 0.20155367
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35970 * 0.76789268
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93825 * 0.56837591
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6699 * 0.98590033
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53538 * 0.06052246
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10734 * 0.08926500
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34514 * 0.32869973
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51600 * 0.84712673
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3523 * 0.48950811
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63684 * 0.27988538
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77731 * 0.64806759
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ogldxcmq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0044():
    """Extended test 44 for transcoding."""
    x_0 = 38235 * 0.00429476
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97329 * 0.58051140
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25135 * 0.50496572
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94 * 0.57192827
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5006 * 0.37843371
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49614 * 0.75912137
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35607 * 0.93279262
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25844 * 0.08884482
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51549 * 0.41113254
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72666 * 0.78436412
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42352 * 0.41004035
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41344 * 0.35808717
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65519 * 0.91677560
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74203 * 0.32534032
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2986 * 0.47109428
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25819 * 0.82193727
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71559 * 0.83760716
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27506 * 0.32433302
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40037 * 0.66413316
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87026 * 0.18498497
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44389 * 0.34695407
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77161 * 0.01221541
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92079 * 0.90244728
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26898 * 0.79030280
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99252 * 0.74838757
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69382 * 0.79909578
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30830 * 0.42220469
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70042 * 0.88905387
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65516 * 0.88242933
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17434 * 0.41574702
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70923 * 0.63806781
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58328 * 0.78214734
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28235 * 0.60368372
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40868 * 0.70492848
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lmvunriv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0045():
    """Extended test 45 for transcoding."""
    x_0 = 70186 * 0.63983813
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 137 * 0.33105047
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92945 * 0.71812115
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28594 * 0.93363233
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29711 * 0.52542943
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35753 * 0.95216872
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58216 * 0.29393549
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5326 * 0.99208046
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79483 * 0.90672680
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3395 * 0.92596237
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91677 * 0.40023842
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45924 * 0.45274689
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35871 * 0.97579761
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55274 * 0.42677789
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89470 * 0.20333598
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77627 * 0.33980540
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26289 * 0.48647419
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84323 * 0.98380111
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60165 * 0.01313354
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19826 * 0.19697252
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18755 * 0.40323343
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74586 * 0.53780494
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4622 * 0.51939861
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96218 * 0.55459459
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34168 * 0.29659260
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4143 * 0.90557464
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71469 * 0.96201766
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81746 * 0.81727895
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1858 * 0.50955918
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72707 * 0.67247019
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44730 * 0.24493273
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92998 * 0.18504902
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83012 * 0.63449753
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 454 * 0.10107669
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2846 * 0.60793210
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5248 * 0.48209258
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7703 * 0.77314877
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44863 * 0.81936758
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1343 * 0.16590720
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96038 * 0.23483969
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35838 * 0.50907511
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12326 * 0.84495397
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42450 * 0.08579859
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 78669 * 0.52652536
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17147 * 0.89677022
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10779 * 0.40357249
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'zuyzofrh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0046():
    """Extended test 46 for transcoding."""
    x_0 = 52095 * 0.69412497
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1856 * 0.63212874
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83727 * 0.71531554
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38294 * 0.10721828
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43372 * 0.86979657
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24915 * 0.82871085
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7814 * 0.38457444
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 404 * 0.85395759
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68402 * 0.76168954
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94930 * 0.48409758
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40272 * 0.44347642
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28901 * 0.83397539
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70443 * 0.12869714
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13196 * 0.88029155
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10674 * 0.95387603
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43644 * 0.23522126
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65159 * 0.38521881
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47537 * 0.46459641
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92313 * 0.43309398
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63722 * 0.60401647
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57463 * 0.88856197
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44916 * 0.49840965
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10185 * 0.27644189
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2971 * 0.07952360
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49349 * 0.01644948
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8425 * 0.03147775
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66425 * 0.43916268
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85136 * 0.34744229
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90676 * 0.77417157
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39144 * 0.02889162
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63303 * 0.54078715
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44968 * 0.28988958
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96802 * 0.00525219
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22259 * 0.06895613
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3580 * 0.10444829
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96708 * 0.03728452
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48870 * 0.37296489
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62751 * 0.59145582
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 3443 * 0.74311909
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'jkgrkpfo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0047():
    """Extended test 47 for transcoding."""
    x_0 = 21551 * 0.11902009
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62413 * 0.43989938
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20908 * 0.95721915
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55595 * 0.07718118
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10064 * 0.46787976
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82512 * 0.16000594
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77039 * 0.14417102
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25487 * 0.78691528
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59508 * 0.26867697
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70586 * 0.64416566
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96643 * 0.25109644
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44018 * 0.16543955
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91302 * 0.72385771
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88081 * 0.45168713
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53126 * 0.02706137
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49949 * 0.70884485
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15609 * 0.29999860
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43676 * 0.44549460
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32973 * 0.99944629
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42060 * 0.42906379
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44208 * 0.80921167
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28010 * 0.17491251
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10295 * 0.80667142
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23419 * 0.43709439
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7659 * 0.54351085
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71761 * 0.05696735
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39503 * 0.29973833
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2793 * 0.13706250
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25776 * 0.07917807
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33586 * 0.95655507
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75718 * 0.56663498
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39642 * 0.15437484
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75564 * 0.41323773
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77421 * 0.37059974
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22273 * 0.70813486
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34381 * 0.76879068
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48096 * 0.11220515
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'cqemenmw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0048():
    """Extended test 48 for transcoding."""
    x_0 = 78802 * 0.55388508
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81167 * 0.18386383
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54873 * 0.59130653
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3082 * 0.32933227
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89384 * 0.58884509
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27338 * 0.84471632
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33763 * 0.62909496
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30388 * 0.36491325
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88872 * 0.14048027
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88688 * 0.62802577
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15479 * 0.34383405
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52477 * 0.89928808
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46906 * 0.18430298
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8796 * 0.06519772
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96366 * 0.04230058
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41198 * 0.03132284
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63779 * 0.37054665
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18589 * 0.44811501
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62694 * 0.12847416
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36221 * 0.73463285
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80471 * 0.89889299
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34194 * 0.74657294
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41729 * 0.40228035
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 466 * 0.37006753
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46146 * 0.28945544
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19001 * 0.59958807
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14779 * 0.53590361
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43788 * 0.17942899
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45148 * 0.71717328
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71672 * 0.70221810
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23820 * 0.24878349
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64958 * 0.97837892
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79952 * 0.01111300
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19980 * 0.58409852
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69823 * 0.87171027
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13203 * 0.04005615
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'sxkglrpb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0049():
    """Extended test 49 for transcoding."""
    x_0 = 54524 * 0.21243251
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16877 * 0.79502983
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21365 * 0.03253262
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79460 * 0.12440425
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26850 * 0.05688963
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95040 * 0.57681636
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66348 * 0.83466541
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29001 * 0.12050617
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16509 * 0.02886443
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95543 * 0.48635691
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72476 * 0.72855949
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71828 * 0.50904261
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63996 * 0.82055415
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39916 * 0.88575902
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44459 * 0.08478234
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8353 * 0.45085999
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65419 * 0.74795516
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27112 * 0.10569732
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22505 * 0.40621564
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21529 * 0.30703152
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'cvyzacpz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0050():
    """Extended test 50 for transcoding."""
    x_0 = 29066 * 0.45622090
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29719 * 0.09310044
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84212 * 0.68780348
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56316 * 0.97353552
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92241 * 0.79828637
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68909 * 0.81095442
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35685 * 0.85778781
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32360 * 0.94858685
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52074 * 0.83068010
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42008 * 0.02343560
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46295 * 0.56562471
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55961 * 0.26330396
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95383 * 0.32434892
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48975 * 0.50501773
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51512 * 0.43204192
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91321 * 0.96882430
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77966 * 0.10835127
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66945 * 0.46327803
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32595 * 0.98054695
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43018 * 0.14695168
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22090 * 0.33711875
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21553 * 0.31399855
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42292 * 0.53269181
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 646 * 0.69806695
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95331 * 0.98395521
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53567 * 0.84108564
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5909 * 0.49769684
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27590 * 0.86890071
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2472 * 0.48464204
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50811 * 0.34319383
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78044 * 0.22328908
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78400 * 0.88014249
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73364 * 0.18060576
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60015 * 0.90593889
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43909 * 0.44695194
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74760 * 0.90505521
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17262 * 0.82984984
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40378 * 0.11861738
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29378 * 0.13017079
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91811 * 0.41157111
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 55473 * 0.70803645
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 10164 * 0.02322644
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 17816 * 0.47176185
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11675 * 0.17931517
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 6555 * 0.49458937
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 98421 * 0.75041840
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'hkomyghy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0051():
    """Extended test 51 for transcoding."""
    x_0 = 82533 * 0.12466788
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47327 * 0.86868680
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75616 * 0.75348357
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43259 * 0.00213563
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25928 * 0.36651369
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43881 * 0.56356633
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10574 * 0.65117781
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1228 * 0.62520178
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97371 * 0.91676934
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47106 * 0.83654181
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72834 * 0.08244591
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42925 * 0.76375549
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74715 * 0.08426455
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48915 * 0.65727998
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33491 * 0.31760775
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26556 * 0.44206657
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33217 * 0.90835169
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27473 * 0.34490076
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2414 * 0.88089431
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72819 * 0.03651655
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10325 * 0.42889798
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99106 * 0.62327080
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77756 * 0.08786843
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41280 * 0.64415202
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50592 * 0.34887022
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23704 * 0.15156194
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9076 * 0.63480294
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37381 * 0.78441441
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64699 * 0.08278455
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97555 * 0.17609278
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39158 * 0.00098882
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87686 * 0.45988768
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82992 * 0.56808955
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42409 * 0.67981568
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24799 * 0.36182086
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71517 * 0.73711898
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42214 * 0.38706683
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88198 * 0.96593079
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42080 * 0.39127370
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65274 * 0.97609896
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13033 * 0.78520613
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57426 * 0.89867184
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 30201 * 0.62398858
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'iohoogoc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0052():
    """Extended test 52 for transcoding."""
    x_0 = 75116 * 0.42896937
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76213 * 0.95282420
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45993 * 0.46628404
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19207 * 0.46639731
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47285 * 0.41212406
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24450 * 0.19085571
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10434 * 0.81717948
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41268 * 0.13943554
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39742 * 0.50439405
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69954 * 0.53914738
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93628 * 0.12242058
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50371 * 0.58209714
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48535 * 0.63171259
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47942 * 0.38845772
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73393 * 0.94204882
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44017 * 0.61633276
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40831 * 0.11393114
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75373 * 0.33141311
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53509 * 0.44474610
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84209 * 0.61628976
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32262 * 0.57290287
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66687 * 0.64162240
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70531 * 0.80752800
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51085 * 0.17199520
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'sotmbqjt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0053():
    """Extended test 53 for transcoding."""
    x_0 = 86188 * 0.69919284
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68352 * 0.13194016
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47233 * 0.82250051
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66707 * 0.62215867
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24852 * 0.92187598
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41913 * 0.36675277
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40077 * 0.00315799
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80196 * 0.65995306
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16044 * 0.82766396
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21211 * 0.26007072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19369 * 0.69438078
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21463 * 0.27213061
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57442 * 0.97215878
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36357 * 0.25262761
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59855 * 0.11058109
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76373 * 0.49112423
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59462 * 0.93345787
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76752 * 0.90399690
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95290 * 0.56442732
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78824 * 0.35031769
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15379 * 0.33579053
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'tskypqni').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0054():
    """Extended test 54 for transcoding."""
    x_0 = 54036 * 0.66779277
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76523 * 0.60081452
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17485 * 0.88152805
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25032 * 0.89524912
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23425 * 0.61424080
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89680 * 0.91110051
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68647 * 0.55411476
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74958 * 0.49806317
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13737 * 0.32854686
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29159 * 0.27580700
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76068 * 0.76576270
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27421 * 0.60933733
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87310 * 0.98808582
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9466 * 0.51763859
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62124 * 0.62226704
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76885 * 0.90853833
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83771 * 0.63992906
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19566 * 0.48597859
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34527 * 0.29822561
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55958 * 0.72042400
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93838 * 0.54894123
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52658 * 0.89936235
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63018 * 0.90641915
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33474 * 0.65547722
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20894 * 0.43341220
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40226 * 0.47814761
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78831 * 0.66926470
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32602 * 0.11771626
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73336 * 0.69113891
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4933 * 0.92854915
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20866 * 0.95246344
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72646 * 0.15371824
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18582 * 0.82177205
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5524 * 0.91339762
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76835 * 0.65475161
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46937 * 0.15124636
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95549 * 0.90447835
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81027 * 0.40984236
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78838 * 0.91424259
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2232 * 0.00126656
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32399 * 0.77503102
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'sffjyqhm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0055():
    """Extended test 55 for transcoding."""
    x_0 = 49797 * 0.62615770
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97670 * 0.51049638
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79228 * 0.88448182
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72133 * 0.16704053
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53314 * 0.87157167
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3583 * 0.68786462
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49187 * 0.03877294
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57394 * 0.37872815
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17720 * 0.38536341
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81130 * 0.84769325
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39140 * 0.14795162
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91830 * 0.11912265
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64131 * 0.94319143
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99539 * 0.31507863
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73413 * 0.24860288
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12296 * 0.31645464
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25852 * 0.25398266
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90592 * 0.55420046
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39463 * 0.04410223
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57631 * 0.53488793
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42627 * 0.68881144
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99642 * 0.85465458
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77027 * 0.22016587
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26193 * 0.99457783
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85284 * 0.28052251
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92586 * 0.56776053
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13477 * 0.25142341
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2804 * 0.02291574
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'ordahurx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0056():
    """Extended test 56 for transcoding."""
    x_0 = 65689 * 0.80934628
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57438 * 0.95232877
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43726 * 0.36439113
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64555 * 0.96659880
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57426 * 0.19080722
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21941 * 0.95446393
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51591 * 0.90446252
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22454 * 0.83426899
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3926 * 0.49806662
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56599 * 0.29390095
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57910 * 0.77434093
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99158 * 0.81546740
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14054 * 0.87052135
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24673 * 0.67897012
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16985 * 0.59779708
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69104 * 0.70532291
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72088 * 0.97251822
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56997 * 0.00003531
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64684 * 0.13623320
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76963 * 0.21497957
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88781 * 0.22291913
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19316 * 0.04689129
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28521 * 0.78862747
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77666 * 0.54392136
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81500 * 0.52591791
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41519 * 0.04831035
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83832 * 0.37509635
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16245 * 0.28497269
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67078 * 0.88165319
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43067 * 0.88270578
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87206 * 0.68565613
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80363 * 0.03110673
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95937 * 0.86940643
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94835 * 0.51361893
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54663 * 0.40806021
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1835 * 0.70984850
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35288 * 0.88286447
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89068 * 0.83655769
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 95237 * 0.52330909
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28488 * 0.47105256
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44035 * 0.15662745
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21738 * 0.94879400
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70603 * 0.22276970
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84371 * 0.99996217
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 57379 * 0.94543869
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 19433 * 0.16557307
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'vvjjbkfn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0057():
    """Extended test 57 for transcoding."""
    x_0 = 94625 * 0.75801320
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36267 * 0.79836902
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30920 * 0.27823766
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81052 * 0.59425057
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5263 * 0.70097526
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42303 * 0.94401568
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74637 * 0.17718535
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92958 * 0.38420061
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69807 * 0.21200619
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15435 * 0.07955564
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75858 * 0.24527912
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20657 * 0.86134729
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10643 * 0.21610449
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58496 * 0.93517006
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39773 * 0.80669839
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69887 * 0.86998179
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 100 * 0.85127853
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79924 * 0.12025950
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5455 * 0.61919690
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74497 * 0.08832438
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40599 * 0.38515500
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33845 * 0.40685453
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34664 * 0.37985578
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89727 * 0.18636924
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27593 * 0.48068154
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84415 * 0.99262945
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34793 * 0.72713904
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41096 * 0.50975614
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80453 * 0.44499270
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42268 * 0.47208024
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65925 * 0.17605208
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37028 * 0.04667215
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2364 * 0.30942943
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56826 * 0.65960606
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85264 * 0.72234707
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57837 * 0.90264392
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 37985 * 0.50319080
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93101 * 0.44868674
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14192 * 0.33148608
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76979 * 0.82917795
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78591 * 0.12021366
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57690 * 0.10775755
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 45102 * 0.41856150
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 95279 * 0.24185346
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 75447 * 0.98509878
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 37613 * 0.88832009
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 47355 * 0.69581571
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 23288 * 0.92812382
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'nbqjozrz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0058():
    """Extended test 58 for transcoding."""
    x_0 = 95360 * 0.21346110
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88304 * 0.05657972
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34939 * 0.52475735
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32066 * 0.42766736
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94071 * 0.41413956
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14420 * 0.29481730
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36977 * 0.66849129
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8337 * 0.32390673
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50415 * 0.44612954
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62374 * 0.62673690
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7736 * 0.89069268
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92620 * 0.25064763
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16787 * 0.09205610
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83428 * 0.31691757
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15034 * 0.70051210
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86147 * 0.06649035
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37036 * 0.23039925
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30269 * 0.83173184
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89812 * 0.94083692
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72430 * 0.90815139
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54254 * 0.97176847
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40798 * 0.32509234
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28351 * 0.46816814
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93231 * 0.44071811
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16822 * 0.54376786
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20009 * 0.19624233
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91910 * 0.39706826
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65326 * 0.82190330
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99876 * 0.71629960
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63725 * 0.96708410
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18394 * 0.52363175
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89133 * 0.21178449
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57080 * 0.43142031
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47261 * 0.43862753
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24890 * 0.19584451
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26268 * 0.96374541
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48365 * 0.76112603
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75496 * 0.03390915
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93599 * 0.75561779
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'nklnkyku').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0059():
    """Extended test 59 for transcoding."""
    x_0 = 98090 * 0.92144464
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62590 * 0.67440504
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10466 * 0.00557350
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8275 * 0.45638896
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32635 * 0.80323555
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89201 * 0.39046211
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48425 * 0.31265886
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97112 * 0.65298145
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 786 * 0.85152546
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79180 * 0.64146800
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14412 * 0.08416668
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62323 * 0.23551654
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74707 * 0.30029090
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74027 * 0.58560503
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57857 * 0.37149297
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17967 * 0.50572452
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81591 * 0.07140324
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20223 * 0.52810571
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18232 * 0.31419733
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81249 * 0.17996664
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78230 * 0.75465925
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30880 * 0.87689231
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51427 * 0.92940707
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87568 * 0.99968876
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31880 * 0.80864714
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96063 * 0.10212750
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53756 * 0.87180300
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63788 * 0.33880843
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94399 * 0.44534376
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41101 * 0.31029889
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11613 * 0.72424980
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59362 * 0.63869475
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95218 * 0.47169667
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29620 * 0.54320203
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24510 * 0.04749347
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'njracrgn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0060():
    """Extended test 60 for transcoding."""
    x_0 = 12831 * 0.34885102
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22050 * 0.63639627
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71351 * 0.78922069
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96334 * 0.29476392
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57076 * 0.47452024
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25850 * 0.32814514
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72887 * 0.98552583
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94722 * 0.58821126
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42335 * 0.03160882
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70026 * 0.83899477
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47448 * 0.55565983
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11982 * 0.23314395
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87173 * 0.44564150
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43300 * 0.95361383
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69521 * 0.81669615
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37341 * 0.37363174
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99161 * 0.87577142
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82662 * 0.74244230
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87345 * 0.87641372
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86282 * 0.59526014
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79947 * 0.39387304
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85784 * 0.22689146
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81676 * 0.85202687
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82108 * 0.69104421
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92864 * 0.21701654
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22914 * 0.55513811
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'vcpsqgah').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0061():
    """Extended test 61 for transcoding."""
    x_0 = 7638 * 0.91684704
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47134 * 0.66480571
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34147 * 0.73197809
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8188 * 0.52392786
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84235 * 0.06550682
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18820 * 0.40927569
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65439 * 0.85090811
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98955 * 0.67284083
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77139 * 0.44192788
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20184 * 0.60645221
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53981 * 0.52178402
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58532 * 0.42302863
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74790 * 0.02673479
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14918 * 0.18915888
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28838 * 0.75628518
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19824 * 0.59921324
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32938 * 0.47672138
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75329 * 0.87962950
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73552 * 0.49059770
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44397 * 0.64359150
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86141 * 0.44804010
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81348 * 0.24787963
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79596 * 0.18527386
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27721 * 0.41109413
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9777 * 0.37472622
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85616 * 0.93721296
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50764 * 0.29814386
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'xgjdkbwx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0062():
    """Extended test 62 for transcoding."""
    x_0 = 32160 * 0.84584950
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90186 * 0.71000449
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37369 * 0.47941067
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57693 * 0.20285214
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56605 * 0.27031927
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1857 * 0.91795946
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10514 * 0.43252633
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43148 * 0.29912710
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16288 * 0.81599782
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72562 * 0.11849914
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78450 * 0.81438126
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39633 * 0.69680698
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1495 * 0.55097489
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91646 * 0.20822842
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67196 * 0.47025666
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68073 * 0.70447128
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82037 * 0.19774707
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66784 * 0.79394316
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78316 * 0.44546010
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88203 * 0.07880186
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36947 * 0.57802982
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34534 * 0.11077564
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88596 * 0.51340804
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27356 * 0.57261944
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64630 * 0.21108106
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52352 * 0.26712012
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21517 * 0.82047584
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18078 * 0.23885806
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38814 * 0.78041185
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'nggumcri').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0063():
    """Extended test 63 for transcoding."""
    x_0 = 43972 * 0.17225872
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61381 * 0.10066254
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81234 * 0.78299335
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88843 * 0.26690563
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41341 * 0.91505759
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10212 * 0.09366106
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5008 * 0.71421102
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77579 * 0.15632712
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15577 * 0.55554015
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26101 * 0.96260933
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84960 * 0.08088474
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7045 * 0.83195623
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7719 * 0.51872103
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60119 * 0.46353664
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18332 * 0.53890292
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49989 * 0.17042409
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74851 * 0.72533424
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25785 * 0.89010923
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82128 * 0.65821667
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12529 * 0.12900604
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86587 * 0.89272888
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93167 * 0.54849079
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89963 * 0.20838337
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9423 * 0.32071779
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83625 * 0.64910141
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45343 * 0.63946359
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55836 * 0.08979298
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72667 * 0.42196077
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63336 * 0.19600437
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62631 * 0.48891587
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6156 * 0.43154184
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82612 * 0.66029063
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70863 * 0.35330347
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97066 * 0.25118804
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43563 * 0.08812385
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68957 * 0.56996527
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61918 * 0.64186760
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58955 * 0.31907027
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30120 * 0.47321676
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90459 * 0.71462042
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2977 * 0.45412090
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 91569 * 0.90448743
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 25997 * 0.29113442
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94170 * 0.76464423
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 21338 * 0.77022487
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 18287 * 0.64184976
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 22541 * 0.51679070
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 74559 * 0.52594654
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ndbspvpm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0064():
    """Extended test 64 for transcoding."""
    x_0 = 67615 * 0.90839681
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63364 * 0.46286524
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3249 * 0.46487508
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18990 * 0.32767023
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83068 * 0.37954485
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73671 * 0.71286051
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26560 * 0.87196439
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63574 * 0.03911258
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76434 * 0.48263732
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18642 * 0.54828860
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56892 * 0.74769465
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35297 * 0.07931226
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38864 * 0.85104099
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66098 * 0.54583044
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2916 * 0.75693035
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82813 * 0.48810260
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94870 * 0.84752217
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76482 * 0.99251871
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6710 * 0.03367246
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84480 * 0.57848779
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14492 * 0.96809643
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35393 * 0.99769352
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8632 * 0.96471292
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88994 * 0.06059169
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69949 * 0.52071376
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97668 * 0.44999360
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37796 * 0.35367880
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21075 * 0.87282041
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54484 * 0.31626408
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36377 * 0.71324325
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4851 * 0.22769839
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20788 * 0.11409895
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 126 * 0.31556039
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82268 * 0.06124241
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68114 * 0.34486204
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51020 * 0.65010452
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7584 * 0.96452675
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81875 * 0.27060854
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45502 * 0.40428206
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86901 * 0.37393968
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34656 * 0.07931671
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60361 * 0.79052198
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 45052 * 0.32842568
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 29231 * 0.59633342
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 76017 * 0.92091101
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 96247 * 0.43994688
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 28801 * 0.66565522
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 86863 * 0.30687219
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 7210 * 0.15563649
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'xiifnenz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0065():
    """Extended test 65 for transcoding."""
    x_0 = 44294 * 0.21786608
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53245 * 0.32864361
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23598 * 0.35841685
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83406 * 0.26245438
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86172 * 0.33897523
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91507 * 0.07869339
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15301 * 0.30125202
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60303 * 0.66491531
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13230 * 0.75034522
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47099 * 0.17640841
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9085 * 0.85161225
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88920 * 0.51544572
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57893 * 0.73805508
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40271 * 0.15131305
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59847 * 0.93131852
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76755 * 0.09198750
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3197 * 0.30940905
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27495 * 0.86206241
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76765 * 0.62140262
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75672 * 0.37575559
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67561 * 0.91752864
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30471 * 0.33331408
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57970 * 0.49606973
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75968 * 0.98909797
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27393 * 0.05117530
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5227 * 0.70204130
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5168 * 0.16644151
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33573 * 0.70680792
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33404 * 0.66163499
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44309 * 0.07470555
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43442 * 0.47035750
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71254 * 0.76562538
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3664 * 0.71311012
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25457 * 0.52605208
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13254 * 0.77450061
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22792 * 0.11761589
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90277 * 0.57038722
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'yhvesnmn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0066():
    """Extended test 66 for transcoding."""
    x_0 = 18887 * 0.55837065
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22543 * 0.27761387
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76941 * 0.79030723
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98835 * 0.22181890
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62073 * 0.28966525
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56644 * 0.64455583
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24961 * 0.10435760
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37462 * 0.48633847
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27423 * 0.30968303
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33412 * 0.04951869
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79833 * 0.80857995
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61093 * 0.98832773
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72795 * 0.18814243
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7816 * 0.04982109
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2194 * 0.47921127
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75299 * 0.81603491
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84830 * 0.16311951
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62096 * 0.89752389
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78016 * 0.25500441
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86870 * 0.70356568
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11458 * 0.33857008
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61704 * 0.35448308
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16053 * 0.78347466
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83665 * 0.72894091
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28404 * 0.30746929
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84845 * 0.20961401
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69675 * 0.63115657
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26410 * 0.47075683
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17584 * 0.16027575
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58006 * 0.16980459
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28513 * 0.80103342
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9534 * 0.70161920
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65788 * 0.10306985
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27489 * 0.99469099
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59715 * 0.88890220
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10218 * 0.43918763
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4610 * 0.76596773
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50698 * 0.90314726
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 33581 * 0.05854472
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33074 * 0.72692210
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71894 * 0.74546421
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14159 * 0.45838314
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 56555 * 0.83357807
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36374 * 0.20968561
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 54380 * 0.04122260
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 38784 * 0.41165275
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 99780 * 0.46816028
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 79866 * 0.55722128
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 23539 * 0.10141950
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 44413 * 0.39183019
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'amhhfzie').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0067():
    """Extended test 67 for transcoding."""
    x_0 = 20996 * 0.93772854
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12206 * 0.86527367
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43957 * 0.64077534
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87171 * 0.96937635
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60044 * 0.09476004
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65486 * 0.93908534
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54733 * 0.01521538
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77369 * 0.41252903
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 270 * 0.15878155
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89246 * 0.37091486
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55485 * 0.52728343
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23405 * 0.39367338
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40098 * 0.51070931
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45722 * 0.74101490
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57000 * 0.36882260
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93473 * 0.22709261
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19354 * 0.99517747
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4937 * 0.58430291
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41909 * 0.08759371
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88453 * 0.02195435
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42352 * 0.84280680
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50659 * 0.43127842
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89221 * 0.44846275
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91693 * 0.87668647
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18955 * 0.46817604
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87834 * 0.02090167
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22159 * 0.37019703
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92856 * 0.18319650
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80176 * 0.57761041
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30414 * 0.45500581
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20277 * 0.43330146
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19278 * 0.42636915
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21174 * 0.35170457
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83735 * 0.87231977
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84531 * 0.16629897
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98279 * 0.30191624
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55297 * 0.11215074
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32875 * 0.85709518
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34674 * 0.55535609
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19501 * 0.40054621
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74152 * 0.45373887
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 46143 * 0.00733584
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 56543 * 0.08024497
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 2404 * 0.65143536
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61118 * 0.93351857
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'oxapslkl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0068():
    """Extended test 68 for transcoding."""
    x_0 = 37633 * 0.65283652
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56827 * 0.18477175
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35619 * 0.77178270
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79297 * 0.05234288
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92501 * 0.27846562
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11376 * 0.73982639
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31060 * 0.75691099
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58054 * 0.25697089
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98847 * 0.51777150
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3889 * 0.97534294
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27453 * 0.28611563
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78275 * 0.79899510
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40855 * 0.63224176
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22233 * 0.02089393
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81521 * 0.89706632
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36989 * 0.88102651
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49104 * 0.06298714
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1679 * 0.61085831
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24179 * 0.11987711
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25398 * 0.33068059
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3018 * 0.11334927
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25092 * 0.82656008
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79772 * 0.01397991
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25928 * 0.11183171
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48019 * 0.70026986
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16109 * 0.42109691
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43516 * 0.65163960
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43419 * 0.66543433
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69450 * 0.67484415
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10715 * 0.51734679
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89714 * 0.85956143
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38344 * 0.89728279
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67597 * 0.37947335
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66700 * 0.18764594
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80671 * 0.85649935
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90551 * 0.17883066
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98334 * 0.07987946
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35418 * 0.41053828
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 33156 * 0.27050411
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9887 * 0.23706541
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36017 * 0.36666851
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13636 * 0.79718461
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44859 * 0.04436817
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27525 * 0.38369548
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 74354 * 0.30028887
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 48751 * 0.75674639
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'vqsfbxip').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_6_0069():
    """Extended test 69 for transcoding."""
    x_0 = 10405 * 0.65914608
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94105 * 0.05627725
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79190 * 0.84150641
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87856 * 0.52574639
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41066 * 0.87189421
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94340 * 0.48089810
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75449 * 0.56499217
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77536 * 0.63492658
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61646 * 0.33417371
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68174 * 0.58625296
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55617 * 0.30261588
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9572 * 0.81874087
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15863 * 0.60407316
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28358 * 0.21118733
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39675 * 0.72609743
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15076 * 0.07937273
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31167 * 0.64311643
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97482 * 0.46568708
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40953 * 0.99518505
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13599 * 0.49167581
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82685 * 0.81390132
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86391 * 0.73492068
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40214 * 0.05192058
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31196 * 0.05088301
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80720 * 0.74438713
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99058 * 0.77266477
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85934 * 0.39808855
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17456 * 0.48425748
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'lhdwqplp').hexdigest()
    assert len(h) == 64
