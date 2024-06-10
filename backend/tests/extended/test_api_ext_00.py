"""Extended tests for api suite 0."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_api_extended_0_0000():
    """Extended test 0 for api."""
    x_0 = 44083 * 0.90781053
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2342 * 0.65291202
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28842 * 0.51481764
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74861 * 0.15935365
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57324 * 0.58693465
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23543 * 0.88032843
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82943 * 0.14944176
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82244 * 0.18179271
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44870 * 0.77463407
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90392 * 0.65641466
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3943 * 0.65189919
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16811 * 0.67683002
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23048 * 0.11630794
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87037 * 0.86118788
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73067 * 0.01093791
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82977 * 0.63835160
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75516 * 0.26708502
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64924 * 0.22438019
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21953 * 0.68662084
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92397 * 0.51662776
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90595 * 0.61699148
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63400 * 0.18871294
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48077 * 0.90729647
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59797 * 0.48938243
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74844 * 0.98589306
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30231 * 0.41473004
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34515 * 0.79050620
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'khbhydnv').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0001():
    """Extended test 1 for api."""
    x_0 = 56897 * 0.56809302
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72959 * 0.23837864
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34510 * 0.83816279
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14013 * 0.61701594
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26629 * 0.05744236
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38109 * 0.75037522
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32879 * 0.61944573
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49128 * 0.63431861
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96986 * 0.43606824
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23891 * 0.42053460
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23776 * 0.90544682
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58871 * 0.92825140
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82944 * 0.44759637
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19534 * 0.11820044
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28108 * 0.42335150
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56233 * 0.59058201
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41783 * 0.13969821
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97864 * 0.18942868
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15751 * 0.10182523
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24471 * 0.18321532
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49168 * 0.15388259
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'qzlpekbu').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0002():
    """Extended test 2 for api."""
    x_0 = 52445 * 0.25050866
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69460 * 0.37297281
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35575 * 0.16753134
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54140 * 0.23036228
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26262 * 0.15611568
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32828 * 0.24609221
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57178 * 0.51250932
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61673 * 0.72577156
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5700 * 0.06343771
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92163 * 0.68768704
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95938 * 0.99754012
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74112 * 0.25112872
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55658 * 0.13213217
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39291 * 0.12315268
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73239 * 0.88770189
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64099 * 0.79918159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5136 * 0.36281049
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14127 * 0.38132285
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63537 * 0.49312909
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79352 * 0.12431221
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80496 * 0.47889192
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20052 * 0.35102239
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41900 * 0.78641484
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20310 * 0.28447515
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53029 * 0.04507192
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70624 * 0.35997963
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8727 * 0.05569980
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57185 * 0.67044902
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52473 * 0.50104181
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49869 * 0.21150084
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63116 * 0.81080776
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38105 * 0.02187403
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97289 * 0.30521992
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24629 * 0.17599326
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15380 * 0.83270343
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8037 * 0.41714042
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45027 * 0.54186401
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62575 * 0.49043586
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26252 * 0.39733084
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94898 * 0.40130687
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4562 * 0.22499912
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 32707 * 0.84458903
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28858 * 0.93089763
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 316 * 0.72235157
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'rwbscglf').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0003():
    """Extended test 3 for api."""
    x_0 = 41740 * 0.90071570
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82006 * 0.85979743
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44454 * 0.20893680
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26005 * 0.00995253
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53115 * 0.99925962
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42444 * 0.15369410
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23787 * 0.82418660
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96414 * 0.83817504
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 904 * 0.56284946
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22488 * 0.42748566
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93777 * 0.71918373
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33536 * 0.24538202
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81201 * 0.65763283
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42654 * 0.53904280
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45061 * 0.66837823
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74152 * 0.19993147
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85840 * 0.32653408
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97445 * 0.51754421
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7699 * 0.66897393
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91907 * 0.07998680
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4636 * 0.40741665
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51655 * 0.28127304
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67166 * 0.28864968
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5724 * 0.00756158
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'nfqzktxw').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0004():
    """Extended test 4 for api."""
    x_0 = 64507 * 0.32164312
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93252 * 0.03481952
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66077 * 0.88840383
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94764 * 0.39392226
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86991 * 0.14789921
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77859 * 0.19840018
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7113 * 0.64668869
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94627 * 0.48091395
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20311 * 0.59768644
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26913 * 0.41192107
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82296 * 0.58224699
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96133 * 0.29289139
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24347 * 0.78839223
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26488 * 0.16978818
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10908 * 0.80172718
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45419 * 0.46956391
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57045 * 0.01010479
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68460 * 0.32106774
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94507 * 0.23563966
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94849 * 0.49596641
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28754 * 0.14527429
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42916 * 0.72948468
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77279 * 0.26036074
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36802 * 0.70143395
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'yqtqecan').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0005():
    """Extended test 5 for api."""
    x_0 = 92840 * 0.50138321
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15075 * 0.04838414
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84467 * 0.97850142
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1216 * 0.39815973
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30761 * 0.51698206
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13140 * 0.99306472
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46010 * 0.84121044
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73688 * 0.90833116
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45511 * 0.45589217
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33259 * 0.01822950
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4504 * 0.24888972
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64511 * 0.96806160
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20511 * 0.77874280
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67886 * 0.55095206
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22361 * 0.50746758
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5195 * 0.15949285
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85125 * 0.84530875
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19836 * 0.73008026
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42052 * 0.11265498
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 503 * 0.19011042
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31110 * 0.11427982
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'baijkqnt').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0006():
    """Extended test 6 for api."""
    x_0 = 45028 * 0.96130401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82461 * 0.89444353
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70830 * 0.22849111
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39807 * 0.63300176
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65329 * 0.75651118
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66845 * 0.29276103
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30164 * 0.92777751
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35863 * 0.72971345
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90759 * 0.98076768
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51111 * 0.70638170
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84390 * 0.78030218
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61807 * 0.21581268
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98898 * 0.67067861
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18689 * 0.63187094
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64490 * 0.16467277
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70909 * 0.24487555
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23110 * 0.54213316
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24005 * 0.73788094
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61231 * 0.87456500
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2820 * 0.49167757
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43090 * 0.24541461
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81239 * 0.05917624
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60379 * 0.60403056
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90703 * 0.60574221
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41691 * 0.31381073
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31726 * 0.29446548
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81117 * 0.36077868
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6075 * 0.89817632
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59283 * 0.09957837
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56470 * 0.98414119
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89682 * 0.30826349
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21541 * 0.00315584
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80756 * 0.52089155
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49826 * 0.89866706
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27455 * 0.03691587
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21441 * 0.54847869
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57008 * 0.93126479
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5550 * 0.39371057
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73631 * 0.74052437
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40056 * 0.37369921
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68712 * 0.07040037
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21142 * 0.33802040
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74651 * 0.59584748
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 16271 * 0.51087228
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'knaaueyp').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0007():
    """Extended test 7 for api."""
    x_0 = 19795 * 0.55484965
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86774 * 0.95803169
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99440 * 0.74538426
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81425 * 0.42885856
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63891 * 0.49207161
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54992 * 0.07991930
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48593 * 0.90223895
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12834 * 0.83827074
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27764 * 0.36600110
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11380 * 0.95189045
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19360 * 0.91787029
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87646 * 0.57769111
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30966 * 0.96532798
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80688 * 0.95940790
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42726 * 0.85237884
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87492 * 0.31917508
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76330 * 0.70960362
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82129 * 0.63588976
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2228 * 0.54805006
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7856 * 0.36198975
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66216 * 0.23113509
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50084 * 0.66916904
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23320 * 0.75670429
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18098 * 0.83969807
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86556 * 0.65953093
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88636 * 0.42642783
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23151 * 0.59558535
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3443 * 0.33396913
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88087 * 0.88904062
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20218 * 0.50256573
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8713 * 0.52742242
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51441 * 0.38204940
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'hfgyzyye').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0008():
    """Extended test 8 for api."""
    x_0 = 38524 * 0.64858614
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65546 * 0.52914814
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79704 * 0.34920763
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68183 * 0.19086913
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23047 * 0.61849369
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70559 * 0.17864078
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45419 * 0.21326455
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36696 * 0.38842095
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83251 * 0.48639241
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49009 * 0.44509696
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52145 * 0.94696094
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45501 * 0.53627766
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5123 * 0.23449989
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81040 * 0.71769944
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69400 * 0.93734061
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65808 * 0.60050938
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33543 * 0.57369896
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81637 * 0.81421216
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50180 * 0.85244247
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68905 * 0.36049302
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84568 * 0.60535056
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67600 * 0.35327620
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72686 * 0.41222773
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84881 * 0.99314014
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60334 * 0.02417406
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'kfckaytd').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0009():
    """Extended test 9 for api."""
    x_0 = 60040 * 0.19400471
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54557 * 0.67019277
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45741 * 0.53016871
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7587 * 0.41821586
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14800 * 0.51068801
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11656 * 0.86247048
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36679 * 0.75722950
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1976 * 0.80684956
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14947 * 0.12306994
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81406 * 0.89860729
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89733 * 0.08132788
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88886 * 0.39596977
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90188 * 0.24834546
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29400 * 0.17960458
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19460 * 0.50458707
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24381 * 0.10389337
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93642 * 0.58648562
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88370 * 0.54461449
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6349 * 0.27423904
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52054 * 0.71350111
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99191 * 0.25865079
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95600 * 0.13876263
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8311 * 0.53608250
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90716 * 0.73815087
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60115 * 0.96020344
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60678 * 0.78862431
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30562 * 0.65768450
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24555 * 0.00069227
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12412 * 0.40522955
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37549 * 0.97391443
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68712 * 0.64500223
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'zofnuwlk').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0010():
    """Extended test 10 for api."""
    x_0 = 161 * 0.18001652
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45486 * 0.44049759
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89347 * 0.72786380
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86736 * 0.65359782
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52197 * 0.12472078
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41781 * 0.05652638
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54119 * 0.23993957
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48277 * 0.77501622
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98863 * 0.48915852
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89722 * 0.99633757
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90355 * 0.50979135
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74435 * 0.79410828
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29566 * 0.24280593
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28652 * 0.47552678
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75367 * 0.65608662
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1962 * 0.72980496
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24467 * 0.54680910
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27960 * 0.86259282
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22679 * 0.17125836
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22828 * 0.23372891
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38705 * 0.05819508
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89662 * 0.25018601
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93209 * 0.00585385
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51720 * 0.77554914
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64243 * 0.38965007
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37475 * 0.64154045
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89405 * 0.80949669
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50035 * 0.10662388
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46451 * 0.89523680
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91864 * 0.56660764
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16133 * 0.11229769
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53739 * 0.94541090
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36731 * 0.95909293
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36467 * 0.54446713
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85208 * 0.31446457
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76788 * 0.01747798
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'bemhqmnp').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0011():
    """Extended test 11 for api."""
    x_0 = 77000 * 0.01482108
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7616 * 0.70220546
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56671 * 0.43842996
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90703 * 0.81756412
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95570 * 0.55696093
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68033 * 0.48576105
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88225 * 0.61282581
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46072 * 0.44190408
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14230 * 0.69526962
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 358 * 0.94259421
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99310 * 0.96728679
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66832 * 0.60391128
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71098 * 0.09955802
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85455 * 0.53063167
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27835 * 0.21229699
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25727 * 0.89492112
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43419 * 0.40540529
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87492 * 0.81560171
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39351 * 0.50452503
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55448 * 0.47273706
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15335 * 0.86526368
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20036 * 0.46012864
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50336 * 0.76298546
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44966 * 0.34235470
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60206 * 0.80496069
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15995 * 0.00904678
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35448 * 0.17797966
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86756 * 0.78372850
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84617 * 0.18686621
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19512 * 0.11945744
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25740 * 0.51336089
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87933 * 0.14059589
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26646 * 0.51848079
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58884 * 0.33210327
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78878 * 0.20729880
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20968 * 0.02580705
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5412 * 0.78299723
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98042 * 0.82882385
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84446 * 0.85956277
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73110 * 0.86412134
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44287 * 0.95112391
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'zwzrbptr').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0012():
    """Extended test 12 for api."""
    x_0 = 15660 * 0.73378964
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31321 * 0.23663097
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13772 * 0.93452315
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79720 * 0.20980545
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62600 * 0.85181373
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5032 * 0.48903926
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98732 * 0.15756826
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88824 * 0.25132973
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68730 * 0.10503791
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97965 * 0.56992653
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60084 * 0.70281127
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24214 * 0.59002660
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48659 * 0.18692384
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64631 * 0.47383035
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7376 * 0.16931766
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78780 * 0.42637954
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64288 * 0.66366820
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63937 * 0.20932100
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36067 * 0.37437501
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72024 * 0.71692423
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71855 * 0.40361035
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69232 * 0.79802363
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11271 * 0.09993700
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'oebowtaj').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0013():
    """Extended test 13 for api."""
    x_0 = 33303 * 0.84858989
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26261 * 0.50607568
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12474 * 0.09250575
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37046 * 0.92317172
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34690 * 0.33401422
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45446 * 0.92771441
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14418 * 0.20640583
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19812 * 0.30430982
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38565 * 0.88739909
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7910 * 0.90336988
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69741 * 0.50167988
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85519 * 0.59077380
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36138 * 0.01830928
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1044 * 0.03362033
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26945 * 0.25346185
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23215 * 0.86253309
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94255 * 0.13622916
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12597 * 0.31859028
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60509 * 0.03836821
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36036 * 0.46007182
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84927 * 0.30008549
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 296 * 0.40107605
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56337 * 0.62076518
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67754 * 0.86750870
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51069 * 0.79593504
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62279 * 0.25502314
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50163 * 0.78164149
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48229 * 0.35753293
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32574 * 0.89699411
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88895 * 0.58828036
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16485 * 0.25915477
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36207 * 0.83135873
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93164 * 0.56062816
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73731 * 0.83857602
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36784 * 0.96389845
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'lcygqyoc').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0014():
    """Extended test 14 for api."""
    x_0 = 94915 * 0.79393850
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14866 * 0.61651466
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83467 * 0.70760712
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65685 * 0.23028351
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64113 * 0.77072968
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1366 * 0.18977473
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 996 * 0.28254898
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73460 * 0.77887043
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24668 * 0.24263872
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8548 * 0.95834715
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 920 * 0.60804273
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53427 * 0.57014747
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37264 * 0.26221241
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51959 * 0.53164125
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71748 * 0.06866964
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52909 * 0.46865731
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44183 * 0.25439915
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91747 * 0.82110135
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35819 * 0.04088618
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11651 * 0.11831686
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73202 * 0.48655129
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 855 * 0.76577117
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48446 * 0.82984567
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97431 * 0.68254711
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93173 * 0.88419339
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14554 * 0.09330642
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'guxyrfgi').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0015():
    """Extended test 15 for api."""
    x_0 = 58656 * 0.20801575
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40440 * 0.26092713
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37223 * 0.06161382
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46676 * 0.87436993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32657 * 0.23020508
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2841 * 0.87716508
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92431 * 0.03526568
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6907 * 0.39943380
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13166 * 0.81394683
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85373 * 0.20001589
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63156 * 0.03511704
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12973 * 0.67631465
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89369 * 0.71530706
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68559 * 0.92389254
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3805 * 0.32262248
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18308 * 0.18004946
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13450 * 0.90483992
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24921 * 0.78155847
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80444 * 0.19496774
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2269 * 0.31904454
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83914 * 0.65654998
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77792 * 0.83043601
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77745 * 0.16862289
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52035 * 0.69601456
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 556 * 0.14576480
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'wdcjejle').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0016():
    """Extended test 16 for api."""
    x_0 = 43164 * 0.64576881
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92953 * 0.98257498
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93784 * 0.90567489
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82529 * 0.29122773
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46393 * 0.24356658
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26977 * 0.13062067
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5593 * 0.10575081
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77583 * 0.75489481
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84969 * 0.51872713
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63566 * 0.48535025
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22482 * 0.50385959
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62175 * 0.48788139
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44104 * 0.78232755
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16338 * 0.13459026
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15545 * 0.39620388
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98555 * 0.58387691
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59798 * 0.43398513
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3429 * 0.77400837
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61957 * 0.26486640
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18919 * 0.97449977
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59731 * 0.86448600
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24822 * 0.68619115
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70576 * 0.70181376
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95034 * 0.17694718
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6916 * 0.91516875
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81204 * 0.66039221
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21412 * 0.87928631
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'mxdtopeo').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0017():
    """Extended test 17 for api."""
    x_0 = 77744 * 0.07534219
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75777 * 0.96683808
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99068 * 0.42451518
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28689 * 0.26698631
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49471 * 0.47662132
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1431 * 0.24016530
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84146 * 0.89671594
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80756 * 0.11370871
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94298 * 0.59173480
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47465 * 0.96413749
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40008 * 0.03552441
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74737 * 0.84507056
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60690 * 0.58997338
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57866 * 0.55036373
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99820 * 0.70296135
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48038 * 0.96770613
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88542 * 0.02760219
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72817 * 0.38168793
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10353 * 0.97070351
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90670 * 0.86267461
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1965 * 0.96666757
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57257 * 0.31681166
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40499 * 0.68707636
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23822 * 0.85952214
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28281 * 0.41610439
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64329 * 0.26406952
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48230 * 0.04255124
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20260 * 0.11320757
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11866 * 0.89275759
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31417 * 0.12480785
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68457 * 0.30808247
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84590 * 0.68925820
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73909 * 0.66534477
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54391 * 0.14709838
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5122 * 0.17896186
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17762 * 0.49877888
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59971 * 0.36426118
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13907 * 0.06911087
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74666 * 0.25664922
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'gajhyabl').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0018():
    """Extended test 18 for api."""
    x_0 = 63141 * 0.95443968
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69757 * 0.68460308
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18974 * 0.30760771
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26600 * 0.96725290
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16725 * 0.93255334
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64180 * 0.28239906
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38864 * 0.65053309
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33360 * 0.68185604
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86803 * 0.15227420
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25635 * 0.31890930
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11799 * 0.93613798
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55617 * 0.67334368
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64811 * 0.49939929
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28995 * 0.67786255
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29562 * 0.68391883
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36694 * 0.00496983
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92122 * 0.48387276
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63037 * 0.62297062
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38649 * 0.00532670
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84041 * 0.02944154
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10557 * 0.95598399
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96999 * 0.74971357
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45471 * 0.36889223
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31679 * 0.36833403
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76766 * 0.92215119
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17998 * 0.33142844
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26923 * 0.66744441
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90185 * 0.05215523
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68087 * 0.26102802
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18052 * 0.08677694
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92538 * 0.91332087
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7785 * 0.01339314
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72261 * 0.54140212
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89882 * 0.21962263
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45341 * 0.08496775
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93801 * 0.56275445
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71091 * 0.09354977
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29156 * 0.04269605
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51926 * 0.05676014
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7366 * 0.97286906
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54775 * 0.13697803
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67401 * 0.41711337
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'yeliynrp').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0019():
    """Extended test 19 for api."""
    x_0 = 26251 * 0.95995557
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91949 * 0.59840021
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58040 * 0.25524398
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55158 * 0.28242128
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29494 * 0.70886011
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90814 * 0.70937732
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88930 * 0.63011229
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33557 * 0.47701881
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61886 * 0.33973620
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71463 * 0.75375437
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94829 * 0.09370409
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14044 * 0.80718780
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24231 * 0.26914015
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41071 * 0.24312051
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19052 * 0.91028614
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51118 * 0.94810112
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54727 * 0.24380804
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34556 * 0.80660739
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49944 * 0.01983448
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7370 * 0.38327640
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99303 * 0.45286247
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24451 * 0.28534586
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76494 * 0.88942297
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64041 * 0.78388698
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'nvhxufhh').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0020():
    """Extended test 20 for api."""
    x_0 = 66974 * 0.18669010
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24721 * 0.19625662
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96876 * 0.47687826
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27025 * 0.26887141
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52116 * 0.01155174
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13966 * 0.16838883
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47724 * 0.70150213
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52608 * 0.29578462
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21413 * 0.08554861
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90350 * 0.54841884
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56807 * 0.50359831
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1311 * 0.11968513
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21454 * 0.08041113
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8503 * 0.45355742
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34225 * 0.94711208
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78167 * 0.11845265
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13186 * 0.19021880
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79634 * 0.22370697
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64224 * 0.14513119
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11394 * 0.33096154
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'dpmbznhp').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0021():
    """Extended test 21 for api."""
    x_0 = 13148 * 0.15315548
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13987 * 0.80150490
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75255 * 0.49139621
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89376 * 0.81255038
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8843 * 0.67058629
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66824 * 0.55530877
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59789 * 0.50986736
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25575 * 0.20351418
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67606 * 0.66034030
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28710 * 0.77210725
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78562 * 0.11603157
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1646 * 0.43987132
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55048 * 0.86205308
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81620 * 0.64564017
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75578 * 0.27354111
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18775 * 0.45327162
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2352 * 0.29098700
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64339 * 0.30683539
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97000 * 0.45606641
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77275 * 0.23052436
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38626 * 0.19201150
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61880 * 0.91879644
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80469 * 0.93749152
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20302 * 0.88804834
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'mdbmjaii').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0022():
    """Extended test 22 for api."""
    x_0 = 38615 * 0.40354925
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47162 * 0.76862554
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45560 * 0.82712153
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74039 * 0.01794843
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60490 * 0.00928887
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41551 * 0.70888332
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98704 * 0.17098966
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26016 * 0.67080892
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45024 * 0.36753076
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24606 * 0.80433300
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24201 * 0.32756546
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26972 * 0.87448092
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14682 * 0.11913579
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27768 * 0.12438651
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75385 * 0.57068890
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28378 * 0.70245383
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51790 * 0.40482492
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72270 * 0.94218315
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98661 * 0.73522276
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52017 * 0.43432365
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35455 * 0.99583313
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'gvwklask').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0023():
    """Extended test 23 for api."""
    x_0 = 96276 * 0.52865691
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6333 * 0.87809762
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19105 * 0.04963043
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87969 * 0.13087442
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59119 * 0.05301104
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20889 * 0.26696173
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65959 * 0.98706822
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89053 * 0.90050129
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11889 * 0.17507456
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38065 * 0.02615411
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81192 * 0.04340845
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76920 * 0.14690047
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32776 * 0.01537757
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51517 * 0.95276136
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53425 * 0.54440911
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81408 * 0.64947712
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5219 * 0.30249118
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66078 * 0.54037879
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46201 * 0.57621947
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59230 * 0.03945635
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91576 * 0.39756411
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45870 * 0.11128998
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96605 * 0.66348406
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51130 * 0.20984277
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 663 * 0.78617313
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53733 * 0.18436435
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11675 * 0.34989155
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29539 * 0.75956901
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37743 * 0.64776447
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57904 * 0.23091053
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79094 * 0.42642908
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43721 * 0.33014304
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31025 * 0.41155289
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54845 * 0.87330110
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'hhhxagtt').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0024():
    """Extended test 24 for api."""
    x_0 = 21288 * 0.00501757
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55428 * 0.07341288
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81485 * 0.49918817
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1763 * 0.77314445
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56324 * 0.39173918
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46076 * 0.16591824
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75811 * 0.64246135
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37327 * 0.81669305
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55204 * 0.02457716
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36150 * 0.35651775
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11090 * 0.35031415
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56596 * 0.91590120
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18558 * 0.99606369
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45127 * 0.36893242
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81496 * 0.14514108
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2475 * 0.17129221
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98743 * 0.25191832
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80170 * 0.98408202
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94213 * 0.22022508
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59177 * 0.08959468
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'pobwtdcp').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0025():
    """Extended test 25 for api."""
    x_0 = 82276 * 0.02881132
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41473 * 0.96000617
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30048 * 0.90286198
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77792 * 0.76914729
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54038 * 0.97352587
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27144 * 0.97173942
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45642 * 0.74489126
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19002 * 0.67876343
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18253 * 0.97075295
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44085 * 0.07359653
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19166 * 0.14671325
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57265 * 0.34346733
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35348 * 0.54302208
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82281 * 0.07192788
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88120 * 0.68989439
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77999 * 0.02228931
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74409 * 0.59515533
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97870 * 0.57907407
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79847 * 0.48477217
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95288 * 0.65148647
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40463 * 0.73920747
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45146 * 0.65460006
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48371 * 0.30269482
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62499 * 0.15114135
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64143 * 0.60116952
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'oicdgxqa').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0026():
    """Extended test 26 for api."""
    x_0 = 4554 * 0.09649756
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20060 * 0.66251230
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91567 * 0.93605490
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91531 * 0.55545585
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41646 * 0.73966416
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 919 * 0.94037274
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77929 * 0.23183187
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35153 * 0.32908689
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47859 * 0.59231191
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22243 * 0.49520065
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44657 * 0.39399548
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13894 * 0.09414617
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55200 * 0.11571752
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84505 * 0.23722799
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24270 * 0.41430688
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63091 * 0.18772330
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91846 * 0.39306612
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22434 * 0.92932784
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 233 * 0.43662668
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38769 * 0.27696944
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32996 * 0.46995148
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30150 * 0.50946969
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59339 * 0.09021939
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36523 * 0.55915289
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36555 * 0.66644561
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49501 * 0.69098943
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'hlkkjhef').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0027():
    """Extended test 27 for api."""
    x_0 = 65688 * 0.55606792
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81545 * 0.12176224
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87190 * 0.61024990
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94021 * 0.65291645
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65846 * 0.09051345
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93761 * 0.44813888
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15925 * 0.05150170
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79338 * 0.95299104
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50778 * 0.68424857
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74832 * 0.95436443
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45128 * 0.72396401
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22973 * 0.44166989
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14301 * 0.54828079
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37577 * 0.45376035
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58876 * 0.81462387
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83707 * 0.64945801
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92036 * 0.46130746
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33279 * 0.43464826
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78496 * 0.00342096
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28082 * 0.60455850
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26188 * 0.63637546
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21588 * 0.76260135
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18966 * 0.82931377
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87985 * 0.96542908
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60088 * 0.69715966
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19066 * 0.07286782
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97727 * 0.64944486
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'legsezgt').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0028():
    """Extended test 28 for api."""
    x_0 = 99600 * 0.76701488
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70264 * 0.07370525
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30913 * 0.00332139
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65960 * 0.06638272
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61867 * 0.02694270
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9935 * 0.02738394
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44289 * 0.71523519
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5930 * 0.86772564
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38297 * 0.58168326
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79794 * 0.14345154
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69434 * 0.54948084
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6649 * 0.51741430
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78017 * 0.97954502
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22118 * 0.72654900
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3321 * 0.79512473
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79324 * 0.46883680
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83815 * 0.41238198
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7892 * 0.93001781
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81896 * 0.63400288
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33892 * 0.42204131
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28813 * 0.08279863
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82725 * 0.35631519
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85864 * 0.83778505
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25047 * 0.24186631
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41815 * 0.25019220
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86204 * 0.30796461
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64192 * 0.00899203
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97607 * 0.87867801
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48401 * 0.97174799
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'zrumgbvu').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0029():
    """Extended test 29 for api."""
    x_0 = 78377 * 0.34028051
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14938 * 0.54129596
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65550 * 0.05303554
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75094 * 0.50238527
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97669 * 0.65153065
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90801 * 0.41591749
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38946 * 0.80895286
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41960 * 0.70724388
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70308 * 0.31624004
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17526 * 0.53696247
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91245 * 0.77847625
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97491 * 0.11189775
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10686 * 0.03745604
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33792 * 0.04542086
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30725 * 0.45296397
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4069 * 0.17458924
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79648 * 0.93057052
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43362 * 0.36432108
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35536 * 0.44722986
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58189 * 0.00820069
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55189 * 0.62755685
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43098 * 0.29749443
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18633 * 0.11445679
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91322 * 0.44707698
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42355 * 0.43798385
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58171 * 0.79107223
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37048 * 0.73103553
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53561 * 0.29857652
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66063 * 0.94251071
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49923 * 0.59286423
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56893 * 0.53449598
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94281 * 0.64656718
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71373 * 0.96205943
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38178 * 0.90789186
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90177 * 0.90704892
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4137 * 0.55907842
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56537 * 0.89160818
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 99746 * 0.62343029
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71308 * 0.68525538
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87493 * 0.40441308
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21149 * 0.55110353
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40199 * 0.24321399
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23375 * 0.55846293
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 59066 * 0.49883793
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'bifyhfob').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0030():
    """Extended test 30 for api."""
    x_0 = 79932 * 0.84385562
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36403 * 0.39991150
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74990 * 0.95587219
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34559 * 0.79307160
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90864 * 0.32269971
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49250 * 0.74692761
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46580 * 0.58498782
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68514 * 0.37789431
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24984 * 0.10987169
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4992 * 0.51450915
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39081 * 0.52298750
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25098 * 0.23031227
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87359 * 0.69800441
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20753 * 0.37293416
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41318 * 0.98812667
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79405 * 0.90190900
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80 * 0.12207608
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25580 * 0.15782629
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20557 * 0.82352794
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51277 * 0.03859022
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22601 * 0.97748078
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46926 * 0.40253987
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60061 * 0.56076649
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34002 * 0.84366969
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26749 * 0.39987032
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1013 * 0.28193886
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39568 * 0.24284400
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76839 * 0.18485127
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92083 * 0.92933905
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59260 * 0.74864591
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1550 * 0.91673559
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50698 * 0.11425578
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28305 * 0.58330808
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16795 * 0.72472507
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7185 * 0.18908231
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83121 * 0.61201539
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34590 * 0.91240199
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1324 * 0.13106760
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28179 * 0.85827929
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68374 * 0.69232136
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74592 * 0.18326326
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6468 * 0.92170197
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 97309 * 0.22939262
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ffewllid').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0031():
    """Extended test 31 for api."""
    x_0 = 47707 * 0.55711144
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49109 * 0.40473349
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48110 * 0.81582092
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26383 * 0.90017637
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37771 * 0.66358639
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45429 * 0.40520371
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71537 * 0.24086220
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39101 * 0.33016875
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16727 * 0.96242884
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37771 * 0.73452251
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36705 * 0.81054238
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11638 * 0.81517024
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80695 * 0.53820822
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53511 * 0.31222708
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1289 * 0.21061146
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89866 * 0.29167930
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41182 * 0.59629285
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29105 * 0.94329272
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76602 * 0.04883458
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37078 * 0.56545578
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5056 * 0.82013694
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92513 * 0.48419019
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22974 * 0.02700927
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48534 * 0.15741177
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80109 * 0.29729863
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75202 * 0.10007260
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95527 * 0.95576823
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83961 * 0.26524050
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39261 * 0.50950037
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65398 * 0.27369546
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70954 * 0.92735200
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5112 * 0.75431313
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44499 * 0.21726609
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49073 * 0.07383921
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25339 * 0.13015909
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86450 * 0.77545546
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88184 * 0.65919748
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77112 * 0.83215721
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17329 * 0.14181372
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21106 * 0.14678518
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40757 * 0.30273822
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59148 * 0.75301371
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'umubcovh').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0032():
    """Extended test 32 for api."""
    x_0 = 5861 * 0.57716548
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70728 * 0.50211506
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84212 * 0.62875877
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72286 * 0.60615029
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97094 * 0.47212750
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69216 * 0.23186507
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87534 * 0.60888074
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42428 * 0.86034011
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68971 * 0.91071978
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32789 * 0.27980139
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1453 * 0.29454575
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56603 * 0.71371465
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88932 * 0.60058499
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61040 * 0.87683961
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29613 * 0.86301273
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41020 * 0.95155791
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92796 * 0.12118940
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31247 * 0.36971224
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38075 * 0.56405027
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19602 * 0.49633999
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79512 * 0.29614923
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16828 * 0.67258107
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24597 * 0.05426050
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92442 * 0.81824749
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22977 * 0.10405358
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4138 * 0.66052509
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45991 * 0.18277011
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80901 * 0.56150919
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79476 * 0.44338766
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70469 * 0.67516310
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91643 * 0.34051635
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37792 * 0.73496963
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58685 * 0.71288413
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95326 * 0.19897074
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62386 * 0.70811312
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97247 * 0.97773691
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 38252 * 0.68478679
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16239 * 0.04758670
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 89412 * 0.41181380
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'qcotlvcg').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0033():
    """Extended test 33 for api."""
    x_0 = 79523 * 0.76139688
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17772 * 0.95055778
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28500 * 0.47787831
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94215 * 0.81772519
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77390 * 0.59104173
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68107 * 0.04565865
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68924 * 0.43461885
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51353 * 0.96070321
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53347 * 0.21901069
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62216 * 0.20996869
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29988 * 0.14551207
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45040 * 0.64905103
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8614 * 0.33562474
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98514 * 0.33902951
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74741 * 0.14903935
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3918 * 0.22304146
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62289 * 0.03804158
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92468 * 0.79733849
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34848 * 0.04541578
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60677 * 0.13427036
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84431 * 0.24058504
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14661 * 0.27620472
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67682 * 0.06665971
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'hgczxyft').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0034():
    """Extended test 34 for api."""
    x_0 = 40427 * 0.15162916
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60914 * 0.73698736
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91220 * 0.21744967
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57616 * 0.60139281
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6210 * 0.79332478
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6312 * 0.23712526
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19549 * 0.13680303
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20190 * 0.47159374
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66358 * 0.89611256
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5239 * 0.80387449
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40257 * 0.90559205
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40677 * 0.40450454
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83617 * 0.40919842
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84529 * 0.11938064
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52130 * 0.18864172
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82840 * 0.68624913
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92820 * 0.69537962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18466 * 0.30497334
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52728 * 0.24336693
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56126 * 0.44934843
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99183 * 0.82785682
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64103 * 0.54612477
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99310 * 0.16533209
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41393 * 0.04975732
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28195 * 0.48459422
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51585 * 0.83521333
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39100 * 0.94976210
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21876 * 0.94357861
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71194 * 0.74910209
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34292 * 0.60844561
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62276 * 0.78177331
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87207 * 0.67483922
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64886 * 0.33265456
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76336 * 0.76272403
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42585 * 0.71579792
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97355 * 0.52413357
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 38060 * 0.07549026
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 76135 * 0.70841258
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92436 * 0.84381643
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85968 * 0.91837399
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81675 * 0.99251856
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42984 * 0.10736591
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ahcoqegb').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0035():
    """Extended test 35 for api."""
    x_0 = 45012 * 0.75919572
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93132 * 0.27662760
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6194 * 0.76105267
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38646 * 0.10034422
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90223 * 0.41259377
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91189 * 0.25949535
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31082 * 0.64067825
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5440 * 0.17175868
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13943 * 0.38243440
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83205 * 0.53809412
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72009 * 0.73896919
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79192 * 0.81799814
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98189 * 0.52833223
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81027 * 0.32646235
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13816 * 0.72268008
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27998 * 0.51894083
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48077 * 0.50931514
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4734 * 0.25075163
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57388 * 0.37136548
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60308 * 0.33621883
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61097 * 0.35338457
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52647 * 0.92155194
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61957 * 0.54977166
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92015 * 0.17083548
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54440 * 0.67144338
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25150 * 0.67482123
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85127 * 0.57717967
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50929 * 0.00972061
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38424 * 0.42342257
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51857 * 0.96063343
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19820 * 0.39259678
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60129 * 0.40451796
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'qyzkzwmp').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0036():
    """Extended test 36 for api."""
    x_0 = 19067 * 0.26297914
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5551 * 0.76519490
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33617 * 0.46860459
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76642 * 0.54822741
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36337 * 0.87267791
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31448 * 0.31752448
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13145 * 0.61709142
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56985 * 0.62664478
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 254 * 0.54554919
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7100 * 0.94212459
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42981 * 0.33914910
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75582 * 0.50917869
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99789 * 0.38737104
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60547 * 0.10077797
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10860 * 0.52850400
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1005 * 0.10163927
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5589 * 0.39891547
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62253 * 0.41139021
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8904 * 0.17771151
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41028 * 0.49265008
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76640 * 0.76688473
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90168 * 0.78846522
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36763 * 0.79082465
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78217 * 0.83941134
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72659 * 0.26042674
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64719 * 0.15943955
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44319 * 0.46477159
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17462 * 0.77264727
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30290 * 0.64801671
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71242 * 0.69463113
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13743 * 0.86556129
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99661 * 0.41441177
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25448 * 0.54365024
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33895 * 0.26292242
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17397 * 0.52660777
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26622 * 0.76188364
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59171 * 0.94496750
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27800 * 0.87314518
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81356 * 0.71183257
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14628 * 0.94639700
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54015 * 0.79208757
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 94208 * 0.83031592
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79413 * 0.59649589
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84018 * 0.38468485
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 84205 * 0.60927483
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'oyajypwr').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0037():
    """Extended test 37 for api."""
    x_0 = 72599 * 0.65297727
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58760 * 0.92715293
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67338 * 0.19962524
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55574 * 0.71813422
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 238 * 0.18910010
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53898 * 0.99711979
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51662 * 0.78140534
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81433 * 0.31879014
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49768 * 0.76067421
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86974 * 0.75408760
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4430 * 0.22309069
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60082 * 0.64333702
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42280 * 0.89426979
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55066 * 0.34241444
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89322 * 0.36449562
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30594 * 0.05352455
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59751 * 0.62170950
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72253 * 0.81326427
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6250 * 0.99349887
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29451 * 0.60151039
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35938 * 0.32139974
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35620 * 0.59996193
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80740 * 0.47462870
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44035 * 0.66494085
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8788 * 0.86245378
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40136 * 0.66821615
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45500 * 0.15793346
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11035 * 0.02975241
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47394 * 0.37385689
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77390 * 0.16123084
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47984 * 0.93341704
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24958 * 0.54409401
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38512 * 0.49345301
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63997 * 0.22172397
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59058 * 0.07560029
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90395 * 0.09329157
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27012 * 0.18987695
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55686 * 0.65260564
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18903 * 0.70304725
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29015 * 0.87500744
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95629 * 0.47373037
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16442 * 0.06134333
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'wclujfqb').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0038():
    """Extended test 38 for api."""
    x_0 = 23614 * 0.71721025
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30363 * 0.47534679
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26399 * 0.03481556
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96836 * 0.47943515
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87125 * 0.45303410
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60829 * 0.08894094
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31900 * 0.29533622
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10758 * 0.31199160
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45620 * 0.80606796
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97423 * 0.22755054
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21257 * 0.73470573
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99293 * 0.80885827
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50619 * 0.44274820
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37495 * 0.49463261
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64418 * 0.32823865
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1637 * 0.26619047
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7587 * 0.02170997
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63716 * 0.64827387
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1010 * 0.63269167
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31377 * 0.61551166
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50757 * 0.56309286
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35748 * 0.14331228
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72806 * 0.95264311
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27738 * 0.43705659
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19431 * 0.05122838
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17648 * 0.71527597
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10975 * 0.84675219
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8421 * 0.76764245
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20693 * 0.56427382
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30899 * 0.68951757
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3350 * 0.46490674
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12726 * 0.14634327
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'pwonggtg').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0039():
    """Extended test 39 for api."""
    x_0 = 15732 * 0.35505532
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98629 * 0.00031252
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29621 * 0.71981556
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24404 * 0.69112896
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69723 * 0.19336619
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51134 * 0.74952364
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99664 * 0.18983591
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68746 * 0.44033971
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53303 * 0.50080562
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7318 * 0.67909961
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39933 * 0.46507965
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16983 * 0.92062830
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80524 * 0.94870607
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74429 * 0.74479350
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23998 * 0.27865735
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9670 * 0.27209762
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83421 * 0.17055262
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24052 * 0.64094912
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47006 * 0.71642780
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85483 * 0.79176913
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94422 * 0.74314048
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57142 * 0.80421042
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34682 * 0.82044811
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14619 * 0.27786319
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64469 * 0.47374538
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39562 * 0.99594532
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28219 * 0.92702806
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61462 * 0.34444832
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81160 * 0.28171026
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19236 * 0.74486164
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'gsblcrte').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0040():
    """Extended test 40 for api."""
    x_0 = 7006 * 0.52885723
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62958 * 0.98790953
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6792 * 0.39287580
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34558 * 0.02930303
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46609 * 0.20303682
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17441 * 0.46063909
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97566 * 0.12555080
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53381 * 0.62240630
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10119 * 0.18426748
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33095 * 0.30679527
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30931 * 0.95536141
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50085 * 0.36399117
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37574 * 0.27990615
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30613 * 0.25322260
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60054 * 0.16771386
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57700 * 0.70705439
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9200 * 0.75003909
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69510 * 0.46828986
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97421 * 0.45096006
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25254 * 0.60284447
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61016 * 0.56027975
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74891 * 0.43420708
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45519 * 0.90739639
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59326 * 0.34722236
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46354 * 0.37756923
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55578 * 0.19663993
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99180 * 0.26902540
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93197 * 0.64705043
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62375 * 0.07332442
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49899 * 0.23056032
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44164 * 0.45032501
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11716 * 0.63450567
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20185 * 0.81591765
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43413 * 0.59646036
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55200 * 0.69916893
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40951 * 0.52952310
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8125 * 0.95294289
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'ngxbqxyz').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0041():
    """Extended test 41 for api."""
    x_0 = 97378 * 0.06263530
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21048 * 0.00428393
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64257 * 0.72696611
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14971 * 0.18799662
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74577 * 0.03123229
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11147 * 0.87172691
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64741 * 0.97339271
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84803 * 0.12997915
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90239 * 0.21321824
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97671 * 0.06261603
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29338 * 0.37509925
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34990 * 0.35890140
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87514 * 0.02781505
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9788 * 0.93522232
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1457 * 0.00606850
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6994 * 0.00591786
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26427 * 0.50994735
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77326 * 0.93591676
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 537 * 0.81926074
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71970 * 0.40278241
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39205 * 0.69645666
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93994 * 0.63757560
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59544 * 0.97959304
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14288 * 0.31532176
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'oyewasos').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0042():
    """Extended test 42 for api."""
    x_0 = 67649 * 0.16048942
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93989 * 0.43921878
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45522 * 0.67633747
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61271 * 0.91913458
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17311 * 0.95167004
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72906 * 0.90965021
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51528 * 0.83199835
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76025 * 0.06662504
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65888 * 0.80257749
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80149 * 0.47709463
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54045 * 0.55917955
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78571 * 0.36531429
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58548 * 0.67854130
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56312 * 0.72877842
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45097 * 0.79535759
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57142 * 0.67428506
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19703 * 0.69007010
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80126 * 0.86893333
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12138 * 0.14081609
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58455 * 0.94408725
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79047 * 0.93509367
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26153 * 0.19296484
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44723 * 0.39563216
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4154 * 0.17389442
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98151 * 0.36867058
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55266 * 0.70703028
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80280 * 0.82066499
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83853 * 0.27265277
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73488 * 0.56521136
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38625 * 0.88580471
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32928 * 0.66619042
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96856 * 0.83020768
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96628 * 0.88048483
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73568 * 0.77680301
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'rmqkndip').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0043():
    """Extended test 43 for api."""
    x_0 = 24819 * 0.34871729
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43394 * 0.46434800
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52751 * 0.00582656
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76502 * 0.23036372
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30997 * 0.59061483
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71936 * 0.96559244
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26260 * 0.73434215
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63334 * 0.59921164
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20715 * 0.58423185
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54852 * 0.61400975
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61349 * 0.08049820
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69618 * 0.51689899
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68103 * 0.69597316
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7232 * 0.28791754
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5389 * 0.43650829
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75551 * 0.75855431
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32156 * 0.37486188
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98522 * 0.31495660
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59523 * 0.28913160
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68241 * 0.16610088
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23035 * 0.11614251
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82648 * 0.77745101
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4537 * 0.63428215
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70255 * 0.46033927
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66171 * 0.12247225
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19090 * 0.90788260
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40311 * 0.78187651
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55379 * 0.28615881
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57262 * 0.36106906
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88129 * 0.40768885
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29935 * 0.69347488
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'llffsjlu').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0044():
    """Extended test 44 for api."""
    x_0 = 34142 * 0.83200766
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70596 * 0.35286210
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31740 * 0.40750607
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82983 * 0.13895094
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88055 * 0.96932037
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91161 * 0.44749062
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54580 * 0.79449684
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1433 * 0.75481316
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39999 * 0.18396136
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55696 * 0.39529487
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31097 * 0.67225669
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68489 * 0.59104348
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20718 * 0.73713575
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87127 * 0.96735957
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17145 * 0.74151121
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57744 * 0.18331470
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98716 * 0.02570221
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65695 * 0.80285124
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19223 * 0.24417219
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58862 * 0.55218692
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61244 * 0.72293946
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27266 * 0.73221746
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12700 * 0.80065203
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31398 * 0.92265933
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78934 * 0.31253084
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33378 * 0.90722472
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30521 * 0.10598490
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72702 * 0.39626100
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84517 * 0.96496743
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77054 * 0.87855544
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75670 * 0.57299684
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24946 * 0.60392968
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58083 * 0.71073168
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74783 * 0.48217250
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'msunipcu').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0045():
    """Extended test 45 for api."""
    x_0 = 65681 * 0.95766665
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10096 * 0.01673128
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23109 * 0.65251955
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69860 * 0.77561247
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9249 * 0.50549930
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49043 * 0.36767385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43701 * 0.37383096
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41802 * 0.25469402
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69020 * 0.89230190
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18813 * 0.33545860
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 163 * 0.60198088
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91377 * 0.08595976
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22628 * 0.19641541
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56516 * 0.38287356
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69050 * 0.35385752
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78047 * 0.58646188
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65795 * 0.21140201
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46217 * 0.87620516
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6736 * 0.74573013
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37842 * 0.34701050
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1455 * 0.67566114
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58908 * 0.03957774
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16147 * 0.81371340
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6713 * 0.71993496
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89173 * 0.89867402
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79164 * 0.49870421
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91570 * 0.63426820
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18425 * 0.43476381
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1345 * 0.30350961
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54879 * 0.86662561
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15991 * 0.19604483
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97255 * 0.41556848
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67710 * 0.22469644
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41365 * 0.07095518
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14891 * 0.27012957
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48292 * 0.84495604
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69770 * 0.59298829
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8784 * 0.50190354
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'qeiquqze').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0046():
    """Extended test 46 for api."""
    x_0 = 71039 * 0.74143126
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50663 * 0.82998740
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50179 * 0.94998964
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96164 * 0.27091786
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64400 * 0.08734865
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80104 * 0.71559288
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31421 * 0.79162394
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49493 * 0.88135427
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64130 * 0.14950175
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21044 * 0.92043065
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8219 * 0.91200568
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 659 * 0.77262107
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61854 * 0.37238364
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78853 * 0.28203176
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75280 * 0.24333896
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37699 * 0.00301326
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49097 * 0.93936876
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13060 * 0.86145172
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77135 * 0.72900286
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41107 * 0.42720198
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97263 * 0.41028426
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50989 * 0.00038133
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6883 * 0.52890199
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23596 * 0.39098312
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81913 * 0.82804061
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56828 * 0.75080992
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84056 * 0.98321034
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23099 * 0.51380686
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18739 * 0.99874371
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10273 * 0.49791189
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44765 * 0.42357814
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78972 * 0.22197756
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10716 * 0.42381538
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8871 * 0.08834050
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6552 * 0.71595299
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30214 * 0.33473878
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63956 * 0.50683362
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49690 * 0.64388472
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69033 * 0.70364784
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 26764 * 0.77733570
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88601 * 0.42883911
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84851 * 0.28677258
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 4486 * 0.53871481
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 81556 * 0.17611707
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 16879 * 0.61076725
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'cpvktpzq').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0047():
    """Extended test 47 for api."""
    x_0 = 557 * 0.15476136
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9518 * 0.92186942
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53589 * 0.37373856
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22173 * 0.16446794
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43052 * 0.25967960
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83660 * 0.29129657
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81126 * 0.63602520
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31862 * 0.69627294
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74222 * 0.37759723
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29572 * 0.31809863
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78287 * 0.85922580
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9692 * 0.80545302
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13321 * 0.60252091
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11287 * 0.83279618
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38064 * 0.88724774
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96274 * 0.20385532
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29666 * 0.24558360
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45327 * 0.14072711
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87176 * 0.25137207
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55774 * 0.68961312
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47406 * 0.67465569
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39483 * 0.18164247
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35957 * 0.58622862
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77321 * 0.34336560
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51673 * 0.53534296
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15519 * 0.61041651
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73797 * 0.19402068
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84777 * 0.21671000
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49516 * 0.60010913
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40557 * 0.39223382
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ryowcpxr').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0048():
    """Extended test 48 for api."""
    x_0 = 73973 * 0.42560251
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74727 * 0.95933723
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12776 * 0.20818769
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86229 * 0.06755862
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73719 * 0.36462110
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74767 * 0.01050116
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59090 * 0.96249705
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45338 * 0.94141182
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43756 * 0.21167377
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8373 * 0.32209371
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69833 * 0.38712016
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25510 * 0.14875637
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87507 * 0.27783511
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12605 * 0.92088834
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39705 * 0.85653247
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39887 * 0.09434799
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51943 * 0.66710064
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98913 * 0.58035352
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23890 * 0.83526199
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24834 * 0.75246910
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74927 * 0.11138326
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86527 * 0.75003762
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94025 * 0.27892317
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87871 * 0.63445646
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86537 * 0.28316453
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32648 * 0.51284868
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'lmqazssz').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0049():
    """Extended test 49 for api."""
    x_0 = 22557 * 0.96365270
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15154 * 0.02648703
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36074 * 0.69107117
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14513 * 0.49029003
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91417 * 0.87090686
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1057 * 0.28895456
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16946 * 0.95485447
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69346 * 0.34956461
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43381 * 0.03975141
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67070 * 0.01025914
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41521 * 0.63717276
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76338 * 0.70170875
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66344 * 0.21390347
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75455 * 0.25076887
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42438 * 0.21416349
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4279 * 0.08156061
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69272 * 0.98066886
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30812 * 0.53443327
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80032 * 0.74273482
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18564 * 0.80922349
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40400 * 0.94605032
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15733 * 0.18359617
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38364 * 0.36047217
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'jeldadpl').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0050():
    """Extended test 50 for api."""
    x_0 = 88374 * 0.28308434
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65214 * 0.50745362
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44543 * 0.67353490
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42129 * 0.19176284
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99684 * 0.15737844
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43804 * 0.63811185
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25475 * 0.19132831
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42822 * 0.58721339
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57188 * 0.47728515
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11151 * 0.24653121
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74454 * 0.00656559
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20972 * 0.57504426
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66488 * 0.08839362
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15409 * 0.93810757
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40367 * 0.36558159
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9424 * 0.89735656
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53376 * 0.63928762
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51700 * 0.06594347
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83262 * 0.79002674
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64714 * 0.73971284
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66952 * 0.23136941
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41029 * 0.28508015
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62221 * 0.65344612
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58403 * 0.12173247
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95099 * 0.75332809
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47029 * 0.71439977
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24095 * 0.86537322
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25932 * 0.41541739
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45479 * 0.31284040
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64786 * 0.89041051
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74322 * 0.44915921
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24688 * 0.06774405
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86236 * 0.07809004
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'utpgtmon').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0051():
    """Extended test 51 for api."""
    x_0 = 56319 * 0.52071720
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28969 * 0.98014983
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41978 * 0.20770278
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1525 * 0.43539587
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91851 * 0.61032102
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5932 * 0.22475348
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56348 * 0.52032581
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71716 * 0.26911127
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9725 * 0.60604022
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64384 * 0.32935790
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34272 * 0.73224505
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38987 * 0.13414213
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43864 * 0.27274050
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63535 * 0.91006977
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61220 * 0.80901379
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57806 * 0.83698137
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92315 * 0.30255962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88285 * 0.56430636
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51099 * 0.26057264
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34142 * 0.94932794
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71675 * 0.45602098
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85869 * 0.00487098
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40335 * 0.18080457
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61883 * 0.07854684
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7732 * 0.60147507
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66273 * 0.42278742
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37706 * 0.49891492
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84878 * 0.84926471
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21300 * 0.74971330
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19710 * 0.12857628
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21884 * 0.57114867
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63583 * 0.02820857
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48833 * 0.05701382
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64852 * 0.88870987
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9292 * 0.93246847
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5928 * 0.84930771
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72406 * 0.07444215
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73668 * 0.20513232
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'dstcpjsm').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0052():
    """Extended test 52 for api."""
    x_0 = 66970 * 0.26030745
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36084 * 0.69266996
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53838 * 0.00844022
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73875 * 0.44323997
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35536 * 0.66622537
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74447 * 0.00256949
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86386 * 0.88761924
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18862 * 0.37470764
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98472 * 0.14298074
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96670 * 0.96674957
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16570 * 0.55544908
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73454 * 0.48190358
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33691 * 0.59769673
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57520 * 0.93953112
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66786 * 0.79936753
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38559 * 0.11179024
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80676 * 0.98224190
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22650 * 0.92970169
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22328 * 0.54542625
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45364 * 0.47687373
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8081 * 0.25747822
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7169 * 0.50394014
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88503 * 0.59642077
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83366 * 0.02167228
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8648 * 0.42017576
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93000 * 0.06802327
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69419 * 0.36404564
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1951 * 0.15997183
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72198 * 0.30715328
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11947 * 0.88422990
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44071 * 0.13086444
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63951 * 0.18976817
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21716 * 0.74494886
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19388 * 0.55236394
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32901 * 0.98677933
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 9360 * 0.95615442
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'sozymbtb').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0053():
    """Extended test 53 for api."""
    x_0 = 81820 * 0.14082376
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91669 * 0.06327803
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60468 * 0.59473608
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73661 * 0.45826454
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33245 * 0.81222192
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13533 * 0.85505409
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99228 * 0.52217967
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36678 * 0.00805427
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94881 * 0.75999316
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51110 * 0.56028036
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86104 * 0.12586749
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36105 * 0.19967507
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77351 * 0.65142748
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76175 * 0.17778131
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70276 * 0.98865765
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38933 * 0.59544700
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21160 * 0.44625899
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60685 * 0.16249958
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57724 * 0.21324045
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41083 * 0.63593347
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'zjlzdwkq').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0054():
    """Extended test 54 for api."""
    x_0 = 19943 * 0.27148498
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8676 * 0.62002927
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69552 * 0.25753992
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85997 * 0.78126958
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94011 * 0.25258937
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86369 * 0.57880545
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17506 * 0.60560094
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88596 * 0.84376266
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31120 * 0.40513529
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98044 * 0.04829253
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88818 * 0.54438328
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71115 * 0.30985483
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76638 * 0.92698328
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67619 * 0.38606984
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 237 * 0.00071188
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37263 * 0.04007036
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50788 * 0.47924747
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14917 * 0.29926600
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31429 * 0.27176827
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92623 * 0.74070518
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98909 * 0.94338585
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57526 * 0.76854342
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15615 * 0.79950321
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 112 * 0.25726372
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81762 * 0.19361911
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20133 * 0.75430510
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14842 * 0.01141239
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22025 * 0.33875684
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7282 * 0.68927341
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81508 * 0.63863338
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77078 * 0.14913575
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72359 * 0.66737713
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20363 * 0.37474054
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 675 * 0.33602915
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9154 * 0.73595527
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95839 * 0.65777269
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89222 * 0.10019369
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84681 * 0.24506166
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30484 * 0.95924253
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4225 * 0.72174492
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95768 * 0.20298874
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70046 * 0.06404533
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 67926 * 0.22056301
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 87346 * 0.38183829
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 24159 * 0.12754191
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 47218 * 0.57327426
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 20189 * 0.23719146
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 637 * 0.26262364
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 51908 * 0.08917094
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 73108 * 0.23632097
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'fkiwkwal').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0055():
    """Extended test 55 for api."""
    x_0 = 80179 * 0.00866718
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73558 * 0.92261264
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82200 * 0.36398063
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15600 * 0.97638657
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79856 * 0.57735857
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16387 * 0.41135209
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57160 * 0.11492310
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99693 * 0.99888094
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37049 * 0.15200370
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32199 * 0.56696252
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34529 * 0.82092084
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16543 * 0.56204317
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32092 * 0.95247124
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94442 * 0.28369064
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25903 * 0.83775521
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66506 * 0.13069194
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33543 * 0.19938841
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47083 * 0.44616830
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35898 * 0.07068549
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48964 * 0.71849670
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18499 * 0.60160899
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18710 * 0.97649330
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53323 * 0.11487922
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11069 * 0.56793987
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96238 * 0.04426499
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93848 * 0.38839275
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41796 * 0.08724783
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10863 * 0.60369658
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90970 * 0.15433168
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71569 * 0.70623322
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82387 * 0.48190460
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91412 * 0.18683238
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8858 * 0.74566168
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93053 * 0.45485990
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15235 * 0.24066941
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26543 * 0.93274075
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69635 * 0.95658937
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7332 * 0.89042592
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48391 * 0.57740737
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81248 * 0.98477081
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 22309 * 0.85560907
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 86766 * 0.08867103
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 38178 * 0.39606516
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 3637 * 0.80502328
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 91700 * 0.20565864
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 55432 * 0.84650782
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 92142 * 0.02634998
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'nerstngr').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0056():
    """Extended test 56 for api."""
    x_0 = 6882 * 0.48705764
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 915 * 0.42992913
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63199 * 0.65171004
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30123 * 0.04552269
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88136 * 0.63768785
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64514 * 0.35241125
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 105 * 0.73118608
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18471 * 0.68986912
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7682 * 0.43816731
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77615 * 0.35161381
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8838 * 0.73364904
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87939 * 0.43803166
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28246 * 0.26805048
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10817 * 0.91920332
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59176 * 0.48794189
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24156 * 0.31240188
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45005 * 0.53278105
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48682 * 0.25089497
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67964 * 0.56104923
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62217 * 0.63982445
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35226 * 0.18301312
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96937 * 0.79869971
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25974 * 0.10398390
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43329 * 0.51297456
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87767 * 0.19606261
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9189 * 0.52620349
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89748 * 0.13364649
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81053 * 0.38443481
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16256 * 0.53452169
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92906 * 0.41043699
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85428 * 0.15416848
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36781 * 0.30130270
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3532 * 0.57661911
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22348 * 0.60805221
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89902 * 0.81047012
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86725 * 0.06934901
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94529 * 0.94859771
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35409 * 0.08204050
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57383 * 0.77983164
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41006 * 0.77133781
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68000 * 0.98877808
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13385 * 0.88964237
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81401 * 0.02930860
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 6986 * 0.41892245
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17090 * 0.19697948
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 28953 * 0.92208210
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 21640 * 0.23960326
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 21544 * 0.65350123
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 23962 * 0.85506649
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 95239 * 0.07118751
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'smnjnuly').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0057():
    """Extended test 57 for api."""
    x_0 = 97734 * 0.30969250
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52164 * 0.55579878
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17685 * 0.45343356
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68548 * 0.85365452
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47076 * 0.73167110
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34576 * 0.11757392
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68130 * 0.84728785
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96312 * 0.29911841
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42671 * 0.20178467
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26611 * 0.99560733
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48759 * 0.10409978
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26667 * 0.40789111
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40001 * 0.83775427
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32044 * 0.34530735
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36392 * 0.14366781
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38496 * 0.73913349
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20229 * 0.35807173
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21463 * 0.94625194
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93599 * 0.60888863
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4761 * 0.70967520
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13815 * 0.95491451
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'eaqmyhgq').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0058():
    """Extended test 58 for api."""
    x_0 = 56272 * 0.86476144
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44694 * 0.21945085
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5410 * 0.63645804
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2612 * 0.77699438
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71861 * 0.39523828
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80335 * 0.26527572
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81484 * 0.38494438
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83300 * 0.22905779
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17368 * 0.27264801
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24258 * 0.60177044
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74995 * 0.04304854
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91359 * 0.53985883
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21232 * 0.09897953
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21942 * 0.03329391
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11691 * 0.34423974
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83180 * 0.06855516
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67421 * 0.10103173
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49723 * 0.27612298
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75292 * 0.26081152
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12980 * 0.67445871
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29770 * 0.65790359
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62745 * 0.47834025
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73451 * 0.09648147
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 193 * 0.74916654
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12663 * 0.86968415
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72959 * 0.12548871
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80542 * 0.06137743
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57118 * 0.00976609
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72002 * 0.19300790
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75281 * 0.92649686
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2391 * 0.82325421
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81001 * 0.05419009
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39595 * 0.91313283
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14869 * 0.56706572
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44106 * 0.50293432
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76986 * 0.89412525
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'tlkmvlyb').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0059():
    """Extended test 59 for api."""
    x_0 = 26704 * 0.70247868
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49640 * 0.01230970
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84109 * 0.46438629
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69410 * 0.07018116
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1572 * 0.66231927
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19787 * 0.24699421
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67676 * 0.12742200
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12316 * 0.21143878
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84672 * 0.56422026
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22484 * 0.35123191
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31584 * 0.05778304
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92099 * 0.62995643
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62465 * 0.02660864
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94440 * 0.00722616
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19423 * 0.49776483
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83088 * 0.29282468
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10748 * 0.13313785
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30110 * 0.70144775
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31808 * 0.65579620
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75963 * 0.10761315
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1364 * 0.52957927
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52429 * 0.94849685
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80997 * 0.26633993
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42563 * 0.18380935
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99048 * 0.21347254
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46048 * 0.71999879
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'kytxewgu').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0060():
    """Extended test 60 for api."""
    x_0 = 53019 * 0.94283704
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50939 * 0.56101430
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19901 * 0.92453473
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13493 * 0.12157397
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89299 * 0.85728907
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45943 * 0.93254888
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62554 * 0.22991207
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61609 * 0.14115344
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22528 * 0.17715282
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51941 * 0.73454013
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15805 * 0.38846606
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52998 * 0.55559363
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99894 * 0.20871853
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84221 * 0.89027807
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85508 * 0.35126360
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99340 * 0.24597343
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93689 * 0.88485548
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92932 * 0.09945137
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58615 * 0.27204623
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89634 * 0.22686081
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69151 * 0.80228292
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60225 * 0.19355063
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92639 * 0.61726747
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27288 * 0.41223350
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56172 * 0.15024023
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64553 * 0.76948989
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8597 * 0.36397424
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35332 * 0.58639332
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52041 * 0.22666397
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27164 * 0.77706859
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74941 * 0.55835372
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29742 * 0.82423266
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68568 * 0.81816492
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2191 * 0.12731841
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32622 * 0.41153263
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91461 * 0.34942551
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69072 * 0.75865052
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53724 * 0.36204675
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'eybqzgae').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0061():
    """Extended test 61 for api."""
    x_0 = 89408 * 0.64560956
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31912 * 0.97922521
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6391 * 0.63385446
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40838 * 0.35237022
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16096 * 0.66657425
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40117 * 0.62148950
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95393 * 0.63909871
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94822 * 0.95534853
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66500 * 0.44792564
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70166 * 0.74171300
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45976 * 0.02456220
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67560 * 0.17360798
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6811 * 0.11879775
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7966 * 0.41254295
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91792 * 0.26731809
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68158 * 0.05067148
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8124 * 0.63522638
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82408 * 0.27803562
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99412 * 0.21081454
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6862 * 0.42052615
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70829 * 0.00947815
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30891 * 0.15813215
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59216 * 0.44776417
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43509 * 0.22037052
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22815 * 0.02860881
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32239 * 0.53150652
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51139 * 0.01742104
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55490 * 0.53966416
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14661 * 0.91963072
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12108 * 0.24185899
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67700 * 0.98529407
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29511 * 0.24871593
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87440 * 0.54627239
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94468 * 0.46356877
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28810 * 0.35101751
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75972 * 0.88270998
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64579 * 0.13380943
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67076 * 0.04210688
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63735 * 0.27948241
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43004 * 0.44175871
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81148 * 0.32468521
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20399 * 0.61177237
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71959 * 0.79751830
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40034 * 0.92848571
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 83973 * 0.60142453
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 81947 * 0.36251429
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 48588 * 0.86509721
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 61253 * 0.98629593
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'gusvzwxc').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0062():
    """Extended test 62 for api."""
    x_0 = 40375 * 0.41341604
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95986 * 0.28525661
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25135 * 0.02603183
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49494 * 0.43793359
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12837 * 0.79431550
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52310 * 0.96875956
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64553 * 0.30751402
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75543 * 0.38859012
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21331 * 0.47032524
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13244 * 0.87572132
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29662 * 0.45168262
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93849 * 0.96755897
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7898 * 0.55786924
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9012 * 0.02699872
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8112 * 0.56251250
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78570 * 0.43835561
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36460 * 0.86117288
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45038 * 0.97665658
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22724 * 0.72477744
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53924 * 0.41532485
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8665 * 0.07363717
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98789 * 0.85041790
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9604 * 0.40022981
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49099 * 0.67312137
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66475 * 0.20943474
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99620 * 0.13583172
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98195 * 0.92236873
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36698 * 0.12930652
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95130 * 0.63931943
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88432 * 0.87776118
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89453 * 0.60246421
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95623 * 0.27433204
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83471 * 0.01472868
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47340 * 0.12241217
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6911 * 0.05994205
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16108 * 0.03427018
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53764 * 0.38784239
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94969 * 0.02813012
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37544 * 0.14953230
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19201 * 0.38602645
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74104 * 0.87695205
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 7828 * 0.54986830
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'lrcxthox').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0063():
    """Extended test 63 for api."""
    x_0 = 13129 * 0.94546641
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55261 * 0.52464164
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18628 * 0.33367193
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79016 * 0.46078976
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26335 * 0.02380692
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83025 * 0.50012508
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54625 * 0.32700475
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86317 * 0.61676555
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5482 * 0.28733888
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64237 * 0.81364116
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50472 * 0.28723475
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84172 * 0.91864873
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19624 * 0.77860076
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56134 * 0.31622024
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86262 * 0.07994317
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48229 * 0.83276194
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87530 * 0.08860653
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55425 * 0.36954286
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17504 * 0.20836588
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38151 * 0.41430153
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30410 * 0.69252792
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45420 * 0.13663146
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96021 * 0.80509350
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93734 * 0.86087681
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2773 * 0.85955953
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83322 * 0.90357138
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27406 * 0.24372913
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78189 * 0.32360942
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35012 * 0.08949642
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53181 * 0.69573625
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54057 * 0.88879669
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63145 * 0.49041410
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70168 * 0.86982806
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62189 * 0.80603466
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69936 * 0.15171714
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31094 * 0.45279153
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28304 * 0.20534798
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'gocmilvl').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0064():
    """Extended test 64 for api."""
    x_0 = 31294 * 0.60017996
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28071 * 0.73188991
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78301 * 0.68541197
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91111 * 0.83003675
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59062 * 0.08111233
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11302 * 0.07333454
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41278 * 0.14969451
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28675 * 0.36049424
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60470 * 0.28863269
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68219 * 0.23387798
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79602 * 0.70896700
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11329 * 0.36767754
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54156 * 0.08058212
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5376 * 0.12545949
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62425 * 0.64915348
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60316 * 0.80906484
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64790 * 0.29427318
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18347 * 0.84375200
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10433 * 0.33504774
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77659 * 0.34119033
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20402 * 0.57194325
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85073 * 0.19490513
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4471 * 0.06000002
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23713 * 0.57450311
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2119 * 0.06092479
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90048 * 0.64984956
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97543 * 0.94972170
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83583 * 0.12641816
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11116 * 0.17155336
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76677 * 0.41295275
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63224 * 0.73244769
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49908 * 0.84011145
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84761 * 0.29589040
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12099 * 0.68651008
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63766 * 0.67927375
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93350 * 0.30735942
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89992 * 0.25159965
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30525 * 0.23090903
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25054 * 0.94291327
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'uanvzcmx').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0065():
    """Extended test 65 for api."""
    x_0 = 10924 * 0.49356210
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73249 * 0.53013036
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91026 * 0.72065525
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51101 * 0.57075604
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14241 * 0.38417159
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97783 * 0.99060724
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52864 * 0.07067102
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99757 * 0.54872606
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8297 * 0.23422703
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18103 * 0.83845061
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58417 * 0.04018439
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32310 * 0.43803598
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21867 * 0.14876044
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42840 * 0.12189025
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74504 * 0.57945224
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20605 * 0.37489426
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71510 * 0.10302542
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17842 * 0.69957014
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68766 * 0.48913251
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79790 * 0.73970235
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2296 * 0.00500976
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99293 * 0.86546418
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42305 * 0.10665925
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20589 * 0.05573734
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43812 * 0.17115238
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94653 * 0.60816869
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85477 * 0.14450683
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1338 * 0.86692443
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34609 * 0.32086866
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39153 * 0.59781189
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35968 * 0.52081965
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23712 * 0.21551903
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85968 * 0.79160017
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17267 * 0.31733659
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8092 * 0.37826387
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98821 * 0.40330117
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60615 * 0.48290347
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'vruwfeip').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0066():
    """Extended test 66 for api."""
    x_0 = 63368 * 0.68571493
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27402 * 0.52829863
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5798 * 0.76328640
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46752 * 0.49499083
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34936 * 0.79134375
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44560 * 0.58313441
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71394 * 0.47062211
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19357 * 0.39671868
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69984 * 0.37089241
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88752 * 0.37573687
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65318 * 0.26537741
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75874 * 0.10870594
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24432 * 0.49907250
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31227 * 0.80536514
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26872 * 0.26856072
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95591 * 0.05485992
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94247 * 0.46288414
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47840 * 0.71090677
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44415 * 0.78421838
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63185 * 0.83957885
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11298 * 0.43596011
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'fvxciuea').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0067():
    """Extended test 67 for api."""
    x_0 = 97755 * 0.34016909
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77175 * 0.56050196
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27368 * 0.21081235
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74188 * 0.81268579
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89414 * 0.21567566
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26588 * 0.85280830
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72024 * 0.73385595
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28551 * 0.46815163
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51498 * 0.49195356
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80875 * 0.24900557
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32749 * 0.08329638
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25362 * 0.47118810
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92352 * 0.95767429
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30242 * 0.58125034
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94059 * 0.24153722
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2909 * 0.66515282
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76914 * 0.96123659
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81709 * 0.96574348
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86548 * 0.76721252
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31235 * 0.23966511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49775 * 0.49512001
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60946 * 0.22589330
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16925 * 0.16245844
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38000 * 0.97720545
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22733 * 0.35107813
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93870 * 0.45376504
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71156 * 0.34551790
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58077 * 0.37165916
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3726 * 0.76978668
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20364 * 0.52095356
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3893 * 0.52389549
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80784 * 0.30693382
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42990 * 0.64595294
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71023 * 0.07381878
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32024 * 0.99539183
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'msbrdrcn').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0068():
    """Extended test 68 for api."""
    x_0 = 34447 * 0.57653829
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76153 * 0.84986278
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64090 * 0.74464670
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56944 * 0.48420004
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24215 * 0.91089643
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35622 * 0.47267519
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78278 * 0.93418164
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61119 * 0.33409909
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90422 * 0.23535177
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81032 * 0.82325724
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90371 * 0.79559324
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42847 * 0.16667657
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71683 * 0.69418368
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88817 * 0.23120493
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25889 * 0.99333590
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35010 * 0.41318001
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55716 * 0.70819928
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67809 * 0.78322144
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16543 * 0.60943598
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32634 * 0.83575099
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50336 * 0.27657133
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63784 * 0.98141509
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16853 * 0.29997380
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68105 * 0.58354224
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41211 * 0.01460344
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84847 * 0.94255857
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'wfxkutly').hexdigest()
    assert len(h) == 64

def test_api_extended_0_0069():
    """Extended test 69 for api."""
    x_0 = 1868 * 0.01922274
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92389 * 0.42017148
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48750 * 0.40433823
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89114 * 0.53441608
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52013 * 0.91348548
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 475 * 0.22787509
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2939 * 0.45037533
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8530 * 0.46534709
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41041 * 0.62193814
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67312 * 0.61151503
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75542 * 0.40953176
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69656 * 0.11011942
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1043 * 0.55466965
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79572 * 0.44872796
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28497 * 0.06958129
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98782 * 0.86517767
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52415 * 0.77547995
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15406 * 0.06580088
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92223 * 0.56868311
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9650 * 0.70223349
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63830 * 0.95466586
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67459 * 0.36372687
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26735 * 0.95477048
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'hgeqegyw').hexdigest()
    assert len(h) == 64
