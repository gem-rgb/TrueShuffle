"""Extended tests for billing suite 6."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_billing_extended_6_0000():
    """Extended test 0 for billing."""
    x_0 = 1317 * 0.32819971
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28191 * 0.56380648
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18937 * 0.36407694
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1188 * 0.88426149
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33965 * 0.76221793
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53358 * 0.04954146
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42109 * 0.19828000
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25986 * 0.70408736
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29262 * 0.03836682
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68867 * 0.67482324
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50323 * 0.91659702
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52854 * 0.83223071
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38595 * 0.84549449
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57963 * 0.98950215
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74156 * 0.05675191
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14392 * 0.14419947
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16495 * 0.07150787
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8205 * 0.38671898
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98157 * 0.36915991
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19010 * 0.86935877
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76483 * 0.74023211
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91147 * 0.41643761
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67981 * 0.84785237
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'fismsxlh').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0001():
    """Extended test 1 for billing."""
    x_0 = 68470 * 0.66964076
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97580 * 0.61148147
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25247 * 0.02102479
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37927 * 0.03939788
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 193 * 0.47122130
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31235 * 0.89727066
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72341 * 0.66699910
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44570 * 0.57317667
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4573 * 0.62419563
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82498 * 0.89546427
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40300 * 0.65480035
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12959 * 0.87099934
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66606 * 0.38484242
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77775 * 0.59746914
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47935 * 0.57916513
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63970 * 0.46400921
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36488 * 0.95211831
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65794 * 0.06429325
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15590 * 0.85967352
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61059 * 0.43952721
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15754 * 0.86228971
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83074 * 0.73691589
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75554 * 0.71712359
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28612 * 0.32919004
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66567 * 0.71587177
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29064 * 0.40450810
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84610 * 0.26163432
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32778 * 0.12395871
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47008 * 0.62931464
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66790 * 0.27758678
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87811 * 0.11618350
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'slbweate').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0002():
    """Extended test 2 for billing."""
    x_0 = 12072 * 0.00417294
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82635 * 0.05394765
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1675 * 0.14003468
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44120 * 0.62326140
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27591 * 0.14672482
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11237 * 0.58176276
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56932 * 0.82970148
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27632 * 0.09915159
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75668 * 0.57416659
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1537 * 0.58786073
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53441 * 0.45067092
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84863 * 0.70836393
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97922 * 0.76509969
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69522 * 0.18957270
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2757 * 0.48696323
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48579 * 0.23551021
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73138 * 0.29544128
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54155 * 0.44575387
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18487 * 0.07829233
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43223 * 0.06682366
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75447 * 0.52184478
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89521 * 0.41937136
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38786 * 0.66388665
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45852 * 0.34632199
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38609 * 0.07071962
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44334 * 0.97736056
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92796 * 0.62349760
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80452 * 0.21698268
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75616 * 0.57619337
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23822 * 0.76760288
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25134 * 0.13795361
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21220 * 0.31180126
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37991 * 0.05065421
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34158 * 0.89406721
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64294 * 0.18808109
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30742 * 0.92328005
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5113 * 0.65045667
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20937 * 0.37055516
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87499 * 0.61106267
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67188 * 0.85138257
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 66557 * 0.24256383
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70068 * 0.36556928
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75404 * 0.35449352
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 490 * 0.48230383
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 62804 * 0.89314433
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'lpzhgqxk').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0003():
    """Extended test 3 for billing."""
    x_0 = 66137 * 0.51315509
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33160 * 0.42210991
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16281 * 0.99016021
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65228 * 0.72380629
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56040 * 0.24807361
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42019 * 0.38807274
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69726 * 0.04301718
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94651 * 0.53391562
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30339 * 0.66109283
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28206 * 0.16141747
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22897 * 0.33560150
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81484 * 0.15768752
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98646 * 0.70435272
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45644 * 0.56961368
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95197 * 0.71855890
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87595 * 0.67222770
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20242 * 0.71921426
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22912 * 0.59173862
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71108 * 0.40794040
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34117 * 0.22725023
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17964 * 0.77927687
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99696 * 0.94711912
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98315 * 0.12293719
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74336 * 0.33385012
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1213 * 0.82590923
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65131 * 0.53591344
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62194 * 0.46791276
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'cybaefta').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0004():
    """Extended test 4 for billing."""
    x_0 = 91451 * 0.74656803
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42730 * 0.91729321
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8778 * 0.44746984
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4159 * 0.44343815
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14808 * 0.48943859
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79730 * 0.13490297
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87365 * 0.22093921
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43187 * 0.72793440
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27441 * 0.48324540
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32363 * 0.48105863
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78501 * 0.78636451
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81557 * 0.30492960
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28504 * 0.09087392
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92012 * 0.26965450
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22197 * 0.36892040
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28714 * 0.02173082
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91938 * 0.84924519
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62956 * 0.03516101
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95625 * 0.74326787
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55181 * 0.03201207
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45102 * 0.98653824
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1832 * 0.37151115
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6365 * 0.72380260
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98655 * 0.09424484
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81762 * 0.21152152
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76951 * 0.75145592
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69488 * 0.70204183
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59239 * 0.94091555
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65122 * 0.69141940
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43675 * 0.50589528
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'vcxczpxo').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0005():
    """Extended test 5 for billing."""
    x_0 = 4193 * 0.14139794
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57640 * 0.35810089
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94761 * 0.34432174
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77907 * 0.97902997
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45363 * 0.19274879
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25809 * 0.24011872
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46629 * 0.93959011
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85440 * 0.06021717
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72752 * 0.08764857
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15356 * 0.63319400
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52418 * 0.82969020
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79636 * 0.05861173
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3475 * 0.07964999
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75677 * 0.70254808
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91305 * 0.99291918
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35883 * 0.06717947
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99005 * 0.94196166
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54752 * 0.18909218
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69127 * 0.39154042
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51427 * 0.62215078
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72318 * 0.34369141
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42250 * 0.30562604
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76902 * 0.21600592
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4030 * 0.47881382
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83397 * 0.00916377
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29319 * 0.49138768
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59819 * 0.00351517
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25938 * 0.90817864
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84219 * 0.40201480
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64338 * 0.30256081
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25121 * 0.96867941
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47968 * 0.57424444
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36761 * 0.94367764
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26222 * 0.28564788
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32255 * 0.45981903
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42805 * 0.13396715
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22186 * 0.88827704
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47423 * 0.78599940
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47224 * 0.47622131
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90367 * 0.15915258
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77460 * 0.09214862
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16870 * 0.36338424
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 68944 * 0.20793833
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 41649 * 0.01839672
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 9049 * 0.76179256
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 64355 * 0.43537842
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'wuygalcr').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0006():
    """Extended test 6 for billing."""
    x_0 = 40141 * 0.88749780
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38770 * 0.55981899
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33054 * 0.48099217
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46398 * 0.82064526
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84448 * 0.66412440
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19041 * 0.91037963
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29937 * 0.66532441
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34431 * 0.16002699
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76412 * 0.76988536
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94575 * 0.32671202
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85887 * 0.01142314
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38557 * 0.13833465
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86262 * 0.98889897
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82196 * 0.15124368
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89393 * 0.51926697
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87194 * 0.30939362
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53994 * 0.30040056
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91523 * 0.18842478
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37379 * 0.02227321
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60372 * 0.73402481
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23764 * 0.58638455
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30069 * 0.45576970
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39704 * 0.75102886
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75195 * 0.88149226
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29632 * 0.33222040
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60015 * 0.54007816
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22663 * 0.73025883
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62380 * 0.39457718
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61638 * 0.91815308
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18803 * 0.14177127
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47206 * 0.43563371
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27076 * 0.32345053
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32648 * 0.92542088
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65438 * 0.21199835
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48612 * 0.23714548
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56665 * 0.66592412
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29741 * 0.23023113
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52790 * 0.08949592
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12374 * 0.18370921
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8656 * 0.95601998
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43892 * 0.48108820
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9149 * 0.56718717
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 298 * 0.52289349
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'bdtvppll').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0007():
    """Extended test 7 for billing."""
    x_0 = 5390 * 0.67854125
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50875 * 0.55343118
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34161 * 0.68405746
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88421 * 0.57137620
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51140 * 0.23074610
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64009 * 0.95249440
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28616 * 0.77290099
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84941 * 0.09616060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68652 * 0.91465846
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5356 * 0.99117770
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99569 * 0.19847456
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78732 * 0.59914399
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95672 * 0.15596911
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95649 * 0.02506816
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63156 * 0.41037816
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61546 * 0.46737661
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20269 * 0.13423327
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99254 * 0.55732442
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65607 * 0.58581685
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75664 * 0.52540440
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77257 * 0.52102385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22689 * 0.36830735
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65666 * 0.59915257
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16906 * 0.05146817
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ifkvlhwq').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0008():
    """Extended test 8 for billing."""
    x_0 = 43939 * 0.17505112
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87931 * 0.59042045
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86535 * 0.73719192
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71736 * 0.04161761
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40937 * 0.43183847
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24145 * 0.70714040
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80842 * 0.90758614
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2843 * 0.05994511
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6546 * 0.63576075
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6152 * 0.94583170
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60603 * 0.57080154
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53568 * 0.46223019
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92110 * 0.50632090
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61067 * 0.69974188
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5396 * 0.02431833
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22367 * 0.72240294
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65834 * 0.63743066
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22821 * 0.45046378
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1949 * 0.72128855
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80109 * 0.14176516
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77276 * 0.70953156
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'zvkwbplj').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0009():
    """Extended test 9 for billing."""
    x_0 = 56956 * 0.72950144
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84670 * 0.46285420
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36945 * 0.01410221
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43087 * 0.23209655
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81931 * 0.65098133
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2705 * 0.75448002
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38733 * 0.16904616
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78195 * 0.65550899
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73114 * 0.85677381
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50347 * 0.66410791
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71320 * 0.47634664
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77455 * 0.48491907
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45714 * 0.08102629
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48604 * 0.65072908
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58767 * 0.98659006
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28137 * 0.34611671
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9695 * 0.36584551
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60819 * 0.60100125
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49968 * 0.14190305
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9991 * 0.02420333
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74054 * 0.98279208
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36773 * 0.02344296
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67147 * 0.01371287
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53340 * 0.56263510
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45532 * 0.92952264
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37146 * 0.50450165
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48051 * 0.21858781
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'uonfseql').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0010():
    """Extended test 10 for billing."""
    x_0 = 88894 * 0.90077245
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17888 * 0.64093014
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89623 * 0.19958712
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91622 * 0.76458120
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20492 * 0.11007757
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12996 * 0.21782696
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27758 * 0.08604297
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39763 * 0.76341902
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46132 * 0.70934228
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22141 * 0.98393144
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84836 * 0.89529429
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20995 * 0.35851749
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80426 * 0.00528135
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46012 * 0.85049641
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62508 * 0.74208431
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88899 * 0.23477203
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35932 * 0.28773767
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5686 * 0.72796724
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39696 * 0.37492591
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59540 * 0.19236124
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34670 * 0.03389029
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3989 * 0.10157668
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72745 * 0.29574242
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'wwlluhka').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0011():
    """Extended test 11 for billing."""
    x_0 = 728 * 0.25938145
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94182 * 0.73111073
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3254 * 0.33657826
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24792 * 0.30144530
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97257 * 0.06234127
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7927 * 0.05581850
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55939 * 0.60397282
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69815 * 0.28638949
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44736 * 0.33223980
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14675 * 0.01690540
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5391 * 0.17590538
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57658 * 0.30179845
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21872 * 0.24009174
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45991 * 0.95441604
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27505 * 0.33679544
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37412 * 0.73125552
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39638 * 0.14542839
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44665 * 0.34057127
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69504 * 0.83993153
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36992 * 0.08447107
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27907 * 0.94740561
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54556 * 0.11207977
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13575 * 0.75326603
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73688 * 0.83472136
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77164 * 0.40961811
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66922 * 0.33705087
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15899 * 0.67404944
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58630 * 0.27197048
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98158 * 0.67991145
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16099 * 0.41945401
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75915 * 0.07196375
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57170 * 0.38264394
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78814 * 0.90976246
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81921 * 0.71016471
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77263 * 0.10452293
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13700 * 0.36219548
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8721 * 0.32254543
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75107 * 0.14232656
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9009 * 0.95691595
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23714 * 0.13845568
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53957 * 0.17997547
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80247 * 0.62133020
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24014 * 0.23883090
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 16318 * 0.56409464
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 32537 * 0.34387485
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 34443 * 0.50563461
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 46402 * 0.63358780
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'lsncdyui').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0012():
    """Extended test 12 for billing."""
    x_0 = 60991 * 0.63327082
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35815 * 0.63205799
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65277 * 0.17554190
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27415 * 0.92296147
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41981 * 0.27927970
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47702 * 0.23624498
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40633 * 0.86671511
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4914 * 0.91525162
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59613 * 0.87174849
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42307 * 0.38526888
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46110 * 0.82068084
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12361 * 0.06562765
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9438 * 0.52675946
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62344 * 0.04124663
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21691 * 0.44564740
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83176 * 0.73437119
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94624 * 0.83584077
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5604 * 0.00903093
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62601 * 0.80552028
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50463 * 0.95790695
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68845 * 0.38775788
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19896 * 0.30106242
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72693 * 0.04390199
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93961 * 0.80074167
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31709 * 0.43187687
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24712 * 0.48005550
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36639 * 0.40882345
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'obftzceb').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0013():
    """Extended test 13 for billing."""
    x_0 = 12435 * 0.09195727
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27936 * 0.90726613
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75029 * 0.18392455
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7740 * 0.62122425
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61395 * 0.88300322
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23696 * 0.90963901
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56185 * 0.94902495
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51541 * 0.24459751
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32538 * 0.49811164
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20563 * 0.87722093
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67155 * 0.57931032
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88294 * 0.25622644
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45228 * 0.32935800
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30734 * 0.52007494
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21539 * 0.36851713
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19890 * 0.38657660
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75267 * 0.57014928
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79205 * 0.03534405
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41293 * 0.93786738
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84090 * 0.99447090
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32342 * 0.09838140
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91250 * 0.48393690
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11984 * 0.57051582
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14940 * 0.60244891
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87730 * 0.23368724
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93982 * 0.13336869
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56829 * 0.48292781
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3393 * 0.70407279
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12441 * 0.39944915
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61660 * 0.48697448
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38174 * 0.89162235
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51929 * 0.73318613
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47399 * 0.47163604
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88827 * 0.38220048
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'gwujvtne').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0014():
    """Extended test 14 for billing."""
    x_0 = 27518 * 0.70007144
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70720 * 0.48204074
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32373 * 0.94595670
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64668 * 0.25999594
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59661 * 0.65035643
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85289 * 0.61302777
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20773 * 0.33171590
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61466 * 0.38210752
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67130 * 0.88090725
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30888 * 0.01421438
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87011 * 0.01295096
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43143 * 0.32554774
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25313 * 0.60716038
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52236 * 0.37139547
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19556 * 0.16961799
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64664 * 0.02247983
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79241 * 0.16981846
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64059 * 0.43655319
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49205 * 0.52820841
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70431 * 0.89189703
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25302 * 0.86479886
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47683 * 0.63223816
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83226 * 0.64041754
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87447 * 0.22852102
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69994 * 0.46123912
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21763 * 0.89279169
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24791 * 0.20268995
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72208 * 0.07253337
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2508 * 0.07912893
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25017 * 0.02238657
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11484 * 0.16519448
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84874 * 0.13252651
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37665 * 0.13964061
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60079 * 0.28537743
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84319 * 0.29747661
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41402 * 0.95609352
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75942 * 0.72392911
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98438 * 0.56294667
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20811 * 0.80604922
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8677 * 0.13275405
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 57095 * 0.20511762
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88195 * 0.60327487
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95402 * 0.77313740
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58171 * 0.80249318
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 21124 * 0.33338718
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 22353 * 0.36184884
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 37728 * 0.20730067
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 49238 * 0.91118956
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 41155 * 0.27213267
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'gvvtkvye').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0015():
    """Extended test 15 for billing."""
    x_0 = 58230 * 0.79613589
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97915 * 0.57948179
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25124 * 0.82078401
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79161 * 0.07249086
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50721 * 0.55987340
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65506 * 0.60090804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41608 * 0.55343554
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99288 * 0.42485007
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87338 * 0.39022140
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84784 * 0.54419314
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60615 * 0.05989844
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60360 * 0.88540864
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96684 * 0.12581811
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79025 * 0.81122485
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42663 * 0.21786738
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73011 * 0.78589926
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86098 * 0.62771018
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55549 * 0.54558548
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10590 * 0.85514183
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99976 * 0.91025752
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79662 * 0.43849180
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ennxxwim').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0016():
    """Extended test 16 for billing."""
    x_0 = 37775 * 0.51753623
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93495 * 0.98509158
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13051 * 0.39767699
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64695 * 0.77099488
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92645 * 0.96122010
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11205 * 0.65618698
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58763 * 0.49170121
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56724 * 0.97731693
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33839 * 0.16343987
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35151 * 0.19805754
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96003 * 0.54756203
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92962 * 0.74172328
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3753 * 0.96656604
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10985 * 0.04326888
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94310 * 0.72438281
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64905 * 0.24672081
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21246 * 0.17256991
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89408 * 0.74353694
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64294 * 0.17603642
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5127 * 0.41413596
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31953 * 0.58559328
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10327 * 0.22597036
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84117 * 0.13591599
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72256 * 0.24308027
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54713 * 0.33915760
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23557 * 0.80895813
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93137 * 0.86478255
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51827 * 0.06066135
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10800 * 0.25028479
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26395 * 0.04648011
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95756 * 0.38001306
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82072 * 0.02631092
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92199 * 0.60635823
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88939 * 0.85463439
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7849 * 0.32500771
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95214 * 0.06007703
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95782 * 0.72210615
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'umznmbpn').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0017():
    """Extended test 17 for billing."""
    x_0 = 29949 * 0.17390405
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87459 * 0.78721146
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11299 * 0.98630169
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88964 * 0.34971502
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19106 * 0.04192997
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6054 * 0.33530896
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23423 * 0.24132926
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21315 * 0.32476856
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44970 * 0.30682676
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86727 * 0.23192109
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17272 * 0.09447620
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74744 * 0.14626182
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50172 * 0.62900585
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93194 * 0.59085638
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94136 * 0.11669495
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26292 * 0.70007426
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96644 * 0.37179348
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11812 * 0.10977350
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65605 * 0.72820818
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51349 * 0.15024226
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24512 * 0.43290576
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80164 * 0.35420819
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1648 * 0.51382564
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21926 * 0.33187458
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71363 * 0.73738198
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19887 * 0.19294377
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35028 * 0.72658696
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83763 * 0.15359337
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26689 * 0.47747712
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21222 * 0.40445678
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23402 * 0.51039354
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40680 * 0.29687684
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73429 * 0.04518939
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13163 * 0.20039129
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10836 * 0.85602251
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 9008 * 0.17640613
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44084 * 0.52675887
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'frufxurj').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0018():
    """Extended test 18 for billing."""
    x_0 = 58068 * 0.83104973
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71005 * 0.42605673
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90542 * 0.36389023
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80342 * 0.57065113
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45066 * 0.54341327
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33421 * 0.94369096
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62725 * 0.28840200
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49483 * 0.61116274
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18718 * 0.92283754
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4109 * 0.01183223
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18431 * 0.19484831
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15843 * 0.74375495
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5101 * 0.55069723
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89822 * 0.67579604
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90771 * 0.07394100
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17107 * 0.55614191
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6787 * 0.74731386
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94171 * 0.91986045
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50202 * 0.66466397
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93455 * 0.74830975
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58577 * 0.12397333
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79212 * 0.45123459
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24774 * 0.33517308
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1917 * 0.95251511
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95821 * 0.65560381
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18818 * 0.80003829
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36751 * 0.92958097
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12051 * 0.75331809
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7163 * 0.98198069
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8784 * 0.10446651
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40703 * 0.17582541
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27287 * 0.68328270
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6090 * 0.11970534
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36864 * 0.88259240
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'piqiyjhi').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0019():
    """Extended test 19 for billing."""
    x_0 = 147 * 0.97682886
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18075 * 0.76422657
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79878 * 0.58129439
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27388 * 0.98670803
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12510 * 0.44260195
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4890 * 0.91242566
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63932 * 0.12790430
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83862 * 0.39697419
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37161 * 0.05349749
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13567 * 0.30318238
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11688 * 0.90923199
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19909 * 0.05722211
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56374 * 0.20389067
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12139 * 0.65207281
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56707 * 0.09589340
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69168 * 0.29396266
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22888 * 0.63198111
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11331 * 0.71634168
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83747 * 0.72125083
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26440 * 0.04192324
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64113 * 0.38181649
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53333 * 0.16626739
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15523 * 0.98568045
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9090 * 0.82985038
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65008 * 0.04145739
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14932 * 0.13735022
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43290 * 0.03032582
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29153 * 0.82460798
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35707 * 0.23375985
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64086 * 0.02654805
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83379 * 0.49603462
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12963 * 0.63466470
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65140 * 0.05873187
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24665 * 0.51588686
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81381 * 0.18508386
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27791 * 0.78954180
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67576 * 0.63202953
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77397 * 0.79155285
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98219 * 0.91706521
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86957 * 0.13495947
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84311 * 0.92271840
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9118 * 0.44861624
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 72703 * 0.92693044
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'pngbejey').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0020():
    """Extended test 20 for billing."""
    x_0 = 80238 * 0.83938829
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99473 * 0.00532257
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29594 * 0.69687265
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4336 * 0.08721712
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63558 * 0.27529224
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61754 * 0.79194453
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18978 * 0.57882353
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59344 * 0.39396525
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55848 * 0.84999618
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96079 * 0.05815130
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29274 * 0.45587399
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68746 * 0.36876831
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36026 * 0.57748702
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24894 * 0.42215854
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94189 * 0.22698408
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36397 * 0.03221430
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56021 * 0.29629999
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89255 * 0.88706938
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48486 * 0.46139691
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34594 * 0.10564248
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79174 * 0.73698569
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21435 * 0.75216335
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 459 * 0.04599002
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41223 * 0.25427015
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19425 * 0.33312634
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87792 * 0.34325751
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88868 * 0.30494451
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67614 * 0.36545071
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5800 * 0.86450194
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82618 * 0.21943046
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62517 * 0.16711341
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74528 * 0.00382495
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41847 * 0.79977634
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17800 * 0.03489390
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63230 * 0.58843112
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61023 * 0.82817429
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80328 * 0.38005528
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62303 * 0.00650425
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56770 * 0.20560175
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24328 * 0.18064873
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23254 * 0.49256446
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 98639 * 0.39969959
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 80574 * 0.54952770
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22606 * 0.52984634
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 31635 * 0.35358128
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'wfpuhamn').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0021():
    """Extended test 21 for billing."""
    x_0 = 60943 * 0.15242981
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19642 * 0.58167665
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41561 * 0.94756344
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32650 * 0.64926017
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37693 * 0.99638968
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2225 * 0.58718169
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39622 * 0.74656978
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24628 * 0.56447062
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42900 * 0.66090364
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52873 * 0.51638120
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88246 * 0.58335878
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39913 * 0.45618300
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63824 * 0.09975175
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87187 * 0.45350049
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80715 * 0.39972668
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70524 * 0.34747256
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70789 * 0.85668106
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49281 * 0.00097420
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86111 * 0.11535339
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79910 * 0.47576633
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 821 * 0.65919605
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'uskingzw').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0022():
    """Extended test 22 for billing."""
    x_0 = 87517 * 0.82391651
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2788 * 0.09256377
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44869 * 0.45814899
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87054 * 0.33864387
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12177 * 0.59555484
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80811 * 0.89610463
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74012 * 0.12001945
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32056 * 0.34092389
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59926 * 0.45239841
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90293 * 0.30233876
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47535 * 0.64273656
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47112 * 0.83495083
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66668 * 0.01563802
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74715 * 0.80454917
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86638 * 0.47122835
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37733 * 0.98664919
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85156 * 0.76609166
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30428 * 0.32515895
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93994 * 0.85704337
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76740 * 0.83512049
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47764 * 0.98302972
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72856 * 0.49728442
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66619 * 0.53133870
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47334 * 0.72774487
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'rpteljco').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0023():
    """Extended test 23 for billing."""
    x_0 = 90030 * 0.51282717
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58487 * 0.94875280
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92796 * 0.96946291
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73017 * 0.69268151
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34721 * 0.93391404
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68071 * 0.43951327
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32485 * 0.23007169
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81973 * 0.64784738
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31928 * 0.60528397
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58325 * 0.03377582
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9305 * 0.17705944
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3967 * 0.13424841
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70342 * 0.22778438
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52243 * 0.97569197
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64543 * 0.02611002
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78587 * 0.69824048
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97090 * 0.33051864
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39092 * 0.40718926
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48227 * 0.82064649
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20803 * 0.38251785
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56685 * 0.48444441
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69223 * 0.44341787
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62831 * 0.78535402
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30713 * 0.80944917
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97256 * 0.11322758
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89329 * 0.39938910
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10849 * 0.62094612
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'glnkkczy').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0024():
    """Extended test 24 for billing."""
    x_0 = 64090 * 0.71035339
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36716 * 0.34894766
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79808 * 0.24036031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10053 * 0.99595383
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76525 * 0.21865472
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57264 * 0.38905875
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8857 * 0.45138944
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46198 * 0.08051794
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41138 * 0.23949915
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89065 * 0.81774974
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83484 * 0.32867514
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87873 * 0.14956330
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78824 * 0.34141889
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17170 * 0.71769525
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3965 * 0.18008317
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18 * 0.67808309
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46193 * 0.59655438
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41655 * 0.32391836
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18369 * 0.29031479
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55536 * 0.82083429
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67123 * 0.61263188
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11733 * 0.77952151
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26324 * 0.88353479
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89349 * 0.65833931
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76084 * 0.49237191
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 697 * 0.24955883
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11163 * 0.96197108
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83930 * 0.18373452
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8282 * 0.61688243
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'wspeqepo').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0025():
    """Extended test 25 for billing."""
    x_0 = 43653 * 0.60129509
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11557 * 0.43548544
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55389 * 0.95440148
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35551 * 0.28325181
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94324 * 0.14765509
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80878 * 0.97125953
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46349 * 0.80977798
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13820 * 0.50245249
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56982 * 0.73010483
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36105 * 0.04238297
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64205 * 0.75090375
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44868 * 0.72708945
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27836 * 0.80822436
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53048 * 0.34691542
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75309 * 0.52283896
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71385 * 0.50662892
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98535 * 0.71769331
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78917 * 0.05671850
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6678 * 0.35857390
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54136 * 0.09366276
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74670 * 0.48898852
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92374 * 0.64703718
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51737 * 0.71418582
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40236 * 0.72298552
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28790 * 0.98956051
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43669 * 0.92828479
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24522 * 0.67581262
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84711 * 0.97798516
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48920 * 0.87790850
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77746 * 0.17669717
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23878 * 0.01123345
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91605 * 0.01797613
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25107 * 0.57455578
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85101 * 0.08585239
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62103 * 0.42649105
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79681 * 0.75254624
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91364 * 0.39533722
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27464 * 0.16244021
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87853 * 0.98798948
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1788 * 0.49362022
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19459 * 0.77286152
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63445 * 0.62093398
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9056 * 0.26937465
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22922 * 0.02028446
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 42088 * 0.28195032
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'vczmwxzb').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0026():
    """Extended test 26 for billing."""
    x_0 = 71257 * 0.01047125
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54060 * 0.20256961
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57670 * 0.26385229
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40818 * 0.92789789
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61184 * 0.83033108
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85304 * 0.94202119
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27418 * 0.52756578
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20028 * 0.04082672
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2244 * 0.88595176
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48645 * 0.10755729
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64483 * 0.42861909
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32905 * 0.33268285
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68027 * 0.35609423
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52836 * 0.63603265
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91500 * 0.50818645
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47894 * 0.01898149
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84692 * 0.10581738
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29770 * 0.77170711
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92905 * 0.34983108
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58603 * 0.76566193
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16617 * 0.32933033
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73962 * 0.87900895
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34608 * 0.64897297
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20964 * 0.98944642
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9227 * 0.17481120
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75530 * 0.27622225
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16976 * 0.99269530
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11910 * 0.60117964
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46024 * 0.98315301
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17676 * 0.15251531
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73608 * 0.70861846
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68009 * 0.62554294
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63170 * 0.95793436
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'jznxjjwi').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0027():
    """Extended test 27 for billing."""
    x_0 = 84816 * 0.33763067
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65448 * 0.50383772
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15942 * 0.78995104
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96315 * 0.10815723
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95679 * 0.83591428
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64784 * 0.07227371
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55629 * 0.66527969
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40617 * 0.92956997
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32292 * 0.66382972
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93331 * 0.33828451
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28265 * 0.26809079
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27417 * 0.66214565
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50954 * 0.08180267
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20660 * 0.13594511
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19860 * 0.93765862
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11214 * 0.56140936
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89388 * 0.16763869
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44400 * 0.42967603
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90544 * 0.74502352
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41555 * 0.87716689
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69070 * 0.26968057
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4602 * 0.02486815
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36377 * 0.39361429
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81156 * 0.97198695
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94469 * 0.94821047
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7209 * 0.16480146
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28551 * 0.97589400
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20715 * 0.79759991
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93857 * 0.98948203
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53272 * 0.91617030
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77738 * 0.12438786
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19796 * 0.04575634
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21313 * 0.83151938
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80586 * 0.82736501
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62169 * 0.27965557
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56959 * 0.73506190
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33223 * 0.52503997
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52636 * 0.41297947
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18249 * 0.89419431
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95361 * 0.62168070
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 25205 * 0.08757473
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 24805 * 0.27229710
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9931 * 0.09001756
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'oqcrlhlh').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0028():
    """Extended test 28 for billing."""
    x_0 = 66515 * 0.97134330
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65698 * 0.74603851
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44297 * 0.42312565
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80554 * 0.71065773
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69727 * 0.59379104
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92744 * 0.36861284
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25547 * 0.19938384
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44795 * 0.90707280
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25803 * 0.42467301
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97717 * 0.86083000
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17925 * 0.25656852
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20616 * 0.11102674
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52842 * 0.59478353
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7390 * 0.59360351
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46564 * 0.84490314
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77384 * 0.28118039
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19783 * 0.53633599
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42851 * 0.48471632
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44199 * 0.09061105
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92926 * 0.50577452
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61085 * 0.12112151
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61674 * 0.80914526
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84522 * 0.15855540
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17453 * 0.09511799
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76999 * 0.62064592
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70985 * 0.25263197
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90239 * 0.49062786
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90612 * 0.36503101
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48991 * 0.94829912
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86738 * 0.93209790
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8917 * 0.48078063
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57582 * 0.41533069
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30685 * 0.11893835
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71282 * 0.26567454
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84069 * 0.27622450
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95138 * 0.16022164
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44496 * 0.80543901
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38256 * 0.89305318
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19011 * 0.62639997
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40847 * 0.63478032
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84302 * 0.54439225
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 17168 * 0.90845270
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47276 * 0.43551460
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40549 * 0.18499823
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 74179 * 0.48948855
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'caeimekw').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0029():
    """Extended test 29 for billing."""
    x_0 = 20669 * 0.19403004
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 918 * 0.36752861
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85217 * 0.91454154
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10465 * 0.17143717
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44051 * 0.33042154
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14672 * 0.43934234
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85005 * 0.85297920
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92163 * 0.38672309
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41271 * 0.78003310
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95110 * 0.02817710
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50669 * 0.70736135
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47726 * 0.93190849
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46278 * 0.98366832
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32422 * 0.84044705
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51337 * 0.64884228
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79865 * 0.82658018
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34232 * 0.34826140
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48593 * 0.88744461
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55982 * 0.28734452
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38091 * 0.60830031
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47079 * 0.34129256
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16691 * 0.74093359
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6640 * 0.82684157
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82156 * 0.09669998
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64514 * 0.30616296
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96712 * 0.25879998
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70427 * 0.83945720
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6696 * 0.28959602
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93372 * 0.44524079
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32320 * 0.00640005
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65445 * 0.65775702
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83811 * 0.91972445
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3390 * 0.83425929
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10386 * 0.99380081
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50249 * 0.90110160
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89372 * 0.56943056
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 164 * 0.41956241
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22764 * 0.46949364
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10937 * 0.53604355
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95384 * 0.97339676
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94289 * 0.87793552
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25405 * 0.98037145
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12076 * 0.60274991
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 16161 * 0.42184298
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'qaakdgsm').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0030():
    """Extended test 30 for billing."""
    x_0 = 14636 * 0.37754812
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28633 * 0.18262967
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49932 * 0.33646701
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41429 * 0.10747756
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83988 * 0.20417220
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77617 * 0.03147368
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99014 * 0.65959841
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96536 * 0.67133340
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32489 * 0.88731417
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73955 * 0.06785072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76633 * 0.98900273
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52471 * 0.50517958
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87843 * 0.34980194
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76775 * 0.82917232
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81324 * 0.37319510
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99678 * 0.42118374
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16781 * 0.32438062
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38318 * 0.10112114
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16300 * 0.75440933
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78264 * 0.02937524
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21866 * 0.85324316
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77290 * 0.20743479
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36103 * 0.42566201
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32572 * 0.89509244
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30562 * 0.36072546
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95435 * 0.60284963
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66047 * 0.22937346
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 524 * 0.11048705
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31408 * 0.93777139
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19677 * 0.70757502
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3453 * 0.95768866
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22986 * 0.55438350
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66786 * 0.14357033
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63928 * 0.15016377
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64151 * 0.88540292
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70778 * 0.41020010
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42123 * 0.83039935
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86312 * 0.39607388
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87814 * 0.72658587
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28383 * 0.01959309
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38676 * 0.36678418
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18864 * 0.74213871
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'icaghssa').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0031():
    """Extended test 31 for billing."""
    x_0 = 73577 * 0.10519914
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12617 * 0.40499376
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81963 * 0.10161996
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8793 * 0.16761621
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48987 * 0.58905004
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87981 * 0.09532009
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39410 * 0.69122313
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43052 * 0.59446567
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47700 * 0.15557761
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61774 * 0.36336692
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20218 * 0.51108204
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81817 * 0.16819840
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14321 * 0.38527007
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1917 * 0.92264394
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91677 * 0.17430549
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11854 * 0.21253594
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80981 * 0.57535555
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61785 * 0.46612654
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2217 * 0.14995933
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37559 * 0.25717669
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78024 * 0.07795336
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71141 * 0.20761821
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36413 * 0.12857023
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45590 * 0.79223447
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51828 * 0.89870531
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2649 * 0.21263939
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23381 * 0.50911201
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74080 * 0.56382931
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42494 * 0.39258362
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3870 * 0.24812549
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63416 * 0.71483448
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76685 * 0.75514416
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1218 * 0.01101670
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39848 * 0.25042284
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14611 * 0.45839617
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10636 * 0.99148116
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91520 * 0.69867270
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18720 * 0.79161032
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 233 * 0.72744155
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2424 * 0.59991789
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1134 * 0.77776289
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 17473 * 0.88510601
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 33856 * 0.49217144
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 70120 * 0.65500484
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 95846 * 0.93109667
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 31719 * 0.66782518
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 97738 * 0.03119575
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 28992 * 0.21183099
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 82749 * 0.66874017
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 362 * 0.75335989
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'jdawaydx').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0032():
    """Extended test 32 for billing."""
    x_0 = 86168 * 0.12955087
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58126 * 0.35979772
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 369 * 0.62011354
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63371 * 0.87358681
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3454 * 0.22897541
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51644 * 0.34013743
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46663 * 0.14242735
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7728 * 0.07219759
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91649 * 0.56242417
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45252 * 0.63127692
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21811 * 0.07239086
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82581 * 0.54618676
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2371 * 0.10731798
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25587 * 0.79342524
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20331 * 0.44001871
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32568 * 0.45921072
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63073 * 0.23538650
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4574 * 0.78391996
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65129 * 0.26809109
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70260 * 0.27850362
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16223 * 0.83762168
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10242 * 0.77701257
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31915 * 0.28309531
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33864 * 0.70185274
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16713 * 0.22538790
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21623 * 0.61759124
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34757 * 0.22243566
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69196 * 0.18203382
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78780 * 0.72853731
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18143 * 0.64428736
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15360 * 0.57648939
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63844 * 0.16154440
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49389 * 0.40230587
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16428 * 0.72765382
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85658 * 0.73736327
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52429 * 0.32237115
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40727 * 0.42576342
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59011 * 0.44200803
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91242 * 0.79377960
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96255 * 0.26663410
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74817 * 0.86295607
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15866 * 0.26554974
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74276 * 0.07800641
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 77083 * 0.60292262
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 45613 * 0.01711202
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 60931 * 0.17158301
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'atgprsjk').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0033():
    """Extended test 33 for billing."""
    x_0 = 12232 * 0.61046724
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68400 * 0.14763468
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71245 * 0.68578218
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57533 * 0.32724554
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84829 * 0.79760261
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43160 * 0.06588327
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57761 * 0.79775451
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51599 * 0.17289500
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35830 * 0.38219695
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91449 * 0.96593037
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63097 * 0.92833076
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83107 * 0.54656718
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21447 * 0.40487240
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54294 * 0.58758195
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62797 * 0.57573398
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33736 * 0.01228754
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52139 * 0.80166000
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85836 * 0.40140306
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16085 * 0.04926727
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9818 * 0.44646233
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46338 * 0.56477139
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48319 * 0.53325161
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94617 * 0.50856718
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85430 * 0.15228876
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20157 * 0.56090396
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64681 * 0.03095034
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79546 * 0.87272087
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11598 * 0.92756382
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50672 * 0.84195382
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'bgcjjzxd').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0034():
    """Extended test 34 for billing."""
    x_0 = 40591 * 0.92587954
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29926 * 0.06101920
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14508 * 0.13556293
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29721 * 0.93269655
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43626 * 0.84756248
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85934 * 0.89594398
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56037 * 0.01403186
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35744 * 0.69971648
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80123 * 0.56488980
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5380 * 0.10649138
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50641 * 0.82604618
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35689 * 0.32938621
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2124 * 0.35152041
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31411 * 0.25409921
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 602 * 0.88466281
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55798 * 0.10411897
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35325 * 0.21181319
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81887 * 0.44578981
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1245 * 0.07967796
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70936 * 0.87645466
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14363 * 0.65799515
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32112 * 0.41572429
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15068 * 0.36323641
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94257 * 0.10305158
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5492 * 0.39523763
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9209 * 0.53030554
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48242 * 0.59245543
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'utmipgyh').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0035():
    """Extended test 35 for billing."""
    x_0 = 33652 * 0.66268001
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3855 * 0.94862283
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21829 * 0.87297800
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21826 * 0.30263694
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26055 * 0.93102037
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41279 * 0.20839704
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52241 * 0.71694679
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53340 * 0.00700131
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61520 * 0.46148575
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40224 * 0.39767372
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71179 * 0.57552922
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76932 * 0.43865471
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96645 * 0.54671419
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80706 * 0.94223928
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1657 * 0.62816279
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3941 * 0.61648780
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46223 * 0.94168086
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93875 * 0.37958168
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38923 * 0.65970383
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73396 * 0.49948394
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42418 * 0.74848112
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13726 * 0.34215581
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71146 * 0.97354855
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20673 * 0.54901043
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68279 * 0.12014622
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28582 * 0.80794157
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41874 * 0.44049456
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44738 * 0.79774015
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12283 * 0.06330650
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56123 * 0.46242397
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66512 * 0.49712998
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62230 * 0.96132319
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41454 * 0.70692154
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13145 * 0.76375100
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50214 * 0.30771959
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'wshvrvav').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0036():
    """Extended test 36 for billing."""
    x_0 = 86202 * 0.55893400
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19433 * 0.11365718
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71239 * 0.45575334
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25898 * 0.14182433
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97445 * 0.53760888
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8883 * 0.35361689
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90204 * 0.37853595
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59068 * 0.46781357
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16958 * 0.64303187
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5507 * 0.03440187
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19433 * 0.19287186
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39899 * 0.47920307
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18671 * 0.67851242
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88429 * 0.91983097
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33456 * 0.93417837
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96019 * 0.21001067
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34341 * 0.06591996
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38929 * 0.82775009
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38742 * 0.08492986
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26946 * 0.12076184
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46749 * 0.31312507
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7973 * 0.88342912
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51313 * 0.97352055
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69981 * 0.42367703
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75438 * 0.14347854
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'gsljdafl').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0037():
    """Extended test 37 for billing."""
    x_0 = 6581 * 0.78366220
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37802 * 0.47610928
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57480 * 0.72893086
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69670 * 0.25369533
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2980 * 0.33931162
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83189 * 0.04965599
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91924 * 0.13847380
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60503 * 0.45764642
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52751 * 0.04602143
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59601 * 0.02108914
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34750 * 0.17552097
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66673 * 0.68996250
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17055 * 0.96869641
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26340 * 0.24739033
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81097 * 0.07466632
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72372 * 0.96528244
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73443 * 0.54883827
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18199 * 0.95921274
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79377 * 0.62367675
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68174 * 0.09626792
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7616 * 0.20512165
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 822 * 0.19136544
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12462 * 0.40483173
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1124 * 0.44440431
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58322 * 0.43494344
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46156 * 0.48478402
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75433 * 0.38982855
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'bymirfcf').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0038():
    """Extended test 38 for billing."""
    x_0 = 38179 * 0.88334416
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68290 * 0.58464882
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67969 * 0.85955487
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67940 * 0.61976059
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47138 * 0.40912252
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39076 * 0.78151136
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90491 * 0.98731315
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4068 * 0.85324092
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46321 * 0.71046939
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60230 * 0.43707777
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93662 * 0.45259119
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80642 * 0.65405439
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97343 * 0.00105894
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63295 * 0.49792423
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56014 * 0.42188452
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81801 * 0.39103474
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39814 * 0.90397637
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8915 * 0.97055742
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42609 * 0.59066700
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99274 * 0.80920006
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81229 * 0.53016793
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36606 * 0.83158497
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14589 * 0.62127660
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30050 * 0.29818528
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20857 * 0.81029273
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86772 * 0.52371722
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89966 * 0.89027046
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75013 * 0.22635659
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38145 * 0.98107313
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17885 * 0.89769506
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89546 * 0.03344712
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20731 * 0.35262644
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14086 * 0.00091886
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14723 * 0.68185043
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84465 * 0.32852681
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12881 * 0.74643035
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1685 * 0.33758240
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39274 * 0.63943257
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87044 * 0.55023363
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51557 * 0.52573188
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51099 * 0.59723167
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26968 * 0.73586423
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 86359 * 0.51005967
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 91932 * 0.55130405
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 33188 * 0.25328358
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 48187 * 0.80577165
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 58469 * 0.42679987
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 12674 * 0.58429286
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 26174 * 0.95270889
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'agapicdl').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0039():
    """Extended test 39 for billing."""
    x_0 = 59417 * 0.94310111
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11468 * 0.50136313
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97761 * 0.76604136
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82442 * 0.80678100
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6118 * 0.44607272
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89673 * 0.28229133
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9309 * 0.41996966
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31656 * 0.14162474
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3568 * 0.09506046
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25607 * 0.74939990
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2310 * 0.72171146
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35760 * 0.48379908
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10346 * 0.92983852
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23062 * 0.38921275
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21011 * 0.02701763
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40735 * 0.99684060
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54634 * 0.71202180
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74491 * 0.35795558
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94119 * 0.77695545
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40833 * 0.37001966
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33549 * 0.14946643
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76167 * 0.69126707
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51645 * 0.30002749
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79261 * 0.81903322
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68109 * 0.98280134
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29082 * 0.76934211
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93978 * 0.62495499
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20390 * 0.60508176
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12108 * 0.63727755
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80445 * 0.38954508
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49157 * 0.20965471
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39036 * 0.15501529
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87830 * 0.94373312
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23040 * 0.60280918
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18281 * 0.24231404
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35816 * 0.82489539
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41494 * 0.94859789
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83867 * 0.63732947
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2831 * 0.72689643
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76145 * 0.70862900
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21793 * 0.71057760
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85463 * 0.92125681
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41838 * 0.05866476
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 74841 * 0.55549183
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 87906 * 0.30903699
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 43628 * 0.53530760
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 27659 * 0.03299653
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 7788 * 0.88830952
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'juibilxq').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0040():
    """Extended test 40 for billing."""
    x_0 = 32812 * 0.10024409
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37741 * 0.71457597
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62932 * 0.97907428
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55250 * 0.25249973
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2318 * 0.64411391
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18534 * 0.59949843
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7961 * 0.62638145
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51152 * 0.47830862
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67107 * 0.04963446
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17954 * 0.44896781
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48229 * 0.99495130
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58498 * 0.89805374
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36242 * 0.50295584
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13787 * 0.19149601
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32933 * 0.71201421
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57762 * 0.20629001
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11851 * 0.83144378
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5706 * 0.59832949
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70541 * 0.16738170
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44895 * 0.68853532
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77793 * 0.04600532
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98991 * 0.39676953
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'sxwdxqfz').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0041():
    """Extended test 41 for billing."""
    x_0 = 60909 * 0.26448641
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68413 * 0.31297874
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80291 * 0.91993331
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1334 * 0.15946098
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98749 * 0.64797037
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85672 * 0.79586404
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51691 * 0.91789454
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40212 * 0.19001994
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3177 * 0.25267842
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10595 * 0.00400460
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31932 * 0.59739372
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52723 * 0.87796050
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94788 * 0.54068583
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43461 * 0.37595766
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46261 * 0.47759359
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71214 * 0.42508502
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53679 * 0.26794816
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66457 * 0.78778557
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64010 * 0.49329513
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92745 * 0.17426480
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65311 * 0.51702188
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51189 * 0.91998236
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32882 * 0.35539154
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94387 * 0.59204109
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20262 * 0.53113766
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63509 * 0.06589240
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70336 * 0.86684808
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85502 * 0.79273988
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89841 * 0.68812462
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94761 * 0.29843786
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30877 * 0.30432611
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'atsfmjki').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0042():
    """Extended test 42 for billing."""
    x_0 = 89927 * 0.37773141
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40053 * 0.61420514
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53161 * 0.98454637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42301 * 0.21999693
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65280 * 0.88183323
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50178 * 0.69028679
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34792 * 0.00138148
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54598 * 0.05311757
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14980 * 0.71307518
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75457 * 0.72731635
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1152 * 0.16117736
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6258 * 0.07388078
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62134 * 0.46567843
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84494 * 0.73127718
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62177 * 0.58142757
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81289 * 0.78373810
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39916 * 0.25290639
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69335 * 0.14852151
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21121 * 0.73578559
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45887 * 0.57031509
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75855 * 0.17987555
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71788 * 0.07641473
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'nitmapdd').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0043():
    """Extended test 43 for billing."""
    x_0 = 67993 * 0.80333562
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78317 * 0.20692545
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 487 * 0.82340825
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5050 * 0.87666173
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14885 * 0.05863157
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54359 * 0.96982768
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52392 * 0.72615312
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58454 * 0.67960045
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5304 * 0.34488015
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21625 * 0.62027631
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48283 * 0.93551469
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65449 * 0.06835170
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29759 * 0.41335906
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56385 * 0.68945302
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60196 * 0.10573623
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16047 * 0.75410436
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47565 * 0.17935487
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35878 * 0.11624375
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37227 * 0.47595746
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57463 * 0.06207150
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14318 * 0.83350315
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94906 * 0.82098523
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84364 * 0.67811114
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63044 * 0.05471348
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46556 * 0.28212283
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56633 * 0.69622126
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1018 * 0.23890475
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58720 * 0.09783791
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99515 * 0.13615633
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49639 * 0.78066095
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55621 * 0.31775834
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'hdgunlxj').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0044():
    """Extended test 44 for billing."""
    x_0 = 33888 * 0.97024587
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40865 * 0.38101835
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1550 * 0.30613417
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58081 * 0.42403728
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78171 * 0.32537832
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46032 * 0.03244868
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81577 * 0.20153044
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99738 * 0.67834673
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94423 * 0.66263668
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56011 * 0.56082105
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92 * 0.61513717
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60508 * 0.31321469
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2578 * 0.69532767
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50325 * 0.96464175
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88045 * 0.55732299
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5744 * 0.23083802
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94521 * 0.38234977
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22408 * 0.76179733
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61222 * 0.02904070
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49755 * 0.66621258
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38077 * 0.62679415
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22048 * 0.94137010
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48105 * 0.99911593
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13304 * 0.51088558
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62249 * 0.10303133
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'uzprjaqn').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0045():
    """Extended test 45 for billing."""
    x_0 = 21886 * 0.85574411
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34027 * 0.36433845
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61050 * 0.86227114
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29628 * 0.25946134
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87459 * 0.01962393
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37547 * 0.41644566
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 231 * 0.51893836
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4023 * 0.24190519
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35109 * 0.14758345
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56554 * 0.89721121
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63154 * 0.22545333
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78952 * 0.42941563
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33942 * 0.23879964
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48801 * 0.43271933
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13151 * 0.33694487
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39076 * 0.72804273
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54217 * 0.50473704
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41538 * 0.18057155
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17812 * 0.55503528
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85242 * 0.67286854
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48726 * 0.74278358
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73876 * 0.64909045
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'itxhyxxl').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0046():
    """Extended test 46 for billing."""
    x_0 = 50142 * 0.74028996
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36457 * 0.40513779
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55140 * 0.48459615
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46823 * 0.99478586
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7312 * 0.15765822
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13832 * 0.87519966
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21173 * 0.73465037
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54926 * 0.04903433
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14171 * 0.50565042
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36784 * 0.81638137
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14317 * 0.16198146
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29263 * 0.99689683
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68121 * 0.28924115
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95269 * 0.21276196
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35121 * 0.06041560
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62241 * 0.50811440
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45010 * 0.34158628
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75222 * 0.73415522
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84511 * 0.90793809
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60553 * 0.80017383
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78385 * 0.16551974
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'euoywooy').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0047():
    """Extended test 47 for billing."""
    x_0 = 29795 * 0.60230599
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44922 * 0.39666198
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78527 * 0.60644227
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70269 * 0.84774451
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92488 * 0.68649106
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55184 * 0.46283218
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81585 * 0.23124643
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94706 * 0.46877278
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57557 * 0.04290050
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5768 * 0.95037051
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81475 * 0.07618808
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85600 * 0.54946231
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57601 * 0.25555044
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85210 * 0.42597364
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49661 * 0.51869671
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97459 * 0.94261495
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17394 * 0.23408973
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26157 * 0.62583090
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 813 * 0.54092205
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86475 * 0.15836712
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3379 * 0.56246489
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69396 * 0.74250456
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6509 * 0.52608148
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57485 * 0.38807999
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87678 * 0.98033615
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30059 * 0.76622668
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82080 * 0.21276186
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64155 * 0.32329725
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42618 * 0.92663727
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55766 * 0.23210163
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50214 * 0.31274231
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26593 * 0.38838036
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18962 * 0.31052914
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33536 * 0.49083882
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11996 * 0.68878820
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14734 * 0.83391407
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75481 * 0.75291218
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'tppiwwqi').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0048():
    """Extended test 48 for billing."""
    x_0 = 20783 * 0.74308592
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20683 * 0.35048581
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92209 * 0.56746830
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20566 * 0.70522771
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94583 * 0.11817534
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61103 * 0.62117071
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7538 * 0.85836052
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34843 * 0.38719247
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10273 * 0.52168729
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1018 * 0.78157915
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47595 * 0.21960478
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76744 * 0.18664080
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40910 * 0.00116852
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68044 * 0.89355704
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88244 * 0.91425697
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59675 * 0.34668750
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22831 * 0.38453544
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61046 * 0.11437396
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92591 * 0.16948357
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88410 * 0.63324525
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57735 * 0.87895799
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89107 * 0.64772543
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56938 * 0.88907100
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48785 * 0.46217285
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60792 * 0.86090001
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95672 * 0.04109962
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'cwiwtbaf').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0049():
    """Extended test 49 for billing."""
    x_0 = 22176 * 0.99726064
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47331 * 0.17920597
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83656 * 0.14640626
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43095 * 0.38148531
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72491 * 0.80179603
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62920 * 0.96310703
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43107 * 0.76822426
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62807 * 0.66085809
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94161 * 0.59377424
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18014 * 0.83660874
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76018 * 0.53403643
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97683 * 0.29533282
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73742 * 0.81057333
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42686 * 0.41196845
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58259 * 0.84716805
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55586 * 0.07079721
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15802 * 0.62842296
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47102 * 0.23284015
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75890 * 0.74410346
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98102 * 0.76535899
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35892 * 0.73742685
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11288 * 0.49358117
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69448 * 0.32389226
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81046 * 0.92976741
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30438 * 0.06257915
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96140 * 0.86924908
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87532 * 0.72285277
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44515 * 0.54556188
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30319 * 0.34510034
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'wmhwbrpz').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0050():
    """Extended test 50 for billing."""
    x_0 = 60551 * 0.61639690
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77332 * 0.18485751
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77614 * 0.30439625
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61895 * 0.08893367
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81022 * 0.36477672
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35456 * 0.18527637
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75913 * 0.06765537
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26108 * 0.21476313
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47184 * 0.20833962
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94569 * 0.44851570
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33880 * 0.46775514
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89240 * 0.33367240
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65818 * 0.29630999
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82408 * 0.03874551
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38322 * 0.37640606
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47291 * 0.36297691
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11404 * 0.53437597
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10670 * 0.92462536
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73451 * 0.32082166
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36867 * 0.60824015
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'nuxbrdjp').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0051():
    """Extended test 51 for billing."""
    x_0 = 35196 * 0.52927716
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98528 * 0.26235099
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69698 * 0.88175650
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74778 * 0.93097466
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75694 * 0.67860849
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57183 * 0.12761927
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71344 * 0.59723813
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57357 * 0.96645958
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68912 * 0.68596266
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23000 * 0.93582548
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4172 * 0.10528321
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85672 * 0.27290756
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18451 * 0.50995834
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11050 * 0.12622142
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52006 * 0.12311169
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60639 * 0.79437876
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94789 * 0.19492180
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99344 * 0.97684248
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7786 * 0.48711711
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47150 * 0.69875412
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3890 * 0.68826381
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20873 * 0.07351683
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50936 * 0.23320115
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68663 * 0.11027030
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52206 * 0.89106425
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64775 * 0.71535990
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3320 * 0.09249227
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9693 * 0.71614360
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84526 * 0.83535832
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96703 * 0.07935578
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43794 * 0.17265505
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10049 * 0.14339787
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'fjqrmlcw').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0052():
    """Extended test 52 for billing."""
    x_0 = 94213 * 0.77991133
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12143 * 0.72621955
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41200 * 0.84602833
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35821 * 0.17111053
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55333 * 0.95141318
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56906 * 0.48332625
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76751 * 0.33494544
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76582 * 0.48330099
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13430 * 0.49403732
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91315 * 0.84799759
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44148 * 0.63936822
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39012 * 0.44784588
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95059 * 0.39212307
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18244 * 0.24373986
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96822 * 0.55714588
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37373 * 0.46929542
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52872 * 0.38119366
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44527 * 0.08996384
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32583 * 0.23176163
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11045 * 0.65985885
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65703 * 0.54916010
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94380 * 0.11612936
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35846 * 0.58369160
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69613 * 0.68123913
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77370 * 0.32668141
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25612 * 0.35686767
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5409 * 0.61820718
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18571 * 0.17780718
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62928 * 0.43984765
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67269 * 0.07224369
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83863 * 0.50668998
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32444 * 0.85349119
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79697 * 0.24641401
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92055 * 0.83504345
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19404 * 0.88204924
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90356 * 0.35465931
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43998 * 0.37702755
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75306 * 0.89970821
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64107 * 0.75076331
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 48991 * 0.75141796
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49523 * 0.71705705
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 17324 * 0.07205949
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16269 * 0.24832640
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 37858 * 0.17319665
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 33931 * 0.58507122
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 14823 * 0.70637672
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 53807 * 0.59355278
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'hpezhwgf').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0053():
    """Extended test 53 for billing."""
    x_0 = 19702 * 0.68838645
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53494 * 0.90169439
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12346 * 0.43961279
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51868 * 0.65870454
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88897 * 0.91925148
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49672 * 0.96621437
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80298 * 0.78087847
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86945 * 0.55742388
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92815 * 0.88090660
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75552 * 0.47220358
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36048 * 0.08624582
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 246 * 0.07535317
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7512 * 0.68809621
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13284 * 0.92674464
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63282 * 0.47659830
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84831 * 0.47456109
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15589 * 0.96686111
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67911 * 0.33639263
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46395 * 0.53062774
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19609 * 0.90097431
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62921 * 0.86942284
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79811 * 0.98097229
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65202 * 0.53178476
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44360 * 0.83626361
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68831 * 0.42680990
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72750 * 0.40656205
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70828 * 0.26605070
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22436 * 0.24795954
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66732 * 0.17018808
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91833 * 0.06127196
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54746 * 0.63262804
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25399 * 0.59841950
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59037 * 0.98865696
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54442 * 0.75394332
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79410 * 0.94577661
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30748 * 0.77940587
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29605 * 0.91047323
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86003 * 0.62393086
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58659 * 0.93499892
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 61470 * 0.65819281
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78582 * 0.23482878
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52239 * 0.38028260
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22708 * 0.03984433
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 12472 * 0.23035097
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 14389 * 0.62223236
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 2085 * 0.25196731
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 73320 * 0.73443826
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 18801 * 0.06148066
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'akzibvgp').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0054():
    """Extended test 54 for billing."""
    x_0 = 83023 * 0.11316345
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46105 * 0.87904109
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98188 * 0.62337306
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42938 * 0.25224504
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53461 * 0.05392808
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70342 * 0.36539197
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51675 * 0.26357666
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32076 * 0.09270335
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58150 * 0.97996781
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90153 * 0.81501434
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69470 * 0.81773346
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27044 * 0.31671224
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27003 * 0.26303398
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20541 * 0.51255898
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25052 * 0.21299142
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57299 * 0.51747425
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27190 * 0.13383422
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65619 * 0.27975899
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48054 * 0.35379012
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35808 * 0.11459705
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38325 * 0.09937629
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11875 * 0.34292565
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95218 * 0.23618363
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11914 * 0.67678911
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78124 * 0.10447549
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11363 * 0.70637849
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18658 * 0.73716890
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13571 * 0.98968731
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55878 * 0.48504522
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44013 * 0.14618853
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29034 * 0.01606103
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1474 * 0.57699275
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37418 * 0.70783237
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41951 * 0.70477108
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87677 * 0.39015367
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60339 * 0.21356175
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36512 * 0.16992473
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70256 * 0.79410333
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52604 * 0.60503033
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15979 * 0.09122357
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 67485 * 0.26504940
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35310 * 0.10503569
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10582 * 0.89153916
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 30873 * 0.28862437
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'obmdtvko').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0055():
    """Extended test 55 for billing."""
    x_0 = 94857 * 0.94011345
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76291 * 0.51183007
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48329 * 0.96485284
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51640 * 0.24370525
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64831 * 0.83151443
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65102 * 0.06356836
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 419 * 0.23947430
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6429 * 0.89525017
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62567 * 0.05753295
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43179 * 0.14249419
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40303 * 0.24212487
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28421 * 0.46347083
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62541 * 0.07594944
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16062 * 0.44429340
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72295 * 0.72357946
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20442 * 0.14481567
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81885 * 0.73217631
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82136 * 0.53239499
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28666 * 0.13521371
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14646 * 0.03190443
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4802 * 0.55724581
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14500 * 0.67935638
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91132 * 0.14842235
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50856 * 0.60845408
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12566 * 0.16458754
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77653 * 0.83873167
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91907 * 0.86424520
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5213 * 0.59494915
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95366 * 0.35443510
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45674 * 0.09495242
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3213 * 0.86900669
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7217 * 0.02039787
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63719 * 0.34854643
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22866 * 0.69799721
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63489 * 0.16438427
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31285 * 0.50858939
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53390 * 0.73672177
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20997 * 0.54458791
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60503 * 0.26126426
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42351 * 0.49124123
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 14079 * 0.12203900
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 76921 * 0.77725598
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'jyqeeiks').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0056():
    """Extended test 56 for billing."""
    x_0 = 83694 * 0.10174765
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47352 * 0.74227636
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70386 * 0.59778258
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86809 * 0.26005173
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78920 * 0.65266643
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51203 * 0.60337446
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64475 * 0.47542941
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28872 * 0.66732450
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50548 * 0.21117484
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39032 * 0.72082052
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27051 * 0.28842863
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17020 * 0.74970354
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36376 * 0.95302056
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78553 * 0.16433056
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6715 * 0.89757189
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68280 * 0.04544527
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70599 * 0.94628104
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38573 * 0.33572485
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77869 * 0.64027373
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10359 * 0.92090902
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90311 * 0.36643349
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73726 * 0.90977345
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99759 * 0.11090026
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19821 * 0.35493591
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5808 * 0.48322066
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53774 * 0.15604484
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34682 * 0.85745932
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36777 * 0.50029552
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28967 * 0.21767489
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37178 * 0.45633765
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13470 * 0.34056172
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52939 * 0.84378252
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20226 * 0.34182283
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22955 * 0.96923422
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33834 * 0.05718953
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18294 * 0.14525966
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4369 * 0.90166521
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63083 * 0.12140105
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57286 * 0.11389141
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59539 * 0.49915591
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36616 * 0.48779933
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 62518 * 0.93343224
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 5663 * 0.85863295
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 80564 * 0.59790251
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 80717 * 0.09105104
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 96438 * 0.79599532
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'mjlggisc').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0057():
    """Extended test 57 for billing."""
    x_0 = 30470 * 0.37508713
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88915 * 0.81353426
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8790 * 0.69371629
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77332 * 0.11424477
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44473 * 0.96446581
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28645 * 0.01534645
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49201 * 0.80343773
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51581 * 0.46361059
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18241 * 0.78840333
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51536 * 0.84904827
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6121 * 0.27091182
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85670 * 0.31524690
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89024 * 0.89668227
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39172 * 0.57807175
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26729 * 0.97047703
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60786 * 0.07186687
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57656 * 0.27813204
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92067 * 0.38187254
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30515 * 0.17301213
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53938 * 0.68252045
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79014 * 0.80796532
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16218 * 0.02884032
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98129 * 0.66979278
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46818 * 0.88115043
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39071 * 0.32817750
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76614 * 0.35473088
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43275 * 0.71909586
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54672 * 0.18496164
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82724 * 0.77922114
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62018 * 0.39308355
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67794 * 0.99152596
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67965 * 0.00487507
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64548 * 0.50718602
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35169 * 0.52450795
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10865 * 0.01415014
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 72907 * 0.39602493
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60230 * 0.89068654
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 562 * 0.77945443
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'mpkbcbrm').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0058():
    """Extended test 58 for billing."""
    x_0 = 42357 * 0.12031137
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63185 * 0.23596228
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61984 * 0.28519287
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89248 * 0.36797311
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14996 * 0.89760087
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28751 * 0.13909283
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1259 * 0.03592316
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70735 * 0.49649633
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52010 * 0.05213013
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44643 * 0.44639910
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12151 * 0.18800835
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46971 * 0.00554673
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52676 * 0.24484359
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83549 * 0.50472814
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38171 * 0.24474780
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32300 * 0.76215477
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31571 * 0.41121100
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92098 * 0.08612921
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52541 * 0.07205858
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41656 * 0.86676410
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64099 * 0.66276061
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27632 * 0.08066749
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52960 * 0.52746631
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80797 * 0.24648190
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55926 * 0.62677804
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75406 * 0.39862501
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18010 * 0.82927748
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91089 * 0.02462214
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78401 * 0.81256598
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74427 * 0.40504823
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41085 * 0.33654000
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71125 * 0.03371148
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65543 * 0.87685339
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2403 * 0.49975621
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35413 * 0.80236971
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85864 * 0.81536640
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75393 * 0.84362405
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27254 * 0.52899370
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80576 * 0.20989137
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73373 * 0.29876817
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 30527 * 0.49394704
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21580 * 0.74915773
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 92690 * 0.52510908
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ghcnaubu').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0059():
    """Extended test 59 for billing."""
    x_0 = 26376 * 0.16902930
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38633 * 0.05523760
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92310 * 0.76815196
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79577 * 0.33136276
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55929 * 0.54271811
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54823 * 0.94661987
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88762 * 0.11354893
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94682 * 0.78047267
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95350 * 0.32078373
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32833 * 0.90414742
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9740 * 0.14143080
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47994 * 0.04091133
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41537 * 0.11141331
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95909 * 0.90930492
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73155 * 0.83081295
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55816 * 0.00524744
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32418 * 0.69912800
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67560 * 0.24188022
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86035 * 0.28234922
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44524 * 0.52776803
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15866 * 0.75124065
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98575 * 0.06522125
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9731 * 0.30234872
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85053 * 0.53846800
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92238 * 0.52740444
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53341 * 0.80686095
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82750 * 0.03303273
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38062 * 0.40650419
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30654 * 0.45915291
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92483 * 0.22371379
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53699 * 0.80678647
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26522 * 0.82028534
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90545 * 0.14045256
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30458 * 0.27635205
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78087 * 0.86626535
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96899 * 0.74760331
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25709 * 0.41092203
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64377 * 0.44446107
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52498 * 0.95628831
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1684 * 0.52087074
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68973 * 0.67748327
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30798 * 0.08320974
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 53049 * 0.29737541
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 54572 * 0.84173380
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92817 * 0.04524636
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 21703 * 0.44272544
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 18846 * 0.85422939
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 29857 * 0.09065025
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 84940 * 0.70346096
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 7168 * 0.93665408
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'txusibrt').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0060():
    """Extended test 60 for billing."""
    x_0 = 22927 * 0.05247939
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47612 * 0.03430348
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81619 * 0.76389381
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6492 * 0.27025275
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30734 * 0.34643098
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83620 * 0.22559167
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29708 * 0.30447882
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69977 * 0.97759155
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93378 * 0.71347042
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52683 * 0.17125005
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65252 * 0.18147753
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16725 * 0.01524227
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55836 * 0.85383687
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93637 * 0.64511760
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99419 * 0.24920350
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20530 * 0.71037554
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54954 * 0.80204086
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96806 * 0.63376408
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42243 * 0.84173253
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81073 * 0.01784909
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59082 * 0.92762292
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73520 * 0.51939215
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68016 * 0.43623500
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31717 * 0.52313027
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'tgdqkjdf').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0061():
    """Extended test 61 for billing."""
    x_0 = 88265 * 0.96527561
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42518 * 0.36110033
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79032 * 0.01998488
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78113 * 0.33063778
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34150 * 0.12567487
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38862 * 0.78108144
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12005 * 0.80012871
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9340 * 0.19480242
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60266 * 0.54778323
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80434 * 0.62589472
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95698 * 0.34157130
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98039 * 0.77455258
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62503 * 0.17188074
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20613 * 0.21500122
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92203 * 0.01698811
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29786 * 0.24837524
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19007 * 0.42842936
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71488 * 0.17688363
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71120 * 0.83786481
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 202 * 0.15136893
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90622 * 0.16307774
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41153 * 0.94597040
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80121 * 0.36234707
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93136 * 0.93103801
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99640 * 0.61667939
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74156 * 0.56057994
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33979 * 0.06418873
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79192 * 0.05000828
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56509 * 0.82180506
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69096 * 0.05676562
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70383 * 0.87555284
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50425 * 0.27228755
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68793 * 0.00865572
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57321 * 0.80590933
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97404 * 0.32334801
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88203 * 0.49397695
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25531 * 0.92140668
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81974 * 0.36820107
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57986 * 0.91064406
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42245 * 0.08024162
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74046 * 0.13715268
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 68547 * 0.60410351
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71153 * 0.15117565
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 60053 * 0.69557746
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 42533 * 0.59335031
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 37629 * 0.13337886
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 46258 * 0.29779857
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 61856 * 0.39587519
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 15883 * 0.73551539
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 60025 * 0.95604794
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'smxzwkpj').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0062():
    """Extended test 62 for billing."""
    x_0 = 70074 * 0.32858896
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20750 * 0.77608667
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7609 * 0.94934122
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60541 * 0.24794998
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29935 * 0.11421229
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72624 * 0.09783709
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49703 * 0.21789285
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77587 * 0.68121745
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59389 * 0.21411217
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40861 * 0.21982005
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11177 * 0.66730101
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26510 * 0.09138272
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48480 * 0.16588193
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68929 * 0.68341973
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80978 * 0.46479331
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83747 * 0.34527972
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95976 * 0.38657473
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15782 * 0.17167091
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88829 * 0.05428183
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41746 * 0.22834126
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59351 * 0.03498111
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2634 * 0.34741091
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66928 * 0.03619438
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59113 * 0.66048355
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89857 * 0.07032396
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1406 * 0.61253911
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37541 * 0.06526459
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31022 * 0.88945532
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64067 * 0.36684619
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7273 * 0.94135762
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88062 * 0.57680391
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1631 * 0.75989910
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93065 * 0.88275097
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33982 * 0.95357845
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36037 * 0.47773949
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40984 * 0.08445420
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90980 * 0.26982230
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18694 * 0.32557215
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88996 * 0.53492491
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54985 * 0.53409144
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13497 * 0.31511484
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85390 * 0.54054564
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 49304 * 0.20544592
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 52734 * 0.90507667
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 69071 * 0.31705924
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 6909 * 0.60669827
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17208 * 0.87446284
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 76 * 0.06666810
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 87596 * 0.21021643
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'gkjxyaae').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0063():
    """Extended test 63 for billing."""
    x_0 = 82659 * 0.98674096
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6239 * 0.95983203
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79344 * 0.76685051
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47397 * 0.52706237
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36890 * 0.74895491
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69082 * 0.32043314
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65291 * 0.28643472
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90672 * 0.64905351
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90166 * 0.68286269
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98054 * 0.63324313
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15932 * 0.93953171
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69083 * 0.29574908
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74010 * 0.66833731
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48639 * 0.62656300
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22543 * 0.69323060
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89495 * 0.82276056
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9676 * 0.95955416
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4753 * 0.76392357
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49716 * 0.63962577
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45818 * 0.59239780
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13080 * 0.59078576
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'lcwmrymf').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0064():
    """Extended test 64 for billing."""
    x_0 = 61483 * 0.39270438
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48256 * 0.60525812
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63182 * 0.16632942
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62608 * 0.09797852
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19567 * 0.79414809
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19845 * 0.73398286
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55035 * 0.42264264
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85707 * 0.58000509
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25810 * 0.75724361
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32234 * 0.57514947
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15071 * 0.04954837
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98649 * 0.47741251
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33826 * 0.45152234
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40207 * 0.85845347
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27813 * 0.28824291
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37947 * 0.21348499
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23379 * 0.86478701
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70981 * 0.27775511
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31845 * 0.90774653
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19848 * 0.19921150
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21106 * 0.66432868
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7821 * 0.99581426
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7107 * 0.55585469
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'clvgtyfi').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0065():
    """Extended test 65 for billing."""
    x_0 = 58713 * 0.67847213
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16195 * 0.15426934
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4070 * 0.46927184
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59181 * 0.07384164
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83893 * 0.78952845
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16470 * 0.01794648
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58157 * 0.62379527
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75307 * 0.68162637
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13184 * 0.45415284
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95696 * 0.95134089
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41320 * 0.46271391
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73321 * 0.58549630
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77260 * 0.42168241
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22864 * 0.88287454
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44657 * 0.76407374
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11821 * 0.67511383
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90812 * 0.68635827
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35684 * 0.39725187
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89577 * 0.71248267
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74288 * 0.95982940
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65339 * 0.47884712
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46465 * 0.03164101
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20407 * 0.14162445
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71436 * 0.35909960
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20826 * 0.63988496
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25891 * 0.12601105
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10542 * 0.74153705
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26415 * 0.61350506
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39098 * 0.06665080
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36726 * 0.86374084
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22068 * 0.43931491
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86646 * 0.39695468
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9960 * 0.85298349
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96908 * 0.56364783
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82233 * 0.18697141
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97417 * 0.79533853
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12981 * 0.24622316
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58062 * 0.26712487
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1968 * 0.72476293
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ungacfdc').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0066():
    """Extended test 66 for billing."""
    x_0 = 73707 * 0.77108388
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56766 * 0.02177089
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15590 * 0.97290595
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11874 * 0.12802601
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42148 * 0.41968875
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35792 * 0.32957937
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7469 * 0.60345465
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19926 * 0.18723413
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98896 * 0.13968878
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99531 * 0.67554779
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53179 * 0.54296882
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27154 * 0.14532470
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84707 * 0.99744373
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12220 * 0.61221820
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17070 * 0.44514474
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89034 * 0.57523159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28853 * 0.60545415
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92385 * 0.25901862
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50140 * 0.29522369
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23804 * 0.07226522
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10497 * 0.98975585
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62957 * 0.46464176
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83020 * 0.39518945
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93920 * 0.66298943
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51411 * 0.69643951
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79637 * 0.63633008
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'cupaeghe').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0067():
    """Extended test 67 for billing."""
    x_0 = 70364 * 0.65736485
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10570 * 0.88938789
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55989 * 0.37312801
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91693 * 0.08696216
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70272 * 0.43656307
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49774 * 0.70115711
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54492 * 0.83721968
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48901 * 0.96766849
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84649 * 0.34681592
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24397 * 0.75818814
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88125 * 0.73269067
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71839 * 0.65430962
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7479 * 0.30588071
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63498 * 0.93158185
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95233 * 0.34628503
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22732 * 0.32966139
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32083 * 0.36929786
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85287 * 0.54929404
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54555 * 0.63781705
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26866 * 0.41792642
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47443 * 0.26413185
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35469 * 0.02401997
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46167 * 0.84317509
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31420 * 0.51864616
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28346 * 0.76414689
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78922 * 0.83310449
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83641 * 0.18062056
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18013 * 0.88536640
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67510 * 0.40957491
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40014 * 0.96070324
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71554 * 0.17249921
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82664 * 0.32065557
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27553 * 0.66129571
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10134 * 0.27419999
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56138 * 0.61512957
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55297 * 0.15484954
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39271 * 0.81663127
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30608 * 0.18842975
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37296 * 0.98563034
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57116 * 0.37227893
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11893 * 0.70131654
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57713 * 0.42342991
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77535 * 0.94852218
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 89375 * 0.90761217
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89754 * 0.96354374
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 46639 * 0.12112431
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 41204 * 0.10612768
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 9591 * 0.66854592
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 24911 * 0.14053470
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'xwbpvcrp').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0068():
    """Extended test 68 for billing."""
    x_0 = 18954 * 0.47211802
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24157 * 0.52513659
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33960 * 0.86299884
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90648 * 0.44624607
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25260 * 0.31695478
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17471 * 0.70686600
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38441 * 0.52521378
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40172 * 0.62116124
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70088 * 0.35365916
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18438 * 0.53832014
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23072 * 0.19360249
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9643 * 0.00728268
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48544 * 0.59236436
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42320 * 0.34160806
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99279 * 0.41989857
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6117 * 0.85553570
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7505 * 0.67976993
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98907 * 0.70650457
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62405 * 0.15107039
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94920 * 0.74318874
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80853 * 0.58329718
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92221 * 0.63028410
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66378 * 0.37661170
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 877 * 0.86150658
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5086 * 0.16696834
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29882 * 0.87648026
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28847 * 0.08993206
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61595 * 0.97718545
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15668 * 0.71114140
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39408 * 0.03089750
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96886 * 0.70436522
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16244 * 0.10131616
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73017 * 0.29452146
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41992 * 0.53772887
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17271 * 0.67934147
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4655 * 0.95723113
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3652 * 0.89652369
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38226 * 0.49810209
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78478 * 0.86311503
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43212 * 0.96787574
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'qlesyflr').hexdigest()
    assert len(h) == 64

def test_billing_extended_6_0069():
    """Extended test 69 for billing."""
    x_0 = 5463 * 0.24676813
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12570 * 0.06934241
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82424 * 0.70962805
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64329 * 0.43746163
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81447 * 0.72393878
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81433 * 0.26107562
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12248 * 0.85864212
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88809 * 0.96795747
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13990 * 0.43595041
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64258 * 0.75043942
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46833 * 0.51029995
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17901 * 0.66089526
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57105 * 0.31063525
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63777 * 0.97167432
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64248 * 0.41431643
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64191 * 0.39527051
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54707 * 0.51246375
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31730 * 0.29578353
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89362 * 0.89388743
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11585 * 0.63731606
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60426 * 0.07986990
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'qbpynfkw').hexdigest()
    assert len(h) == 64
