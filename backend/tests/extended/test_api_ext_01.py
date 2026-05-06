"""Extended tests for api suite 1."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_api_extended_1_0000():
    """Extended test 0 for api."""
    x_0 = 75200 * 0.53263990
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73725 * 0.03267242
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99409 * 0.87531717
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91076 * 0.10175934
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89211 * 0.20290266
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69210 * 0.31891014
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55943 * 0.74124844
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16796 * 0.61336839
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97093 * 0.14976669
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55193 * 0.41191764
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8283 * 0.39208983
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13485 * 0.72835333
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35132 * 0.65058994
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80154 * 0.75639822
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18708 * 0.92435803
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42939 * 0.86489687
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76840 * 0.55691020
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77243 * 0.65842633
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95031 * 0.42739687
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39268 * 0.05901035
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22834 * 0.70224850
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68752 * 0.70406325
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26674 * 0.28933791
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44454 * 0.82411186
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14838 * 0.87791252
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94855 * 0.34848448
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73733 * 0.45607913
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77963 * 0.09800577
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34972 * 0.75665399
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21200 * 0.80085196
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7659 * 0.65889538
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59770 * 0.67435350
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93343 * 0.50873469
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72030 * 0.58111524
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85911 * 0.61409312
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76652 * 0.93630861
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'nxpkhais').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0001():
    """Extended test 1 for api."""
    x_0 = 40187 * 0.35405203
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34465 * 0.60857369
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2931 * 0.87049269
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11575 * 0.67600365
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99451 * 0.26106382
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63765 * 0.76466713
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8605 * 0.92175844
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22819 * 0.98546876
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36591 * 0.68951113
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52083 * 0.69420095
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72619 * 0.73527672
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27783 * 0.52071589
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99113 * 0.55760242
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43960 * 0.04885180
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88801 * 0.09563951
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98054 * 0.44243720
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42502 * 0.29407617
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18188 * 0.41382413
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4870 * 0.71543134
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16239 * 0.69700265
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3129 * 0.13593385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49230 * 0.24643665
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97950 * 0.66427704
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63290 * 0.61812159
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90709 * 0.87936994
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37235 * 0.32066899
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5102 * 0.20351544
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54654 * 0.15767212
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18232 * 0.58812490
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66656 * 0.67747879
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11425 * 0.94201308
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94029 * 0.66403262
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82662 * 0.60906305
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68573 * 0.13287362
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73352 * 0.49366889
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47801 * 0.07277398
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41980 * 0.32291188
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3163 * 0.62929972
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80941 * 0.95081592
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84226 * 0.67813429
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27657 * 0.27253501
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 31713 * 0.22711214
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11982 * 0.73856954
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 6406 * 0.56609683
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 75390 * 0.63708983
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 98685 * 0.56866796
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'jrvwttwg').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0002():
    """Extended test 2 for api."""
    x_0 = 81955 * 0.32927804
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89221 * 0.48446979
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82937 * 0.11766207
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33568 * 0.72294980
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9841 * 0.12034556
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75123 * 0.21913305
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64307 * 0.13459291
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68946 * 0.91629005
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52658 * 0.76329049
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93652 * 0.20009797
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72769 * 0.39716531
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10725 * 0.72542481
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6854 * 0.69851897
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35840 * 0.45600038
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17723 * 0.28371135
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87718 * 0.96292804
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76526 * 0.74023084
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83830 * 0.07531924
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24556 * 0.23068157
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91219 * 0.74864164
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73200 * 0.98876973
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51238 * 0.71134410
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36138 * 0.50897097
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5254 * 0.23708104
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'yltcwnsj').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0003():
    """Extended test 3 for api."""
    x_0 = 10785 * 0.46272499
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47243 * 0.39702355
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86179 * 0.13966611
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62843 * 0.35188086
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46744 * 0.77648792
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68339 * 0.30424586
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16363 * 0.38333065
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39312 * 0.10007146
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61095 * 0.71473301
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48506 * 0.87345305
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22349 * 0.66072308
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40101 * 0.20565534
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93544 * 0.07581948
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55725 * 0.10921308
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86253 * 0.04260582
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66975 * 0.85735381
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74425 * 0.75250948
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1954 * 0.54033586
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5522 * 0.60540946
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41960 * 0.01947972
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27113 * 0.55273299
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12387 * 0.46347968
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87881 * 0.90165107
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7874 * 0.25759579
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76071 * 0.39072935
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78424 * 0.48597664
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5290 * 0.47792498
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81452 * 0.66333297
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79502 * 0.56314063
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78642 * 0.94949100
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14937 * 0.85129696
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45100 * 0.01427410
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95568 * 0.84424234
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39461 * 0.88648984
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'olbzdkjp').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0004():
    """Extended test 4 for api."""
    x_0 = 81403 * 0.30902367
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84126 * 0.51657898
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12141 * 0.96539414
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38847 * 0.50031037
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78603 * 0.72408256
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92607 * 0.04707547
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63871 * 0.02873051
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25334 * 0.90830340
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6576 * 0.74218907
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71529 * 0.17644114
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99713 * 0.90285613
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90605 * 0.19538604
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35388 * 0.10878161
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75880 * 0.23498573
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68035 * 0.64467883
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64530 * 0.82281786
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16720 * 0.71806744
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66529 * 0.20542925
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57770 * 0.87856460
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91931 * 0.95410930
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57638 * 0.87674992
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18064 * 0.38500992
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7966 * 0.27909421
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98535 * 0.43756947
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78537 * 0.70444985
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35841 * 0.07577802
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92498 * 0.66776474
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39389 * 0.53623925
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72461 * 0.40334897
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77158 * 0.58819698
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90813 * 0.42254318
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85857 * 0.76853346
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53742 * 0.00278480
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17011 * 0.02748258
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87985 * 0.04783229
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94767 * 0.56340835
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92283 * 0.90665325
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13172 * 0.10351106
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44735 * 0.94725897
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22111 * 0.64214715
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2722 * 0.19495787
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 62090 * 0.81060363
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11252 * 0.42800294
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61905 * 0.24489064
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'pjeentfr').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0005():
    """Extended test 5 for api."""
    x_0 = 97548 * 0.01081246
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90785 * 0.46601545
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12801 * 0.91471015
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22821 * 0.86830256
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44036 * 0.11479374
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98594 * 0.28655241
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69419 * 0.31883379
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22407 * 0.26514288
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53444 * 0.85363331
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21515 * 0.43948323
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73492 * 0.75646275
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44143 * 0.57687143
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83216 * 0.07806090
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55486 * 0.11869408
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87936 * 0.67340360
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64590 * 0.56882284
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84208 * 0.13935358
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99588 * 0.28238096
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90188 * 0.33983351
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28748 * 0.81973273
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62195 * 0.32475302
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79851 * 0.90982384
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59258 * 0.07881099
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 794 * 0.56278155
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64875 * 0.88650263
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7167 * 0.02367469
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96595 * 0.13240521
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77011 * 0.49240688
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6652 * 0.84795099
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87417 * 0.46897034
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97568 * 0.08126965
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43022 * 0.69258571
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26730 * 0.65461506
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48459 * 0.49315151
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63081 * 0.16095852
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81923 * 0.39524455
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50471 * 0.34137567
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74880 * 0.73866740
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66106 * 0.38702697
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52544 * 0.05846187
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80989 * 0.19927280
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69588 * 0.68087490
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 82877 * 0.45196157
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 98878 * 0.55892422
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xsirgotx').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0006():
    """Extended test 6 for api."""
    x_0 = 34569 * 0.51852842
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52097 * 0.62497909
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54131 * 0.17933089
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42234 * 0.69249546
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30826 * 0.09024751
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7769 * 0.66745621
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53515 * 0.54260099
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9138 * 0.46392096
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56274 * 0.52910370
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57918 * 0.74565198
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71316 * 0.29478583
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36152 * 0.21213491
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23226 * 0.03979308
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91703 * 0.23433940
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72811 * 0.01351779
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62111 * 0.29738517
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29325 * 0.08732870
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77452 * 0.46967706
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46337 * 0.82556328
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58845 * 0.76551280
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17599 * 0.66881389
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34318 * 0.72314761
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4043 * 0.73133001
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87441 * 0.41739169
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50088 * 0.09967369
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5116 * 0.12250453
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42560 * 0.13233805
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25835 * 0.38567507
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30647 * 0.04327063
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44683 * 0.48732293
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38664 * 0.46149480
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33531 * 0.45066267
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96180 * 0.62325787
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58426 * 0.74891426
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23461 * 0.92698994
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70397 * 0.79049902
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64550 * 0.16811576
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45800 * 0.26128442
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5109 * 0.20687659
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9691 * 0.79932474
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 66336 * 0.58153493
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18637 * 0.86964780
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77207 * 0.40850409
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 50834 * 0.14732507
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 3756 * 0.51684162
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 55459 * 0.49196809
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 84453 * 0.32743460
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 9416 * 0.60537395
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'rkrkjcwa').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0007():
    """Extended test 7 for api."""
    x_0 = 94075 * 0.05043269
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4620 * 0.04052951
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37985 * 0.18394459
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98719 * 0.55876375
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64388 * 0.63157007
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66106 * 0.50732605
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97962 * 0.35525055
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10224 * 0.12975441
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28619 * 0.10036342
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31561 * 0.65034837
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47699 * 0.59003292
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79712 * 0.42567507
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49652 * 0.08953901
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91790 * 0.58702832
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45035 * 0.50184567
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30363 * 0.05313460
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58092 * 0.65141988
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21214 * 0.22640277
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20010 * 0.68723514
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10074 * 0.61081187
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24523 * 0.81706184
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52338 * 0.25856228
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8199 * 0.92005835
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56899 * 0.75815259
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5483 * 0.38416023
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3536 * 0.54151449
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20466 * 0.10779733
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54521 * 0.42014725
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85248 * 0.54284575
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54967 * 0.84392488
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52940 * 0.55476961
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52615 * 0.35073118
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58428 * 0.33579625
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26416 * 0.65835646
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36784 * 0.22088027
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15985 * 0.29235305
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27903 * 0.02942261
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 14191 * 0.73526924
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21696 * 0.70186724
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87021 * 0.32734365
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34470 * 0.23270069
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12716 * 0.45932300
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62607 * 0.92933322
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 21169 * 0.08857053
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86328 * 0.27380646
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 57346 * 0.88577267
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 21052 * 0.67978158
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 81932 * 0.60772753
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 80290 * 0.48560812
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 47718 * 0.76651334
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'svcfnuut').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0008():
    """Extended test 8 for api."""
    x_0 = 56909 * 0.23014953
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35851 * 0.53192110
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45644 * 0.06136258
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20002 * 0.26625095
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37441 * 0.34648248
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95810 * 0.88629582
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94745 * 0.67518847
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68528 * 0.52944723
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34983 * 0.90587767
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15647 * 0.21569779
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48482 * 0.72175875
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15256 * 0.81013059
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54174 * 0.00529121
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66039 * 0.96808839
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47035 * 0.92176171
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96044 * 0.48226636
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9032 * 0.74155270
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88162 * 0.36747132
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1836 * 0.21331913
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7656 * 0.99711268
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51032 * 0.10457967
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6540 * 0.94984600
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85006 * 0.41238682
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 903 * 0.72170387
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30964 * 0.14141245
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38383 * 0.37062998
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60701 * 0.35290107
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64801 * 0.98105411
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38039 * 0.31380888
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29490 * 0.89417895
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76302 * 0.61729609
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10352 * 0.98338053
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78455 * 0.98249955
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87653 * 0.98396472
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41076 * 0.95245596
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21240 * 0.92162646
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12658 * 0.61528666
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82372 * 0.07120561
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72080 * 0.40278151
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63195 * 0.61615399
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'dtmoknra').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0009():
    """Extended test 9 for api."""
    x_0 = 55540 * 0.31314255
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81931 * 0.05540001
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63383 * 0.28728248
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34615 * 0.74519585
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68926 * 0.90680043
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34262 * 0.14105859
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54401 * 0.43302312
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64819 * 0.47397687
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24685 * 0.40326875
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81932 * 0.81248274
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62000 * 0.00256330
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8072 * 0.65380578
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39790 * 0.47495193
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74196 * 0.42708520
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15195 * 0.69091240
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64684 * 0.86374968
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97285 * 0.19416874
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63814 * 0.19639905
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81590 * 0.01107123
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32265 * 0.92482336
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60668 * 0.57315329
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71320 * 0.16744761
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37343 * 0.69258314
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27518 * 0.97054382
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83853 * 0.46961912
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22596 * 0.77398084
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'rotxnlks').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0010():
    """Extended test 10 for api."""
    x_0 = 14619 * 0.65220270
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70813 * 0.03757781
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9173 * 0.95921853
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67255 * 0.51518367
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6421 * 0.14146279
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68923 * 0.21738614
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23688 * 0.58603139
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54990 * 0.77332959
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51727 * 0.65505711
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98400 * 0.87870892
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90893 * 0.96627874
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1930 * 0.74153160
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80009 * 0.75538106
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87622 * 0.70157623
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67238 * 0.38714832
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66628 * 0.07432647
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38529 * 0.41286366
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46068 * 0.07121824
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46341 * 0.80090607
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42577 * 0.54200313
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63676 * 0.38098638
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29107 * 0.42047287
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12433 * 0.48109631
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74968 * 0.82055615
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66463 * 0.12553145
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86651 * 0.22683169
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5284 * 0.99037464
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41876 * 0.02084656
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15270 * 0.15090252
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51319 * 0.78337572
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76022 * 0.99297191
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88874 * 0.50510727
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92372 * 0.06149820
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52385 * 0.15010068
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28167 * 0.02669659
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11567 * 0.90242120
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11119 * 0.06180481
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69540 * 0.90323130
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79143 * 0.46848705
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 26118 * 0.77022250
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8695 * 0.04966635
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63746 * 0.81413674
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41599 * 0.49116617
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 81082 * 0.59140364
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'nxzyrwln').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0011():
    """Extended test 11 for api."""
    x_0 = 78492 * 0.52753694
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32372 * 0.96956002
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15455 * 0.23097382
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5502 * 0.11256058
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70608 * 0.86619744
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23060 * 0.64756451
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47576 * 0.63788003
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63445 * 0.82690750
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58717 * 0.15361860
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33866 * 0.68446087
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10263 * 0.69155030
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47715 * 0.22571052
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50652 * 0.55305528
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51286 * 0.73719830
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53854 * 0.79088359
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79889 * 0.44570083
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43448 * 0.82919284
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84135 * 0.45066439
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22578 * 0.14568038
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90256 * 0.13083592
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42413 * 0.66227879
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18625 * 0.14500457
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54519 * 0.80714500
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33154 * 0.48200264
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33878 * 0.00572093
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92875 * 0.98729451
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23594 * 0.27738401
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95568 * 0.39484090
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43148 * 0.13176636
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39626 * 0.93578425
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80570 * 0.77757601
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93013 * 0.84161836
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4741 * 0.04602618
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60311 * 0.13366107
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97343 * 0.89602941
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51291 * 0.26692273
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1663 * 0.93812715
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1712 * 0.79679996
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 68343 * 0.97467299
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66104 * 0.61243331
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46836 * 0.41193123
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96646 * 0.02895286
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'sbponapj').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0012():
    """Extended test 12 for api."""
    x_0 = 23173 * 0.90611770
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85506 * 0.70251291
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 827 * 0.03238133
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10088 * 0.49324928
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13066 * 0.31551063
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51940 * 0.78188137
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36105 * 0.13055057
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39471 * 0.61425889
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92060 * 0.76645909
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48586 * 0.12361337
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54041 * 0.03279829
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97586 * 0.75720120
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45972 * 0.79742612
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64481 * 0.91468807
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41682 * 0.13682307
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81381 * 0.03043178
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78159 * 0.41119360
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84926 * 0.71356736
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88656 * 0.26981677
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86852 * 0.22653518
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72311 * 0.75053158
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95246 * 0.08002346
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93539 * 0.44157998
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94932 * 0.80838714
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43124 * 0.05327938
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25737 * 0.21426213
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65383 * 0.24230398
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95231 * 0.07865223
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64618 * 0.90853244
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54323 * 0.35206980
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16750 * 0.32401345
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78699 * 0.39226903
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73584 * 0.15388321
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86277 * 0.68194133
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37156 * 0.76796059
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83790 * 0.77224428
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75736 * 0.07496294
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28997 * 0.50822970
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 32116 * 0.70725795
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10157 * 0.40419500
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80515 * 0.48373346
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63847 * 0.83785105
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'rssmxsye').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0013():
    """Extended test 13 for api."""
    x_0 = 51501 * 0.67133512
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15371 * 0.02992253
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24120 * 0.34794507
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62290 * 0.95670532
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87259 * 0.27195911
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16444 * 0.77300792
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27107 * 0.49731485
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12446 * 0.71413792
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19148 * 0.46721626
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92998 * 0.87700424
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55152 * 0.21132324
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39997 * 0.90775919
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4154 * 0.09591175
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33677 * 0.84616118
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37830 * 0.39008955
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63638 * 0.58542409
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13839 * 0.42806414
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24742 * 0.74657393
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95386 * 0.76708524
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99148 * 0.81916952
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12744 * 0.28498198
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49687 * 0.07200695
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99274 * 0.47499261
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87508 * 0.96629498
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26708 * 0.59757089
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28719 * 0.56215712
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66734 * 0.98202394
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20781 * 0.48405941
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'cfetsece').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0014():
    """Extended test 14 for api."""
    x_0 = 15795 * 0.19096363
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8203 * 0.52908027
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44092 * 0.73615168
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28633 * 0.25498583
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76416 * 0.38086042
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16365 * 0.09205379
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43590 * 0.66123916
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52869 * 0.31383594
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80664 * 0.44264967
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10546 * 0.04464676
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42554 * 0.46949189
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19676 * 0.28123789
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23831 * 0.81634995
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86818 * 0.27157062
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46900 * 0.15722379
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80169 * 0.49950392
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83246 * 0.79854720
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85000 * 0.21331313
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96072 * 0.86310992
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51229 * 0.51754978
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93611 * 0.47232888
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58894 * 0.54371073
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10704 * 0.12939627
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35034 * 0.69334434
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16246 * 0.19822976
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21745 * 0.51288530
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66659 * 0.75829064
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77974 * 0.40597379
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50899 * 0.57865939
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24226 * 0.17072778
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39588 * 0.57997417
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66828 * 0.48253657
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46015 * 0.26004183
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73785 * 0.26791927
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15929 * 0.26001898
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93836 * 0.91891080
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13540 * 0.63887129
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28169 * 0.00518770
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 3203 * 0.66604332
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95979 * 0.45440907
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85934 * 0.03335210
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79314 * 0.56293222
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47500 * 0.85262357
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'wzbnnnfg').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0015():
    """Extended test 15 for api."""
    x_0 = 73363 * 0.12470638
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36798 * 0.27733560
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23170 * 0.03458486
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54368 * 0.52026144
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10197 * 0.10772526
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21785 * 0.86996925
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21537 * 0.16316754
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29820 * 0.44948157
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4708 * 0.22351111
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27123 * 0.24118894
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65759 * 0.70718113
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69063 * 0.23866870
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53723 * 0.03493788
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1865 * 0.37952883
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97664 * 0.42682517
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61584 * 0.91597205
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39035 * 0.95694982
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76360 * 0.85628292
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79416 * 0.54313860
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95968 * 0.91361842
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9495 * 0.73775315
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92828 * 0.38133436
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53053 * 0.01518431
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76818 * 0.75116180
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5166 * 0.21167020
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65961 * 0.91957407
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75695 * 0.65319697
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57492 * 0.97914138
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10411 * 0.49985410
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86772 * 0.59108640
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75215 * 0.90700337
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76818 * 0.03557322
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86105 * 0.19306731
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83156 * 0.99183177
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58199 * 0.86656917
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48889 * 0.16408829
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51152 * 0.42727452
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 51549 * 0.44656673
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96036 * 0.14414175
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97250 * 0.36302879
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79311 * 0.38348820
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57139 * 0.81451297
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12327 * 0.16728838
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11693 * 0.62236326
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 24810 * 0.48382496
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 87498 * 0.80633352
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 25751 * 0.73523639
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 87215 * 0.43565642
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 41266 * 0.35821654
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'kitcdhvz').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0016():
    """Extended test 16 for api."""
    x_0 = 68482 * 0.17438339
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46581 * 0.33278119
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30812 * 0.09608143
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16508 * 0.58358300
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13654 * 0.65857174
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70237 * 0.63690498
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49569 * 0.60042943
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31653 * 0.69469281
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65601 * 0.00816332
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40873 * 0.28525153
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48316 * 0.46186659
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88645 * 0.25644602
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65884 * 0.20150362
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57304 * 0.98514335
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71398 * 0.73543649
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80725 * 0.64956607
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5036 * 0.37555003
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27994 * 0.99065612
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25941 * 0.89474628
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77541 * 0.99015857
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11439 * 0.20250890
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31469 * 0.12636015
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25759 * 0.41441157
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55892 * 0.60130581
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78928 * 0.03649752
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67565 * 0.68016628
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29347 * 0.28207242
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63445 * 0.28863706
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75780 * 0.61569725
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73683 * 0.28149541
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78230 * 0.94702487
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64498 * 0.51521786
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 340 * 0.17409130
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21627 * 0.59992422
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87165 * 0.53821156
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46443 * 0.56015194
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46495 * 0.99289778
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33736 * 0.41561366
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93123 * 0.07960080
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21447 * 0.31273838
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52616 * 0.22587659
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74511 * 0.14153407
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62223 * 0.62411256
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94517 * 0.79689738
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 63699 * 0.17645591
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'fsodvzci').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0017():
    """Extended test 17 for api."""
    x_0 = 38449 * 0.91371797
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50197 * 0.79625476
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3220 * 0.93926331
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34814 * 0.31611207
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50081 * 0.12593880
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78207 * 0.05237404
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35768 * 0.88985633
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11621 * 0.99118046
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40060 * 0.89110324
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62815 * 0.50044909
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63740 * 0.57243243
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83660 * 0.83946766
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80085 * 0.19988750
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66055 * 0.71627186
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42369 * 0.69556634
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97595 * 0.69436129
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4554 * 0.26886709
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62903 * 0.96612394
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42778 * 0.65595285
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38681 * 0.39163552
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42548 * 0.44559644
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62048 * 0.70947862
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24007 * 0.87166110
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84888 * 0.70124084
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85672 * 0.05190137
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41473 * 0.41414679
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95508 * 0.10832381
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7638 * 0.52184246
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'gspxskuz').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0018():
    """Extended test 18 for api."""
    x_0 = 90118 * 0.64335389
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64391 * 0.62931552
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32704 * 0.57932170
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57031 * 0.76103769
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71558 * 0.11648673
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40683 * 0.72258875
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91970 * 0.71643153
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12495 * 0.03545076
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35145 * 0.28211761
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85967 * 0.86465704
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68939 * 0.84296371
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78871 * 0.11966118
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92805 * 0.36574272
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96319 * 0.41592321
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17658 * 0.59973400
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69477 * 0.48548050
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8541 * 0.65556602
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54936 * 0.67259319
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49637 * 0.95156284
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75151 * 0.75472368
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91053 * 0.63610108
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70419 * 0.42549242
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2594 * 0.11521219
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39122 * 0.45358589
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11384 * 0.16064634
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47907 * 0.40246613
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75363 * 0.72599452
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27572 * 0.42840138
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62677 * 0.19135727
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74618 * 0.08058512
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'lckietud').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0019():
    """Extended test 19 for api."""
    x_0 = 47868 * 0.26312818
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72144 * 0.79847610
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48561 * 0.61114013
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13883 * 0.85662877
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22958 * 0.20878661
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44749 * 0.93047247
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30471 * 0.39019919
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83302 * 0.13675004
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58157 * 0.86906272
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56737 * 0.49523128
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45608 * 0.75283172
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97047 * 0.69771088
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89188 * 0.81103971
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76185 * 0.12311297
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34429 * 0.50757719
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79150 * 0.23880866
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9794 * 0.41478849
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42104 * 0.35370195
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82119 * 0.27578213
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18233 * 0.31525017
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18432 * 0.87478690
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27057 * 0.99921718
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22492 * 0.93008148
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85239 * 0.28039934
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19530 * 0.05938652
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46675 * 0.53312662
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10008 * 0.36085171
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33017 * 0.79023095
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86677 * 0.20715511
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49097 * 0.58943807
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9705 * 0.44429578
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74585 * 0.94007184
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43468 * 0.99673036
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22032 * 0.58794903
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21339 * 0.83446340
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81134 * 0.00816440
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60802 * 0.60888294
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46744 * 0.50666453
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14480 * 0.82663856
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64047 * 0.84866356
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35133 * 0.65831561
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53069 * 0.84513364
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 34975 * 0.20465499
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20880 * 0.35569932
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 2905 * 0.61118306
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 11760 * 0.94113619
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 8297 * 0.38396221
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'qzbsrtug').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0020():
    """Extended test 20 for api."""
    x_0 = 1633 * 0.95587262
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50143 * 0.01716837
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81762 * 0.98278328
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9001 * 0.81043404
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7376 * 0.35487949
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21396 * 0.02362016
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69746 * 0.30445033
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3772 * 0.06929866
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82433 * 0.04386554
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53332 * 0.83452588
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3662 * 0.50940019
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37891 * 0.71527991
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85197 * 0.33000798
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36688 * 0.04189029
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96856 * 0.72275046
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46091 * 0.16957012
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79047 * 0.29032874
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96515 * 0.02284108
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35110 * 0.57138219
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91154 * 0.34222899
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34884 * 0.82294025
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60442 * 0.49049305
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42656 * 0.56475295
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23057 * 0.59981514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2602 * 0.89871429
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33091 * 0.63323311
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29546 * 0.57330968
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69373 * 0.86075428
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87322 * 0.09548238
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27376 * 0.88323710
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28657 * 0.41266244
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32897 * 0.71450256
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63784 * 0.96213135
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35110 * 0.82196119
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95463 * 0.75811934
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95672 * 0.93104665
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22002 * 0.31774345
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83120 * 0.73403362
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'adpftppv').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0021():
    """Extended test 21 for api."""
    x_0 = 17520 * 0.19679187
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35295 * 0.64079487
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73541 * 0.11154916
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59678 * 0.68186441
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98442 * 0.91160668
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81998 * 0.09571283
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33275 * 0.10138332
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28367 * 0.86080025
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59827 * 0.19147901
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51702 * 0.90098348
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23464 * 0.25777876
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16435 * 0.76806683
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53127 * 0.09855265
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70703 * 0.56171741
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60395 * 0.88611815
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24047 * 0.35516776
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53595 * 0.42044151
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4160 * 0.73518407
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30412 * 0.98645433
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46912 * 0.88378381
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99757 * 0.27904486
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18001 * 0.94390310
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74728 * 0.93971086
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36178 * 0.69058421
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18790 * 0.73231072
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74665 * 0.50607231
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81493 * 0.82668689
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44393 * 0.66257237
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10606 * 0.53964358
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13613 * 0.77920391
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48536 * 0.56888658
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95485 * 0.88711148
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28712 * 0.86570865
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 429 * 0.10557068
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'bbudzigr').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0022():
    """Extended test 22 for api."""
    x_0 = 61431 * 0.56316448
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82542 * 0.60752799
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84125 * 0.58656829
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23291 * 0.39393348
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26892 * 0.79266688
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8990 * 0.70267321
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57674 * 0.00469897
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37641 * 0.38893428
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85404 * 0.74296544
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17227 * 0.72603719
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28746 * 0.52497927
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8523 * 0.00752771
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27148 * 0.33224794
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37605 * 0.04842211
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57551 * 0.88356893
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75211 * 0.49940089
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85938 * 0.56877151
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17760 * 0.48740094
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15032 * 0.04152859
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63843 * 0.67009438
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74462 * 0.94953137
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45718 * 0.92375063
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36209 * 0.58463790
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5699 * 0.21323203
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77376 * 0.78926339
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2443 * 0.39520251
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 715 * 0.60781997
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75865 * 0.30160875
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17589 * 0.49350443
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1925 * 0.28131006
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58093 * 0.15856777
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45437 * 0.51486042
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96093 * 0.60771477
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20232 * 0.99395588
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70383 * 0.28582666
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 147 * 0.78603046
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83233 * 0.19659944
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1683 * 0.17642636
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15481 * 0.46861068
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56184 * 0.72018699
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 55788 * 0.39994742
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'edntijgf').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0023():
    """Extended test 23 for api."""
    x_0 = 47504 * 0.78832452
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21432 * 0.58105047
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5983 * 0.89897894
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49963 * 0.08087453
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92156 * 0.50301060
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20368 * 0.75419575
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58658 * 0.73051631
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35925 * 0.38602633
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24275 * 0.71482119
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77625 * 0.60663533
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69494 * 0.81282938
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35846 * 0.48062563
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18689 * 0.11983632
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57160 * 0.43332820
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4065 * 0.73834994
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25192 * 0.09020025
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21838 * 0.15314692
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52268 * 0.42603609
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13303 * 0.88523379
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90255 * 0.71953489
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50515 * 0.99327637
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15558 * 0.38334349
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71945 * 0.73164277
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14166 * 0.89903001
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25184 * 0.65756563
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7491 * 0.51126973
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23922 * 0.82140487
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34647 * 0.31422596
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8353 * 0.90150280
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29821 * 0.09993657
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4549 * 0.67287512
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'vnmqqgdw').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0024():
    """Extended test 24 for api."""
    x_0 = 12118 * 0.06891736
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84699 * 0.18251883
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21634 * 0.66506495
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58409 * 0.74583869
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1020 * 0.84638307
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96621 * 0.95528139
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91239 * 0.22212681
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93901 * 0.72601021
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3414 * 0.23296079
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18519 * 0.69394398
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52224 * 0.71079188
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77348 * 0.00502858
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48998 * 0.66275587
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9010 * 0.47072897
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13201 * 0.34562744
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97417 * 0.32937800
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34116 * 0.97900698
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39913 * 0.60512098
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12091 * 0.45154016
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59585 * 0.55941814
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24763 * 0.80540059
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61580 * 0.11062231
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23958 * 0.85225200
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88134 * 0.80391990
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34654 * 0.75289294
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67060 * 0.92612905
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28065 * 0.26457713
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33790 * 0.42202257
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51946 * 0.94937736
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15803 * 0.46036964
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ocdtsyrw').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0025():
    """Extended test 25 for api."""
    x_0 = 69482 * 0.32960984
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21833 * 0.91160684
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38256 * 0.51662538
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74390 * 0.57930492
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65447 * 0.24905340
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5778 * 0.12413854
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78228 * 0.62254021
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 468 * 0.69724858
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79159 * 0.29663663
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66990 * 0.14260006
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80044 * 0.80379087
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59357 * 0.59921298
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68650 * 0.38348768
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18809 * 0.41387616
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41712 * 0.20744464
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44775 * 0.21453278
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15978 * 0.57626455
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97826 * 0.47715794
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29956 * 0.09182663
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25363 * 0.78826233
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ospeympz').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0026():
    """Extended test 26 for api."""
    x_0 = 36007 * 0.08384878
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84296 * 0.90799664
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25701 * 0.96201368
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23832 * 0.14821122
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46423 * 0.35281284
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63974 * 0.29281601
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43197 * 0.23638883
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37111 * 0.46153029
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93013 * 0.99533938
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61126 * 0.04233280
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83937 * 0.60823425
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91142 * 0.66533391
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69356 * 0.32128368
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1716 * 0.54316089
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43152 * 0.38650024
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89352 * 0.19506682
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87266 * 0.19800462
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11135 * 0.11816022
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71129 * 0.36931337
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93953 * 0.25131028
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'sboeqjit').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0027():
    """Extended test 27 for api."""
    x_0 = 4667 * 0.42891278
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12131 * 0.73550178
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74258 * 0.94718887
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73223 * 0.06191763
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76979 * 0.51588006
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32446 * 0.98460820
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59705 * 0.32326038
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30692 * 0.54573485
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50691 * 0.53439081
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68494 * 0.20741670
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57977 * 0.19609751
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32702 * 0.53314577
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47738 * 0.86973716
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86905 * 0.46870020
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12654 * 0.32882723
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87617 * 0.52258715
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46022 * 0.22102702
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86001 * 0.35933685
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10146 * 0.31528405
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62514 * 0.71734376
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70196 * 0.40070360
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21537 * 0.14819400
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37630 * 0.28521873
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11846 * 0.60640286
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34996 * 0.25007194
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58475 * 0.34164671
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15083 * 0.29791832
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90466 * 0.16269340
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78568 * 0.90043552
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 641 * 0.39702316
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83254 * 0.33636193
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30556 * 0.12186897
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16248 * 0.87758207
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57930 * 0.36761019
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52680 * 0.45192238
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58465 * 0.35887684
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'mzuljdxc').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0028():
    """Extended test 28 for api."""
    x_0 = 96545 * 0.47436613
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11378 * 0.04280236
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63739 * 0.07193813
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28060 * 0.37393089
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42955 * 0.40969493
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25482 * 0.10273655
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59368 * 0.91430080
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45839 * 0.45815167
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4830 * 0.74037656
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94724 * 0.57068318
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28514 * 0.65077638
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48194 * 0.80480064
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15670 * 0.14005318
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22725 * 0.16109802
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26902 * 0.99905497
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20808 * 0.94453332
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84218 * 0.58962112
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2646 * 0.25557878
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98109 * 0.70952570
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86888 * 0.24559897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85645 * 0.44233880
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93251 * 0.39761030
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70657 * 0.63753184
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82327 * 0.50100842
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31556 * 0.28735854
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71026 * 0.60459281
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52306 * 0.86251523
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55955 * 0.04703221
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19092 * 0.67975789
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76742 * 0.46797122
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85843 * 0.63972096
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81046 * 0.53603175
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78978 * 0.30616063
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41075 * 0.80484976
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73416 * 0.20911171
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74430 * 0.56630049
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62423 * 0.63920841
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4117 * 0.40352337
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21447 * 0.45478401
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51010 * 0.08406077
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38836 * 0.36271192
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41699 * 0.61755036
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 25754 * 0.14181346
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58293 * 0.61362322
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 63910 * 0.33178579
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4234 * 0.66212915
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 5516 * 0.02748584
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'rrichgrc').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0029():
    """Extended test 29 for api."""
    x_0 = 53583 * 0.39533960
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76772 * 0.47133075
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51792 * 0.39311476
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58156 * 0.50705060
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51384 * 0.83897591
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59916 * 0.44011803
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38631 * 0.26848156
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20238 * 0.36948962
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29052 * 0.01372551
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66019 * 0.25827099
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63101 * 0.06978530
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56407 * 0.36448986
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86202 * 0.65469670
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79976 * 0.88288948
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34773 * 0.86654816
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15078 * 0.74490391
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81894 * 0.09929878
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51491 * 0.28608947
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2869 * 0.88392965
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2504 * 0.98237348
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37817 * 0.71864253
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48271 * 0.66835027
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8627 * 0.93987980
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69544 * 0.01977344
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15824 * 0.00987540
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42202 * 0.66113029
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'plyowtew').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0030():
    """Extended test 30 for api."""
    x_0 = 30705 * 0.20145774
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61706 * 0.26775886
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24009 * 0.67674355
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17336 * 0.42222182
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57367 * 0.06919648
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12325 * 0.16039008
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94114 * 0.54776301
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15198 * 0.79151169
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5390 * 0.04098381
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44513 * 0.09416059
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6626 * 0.87284029
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83227 * 0.75082909
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34951 * 0.25912448
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37062 * 0.72829512
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37189 * 0.16949394
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92808 * 0.15680367
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45358 * 0.26140328
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30297 * 0.66946738
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23153 * 0.27906630
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3911 * 0.52528928
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55067 * 0.36910003
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70066 * 0.80731320
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58034 * 0.61736169
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99640 * 0.58674569
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93264 * 0.11777980
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54369 * 0.71129867
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9862 * 0.44967769
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61350 * 0.51247943
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25212 * 0.34204113
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15853 * 0.79768986
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52449 * 0.68965177
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89305 * 0.35119966
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89961 * 0.08623514
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10664 * 0.71254282
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18958 * 0.16692379
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26090 * 0.25198296
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55266 * 0.36415454
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 37067 * 0.82016006
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37050 * 0.57961446
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41049 * 0.35158618
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 58716 * 0.69017050
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37361 * 0.63744932
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 54925 * 0.99824182
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 13732 * 0.53485448
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 60641 * 0.50075045
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 12793 * 0.53894594
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 50862 * 0.22361414
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 92475 * 0.32947908
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 1534 * 0.23737187
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'untwkuou').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0031():
    """Extended test 31 for api."""
    x_0 = 55914 * 0.18256993
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67616 * 0.74047536
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15227 * 0.27454468
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78446 * 0.80061260
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91975 * 0.10053408
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82199 * 0.19544420
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61090 * 0.57848780
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53688 * 0.84155026
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31363 * 0.03203313
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71054 * 0.24288901
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47476 * 0.57683564
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59275 * 0.60042374
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5393 * 0.83589725
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85082 * 0.73451131
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92558 * 0.92474912
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15491 * 0.96076811
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55917 * 0.76717541
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20599 * 0.86428712
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37669 * 0.74691425
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84855 * 0.80756611
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70730 * 0.41459376
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92545 * 0.50692693
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'xaxwqmaw').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0032():
    """Extended test 32 for api."""
    x_0 = 29811 * 0.38665836
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44020 * 0.53673736
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49718 * 0.96556292
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69400 * 0.74143672
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70316 * 0.10662081
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15171 * 0.57635556
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45801 * 0.83521715
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87151 * 0.35248387
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24934 * 0.19448054
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84293 * 0.54907211
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46760 * 0.08208839
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49079 * 0.39692359
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10611 * 0.42353149
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99557 * 0.73825470
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84689 * 0.27787250
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18777 * 0.89364024
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5920 * 0.30624747
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39954 * 0.34084630
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66667 * 0.80969974
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44417 * 0.23540504
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28746 * 0.88489314
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30260 * 0.17097509
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47751 * 0.42124927
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86524 * 0.72432170
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11007 * 0.45418297
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49266 * 0.80630071
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21470 * 0.13114649
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32357 * 0.31621117
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'dxbwdfgs').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0033():
    """Extended test 33 for api."""
    x_0 = 86048 * 0.39076052
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6206 * 0.33236978
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52371 * 0.45471113
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2165 * 0.43432747
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69672 * 0.82399634
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90612 * 0.74848029
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75116 * 0.41262106
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14246 * 0.80418200
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18156 * 0.08779814
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77943 * 0.78266239
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25255 * 0.46555975
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13807 * 0.84530842
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90666 * 0.60315641
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28772 * 0.95384007
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7702 * 0.86406595
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20460 * 0.36967526
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40955 * 0.50284534
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4117 * 0.38249720
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11740 * 0.39809420
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64161 * 0.88146400
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86286 * 0.40935207
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50838 * 0.08618948
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74471 * 0.92008399
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22136 * 0.93294688
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4837 * 0.50662386
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37693 * 0.26688629
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95403 * 0.87785247
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7142 * 0.55373809
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39590 * 0.89120837
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56439 * 0.80776946
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83311 * 0.24246852
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93105 * 0.35199171
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38863 * 0.76214732
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70052 * 0.72125845
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66339 * 0.87548606
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62862 * 0.78466733
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87278 * 0.97686230
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82898 * 0.81004838
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8152 * 0.24641829
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38689 * 0.58378101
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11750 * 0.04868522
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54848 * 0.47695078
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 94394 * 0.64276143
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 25143 * 0.44916784
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23412 * 0.94296893
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 69860 * 0.53628217
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 29160 * 0.61340703
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 79280 * 0.90767467
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 80371 * 0.84993678
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'deqrptkp').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0034():
    """Extended test 34 for api."""
    x_0 = 24428 * 0.90708759
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61100 * 0.82988908
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90767 * 0.55900506
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43587 * 0.17303478
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50478 * 0.70997802
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34662 * 0.45317136
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35593 * 0.41835076
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27319 * 0.86044640
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1729 * 0.99391670
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65947 * 0.93803599
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2139 * 0.31554718
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18872 * 0.84608225
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50313 * 0.56778565
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13958 * 0.80088587
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26544 * 0.64551529
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91049 * 0.05095785
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26007 * 0.19168960
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76225 * 0.49113173
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15994 * 0.64471701
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8029 * 0.66823268
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61790 * 0.42254416
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28396 * 0.64632456
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53584 * 0.15844002
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44317 * 0.04129239
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86564 * 0.47212031
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39104 * 0.29797147
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'xiednsuh').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0035():
    """Extended test 35 for api."""
    x_0 = 51272 * 0.76178643
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12452 * 0.75555015
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63975 * 0.73531109
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79773 * 0.75483822
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95365 * 0.30261038
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79888 * 0.18050317
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26100 * 0.78889178
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15012 * 0.30628231
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94206 * 0.59413431
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83840 * 0.57231944
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78597 * 0.19206459
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8470 * 0.95332772
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58491 * 0.32372961
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38190 * 0.53857654
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5896 * 0.66778248
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79447 * 0.61360162
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61031 * 0.98916515
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54043 * 0.34337685
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29208 * 0.49756827
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97881 * 0.43479358
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78197 * 0.59891576
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'cfiwvenl').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0036():
    """Extended test 36 for api."""
    x_0 = 53565 * 0.10176450
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6230 * 0.09516357
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86403 * 0.51940013
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13082 * 0.59758349
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55586 * 0.07883126
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86389 * 0.98597484
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87912 * 0.59315632
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6042 * 0.76583308
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36825 * 0.21093099
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99559 * 0.14035503
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95454 * 0.55550967
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4914 * 0.84694340
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35186 * 0.61517851
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69410 * 0.95300400
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35370 * 0.95312624
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42866 * 0.22180027
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10534 * 0.00034781
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70467 * 0.72896867
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25026 * 0.78028128
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51582 * 0.13018235
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90034 * 0.59613734
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31235 * 0.53071108
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90813 * 0.41360479
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69783 * 0.56406277
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ypygggwl').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0037():
    """Extended test 37 for api."""
    x_0 = 39348 * 0.23952395
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98424 * 0.50312868
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39071 * 0.96720078
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3357 * 0.74772788
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78773 * 0.81078015
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74254 * 0.33712297
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59829 * 0.76588390
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30440 * 0.30643139
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81913 * 0.45487548
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4229 * 0.51921806
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89564 * 0.55692632
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41015 * 0.95050772
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1530 * 0.11064491
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60269 * 0.88750996
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9013 * 0.53361284
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52529 * 0.24588654
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72523 * 0.35683291
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2339 * 0.47312517
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61188 * 0.35833999
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80698 * 0.56924136
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97883 * 0.55973273
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76631 * 0.62331532
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33548 * 0.77272912
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21734 * 0.00150140
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56684 * 0.47714724
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'nlgxabhn').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0038():
    """Extended test 38 for api."""
    x_0 = 18510 * 0.03136474
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33200 * 0.77959317
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55073 * 0.96359650
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64631 * 0.38709688
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11155 * 0.96908312
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78216 * 0.51595535
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 258 * 0.56766515
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84848 * 0.51205382
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26100 * 0.00613145
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46957 * 0.93660585
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28788 * 0.93652155
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45906 * 0.30818846
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39387 * 0.75384530
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25344 * 0.30276138
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14166 * 0.75038420
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17896 * 0.34426528
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53704 * 0.13164518
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97178 * 0.97939207
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12432 * 0.32078341
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69439 * 0.56980264
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3345 * 0.88359542
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88878 * 0.62746486
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74852 * 0.82780088
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6819 * 0.89358511
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79344 * 0.31233753
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16526 * 0.72672984
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15568 * 0.01404263
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 943 * 0.36692678
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39366 * 0.37010546
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94748 * 0.36973344
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2394 * 0.07951447
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63062 * 0.07388876
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40513 * 0.40641506
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91183 * 0.59091973
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40320 * 0.12184047
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56182 * 0.77857742
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61121 * 0.02936857
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89142 * 0.81686802
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 334 * 0.94861757
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'utafakwl').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0039():
    """Extended test 39 for api."""
    x_0 = 66496 * 0.93306312
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66615 * 0.40088023
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72024 * 0.64565816
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70549 * 0.51798706
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78152 * 0.08445841
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68084 * 0.02981514
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67546 * 0.63605231
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73325 * 0.76864538
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77836 * 0.18628843
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12166 * 0.83033278
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61673 * 0.17105818
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71176 * 0.28196485
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35464 * 0.64844869
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82628 * 0.41601158
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71426 * 0.97102515
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4214 * 0.19315178
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93639 * 0.19410723
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78882 * 0.53775417
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28076 * 0.54171486
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7369 * 0.93268359
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58944 * 0.44457922
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8603 * 0.14079420
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18132 * 0.41341750
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39535 * 0.67600630
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92183 * 0.18930515
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16438 * 0.69955882
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51008 * 0.59380788
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63953 * 0.38996513
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62974 * 0.19585708
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66496 * 0.79764520
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15866 * 0.98914502
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67937 * 0.32629396
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26402 * 0.45785776
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88686 * 0.40847773
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56999 * 0.64022711
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98877 * 0.63595303
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84191 * 0.01357889
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25134 * 0.85428098
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49663 * 0.03345511
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 36617 * 0.92879419
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17034 * 0.34140532
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 8110 * 0.02301926
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66430 * 0.67727794
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ozujyadz').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0040():
    """Extended test 40 for api."""
    x_0 = 73224 * 0.90276721
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22298 * 0.15110896
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23338 * 0.01309492
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32643 * 0.71603697
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3764 * 0.61252233
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75128 * 0.92132684
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84239 * 0.26340519
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88901 * 0.35464452
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84038 * 0.80337333
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16826 * 0.63291924
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21187 * 0.59116325
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29032 * 0.05789714
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 252 * 0.55790527
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72550 * 0.16837820
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32952 * 0.72776455
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4710 * 0.71838961
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40962 * 0.31706792
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92403 * 0.23520827
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89611 * 0.40434683
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99741 * 0.94518921
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9432 * 0.30120495
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65667 * 0.85903990
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16863 * 0.92495452
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88642 * 0.79959290
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55811 * 0.44376276
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15855 * 0.51007080
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99193 * 0.04515145
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75698 * 0.88096828
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20589 * 0.30054631
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47545 * 0.39768367
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40461 * 0.49342737
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22005 * 0.60805392
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15775 * 0.48012525
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47919 * 0.91403782
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17552 * 0.08562098
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16066 * 0.44902029
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 706 * 0.73730422
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80237 * 0.20875229
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67799 * 0.33738396
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'yfcqawcr').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0041():
    """Extended test 41 for api."""
    x_0 = 16620 * 0.45192070
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68209 * 0.72416426
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78834 * 0.59200084
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48154 * 0.75356983
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75369 * 0.42181066
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81249 * 0.64273184
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3983 * 0.27002209
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9365 * 0.38293914
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9781 * 0.10757563
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23802 * 0.50254465
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47664 * 0.67965081
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52855 * 0.99727520
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27503 * 0.12209126
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62370 * 0.84780709
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13264 * 0.09044052
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43375 * 0.08971355
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46755 * 0.78998534
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52619 * 0.71745048
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28039 * 0.84018683
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39064 * 0.34897337
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73907 * 0.98730930
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79072 * 0.13992465
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40614 * 0.02333181
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21138 * 0.69154659
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82438 * 0.66997047
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49091 * 0.21498127
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'rhkpnbps').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0042():
    """Extended test 42 for api."""
    x_0 = 9801 * 0.84643916
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69145 * 0.98895209
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90759 * 0.95273007
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18522 * 0.29808934
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58896 * 0.97674485
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19151 * 0.77870423
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17079 * 0.71031981
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66589 * 0.32164328
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16518 * 0.34800606
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80821 * 0.80427729
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73396 * 0.80861037
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85520 * 0.15364951
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98260 * 0.28774690
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42219 * 0.17193576
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33833 * 0.74828183
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47424 * 0.66117905
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80252 * 0.55840884
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44939 * 0.48547344
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40997 * 0.10751218
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97598 * 0.29768990
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64320 * 0.56687492
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93230 * 0.65758646
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66700 * 0.16725458
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71569 * 0.25782003
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51134 * 0.15904205
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'bsrupaef').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0043():
    """Extended test 43 for api."""
    x_0 = 35654 * 0.12373726
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99159 * 0.08593957
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32552 * 0.01047950
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77176 * 0.25211369
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25045 * 0.92648209
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55337 * 0.79521730
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99604 * 0.67643645
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66821 * 0.11241759
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99995 * 0.10313468
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6656 * 0.17128792
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19711 * 0.95860688
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1179 * 0.07157270
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48023 * 0.51984077
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99958 * 0.21470921
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80486 * 0.85806087
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11314 * 0.82922622
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 177 * 0.98417743
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58606 * 0.52326301
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71367 * 0.82047396
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80442 * 0.87421618
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74299 * 0.84463200
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12660 * 0.51443679
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96173 * 0.11379989
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51276 * 0.44554329
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26005 * 0.38168130
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74235 * 0.21729804
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56295 * 0.47728453
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6017 * 0.23691960
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47160 * 0.56335688
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63129 * 0.62252206
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86300 * 0.52224856
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8298 * 0.06436586
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86497 * 0.00180983
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36233 * 0.15699696
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18783 * 0.05079498
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78853 * 0.46072252
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42033 * 0.14631018
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9201 * 0.65654257
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37260 * 0.10214714
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68558 * 0.37941476
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 25111 * 0.25233791
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 78220 * 0.66755213
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 27717 * 0.23775016
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 72645 * 0.67190963
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 74582 * 0.92928735
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'sryoyfxd').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0044():
    """Extended test 44 for api."""
    x_0 = 31858 * 0.79401836
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84573 * 0.61343130
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7976 * 0.07844125
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87241 * 0.97230428
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38434 * 0.55412149
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21927 * 0.80118808
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2976 * 0.34310257
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40248 * 0.91850495
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17124 * 0.30334497
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80538 * 0.11505625
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74311 * 0.40256326
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49417 * 0.00049575
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41710 * 0.83447480
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65504 * 0.76015412
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10462 * 0.67698641
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92260 * 0.38394642
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66841 * 0.13236890
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37683 * 0.48290743
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78889 * 0.80686566
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53503 * 0.67082534
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34468 * 0.11596573
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68233 * 0.53576462
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44637 * 0.56489659
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50285 * 0.06328090
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88649 * 0.85206666
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28014 * 0.96462072
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37397 * 0.54111955
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38087 * 0.77815645
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73848 * 0.85375968
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40533 * 0.65672093
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91578 * 0.50649863
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41464 * 0.59466951
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'vsifcycq').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0045():
    """Extended test 45 for api."""
    x_0 = 11698 * 0.73454505
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95440 * 0.14493736
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61829 * 0.62822025
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19610 * 0.70769869
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83518 * 0.60624058
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87057 * 0.45127448
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82796 * 0.43515557
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39115 * 0.40197639
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63437 * 0.93714526
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56449 * 0.36100438
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14814 * 0.39700718
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6210 * 0.22123501
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41691 * 0.65262187
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27323 * 0.91708560
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21615 * 0.03091680
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54988 * 0.77568404
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3990 * 0.61505326
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70801 * 0.82352699
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37627 * 0.24795491
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 361 * 0.81906251
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73031 * 0.94706102
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76609 * 0.79304679
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'nowluclw').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0046():
    """Extended test 46 for api."""
    x_0 = 97486 * 0.50643920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47553 * 0.83066023
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51258 * 0.15379057
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42756 * 0.14402655
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67117 * 0.06907585
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48994 * 0.46232559
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92072 * 0.54356113
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78912 * 0.85068265
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77399 * 0.43532188
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97491 * 0.97059594
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15636 * 0.57810191
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52467 * 0.21478368
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85547 * 0.10754017
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39931 * 0.08844865
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20448 * 0.19743436
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47055 * 0.20234555
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68044 * 0.23713169
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 359 * 0.62490321
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86450 * 0.99234631
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98436 * 0.57126627
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17027 * 0.16878147
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37388 * 0.55211285
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85392 * 0.47097548
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99196 * 0.34312237
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90278 * 0.59110271
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68277 * 0.91243939
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49541 * 0.68675221
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45295 * 0.27202606
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73706 * 0.13775504
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17472 * 0.26115027
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82300 * 0.61142967
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39880 * 0.95415799
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79084 * 0.45490104
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'gbdezpsx').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0047():
    """Extended test 47 for api."""
    x_0 = 82295 * 0.32670411
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99054 * 0.54809765
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 534 * 0.59745422
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68137 * 0.11291491
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1534 * 0.05748853
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89912 * 0.50654734
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32664 * 0.57552034
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25100 * 0.84114495
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86878 * 0.28296786
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6423 * 0.91012134
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19981 * 0.50967289
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41707 * 0.43843237
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1491 * 0.43192502
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9532 * 0.28558736
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14398 * 0.58174728
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81151 * 0.89890791
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58544 * 0.40668568
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9787 * 0.16235237
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68937 * 0.51679357
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33817 * 0.17364721
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38590 * 0.13089321
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64808 * 0.27029829
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72028 * 0.80667042
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79101 * 0.43851007
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46430 * 0.76552942
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41011 * 0.95130821
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34707 * 0.32114074
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54610 * 0.54288615
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1063 * 0.73496988
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22562 * 0.16218510
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68522 * 0.70510302
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13760 * 0.59894902
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89796 * 0.76532900
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72942 * 0.45144465
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29076 * 0.19519404
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38426 * 0.14037807
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59315 * 0.66946982
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92495 * 0.97444237
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56380 * 0.85432189
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'uomjirvi').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0048():
    """Extended test 48 for api."""
    x_0 = 96245 * 0.93185210
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32034 * 0.37205895
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2923 * 0.95103827
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24291 * 0.05287731
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84762 * 0.38597423
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61596 * 0.46810493
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47997 * 0.30838350
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26235 * 0.58217152
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2764 * 0.53058225
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87466 * 0.79136102
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41252 * 0.13381370
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13294 * 0.83622602
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38414 * 0.39015508
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35557 * 0.75983275
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83599 * 0.57492638
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16979 * 0.97859541
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71907 * 0.06667278
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5136 * 0.22959546
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83831 * 0.75310550
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81873 * 0.66021365
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82875 * 0.68904535
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51411 * 0.91450933
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16997 * 0.78040912
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19012 * 0.84081864
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65620 * 0.13410724
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48679 * 0.50343908
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62628 * 0.69885550
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2134 * 0.99818736
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20190 * 0.56203161
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37192 * 0.40728777
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98290 * 0.46222062
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47618 * 0.21065245
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'raydkmfd').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0049():
    """Extended test 49 for api."""
    x_0 = 92565 * 0.11837322
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15537 * 0.35997773
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64855 * 0.03974028
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6292 * 0.45780700
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55084 * 0.38139156
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47475 * 0.11603332
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73368 * 0.60763089
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15500 * 0.60148606
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20355 * 0.40583087
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 991 * 0.67015051
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19340 * 0.55120407
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30776 * 0.57556754
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69661 * 0.79433494
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18468 * 0.22446689
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89387 * 0.72491353
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34211 * 0.06518848
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7348 * 0.55828037
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19715 * 0.23650165
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33583 * 0.93133872
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13221 * 0.45998573
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80547 * 0.37364383
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84278 * 0.77692712
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81268 * 0.36829715
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84508 * 0.66166937
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66009 * 0.18811945
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58980 * 0.48474833
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23553 * 0.53856873
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67037 * 0.27918767
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98382 * 0.90351828
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43705 * 0.48779671
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46138 * 0.41209088
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83149 * 0.65484308
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12929 * 0.45592864
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48860 * 0.50585822
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99161 * 0.69505083
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25626 * 0.37053507
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35901 * 0.38669809
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10934 * 0.25383703
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 32880 * 0.86499769
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 58810 * 0.17328309
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'wxdfzyax').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0050():
    """Extended test 50 for api."""
    x_0 = 61386 * 0.38375540
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5233 * 0.68843530
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45927 * 0.30817483
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75809 * 0.62911726
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43683 * 0.45297382
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62380 * 0.04885675
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18026 * 0.51742601
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38917 * 0.17766846
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60305 * 0.53290083
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72834 * 0.24089913
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59992 * 0.88646915
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7100 * 0.98765199
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58820 * 0.45750840
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94924 * 0.44689913
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71705 * 0.51037055
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83945 * 0.71914560
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1037 * 0.69799699
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59363 * 0.70546333
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58150 * 0.11396910
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79995 * 0.77085709
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96610 * 0.26251173
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76533 * 0.27858806
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45714 * 0.12177389
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94274 * 0.92838138
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92024 * 0.45486908
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66164 * 0.91813209
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62243 * 0.54036845
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52593 * 0.82194449
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 440 * 0.58246122
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69645 * 0.05706961
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46505 * 0.85356017
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26587 * 0.92820713
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49087 * 0.43729494
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71288 * 0.19097460
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48231 * 0.00056201
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96463 * 0.66441392
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47594 * 0.20046557
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82583 * 0.08559808
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34767 * 0.56460080
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77635 * 0.75115691
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91841 * 0.24328658
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27286 * 0.78332444
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'qgdnsfwd').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0051():
    """Extended test 51 for api."""
    x_0 = 47609 * 0.70813730
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42184 * 0.94827354
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46474 * 0.32926043
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72819 * 0.81414747
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48683 * 0.90780585
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6782 * 0.12022690
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19103 * 0.73135219
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44257 * 0.66437692
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29054 * 0.53950240
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2697 * 0.39804911
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20579 * 0.85622956
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79274 * 0.02775356
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15458 * 0.48860915
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62672 * 0.54875332
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22026 * 0.45745914
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60302 * 0.48495019
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5033 * 0.79422379
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46561 * 0.04812046
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48069 * 0.01447337
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73536 * 0.01602406
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14626 * 0.24204500
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50079 * 0.53156640
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80189 * 0.77615264
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16946 * 0.62361246
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45422 * 0.51996601
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8162 * 0.13780419
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35498 * 0.86848802
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83363 * 0.16672187
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31308 * 0.86708230
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52327 * 0.49965045
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97019 * 0.68727322
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'fxzjxmgz').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0052():
    """Extended test 52 for api."""
    x_0 = 99238 * 0.99605772
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98591 * 0.39637532
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92285 * 0.80084835
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86735 * 0.71018617
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11527 * 0.58356084
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34305 * 0.60023368
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75805 * 0.47004285
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91137 * 0.81030972
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32639 * 0.73345273
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16524 * 0.61795965
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64579 * 0.24385779
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52376 * 0.44831882
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54798 * 0.59297460
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48863 * 0.60315941
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91685 * 0.43180100
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93268 * 0.14262163
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22739 * 0.57240069
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75558 * 0.14959072
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56948 * 0.39057508
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71669 * 0.71744070
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67960 * 0.11772700
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15612 * 0.37892895
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18830 * 0.05878129
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14180 * 0.45834867
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74207 * 0.09533141
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78429 * 0.15437854
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85421 * 0.39906903
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67827 * 0.89752240
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49818 * 0.15689787
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10770 * 0.07306335
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59327 * 0.54335337
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38461 * 0.89121738
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2513 * 0.15143231
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80793 * 0.95463941
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27272 * 0.62254871
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99197 * 0.64698006
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35918 * 0.46950309
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36307 * 0.27585085
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26586 * 0.46481627
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54033 * 0.06928687
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 24928 * 0.12250316
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 10305 * 0.35668879
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15250 * 0.71759245
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92410 * 0.64549004
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 45669 * 0.16514406
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 47043 * 0.81952281
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 41311 * 0.18923341
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 90932 * 0.67090764
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 3728 * 0.39582668
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'witeaecc').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0053():
    """Extended test 53 for api."""
    x_0 = 96142 * 0.26801996
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49104 * 0.79199884
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81958 * 0.09614945
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43794 * 0.74770605
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4030 * 0.44411730
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50005 * 0.50272733
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80329 * 0.24626733
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90688 * 0.27918511
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12905 * 0.16792411
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96475 * 0.24905473
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26431 * 0.24413673
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70245 * 0.95714817
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13711 * 0.93461458
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15606 * 0.56090637
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14727 * 0.97196611
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88835 * 0.84365391
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7703 * 0.10169719
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1598 * 0.89965628
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72746 * 0.02416697
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21162 * 0.80765306
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6200 * 0.26562145
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44446 * 0.67588397
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81868 * 0.49608723
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60082 * 0.21772584
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8973 * 0.20019436
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87075 * 0.21289224
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92145 * 0.76124452
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58182 * 0.97061497
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51122 * 0.99747387
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19348 * 0.67464890
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87403 * 0.52712650
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10264 * 0.79900381
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70902 * 0.38705732
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75299 * 0.02344248
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79842 * 0.25613411
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8883 * 0.73216492
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64706 * 0.53084914
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32502 * 0.22175084
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90495 * 0.98909783
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55009 * 0.82523256
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'jcefbdnv').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0054():
    """Extended test 54 for api."""
    x_0 = 58631 * 0.99713586
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68640 * 0.16461254
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81074 * 0.12452822
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65658 * 0.17403623
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84287 * 0.58781586
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1876 * 0.92449451
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12156 * 0.95805003
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99595 * 0.50975414
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87845 * 0.85470432
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68330 * 0.73589785
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43545 * 0.40306074
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73611 * 0.90731737
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71615 * 0.08855554
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96340 * 0.02357944
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92825 * 0.04436120
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67982 * 0.76156275
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89878 * 0.02231196
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8378 * 0.40195462
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41017 * 0.39362074
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32236 * 0.65172592
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6563 * 0.82376895
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88990 * 0.17396554
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38152 * 0.16219849
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'jbwecgor').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0055():
    """Extended test 55 for api."""
    x_0 = 28603 * 0.04051298
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76600 * 0.40092711
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48826 * 0.90597567
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29223 * 0.51662946
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13326 * 0.83035650
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12842 * 0.34915151
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32155 * 0.08969622
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8038 * 0.77581885
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34960 * 0.20548072
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98614 * 0.54142237
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27548 * 0.32169859
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32877 * 0.76231207
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24767 * 0.46825957
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55787 * 0.39183156
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27770 * 0.64686951
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47530 * 0.18326103
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21795 * 0.15032592
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54700 * 0.73747195
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78478 * 0.52074596
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74012 * 0.38910914
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59486 * 0.65098147
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14190 * 0.48215903
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96922 * 0.81647673
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83554 * 0.23068080
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65677 * 0.53363966
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11416 * 0.43461366
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2526 * 0.96851768
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12 * 0.71055068
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30060 * 0.77840760
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72183 * 0.18431775
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93692 * 0.74969524
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70456 * 0.27002091
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57715 * 0.04064965
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69450 * 0.11018221
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70480 * 0.66843773
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50212 * 0.49209554
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 243 * 0.24724696
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'wvoeesox').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0056():
    """Extended test 56 for api."""
    x_0 = 43920 * 0.05107138
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32121 * 0.66907102
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46635 * 0.34274286
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64089 * 0.16399448
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89673 * 0.60252943
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28733 * 0.20176992
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83858 * 0.25651943
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44771 * 0.79538462
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22142 * 0.92469507
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47122 * 0.45078703
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77560 * 0.65633174
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99695 * 0.90204901
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75226 * 0.94019586
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89557 * 0.24846801
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52384 * 0.36391364
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92864 * 0.18653720
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95764 * 0.37248098
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70896 * 0.99013937
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42239 * 0.44571933
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14002 * 0.90086104
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45318 * 0.21153677
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47109 * 0.16829600
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47827 * 0.75629441
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61983 * 0.54015931
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60315 * 0.37308974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9398 * 0.18662951
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85389 * 0.50059328
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89370 * 0.93290888
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45154 * 0.78880941
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13702 * 0.96738523
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50351 * 0.14246619
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32756 * 0.12116336
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63590 * 0.80099012
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'hwwphjmp').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0057():
    """Extended test 57 for api."""
    x_0 = 41042 * 0.15057970
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98664 * 0.44048194
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75202 * 0.12090439
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66365 * 0.59937578
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83017 * 0.33639889
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30626 * 0.71766946
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78455 * 0.91200320
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49369 * 0.78968999
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44940 * 0.88619147
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33595 * 0.56252188
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75994 * 0.12467643
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69374 * 0.81981454
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96413 * 0.85799598
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96114 * 0.24376832
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84111 * 0.08939002
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76847 * 0.50864811
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84709 * 0.39450330
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95254 * 0.25620226
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26732 * 0.75963492
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99193 * 0.31442434
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46193 * 0.51215192
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5419 * 0.50546135
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40972 * 0.56378899
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69622 * 0.30183736
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61689 * 0.91894616
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35941 * 0.28681395
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82427 * 0.14173397
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97419 * 0.41971696
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8620 * 0.21106423
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91420 * 0.23051347
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27955 * 0.52504901
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76448 * 0.56420851
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9173 * 0.87239911
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70008 * 0.85341763
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76914 * 0.92743897
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13049 * 0.94826915
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57672 * 0.61671118
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46916 * 0.48857541
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48312 * 0.13206426
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83982 * 0.56161602
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51128 * 0.39951543
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41753 * 0.61299241
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22158 * 0.83611659
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 2913 * 0.37341853
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'qeyhcdse').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0058():
    """Extended test 58 for api."""
    x_0 = 24335 * 0.60987448
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76654 * 0.08338140
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22831 * 0.35960049
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12641 * 0.68783467
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44776 * 0.10681654
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53189 * 0.29418749
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69566 * 0.27000638
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28205 * 0.61459949
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95447 * 0.02991281
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55861 * 0.26296975
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81255 * 0.01249849
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29248 * 0.48881846
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95227 * 0.76861902
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82998 * 0.04516024
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19589 * 0.49854854
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66351 * 0.66854163
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48603 * 0.94799478
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15612 * 0.00434234
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78426 * 0.46977228
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93744 * 0.72220713
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28673 * 0.36843744
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66327 * 0.28119416
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6371 * 0.73906381
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28999 * 0.38831252
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94462 * 0.25907733
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51142 * 0.86853049
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32310 * 0.22366986
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17884 * 0.51726844
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72642 * 0.52446539
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15432 * 0.57664758
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9793 * 0.22817865
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88483 * 0.89527114
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64943 * 0.66086505
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74089 * 0.75283143
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86663 * 0.66706105
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45537 * 0.03573447
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92944 * 0.42980343
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34693 * 0.30266717
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 95357 * 0.12773368
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'joiiaxbf').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0059():
    """Extended test 59 for api."""
    x_0 = 46786 * 0.55177501
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90525 * 0.84529737
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86738 * 0.69481698
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96673 * 0.54287820
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7714 * 0.48629754
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83224 * 0.78144738
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85034 * 0.16047218
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74834 * 0.05067946
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27250 * 0.48353748
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85767 * 0.80792510
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48612 * 0.07787742
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7764 * 0.84849285
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39193 * 0.06125383
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8892 * 0.39304969
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17231 * 0.46306563
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2491 * 0.66073662
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56021 * 0.84873758
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27738 * 0.32820183
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72104 * 0.45059999
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64214 * 0.30800174
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'lwgtqlye').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0060():
    """Extended test 60 for api."""
    x_0 = 33713 * 0.40402428
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83455 * 0.97642887
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54734 * 0.03889548
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7134 * 0.32009559
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70849 * 0.22073778
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15713 * 0.54700144
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60518 * 0.74727458
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69522 * 0.87181715
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38141 * 0.67682182
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16204 * 0.22135844
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10704 * 0.59615672
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50339 * 0.56022117
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87869 * 0.44999186
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17985 * 0.27779176
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39143 * 0.85875964
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53892 * 0.58990910
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17577 * 0.90413194
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54567 * 0.53050865
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2657 * 0.27208827
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61793 * 0.65029381
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75828 * 0.96995924
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19993 * 0.57773644
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86636 * 0.76986973
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98259 * 0.68469019
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90226 * 0.75776703
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33882 * 0.85264876
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96771 * 0.83078904
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86112 * 0.03781411
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23333 * 0.62285238
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ajepzqse').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0061():
    """Extended test 61 for api."""
    x_0 = 43141 * 0.50459946
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96811 * 0.11203981
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94535 * 0.62016751
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95387 * 0.03780104
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29155 * 0.37557543
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68318 * 0.34445404
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71156 * 0.95547131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22957 * 0.16361899
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19495 * 0.59231820
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2743 * 0.40483118
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16517 * 0.95963286
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64236 * 0.11791428
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82773 * 0.21009398
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48352 * 0.40402912
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77589 * 0.26896765
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76816 * 0.75136139
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70756 * 0.25750474
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4116 * 0.41692629
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88180 * 0.97245841
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78718 * 0.33680076
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47966 * 0.70853034
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46596 * 0.56380015
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17873 * 0.74746828
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52960 * 0.85303512
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48048 * 0.71269408
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8339 * 0.98866747
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66646 * 0.69522770
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12845 * 0.97568048
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25838 * 0.76903528
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14248 * 0.81997748
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79215 * 0.28267326
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98546 * 0.90934784
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45330 * 0.04629976
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 201 * 0.71947446
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89583 * 0.26875283
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90056 * 0.65388601
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7791 * 0.17042892
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90359 * 0.52855291
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'hpnpkhdu').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0062():
    """Extended test 62 for api."""
    x_0 = 27931 * 0.91916538
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11481 * 0.43771932
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31898 * 0.50402460
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41795 * 0.21103733
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34202 * 0.46065730
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95550 * 0.66705576
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98164 * 0.51442320
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13815 * 0.92843694
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87334 * 0.73513008
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31491 * 0.69336449
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60736 * 0.84973982
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20722 * 0.54493418
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30396 * 0.39647595
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30200 * 0.09528942
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19386 * 0.04925210
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25977 * 0.04948517
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27867 * 0.91156979
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45328 * 0.28226095
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88538 * 0.77566048
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61859 * 0.52058383
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91994 * 0.06141375
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32384 * 0.20609634
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4189 * 0.71235757
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28004 * 0.90053756
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88132 * 0.08344167
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18459 * 0.95193255
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99445 * 0.20870855
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68258 * 0.49627968
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39307 * 0.26403753
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98238 * 0.71035167
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'cxzgksio').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0063():
    """Extended test 63 for api."""
    x_0 = 7570 * 0.39513326
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59955 * 0.55679101
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18222 * 0.22816100
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26957 * 0.56498793
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55525 * 0.50853315
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60860 * 0.69699769
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35340 * 0.78111708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44438 * 0.91396600
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11433 * 0.95760300
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82367 * 0.39558880
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12886 * 0.52911016
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62714 * 0.74905033
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95046 * 0.71419917
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91040 * 0.51778639
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30585 * 0.77400491
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98453 * 0.62816326
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99978 * 0.42188798
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23125 * 0.67081882
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94922 * 0.59424387
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39140 * 0.85556580
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82667 * 0.84501818
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95014 * 0.25502025
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83991 * 0.97450226
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56812 * 0.91936713
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58213 * 0.18149393
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89755 * 0.89883636
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87487 * 0.82238894
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'yqgovokz').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0064():
    """Extended test 64 for api."""
    x_0 = 96882 * 0.31468393
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68048 * 0.86946364
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67659 * 0.91820759
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2117 * 0.18653116
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36608 * 0.57361384
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61349 * 0.33800956
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69215 * 0.32650335
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66807 * 0.33316863
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84752 * 0.13851180
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58158 * 0.88079504
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8934 * 0.17270354
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6866 * 0.72555465
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34768 * 0.46720357
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71836 * 0.55099538
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38405 * 0.69620169
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44965 * 0.72021964
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95503 * 0.26571772
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53188 * 0.95883048
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84182 * 0.03484117
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83024 * 0.27125215
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58335 * 0.33936674
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44244 * 0.40568426
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59365 * 0.64195108
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77064 * 0.83204635
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42301 * 0.66431656
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69974 * 0.09071262
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35064 * 0.12809296
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50736 * 0.63663180
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18419 * 0.78655762
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95394 * 0.38703975
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87375 * 0.29120279
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28744 * 0.91787271
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53445 * 0.84044130
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4447 * 0.56894797
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10991 * 0.03878327
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86724 * 0.93684180
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46585 * 0.12602091
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96257 * 0.75347753
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99191 * 0.76986971
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3542 * 0.67084750
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78433 * 0.86157261
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97233 * 0.36885104
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83683 * 0.70304959
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 49072 * 0.07270269
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35060 * 0.58662278
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 49450 * 0.96966393
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 8498 * 0.80426501
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'iyctioce').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0065():
    """Extended test 65 for api."""
    x_0 = 51707 * 0.47345577
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93998 * 0.82707684
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83206 * 0.85413137
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31971 * 0.21454773
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38130 * 0.12681826
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67986 * 0.22565396
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65140 * 0.94722031
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71033 * 0.60900380
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13922 * 0.38008999
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55165 * 0.84138009
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5495 * 0.03892900
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99388 * 0.45703061
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12976 * 0.08413158
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47454 * 0.53201053
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74828 * 0.92534989
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78649 * 0.98871944
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66674 * 0.52018459
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14810 * 0.13652534
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55168 * 0.02434430
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84493 * 0.81726882
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95436 * 0.55929152
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92794 * 0.83250258
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33023 * 0.28232876
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49195 * 0.12409879
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32097 * 0.55289983
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38628 * 0.23802760
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81062 * 0.44645235
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63315 * 0.08327047
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88096 * 0.93991903
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8442 * 0.97377789
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74203 * 0.65931789
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77750 * 0.65793992
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45942 * 0.54926794
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28389 * 0.45538840
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28806 * 0.97889594
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49434 * 0.03715577
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28356 * 0.89888392
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36807 * 0.07496167
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 85944 * 0.79300236
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19969 * 0.45104767
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23677 * 0.32615248
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 56460 * 0.03249270
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'esbnjkjk').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0066():
    """Extended test 66 for api."""
    x_0 = 93956 * 0.23083940
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22334 * 0.12938735
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9213 * 0.92386525
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98896 * 0.68273244
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30787 * 0.51296999
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92567 * 0.36844999
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82121 * 0.63905245
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50036 * 0.36024542
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29965 * 0.83116661
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 383 * 0.84377724
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81633 * 0.31581981
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20103 * 0.32780508
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41090 * 0.95603096
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72894 * 0.40599578
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94504 * 0.43703704
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69170 * 0.33414497
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7101 * 0.76588738
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77749 * 0.02166804
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83937 * 0.13319347
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90239 * 0.77780743
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45584 * 0.33439173
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96856 * 0.98978343
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76080 * 0.30857951
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25749 * 0.72851692
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52539 * 0.72667231
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26949 * 0.47649770
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31531 * 0.57485221
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57889 * 0.04992833
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77312 * 0.92784785
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29254 * 0.39557337
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'iqvarhhf').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0067():
    """Extended test 67 for api."""
    x_0 = 75437 * 0.00084157
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90893 * 0.35930266
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14576 * 0.08791828
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96758 * 0.75680176
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11595 * 0.65804234
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43965 * 0.30177323
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11976 * 0.98028886
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28142 * 0.51826320
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25105 * 0.09751378
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71927 * 0.48485751
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94122 * 0.72758425
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97335 * 0.14529267
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19352 * 0.29642344
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71340 * 0.57025537
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43884 * 0.76102680
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31217 * 0.91944650
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80338 * 0.44617322
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59286 * 0.40024376
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5606 * 0.48416309
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22418 * 0.23188240
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85431 * 0.82276403
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73153 * 0.78171752
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32286 * 0.95164273
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24272 * 0.70529334
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45754 * 0.62112694
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63347 * 0.94396243
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'zpspfadv').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0068():
    """Extended test 68 for api."""
    x_0 = 57904 * 0.69575589
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31077 * 0.09850746
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52092 * 0.15378279
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89480 * 0.52474705
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15628 * 0.49838277
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79679 * 0.80017402
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67776 * 0.82780878
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27076 * 0.11345043
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57577 * 0.07422600
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31119 * 0.47191374
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51074 * 0.47629642
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70755 * 0.74183596
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71686 * 0.42707541
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62367 * 0.45503098
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12279 * 0.22883366
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30497 * 0.12772435
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2681 * 0.48502070
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76279 * 0.64821930
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68003 * 0.76729496
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21883 * 0.82142066
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21524 * 0.09392336
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6417 * 0.98725171
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65968 * 0.25213730
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52034 * 0.66018941
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98869 * 0.80475354
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47292 * 0.19600043
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18534 * 0.98650692
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61557 * 0.70552577
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74448 * 0.39163011
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50670 * 0.06750520
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17858 * 0.33486625
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98738 * 0.12212007
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41801 * 0.49305839
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77746 * 0.70003730
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37015 * 0.44302493
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7687 * 0.07269674
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20384 * 0.59885418
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67432 * 0.95179227
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93472 * 0.06558424
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91142 * 0.55969652
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 67557 * 0.34838095
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'crnwjapo').hexdigest()
    assert len(h) == 64

def test_api_extended_1_0069():
    """Extended test 69 for api."""
    x_0 = 8601 * 0.31995785
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54003 * 0.80511692
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13102 * 0.17992012
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80541 * 0.42556102
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46609 * 0.85878262
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46676 * 0.39215420
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19397 * 0.33127207
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29826 * 0.23737710
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14191 * 0.92389956
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62260 * 0.17994181
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6479 * 0.65591483
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70644 * 0.42607461
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29003 * 0.21091480
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29535 * 0.43543041
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83303 * 0.66849962
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60696 * 0.90407807
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43989 * 0.28325392
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16907 * 0.46823438
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18021 * 0.63927644
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65464 * 0.55372507
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97528 * 0.35775567
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19845 * 0.28309701
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7397 * 0.24310384
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31351 * 0.97718236
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28290 * 0.25869564
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16152 * 0.15540582
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51466 * 0.42207902
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13584 * 0.63270425
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93134 * 0.79102004
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96089 * 0.19907130
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63965 * 0.98607690
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52295 * 0.94880716
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63117 * 0.46791951
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79489 * 0.41043366
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52236 * 0.82278025
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99423 * 0.11328058
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30555 * 0.71447469
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53298 * 0.44644944
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36587 * 0.14133829
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92102 * 0.91757619
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 55880 * 0.29889842
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71582 * 0.01319901
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 34960 * 0.76305679
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 55472 * 0.23136786
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35542 * 0.61711360
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 22736 * 0.49775310
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'fwcffsre').hexdigest()
    assert len(h) == 64
