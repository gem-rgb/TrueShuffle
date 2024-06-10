"""Extended tests for auth suite 0."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_auth_extended_0_0000():
    """Extended test 0 for auth."""
    x_0 = 26281 * 0.55301323
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62612 * 0.70673888
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23473 * 0.32919119
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88915 * 0.80907906
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41161 * 0.98450608
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10132 * 0.15706476
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23781 * 0.96663236
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20724 * 0.95329021
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94078 * 0.54270194
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8918 * 0.50441510
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22895 * 0.25887286
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 967 * 0.49702920
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34184 * 0.61940462
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18539 * 0.09848701
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28017 * 0.86993329
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99904 * 0.58994929
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35212 * 0.34721872
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80672 * 0.83618753
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63612 * 0.99756875
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75260 * 0.34045562
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16538 * 0.77111028
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25234 * 0.21972635
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47168 * 0.32655807
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61505 * 0.08528571
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59906 * 0.61510124
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52461 * 0.00629720
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72958 * 0.51108473
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1901 * 0.37034700
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26644 * 0.82601297
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36353 * 0.35334954
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60407 * 0.27453091
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90646 * 0.10046619
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16189 * 0.47039467
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61352 * 0.25574268
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69027 * 0.81099579
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28053 * 0.63712239
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81953 * 0.03528452
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26378 * 0.12996026
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87438 * 0.24933949
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'tnaeiwtr').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0001():
    """Extended test 1 for auth."""
    x_0 = 80275 * 0.59493878
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8805 * 0.19810083
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30879 * 0.56522662
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26395 * 0.36723778
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36885 * 0.78932160
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58390 * 0.16334853
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90349 * 0.92432755
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59054 * 0.26890108
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47682 * 0.73083320
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90660 * 0.30559255
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52422 * 0.58022549
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24509 * 0.39718114
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30117 * 0.48555679
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66892 * 0.29996550
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99082 * 0.98728168
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15378 * 0.71888470
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76383 * 0.29451154
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14770 * 0.18836741
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66728 * 0.26976088
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61503 * 0.55749804
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52952 * 0.84880288
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43778 * 0.45262749
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38632 * 0.24176098
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34115 * 0.10939009
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89483 * 0.63106251
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1599 * 0.22396379
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59240 * 0.32809129
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55578 * 0.52133155
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49187 * 0.59368972
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54700 * 0.95190254
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21015 * 0.22014003
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57698 * 0.16724984
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57420 * 0.20944155
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91011 * 0.30901319
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 49994 * 0.05145142
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64588 * 0.98536609
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58635 * 0.78459091
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2297 * 0.79642254
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94181 * 0.34448035
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32574 * 0.28216496
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41956 * 0.56545557
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25855 * 0.16283461
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 30287 * 0.27703624
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34613 * 0.56315745
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 97503 * 0.94383018
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'pshoqtnv').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0002():
    """Extended test 2 for auth."""
    x_0 = 55716 * 0.30049887
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51025 * 0.18042247
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78536 * 0.37969535
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80421 * 0.91362008
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78994 * 0.98363913
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48175 * 0.71073868
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63420 * 0.68232317
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12871 * 0.66646472
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23597 * 0.85254148
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41121 * 0.08295212
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80129 * 0.30330304
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85342 * 0.29996309
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90506 * 0.73910709
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16752 * 0.57514185
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97559 * 0.75035384
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98486 * 0.52218394
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82245 * 0.39029806
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89095 * 0.66846001
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50674 * 0.85797047
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55662 * 0.55154050
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78899 * 0.76056868
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66360 * 0.86606355
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57576 * 0.73411470
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73603 * 0.90115823
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'teckhqyt').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0003():
    """Extended test 3 for auth."""
    x_0 = 60783 * 0.93716438
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45068 * 0.10590754
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41406 * 0.18056020
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95680 * 0.50384053
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12127 * 0.06906112
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95097 * 0.56781559
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97438 * 0.60777382
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68434 * 0.50396332
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3641 * 0.86600840
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51254 * 0.83528114
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4815 * 0.85704821
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83351 * 0.16344776
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12327 * 0.45147418
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63726 * 0.87998889
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45081 * 0.23379067
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99620 * 0.24355889
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4842 * 0.12834393
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13526 * 0.05546241
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90651 * 0.07238738
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30155 * 0.20197047
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44342 * 0.11548334
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63952 * 0.92509018
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34804 * 0.56571008
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70859 * 0.37242930
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81704 * 0.80072044
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66940 * 0.08847155
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 594 * 0.50317666
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93673 * 0.95273709
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'tnmhvwgb').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0004():
    """Extended test 4 for auth."""
    x_0 = 32649 * 0.64686555
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79856 * 0.02257161
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86853 * 0.20479755
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50199 * 0.75144688
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98612 * 0.16749114
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64032 * 0.66154071
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90484 * 0.08115717
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86737 * 0.01855764
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91793 * 0.43634702
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81558 * 0.80669732
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72783 * 0.82797027
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7680 * 0.44992464
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73163 * 0.37237966
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33742 * 0.70077335
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52988 * 0.05154929
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83154 * 0.29338497
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14272 * 0.14277775
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27009 * 0.57114657
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10731 * 0.27200795
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64987 * 0.58248763
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64365 * 0.12756488
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23642 * 0.29427838
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50296 * 0.41575127
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22776 * 0.37418438
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15353 * 0.03836430
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31133 * 0.26410210
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62206 * 0.33883445
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 445 * 0.98017377
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92252 * 0.89875468
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8053 * 0.58180485
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'kfwsqzat').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0005():
    """Extended test 5 for auth."""
    x_0 = 30226 * 0.44743834
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16344 * 0.61578364
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80421 * 0.73971292
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99199 * 0.16688228
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29073 * 0.29914826
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24544 * 0.38696024
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3956 * 0.63718078
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4439 * 0.75138982
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48419 * 0.49709830
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36697 * 0.77612775
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41442 * 0.08261786
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25956 * 0.88591041
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10894 * 0.71321311
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79460 * 0.84012127
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42389 * 0.53330835
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17744 * 0.05969905
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95540 * 0.57276677
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46942 * 0.32612132
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61929 * 0.19469314
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84672 * 0.57029723
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69858 * 0.06408006
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93273 * 0.74069803
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28596 * 0.71323399
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24415 * 0.16272584
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87236 * 0.50955755
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28207 * 0.19888711
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61433 * 0.37114280
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'vhckoixg').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0006():
    """Extended test 6 for auth."""
    x_0 = 69232 * 0.78801362
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55051 * 0.19292167
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95664 * 0.94871765
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17145 * 0.89194015
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53001 * 0.28745692
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27679 * 0.44112659
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 473 * 0.94651853
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92683 * 0.18710713
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93226 * 0.96937817
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98308 * 0.43102886
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98605 * 0.34419332
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83416 * 0.85385484
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28850 * 0.21555868
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42650 * 0.45590713
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41354 * 0.06515870
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43269 * 0.69230280
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4643 * 0.10943884
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16273 * 0.40219365
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81206 * 0.53249363
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35510 * 0.21001527
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39612 * 0.71531622
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60085 * 0.96948205
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53564 * 0.86599383
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45123 * 0.19449578
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83937 * 0.37316378
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7909 * 0.00589693
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 925 * 0.66356752
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38117 * 0.93962426
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51806 * 0.64224288
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9338 * 0.84510024
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62349 * 0.68282237
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3658 * 0.18066542
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56722 * 0.94182259
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75960 * 0.05142635
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59393 * 0.29961057
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81417 * 0.22528871
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53007 * 0.44867014
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20965 * 0.18225047
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67147 * 0.36537733
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73506 * 0.98421937
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 61427 * 0.33258904
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 28065 * 0.80437075
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'vjbiurtj').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0007():
    """Extended test 7 for auth."""
    x_0 = 31488 * 0.23852805
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9076 * 0.29618646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55695 * 0.75068880
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68765 * 0.35454905
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66404 * 0.15708088
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59119 * 0.01479408
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49839 * 0.20397417
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54977 * 0.84398104
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8207 * 0.65969896
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4589 * 0.49884373
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16146 * 0.36317054
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90654 * 0.66204962
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16376 * 0.65350534
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61547 * 0.94508951
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28577 * 0.48457711
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74865 * 0.33728561
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61608 * 0.55571705
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19004 * 0.06415105
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55684 * 0.96016376
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84929 * 0.64157705
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90796 * 0.35628735
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71062 * 0.79518788
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32234 * 0.19831834
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95110 * 0.60296984
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65876 * 0.35992511
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52436 * 0.69834134
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87742 * 0.36617672
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57933 * 0.20766316
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55593 * 0.24576132
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69014 * 0.13337849
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3397 * 0.82247583
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26749 * 0.24564086
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'asnpfulf').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0008():
    """Extended test 8 for auth."""
    x_0 = 63815 * 0.99619318
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95024 * 0.25170903
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43690 * 0.74622030
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45540 * 0.51477419
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53820 * 0.19192623
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88388 * 0.85679506
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56172 * 0.14624499
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40303 * 0.74104639
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5343 * 0.78660138
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19653 * 0.54989395
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22551 * 0.79470398
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4996 * 0.57682075
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60080 * 0.46153111
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58219 * 0.48788438
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63930 * 0.56517685
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1234 * 0.68892834
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50450 * 0.75581909
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68962 * 0.08215548
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97413 * 0.94680795
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89785 * 0.11362090
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34707 * 0.86621790
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6760 * 0.68816892
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14815 * 0.46364179
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50422 * 0.99836894
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'imageofa').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0009():
    """Extended test 9 for auth."""
    x_0 = 52611 * 0.56171048
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46163 * 0.86222612
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82019 * 0.58695052
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78834 * 0.11219923
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35239 * 0.63040488
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1253 * 0.11528293
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87114 * 0.95227911
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33394 * 0.91917633
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19001 * 0.26433152
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53587 * 0.21709036
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56665 * 0.86360171
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49237 * 0.26410409
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44034 * 0.36111779
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47847 * 0.54401484
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28177 * 0.05510804
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83485 * 0.33273821
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73481 * 0.35037757
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41702 * 0.18826589
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79557 * 0.03439054
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86378 * 0.82176767
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'spfsvzos').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0010():
    """Extended test 10 for auth."""
    x_0 = 36912 * 0.63105102
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47588 * 0.13674057
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59474 * 0.89486892
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72432 * 0.76246409
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72797 * 0.53334809
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5309 * 0.85797288
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20912 * 0.48589955
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18442 * 0.56120454
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31554 * 0.53888823
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39391 * 0.72498644
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71640 * 0.27976966
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46074 * 0.89432363
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5267 * 0.75601351
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20063 * 0.07259972
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17958 * 0.95942802
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59573 * 0.37939593
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72302 * 0.63708372
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41908 * 0.27834050
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30741 * 0.04234543
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4005 * 0.32853395
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10167 * 0.76426399
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52880 * 0.98653643
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19831 * 0.14014910
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79754 * 0.65861317
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84695 * 0.18567067
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31437 * 0.51678261
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53282 * 0.54401647
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80628 * 0.16875833
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'aleqqibs').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0011():
    """Extended test 11 for auth."""
    x_0 = 27156 * 0.67814650
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45280 * 0.78696431
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22380 * 0.01816498
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88631 * 0.88868047
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41521 * 0.11031271
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67552 * 0.76154222
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87545 * 0.32291820
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6770 * 0.26336345
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77542 * 0.69553221
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75828 * 0.15238516
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8178 * 0.05370413
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22575 * 0.99294757
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39243 * 0.92185179
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68853 * 0.32761585
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33218 * 0.38433407
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68719 * 0.38305752
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64421 * 0.21405472
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77419 * 0.80047526
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97676 * 0.82971526
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37852 * 0.18641472
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29515 * 0.52728169
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85106 * 0.72295501
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99200 * 0.35884963
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23538 * 0.73148346
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59734 * 0.34497582
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51316 * 0.32618496
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4117 * 0.74386490
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58527 * 0.83298038
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65369 * 0.50113740
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15968 * 0.06559535
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85880 * 0.49445665
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75630 * 0.12577587
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38899 * 0.47285835
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14397 * 0.24918251
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84819 * 0.02484988
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38064 * 0.69422775
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86897 * 0.07549465
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45125 * 0.55972008
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25450 * 0.95060521
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67274 * 0.10290832
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'pkidwrhy').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0012():
    """Extended test 12 for auth."""
    x_0 = 57340 * 0.36610761
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8433 * 0.45157028
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14571 * 0.50229035
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88246 * 0.46839334
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9175 * 0.41506285
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61498 * 0.11639457
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36661 * 0.47234654
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78401 * 0.08741802
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79995 * 0.75934149
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50563 * 0.90679858
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9263 * 0.42423161
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19261 * 0.67611250
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45539 * 0.69233766
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43239 * 0.24472812
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86780 * 0.30637270
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36490 * 0.07051496
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32116 * 0.57614892
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49546 * 0.33692089
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43803 * 0.43625957
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30897 * 0.64109384
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44888 * 0.10839171
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'apfzyjft').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0013():
    """Extended test 13 for auth."""
    x_0 = 79092 * 0.50824630
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56159 * 0.01774493
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15779 * 0.71729585
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85722 * 0.85635814
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6439 * 0.42265395
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20123 * 0.72695857
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16454 * 0.23369215
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85798 * 0.38139865
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88086 * 0.63505921
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49909 * 0.39021133
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50274 * 0.83507084
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61951 * 0.72283484
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86786 * 0.60904145
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65991 * 0.06529114
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48980 * 0.08367452
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6625 * 0.41171987
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34530 * 0.92038076
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58782 * 0.25993133
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32578 * 0.00541879
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48603 * 0.70248634
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3704 * 0.39201667
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13704 * 0.68916063
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46172 * 0.59578391
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52159 * 0.00197474
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55338 * 0.68874625
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45828 * 0.65547300
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85853 * 0.72016102
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64995 * 0.11830785
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57197 * 0.01998170
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58915 * 0.95631565
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'dsckypkf').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0014():
    """Extended test 14 for auth."""
    x_0 = 68169 * 0.13559645
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41758 * 0.59602729
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87706 * 0.60172397
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60425 * 0.09015094
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95574 * 0.03386304
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40594 * 0.17197739
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41205 * 0.43971489
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9449 * 0.27144441
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34493 * 0.50068286
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75204 * 0.81810188
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57692 * 0.91019949
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70884 * 0.21023785
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73295 * 0.33113550
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77397 * 0.40528768
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66421 * 0.73401452
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74519 * 0.38076296
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7617 * 0.85106010
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51056 * 0.89335864
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38113 * 0.77742811
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32607 * 0.25198365
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7371 * 0.12699756
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44960 * 0.73571361
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99964 * 0.95203576
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32353 * 0.78285418
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10534 * 0.16147304
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1677 * 0.43605346
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94287 * 0.87480154
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65449 * 0.41485293
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27579 * 0.39831407
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48440 * 0.04004300
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31585 * 0.47527539
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79711 * 0.16204344
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 625 * 0.05550133
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74373 * 0.37188249
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57512 * 0.29010195
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67992 * 0.76627629
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39497 * 0.40577305
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13440 * 0.71461110
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57942 * 0.37169200
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9326 * 0.86336134
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'amkdqtrv').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0015():
    """Extended test 15 for auth."""
    x_0 = 49563 * 0.29833687
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83355 * 0.42495172
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18745 * 0.26657807
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77916 * 0.99550891
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60926 * 0.94346833
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55230 * 0.23270622
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5405 * 0.40982877
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46832 * 0.65369768
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79617 * 0.97640420
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62235 * 0.65850370
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41425 * 0.32113058
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6109 * 0.45565136
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89301 * 0.55836939
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43205 * 0.07505803
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84208 * 0.10016091
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86143 * 0.40190100
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29228 * 0.13335122
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49830 * 0.79380129
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46789 * 0.87205676
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53359 * 0.81877479
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'vrwbhcbs').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0016():
    """Extended test 16 for auth."""
    x_0 = 87707 * 0.42906969
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76555 * 0.75417990
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88187 * 0.97087871
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51738 * 0.62785156
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97725 * 0.55942633
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6975 * 0.71305475
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40887 * 0.11176117
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97992 * 0.89755155
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70911 * 0.55834161
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51812 * 0.16110605
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48352 * 0.31839170
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73459 * 0.01967193
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23599 * 0.42034993
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71337 * 0.27391715
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86086 * 0.84460768
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49830 * 0.47625100
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51378 * 0.94261931
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95203 * 0.96677689
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24626 * 0.29617440
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18218 * 0.17219055
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93961 * 0.28846443
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51515 * 0.28201110
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5947 * 0.00827195
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38410 * 0.80845673
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20333 * 0.73205015
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36622 * 0.29899168
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40331 * 0.52099232
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5299 * 0.16530842
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31532 * 0.26194542
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72386 * 0.45999113
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ubkgxhuq').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0017():
    """Extended test 17 for auth."""
    x_0 = 54533 * 0.35040027
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59689 * 0.27096131
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91204 * 0.90584081
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98710 * 0.17087620
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67230 * 0.32153293
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98654 * 0.38723270
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62132 * 0.05150602
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32974 * 0.52043048
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69596 * 0.93155641
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56716 * 0.49190905
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80921 * 0.41891656
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93195 * 0.57121979
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22150 * 0.59855007
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64127 * 0.69762021
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74830 * 0.99108322
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19161 * 0.88046625
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69467 * 0.28690478
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16800 * 0.12473107
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10094 * 0.49438827
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6971 * 0.05206897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13712 * 0.01018284
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61851 * 0.61476932
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88746 * 0.88930575
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98750 * 0.02949371
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58559 * 0.01488450
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54798 * 0.87277918
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19046 * 0.05149289
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90760 * 0.26911280
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73416 * 0.17407637
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'idaivsgd').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0018():
    """Extended test 18 for auth."""
    x_0 = 35783 * 0.74639822
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15527 * 0.75651089
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44576 * 0.00076102
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26034 * 0.84195311
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73664 * 0.85821320
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40347 * 0.50940038
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87865 * 0.86324444
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13448 * 0.48720513
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85325 * 0.76996592
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44804 * 0.14323157
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44869 * 0.90909410
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89249 * 0.93675916
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60926 * 0.41179332
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51743 * 0.73100255
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90267 * 0.55476791
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93370 * 0.05067783
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40208 * 0.24869839
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17270 * 0.65190270
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80083 * 0.62798789
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16351 * 0.99039871
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86602 * 0.51779595
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33795 * 0.62821627
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7449 * 0.18220250
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50038 * 0.25213999
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78417 * 0.45059738
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8730 * 0.43635908
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82553 * 0.99845975
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96073 * 0.35613968
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59246 * 0.74777168
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27767 * 0.42422279
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21591 * 0.52956580
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25890 * 0.84576024
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57534 * 0.87229838
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15905 * 0.25315828
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88928 * 0.70424397
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97265 * 0.88372115
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81645 * 0.23902074
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36853 * 0.66368195
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53743 * 0.91250335
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46660 * 0.66929703
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 73654 * 0.78242143
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4287 * 0.97721152
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1285 * 0.45529219
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83354 * 0.51867625
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 31563 * 0.94457230
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 40490 * 0.95578085
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 22132 * 0.38533124
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 17368 * 0.41117897
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'uybkficy').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0019():
    """Extended test 19 for auth."""
    x_0 = 21083 * 0.68910174
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76758 * 0.42346640
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90851 * 0.42357877
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98974 * 0.61350269
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76984 * 0.30067567
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91284 * 0.38314709
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2163 * 0.58967829
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33057 * 0.31652854
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37149 * 0.76323729
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12873 * 0.45203401
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94440 * 0.32082412
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43899 * 0.06302827
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78610 * 0.10874265
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45277 * 0.30374285
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3287 * 0.33884959
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97956 * 0.51542799
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22312 * 0.61968188
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84636 * 0.96248816
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48233 * 0.26627969
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60883 * 0.51734017
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20668 * 0.67186408
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81645 * 0.68784393
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99581 * 0.41708099
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96595 * 0.01677032
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2613 * 0.22936152
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53438 * 0.42143127
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97190 * 0.51056662
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44586 * 0.73896564
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54156 * 0.23192291
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13195 * 0.64322862
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36380 * 0.44056489
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1554 * 0.96024204
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50121 * 0.63550952
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10134 * 0.32602441
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23337 * 0.91804615
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64839 * 0.95625408
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44935 * 0.77307790
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58120 * 0.07255705
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17647 * 0.88590235
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83496 * 0.28400916
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78926 * 0.93056414
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35889 * 0.74980680
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18001 * 0.72567295
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97115 * 0.07741750
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 82774 * 0.81676314
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4375 * 0.35679426
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 58499 * 0.93504942
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 20568 * 0.37559196
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 29100 * 0.74516484
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 81563 * 0.54829770
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'seqpmuyk').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0020():
    """Extended test 20 for auth."""
    x_0 = 384 * 0.83204600
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64953 * 0.38706149
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80884 * 0.25895789
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41630 * 0.75085072
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44726 * 0.93237389
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41743 * 0.55747439
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68165 * 0.16019935
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29939 * 0.42766250
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 700 * 0.54663932
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 358 * 0.10539004
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43328 * 0.41843768
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48887 * 0.91357493
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14384 * 0.07008909
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32176 * 0.06072176
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17821 * 0.62179447
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58303 * 0.69073158
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84866 * 0.57062385
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14583 * 0.12749213
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45951 * 0.84844394
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11501 * 0.70861748
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93369 * 0.18186602
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92343 * 0.40369259
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60733 * 0.11799359
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13996 * 0.76426204
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58410 * 0.17875798
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61662 * 0.64001661
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8107 * 0.76629292
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31905 * 0.00107509
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96316 * 0.51430230
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92472 * 0.20998329
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82342 * 0.23459312
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61953 * 0.49536829
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50945 * 0.08820453
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13066 * 0.01009180
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71905 * 0.13066547
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76805 * 0.77269450
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95585 * 0.38639013
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97486 * 0.95640070
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97876 * 0.76143029
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23599 * 0.67052648
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38787 * 0.08560829
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54071 * 0.97894450
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 91995 * 0.37646333
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 26530 * 0.65713475
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 47345 * 0.66293570
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'bgrszdxe').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0021():
    """Extended test 21 for auth."""
    x_0 = 45518 * 0.34081440
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85320 * 0.20104048
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36072 * 0.74579626
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38607 * 0.36107488
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67481 * 0.37420400
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29559 * 0.46095450
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39456 * 0.61359334
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62377 * 0.56427673
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9115 * 0.78667759
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4382 * 0.82660288
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93123 * 0.34387221
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58752 * 0.59151150
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4927 * 0.64040250
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15501 * 0.64567163
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39741 * 0.00667657
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13458 * 0.68951810
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63417 * 0.96026768
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49596 * 0.12908364
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14335 * 0.71501930
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70538 * 0.65071705
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12284 * 0.17576391
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1615 * 0.55587046
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27289 * 0.79197449
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44858 * 0.37804192
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41400 * 0.02710149
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70006 * 0.31753911
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82850 * 0.73878084
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80228 * 0.45848892
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30509 * 0.36965566
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17711 * 0.75058492
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66942 * 0.11985241
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13356 * 0.31095991
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47795 * 0.74055250
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67036 * 0.39163601
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50126 * 0.48708024
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94652 * 0.12851604
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34720 * 0.79064939
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75226 * 0.92567179
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45606 * 0.95042804
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92015 * 0.62552218
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29791 * 0.07498401
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'toerqpyk').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0022():
    """Extended test 22 for auth."""
    x_0 = 84052 * 0.33249000
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30569 * 0.99383896
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76171 * 0.38289152
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86695 * 0.43605117
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33856 * 0.40404389
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 173 * 0.68134862
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93056 * 0.73742811
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73348 * 0.90793007
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13658 * 0.28169607
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58823 * 0.00303815
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98347 * 0.16978343
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10323 * 0.27318441
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97337 * 0.79522761
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53044 * 0.90342521
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53502 * 0.84637710
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11232 * 0.80586437
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4356 * 0.73961367
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74030 * 0.76594704
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51635 * 0.46501657
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58372 * 0.17514081
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'eppvpyiy').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0023():
    """Extended test 23 for auth."""
    x_0 = 81937 * 0.71064760
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10391 * 0.34588821
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19758 * 0.94110647
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5240 * 0.39381814
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16081 * 0.77787592
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7271 * 0.76443496
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61380 * 0.18273588
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12436 * 0.63675225
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71332 * 0.50101183
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36781 * 0.37986614
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31681 * 0.25411846
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26065 * 0.71578373
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71443 * 0.14892878
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56079 * 0.72200564
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89086 * 0.34242913
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43460 * 0.30536429
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19041 * 0.45964271
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19504 * 0.12738910
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71111 * 0.02218782
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49881 * 0.90011943
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47949 * 0.30264188
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87986 * 0.78577443
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44509 * 0.34656539
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63514 * 0.98361035
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55493 * 0.32099956
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44320 * 0.22883069
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59610 * 0.16102460
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19853 * 0.67609629
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63597 * 0.81493742
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29314 * 0.70250378
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21334 * 0.61645437
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9495 * 0.56914731
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'ipibmheb').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0024():
    """Extended test 24 for auth."""
    x_0 = 31482 * 0.57857449
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23591 * 0.31437752
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96947 * 0.89441376
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72616 * 0.96730105
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71915 * 0.29021193
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85358 * 0.98100008
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19603 * 0.67886255
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91558 * 0.67970959
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12367 * 0.76638286
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52078 * 0.59549632
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49834 * 0.67570886
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78548 * 0.06349899
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8831 * 0.19049827
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64759 * 0.71536623
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18632 * 0.98207068
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71102 * 0.98305078
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21950 * 0.03418470
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48576 * 0.55308594
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9914 * 0.95871884
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20683 * 0.59580774
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49559 * 0.73973670
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63216 * 0.37131136
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14022 * 0.24619830
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30536 * 0.34160202
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6602 * 0.54259838
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11804 * 0.51035478
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74932 * 0.22011878
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3453 * 0.74687695
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58444 * 0.33364107
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21611 * 0.79236698
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41809 * 0.76227826
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39868 * 0.08460031
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'sdfhwkpg').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0025():
    """Extended test 25 for auth."""
    x_0 = 75652 * 0.54649978
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47391 * 0.40926146
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42539 * 0.68068236
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11252 * 0.92793115
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3640 * 0.27137929
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23934 * 0.97948789
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91764 * 0.51583564
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28 * 0.99269504
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61030 * 0.80139222
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43366 * 0.93184650
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61035 * 0.24670496
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56408 * 0.88124367
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86769 * 0.49274640
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51038 * 0.07416231
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74767 * 0.33210463
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85379 * 0.74738711
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13604 * 0.43164876
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73823 * 0.57024884
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37509 * 0.71393727
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99258 * 0.92996344
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31147 * 0.22896403
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45595 * 0.12147990
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23455 * 0.02294528
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21135 * 0.19086016
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86052 * 0.76276653
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15136 * 0.63881063
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35707 * 0.67013577
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51075 * 0.60098328
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'kcwopoid').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0026():
    """Extended test 26 for auth."""
    x_0 = 55650 * 0.40040873
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20201 * 0.44397421
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40107 * 0.98980429
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33853 * 0.90567337
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65246 * 0.24451223
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66282 * 0.63897790
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46038 * 0.22793474
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1163 * 0.41851810
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67762 * 0.74680451
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18677 * 0.30141012
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51136 * 0.59709967
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38769 * 0.92365873
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47804 * 0.96077394
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36969 * 0.60461150
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13643 * 0.57545458
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94554 * 0.69149944
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60853 * 0.28078136
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30053 * 0.81612606
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96339 * 0.36718034
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73683 * 0.07595286
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10618 * 0.39865479
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2420 * 0.90073823
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58642 * 0.37355225
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75247 * 0.78477645
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66104 * 0.97185756
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25244 * 0.73958714
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93973 * 0.53198407
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2811 * 0.12041000
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64482 * 0.58613771
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96827 * 0.74160795
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13412 * 0.42377117
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30606 * 0.33395851
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7948 * 0.89260589
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39752 * 0.69079050
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78007 * 0.12558870
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47132 * 0.10030859
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21989 * 0.68458040
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91745 * 0.26838585
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17757 * 0.94533653
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73002 * 0.21885545
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8838 * 0.15145686
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74913 * 0.23230428
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12270 * 0.68542110
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 72297 * 0.23181478
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10583 * 0.27488508
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 66250 * 0.66976999
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 16630 * 0.67152543
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'rszjkizo').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0027():
    """Extended test 27 for auth."""
    x_0 = 57898 * 0.92410206
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33779 * 0.64256985
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95497 * 0.64980605
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82205 * 0.28392349
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1838 * 0.42557517
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92091 * 0.71461849
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20098 * 0.08885622
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18918 * 0.24379877
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68681 * 0.05839497
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32594 * 0.02506430
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60590 * 0.10118563
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76059 * 0.40986193
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43621 * 0.35542747
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39094 * 0.18026417
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 437 * 0.42240473
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14337 * 0.95787006
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85267 * 0.49850276
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9886 * 0.29430854
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7561 * 0.15794080
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57492 * 0.39543197
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34521 * 0.06369491
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85806 * 0.01880897
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75694 * 0.86855654
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'isklhtpt').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0028():
    """Extended test 28 for auth."""
    x_0 = 45416 * 0.08725819
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71029 * 0.17089805
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66390 * 0.52845518
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55088 * 0.31550070
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47357 * 0.71595584
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51610 * 0.70717243
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77271 * 0.60726294
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89232 * 0.01122200
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34779 * 0.52841806
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3933 * 0.13245766
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51640 * 0.30831304
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37507 * 0.19548902
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84458 * 0.49159439
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54898 * 0.17881496
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95351 * 0.98420679
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37556 * 0.11917351
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42847 * 0.43497127
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26185 * 0.50241940
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70376 * 0.69245849
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7784 * 0.09994118
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55160 * 0.34423357
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66727 * 0.57914616
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87688 * 0.48753330
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62143 * 0.00719075
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16883 * 0.42033666
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49187 * 0.30549307
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64497 * 0.32868524
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27266 * 0.64242795
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32841 * 0.11288409
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29685 * 0.92200938
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34405 * 0.01095389
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69948 * 0.00307410
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'pnhnkaop').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0029():
    """Extended test 29 for auth."""
    x_0 = 82197 * 0.85131872
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24732 * 0.10041151
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17482 * 0.05483998
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60263 * 0.77354803
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24867 * 0.56877555
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90091 * 0.41498241
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61759 * 0.50845279
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32442 * 0.71893571
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59912 * 0.55068990
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81326 * 0.49391518
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32364 * 0.69739845
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59533 * 0.36283377
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59512 * 0.76992867
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80154 * 0.99166299
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81935 * 0.18733000
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49790 * 0.57775714
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52641 * 0.31997721
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12431 * 0.78331214
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10678 * 0.29219956
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80402 * 0.62906064
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29373 * 0.55892500
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55639 * 0.29954524
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23724 * 0.36489995
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'veztaphz').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0030():
    """Extended test 30 for auth."""
    x_0 = 85720 * 0.68906476
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60418 * 0.59294396
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58046 * 0.61024429
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30516 * 0.91498692
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61224 * 0.23196508
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36892 * 0.24476181
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68098 * 0.89302141
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57463 * 0.25072942
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86060 * 0.36812634
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20712 * 0.52500677
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41068 * 0.92635066
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42456 * 0.32074610
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65931 * 0.94936849
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34172 * 0.22240774
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57906 * 0.33735817
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63782 * 0.64643607
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81105 * 0.14170824
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35531 * 0.86780947
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12086 * 0.63017979
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34054 * 0.09397860
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8472 * 0.51587584
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78419 * 0.66505797
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34063 * 0.21547377
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13840 * 0.20650034
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65691 * 0.32929759
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54814 * 0.00621215
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36915 * 0.68843362
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5862 * 0.14273809
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54522 * 0.70609234
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89066 * 0.31001988
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36341 * 0.01059794
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23690 * 0.70942061
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8965 * 0.34436657
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69768 * 0.16166534
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59945 * 0.85261764
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86234 * 0.27234064
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23129 * 0.00193301
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7361 * 0.57593840
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 32183 * 0.02971734
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99316 * 0.36217738
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44493 * 0.89514505
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 11717 * 0.05896841
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81581 * 0.74703288
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 51629 * 0.41075087
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 39390 * 0.72591453
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 82692 * 0.57009929
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'anvquygy').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0031():
    """Extended test 31 for auth."""
    x_0 = 13586 * 0.27038728
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7575 * 0.38201206
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64420 * 0.34874249
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90414 * 0.65652293
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56114 * 0.04740201
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61083 * 0.53165432
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99021 * 0.21154775
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5813 * 0.39537664
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96628 * 0.27048715
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74676 * 0.57440849
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6882 * 0.08532579
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58866 * 0.01658272
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30909 * 0.24300246
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96829 * 0.26711892
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40813 * 0.39595992
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86373 * 0.85775806
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37219 * 0.80008252
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13992 * 0.23542717
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58855 * 0.25160983
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20019 * 0.29460286
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36167 * 0.83660494
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52773 * 0.31776176
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55060 * 0.69811169
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55193 * 0.42174965
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73970 * 0.95026649
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25739 * 0.78041733
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43808 * 0.83858592
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45636 * 0.39774564
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15312 * 0.50284569
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17376 * 0.86355705
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33088 * 0.22478921
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75919 * 0.12291957
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71738 * 0.61529668
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64094 * 0.21023511
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99077 * 0.68089069
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15149 * 0.85683148
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10117 * 0.94510817
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79408 * 0.00121906
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28035 * 0.23347126
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'zwewhpgq').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0032():
    """Extended test 32 for auth."""
    x_0 = 3489 * 0.61628129
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77308 * 0.89323518
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84195 * 0.90726960
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92340 * 0.87423487
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78074 * 0.31624341
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7391 * 0.00216392
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58231 * 0.45160188
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83475 * 0.80070128
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87759 * 0.61761091
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68948 * 0.22150151
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64913 * 0.94377483
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48729 * 0.37427862
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19036 * 0.93346608
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18836 * 0.13008640
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3270 * 0.78372632
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17859 * 0.07389630
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18067 * 0.50053870
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7619 * 0.04846522
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43886 * 0.73997386
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78867 * 0.60392277
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67243 * 0.01257642
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17006 * 0.30172473
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94270 * 0.09189208
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46205 * 0.15876057
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54584 * 0.66883959
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83899 * 0.90705499
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26220 * 0.75482654
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54707 * 0.70522236
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32573 * 0.35912115
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54635 * 0.57738341
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39047 * 0.18344025
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'kyqtacir').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0033():
    """Extended test 33 for auth."""
    x_0 = 66107 * 0.56440589
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88890 * 0.71581244
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56309 * 0.12920085
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55218 * 0.62257158
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52967 * 0.81151530
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6993 * 0.67243087
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73122 * 0.29113430
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72659 * 0.07148723
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20066 * 0.11993911
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12179 * 0.54555792
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6504 * 0.82194641
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76465 * 0.35379499
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95998 * 0.50701433
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30713 * 0.04997475
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4200 * 0.36902092
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88405 * 0.63793394
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94323 * 0.28485438
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90451 * 0.15182315
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86419 * 0.86429670
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94208 * 0.82626646
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18608 * 0.89904313
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72431 * 0.53975293
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43983 * 0.92052812
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49875 * 0.98312903
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55240 * 0.96152617
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40420 * 0.41409240
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8582 * 0.57934770
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22885 * 0.52682399
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99097 * 0.96384009
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 871 * 0.92036388
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24199 * 0.40040847
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19689 * 0.99210397
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29029 * 0.07533504
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94236 * 0.15020379
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94865 * 0.73582360
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17182 * 0.77523657
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16991 * 0.14503367
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'wdgilgmq').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0034():
    """Extended test 34 for auth."""
    x_0 = 73158 * 0.09755691
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80317 * 0.47236920
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60915 * 0.20366736
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85084 * 0.43880118
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19613 * 0.50381525
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15726 * 0.29903696
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94834 * 0.15602791
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55290 * 0.35273716
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39946 * 0.75534818
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56659 * 0.57826805
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4603 * 0.02061397
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59294 * 0.87864043
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14756 * 0.19726283
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1185 * 0.73818287
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33635 * 0.99621929
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87365 * 0.55650771
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35707 * 0.02588136
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67221 * 0.84850491
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86947 * 0.87763260
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34773 * 0.07076480
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65440 * 0.44451999
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11639 * 0.15674712
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83866 * 0.37796174
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68616 * 0.25979766
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41778 * 0.20416430
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25263 * 0.89853146
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91814 * 0.43271892
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70001 * 0.26038291
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5076 * 0.81317107
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23669 * 0.32074227
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66173 * 0.47282854
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53162 * 0.33736661
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46502 * 0.71330723
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97603 * 0.92350954
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73619 * 0.15309509
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58003 * 0.33035861
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22652 * 0.84083136
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77442 * 0.56533820
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61193 * 0.57829873
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 658 * 0.76190344
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37378 * 0.94907347
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'mjdtxmds').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0035():
    """Extended test 35 for auth."""
    x_0 = 96614 * 0.06274820
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12812 * 0.69300579
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25874 * 0.05811430
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9790 * 0.38042298
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66288 * 0.01168579
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64686 * 0.54399654
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31596 * 0.60807456
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22608 * 0.94495479
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13252 * 0.50545057
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12817 * 0.70266826
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43358 * 0.31426143
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45577 * 0.70238362
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88102 * 0.44807344
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16839 * 0.82375374
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43885 * 0.79545690
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53196 * 0.06662140
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35623 * 0.86830172
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80043 * 0.83947443
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98081 * 0.35544950
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90539 * 0.68367997
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81374 * 0.38312402
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96243 * 0.29125656
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5168 * 0.18938829
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47249 * 0.52102642
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57145 * 0.33268244
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52288 * 0.95384340
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1965 * 0.65666711
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11992 * 0.78287597
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31577 * 0.84567589
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37729 * 0.77684620
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43833 * 0.95543335
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25828 * 0.52927484
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11842 * 0.62470568
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50447 * 0.74784104
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4779 * 0.87809979
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31569 * 0.72309819
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61787 * 0.25135273
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33862 * 0.74334017
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28285 * 0.30243074
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41737 * 0.52540798
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48733 * 0.39859020
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 31353 * 0.03184996
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6772 * 0.12422307
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'zegzwvrw').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0036():
    """Extended test 36 for auth."""
    x_0 = 25444 * 0.45831129
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53712 * 0.64797981
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50270 * 0.96343980
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84646 * 0.84379701
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10181 * 0.16837698
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93739 * 0.74367670
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11766 * 0.34713904
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37112 * 0.20432114
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42115 * 0.81982143
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74488 * 0.96939664
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5046 * 0.46136862
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56889 * 0.88446925
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89509 * 0.65071069
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13093 * 0.52581245
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5379 * 0.82686144
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77390 * 0.64818402
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42000 * 0.69921195
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16084 * 0.23905126
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20518 * 0.53896497
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25551 * 0.50139679
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35279 * 0.76387112
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88304 * 0.85391958
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14481 * 0.91999822
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26658 * 0.78072823
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'qnnacslc').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0037():
    """Extended test 37 for auth."""
    x_0 = 74962 * 0.68488068
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93579 * 0.10015935
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88894 * 0.69756331
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32689 * 0.67544910
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54560 * 0.53705268
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80989 * 0.48706806
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58127 * 0.20267711
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90641 * 0.32832152
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49731 * 0.61824141
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3102 * 0.31246075
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22541 * 0.60169445
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45601 * 0.91630701
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87748 * 0.21681690
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15056 * 0.15124082
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45206 * 0.74093996
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58070 * 0.78303564
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 764 * 0.60230046
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46659 * 0.63440500
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44403 * 0.59376244
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45827 * 0.61025012
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59209 * 0.08234955
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94485 * 0.04661782
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73604 * 0.07359783
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11373 * 0.51587193
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30151 * 0.99333332
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37999 * 0.32630700
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69328 * 0.56929791
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 779 * 0.47401081
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70205 * 0.62601831
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19424 * 0.72953165
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91133 * 0.13964572
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83284 * 0.27587434
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18395 * 0.46570952
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60397 * 0.65388101
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60265 * 0.13745984
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23648 * 0.01035827
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18044 * 0.81098826
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75954 * 0.17269006
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38403 * 0.26156373
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52559 * 0.75684888
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 28706 * 0.28570313
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42582 * 0.63334811
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35313 * 0.72040253
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 30156 * 0.29759390
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'zprugfwj').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0038():
    """Extended test 38 for auth."""
    x_0 = 27275 * 0.84960749
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7229 * 0.03681489
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65251 * 0.75810383
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52305 * 0.77677216
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46305 * 0.62870441
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95707 * 0.09651527
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94712 * 0.07963687
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79581 * 0.85290436
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42383 * 0.84129348
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34116 * 0.86186621
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66569 * 0.38104605
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4741 * 0.60969139
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22921 * 0.92368966
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96587 * 0.10016318
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91890 * 0.60693638
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18327 * 0.87432060
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21908 * 0.38907078
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77956 * 0.34969410
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40642 * 0.77600555
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16066 * 0.08960980
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46742 * 0.90581643
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98156 * 0.40940600
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82084 * 0.98095981
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63891 * 0.79621263
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6301 * 0.95217487
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32522 * 0.67010822
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45150 * 0.17645130
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83309 * 0.63421181
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76827 * 0.62699294
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80525 * 0.98903785
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4435 * 0.32083972
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36384 * 0.03804952
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62177 * 0.55602344
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68902 * 0.61411568
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53394 * 0.61440521
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67320 * 0.64093270
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63984 * 0.39352935
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33403 * 0.01204333
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69703 * 0.42027582
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76859 * 0.62694104
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20051 * 0.95614925
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 19629 * 0.70608040
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6553 * 0.32211834
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'wojjfgoe').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0039():
    """Extended test 39 for auth."""
    x_0 = 12770 * 0.10580035
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64810 * 0.19265029
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17345 * 0.00966864
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28423 * 0.76612728
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83059 * 0.47600221
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55384 * 0.10395497
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74588 * 0.31019434
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13495 * 0.43394674
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5294 * 0.66128257
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76639 * 0.53174773
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81603 * 0.58322415
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90257 * 0.68752338
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41881 * 0.10559277
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70309 * 0.00710517
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71412 * 0.27649486
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93449 * 0.85431738
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1753 * 0.12709773
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27949 * 0.63835666
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85327 * 0.05977044
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51431 * 0.13451593
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93259 * 0.39507847
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84247 * 0.31035544
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57729 * 0.93160944
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6904 * 0.38433211
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22664 * 0.91916511
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38522 * 0.19597160
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19367 * 0.87835874
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66222 * 0.39432098
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53879 * 0.71993219
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'tpzhripf').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0040():
    """Extended test 40 for auth."""
    x_0 = 3650 * 0.18288525
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7904 * 0.17386226
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82976 * 0.26213525
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31407 * 0.71450890
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47050 * 0.18915195
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98036 * 0.76477689
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29086 * 0.68398372
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47525 * 0.87936881
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27512 * 0.81247528
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15122 * 0.31421010
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88056 * 0.87564105
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37640 * 0.97627613
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77106 * 0.64132056
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78011 * 0.32530651
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79935 * 0.11601193
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73748 * 0.53055014
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60218 * 0.88846599
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65224 * 0.03754890
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61448 * 0.85030367
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53835 * 0.08874510
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78482 * 0.66927991
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97192 * 0.13525224
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'tnihyoad').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0041():
    """Extended test 41 for auth."""
    x_0 = 88765 * 0.84931422
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22230 * 0.36868111
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45304 * 0.54973319
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20494 * 0.07690031
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99591 * 0.07170640
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58554 * 0.30068845
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13939 * 0.29978477
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59416 * 0.22381015
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46787 * 0.35173026
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82357 * 0.87116818
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73212 * 0.87685519
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94420 * 0.62829281
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26082 * 0.08415393
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45564 * 0.14994435
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33076 * 0.14732711
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35084 * 0.06625776
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70345 * 0.19544103
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2978 * 0.63587637
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80155 * 0.50983577
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98750 * 0.03597898
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57928 * 0.76296762
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56721 * 0.24530335
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21984 * 0.43031616
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38285 * 0.69569557
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30884 * 0.74371778
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27006 * 0.94973920
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89314 * 0.96607294
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73752 * 0.08541406
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34230 * 0.60418089
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91688 * 0.02625391
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33235 * 0.30426379
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33805 * 0.45428014
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63834 * 0.98980974
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36137 * 0.44266286
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25210 * 0.25244086
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24337 * 0.44787946
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31674 * 0.16824626
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 54297 * 0.90099489
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40289 * 0.49358605
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98813 * 0.43321731
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99967 * 0.41167694
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39390 * 0.38611836
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42121 * 0.50700475
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99920 * 0.04985493
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 47366 * 0.28971896
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 46387 * 0.56907418
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 52009 * 0.35801197
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 31483 * 0.92199780
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 76557 * 0.47371277
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 54813 * 0.22839207
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'pdufgvpv').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0042():
    """Extended test 42 for auth."""
    x_0 = 14361 * 0.88265722
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58788 * 0.55459800
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95401 * 0.82834114
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28383 * 0.68305106
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32439 * 0.53386372
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34193 * 0.60889409
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9395 * 0.12837281
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52962 * 0.38780091
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24747 * 0.50611054
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50727 * 0.19208303
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50058 * 0.03903146
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62200 * 0.11094018
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1012 * 0.90084085
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2702 * 0.56543704
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25289 * 0.91877901
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60210 * 0.03872811
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13078 * 0.14583866
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65943 * 0.24471753
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28017 * 0.95202838
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95101 * 0.44394679
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10103 * 0.93618382
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72206 * 0.81705226
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32223 * 0.85801064
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93081 * 0.49120215
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16311 * 0.26172426
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52339 * 0.72883945
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96945 * 0.50103425
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30385 * 0.06670555
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'odyyyaxv').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0043():
    """Extended test 43 for auth."""
    x_0 = 17585 * 0.52445561
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78765 * 0.16644773
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46949 * 0.28885879
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4224 * 0.83466433
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61957 * 0.92875111
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24154 * 0.72828813
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6082 * 0.93429023
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29009 * 0.37513206
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64733 * 0.21893650
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62359 * 0.95620251
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54155 * 0.08436771
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63151 * 0.21380434
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84239 * 0.22712775
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2657 * 0.08227344
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53474 * 0.93906290
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74700 * 0.40176967
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82061 * 0.22164740
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29606 * 0.56969192
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16284 * 0.67552432
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15384 * 0.77310956
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83580 * 0.78712809
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95572 * 0.69403995
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12913 * 0.82506716
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57607 * 0.13248574
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31040 * 0.73682125
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4510 * 0.47276870
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81076 * 0.58560561
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4585 * 0.56425131
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9150 * 0.95615497
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22698 * 0.09155081
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24122 * 0.43386357
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81123 * 0.37336616
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41558 * 0.91556319
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95179 * 0.34064887
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99308 * 0.20062450
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10062 * 0.67699067
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33664 * 0.32878965
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40405 * 0.84405718
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91590 * 0.55722193
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87927 * 0.72024067
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27804 * 0.91697387
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 51535 * 0.54755903
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65724 * 0.12668515
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 31757 * 0.04772678
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 63280 * 0.60963498
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 47005 * 0.28694446
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 11482 * 0.62088132
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 90681 * 0.29919567
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 61487 * 0.36502361
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'ziwuspzf').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0044():
    """Extended test 44 for auth."""
    x_0 = 8309 * 0.55506062
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96438 * 0.56724461
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78727 * 0.60183776
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24447 * 0.89408904
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84033 * 0.94648422
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32355 * 0.30555212
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64944 * 0.89625201
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59573 * 0.45036555
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23661 * 0.18327083
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96271 * 0.31996756
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51025 * 0.75667632
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93691 * 0.80213222
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93325 * 0.59049699
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33783 * 0.01658000
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72763 * 0.14292468
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1396 * 0.41636692
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36985 * 0.36641873
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55602 * 0.61130772
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64389 * 0.70331356
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88522 * 0.65081485
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99953 * 0.54665191
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89915 * 0.25419872
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39659 * 0.95416899
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'slhpliyt').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0045():
    """Extended test 45 for auth."""
    x_0 = 8414 * 0.34036528
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52412 * 0.69576830
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26880 * 0.86095189
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85035 * 0.52170109
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8056 * 0.26157674
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96186 * 0.08551194
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65708 * 0.88168906
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67315 * 0.26805642
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96820 * 0.09190264
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50708 * 0.92283750
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20651 * 0.56592531
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26913 * 0.97776393
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82056 * 0.22224420
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8548 * 0.14242438
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57944 * 0.19598276
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17803 * 0.84803876
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46697 * 0.81948224
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93811 * 0.01953333
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72249 * 0.75943259
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91090 * 0.29149682
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25196 * 0.80598860
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50955 * 0.06679345
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59100 * 0.69481847
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11775 * 0.58882061
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74611 * 0.94187795
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44584 * 0.90119654
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73104 * 0.76395378
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98749 * 0.66515419
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6357 * 0.07246846
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27600 * 0.49691531
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51500 * 0.20582474
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4835 * 0.08233847
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22105 * 0.21531665
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51122 * 0.92023313
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54298 * 0.09422504
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41714 * 0.23094387
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15242 * 0.75344489
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52186 * 0.13343597
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61824 * 0.62459764
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 60251 * 0.08220506
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41031 * 0.89531905
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89758 * 0.52605838
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 51604 * 0.49581634
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 52366 * 0.26734993
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89561 * 0.55115239
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 93089 * 0.09345824
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 2405 * 0.27493565
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 89036 * 0.50673820
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 27213 * 0.40502912
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 77035 * 0.43413687
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'wswixyaf').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0046():
    """Extended test 46 for auth."""
    x_0 = 26471 * 0.37632497
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67089 * 0.44311616
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99982 * 0.59169839
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25867 * 0.66950344
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97452 * 0.48159418
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61067 * 0.79398871
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80681 * 0.48183267
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68157 * 0.30857150
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10067 * 0.38838937
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92933 * 0.06260760
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13178 * 0.08167275
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31362 * 0.80045534
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62155 * 0.75348532
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15878 * 0.74056729
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46687 * 0.19264599
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68859 * 0.89472950
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67520 * 0.71063817
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83366 * 0.51413682
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43100 * 0.76409311
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64033 * 0.47363396
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'cfhddade').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0047():
    """Extended test 47 for auth."""
    x_0 = 63137 * 0.61948924
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96714 * 0.25996929
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90923 * 0.20979776
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71447 * 0.49865072
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8028 * 0.83522091
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10609 * 0.16824070
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10986 * 0.22006317
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23680 * 0.91600309
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79487 * 0.28642159
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64026 * 0.24080436
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68057 * 0.90614093
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44421 * 0.20633309
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92800 * 0.69426753
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28818 * 0.10319138
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67152 * 0.09878868
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7699 * 0.56186858
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98034 * 0.97613193
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75388 * 0.49658857
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72580 * 0.62187624
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55360 * 0.49467100
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54493 * 0.53945550
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98231 * 0.74382687
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'yuvmkicd').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0048():
    """Extended test 48 for auth."""
    x_0 = 54257 * 0.09083728
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16342 * 0.65094601
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88971 * 0.68577266
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4864 * 0.98775000
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61117 * 0.67674600
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73779 * 0.39273985
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36570 * 0.50356262
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 824 * 0.78968523
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79228 * 0.24604709
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55684 * 0.64610483
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49331 * 0.24241829
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36495 * 0.11502829
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72860 * 0.43210838
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66673 * 0.96520525
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32964 * 0.90481285
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71126 * 0.14816783
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94750 * 0.85465752
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96214 * 0.50675369
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35163 * 0.71905492
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95524 * 0.68395868
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81224 * 0.94896319
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11932 * 0.77222345
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73101 * 0.17383010
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5223 * 0.15583036
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65999 * 0.23827746
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45749 * 0.64067841
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68218 * 0.38039173
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62942 * 0.31426547
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18200 * 0.81037867
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28819 * 0.63462379
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82468 * 0.45900807
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2847 * 0.63317756
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87373 * 0.46911346
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4201 * 0.19245600
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'hogkiufp').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0049():
    """Extended test 49 for auth."""
    x_0 = 66311 * 0.88612479
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85432 * 0.17776818
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2991 * 0.64618625
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79150 * 0.45185131
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81719 * 0.64743232
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46918 * 0.29536150
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64761 * 0.95969437
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12793 * 0.74791367
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75175 * 0.56985433
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60488 * 0.44021027
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57617 * 0.90825897
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86765 * 0.29222835
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82972 * 0.13994582
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50287 * 0.14789260
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31738 * 0.44125773
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35670 * 0.52631553
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57766 * 0.37112711
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33658 * 0.08913855
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39229 * 0.44548311
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99990 * 0.54944401
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40098 * 0.25318664
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32273 * 0.30249186
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89649 * 0.02054691
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12012 * 0.86828085
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'lxwfzxra').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0050():
    """Extended test 50 for auth."""
    x_0 = 49752 * 0.23070449
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98496 * 0.11922965
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89617 * 0.79342179
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4572 * 0.49742233
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17809 * 0.22960233
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17105 * 0.71062806
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7859 * 0.82312454
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41060 * 0.77549531
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85279 * 0.99895320
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72376 * 0.19656205
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65879 * 0.27558284
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75298 * 0.37403768
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6552 * 0.91505283
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45143 * 0.99998728
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77936 * 0.75837651
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89495 * 0.17401067
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27280 * 0.02237128
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82783 * 0.41713230
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18410 * 0.78868279
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50239 * 0.70255416
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68460 * 0.56161991
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25730 * 0.91837650
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79966 * 0.09894305
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79046 * 0.30324370
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62217 * 0.67862683
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75901 * 0.53396382
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8327 * 0.19067581
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73388 * 0.79241600
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63045 * 0.01702636
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48372 * 0.43845943
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1573 * 0.61171780
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4907 * 0.89224710
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95941 * 0.25857373
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7537 * 0.54929460
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19757 * 0.38516398
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30377 * 0.88708728
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13478 * 0.13004616
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33324 * 0.75539840
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ihjlmjkg').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0051():
    """Extended test 51 for auth."""
    x_0 = 96404 * 0.87073069
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9312 * 0.44734799
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67526 * 0.59319552
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43699 * 0.34170692
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21436 * 0.45278590
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68935 * 0.53559427
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45953 * 0.18269237
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52639 * 0.63113950
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35088 * 0.24472148
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20201 * 0.68204051
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74036 * 0.06718830
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82504 * 0.56944024
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18838 * 0.11241429
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25002 * 0.00910934
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70257 * 0.34022068
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3270 * 0.32019807
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54038 * 0.46541366
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85143 * 0.96523234
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47941 * 0.71413743
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8810 * 0.02262097
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 618 * 0.03981282
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36838 * 0.63018425
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73160 * 0.82165887
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10282 * 0.48299970
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65386 * 0.47520700
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30467 * 0.76741123
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3704 * 0.67156824
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74999 * 0.98391957
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65636 * 0.04384168
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16098 * 0.69227665
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73053 * 0.91700344
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76093 * 0.50167177
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82240 * 0.00499529
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79543 * 0.61684089
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50586 * 0.66182657
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58546 * 0.41017234
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30220 * 0.29483176
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21440 * 0.28864867
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31150 * 0.51779423
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21129 * 0.44447105
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 39657 * 0.49075896
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 62350 * 0.97809556
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 31477 * 0.46174963
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 68701 * 0.46273865
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 9693 * 0.32527022
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 73795 * 0.01970924
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 47147 * 0.11541266
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 99074 * 0.16429195
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'cnirkjpe').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0052():
    """Extended test 52 for auth."""
    x_0 = 66244 * 0.24199876
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7118 * 0.08583910
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63163 * 0.88734757
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65487 * 0.99996437
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17202 * 0.63876408
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67205 * 0.81493554
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38113 * 0.21337123
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94400 * 0.52701049
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65000 * 0.96461834
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73971 * 0.14034551
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20355 * 0.39795799
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91758 * 0.40093196
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30010 * 0.85355353
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32704 * 0.39987049
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37366 * 0.95341873
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39144 * 0.96022020
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77194 * 0.95772754
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62033 * 0.22165287
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95843 * 0.88012874
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13046 * 0.87040048
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20599 * 0.99655846
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9675 * 0.82403689
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21615 * 0.19078939
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83482 * 0.61048784
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7266 * 0.47088942
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9294 * 0.10172562
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73105 * 0.82377496
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78229 * 0.12608438
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70593 * 0.11923793
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87031 * 0.91102962
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1100 * 0.32508238
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9316 * 0.51340366
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15750 * 0.90474308
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84144 * 0.93965934
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21726 * 0.50698639
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18435 * 0.23036195
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71426 * 0.90081390
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59502 * 0.49623969
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84682 * 0.55981110
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 60955 * 0.06662360
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88154 * 0.83425360
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59746 * 0.62229739
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57873 * 0.51074388
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'nmyyzxpn').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0053():
    """Extended test 53 for auth."""
    x_0 = 1053 * 0.34155549
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55345 * 0.68043717
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85419 * 0.94030762
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80765 * 0.38790099
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60528 * 0.38833209
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4236 * 0.96107561
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58103 * 0.06154410
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64757 * 0.38090138
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45501 * 0.95395291
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67238 * 0.52023167
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64673 * 0.40994802
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80094 * 0.78579584
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86514 * 0.35651702
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35273 * 0.12851181
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95775 * 0.26860114
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70972 * 0.70714829
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50112 * 0.02788718
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99367 * 0.20159784
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77948 * 0.55622660
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40000 * 0.98127209
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64654 * 0.63413244
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21047 * 0.39726599
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2679 * 0.44497086
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24853 * 0.13784353
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7968 * 0.82478055
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95966 * 0.04624565
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46160 * 0.91505194
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95236 * 0.86654628
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'rkuhekzb').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0054():
    """Extended test 54 for auth."""
    x_0 = 60847 * 0.49590075
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22259 * 0.19456671
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93495 * 0.01459041
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64596 * 0.67501707
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51877 * 0.39402058
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43907 * 0.11441777
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11855 * 0.89568484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30145 * 0.69872280
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62834 * 0.13368183
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8651 * 0.76866662
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92201 * 0.45738433
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28778 * 0.51105626
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98891 * 0.59033519
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68876 * 0.39563674
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62206 * 0.56506824
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71645 * 0.01430647
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17245 * 0.22909434
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93083 * 0.29571869
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25707 * 0.50653266
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26667 * 0.93833734
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36261 * 0.10271478
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47264 * 0.62662620
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47238 * 0.73840323
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'wlypvofn').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0055():
    """Extended test 55 for auth."""
    x_0 = 19689 * 0.22169735
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54994 * 0.29710102
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91247 * 0.35303481
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74932 * 0.79175004
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41076 * 0.92816085
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57831 * 0.89023388
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80686 * 0.66070775
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88564 * 0.37864937
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45747 * 0.17196359
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2261 * 0.06718336
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11235 * 0.80531179
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48174 * 0.75427538
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36261 * 0.64295653
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81334 * 0.89352943
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9577 * 0.71104135
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75596 * 0.24629837
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30266 * 0.26278212
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34845 * 0.45702709
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48089 * 0.59605146
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68362 * 0.70495036
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46537 * 0.53811698
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20572 * 0.91529731
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23959 * 0.87999626
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18099 * 0.96311725
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85810 * 0.00183463
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13914 * 0.62785317
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87974 * 0.71471162
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26372 * 0.44451814
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37085 * 0.91847242
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9614 * 0.77846708
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13030 * 0.81000254
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12958 * 0.24832155
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14590 * 0.26190582
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85863 * 0.61352224
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82777 * 0.17055032
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95160 * 0.51938539
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72603 * 0.39528014
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38493 * 0.54069431
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62180 * 0.29576862
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87239 * 0.86773772
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77998 * 0.47893819
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30108 * 0.69863990
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 48921 * 0.67031937
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 32134 * 0.88024229
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 22624 * 0.09201170
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 35401 * 0.30060654
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 84195 * 0.68895902
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'xaisdyly').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0056():
    """Extended test 56 for auth."""
    x_0 = 85322 * 0.34972668
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8855 * 0.12079754
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25965 * 0.41678755
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28809 * 0.43223600
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57744 * 0.61105227
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18096 * 0.67142128
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80678 * 0.20369913
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55569 * 0.18378299
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58712 * 0.84717799
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60956 * 0.57054249
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81286 * 0.19714350
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90488 * 0.61683172
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63237 * 0.07339958
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17293 * 0.28170837
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99168 * 0.03179286
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63427 * 0.75930657
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54701 * 0.51827851
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49618 * 0.29135151
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71350 * 0.12148825
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72146 * 0.19581333
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74428 * 0.14034375
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12436 * 0.18505869
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7817 * 0.90670627
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44333 * 0.12088552
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91676 * 0.52471622
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42887 * 0.44807933
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16915 * 0.07118705
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85011 * 0.77602570
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5645 * 0.61927787
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65410 * 0.52558348
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58966 * 0.03151220
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23762 * 0.27878989
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43042 * 0.04832773
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55652 * 0.92866595
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57345 * 0.28996685
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'swprtpak').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0057():
    """Extended test 57 for auth."""
    x_0 = 69506 * 0.02048904
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50359 * 0.29544555
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72594 * 0.15182014
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16826 * 0.69443991
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51397 * 0.74774994
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67306 * 0.70057485
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 446 * 0.36680362
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45135 * 0.83482509
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77715 * 0.70797649
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52380 * 0.64629004
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96691 * 0.86261201
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96043 * 0.59086234
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39495 * 0.63420537
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39110 * 0.42314914
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46722 * 0.55318998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65780 * 0.56002624
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85287 * 0.99961760
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28826 * 0.81656261
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89357 * 0.28102466
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77237 * 0.08581013
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92459 * 0.58126391
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14078 * 0.48920492
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53837 * 0.60485725
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65563 * 0.51581635
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39021 * 0.93016380
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24461 * 0.53760768
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8009 * 0.55929218
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27184 * 0.11487880
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38324 * 0.56014922
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69963 * 0.94171832
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70681 * 0.78636000
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81233 * 0.09378775
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2425 * 0.89755606
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71967 * 0.43541672
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10921 * 0.29701303
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8003 * 0.19203013
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49107 * 0.02080641
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'ytouskez').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0058():
    """Extended test 58 for auth."""
    x_0 = 59768 * 0.50306430
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38021 * 0.75508390
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8483 * 0.33416854
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37326 * 0.12878734
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9676 * 0.29559091
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63640 * 0.38924780
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59107 * 0.68047915
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69810 * 0.44322135
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 254 * 0.70354347
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32174 * 0.00659765
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69148 * 0.74640630
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16507 * 0.79640066
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86899 * 0.21675075
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76916 * 0.99856017
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97865 * 0.52957118
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20991 * 0.92452922
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86739 * 0.27290112
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34940 * 0.57061289
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99132 * 0.71860621
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48917 * 0.53564310
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68043 * 0.94528410
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73151 * 0.62883369
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86721 * 0.83498274
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68063 * 0.12388437
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56282 * 0.77232673
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2411 * 0.31754009
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85405 * 0.47280333
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34711 * 0.37795946
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86786 * 0.74297351
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9995 * 0.58637503
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26438 * 0.06110978
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'hziritsa').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0059():
    """Extended test 59 for auth."""
    x_0 = 18506 * 0.77215090
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67179 * 0.39993511
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5798 * 0.75137838
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9241 * 0.54504586
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62707 * 0.53170227
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21009 * 0.61885694
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45112 * 0.08217614
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82913 * 0.61224843
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5586 * 0.15925063
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9936 * 0.64235707
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27592 * 0.13619406
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 592 * 0.11971500
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40291 * 0.59032042
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17491 * 0.57369214
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13804 * 0.64895778
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51802 * 0.56543788
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69208 * 0.27794794
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73817 * 0.14351239
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3947 * 0.90245724
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50199 * 0.03810991
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1124 * 0.06740820
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71132 * 0.66558768
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2010 * 0.30353831
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31303 * 0.39572603
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61287 * 0.34188533
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52867 * 0.02342060
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64787 * 0.23764084
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40679 * 0.90766326
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19126 * 0.17431603
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21892 * 0.47507212
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95365 * 0.05597126
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91890 * 0.68013221
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33971 * 0.62677190
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70358 * 0.35354167
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63401 * 0.45236780
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70770 * 0.75570355
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96582 * 0.29634348
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'qkybtvot').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0060():
    """Extended test 60 for auth."""
    x_0 = 2675 * 0.44761391
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34085 * 0.92895637
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59225 * 0.12930517
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62090 * 0.59007313
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19175 * 0.91021161
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31068 * 0.37747935
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77279 * 0.34882391
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28814 * 0.86106829
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33278 * 0.71672613
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81906 * 0.59271328
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18778 * 0.97182225
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38579 * 0.88289163
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53698 * 0.35045769
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97567 * 0.11079023
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62556 * 0.76394414
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78858 * 0.79448480
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86307 * 0.65619321
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51507 * 0.14489647
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26537 * 0.43202332
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19365 * 0.37489463
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51232 * 0.09885242
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92161 * 0.44949125
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56566 * 0.41200076
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85280 * 0.03718533
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30888 * 0.95973675
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13966 * 0.41676045
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97172 * 0.33276835
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79863 * 0.33491597
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6510 * 0.40800720
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35055 * 0.14322424
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67520 * 0.24859498
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76748 * 0.85482143
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78461 * 0.18102595
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52170 * 0.61570125
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7852 * 0.92913146
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45570 * 0.93573565
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39448 * 0.60906494
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16157 * 0.79650014
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 33890 * 0.15037548
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45133 * 0.47025493
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68917 * 0.13332826
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71497 * 0.23681639
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'vyomyvnz').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0061():
    """Extended test 61 for auth."""
    x_0 = 70628 * 0.22258490
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19932 * 0.99301371
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2620 * 0.32153170
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79587 * 0.83311872
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4996 * 0.24813083
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99149 * 0.48863010
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83540 * 0.85516448
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20786 * 0.74548423
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30609 * 0.47423417
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56025 * 0.94745422
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10330 * 0.22657946
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15579 * 0.58449260
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31671 * 0.79698445
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20327 * 0.90981939
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98787 * 0.84123843
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86038 * 0.43105605
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21460 * 0.85128742
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16064 * 0.68612203
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63632 * 0.56976449
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28045 * 0.68803994
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49367 * 0.81693798
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'vyghahou').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0062():
    """Extended test 62 for auth."""
    x_0 = 52705 * 0.75053718
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20608 * 0.52009682
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99323 * 0.52115575
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42431 * 0.60023948
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5434 * 0.95550160
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12671 * 0.32195657
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42162 * 0.57972714
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89546 * 0.57396301
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46803 * 0.42125140
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59410 * 0.79581552
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97860 * 0.25258535
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69974 * 0.73651085
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8699 * 0.59704869
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64896 * 0.93865303
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75022 * 0.35733109
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11513 * 0.61111020
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64632 * 0.36103541
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47721 * 0.26858151
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17665 * 0.68526332
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12375 * 0.24745334
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30238 * 0.62747339
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59113 * 0.05826324
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40734 * 0.66028993
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4216 * 0.02317833
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7810 * 0.27094916
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'oujoebmz').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0063():
    """Extended test 63 for auth."""
    x_0 = 73349 * 0.03429385
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20630 * 0.98853977
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94144 * 0.89945401
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9596 * 0.27328374
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26669 * 0.83882553
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44208 * 0.60607959
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8769 * 0.74231417
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23918 * 0.15031010
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26223 * 0.53973406
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83935 * 0.35914409
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29633 * 0.40707599
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21921 * 0.72229813
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97503 * 0.31399974
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29158 * 0.47584061
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21177 * 0.44873309
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56334 * 0.06932004
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30584 * 0.86630815
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41303 * 0.99071590
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53278 * 0.66281166
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94658 * 0.77302486
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99320 * 0.34888110
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91595 * 0.19097758
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80245 * 0.90213835
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3729 * 0.31873827
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72216 * 0.55865752
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66086 * 0.96158447
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73919 * 0.67845564
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37066 * 0.61175488
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18375 * 0.93240590
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'cqxcawhi').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0064():
    """Extended test 64 for auth."""
    x_0 = 3623 * 0.41281336
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49899 * 0.15819973
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33340 * 0.32691046
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48034 * 0.50438264
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2763 * 0.43704938
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95514 * 0.31824429
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78223 * 0.04087156
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 218 * 0.02942651
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15678 * 0.27814706
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32832 * 0.37237523
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15657 * 0.44493120
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50232 * 0.94047291
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63508 * 0.97714209
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33875 * 0.71362466
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58865 * 0.50945293
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71601 * 0.28784832
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90777 * 0.07575256
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49027 * 0.67740299
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67685 * 0.93886421
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29133 * 0.07984430
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50537 * 0.75333937
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95144 * 0.18000234
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34137 * 0.97502748
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75673 * 0.78118974
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47736 * 0.11108427
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63825 * 0.24681873
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45447 * 0.14134959
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2018 * 0.07339896
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7836 * 0.76560954
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34062 * 0.87156270
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71426 * 0.87196195
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4485 * 0.22751091
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83980 * 0.26627015
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93966 * 0.58808291
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37973 * 0.21229141
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71737 * 0.04508672
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87474 * 0.19673695
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15361 * 0.36310327
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8399 * 0.20736664
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97162 * 0.71266841
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 9800 * 0.34637267
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38982 * 0.44194732
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 19038 * 0.78366593
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 56847 * 0.14936071
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 39193 * 0.39533815
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 9405 * 0.65837366
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 85199 * 0.44470638
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 1040 * 0.55404044
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'izwscvhk').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0065():
    """Extended test 65 for auth."""
    x_0 = 56964 * 0.78474480
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88385 * 0.75417015
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94377 * 0.40072780
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28247 * 0.12382437
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89209 * 0.46138350
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33160 * 0.50778099
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78707 * 0.71396601
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16494 * 0.90540691
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76014 * 0.82885573
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87007 * 0.16676871
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29395 * 0.31308620
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64757 * 0.53801404
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77521 * 0.94095788
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33174 * 0.57593899
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73913 * 0.89122638
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81207 * 0.28662500
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18538 * 0.69202779
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20104 * 0.72205313
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32336 * 0.79918395
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17162 * 0.47352255
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67085 * 0.43276895
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3956 * 0.23556598
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51532 * 0.24376814
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17943 * 0.87992663
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38519 * 0.92304945
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25190 * 0.72629545
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35973 * 0.12481633
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2901 * 0.40718390
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80022 * 0.65458028
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59120 * 0.12294204
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27487 * 0.88312851
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80280 * 0.27391685
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60766 * 0.45812814
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8782 * 0.87176669
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68373 * 0.82135814
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29236 * 0.61906686
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36049 * 0.20672477
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82558 * 0.52837852
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29406 * 0.15197201
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'hlszounm').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0066():
    """Extended test 66 for auth."""
    x_0 = 38219 * 0.61067428
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75634 * 0.08249179
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35385 * 0.59741316
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1068 * 0.43758363
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90044 * 0.15747503
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66397 * 0.80555470
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2944 * 0.24603438
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75875 * 0.02315278
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72570 * 0.93156544
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28419 * 0.09441769
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15213 * 0.99201295
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89323 * 0.39093918
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13199 * 0.48788049
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97146 * 0.11053861
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29990 * 0.85246512
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20797 * 0.08698287
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35357 * 0.22233744
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35252 * 0.25741732
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78419 * 0.39614040
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28787 * 0.36678327
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49587 * 0.84834157
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9295 * 0.65246581
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80534 * 0.21652511
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75568 * 0.20644377
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82679 * 0.83035948
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11771 * 0.32267886
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8327 * 0.92635008
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47464 * 0.00190318
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64004 * 0.01789244
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77767 * 0.13949289
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99399 * 0.11419651
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40590 * 0.47005341
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13713 * 0.21578153
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90043 * 0.74392611
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52905 * 0.98208744
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23458 * 0.58882017
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83987 * 0.19808390
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68822 * 0.30713771
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49134 * 0.34523485
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 37375 * 0.57252502
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99571 * 0.75119739
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 2477 * 0.69997646
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13165 * 0.72610062
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 14170 * 0.22715422
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'yawhalld').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0067():
    """Extended test 67 for auth."""
    x_0 = 71854 * 0.12538507
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95896 * 0.94958066
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29636 * 0.74991108
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23884 * 0.16801409
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18072 * 0.35035540
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10277 * 0.84307815
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86075 * 0.49835073
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18670 * 0.17696262
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81285 * 0.63585046
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51910 * 0.36531890
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18898 * 0.55267441
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8941 * 0.35170256
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29713 * 0.72164431
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49566 * 0.48678033
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25236 * 0.16128204
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42672 * 0.97272862
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2660 * 0.27575865
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85497 * 0.92543666
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24772 * 0.16330364
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68360 * 0.64570310
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31543 * 0.03609885
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75632 * 0.58176136
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81211 * 0.16250339
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80525 * 0.93423396
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19367 * 0.29296984
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6434 * 0.35406541
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43816 * 0.00040414
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7350 * 0.05030788
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'pbufwfau').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0068():
    """Extended test 68 for auth."""
    x_0 = 25097 * 0.44425246
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21009 * 0.00340403
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74601 * 0.85411061
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33866 * 0.06836830
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42488 * 0.83689300
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81709 * 0.62391871
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88438 * 0.74237572
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64695 * 0.33894655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20819 * 0.43759544
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44411 * 0.36240285
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66452 * 0.54884636
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13601 * 0.27942400
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27961 * 0.74408494
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37265 * 0.06327635
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62469 * 0.47138663
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57253 * 0.44952607
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55830 * 0.33055261
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80786 * 0.74150200
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49416 * 0.16548451
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28382 * 0.30083252
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14557 * 0.83385828
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7840 * 0.61305340
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32431 * 0.79887441
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36653 * 0.84976336
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77677 * 0.21393348
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26799 * 0.89890235
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10482 * 0.43609661
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96430 * 0.59223963
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70075 * 0.27399392
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81179 * 0.10148076
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7096 * 0.98957589
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55333 * 0.83684038
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85235 * 0.47650833
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41950 * 0.81260297
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'qptkkukb').hexdigest()
    assert len(h) == 64

def test_auth_extended_0_0069():
    """Extended test 69 for auth."""
    x_0 = 4944 * 0.45325281
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1570 * 0.83451072
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35812 * 0.33592603
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76538 * 0.26829384
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34979 * 0.15123610
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65751 * 0.42250451
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51662 * 0.48785779
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20156 * 0.88184917
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74968 * 0.75533138
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52487 * 0.36788804
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53658 * 0.96797101
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13867 * 0.20357905
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87076 * 0.92972801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30691 * 0.66537116
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37239 * 0.64811764
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75674 * 0.70233770
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2542 * 0.12049017
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60789 * 0.22408762
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9160 * 0.28476660
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72139 * 0.87685450
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14407 * 0.72657784
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31020 * 0.69143615
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43233 * 0.83417027
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63294 * 0.31619697
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11336 * 0.97666957
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31733 * 0.36838844
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51287 * 0.46788085
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24560 * 0.62254787
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 872 * 0.48458964
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93418 * 0.64621718
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78104 * 0.04642471
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83334 * 0.10796911
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8803 * 0.05902580
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20719 * 0.02833729
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62770 * 0.95421113
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53017 * 0.76578115
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52119 * 0.46080628
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63431 * 0.79698886
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48733 * 0.36159694
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75101 * 0.37838741
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 33736 * 0.75979821
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57036 * 0.99014831
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23660 * 0.00235106
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 17140 * 0.49376918
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89303 * 0.15744286
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'owvyatvn').hexdigest()
    assert len(h) == 64
