"""Extended tests for auth suite 9."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_auth_extended_9_0000():
    """Extended test 0 for auth."""
    x_0 = 63166 * 0.04288198
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49572 * 0.44763877
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76708 * 0.37018444
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52993 * 0.88835055
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51344 * 0.66976781
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93686 * 0.38710787
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86769 * 0.09720558
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92718 * 0.68776572
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82306 * 0.79093875
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22565 * 0.35591321
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34483 * 0.63417873
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40344 * 0.09292248
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31873 * 0.20953987
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99135 * 0.10309997
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9254 * 0.31975419
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94406 * 0.77127133
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81305 * 0.56634984
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86326 * 0.21732547
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54930 * 0.45933111
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34541 * 0.78543791
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7617 * 0.65155111
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96454 * 0.53202677
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85318 * 0.65098227
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71629 * 0.30691326
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12306 * 0.87407981
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71734 * 0.04998776
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23036 * 0.72771877
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86900 * 0.56696127
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51225 * 0.36528366
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15835 * 0.48025190
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67744 * 0.73210208
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12549 * 0.65404531
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25517 * 0.68749436
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57614 * 0.24487379
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62858 * 0.05654591
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84568 * 0.67008236
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33807 * 0.81566510
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'klkieyui').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0001():
    """Extended test 1 for auth."""
    x_0 = 2731 * 0.16295525
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74732 * 0.87979181
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89920 * 0.15460200
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59428 * 0.62550500
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48189 * 0.32225664
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49042 * 0.86010706
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74956 * 0.06144738
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21580 * 0.38478749
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21180 * 0.84073979
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16811 * 0.24564059
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62375 * 0.08467272
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68407 * 0.37186758
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5191 * 0.34548435
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72533 * 0.74338965
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76172 * 0.23966849
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2834 * 0.70362471
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10516 * 0.03464437
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74021 * 0.40657313
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47329 * 0.05943658
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10667 * 0.70111704
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19736 * 0.55997429
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4101 * 0.88641399
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65145 * 0.14682113
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91759 * 0.52476455
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52788 * 0.37015227
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59991 * 0.57739718
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97272 * 0.26894024
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65400 * 0.29074495
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53284 * 0.90720597
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42232 * 0.83822888
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66845 * 0.27627768
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29215 * 0.14213235
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49024 * 0.45324434
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36891 * 0.31013371
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'hdepzxng').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0002():
    """Extended test 2 for auth."""
    x_0 = 23636 * 0.09520130
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4258 * 0.11112725
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66860 * 0.76672933
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97123 * 0.57266865
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29507 * 0.27174778
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85677 * 0.11824998
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15808 * 0.24991647
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13724 * 0.64505271
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79462 * 0.39157264
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42671 * 0.15047039
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86823 * 0.64254902
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98347 * 0.00676657
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32500 * 0.08364751
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80619 * 0.50215579
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46596 * 0.93311737
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28606 * 0.37234360
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28239 * 0.78178138
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58481 * 0.35956874
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72346 * 0.27159916
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51357 * 0.65103397
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55771 * 0.95293621
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45886 * 0.17810502
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24722 * 0.74170012
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39834 * 0.41739072
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80757 * 0.98320486
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63688 * 0.65394813
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71652 * 0.30461474
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47843 * 0.09501030
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56331 * 0.30708294
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18876 * 0.44041466
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71931 * 0.94125251
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93063 * 0.08337241
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'oijvarqb').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0003():
    """Extended test 3 for auth."""
    x_0 = 53349 * 0.60333915
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84854 * 0.84230565
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36389 * 0.48001648
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55287 * 0.54368149
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96981 * 0.80617971
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71225 * 0.21481740
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7646 * 0.46577255
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17682 * 0.23544757
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18423 * 0.78038034
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11746 * 0.66360491
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18447 * 0.23689806
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6905 * 0.00617473
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46416 * 0.69312907
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68544 * 0.21538064
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78070 * 0.63197130
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37904 * 0.39582649
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53245 * 0.36342805
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1924 * 0.35043542
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53175 * 0.70468316
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66433 * 0.37309137
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12847 * 0.64957548
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63804 * 0.21917109
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18173 * 0.02347472
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4967 * 0.90583058
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1795 * 0.61223719
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81921 * 0.20903071
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85518 * 0.25673284
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47182 * 0.27643629
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64768 * 0.46033924
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5111 * 0.53564615
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96171 * 0.53556890
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19322 * 0.38901922
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'ojjmdsys').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0004():
    """Extended test 4 for auth."""
    x_0 = 83876 * 0.79579039
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3572 * 0.10659084
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80516 * 0.67962634
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52784 * 0.30973231
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99435 * 0.64453519
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74185 * 0.26266604
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50309 * 0.60779956
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23129 * 0.34303515
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68975 * 0.77579427
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43561 * 0.72499658
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73607 * 0.37321912
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21063 * 0.23674291
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25679 * 0.30666448
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61763 * 0.14192263
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56777 * 0.52828281
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69595 * 0.08367787
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24499 * 0.72888241
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26214 * 0.02929622
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9196 * 0.36156395
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83371 * 0.11075717
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37146 * 0.59532443
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56964 * 0.15713475
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47668 * 0.59053600
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65339 * 0.69993867
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'upxzvcsk').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0005():
    """Extended test 5 for auth."""
    x_0 = 93118 * 0.26389474
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85919 * 0.59982187
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89971 * 0.42965167
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74162 * 0.37210665
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43434 * 0.91350299
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72517 * 0.82294622
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74871 * 0.99498329
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68993 * 0.85691476
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91822 * 0.80176841
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28049 * 0.80730500
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30453 * 0.64168901
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60748 * 0.74306667
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24526 * 0.64009573
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13722 * 0.77018135
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70594 * 0.49639628
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9743 * 0.31651162
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81262 * 0.92461318
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95726 * 0.12778100
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35408 * 0.47860533
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18793 * 0.57557048
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5272 * 0.66743988
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43734 * 0.05823634
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32937 * 0.05411792
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29552 * 0.03170221
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60376 * 0.76890922
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47061 * 0.46461740
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30820 * 0.14096332
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7390 * 0.49625285
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39834 * 0.65585357
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29664 * 0.15526336
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90086 * 0.44304141
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73850 * 0.76568882
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2939 * 0.26725100
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43134 * 0.86437805
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35580 * 0.73158944
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36275 * 0.24362392
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5168 * 0.39169908
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16385 * 0.50453172
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10268 * 0.24906306
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91095 * 0.29312511
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 55272 * 0.96638568
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 64017 * 0.53213692
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47937 * 0.31361612
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 72517 * 0.92166920
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'ihurtuum').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0006():
    """Extended test 6 for auth."""
    x_0 = 55117 * 0.81672311
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9288 * 0.43832493
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52975 * 0.27714548
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52863 * 0.34928717
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62746 * 0.60706198
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59259 * 0.20180249
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6594 * 0.56175272
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52970 * 0.11716506
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65322 * 0.51570807
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45915 * 0.98724247
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2884 * 0.31682749
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15502 * 0.56859029
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27386 * 0.57329577
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77761 * 0.49490858
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70743 * 0.69791003
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82330 * 0.54226091
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70665 * 0.99527637
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10160 * 0.41901189
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40547 * 0.99504732
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16246 * 0.17051244
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34511 * 0.59988445
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9927 * 0.61227913
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57807 * 0.09118412
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80226 * 0.22009977
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60869 * 0.73822316
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40911 * 0.03855658
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57571 * 0.35362615
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68467 * 0.42438718
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32871 * 0.40046520
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7014 * 0.74761664
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68789 * 0.00712269
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18127 * 0.28208408
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'wfajffyp').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0007():
    """Extended test 7 for auth."""
    x_0 = 57256 * 0.55186263
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12103 * 0.48912696
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31357 * 0.39354249
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55955 * 0.59882624
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17393 * 0.81397954
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75508 * 0.42154067
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75701 * 0.61221815
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99371 * 0.85265098
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3952 * 0.25797655
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39711 * 0.43101719
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97687 * 0.33089681
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43969 * 0.24273229
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30692 * 0.63412046
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7438 * 0.38331050
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29593 * 0.74689905
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12120 * 0.81435378
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37247 * 0.49427712
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40351 * 0.30450735
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79055 * 0.18989205
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46310 * 0.02794288
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33057 * 0.82797238
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25046 * 0.03969398
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70447 * 0.87561193
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6627 * 0.52290593
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76450 * 0.24380699
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64229 * 0.97267377
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93927 * 0.69705831
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61520 * 0.27565511
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85454 * 0.16161218
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33209 * 0.00837934
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66778 * 0.92859342
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9049 * 0.48442256
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25785 * 0.09194091
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51213 * 0.22048825
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27408 * 0.35217479
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54963 * 0.03909892
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74018 * 0.30721275
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50816 * 0.03713878
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13239 * 0.19646986
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52325 * 0.87808284
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27854 * 0.74680203
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41347 * 0.61568429
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28994 * 0.66996759
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84982 * 0.44160984
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 13596 * 0.00252687
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 78926 * 0.26225782
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 7182 * 0.40490708
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'qixrkjiy').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0008():
    """Extended test 8 for auth."""
    x_0 = 5943 * 0.05663878
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79638 * 0.01307413
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34965 * 0.46069412
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89519 * 0.43265933
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9421 * 0.41870706
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55918 * 0.98503510
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88209 * 0.61223223
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8458 * 0.55122594
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21889 * 0.61311074
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38078 * 0.70674850
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86188 * 0.81286715
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74799 * 0.27289510
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6305 * 0.78340710
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41750 * 0.90614778
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43071 * 0.18839938
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42286 * 0.39257551
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66298 * 0.15810242
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2360 * 0.30306117
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72780 * 0.09098953
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46494 * 0.18841752
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58548 * 0.18552464
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37097 * 0.02113823
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78303 * 0.07017234
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18957 * 0.75433961
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10883 * 0.87825971
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9702 * 0.96362752
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26425 * 0.93762762
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75288 * 0.42441012
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79453 * 0.41402788
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2999 * 0.17160284
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1188 * 0.98594131
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15940 * 0.63528716
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74722 * 0.89893548
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48295 * 0.83428820
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92052 * 0.48565360
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32217 * 0.57969106
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96300 * 0.33330829
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21860 * 0.20792823
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'qgtunhti').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0009():
    """Extended test 9 for auth."""
    x_0 = 25057 * 0.81619683
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17240 * 0.37985776
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27364 * 0.97245253
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20284 * 0.57419631
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7496 * 0.25529117
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49754 * 0.45834008
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15543 * 0.48722390
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41907 * 0.32229136
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45452 * 0.01980974
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19047 * 0.72137097
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93603 * 0.58318656
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81432 * 0.88414185
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15903 * 0.60528094
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34658 * 0.25445106
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25747 * 0.58136875
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52358 * 0.45861051
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75481 * 0.29076478
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85837 * 0.79481692
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46970 * 0.35988444
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8071 * 0.05761013
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55486 * 0.22574602
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17236 * 0.45364147
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'nxwyeqaj').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0010():
    """Extended test 10 for auth."""
    x_0 = 11034 * 0.52965461
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31136 * 0.85184783
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24761 * 0.79645401
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49458 * 0.12148167
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16120 * 0.61642460
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43775 * 0.27424139
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78457 * 0.23103917
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71098 * 0.19151907
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87223 * 0.18560350
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59923 * 0.92405914
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77322 * 0.32168944
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92989 * 0.81913187
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75309 * 0.31008503
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78642 * 0.42992339
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54794 * 0.73609211
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90805 * 0.76190049
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53930 * 0.64372449
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63321 * 0.68252602
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11976 * 0.60516367
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23437 * 0.04938291
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27079 * 0.18926471
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88503 * 0.17492230
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87042 * 0.41279757
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87485 * 0.31536907
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80038 * 0.49345801
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2206 * 0.32547601
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40289 * 0.45739492
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14233 * 0.87924035
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8230 * 0.79110873
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63207 * 0.88940437
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31793 * 0.79214896
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55615 * 0.05610014
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5999 * 0.59479986
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79538 * 0.52009244
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28685 * 0.10411492
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7247 * 0.58596896
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93014 * 0.34299769
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67293 * 0.99431785
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83226 * 0.50816797
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16920 * 0.20603831
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11357 * 0.11109227
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 11280 * 0.36447433
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44163 * 0.32302285
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27101 * 0.49166770
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71098 * 0.78237461
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'tgzhjvnm').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0011():
    """Extended test 11 for auth."""
    x_0 = 70824 * 0.41805888
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50717 * 0.26749513
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80423 * 0.04249407
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99279 * 0.58613703
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61580 * 0.41723897
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53384 * 0.64239559
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83385 * 0.58319846
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31368 * 0.28441852
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79017 * 0.02392342
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43376 * 0.71420537
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84377 * 0.43324646
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 0 * 0.96058770
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21651 * 0.93357600
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8972 * 0.22211066
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58038 * 0.14207687
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28063 * 0.01434423
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41278 * 0.92312518
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6597 * 0.93106170
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5282 * 0.14905306
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50687 * 0.73686566
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97156 * 0.23598484
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46265 * 0.96930030
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29925 * 0.56551064
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69423 * 0.36894035
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98514 * 0.50820692
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5688 * 0.94446633
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25095 * 0.38261830
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40473 * 0.23402554
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16000 * 0.27492378
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36412 * 0.72314159
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26983 * 0.67432001
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81771 * 0.38036975
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49306 * 0.66920002
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ubzymtjl').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0012():
    """Extended test 12 for auth."""
    x_0 = 32324 * 0.15955290
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37003 * 0.88190136
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98825 * 0.57517590
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45740 * 0.10112041
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21987 * 0.91483810
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47566 * 0.00520095
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97809 * 0.63530262
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77502 * 0.98857587
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6002 * 0.62743002
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34701 * 0.72287459
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58343 * 0.92539124
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26644 * 0.30936415
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49249 * 0.63279538
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45332 * 0.36667038
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1234 * 0.86410623
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41597 * 0.80678639
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88387 * 0.64821882
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72746 * 0.55708651
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92551 * 0.26731792
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5408 * 0.45994803
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41707 * 0.65885561
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27129 * 0.59645625
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20764 * 0.12577141
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66072 * 0.54353476
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76309 * 0.36736043
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12819 * 0.37756637
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67027 * 0.13878049
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78483 * 0.03444225
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53921 * 0.74098795
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6453 * 0.15745457
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72385 * 0.57144348
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27107 * 0.90407121
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31921 * 0.00835363
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3653 * 0.73379524
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27109 * 0.16343410
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29357 * 0.24304896
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75478 * 0.71163425
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81818 * 0.67138239
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30889 * 0.89691997
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 5250 * 0.73603342
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77075 * 0.26104930
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63429 * 0.48780744
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 72718 * 0.73964665
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 17412 * 0.07609128
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 97421 * 0.38388088
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'vfqmsshg').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0013():
    """Extended test 13 for auth."""
    x_0 = 25621 * 0.22832716
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70066 * 0.14982591
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59484 * 0.83022609
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82719 * 0.93964722
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82696 * 0.68504366
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4457 * 0.05796088
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22806 * 0.80380926
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24691 * 0.44241544
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36412 * 0.12616641
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13114 * 0.83872653
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72034 * 0.74174734
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55436 * 0.71030703
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82488 * 0.41176782
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19161 * 0.50596683
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90292 * 0.30205767
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19849 * 0.91021844
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68563 * 0.66572498
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24651 * 0.00491037
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26277 * 0.00334101
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76130 * 0.49534819
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29575 * 0.41164752
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66666 * 0.30511135
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7393 * 0.08928715
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91532 * 0.48307242
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85844 * 0.35308113
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'valbdykc').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0014():
    """Extended test 14 for auth."""
    x_0 = 84923 * 0.02524389
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49559 * 0.21950787
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24020 * 0.75357503
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28948 * 0.40286047
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30987 * 0.17066578
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83666 * 0.88334538
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70552 * 0.38032227
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78726 * 0.50318413
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86122 * 0.38198170
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82645 * 0.09260907
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22122 * 0.87925696
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87505 * 0.76088475
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33873 * 0.49661565
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9975 * 0.46806611
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94035 * 0.41501729
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96999 * 0.88489480
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56151 * 0.39583117
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23975 * 0.98475517
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39519 * 0.78170844
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 472 * 0.98597724
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60951 * 0.52373913
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11997 * 0.56842624
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2946 * 0.19355461
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'zrjvxinv').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0015():
    """Extended test 15 for auth."""
    x_0 = 47844 * 0.04729436
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26581 * 0.20324110
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91001 * 0.76279702
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77690 * 0.83965865
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2371 * 0.44206202
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71658 * 0.26229611
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59334 * 0.13360443
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 582 * 0.33798738
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78449 * 0.61629333
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76281 * 0.31638258
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20909 * 0.66015880
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73433 * 0.28600349
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94541 * 0.92496549
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80801 * 0.26704727
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77009 * 0.89941579
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89794 * 0.70744137
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77406 * 0.46893027
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58423 * 0.28008287
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32574 * 0.75113014
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 589 * 0.05456020
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4149 * 0.59585579
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27058 * 0.10765063
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92080 * 0.23845905
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91363 * 0.16293650
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25695 * 0.17728968
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69260 * 0.91028553
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62390 * 0.70845336
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2369 * 0.72639073
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87477 * 0.25969129
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99153 * 0.13325568
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87899 * 0.27208138
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25216 * 0.05093457
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43025 * 0.55378169
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'mchgqult').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0016():
    """Extended test 16 for auth."""
    x_0 = 29049 * 0.62308491
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67084 * 0.84769793
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41481 * 0.60451776
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14805 * 0.34458129
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14817 * 0.40014191
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28859 * 0.59623298
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11889 * 0.50376833
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54187 * 0.27635506
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18656 * 0.91087279
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72096 * 0.27829592
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93751 * 0.47742783
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87437 * 0.59836090
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28189 * 0.71263563
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59558 * 0.20522023
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76372 * 0.68942556
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78952 * 0.01132660
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52112 * 0.60634016
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92626 * 0.77950103
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48482 * 0.41598601
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38135 * 0.84772225
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80905 * 0.17461599
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22628 * 0.67645425
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66380 * 0.95569282
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68703 * 0.37703356
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62708 * 0.99298222
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7909 * 0.31692820
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14324 * 0.76323646
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63626 * 0.89752646
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48632 * 0.59570308
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10593 * 0.43246134
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64580 * 0.55672205
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80110 * 0.08390400
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17644 * 0.06915532
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63928 * 0.50894835
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98985 * 0.88880370
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87289 * 0.61294702
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74176 * 0.22562374
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43988 * 0.44936008
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66700 * 0.78864479
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20452 * 0.00337606
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 57364 * 0.90224671
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'lccjkcyz').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0017():
    """Extended test 17 for auth."""
    x_0 = 12095 * 0.84008110
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45939 * 0.81608234
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81981 * 0.16531587
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39218 * 0.54740178
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11734 * 0.05887421
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24578 * 0.51904129
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81734 * 0.11646702
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92491 * 0.07710949
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58223 * 0.93173525
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35807 * 0.97338003
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25709 * 0.73686403
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73390 * 0.67298487
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33179 * 0.31235613
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85854 * 0.67667295
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84919 * 0.03587380
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63870 * 0.56505821
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5766 * 0.80786253
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34858 * 0.60248791
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90432 * 0.91186232
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 699 * 0.78892301
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29887 * 0.20966602
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42622 * 0.34628822
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64655 * 0.29360863
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72436 * 0.08151587
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73877 * 0.10592664
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29787 * 0.53224114
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6644 * 0.21069852
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29473 * 0.13547697
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79507 * 0.33874529
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42795 * 0.43139394
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5410 * 0.57135831
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74348 * 0.82313486
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93871 * 0.74388194
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91319 * 0.12116091
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31212 * 0.10172959
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46149 * 0.98727577
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70846 * 0.59728349
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46232 * 0.48617413
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47465 * 0.31941437
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47068 * 0.88787146
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 22297 * 0.16522556
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 86291 * 0.43078899
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 37242 * 0.25900851
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 85211 * 0.24885132
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 12728 * 0.82676478
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 27212 * 0.04470497
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 42469 * 0.60466415
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 63037 * 0.39742122
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 77354 * 0.17879161
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 71627 * 0.04504293
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'jlzscojt').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0018():
    """Extended test 18 for auth."""
    x_0 = 82056 * 0.90627612
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22865 * 0.69595306
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78306 * 0.93857583
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30229 * 0.15232305
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88114 * 0.99802051
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49703 * 0.17833693
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8040 * 0.01887416
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20756 * 0.79236661
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53190 * 0.15905424
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18125 * 0.56228791
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85464 * 0.05196273
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69307 * 0.54512891
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9390 * 0.94842852
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48077 * 0.35307609
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64205 * 0.59723164
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23094 * 0.59501050
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27552 * 0.10318357
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60001 * 0.35788988
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95420 * 0.08610389
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60081 * 0.72400564
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18936 * 0.59277540
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61845 * 0.25985122
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15126 * 0.24676360
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13079 * 0.09729492
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64018 * 0.63584594
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53163 * 0.13129417
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28917 * 0.77092992
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11905 * 0.15865203
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13117 * 0.37365598
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20791 * 0.72401274
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77676 * 0.95345741
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26254 * 0.56585565
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'exvwgqkd').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0019():
    """Extended test 19 for auth."""
    x_0 = 5444 * 0.86132377
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31426 * 0.25194313
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67843 * 0.73510214
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72035 * 0.04535209
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68723 * 0.25680091
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75737 * 0.66419471
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15429 * 0.30597988
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98238 * 0.93123251
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64603 * 0.99435258
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41994 * 0.45370941
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18256 * 0.81417710
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11457 * 0.84835973
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39783 * 0.34278015
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25644 * 0.72510769
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68259 * 0.76430925
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91271 * 0.41584585
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77348 * 0.41863312
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67871 * 0.89285232
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3873 * 0.18503264
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49159 * 0.35174264
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52851 * 0.07986066
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27096 * 0.87675356
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71348 * 0.98411631
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78382 * 0.98067434
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44518 * 0.64433258
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25132 * 0.92713826
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39706 * 0.65011633
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96765 * 0.26076231
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5266 * 0.97383700
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38462 * 0.77048663
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10344 * 0.23127408
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97650 * 0.66477916
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14354 * 0.72891145
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37849 * 0.62915578
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76034 * 0.56154668
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42561 * 0.15172968
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51663 * 0.26091493
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82209 * 0.75182689
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63983 * 0.62408375
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 656 * 0.57921722
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49068 * 0.47900192
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93410 * 0.31164239
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57437 * 0.62640524
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 29899 * 0.88666936
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59063 * 0.33732733
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 73584 * 0.37206076
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'waichuxb').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0020():
    """Extended test 20 for auth."""
    x_0 = 13281 * 0.32750298
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49224 * 0.46353996
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15842 * 0.17359193
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72341 * 0.32620928
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41658 * 0.11425071
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5571 * 0.43438022
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65610 * 0.51944329
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95538 * 0.00049674
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59543 * 0.42276217
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39570 * 0.32172006
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77488 * 0.66088072
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13238 * 0.32119731
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18202 * 0.91985250
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45066 * 0.93779711
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86549 * 0.01913043
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54483 * 0.34908191
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98904 * 0.30169229
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33036 * 0.69606858
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64727 * 0.00087251
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49147 * 0.14952009
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96800 * 0.89698205
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17925 * 0.59743594
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87714 * 0.22282226
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47495 * 0.02944027
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26188 * 0.04544100
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31260 * 0.63505406
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17253 * 0.04128688
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50613 * 0.74487563
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80876 * 0.95020761
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'kergndpu').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0021():
    """Extended test 21 for auth."""
    x_0 = 61125 * 0.52231451
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96678 * 0.93334437
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44196 * 0.89256906
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29025 * 0.82550469
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88680 * 0.08066175
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16756 * 0.48512802
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29749 * 0.84272533
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68670 * 0.92359592
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40779 * 0.56228924
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3373 * 0.63414991
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74848 * 0.34290932
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28046 * 0.63722018
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70321 * 0.22652040
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89873 * 0.26446938
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19474 * 0.52409824
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71174 * 0.22479286
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30882 * 0.02361307
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55680 * 0.95157913
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2558 * 0.77840448
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43707 * 0.22868534
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27036 * 0.16190315
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89350 * 0.01636429
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1755 * 0.91006721
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85264 * 0.27244883
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91129 * 0.56032293
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19872 * 0.03649982
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9575 * 0.14678626
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83460 * 0.45379452
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88340 * 0.47830420
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75639 * 0.95920599
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15147 * 0.18424767
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88607 * 0.97309869
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38480 * 0.21705357
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21515 * 0.97134381
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52113 * 0.24544481
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'utumskyh').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0022():
    """Extended test 22 for auth."""
    x_0 = 3017 * 0.83166521
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52409 * 0.32144704
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94639 * 0.19956872
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54554 * 0.45823049
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1426 * 0.09724609
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33868 * 0.93455838
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39917 * 0.99491380
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70048 * 0.65709351
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90770 * 0.09428936
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70583 * 0.60654712
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11497 * 0.93070228
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94977 * 0.61764025
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97520 * 0.65948144
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1968 * 0.68195407
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59839 * 0.53186917
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68426 * 0.99173390
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81746 * 0.81621420
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23009 * 0.59048224
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18614 * 0.89224600
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85479 * 0.28494295
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5166 * 0.79149798
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22861 * 0.64929858
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7887 * 0.06230804
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53177 * 0.05570241
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3998 * 0.11364392
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95065 * 0.23924568
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70736 * 0.55674250
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77522 * 0.99459156
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91249 * 0.17153255
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61919 * 0.23809002
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9236 * 0.10828944
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21630 * 0.95027562
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24726 * 0.96117651
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3565 * 0.52947363
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8479 * 0.89743287
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31035 * 0.04745252
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75632 * 0.66210092
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5474 * 0.30503068
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37100 * 0.85633567
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8735 * 0.72745398
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62384 * 0.84864788
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52176 * 0.22816736
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77310 * 0.67480471
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 67725 * 0.14494758
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 66113 * 0.75322688
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 45902 * 0.09470867
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 24670 * 0.93370748
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 11738 * 0.19854734
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 48688 * 0.95716809
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 48261 * 0.39969036
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'zbmcqylt').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0023():
    """Extended test 23 for auth."""
    x_0 = 54473 * 0.72975430
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82578 * 0.85051843
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2948 * 0.25100475
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23663 * 0.77679124
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53772 * 0.02032498
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5028 * 0.71373897
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50802 * 0.57356925
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21681 * 0.70576680
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98212 * 0.56931045
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40923 * 0.67609889
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5301 * 0.60792512
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64800 * 0.91065708
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71031 * 0.28340466
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56330 * 0.76503696
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50775 * 0.19383352
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18427 * 0.40981648
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19375 * 0.58225276
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13080 * 0.89657955
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47394 * 0.04230994
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29521 * 0.18469083
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67892 * 0.06065555
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97663 * 0.56944255
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69766 * 0.33271683
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20576 * 0.42034873
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31221 * 0.86047731
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10728 * 0.11791895
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5704 * 0.56587052
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75590 * 0.18902440
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58204 * 0.50558444
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9227 * 0.82508535
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19516 * 0.02319738
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83993 * 0.54833809
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51092 * 0.57873160
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70886 * 0.32029700
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65827 * 0.00255328
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52493 * 0.88639557
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58924 * 0.90228438
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32754 * 0.02488276
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9796 * 0.42530467
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90609 * 0.03736092
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 57791 * 0.92190614
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 17657 * 0.59300292
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 34259 * 0.19808799
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 57974 * 0.84381394
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 3861 * 0.34212363
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 92795 * 0.88659021
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17342 * 0.26799031
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 57718 * 0.39065198
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 78086 * 0.81308351
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 97048 * 0.82411703
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ggpwqzjg').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0024():
    """Extended test 24 for auth."""
    x_0 = 45984 * 0.45341924
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20737 * 0.88126737
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17406 * 0.20027256
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47927 * 0.02137758
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72331 * 0.34419648
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55853 * 0.01100823
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26614 * 0.07969470
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8345 * 0.58845801
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26116 * 0.00637612
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40889 * 0.09091406
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69294 * 0.92689638
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34806 * 0.26086446
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9066 * 0.10304432
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46495 * 0.61202845
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49541 * 0.55065457
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62346 * 0.81622583
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39822 * 0.98307672
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42073 * 0.63223335
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38784 * 0.46999805
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97478 * 0.73895265
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75073 * 0.97353873
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31129 * 0.76900913
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66217 * 0.02575993
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21241 * 0.34378101
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94542 * 0.90034883
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36794 * 0.33812542
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65473 * 0.95805836
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1635 * 0.60363679
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89100 * 0.88005009
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9471 * 0.59686324
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74251 * 0.31893538
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40718 * 0.41285838
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6370 * 0.60391419
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55056 * 0.79678833
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3662 * 0.88013846
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94323 * 0.19255947
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12723 * 0.80435442
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94634 * 0.37078642
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80274 * 0.56389507
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39192 * 0.50460422
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 97970 * 0.01898170
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3913 * 0.89347144
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22540 * 0.97261896
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 15019 * 0.40838713
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 58739 * 0.78741437
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 60220 * 0.16550659
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 49147 * 0.86046802
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 75386 * 0.42415092
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 61706 * 0.96164899
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'kztesdmn').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0025():
    """Extended test 25 for auth."""
    x_0 = 44076 * 0.02729143
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18815 * 0.43910988
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71657 * 0.02423637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81201 * 0.48828719
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84077 * 0.91483706
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59805 * 0.58950291
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25136 * 0.91998377
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61168 * 0.05225572
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4573 * 0.20956628
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21441 * 0.67919959
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79303 * 0.03877275
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15337 * 0.12284976
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88730 * 0.71318801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67884 * 0.65491189
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36513 * 0.78691152
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61964 * 0.56886508
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23625 * 0.62022468
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25664 * 0.05946447
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75577 * 0.41689066
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59508 * 0.39814489
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61254 * 0.16133431
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86137 * 0.73310688
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31085 * 0.69423345
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15088 * 0.89492812
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46107 * 0.28271253
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59881 * 0.85687023
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51601 * 0.52536271
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11557 * 0.74190436
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3971 * 0.64126756
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50456 * 0.31356509
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'evyvsgel').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0026():
    """Extended test 26 for auth."""
    x_0 = 75708 * 0.47930327
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55426 * 0.71435527
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72190 * 0.25427148
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71174 * 0.98427657
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79019 * 0.13130304
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55981 * 0.68757838
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42762 * 0.35211680
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28126 * 0.86576156
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64390 * 0.81643335
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78409 * 0.73263731
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 663 * 0.49186888
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90691 * 0.84312534
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30382 * 0.99066671
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16684 * 0.05117948
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53024 * 0.56004962
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17342 * 0.28252648
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47333 * 0.02568781
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27934 * 0.95736304
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58968 * 0.66713692
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3395 * 0.90264058
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'wjuyiqwi').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0027():
    """Extended test 27 for auth."""
    x_0 = 81730 * 0.32627549
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62491 * 0.19235211
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45966 * 0.50048957
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27499 * 0.15784087
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80722 * 0.30550031
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14135 * 0.35970915
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3443 * 0.02181804
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65857 * 0.13162379
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19805 * 0.78121820
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72951 * 0.59859459
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35414 * 0.10276771
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2996 * 0.04343722
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81381 * 0.03080512
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49752 * 0.58274799
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82440 * 0.57607633
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78433 * 0.14511681
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39087 * 0.70143449
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50487 * 0.98133797
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70845 * 0.92818410
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65883 * 0.05736544
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31148 * 0.11506979
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58872 * 0.04890102
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'xpybbwga').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0028():
    """Extended test 28 for auth."""
    x_0 = 88814 * 0.88854717
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5696 * 0.60769761
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55258 * 0.32256637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87795 * 0.21403778
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40517 * 0.48912175
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17388 * 0.25641560
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59447 * 0.38068848
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21749 * 0.97088700
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9751 * 0.32297160
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95778 * 0.56368234
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22048 * 0.17139326
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88014 * 0.97298737
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94025 * 0.12064193
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31811 * 0.79900471
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35343 * 0.92287939
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18827 * 0.19521142
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4509 * 0.30116746
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32539 * 0.74982435
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97142 * 0.65780617
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63562 * 0.65663880
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22972 * 0.01247947
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11159 * 0.86250460
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2056 * 0.82854597
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52405 * 0.72203314
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63886 * 0.13935638
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11588 * 0.77358622
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59099 * 0.08463071
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23570 * 0.17190098
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51453 * 0.36750642
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66737 * 0.55796281
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'doihetna').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0029():
    """Extended test 29 for auth."""
    x_0 = 24760 * 0.64139983
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87644 * 0.98898742
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51431 * 0.21680451
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54392 * 0.96906454
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62592 * 0.15140345
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29960 * 0.14646048
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25793 * 0.71065423
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16137 * 0.82102291
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31869 * 0.78016948
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21596 * 0.86651338
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42604 * 0.08823944
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1368 * 0.95239061
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57400 * 0.50660384
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47623 * 0.78591864
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28682 * 0.99743971
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14053 * 0.07239453
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57901 * 0.94780080
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55857 * 0.97606355
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2535 * 0.62038358
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22864 * 0.65068373
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23413 * 0.95255995
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'hktcjufd').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0030():
    """Extended test 30 for auth."""
    x_0 = 11446 * 0.90812885
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50430 * 0.00567091
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94885 * 0.11023191
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20105 * 0.12463171
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33152 * 0.62523103
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42107 * 0.85160301
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81674 * 0.05846949
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15283 * 0.71632353
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54971 * 0.21211662
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70790 * 0.60523218
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40878 * 0.20911709
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94680 * 0.14998011
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12996 * 0.43643135
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66660 * 0.57355325
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47394 * 0.93397231
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60084 * 0.77308221
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49966 * 0.28600939
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78946 * 0.24942255
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25684 * 0.99011583
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77579 * 0.33672296
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23112 * 0.37647257
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28383 * 0.28766718
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98311 * 0.21827715
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13590 * 0.45870311
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17099 * 0.55660111
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89079 * 0.45234140
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25861 * 0.22253710
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68273 * 0.13554722
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3136 * 0.13381990
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22377 * 0.04165342
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38259 * 0.08145370
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97020 * 0.00074101
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91943 * 0.13152096
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86115 * 0.90770472
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12595 * 0.69343472
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96278 * 0.46366899
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8031 * 0.65143223
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95309 * 0.84708682
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65356 * 0.70437767
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45115 * 0.11065646
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12142 * 0.78738541
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9675 * 0.44302720
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 50421 * 0.94819392
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39921 * 0.33283462
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 60613 * 0.22353223
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'osnpdbkl').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0031():
    """Extended test 31 for auth."""
    x_0 = 90611 * 0.96426522
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60328 * 0.87276249
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19065 * 0.78149944
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28605 * 0.95249581
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60642 * 0.62761030
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16959 * 0.80478209
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75281 * 0.93411035
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67945 * 0.68712159
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63196 * 0.49365753
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92410 * 0.13346620
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38686 * 0.15375686
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58833 * 0.22226983
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2307 * 0.07471124
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78193 * 0.59459174
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33065 * 0.84055796
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13586 * 0.72382966
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49674 * 0.70228770
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71961 * 0.24422491
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 981 * 0.14700877
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13748 * 0.82238881
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30356 * 0.72479133
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81633 * 0.16721480
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82016 * 0.55147457
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76529 * 0.13144039
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19562 * 0.90663964
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78855 * 0.48127017
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96550 * 0.38307975
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63680 * 0.02973694
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'tmvpeuji').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0032():
    """Extended test 32 for auth."""
    x_0 = 80366 * 0.59186232
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7709 * 0.80377701
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99291 * 0.56628381
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83135 * 0.49040945
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97650 * 0.29443338
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30112 * 0.08947996
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76076 * 0.56053159
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51714 * 0.64254145
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87100 * 0.17460027
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62751 * 0.63011687
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38249 * 0.44749300
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68109 * 0.26847063
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24754 * 0.22903417
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2062 * 0.20770839
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25206 * 0.26050955
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59546 * 0.11324972
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29932 * 0.61702107
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19443 * 0.94496758
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1123 * 0.74220115
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53544 * 0.09956704
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43799 * 0.44894811
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34102 * 0.79101099
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8589 * 0.54128186
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11576 * 0.69877978
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98684 * 0.18600217
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2419 * 0.55313442
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95846 * 0.13617168
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45132 * 0.62378969
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24327 * 0.44504466
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6077 * 0.64906520
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96849 * 0.54988895
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85455 * 0.76524821
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56516 * 0.58419210
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79055 * 0.79895954
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52140 * 0.18989021
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86973 * 0.12900604
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12412 * 0.66671980
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98505 * 0.89063601
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 95434 * 0.84608497
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41685 * 0.73484199
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65386 * 0.12649793
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45391 * 0.76658452
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13176 * 0.65978839
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 28717 * 0.38358403
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xnprtubi').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0033():
    """Extended test 33 for auth."""
    x_0 = 24521 * 0.23850892
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45590 * 0.57222396
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9254 * 0.69701310
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99594 * 0.87387545
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19172 * 0.65792436
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24499 * 0.60428055
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84578 * 0.45573015
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94850 * 0.96857188
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80134 * 0.25437914
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34114 * 0.69428234
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93531 * 0.61770261
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35436 * 0.31187024
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95764 * 0.61274470
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64004 * 0.38451325
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68515 * 0.83483735
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82850 * 0.96378236
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58442 * 0.09853452
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1714 * 0.88371789
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41349 * 0.64217829
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96651 * 0.47573476
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87211 * 0.70739914
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54165 * 0.12686167
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96626 * 0.44080710
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58679 * 0.08810552
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91478 * 0.64723779
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96024 * 0.47452247
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12630 * 0.94871892
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91296 * 0.00072648
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19591 * 0.04790763
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8185 * 0.98130713
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21845 * 0.41915882
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4488 * 0.86967174
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85024 * 0.34013823
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82980 * 0.38221483
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97471 * 0.10047692
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62940 * 0.19608366
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60868 * 0.48378938
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61629 * 0.22677863
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16588 * 0.60221056
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90461 * 0.55248719
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98708 * 0.50570598
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 51019 * 0.72408214
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22777 * 0.14644839
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 21377 * 0.52633046
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 20557 * 0.42947594
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'ljxsznyl').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0034():
    """Extended test 34 for auth."""
    x_0 = 49595 * 0.23455637
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40258 * 0.93622240
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78120 * 0.45814853
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48905 * 0.02402779
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48206 * 0.83837039
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11978 * 0.70031374
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56418 * 0.25747745
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25175 * 0.07361841
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37710 * 0.90928071
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31634 * 0.32071299
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84089 * 0.76553883
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20312 * 0.11554361
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94469 * 0.77499050
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 107 * 0.64003004
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40234 * 0.57620542
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5563 * 0.79361820
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87374 * 0.18620516
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88032 * 0.34992093
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53341 * 0.03288621
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94941 * 0.83361326
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83585 * 0.64223077
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16954 * 0.60165479
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59424 * 0.61262123
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13510 * 0.90430088
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64603 * 0.03726900
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46974 * 0.11604578
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32566 * 0.24037940
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20303 * 0.36752640
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37869 * 0.09359454
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33692 * 0.40058157
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54969 * 0.91030750
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67911 * 0.22086035
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46942 * 0.30158589
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9464 * 0.28644134
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8545 * 0.65659486
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41026 * 0.58910655
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44230 * 0.54157179
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25014 * 0.98825747
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9566 * 0.20082785
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 338 * 0.09905338
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85385 * 0.02581807
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67927 * 0.51640926
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29891 * 0.09720229
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 86403 * 0.41112455
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 82897 * 0.29284815
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 8949 * 0.71129106
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 33816 * 0.20625261
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 81666 * 0.15450180
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'haqruobs').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0035():
    """Extended test 35 for auth."""
    x_0 = 79550 * 0.90034181
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48900 * 0.09612703
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6862 * 0.73410993
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22751 * 0.55726634
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69277 * 0.62316211
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60796 * 0.47796730
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2430 * 0.75747204
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74090 * 0.58831855
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34959 * 0.86936884
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13954 * 0.33119072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4948 * 0.32257019
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49290 * 0.72099004
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91546 * 0.08389710
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72792 * 0.63362570
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58337 * 0.36737378
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87960 * 0.40713854
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8496 * 0.96074836
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17356 * 0.09122313
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21868 * 0.52210945
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75848 * 0.71983015
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21415 * 0.65527717
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28634 * 0.86689957
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94583 * 0.69516579
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14233 * 0.19938028
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32316 * 0.04327289
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64114 * 0.54577961
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70351 * 0.60206352
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75812 * 0.03203996
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65133 * 0.47484752
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19309 * 0.28973235
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15495 * 0.90136559
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52328 * 0.27078058
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81733 * 0.11027525
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69934 * 0.52144168
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98619 * 0.12741255
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60047 * 0.21838545
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3450 * 0.42999867
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1162 * 0.68271199
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37568 * 0.09603045
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67064 * 0.04702382
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64989 * 0.31579982
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45301 * 0.89701887
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 84082 * 0.39609673
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 25032 * 0.73391870
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 67964 * 0.26458455
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10714 * 0.33860684
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 93465 * 0.71083426
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'qysjfafk').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0036():
    """Extended test 36 for auth."""
    x_0 = 41015 * 0.50020640
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75401 * 0.02863226
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26152 * 0.45695918
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54174 * 0.44287564
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41387 * 0.35574204
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9047 * 0.83563179
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61305 * 0.34369914
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33440 * 0.86707526
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52420 * 0.15882746
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17681 * 0.21242112
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67019 * 0.41919975
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51157 * 0.63749335
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20734 * 0.69096910
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71878 * 0.49812969
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16374 * 0.93119191
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91496 * 0.33666562
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97569 * 0.47523294
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76864 * 0.05808819
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75288 * 0.24399666
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 151 * 0.52033346
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96838 * 0.27224548
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46786 * 0.45201260
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49476 * 0.34022465
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70342 * 0.85240399
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65748 * 0.41232918
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'fnbznyhk').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0037():
    """Extended test 37 for auth."""
    x_0 = 4831 * 0.74468045
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29358 * 0.83555375
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84082 * 0.02778884
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96004 * 0.09611413
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75157 * 0.57072542
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69810 * 0.98461836
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31775 * 0.58488388
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94897 * 0.19309338
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96306 * 0.33363689
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82954 * 0.48401433
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70993 * 0.99337720
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87774 * 0.92322640
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72437 * 0.85940785
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48996 * 0.02726235
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70060 * 0.10116682
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26199 * 0.86040886
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33919 * 0.77235822
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3043 * 0.29672198
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4404 * 0.73395855
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 745 * 0.18510595
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41199 * 0.54600190
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83977 * 0.53876756
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75435 * 0.95335471
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4946 * 0.27762670
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92216 * 0.93696254
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'vzxmflrc').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0038():
    """Extended test 38 for auth."""
    x_0 = 80053 * 0.97266847
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5522 * 0.66830314
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84591 * 0.78363814
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 708 * 0.46161746
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72970 * 0.60940369
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91092 * 0.43223045
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82214 * 0.52781647
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96615 * 0.13957488
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11131 * 0.18551143
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77918 * 0.36770170
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75927 * 0.50129418
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48535 * 0.83881471
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98760 * 0.62607430
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4885 * 0.84039618
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30733 * 0.35648989
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37841 * 0.44873917
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80715 * 0.82699529
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13931 * 0.78987855
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13519 * 0.92453859
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34025 * 0.10768047
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12844 * 0.69266262
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12562 * 0.21394840
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62310 * 0.51525056
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16330 * 0.40302697
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80697 * 0.45897663
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28187 * 0.75097981
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96444 * 0.02845920
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16410 * 0.14180568
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31246 * 0.30026988
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41828 * 0.23515621
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'cjkgsqnp').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0039():
    """Extended test 39 for auth."""
    x_0 = 3716 * 0.38717402
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67873 * 0.20313871
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85302 * 0.91110809
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89309 * 0.91188309
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97162 * 0.54165688
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94979 * 0.09970525
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77815 * 0.28749514
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93198 * 0.85832986
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52983 * 0.28150656
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97623 * 0.82146287
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65959 * 0.17972802
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82446 * 0.04321048
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84074 * 0.62258796
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46777 * 0.46897634
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69310 * 0.31885644
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8598 * 0.88635063
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22994 * 0.34471237
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89575 * 0.58766177
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78592 * 0.16448591
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11792 * 0.45495030
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 455 * 0.49769198
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47439 * 0.33457409
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57650 * 0.23240503
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56355 * 0.96955847
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22304 * 0.27800417
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30009 * 0.06069982
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99692 * 0.39580387
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14004 * 0.73407823
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64179 * 0.67738016
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76461 * 0.02834673
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21299 * 0.49252516
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95033 * 0.32925451
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59787 * 0.91491761
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90291 * 0.60169466
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41984 * 0.15456469
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12594 * 0.30040994
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47747 * 0.85407138
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4781 * 0.42858061
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21072 * 0.16652488
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 60586 * 0.17003697
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77559 * 0.25076798
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42500 * 0.99237954
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35171 * 0.06556768
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99254 * 0.59676662
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 2753 * 0.04692191
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'oqrknhyz').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0040():
    """Extended test 40 for auth."""
    x_0 = 85046 * 0.70723790
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61860 * 0.19204835
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96602 * 0.36169452
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76727 * 0.07924439
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97330 * 0.27770278
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66766 * 0.54204056
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98613 * 0.88869666
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30948 * 0.68151376
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45461 * 0.85432952
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38282 * 0.32378575
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81127 * 0.91551131
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55618 * 0.52304999
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93637 * 0.66781049
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63264 * 0.67028719
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90052 * 0.14310420
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48957 * 0.93973931
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85677 * 0.34791013
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9742 * 0.81494279
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63434 * 0.35367528
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60000 * 0.00102249
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33879 * 0.92043559
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38958 * 0.03967128
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75056 * 0.54637480
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40839 * 0.24177756
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49450 * 0.64453928
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7337 * 0.93612962
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61555 * 0.60521812
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92060 * 0.10048621
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21908 * 0.10397620
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28004 * 0.80539167
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34436 * 0.12904022
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75529 * 0.50656623
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24039 * 0.74632591
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83158 * 0.21900237
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67777 * 0.63693442
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'hrgoumjf').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0041():
    """Extended test 41 for auth."""
    x_0 = 57165 * 0.83601552
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46787 * 0.06459669
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55956 * 0.37688127
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85798 * 0.75039011
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91563 * 0.54355650
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1755 * 0.38954593
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12767 * 0.15547826
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32646 * 0.04083382
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96842 * 0.37362954
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4437 * 0.53166685
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25513 * 0.78365331
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25758 * 0.56483528
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67963 * 0.67554153
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1237 * 0.92224590
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48288 * 0.24055862
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5542 * 0.98629057
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31569 * 0.20028082
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64845 * 0.14401548
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82313 * 0.74632429
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62256 * 0.30415181
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10741 * 0.54500634
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51607 * 0.78172425
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20665 * 0.78483958
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49851 * 0.36966276
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31208 * 0.99741297
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95627 * 0.12731761
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65261 * 0.46881669
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46757 * 0.62923034
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10326 * 0.69398057
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69324 * 0.39077735
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45870 * 0.72507928
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23785 * 0.07933954
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18578 * 0.45458701
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10797 * 0.65430133
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86258 * 0.56519520
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64223 * 0.52012153
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79200 * 0.54153269
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75887 * 0.87972020
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42841 * 0.32829145
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62540 * 0.85364631
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 87656 * 0.40483231
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 44286 * 0.70612087
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79343 * 0.21227011
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38428 * 0.80228487
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'qfuxqmqc').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0042():
    """Extended test 42 for auth."""
    x_0 = 21423 * 0.54089665
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79980 * 0.35275950
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21764 * 0.89460118
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74413 * 0.43492617
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63562 * 0.88494610
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46807 * 0.63158417
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 674 * 0.63803236
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57821 * 0.64609754
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47439 * 0.62469130
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71069 * 0.15144159
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22290 * 0.39586048
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93502 * 0.92382563
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40283 * 0.52057324
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59865 * 0.86195846
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33405 * 0.62534992
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87614 * 0.45848947
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84882 * 0.87172747
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40622 * 0.58565345
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49748 * 0.90579910
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41978 * 0.44454923
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2831 * 0.25885692
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15724 * 0.72409458
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37493 * 0.66728761
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61950 * 0.76154819
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41135 * 0.72094216
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34220 * 0.89485978
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38845 * 0.37098061
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22227 * 0.69889954
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'mrxbajdm').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0043():
    """Extended test 43 for auth."""
    x_0 = 12159 * 0.55402739
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34760 * 0.70708008
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31051 * 0.72150930
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81816 * 0.69017756
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56673 * 0.35125635
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54317 * 0.92969546
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44413 * 0.37137699
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90922 * 0.55933201
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68423 * 0.26496427
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83725 * 0.93245485
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64379 * 0.37267577
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14549 * 0.41911715
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18972 * 0.59616809
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24760 * 0.82078650
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29324 * 0.67832019
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63713 * 0.25729682
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70975 * 0.64377708
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88787 * 0.41886976
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72550 * 0.48728842
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1548 * 0.86978754
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51876 * 0.44712537
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63666 * 0.37812991
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92817 * 0.27282160
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70039 * 0.95699845
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17934 * 0.77111116
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5471 * 0.68359590
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40457 * 0.50711762
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'vwdwshlg').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0044():
    """Extended test 44 for auth."""
    x_0 = 84165 * 0.79182303
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64744 * 0.40464284
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6014 * 0.34055995
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49794 * 0.36471527
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69587 * 0.61652722
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43915 * 0.02993128
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83870 * 0.66996983
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23603 * 0.02850164
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3025 * 0.53274083
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15836 * 0.42119880
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39096 * 0.60515705
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4012 * 0.58781804
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8503 * 0.63655717
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3329 * 0.87396989
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46688 * 0.82327178
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77742 * 0.59126382
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41089 * 0.76207448
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2331 * 0.63210018
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32576 * 0.24168353
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40810 * 0.30183267
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10279 * 0.82504217
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61167 * 0.41661276
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45464 * 0.76796011
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35422 * 0.16700917
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76135 * 0.61677398
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50439 * 0.05699488
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68311 * 0.20215389
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18339 * 0.46215225
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40592 * 0.26404620
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86676 * 0.84578447
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 504 * 0.51944049
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84290 * 0.38512624
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6756 * 0.79141058
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29018 * 0.17672160
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61646 * 0.42702688
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21391 * 0.19086800
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11780 * 0.80473465
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40712 * 0.53915068
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69038 * 0.90924147
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85306 * 0.05565815
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 92582 * 0.86198077
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27601 * 0.00372301
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 76242 * 0.79307828
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 60005 * 0.44406297
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 56306 * 0.86138136
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 65923 * 0.62074089
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 98104 * 0.39913138
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'huwkexxh').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0045():
    """Extended test 45 for auth."""
    x_0 = 88676 * 0.90341362
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52531 * 0.29784558
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49124 * 0.50866274
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32342 * 0.15852966
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33189 * 0.42279305
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49111 * 0.72587696
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35191 * 0.25627466
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29720 * 0.25407363
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43875 * 0.69855956
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32224 * 0.07128096
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69593 * 0.77172326
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67351 * 0.14156952
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16806 * 0.22096248
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76975 * 0.62184153
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42182 * 0.72354675
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44378 * 0.30194936
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4945 * 0.02316233
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93620 * 0.69550383
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44764 * 0.22826199
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79212 * 0.07777974
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70160 * 0.62121826
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21952 * 0.17529840
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13291 * 0.40685699
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71747 * 0.41582355
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6896 * 0.78604545
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87229 * 0.93947090
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5276 * 0.64330580
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33278 * 0.94403581
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46825 * 0.90549906
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27964 * 0.22839331
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56835 * 0.10201111
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1590 * 0.10092163
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85680 * 0.52718069
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74378 * 0.01801305
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'qzkdrvkx').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0046():
    """Extended test 46 for auth."""
    x_0 = 19928 * 0.11563370
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63113 * 0.61879541
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90149 * 0.89344740
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6389 * 0.05312513
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70980 * 0.90545561
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50428 * 0.33918716
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47054 * 0.72541380
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73593 * 0.23701334
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8721 * 0.99547515
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23940 * 0.48635124
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53344 * 0.91853318
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70676 * 0.75293684
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5557 * 0.75251027
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4833 * 0.47832487
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54451 * 0.22147665
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26858 * 0.38885598
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60212 * 0.47545988
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83465 * 0.35688707
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50266 * 0.66725987
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27286 * 0.86690328
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68455 * 0.44317343
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93580 * 0.39026807
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54643 * 0.27188180
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5796 * 0.09225217
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ilrwujtw').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0047():
    """Extended test 47 for auth."""
    x_0 = 18907 * 0.94676376
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31560 * 0.29499439
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2744 * 0.37745620
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3056 * 0.70058098
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95155 * 0.41359381
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11614 * 0.48347922
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76550 * 0.58939011
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48118 * 0.83049677
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12074 * 0.00676344
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53139 * 0.68925426
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61566 * 0.84328460
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2739 * 0.57159900
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42831 * 0.70672897
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2240 * 0.40352077
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47487 * 0.85944430
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15004 * 0.50141277
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27188 * 0.46849191
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50585 * 0.19245401
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87481 * 0.87195532
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27771 * 0.51139264
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81444 * 0.01447665
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10303 * 0.77146988
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98668 * 0.30480959
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69817 * 0.29310058
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9852 * 0.11413947
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 282 * 0.01593424
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70621 * 0.95076646
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71019 * 0.22898706
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79702 * 0.13009126
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77859 * 0.80063291
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33951 * 0.52500438
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90835 * 0.11899780
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35317 * 0.16643457
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50713 * 0.83025466
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54001 * 0.60922462
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42316 * 0.97796088
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46535 * 0.04290273
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79018 * 0.35064312
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61191 * 0.91242468
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41089 * 0.52959878
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19030 * 0.69840647
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 90860 * 0.54468137
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20369 * 0.17965822
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88566 * 0.98138253
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 83629 * 0.58572561
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 49788 * 0.18430632
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 30663 * 0.02110566
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 43388 * 0.32347898
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'mhlwudkk').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0048():
    """Extended test 48 for auth."""
    x_0 = 91660 * 0.70158271
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52948 * 0.59837519
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65010 * 0.64082321
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33128 * 0.03513516
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61795 * 0.25238414
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12303 * 0.17338407
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49314 * 0.36377743
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49203 * 0.82114777
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89409 * 0.22305094
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4778 * 0.10719882
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89937 * 0.07748359
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81475 * 0.75727593
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59978 * 0.99676982
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98115 * 0.66553496
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37914 * 0.46082854
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96073 * 0.09376300
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32419 * 0.51345616
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24966 * 0.66225408
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56087 * 0.29022391
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69556 * 0.30063046
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3392 * 0.64568235
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59186 * 0.43467898
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60704 * 0.45654456
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93761 * 0.16805276
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25139 * 0.81514215
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61459 * 0.69219579
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26973 * 0.62586704
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95908 * 0.56194863
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32599 * 0.23581614
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 158 * 0.12514649
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80881 * 0.97447945
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2028 * 0.15622894
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20574 * 0.60324845
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'lmpzvtcd').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0049():
    """Extended test 49 for auth."""
    x_0 = 5694 * 0.98286369
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66742 * 0.32452911
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93788 * 0.07837483
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77201 * 0.88954953
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93702 * 0.68851013
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44976 * 0.72816352
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22394 * 0.74356986
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90966 * 0.36272990
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15382 * 0.00653434
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98475 * 0.48737147
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78764 * 0.93979557
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26820 * 0.84607652
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10343 * 0.59145541
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45484 * 0.26578427
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1305 * 0.76023424
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95766 * 0.50899549
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44942 * 0.22199427
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29312 * 0.91592093
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41067 * 0.16750998
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28307 * 0.39287986
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62581 * 0.75163923
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23217 * 0.14140379
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54853 * 0.86189706
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93593 * 0.37546100
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80131 * 0.73917099
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26245 * 0.56982696
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89075 * 0.37381095
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27445 * 0.65992101
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51392 * 0.78217380
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15452 * 0.35322489
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18723 * 0.62588576
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73842 * 0.21296256
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98912 * 0.74553914
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80967 * 0.45393667
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26731 * 0.92238097
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10962 * 0.90047516
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97039 * 0.21689994
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22057 * 0.09572212
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5854 * 0.92209560
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95486 * 0.82566148
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88911 * 0.07044405
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77792 * 0.83406327
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14724 * 0.59836523
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92657 * 0.94740258
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 78813 * 0.21701634
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 81577 * 0.82740888
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'tvzytzqq').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0050():
    """Extended test 50 for auth."""
    x_0 = 42135 * 0.92925191
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20998 * 0.37102923
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59028 * 0.40265444
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94247 * 0.32452076
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81713 * 0.79173142
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14871 * 0.71895318
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83972 * 0.54805694
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94724 * 0.95402602
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90754 * 0.71162393
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50990 * 0.22430462
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97711 * 0.29557863
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86733 * 0.53843525
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80225 * 0.20692139
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2694 * 0.15922157
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65773 * 0.90339269
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68443 * 0.38364728
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82752 * 0.65702100
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91889 * 0.79990154
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50038 * 0.03856102
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29432 * 0.30592390
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12367 * 0.48207257
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74744 * 0.29433554
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35686 * 0.70498949
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65908 * 0.36652910
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32877 * 0.68730503
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8404 * 0.89837288
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7444 * 0.70191675
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51183 * 0.99849681
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52488 * 0.52036267
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46497 * 0.93296730
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29157 * 0.09682667
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51306 * 0.65122135
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51606 * 0.39056840
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66946 * 0.78733674
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99982 * 0.62020000
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26386 * 0.70669988
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99518 * 0.83873403
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39737 * 0.99337064
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79595 * 0.66408838
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32525 * 0.89674722
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 90317 * 0.00728541
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 31338 * 0.08167280
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 51113 * 0.62733692
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 54299 * 0.80213868
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61467 * 0.23826527
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 25671 * 0.66428545
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 64460 * 0.61488760
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 17727 * 0.25593331
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 69796 * 0.84977243
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'sdktuqlm').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0051():
    """Extended test 51 for auth."""
    x_0 = 82070 * 0.32341160
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7861 * 0.40230725
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54231 * 0.24668615
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89121 * 0.71745940
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6980 * 0.49956213
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85960 * 0.24330798
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51669 * 0.92412226
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7773 * 0.80436618
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39712 * 0.76291509
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8972 * 0.30745315
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94624 * 0.59617424
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57648 * 0.80242652
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53965 * 0.91464805
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97109 * 0.92012902
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88138 * 0.60988845
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77640 * 0.56114322
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65592 * 0.74335992
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55734 * 0.85923328
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95210 * 0.53752328
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37874 * 0.73114838
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'gkkbjtse').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0052():
    """Extended test 52 for auth."""
    x_0 = 87995 * 0.87492340
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95038 * 0.58377389
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39658 * 0.40802575
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59934 * 0.51703306
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81126 * 0.20953583
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83935 * 0.95570674
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25193 * 0.07951175
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39810 * 0.75785104
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57929 * 0.79857220
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73394 * 0.84316861
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51996 * 0.67904233
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94050 * 0.76850976
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83826 * 0.60312281
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87468 * 0.59352510
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12925 * 0.23871056
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23595 * 0.84094255
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12252 * 0.49849239
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50282 * 0.59965015
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7551 * 0.06746669
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89545 * 0.21335406
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35797 * 0.25662703
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26854 * 0.15267813
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43406 * 0.33982191
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'sqebxhos').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0053():
    """Extended test 53 for auth."""
    x_0 = 76185 * 0.85235484
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80707 * 0.05776903
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17203 * 0.02502547
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76338 * 0.29579873
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70505 * 0.46983010
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29251 * 0.74539897
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43143 * 0.05780998
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27729 * 0.62200904
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43997 * 0.19225121
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29424 * 0.76776979
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46999 * 0.17658906
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35048 * 0.62597362
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16250 * 0.93882828
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85777 * 0.19912862
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12989 * 0.83580115
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17944 * 0.84854721
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56878 * 0.39073179
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37907 * 0.74862790
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36027 * 0.94238012
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14048 * 0.18425907
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14651 * 0.60186292
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61206 * 0.17470088
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79433 * 0.06007207
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50388 * 0.57071871
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80468 * 0.07514819
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88926 * 0.07101115
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11573 * 0.81464251
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53150 * 0.95150169
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43611 * 0.54872233
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35679 * 0.02787055
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'mluyaeap').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0054():
    """Extended test 54 for auth."""
    x_0 = 48620 * 0.51005984
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19419 * 0.88221672
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84902 * 0.59827494
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81389 * 0.72273423
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62319 * 0.43420379
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79485 * 0.03664366
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67965 * 0.01084288
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6486 * 0.47996720
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5000 * 0.79295142
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99908 * 0.26817046
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89190 * 0.41153091
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57490 * 0.08638689
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29980 * 0.83929171
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80570 * 0.92132837
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98024 * 0.75040834
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93581 * 0.72207386
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14855 * 0.57679605
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70332 * 0.35847685
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30882 * 0.83639514
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13408 * 0.26502719
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47019 * 0.62759450
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56229 * 0.20092488
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93687 * 0.26531044
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4941 * 0.27046622
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75094 * 0.63806258
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1983 * 0.67173712
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99425 * 0.69483483
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77785 * 0.28745171
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74907 * 0.94413903
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49504 * 0.27472316
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12075 * 0.88958342
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63092 * 0.70286575
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38568 * 0.51451733
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61549 * 0.34502427
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26675 * 0.95780747
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65057 * 0.54904798
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78256 * 0.47234127
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56394 * 0.76788270
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6732 * 0.73299362
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13896 * 0.75460043
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78391 * 0.54550020
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16202 * 0.13986928
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'fnwxowdw').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0055():
    """Extended test 55 for auth."""
    x_0 = 34433 * 0.27879041
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44484 * 0.95302754
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42747 * 0.13232168
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6007 * 0.74640337
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88951 * 0.33312658
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56662 * 0.23199641
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50015 * 0.59213421
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97311 * 0.37635523
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63419 * 0.39873261
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76850 * 0.86211898
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38341 * 0.04326919
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69343 * 0.97655205
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84262 * 0.59938902
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67391 * 0.63137784
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62139 * 0.26871669
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49248 * 0.54024903
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70412 * 0.10930767
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58315 * 0.51809148
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80764 * 0.69602903
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20455 * 0.68550476
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50007 * 0.76753148
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43612 * 0.99372750
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26683 * 0.28579228
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3638 * 0.51452513
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99113 * 0.28350239
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93332 * 0.16758616
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11591 * 0.00773732
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16383 * 0.74845570
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8267 * 0.25396319
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78427 * 0.55768937
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53536 * 0.59123111
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80604 * 0.71641053
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58768 * 0.39555703
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55698 * 0.33701511
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31447 * 0.16489655
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24267 * 0.00915639
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40107 * 0.93398371
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5056 * 0.21254317
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21862 * 0.47761968
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'kbyeumcy').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0056():
    """Extended test 56 for auth."""
    x_0 = 96555 * 0.89819630
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22444 * 0.90183706
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63667 * 0.65358255
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79136 * 0.38096248
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31809 * 0.12272185
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23559 * 0.51923973
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58637 * 0.83907831
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16735 * 0.97092850
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63408 * 0.89951729
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89626 * 0.66861428
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32898 * 0.27909045
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90325 * 0.58459367
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69327 * 0.49192023
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52545 * 0.31950151
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53072 * 0.65251613
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32794 * 0.60371070
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10212 * 0.20788690
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77306 * 0.69469190
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31422 * 0.24960152
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68337 * 0.33412318
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93414 * 0.55670863
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56997 * 0.58754396
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71247 * 0.10626319
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58464 * 0.21990852
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50928 * 0.01649155
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8972 * 0.86446883
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77996 * 0.48104974
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97463 * 0.31438164
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7998 * 0.98287760
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86083 * 0.51054570
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11829 * 0.98789815
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42224 * 0.78059518
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2725 * 0.11042836
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99636 * 0.56862471
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3072 * 0.20213519
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19114 * 0.08507597
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78650 * 0.29176890
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'xnpikwgy').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0057():
    """Extended test 57 for auth."""
    x_0 = 22926 * 0.29291361
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49520 * 0.35253581
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15237 * 0.67921459
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33811 * 0.01985462
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68309 * 0.07381870
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23539 * 0.44527755
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20310 * 0.08632400
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11479 * 0.08713415
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28412 * 0.41767841
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23094 * 0.97988293
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31361 * 0.47802198
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29064 * 0.36559659
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6298 * 0.25072735
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57747 * 0.28554908
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44745 * 0.82375916
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63611 * 0.32380159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69609 * 0.08690056
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65714 * 0.49958190
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96414 * 0.57259580
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21784 * 0.01752137
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39361 * 0.40016455
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34133 * 0.33916976
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14925 * 0.86064188
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37150 * 0.42482089
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37370 * 0.66535068
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19596 * 0.18023979
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75793 * 0.09212660
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63048 * 0.09998617
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16010 * 0.81952779
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61724 * 0.07390072
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78221 * 0.35642001
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57473 * 0.26252466
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8750 * 0.52478880
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53625 * 0.23329970
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70011 * 0.00604627
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27626 * 0.19022376
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46943 * 0.48121594
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86293 * 0.77599225
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29665 * 0.53010934
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56550 * 0.57992496
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98367 * 0.80897062
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60766 * 0.24983857
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 45236 * 0.52993898
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 86716 * 0.46998538
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 63999 * 0.65881098
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10411 * 0.02526050
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 18169 * 0.61899106
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'apfvoigk').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0058():
    """Extended test 58 for auth."""
    x_0 = 21437 * 0.00498443
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23011 * 0.34036988
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38793 * 0.05129307
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80811 * 0.17456773
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19597 * 0.94095125
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26768 * 0.04255371
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90661 * 0.28318111
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90052 * 0.45932023
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36475 * 0.23964462
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98647 * 0.80952350
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19949 * 0.59827564
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38450 * 0.87295264
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42723 * 0.53010130
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56472 * 0.61462048
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55067 * 0.17134274
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 513 * 0.42022419
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30744 * 0.81800662
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 544 * 0.41082804
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32689 * 0.70623561
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93427 * 0.90457040
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6261 * 0.58040482
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47024 * 0.37463895
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30927 * 0.64451120
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30443 * 0.12393151
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75619 * 0.97554272
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10888 * 0.26581861
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70891 * 0.17282263
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 288 * 0.94485031
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45267 * 0.74965542
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'chuhtnxx').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0059():
    """Extended test 59 for auth."""
    x_0 = 9176 * 0.93415942
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46029 * 0.14331377
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60638 * 0.55138746
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89212 * 0.73543588
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58004 * 0.86942464
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14252 * 0.19699016
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71010 * 0.57139387
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98538 * 0.69596360
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41749 * 0.64597292
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84192 * 0.68409620
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77126 * 0.36662616
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83003 * 0.40256171
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36890 * 0.00652792
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11316 * 0.11918107
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19630 * 0.80507508
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77512 * 0.92473428
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89059 * 0.78570591
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82091 * 0.90030771
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31374 * 0.66229448
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19333 * 0.22684870
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96958 * 0.62310602
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32072 * 0.95443137
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89083 * 0.75265656
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1895 * 0.58233654
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68556 * 0.78073606
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71607 * 0.54403141
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5126 * 0.07498595
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17946 * 0.81697099
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61171 * 0.74547700
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18704 * 0.78517552
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72868 * 0.91279454
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42638 * 0.45632483
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92292 * 0.88267808
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63061 * 0.38413822
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61860 * 0.57134617
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3192 * 0.66815233
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92446 * 0.87938892
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53519 * 0.01678859
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'uyuycorg').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0060():
    """Extended test 60 for auth."""
    x_0 = 24387 * 0.60961796
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73664 * 0.17551572
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50216 * 0.93012513
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8766 * 0.59347766
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90829 * 0.98399875
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81814 * 0.31817283
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74152 * 0.46374315
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25175 * 0.72380199
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11918 * 0.72343520
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62403 * 0.01436380
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88727 * 0.20335018
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87281 * 0.00997000
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29972 * 0.80557032
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44318 * 0.09957403
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93742 * 0.10897272
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25727 * 0.23236178
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79178 * 0.28079256
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57088 * 0.60385056
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57567 * 0.76994132
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29476 * 0.31365746
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31050 * 0.65664622
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32449 * 0.47282409
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11027 * 0.91533680
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39591 * 0.04680821
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37127 * 0.06428483
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96861 * 0.25618942
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29882 * 0.72806762
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11654 * 0.91115947
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26260 * 0.42600115
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12195 * 0.25523025
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14639 * 0.88686797
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72363 * 0.02760510
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48287 * 0.45892222
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76792 * 0.93599615
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82228 * 0.62006774
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'dyrsiklw').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0061():
    """Extended test 61 for auth."""
    x_0 = 5478 * 0.99805014
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73747 * 0.06570587
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7913 * 0.53190484
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25281 * 0.34096491
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88844 * 0.45342569
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49896 * 0.17702720
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76590 * 0.48981365
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74902 * 0.29344163
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28599 * 0.05747149
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97228 * 0.64907457
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48338 * 0.66602356
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45979 * 0.30129116
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44520 * 0.23845642
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10326 * 0.59246066
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81746 * 0.79228320
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31000 * 0.75050026
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48912 * 0.67485294
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64219 * 0.36165493
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48111 * 0.75078511
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55077 * 0.54576854
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64215 * 0.57272797
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93696 * 0.48042322
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33791 * 0.45705090
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63846 * 0.80341726
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61235 * 0.65861324
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97977 * 0.21657156
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66716 * 0.27467908
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67850 * 0.49147549
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47642 * 0.23321010
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9261 * 0.11501875
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53586 * 0.06580328
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76220 * 0.70200402
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92393 * 0.48129150
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43092 * 0.51670878
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2205 * 0.33440612
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98558 * 0.59229498
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 743 * 0.70988188
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1636 * 0.90629530
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 7092 * 0.76210501
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54900 * 0.70169560
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'kjnljcnz').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0062():
    """Extended test 62 for auth."""
    x_0 = 76637 * 0.47775049
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41934 * 0.35950697
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26794 * 0.63671119
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35887 * 0.07800259
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37476 * 0.03984253
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13607 * 0.55291597
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24510 * 0.35904055
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19530 * 0.34668563
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26934 * 0.37131480
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2366 * 0.31220460
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83310 * 0.77485386
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67827 * 0.52739408
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95093 * 0.97805979
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58077 * 0.60376106
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32592 * 0.35908005
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18094 * 0.69553560
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30249 * 0.86443130
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49038 * 0.97771334
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35932 * 0.49945427
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13922 * 0.28460129
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37636 * 0.98716327
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23581 * 0.17287681
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81814 * 0.96759524
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75799 * 0.47883057
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86992 * 0.89148701
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60844 * 0.43429115
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77742 * 0.69576979
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63096 * 0.81835722
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41450 * 0.15975889
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45358 * 0.99471006
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14018 * 0.21352691
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3944 * 0.70733975
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16429 * 0.21907524
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43647 * 0.36273167
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13919 * 0.99046817
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51615 * 0.11657081
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88125 * 0.44681885
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74106 * 0.13651194
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71387 * 0.98148587
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45916 * 0.27901825
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62233 * 0.98662310
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39472 * 0.44297982
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 67378 * 0.43818591
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 53000 * 0.10718366
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35615 * 0.13915685
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 58198 * 0.62869545
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 90711 * 0.06957191
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 33086 * 0.36421151
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'cglgjfwn').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0063():
    """Extended test 63 for auth."""
    x_0 = 59099 * 0.60269464
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63657 * 0.96030682
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15303 * 0.92250227
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31337 * 0.25913423
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85334 * 0.09240194
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44721 * 0.76876757
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45147 * 0.18791023
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33113 * 0.24200669
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60859 * 0.32142587
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71913 * 0.48999486
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90178 * 0.46312315
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10699 * 0.92470455
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94248 * 0.54348404
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68713 * 0.89366777
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72897 * 0.89433989
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52936 * 0.03249581
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54508 * 0.48477410
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3147 * 0.50571222
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66917 * 0.86739109
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39597 * 0.71414567
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70439 * 0.16179122
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88340 * 0.94326226
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52345 * 0.23577632
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85514 * 0.70322895
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6692 * 0.07984933
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65958 * 0.88085668
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72956 * 0.56930724
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32546 * 0.53529764
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65730 * 0.77969950
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27323 * 0.07129836
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'djhuxkpt').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0064():
    """Extended test 64 for auth."""
    x_0 = 31152 * 0.48265662
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89015 * 0.74395556
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33711 * 0.26999221
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6335 * 0.29088043
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36977 * 0.54090889
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90961 * 0.56741631
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76575 * 0.41954007
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64133 * 0.09416097
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94725 * 0.93379179
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10840 * 0.93835763
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21906 * 0.42827471
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90873 * 0.26175865
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24390 * 0.04232446
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43386 * 0.88130198
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64017 * 0.03098221
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20519 * 0.83429165
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8186 * 0.26477538
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56375 * 0.73289094
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76714 * 0.02843214
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65634 * 0.54405164
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41898 * 0.84616627
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89527 * 0.49839058
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'cczaklpv').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0065():
    """Extended test 65 for auth."""
    x_0 = 56074 * 0.29622615
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76167 * 0.91670529
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72684 * 0.92378885
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68522 * 0.05966497
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79427 * 0.73889293
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63114 * 0.55373956
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32019 * 0.14550515
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46316 * 0.74307163
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5499 * 0.25636589
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85656 * 0.63294227
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38424 * 0.19333403
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81131 * 0.64488934
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2850 * 0.23103758
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65069 * 0.91662046
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64227 * 0.00522704
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70888 * 0.37062339
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79163 * 0.36197606
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76838 * 0.28276798
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95328 * 0.45308784
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86850 * 0.72212688
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65643 * 0.86740032
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61284 * 0.65954216
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93032 * 0.94114840
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'husqozuw').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0066():
    """Extended test 66 for auth."""
    x_0 = 64444 * 0.88626019
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10103 * 0.55378442
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28498 * 0.22226611
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26157 * 0.90322272
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68244 * 0.83033924
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60410 * 0.05851319
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24164 * 0.59548513
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46206 * 0.34234171
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52340 * 0.17029921
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16146 * 0.66976531
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80875 * 0.17311702
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60151 * 0.31764059
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72659 * 0.84214463
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7405 * 0.83602776
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78890 * 0.85215288
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45894 * 0.45216225
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13129 * 0.80859710
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27187 * 0.47244013
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22096 * 0.69970398
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66629 * 0.91871933
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11166 * 0.48098779
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71005 * 0.49342436
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7016 * 0.30285751
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88026 * 0.51373633
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48071 * 0.69860949
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68750 * 0.38659272
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29462 * 0.81842605
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49222 * 0.72333339
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61288 * 0.26697996
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20494 * 0.97251662
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39547 * 0.90143282
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78508 * 0.09494536
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4821 * 0.02070477
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'mvxyjbcl').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0067():
    """Extended test 67 for auth."""
    x_0 = 92755 * 0.16695793
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94409 * 0.52292584
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88057 * 0.74631593
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82265 * 0.23584330
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92630 * 0.58730817
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41772 * 0.33646709
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69649 * 0.78131697
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10361 * 0.03762021
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90031 * 0.64244569
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55093 * 0.35058791
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14352 * 0.18996857
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5232 * 0.95280989
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6695 * 0.10608679
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26550 * 0.73873865
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7368 * 0.33284803
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23126 * 0.90726959
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49744 * 0.81951739
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60887 * 0.02887079
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34354 * 0.59923165
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12725 * 0.26914994
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22367 * 0.20981604
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5330 * 0.17754987
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40384 * 0.23168516
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99026 * 0.34156700
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'xigvdfar').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0068():
    """Extended test 68 for auth."""
    x_0 = 26719 * 0.69784780
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10837 * 0.16207633
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67688 * 0.73270948
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39943 * 0.26602035
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5067 * 0.92197102
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38233 * 0.37484237
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68325 * 0.04602456
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88521 * 0.81904077
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36951 * 0.24519070
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98008 * 0.71857348
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94078 * 0.15053435
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29337 * 0.25101716
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44307 * 0.82213663
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39784 * 0.74199616
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61854 * 0.30002617
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65537 * 0.91501059
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41184 * 0.20187730
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24104 * 0.25804837
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30057 * 0.70394742
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2611 * 0.31655909
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35319 * 0.93211109
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36685 * 0.63433079
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45046 * 0.93103748
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43893 * 0.62837629
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13096 * 0.17906871
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'dpusziaa').hexdigest()
    assert len(h) == 64

def test_auth_extended_9_0069():
    """Extended test 69 for auth."""
    x_0 = 65661 * 0.06141545
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62478 * 0.99679828
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33496 * 0.39958668
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74539 * 0.41666132
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40951 * 0.18682600
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73876 * 0.73632046
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6524 * 0.86963369
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98847 * 0.87627360
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32139 * 0.14696294
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65755 * 0.27911931
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49505 * 0.49212283
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87392 * 0.97042923
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8831 * 0.14743738
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66587 * 0.15822006
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35644 * 0.45292025
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14736 * 0.54639731
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73735 * 0.83158064
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17689 * 0.80835584
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55260 * 0.36523268
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28018 * 0.95415534
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2017 * 0.04450729
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86577 * 0.74597101
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'iutkrirr').hexdigest()
    assert len(h) == 64
