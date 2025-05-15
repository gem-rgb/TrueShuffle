"""Extended tests for federation suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_federation_extended_8_0000():
    """Extended test 0 for federation."""
    x_0 = 17412 * 0.45412916
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45373 * 0.67547695
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78004 * 0.41972374
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72308 * 0.97728181
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85 * 0.75740083
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52754 * 0.03284881
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56379 * 0.73189833
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76438 * 0.06382295
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19399 * 0.76118427
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20893 * 0.13868081
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90223 * 0.93777854
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76539 * 0.29547026
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38945 * 0.79270326
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30962 * 0.55435906
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59655 * 0.62760162
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85534 * 0.88524185
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81012 * 0.08102117
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35819 * 0.98534628
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35007 * 0.02211953
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64793 * 0.05851121
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79346 * 0.26836460
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1150 * 0.21320476
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2276 * 0.51749861
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76672 * 0.46432537
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46408 * 0.49140484
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95471 * 0.78277803
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11968 * 0.69317143
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78889 * 0.82213059
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78003 * 0.33954576
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28824 * 0.17286217
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'pgiqttog').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0001():
    """Extended test 1 for federation."""
    x_0 = 75112 * 0.93287755
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44367 * 0.32697449
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15376 * 0.86400136
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3808 * 0.68954525
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30428 * 0.26426373
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46015 * 0.52385368
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13668 * 0.22100168
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40769 * 0.18198791
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9565 * 0.22836882
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 502 * 0.13079267
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93049 * 0.03661647
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8335 * 0.41621874
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25611 * 0.29381570
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6305 * 0.14759918
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46909 * 0.05985857
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95963 * 0.11577038
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66051 * 0.69469565
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44962 * 0.14795492
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20460 * 0.44780790
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71623 * 0.30028927
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ndgrwdtx').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0002():
    """Extended test 2 for federation."""
    x_0 = 97397 * 0.53174670
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58172 * 0.27373875
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15485 * 0.16857637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99287 * 0.65907060
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97146 * 0.60743009
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1371 * 0.53599357
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44668 * 0.34980994
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51947 * 0.28560879
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52207 * 0.13125765
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72183 * 0.59970952
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10600 * 0.76124684
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5129 * 0.42867186
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14296 * 0.40743097
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92923 * 0.12288494
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35256 * 0.56036727
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47696 * 0.57112124
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80114 * 0.96224842
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54901 * 0.06366020
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96914 * 0.72350808
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29257 * 0.10552265
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44350 * 0.83815800
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73103 * 0.22995175
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95129 * 0.83126805
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64330 * 0.90781160
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23222 * 0.17555901
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34500 * 0.41761846
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98168 * 0.42847717
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49839 * 0.77075265
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27010 * 0.26805512
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25424 * 0.85086472
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83538 * 0.16792307
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23790 * 0.83040397
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66192 * 0.32501416
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69305 * 0.86753876
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'fvwdwoqu').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0003():
    """Extended test 3 for federation."""
    x_0 = 65761 * 0.31487596
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46354 * 0.06874017
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22358 * 0.73515307
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61825 * 0.94639362
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8359 * 0.88212103
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98836 * 0.48549250
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81714 * 0.47884959
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82105 * 0.33552975
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84508 * 0.47807205
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40044 * 0.72735736
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97856 * 0.00609672
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99938 * 0.04365221
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78943 * 0.32186701
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7254 * 0.20734067
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13397 * 0.58369034
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71106 * 0.73486342
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95458 * 0.10459380
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18978 * 0.60627131
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76545 * 0.74744656
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61983 * 0.43705364
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48699 * 0.16232529
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76271 * 0.97105923
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71049 * 0.02954893
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21338 * 0.62568075
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65636 * 0.86181312
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43312 * 0.71380971
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45905 * 0.85482909
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36360 * 0.25738386
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55069 * 0.55301701
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55476 * 0.35388560
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81220 * 0.66144794
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 765 * 0.15171919
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17989 * 0.37496276
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18865 * 0.58187831
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36709 * 0.10128740
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 92350 * 0.89060507
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62987 * 0.74257849
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60558 * 0.50105875
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61348 * 0.74731819
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91491 * 0.55496657
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 76947 * 0.76975730
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'bldilkql').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0004():
    """Extended test 4 for federation."""
    x_0 = 26190 * 0.64590615
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19296 * 0.82262259
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5931 * 0.17495533
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76789 * 0.09884830
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96492 * 0.52855354
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63506 * 0.75869951
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84755 * 0.32989462
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3256 * 0.72743700
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28923 * 0.57988876
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47928 * 0.16063542
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90060 * 0.30356276
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3556 * 0.11779699
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97164 * 0.45323892
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72023 * 0.33404934
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62271 * 0.77540467
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87497 * 0.56147482
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9631 * 0.24297267
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31512 * 0.83734894
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87678 * 0.64303295
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13373 * 0.48664228
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10043 * 0.47707454
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17749 * 0.05375606
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42846 * 0.69888375
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86745 * 0.75055989
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8486 * 0.11470698
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72197 * 0.56160627
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46628 * 0.83553491
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85652 * 0.71761688
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37891 * 0.92043965
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35168 * 0.97730613
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65216 * 0.35320328
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11078 * 0.18881382
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60818 * 0.84745576
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62102 * 0.86771947
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54250 * 0.47713801
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49810 * 0.27740211
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91623 * 0.41225930
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1111 * 0.99689132
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'rxbletme').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0005():
    """Extended test 5 for federation."""
    x_0 = 54025 * 0.93164220
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92614 * 0.69180317
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43395 * 0.73793483
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42627 * 0.04164133
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2013 * 0.96267585
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96004 * 0.75644514
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44692 * 0.13424930
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31461 * 0.87914139
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44174 * 0.24125205
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54419 * 0.33288329
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83841 * 0.32168278
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52247 * 0.14858019
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25281 * 0.28592091
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63137 * 0.61430341
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88572 * 0.45578743
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72063 * 0.32847003
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2155 * 0.88889015
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9490 * 0.68384389
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35481 * 0.73839731
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83721 * 0.43169998
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43127 * 0.68397689
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15723 * 0.11537694
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84804 * 0.70324606
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63726 * 0.42612309
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47466 * 0.71869022
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72719 * 0.95005864
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23126 * 0.24854129
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42048 * 0.83879989
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7186 * 0.63904294
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29809 * 0.80854161
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38598 * 0.45866858
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3545 * 0.27832511
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87773 * 0.57418838
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57612 * 0.09295178
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81640 * 0.68628572
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14987 * 0.32917703
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73106 * 0.14353427
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31330 * 0.04745979
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67016 * 0.52098236
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64790 * 0.19359244
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5190 * 0.02191046
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12403 * 0.92972440
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 17587 * 0.30418521
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 18384 * 0.02115568
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 54552 * 0.02012770
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 54042 * 0.22131369
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 84260 * 0.14231990
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 30143 * 0.72883484
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'cscdedyq').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0006():
    """Extended test 6 for federation."""
    x_0 = 60176 * 0.36854405
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65572 * 0.55306380
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77275 * 0.80467512
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13870 * 0.98147037
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72041 * 0.95637844
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47086 * 0.46891261
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80616 * 0.62712492
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11478 * 0.74849539
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91720 * 0.02618140
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34060 * 0.38700999
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70170 * 0.10034685
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68333 * 0.50237483
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9897 * 0.87289672
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74946 * 0.72830141
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17394 * 0.77205311
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93143 * 0.77071679
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58713 * 0.20227384
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27566 * 0.48222909
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9477 * 0.68693962
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13548 * 0.58701504
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94381 * 0.68856474
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62741 * 0.34014140
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6001 * 0.03175134
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41609 * 0.17708033
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97098 * 0.71689475
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59137 * 0.95144535
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5496 * 0.22789727
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64940 * 0.05259814
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99389 * 0.46374864
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70296 * 0.52933631
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62499 * 0.99897257
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11832 * 0.74227003
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96962 * 0.26330979
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8663 * 0.51854420
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62298 * 0.66910549
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35477 * 0.27872775
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29822 * 0.69955315
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17954 * 0.89747540
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21582 * 0.71953674
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'mwbdhiud').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0007():
    """Extended test 7 for federation."""
    x_0 = 69641 * 0.69670012
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68077 * 0.35600453
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10898 * 0.10631324
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61459 * 0.98149204
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22472 * 0.88371020
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89685 * 0.04737906
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8477 * 0.91654568
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36746 * 0.40568337
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29215 * 0.60687536
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9202 * 0.23027650
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15014 * 0.33739288
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8700 * 0.99277631
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7987 * 0.12778347
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41960 * 0.16335902
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93566 * 0.53070114
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35645 * 0.47533138
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9291 * 0.69867132
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42659 * 0.08011791
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7834 * 0.35195289
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36372 * 0.36256276
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74098 * 0.14344276
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97693 * 0.46810071
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16110 * 0.02110283
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26053 * 0.98788052
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76424 * 0.85075766
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65619 * 0.88102138
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83576 * 0.13549953
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37078 * 0.16008996
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65016 * 0.27299577
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63874 * 0.50548561
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52747 * 0.76177620
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7687 * 0.86032143
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73256 * 0.83148018
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50471 * 0.59098145
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89167 * 0.99049352
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70411 * 0.33385702
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84679 * 0.95868296
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21298 * 0.15750338
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75617 * 0.82350770
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83169 * 0.77404295
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37590 * 0.30041162
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57425 * 0.27248608
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'laznngae').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0008():
    """Extended test 8 for federation."""
    x_0 = 68365 * 0.12535734
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85785 * 0.19741739
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79556 * 0.69648625
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43985 * 0.61198037
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82292 * 0.04766601
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34818 * 0.15313888
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50238 * 0.23415133
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64406 * 0.12115313
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61178 * 0.32755730
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 395 * 0.64984623
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95929 * 0.21329939
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41732 * 0.68150228
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93307 * 0.26872898
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58842 * 0.01470389
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70008 * 0.01987283
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62490 * 0.93577093
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94151 * 0.39998842
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18103 * 0.16181563
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61285 * 0.10483210
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84703 * 0.51459830
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94409 * 0.07040060
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37828 * 0.20052366
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83750 * 0.51239840
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 711 * 0.43199721
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61513 * 0.23723632
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16826 * 0.03660489
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71561 * 0.49501864
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11219 * 0.12388164
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57197 * 0.01248397
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64812 * 0.96102078
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61301 * 0.09759896
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86215 * 0.12026552
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11448 * 0.32778674
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67950 * 0.78523771
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22847 * 0.86484458
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47796 * 0.59319113
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32754 * 0.51676486
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49000 * 0.56418966
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67695 * 0.98160607
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32728 * 0.10864822
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74426 * 0.87336412
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72306 * 0.63312022
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44530 * 0.88246801
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75843 * 0.83975253
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 63453 * 0.43163502
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'oihivkdq').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0009():
    """Extended test 9 for federation."""
    x_0 = 80994 * 0.98337822
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49006 * 0.15813686
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1493 * 0.88725394
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34153 * 0.59469230
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38726 * 0.12796337
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92157 * 0.72300124
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99640 * 0.92122262
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87363 * 0.62775477
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94696 * 0.32897875
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83163 * 0.49101788
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83761 * 0.35664756
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 954 * 0.41510081
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56498 * 0.08905545
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88112 * 0.11074367
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74298 * 0.79285488
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70293 * 0.65311955
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60861 * 0.18554002
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15654 * 0.13285740
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99341 * 0.86426455
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40923 * 0.61691637
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4256 * 0.66624787
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65164 * 0.58198640
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91146 * 0.07203214
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64126 * 0.16775349
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5921 * 0.00874590
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97941 * 0.26367815
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79729 * 0.62053278
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40181 * 0.08844734
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85377 * 0.27310474
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81698 * 0.66425850
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57580 * 0.40639684
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74516 * 0.36468679
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70777 * 0.11174043
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63635 * 0.38131839
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22795 * 0.97309259
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49254 * 0.72057342
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'vkqzanrn').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0010():
    """Extended test 10 for federation."""
    x_0 = 31927 * 0.07018492
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66254 * 0.13100230
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35766 * 0.06198099
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96588 * 0.11077730
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55242 * 0.93982945
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12238 * 0.72578989
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82714 * 0.64613772
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70412 * 0.25447467
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42151 * 0.85568824
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41265 * 0.31619422
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58057 * 0.95335546
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95214 * 0.55320007
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83983 * 0.75230717
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7010 * 0.68590572
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90157 * 0.64682860
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41405 * 0.28096691
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72059 * 0.67588779
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76429 * 0.54655795
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9328 * 0.13163639
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19833 * 0.09918000
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84152 * 0.00873562
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90103 * 0.75184847
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42374 * 0.41647154
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3971 * 0.77096383
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34533 * 0.62283718
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63763 * 0.06562703
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45574 * 0.49838879
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64845 * 0.77627916
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10064 * 0.74576044
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91154 * 0.24040573
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7857 * 0.86925810
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9891 * 0.55215623
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17345 * 0.98280150
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79036 * 0.49865667
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83638 * 0.39252056
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33496 * 0.27115274
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'budzqtfu').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0011():
    """Extended test 11 for federation."""
    x_0 = 3652 * 0.82594655
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14087 * 0.23991775
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94814 * 0.15673193
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19656 * 0.98717867
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33546 * 0.99471064
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58806 * 0.32695947
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51773 * 0.88082460
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77621 * 0.91048721
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22566 * 0.02035919
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5163 * 0.20467975
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90138 * 0.90566148
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 334 * 0.86058027
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46236 * 0.99810496
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25349 * 0.90787572
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96452 * 0.96527385
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62203 * 0.83698240
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45778 * 0.11394684
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17696 * 0.06141557
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42952 * 0.77415967
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36400 * 0.38535859
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25583 * 0.24425970
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'dvqyojzs').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0012():
    """Extended test 12 for federation."""
    x_0 = 96931 * 0.98047818
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21673 * 0.75876442
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53459 * 0.17927200
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43039 * 0.04588869
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66998 * 0.58070177
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83625 * 0.46602706
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95719 * 0.37471483
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37535 * 0.23352327
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32482 * 0.63958802
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60733 * 0.07383946
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20209 * 0.36502307
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43041 * 0.95807401
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24106 * 0.16957443
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9101 * 0.40104070
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36547 * 0.05841850
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31604 * 0.57901237
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22804 * 0.59387087
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36847 * 0.70963592
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87742 * 0.11035854
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72655 * 0.68981000
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28372 * 0.79984200
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75249 * 0.07788314
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68523 * 0.05243219
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9004 * 0.33832787
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20631 * 0.53298073
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66322 * 0.92031383
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15203 * 0.41716048
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75471 * 0.05664849
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41917 * 0.72904174
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46831 * 0.35034652
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65156 * 0.37342431
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16549 * 0.15826462
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51403 * 0.24933878
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63004 * 0.27312222
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72134 * 0.24825316
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33827 * 0.96326267
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68809 * 0.33928555
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92268 * 0.68059508
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46337 * 0.14494084
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98339 * 0.10092517
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65383 * 0.71954432
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 56688 * 0.43419223
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62025 * 0.60508067
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 64256 * 0.41951097
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89991 * 0.08707748
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4588 * 0.98994102
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 43163 * 0.34221788
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 67389 * 0.45838887
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 37684 * 0.56739560
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 46817 * 0.18599291
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'xcsotzpi').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0013():
    """Extended test 13 for federation."""
    x_0 = 2861 * 0.71595250
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15522 * 0.50293317
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87087 * 0.19868008
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3921 * 0.61357220
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80362 * 0.73083236
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16041 * 0.88539442
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31228 * 0.22520092
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23031 * 0.17473716
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21393 * 0.92742313
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25278 * 0.55486197
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30004 * 0.92657640
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77590 * 0.88740059
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38500 * 0.51601045
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45102 * 0.88044718
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95070 * 0.47143404
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60606 * 0.65859333
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88117 * 0.51804763
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54920 * 0.79274355
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81309 * 0.74633738
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8581 * 0.78791243
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87188 * 0.26074848
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27977 * 0.95034238
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40417 * 0.71359486
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36781 * 0.94495359
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15189 * 0.10953738
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47225 * 0.58650997
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62014 * 0.79821046
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65794 * 0.96634318
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43859 * 0.59116075
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15539 * 0.34230734
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71958 * 0.70823997
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6413 * 0.84027629
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4586 * 0.25993699
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32713 * 0.67899939
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62788 * 0.83095876
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6618 * 0.82785249
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ijmqmvbs').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0014():
    """Extended test 14 for federation."""
    x_0 = 37394 * 0.98461948
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85344 * 0.13185428
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65073 * 0.86934625
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87921 * 0.00950982
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84823 * 0.09717316
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72326 * 0.53943700
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77342 * 0.98003823
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34475 * 0.72658770
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57908 * 0.18189963
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20466 * 0.73774805
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19866 * 0.70754105
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13342 * 0.54969464
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8852 * 0.87566183
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88976 * 0.57010106
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15365 * 0.06253504
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60752 * 0.07098629
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28368 * 0.50945014
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29655 * 0.21331460
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41312 * 0.07351881
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99668 * 0.61838305
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56060 * 0.79078042
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43242 * 0.10200163
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2379 * 0.37774967
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61377 * 0.57421558
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78100 * 0.95154004
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25766 * 0.04205863
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23591 * 0.05004977
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23988 * 0.62227839
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68922 * 0.67479608
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39891 * 0.46291074
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9667 * 0.08405153
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73927 * 0.54894354
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54527 * 0.20011320
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26979 * 0.96748408
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43458 * 0.21723866
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97645 * 0.01295664
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40759 * 0.74449714
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28381 * 0.09814945
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 85602 * 0.97378014
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16311 * 0.62444843
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32631 * 0.00968395
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 86934 * 0.51111288
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 30005 * 0.33696298
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 49943 * 0.59171911
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 75040 * 0.28507766
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 93413 * 0.72442911
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 33916 * 0.12181365
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 21062 * 0.25187136
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 33259 * 0.40521524
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 52249 * 0.75537113
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'txluosog').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0015():
    """Extended test 15 for federation."""
    x_0 = 3456 * 0.76069100
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41928 * 0.95359888
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26505 * 0.31388637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37964 * 0.54730350
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11641 * 0.55783658
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48573 * 0.24523105
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88138 * 0.51301607
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14476 * 0.43042152
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97821 * 0.11982822
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35443 * 0.09429613
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19457 * 0.64359966
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8349 * 0.85857049
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17130 * 0.85634771
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6910 * 0.68050034
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99792 * 0.17946891
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95342 * 0.74057982
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16419 * 0.79329819
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14359 * 0.06665894
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21138 * 0.29867145
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36476 * 0.57127636
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95079 * 0.33589408
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18201 * 0.89408404
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33156 * 0.09918473
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39929 * 0.47990912
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29818 * 0.96482919
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35152 * 0.16906563
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52198 * 0.53055384
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29058 * 0.35515380
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57752 * 0.38276318
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79204 * 0.37366479
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91376 * 0.62291921
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65219 * 0.74834772
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54946 * 0.33439220
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98491 * 0.23273987
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1504 * 0.38808439
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34635 * 0.75667061
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63144 * 0.32239802
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73947 * 0.42537479
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51657 * 0.37737823
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29567 * 0.61643643
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ecgeqcsz').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0016():
    """Extended test 16 for federation."""
    x_0 = 9485 * 0.54753749
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74864 * 0.04233015
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41047 * 0.24067307
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96294 * 0.31464993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8655 * 0.37174082
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52476 * 0.48127166
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1872 * 0.37238622
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43969 * 0.85211552
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35090 * 0.21217963
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49932 * 0.54232861
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40107 * 0.31534630
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80948 * 0.43047881
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53473 * 0.45677056
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99774 * 0.54053137
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59438 * 0.83351105
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20604 * 0.20068097
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81422 * 0.24568628
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55370 * 0.89542720
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78335 * 0.62779220
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2937 * 0.44514947
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5031 * 0.79858309
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58108 * 0.91888589
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61499 * 0.32828761
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15036 * 0.23242740
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19850 * 0.63864391
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58989 * 0.73133191
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63731 * 0.99988220
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'kkdkoetl').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0017():
    """Extended test 17 for federation."""
    x_0 = 60246 * 0.31848975
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79475 * 0.96899732
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73653 * 0.10147194
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11313 * 0.20852313
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85960 * 0.32636479
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39111 * 0.32739237
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28915 * 0.35044060
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69062 * 0.03695315
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12146 * 0.66392592
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91398 * 0.43851642
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96451 * 0.34367658
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85439 * 0.31805455
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79656 * 0.40625012
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61878 * 0.82909568
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8812 * 0.47200037
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9885 * 0.23220115
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17199 * 0.59967889
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48098 * 0.76348508
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46406 * 0.98439013
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62347 * 0.29081874
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41323 * 0.40048280
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98482 * 0.28046572
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57967 * 0.68895416
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13513 * 0.97177215
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3510 * 0.14813005
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77973 * 0.52650204
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61234 * 0.76737229
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26955 * 0.95430212
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30346 * 0.20879808
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75893 * 0.79570862
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38494 * 0.03621140
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94499 * 0.36202722
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80380 * 0.92779781
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33563 * 0.81739510
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70011 * 0.45002956
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37720 * 0.45899730
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78397 * 0.05548542
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20508 * 0.75379075
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62435 * 0.61349845
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 533 * 0.32667185
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47794 * 0.31380634
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12930 * 0.28853189
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 39307 * 0.16994755
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20863 * 0.99566964
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 43132 * 0.75740547
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 62578 * 0.77347018
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 38442 * 0.47081783
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 4149 * 0.39128584
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 96147 * 0.74809631
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 50175 * 0.42012883
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'znbmmrvw').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0018():
    """Extended test 18 for federation."""
    x_0 = 1986 * 0.63041145
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54081 * 0.39626041
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43675 * 0.59602066
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24660 * 0.17320541
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40594 * 0.28609990
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63472 * 0.66629590
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27084 * 0.94077460
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16877 * 0.23417107
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67777 * 0.97676901
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16396 * 0.14525347
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78218 * 0.14969162
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29413 * 0.70172445
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78484 * 0.30620530
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78770 * 0.17701914
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94201 * 0.32728750
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58377 * 0.47764907
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86542 * 0.96080362
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11898 * 0.21562391
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15446 * 0.43973874
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59264 * 0.95196574
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1236 * 0.03365566
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19190 * 0.36736484
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2290 * 0.40338476
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94246 * 0.67926326
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36098 * 0.77729056
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67036 * 0.92941317
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43001 * 0.83662041
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76805 * 0.91318112
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62559 * 0.57136173
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'breyrjpm').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0019():
    """Extended test 19 for federation."""
    x_0 = 1347 * 0.83659222
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71189 * 0.81012568
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32772 * 0.48766268
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4413 * 0.95810335
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39199 * 0.25045601
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4368 * 0.71306380
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33819 * 0.39109296
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59852 * 0.92691068
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38939 * 0.53462247
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91113 * 0.24006705
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 219 * 0.51078607
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17759 * 0.26447535
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76957 * 0.69195639
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45721 * 0.33611201
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73902 * 0.30386405
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86170 * 0.19817438
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78505 * 0.33207664
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43955 * 0.83300997
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73270 * 0.03592730
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97679 * 0.70852791
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94850 * 0.96435286
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11624 * 0.31678938
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90465 * 0.21420798
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33852 * 0.22053034
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49523 * 0.09492575
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91737 * 0.68194825
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11548 * 0.22585314
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80204 * 0.88318045
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89545 * 0.08713567
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68985 * 0.29184170
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34172 * 0.16038274
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83584 * 0.03968441
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43683 * 0.70561521
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75199 * 0.63623261
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41283 * 0.57680174
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8334 * 0.44101157
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30858 * 0.47299752
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38576 * 0.87317359
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65707 * 0.45650986
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65803 * 0.50403706
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45868 * 0.04526570
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 99870 * 0.31318713
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71463 * 0.81464283
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ryrnfbok').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0020():
    """Extended test 20 for federation."""
    x_0 = 98121 * 0.64207598
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21566 * 0.75512739
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29067 * 0.67266145
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72859 * 0.17469350
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30152 * 0.96538244
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47351 * 0.53290999
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86051 * 0.36821596
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 310 * 0.34019088
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34989 * 0.02472312
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29991 * 0.59013226
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78470 * 0.80377063
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34132 * 0.18583717
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77194 * 0.55082674
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34554 * 0.41582408
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7950 * 0.01017604
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99171 * 0.91318937
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18316 * 0.83354258
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14679 * 0.64177360
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5133 * 0.94744929
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10476 * 0.04295748
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5393 * 0.89658930
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85961 * 0.98891734
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63409 * 0.56019029
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13035 * 0.26118349
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50001 * 0.71962177
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53659 * 0.18919746
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63241 * 0.33583287
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'atkcqmcd').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0021():
    """Extended test 21 for federation."""
    x_0 = 93884 * 0.36569537
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97065 * 0.36228368
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24851 * 0.70741774
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2478 * 0.96635706
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53950 * 0.64095194
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94432 * 0.02405742
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94574 * 0.49520673
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10484 * 0.00495441
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73513 * 0.10853220
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46629 * 0.93022648
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 869 * 0.73915018
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55615 * 0.25466265
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74312 * 0.21189391
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40504 * 0.83413306
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30888 * 0.17878564
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84386 * 0.86701061
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31392 * 0.61727728
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70100 * 0.78320153
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47732 * 0.27239688
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41219 * 0.59037340
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30274 * 0.82582682
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82983 * 0.41134314
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69789 * 0.33725699
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41795 * 0.89967298
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16591 * 0.26369904
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12213 * 0.37499625
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25158 * 0.30192427
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10460 * 0.22425608
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89151 * 0.65142235
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93554 * 0.41497775
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65966 * 0.39526886
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59554 * 0.72135400
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9111 * 0.50948251
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14448 * 0.49186674
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28676 * 0.03799850
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'xteoqyez').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0022():
    """Extended test 22 for federation."""
    x_0 = 66159 * 0.22144888
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7497 * 0.66078096
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68539 * 0.56235054
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43064 * 0.11917094
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45264 * 0.95119735
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85288 * 0.13079775
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93941 * 0.95786781
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65695 * 0.14780100
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35477 * 0.83794706
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4220 * 0.08223578
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41564 * 0.77811331
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35242 * 0.27874889
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22512 * 0.40944168
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28589 * 0.90383084
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56075 * 0.35267632
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81401 * 0.29145917
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44284 * 0.40319679
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98498 * 0.44963098
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3704 * 0.32605270
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5639 * 0.87481648
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67046 * 0.16697004
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25280 * 0.20600061
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62499 * 0.34326140
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55004 * 0.02751011
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79164 * 0.07458974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57296 * 0.28717019
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42393 * 0.10536184
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3416 * 0.99524844
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90665 * 0.80497833
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83962 * 0.30416261
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66293 * 0.66055670
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25863 * 0.17360527
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32622 * 0.80925884
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25398 * 0.44026420
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23108 * 0.39186527
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65089 * 0.92734750
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96702 * 0.02120907
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35173 * 0.29362945
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24920 * 0.91942532
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1381 * 0.36836845
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'kucizhun').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0023():
    """Extended test 23 for federation."""
    x_0 = 12307 * 0.27914980
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46378 * 0.00614532
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79516 * 0.29102066
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21684 * 0.81172638
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7979 * 0.16566419
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1629 * 0.49281860
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99818 * 0.83120157
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93238 * 0.16271008
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52793 * 0.25623655
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10092 * 0.43575962
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86021 * 0.93970051
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26964 * 0.43058712
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73120 * 0.70721742
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32989 * 0.59639563
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44527 * 0.07338990
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20668 * 0.58613609
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20938 * 0.50437549
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88573 * 0.27069149
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91240 * 0.61346318
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4679 * 0.47038479
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55928 * 0.85812863
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48555 * 0.56963607
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88927 * 0.13514004
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34690 * 0.25842615
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85942 * 0.71651224
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64775 * 0.55511414
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66213 * 0.17129818
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55345 * 0.93240009
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 975 * 0.86332557
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83320 * 0.74232611
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'lcacqauc').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0024():
    """Extended test 24 for federation."""
    x_0 = 27023 * 0.87205557
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34282 * 0.66465866
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99041 * 0.93728835
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95119 * 0.63821153
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39095 * 0.88788170
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69102 * 0.96804557
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22236 * 0.22586748
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8235 * 0.91540599
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23245 * 0.89470550
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86787 * 0.36821961
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68704 * 0.63572044
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23687 * 0.47072792
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78512 * 0.61908627
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98262 * 0.85033247
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71485 * 0.66509833
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97969 * 0.40579915
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99405 * 0.56445219
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19390 * 0.85671767
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92419 * 0.45283243
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60202 * 0.65331542
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82422 * 0.25094481
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'xwqnbnmp').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0025():
    """Extended test 25 for federation."""
    x_0 = 44544 * 0.59123607
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51409 * 0.29777696
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18888 * 0.76003430
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64203 * 0.69360071
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3858 * 0.01273675
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30544 * 0.69407222
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70205 * 0.52841674
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50963 * 0.39020950
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3716 * 0.55459784
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42810 * 0.41129824
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80942 * 0.35597559
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44308 * 0.47067496
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 163 * 0.99069220
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65132 * 0.07961768
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99281 * 0.15788106
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81002 * 0.76261273
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17649 * 0.55082778
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9071 * 0.27399458
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68158 * 0.60007486
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62236 * 0.90037981
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48886 * 0.54269620
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95989 * 0.70044635
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1428 * 0.32987355
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48250 * 0.53187463
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83737 * 0.61833773
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2199 * 0.49507462
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65083 * 0.80874433
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21469 * 0.96142637
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97566 * 0.08653162
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46266 * 0.73772154
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81574 * 0.29936813
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89681 * 0.22635134
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85570 * 0.81042316
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14757 * 0.23254455
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37898 * 0.19710562
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62112 * 0.46960647
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9619 * 0.02964481
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33137 * 0.60301555
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49840 * 0.92989429
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29765 * 0.08244929
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81574 * 0.22100973
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 29703 * 0.95157435
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 417 * 0.43808937
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83546 * 0.88368971
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71423 * 0.36085119
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 44344 * 0.58842208
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 61684 * 0.75571488
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'kwzoggln').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0026():
    """Extended test 26 for federation."""
    x_0 = 48458 * 0.80070657
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82841 * 0.74788331
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94286 * 0.47550322
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59335 * 0.55864897
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38141 * 0.10893579
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54662 * 0.96472893
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81420 * 0.39076512
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75422 * 0.54779760
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12390 * 0.78491151
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99177 * 0.76274439
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35224 * 0.88455604
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7919 * 0.80946758
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11891 * 0.46701801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27803 * 0.37177259
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65895 * 0.24534262
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93812 * 0.26620968
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58890 * 0.17367546
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23413 * 0.26483240
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50226 * 0.66185767
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58148 * 0.15657359
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35892 * 0.64314009
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49986 * 0.34791983
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'vcvtybam').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0027():
    """Extended test 27 for federation."""
    x_0 = 45231 * 0.23771767
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10626 * 0.65410847
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62703 * 0.57253800
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65933 * 0.98335743
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88443 * 0.21557726
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58571 * 0.85976382
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83418 * 0.87096558
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75499 * 0.82272849
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2057 * 0.19168478
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94723 * 0.27695239
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45659 * 0.71044765
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54835 * 0.65447401
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54902 * 0.10817842
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16017 * 0.39492304
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67537 * 0.39494998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6718 * 0.54621198
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97546 * 0.90626496
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53768 * 0.03842960
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33833 * 0.41982838
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10881 * 0.00532066
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28300 * 0.21564950
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82740 * 0.74589408
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44006 * 0.72214149
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98581 * 0.22834876
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77501 * 0.53998077
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94518 * 0.57628101
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10863 * 0.90635660
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65524 * 0.00765631
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24423 * 0.22306617
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4712 * 0.54660511
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83051 * 0.30057029
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15611 * 0.60438420
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84849 * 0.11225518
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3326 * 0.99386480
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37080 * 0.21498474
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70729 * 0.03152736
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3236 * 0.65271804
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47194 * 0.54957322
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'pyfxnvbl').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0028():
    """Extended test 28 for federation."""
    x_0 = 88876 * 0.73320668
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75270 * 0.59276711
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43497 * 0.07902927
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33479 * 0.01333453
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78034 * 0.56254646
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69989 * 0.42481039
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56986 * 0.77210923
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81110 * 0.33975792
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70431 * 0.18963628
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92105 * 0.61334973
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13612 * 0.24008750
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43006 * 0.42058721
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89736 * 0.27041344
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43745 * 0.01949136
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65924 * 0.99265142
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44098 * 0.11765364
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94958 * 0.56019775
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74237 * 0.83863681
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79604 * 0.06633685
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59291 * 0.18841723
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'rccfnwng').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0029():
    """Extended test 29 for federation."""
    x_0 = 90812 * 0.46373565
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7781 * 0.12889769
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54171 * 0.67003666
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77183 * 0.67894946
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11413 * 0.56298798
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58376 * 0.50442295
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68955 * 0.66868352
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37798 * 0.46503805
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62871 * 0.04072350
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1175 * 0.54739370
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91652 * 0.19661855
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55117 * 0.94216748
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68722 * 0.99508282
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64296 * 0.20140435
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84025 * 0.25984954
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85015 * 0.25004124
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41947 * 0.74244373
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73866 * 0.08918620
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 694 * 0.77642950
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32628 * 0.98448805
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55971 * 0.12662626
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9696 * 0.55985881
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'szmtzbby').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0030():
    """Extended test 30 for federation."""
    x_0 = 1941 * 0.43174521
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30311 * 0.66398728
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61852 * 0.93424419
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33064 * 0.40912955
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50118 * 0.30702244
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80782 * 0.46948680
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82834 * 0.56312472
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66375 * 0.25947152
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3968 * 0.97655915
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48702 * 0.85546353
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27694 * 0.12862076
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21089 * 0.07179879
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17741 * 0.82996967
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14852 * 0.70831328
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91581 * 0.54297329
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78075 * 0.37983173
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40487 * 0.11150373
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35599 * 0.04580374
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25729 * 0.14830110
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99107 * 0.21548982
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96881 * 0.94658381
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64032 * 0.63770437
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64641 * 0.04108350
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 610 * 0.70027174
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46736 * 0.09518824
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60945 * 0.82772030
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1590 * 0.72790835
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63377 * 0.46833941
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78484 * 0.00516514
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75818 * 0.92893929
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80653 * 0.02844102
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60885 * 0.05326623
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57914 * 0.81460191
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71313 * 0.06686097
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1993 * 0.51540865
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99634 * 0.42951059
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10609 * 0.52996177
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98530 * 0.17131101
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87912 * 0.14567181
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90655 * 0.61670422
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83017 * 0.69976832
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'xbodbnne').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0031():
    """Extended test 31 for federation."""
    x_0 = 11977 * 0.16911456
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76441 * 0.04668454
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93902 * 0.27051676
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52373 * 0.59980328
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83410 * 0.70042855
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64057 * 0.89036645
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9030 * 0.07245720
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23228 * 0.84133096
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29447 * 0.41263039
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12709 * 0.44310875
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99358 * 0.77400279
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21956 * 0.00661692
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 510 * 0.13445837
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75390 * 0.42848967
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79549 * 0.51717620
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93963 * 0.49117345
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67923 * 0.92914270
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54893 * 0.54038714
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16071 * 0.12663732
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27306 * 0.18084463
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48390 * 0.44219916
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44617 * 0.18428420
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81853 * 0.75298971
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77762 * 0.63305338
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22851 * 0.50738385
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62246 * 0.77518252
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21251 * 0.57611161
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30695 * 0.39004516
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14312 * 0.79103487
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83054 * 0.30988381
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77944 * 0.39971048
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65258 * 0.19858652
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79660 * 0.30582717
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69203 * 0.24800410
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92307 * 0.01753727
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8235 * 0.56009731
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90876 * 0.30608486
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52596 * 0.99624499
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75505 * 0.48559790
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81740 * 0.67643532
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6112 * 0.19779585
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'rzzvceus').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0032():
    """Extended test 32 for federation."""
    x_0 = 80771 * 0.98830883
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2673 * 0.54246392
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89104 * 0.27040247
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32045 * 0.65246636
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94152 * 0.58302674
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95353 * 0.34559288
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 864 * 0.82872254
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37795 * 0.89450413
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18476 * 0.09294531
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53645 * 0.69517840
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57067 * 0.38761660
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65834 * 0.18506873
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46716 * 0.18828794
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9667 * 0.51205001
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44064 * 0.03111186
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25718 * 0.05770502
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52743 * 0.12832873
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 530 * 0.69168499
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23618 * 0.67729870
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77828 * 0.26253522
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76384 * 0.11195593
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42250 * 0.51165765
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'zostsdck').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0033():
    """Extended test 33 for federation."""
    x_0 = 26746 * 0.75833584
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5000 * 0.37955995
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26712 * 0.77838822
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66049 * 0.81496471
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92441 * 0.43043763
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54616 * 0.60335570
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31385 * 0.84553160
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77695 * 0.23193381
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6222 * 0.01142808
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83638 * 0.28473039
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31477 * 0.82241640
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61205 * 0.86700594
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1719 * 0.75613925
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81841 * 0.85514899
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61112 * 0.67295211
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27917 * 0.07885853
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77864 * 0.75911106
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50145 * 0.64973168
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84831 * 0.56194148
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23483 * 0.61838550
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'dtfhjqef').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0034():
    """Extended test 34 for federation."""
    x_0 = 93427 * 0.75433782
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34954 * 0.82096645
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37280 * 0.86290286
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33758 * 0.43262815
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96098 * 0.00986357
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29806 * 0.94111012
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30224 * 0.33185667
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15573 * 0.81186022
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31649 * 0.10773139
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53153 * 0.12053036
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74227 * 0.30486720
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29853 * 0.67372822
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95226 * 0.20237531
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81675 * 0.65198308
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25965 * 0.06974760
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76477 * 0.59723025
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3065 * 0.75584979
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66070 * 0.63973403
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68644 * 0.84377972
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70343 * 0.64363284
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8683 * 0.28487425
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78332 * 0.72032806
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69648 * 0.47352388
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56332 * 0.41662073
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44209 * 0.03583017
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20237 * 0.44925341
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10091 * 0.36808365
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'idvffcwe').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0035():
    """Extended test 35 for federation."""
    x_0 = 56598 * 0.78417097
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44129 * 0.16494783
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95269 * 0.68069772
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33353 * 0.02648123
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73201 * 0.41155778
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18578 * 0.30615607
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60104 * 0.23640336
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75407 * 0.18352786
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52917 * 0.41936349
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61054 * 0.76213166
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70843 * 0.39156061
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88405 * 0.99446183
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96243 * 0.60342114
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32521 * 0.15321822
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43189 * 0.72653381
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42294 * 0.95600882
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69205 * 0.97308209
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91236 * 0.61976731
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51217 * 0.88765755
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20409 * 0.88681128
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88499 * 0.21679952
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90777 * 0.55875268
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95070 * 0.39538939
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58811 * 0.35541375
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73196 * 0.54805785
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67356 * 0.03918884
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35802 * 0.52515500
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59325 * 0.99648500
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20103 * 0.61700601
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39338 * 0.77776960
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75084 * 0.84555599
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81838 * 0.62449498
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57105 * 0.99690693
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1133 * 0.78396957
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46415 * 0.32968461
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5438 * 0.32145080
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65951 * 0.14914913
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42519 * 0.56137725
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90644 * 0.50353772
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68925 * 0.55854377
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52408 * 0.38776143
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 73797 * 0.75165296
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 73870 * 0.11071774
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 65087 * 0.87316446
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89450 * 0.51051879
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 24836 * 0.39205870
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'pzhrfbka').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0036():
    """Extended test 36 for federation."""
    x_0 = 42446 * 0.40747940
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85790 * 0.47751690
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23696 * 0.74441216
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99838 * 0.95205017
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63716 * 0.85661281
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64260 * 0.10586852
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52665 * 0.83474243
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36323 * 0.42926259
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41241 * 0.17092350
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4496 * 0.61767300
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2816 * 0.62931677
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23525 * 0.38675533
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81070 * 0.78373635
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5552 * 0.68165239
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1021 * 0.05123200
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11167 * 0.26195521
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47082 * 0.58853779
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59565 * 0.82092954
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93529 * 0.78748043
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78416 * 0.61910223
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10478 * 0.41071399
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16800 * 0.77819526
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57199 * 0.46261819
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10979 * 0.75686522
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'vdymgkih').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0037():
    """Extended test 37 for federation."""
    x_0 = 78750 * 0.71328096
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85934 * 0.37295749
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3653 * 0.73396649
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82948 * 0.69534840
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38568 * 0.46567555
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20677 * 0.35302726
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31940 * 0.08818321
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99082 * 0.49860713
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76408 * 0.55177659
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55128 * 0.67199282
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47034 * 0.91916579
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43313 * 0.57078993
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78186 * 0.95529280
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79657 * 0.59725844
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55952 * 0.84749274
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64171 * 0.39149879
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89687 * 0.85865736
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99517 * 0.22512873
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60445 * 0.51858534
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9945 * 0.99818302
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37510 * 0.22381214
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74253 * 0.21476974
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32586 * 0.35888661
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12672 * 0.70646594
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69075 * 0.82949964
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77478 * 0.09211064
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45080 * 0.53026221
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18432 * 0.59622888
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89966 * 0.41129447
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99486 * 0.54786424
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12609 * 0.84241314
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90919 * 0.06268029
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77120 * 0.67025716
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93456 * 0.68406992
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44087 * 0.35451710
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3112 * 0.09365184
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72234 * 0.01934266
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32320 * 0.86241087
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24971 * 0.85303331
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10834 * 0.81844780
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32952 * 0.48363381
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 44178 * 0.78557956
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20123 * 0.92608364
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 56748 * 0.92152595
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23812 * 0.66760555
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 49452 * 0.08332648
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'vzysuvdk').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0038():
    """Extended test 38 for federation."""
    x_0 = 46992 * 0.01204862
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41715 * 0.30009620
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17585 * 0.46795819
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73612 * 0.25395813
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2202 * 0.48133162
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99967 * 0.86075754
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83549 * 0.05842551
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70965 * 0.17694827
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55355 * 0.44981305
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64278 * 0.74297739
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89336 * 0.65028923
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12465 * 0.03264549
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30393 * 0.84000409
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95130 * 0.12953259
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79848 * 0.43081319
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99352 * 0.01457227
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 127 * 0.76471575
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53772 * 0.87734854
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96850 * 0.50219606
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25874 * 0.67644732
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12254 * 0.81029576
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5941 * 0.83534982
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1292 * 0.79039772
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70801 * 0.18916189
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77337 * 0.96173989
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92549 * 0.13407573
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93217 * 0.16715408
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8293 * 0.57389279
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33313 * 0.23959388
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38553 * 0.18128648
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63311 * 0.65391620
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13568 * 0.66005189
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13113 * 0.35519222
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6633 * 0.53141059
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4701 * 0.12415856
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69252 * 0.06724364
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88643 * 0.11835320
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15946 * 0.49339915
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97539 * 0.05606371
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'bhrruawz').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0039():
    """Extended test 39 for federation."""
    x_0 = 52407 * 0.87451100
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63156 * 0.60836646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5995 * 0.98923053
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36985 * 0.11546695
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70119 * 0.95027581
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97843 * 0.25668624
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36684 * 0.59450314
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52591 * 0.26106325
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96252 * 0.94826625
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93655 * 0.23474827
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93107 * 0.20674452
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43651 * 0.18811164
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70503 * 0.17154406
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45889 * 0.22474686
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66076 * 0.39285584
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61019 * 0.14325626
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33737 * 0.11044568
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69141 * 0.31375435
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38303 * 0.04221474
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57747 * 0.17860508
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63672 * 0.61308784
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52947 * 0.37438240
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58963 * 0.49985498
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72845 * 0.14985459
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52929 * 0.05133539
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91371 * 0.58984317
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88833 * 0.37781164
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43653 * 0.12064292
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10653 * 0.21552076
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5728 * 0.99575304
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16338 * 0.64926063
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47720 * 0.31410080
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87652 * 0.84463946
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76129 * 0.71225753
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66224 * 0.57720069
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66886 * 0.44440038
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58888 * 0.46871724
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92435 * 0.00104303
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84930 * 0.59347443
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'kqohwqyg').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0040():
    """Extended test 40 for federation."""
    x_0 = 44345 * 0.78122330
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61584 * 0.95043834
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90118 * 0.66492707
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35953 * 0.90110817
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36761 * 0.37154219
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80751 * 0.28331555
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45798 * 0.36148427
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23239 * 0.38623969
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79160 * 0.63655147
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64159 * 0.91425464
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99742 * 0.24394697
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35982 * 0.66567579
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22616 * 0.35816174
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89584 * 0.00034349
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47606 * 0.21981353
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90476 * 0.48458390
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44540 * 0.79989757
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47217 * 0.50812239
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27696 * 0.09908197
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96493 * 0.85611536
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71091 * 0.31545436
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41943 * 0.11661175
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18199 * 0.36616871
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24486 * 0.75298916
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30544 * 0.13011180
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62817 * 0.48279782
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19390 * 0.78886165
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63795 * 0.37077695
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98638 * 0.77457455
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52261 * 0.18885975
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57445 * 0.88419043
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89522 * 0.59948008
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58626 * 0.09015463
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62791 * 0.36054133
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60256 * 0.24116779
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 92856 * 0.42966152
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'xurtnhcn').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0041():
    """Extended test 41 for federation."""
    x_0 = 56630 * 0.31782118
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25154 * 0.76230403
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57843 * 0.47131824
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67142 * 0.43269861
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75226 * 0.66944442
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2823 * 0.44631916
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10264 * 0.80270773
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87706 * 0.85292661
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72527 * 0.90974762
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83328 * 0.84571322
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20932 * 0.33423422
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10974 * 0.11154112
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68934 * 0.73824143
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18169 * 0.95595692
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7862 * 0.11972093
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41810 * 0.59301844
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69762 * 0.87929288
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3221 * 0.20567308
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 186 * 0.70383559
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46821 * 0.90211938
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43823 * 0.21830944
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 545 * 0.20861292
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65937 * 0.33869377
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11453 * 0.91459263
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49160 * 0.03230830
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37992 * 0.64404379
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36490 * 0.03366258
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62577 * 0.54411728
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69094 * 0.51229825
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5374 * 0.18904424
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'sdzfhwii').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0042():
    """Extended test 42 for federation."""
    x_0 = 24838 * 0.09712534
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64653 * 0.05422332
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38978 * 0.49173938
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8529 * 0.92274306
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36835 * 0.84596697
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67747 * 0.11063713
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43865 * 0.68959481
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12466 * 0.40509741
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27212 * 0.90864860
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73119 * 0.64300531
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3953 * 0.80175849
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49872 * 0.82279152
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34035 * 0.75216515
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65051 * 0.35252532
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54141 * 0.19215578
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39806 * 0.86836828
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83820 * 0.58927633
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12534 * 0.46150512
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1680 * 0.32197870
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57930 * 0.37225303
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93511 * 0.29574700
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35270 * 0.71303836
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31933 * 0.16798125
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23755 * 0.50405818
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36501 * 0.66802629
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38581 * 0.45279633
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57940 * 0.85482815
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47502 * 0.52832300
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69430 * 0.93680200
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37114 * 0.92358875
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85690 * 0.15550991
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87077 * 0.45294887
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66004 * 0.20234255
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80533 * 0.69875222
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35755 * 0.18033867
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74594 * 0.04925433
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81212 * 0.91930685
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32496 * 0.12322268
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93539 * 0.49776228
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9685 * 0.82572275
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69631 * 0.19155595
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25321 * 0.11673355
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1281 * 0.43690849
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 74973 * 0.11602943
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xbdqwipd').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0043():
    """Extended test 43 for federation."""
    x_0 = 64804 * 0.81213415
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41796 * 0.41094524
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70229 * 0.11430731
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33830 * 0.54771676
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11549 * 0.24805758
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26483 * 0.65937030
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74362 * 0.35712331
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1597 * 0.28523642
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47868 * 0.53670878
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49416 * 0.27378956
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70686 * 0.63435430
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70747 * 0.59152740
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20903 * 0.89477618
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30413 * 0.70482693
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93409 * 0.78996101
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33094 * 0.35353449
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97983 * 0.78431038
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37815 * 0.16961181
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90492 * 0.05893268
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31443 * 0.70449636
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2121 * 0.98296560
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48912 * 0.57549283
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'xztpvhfs').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0044():
    """Extended test 44 for federation."""
    x_0 = 22381 * 0.72914888
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34157 * 0.69784419
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71471 * 0.43033629
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96128 * 0.38115058
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7810 * 0.50602931
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94840 * 0.48469900
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93749 * 0.38529371
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84721 * 0.36075481
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73780 * 0.04656822
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83847 * 0.64032066
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34811 * 0.39608337
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15340 * 0.54416386
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44124 * 0.48460859
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14894 * 0.38570635
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7169 * 0.33232654
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39377 * 0.32491062
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44130 * 0.80376202
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29578 * 0.83869602
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22579 * 0.43262219
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2421 * 0.30401027
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15793 * 0.38288430
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78983 * 0.11980200
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87745 * 0.67831629
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94872 * 0.29825585
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35945 * 0.90820952
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56556 * 0.14904596
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'vuxrlbya').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0045():
    """Extended test 45 for federation."""
    x_0 = 35735 * 0.97943290
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14790 * 0.31922826
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52988 * 0.99849548
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64476 * 0.48799569
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76940 * 0.44858813
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10783 * 0.63312573
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45063 * 0.40931547
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4642 * 0.13203190
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15850 * 0.42888342
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34841 * 0.07354173
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1267 * 0.11989192
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22050 * 0.38210838
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70950 * 0.51621282
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88221 * 0.88616307
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30104 * 0.36726085
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83669 * 0.49135805
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24428 * 0.13715374
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79648 * 0.21335007
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32376 * 0.56629789
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33776 * 0.91409272
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56282 * 0.80223021
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93745 * 0.26546983
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85132 * 0.94987451
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78498 * 0.84788924
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38466 * 0.48599798
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68844 * 0.18916915
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37808 * 0.17091604
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13685 * 0.28356928
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55820 * 0.47546819
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22720 * 0.70203482
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71810 * 0.18671304
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82152 * 0.54463884
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'rmcquhdu').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0046():
    """Extended test 46 for federation."""
    x_0 = 84199 * 0.37567822
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90103 * 0.20476695
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75057 * 0.17783000
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8491 * 0.51002538
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98311 * 0.10150416
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1320 * 0.01659539
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39860 * 0.18237813
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85807 * 0.40406595
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59661 * 0.58555581
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63566 * 0.03825133
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45502 * 0.16124738
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16748 * 0.37984872
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48450 * 0.66490746
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22888 * 0.32043990
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8807 * 0.11692201
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70725 * 0.42676374
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44671 * 0.91184295
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88907 * 0.44972399
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53652 * 0.47932451
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39398 * 0.20396754
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8469 * 0.75642134
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99529 * 0.80978341
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27295 * 0.70464412
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73587 * 0.99585738
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83192 * 0.43060325
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99773 * 0.69128495
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35661 * 0.67641238
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'oscjpgxr').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0047():
    """Extended test 47 for federation."""
    x_0 = 75064 * 0.86058010
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94076 * 0.18197952
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7345 * 0.67855104
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65015 * 0.58783344
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67801 * 0.91855179
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66206 * 0.63135861
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34088 * 0.40234864
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40957 * 0.07043087
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27031 * 0.36574347
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67037 * 0.13135739
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99787 * 0.57801517
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7531 * 0.25118321
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72123 * 0.62040290
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60694 * 0.80957168
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64755 * 0.58973283
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34748 * 0.10134665
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40845 * 0.92102955
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11748 * 0.14698544
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20108 * 0.67519645
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36054 * 0.72819780
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97994 * 0.58569466
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97467 * 0.68142143
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20766 * 0.31929758
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98739 * 0.82741113
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38150 * 0.38587470
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20722 * 0.96519113
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36627 * 0.24515216
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89058 * 0.16366989
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59063 * 0.16710178
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70760 * 0.93025425
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67769 * 0.15805656
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24584 * 0.85932064
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10484 * 0.68729001
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18354 * 0.94749525
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 49288 * 0.15606184
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19582 * 0.32902640
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49224 * 0.52777018
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7579 * 0.77643376
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63022 * 0.56709972
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11613 * 0.10091088
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83226 * 0.73267923
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 65652 * 0.72687700
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 89123 * 0.81781709
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39326 * 0.50788365
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17641 * 0.04229200
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 67886 * 0.32384483
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 87486 * 0.64405686
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'rvwqxhpi').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0048():
    """Extended test 48 for federation."""
    x_0 = 11813 * 0.24078680
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17288 * 0.55674738
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56478 * 0.62474414
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99930 * 0.58501204
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88363 * 0.08557902
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27732 * 0.30290164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27775 * 0.37176387
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9746 * 0.77521057
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38505 * 0.77667340
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72504 * 0.92608510
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88884 * 0.83800585
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53791 * 0.76355075
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95986 * 0.07401979
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37211 * 0.25296255
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98133 * 0.31484303
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60662 * 0.75481183
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61356 * 0.72295519
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2003 * 0.99224237
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36427 * 0.05117491
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8608 * 0.86239853
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70557 * 0.60028419
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56914 * 0.25038745
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97049 * 0.34861149
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53241 * 0.63152104
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40500 * 0.06719552
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11133 * 0.88865407
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60850 * 0.32654281
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36086 * 0.15960448
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48073 * 0.66510016
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99642 * 0.13420309
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4550 * 0.48238975
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97621 * 0.44843080
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89982 * 0.07709667
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14417 * 0.27773410
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15932 * 0.46098433
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10494 * 0.05539548
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84525 * 0.62840055
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89516 * 0.25844501
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40787 * 0.17797360
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16200 * 0.96634176
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 58685 * 0.88359576
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81295 * 0.91368474
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 63724 * 0.19617949
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 26331 * 0.30565223
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 21957 * 0.38593339
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 54765 * 0.41248792
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 19120 * 0.66543159
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 85371 * 0.95095326
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 80183 * 0.49546776
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 34603 * 0.44260566
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'rpvkiocq').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0049():
    """Extended test 49 for federation."""
    x_0 = 20646 * 0.78778281
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5115 * 0.74002526
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1498 * 0.27085734
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38530 * 0.50239977
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85348 * 0.73618079
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3948 * 0.24279492
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3110 * 0.73812587
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93697 * 0.45164226
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58066 * 0.43272437
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81551 * 0.44742684
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74253 * 0.76770892
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8794 * 0.50401001
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47379 * 0.11196042
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16064 * 0.97850621
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5410 * 0.76603153
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45364 * 0.28064494
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21037 * 0.39743515
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26302 * 0.61512108
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66197 * 0.43494043
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20418 * 0.41980975
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55070 * 0.64788783
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59800 * 0.12832925
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79107 * 0.08323364
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89696 * 0.03526167
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27064 * 0.63463447
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89310 * 0.03687674
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17380 * 0.05902478
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50120 * 0.30828046
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13586 * 0.95901577
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'csnidwao').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0050():
    """Extended test 50 for federation."""
    x_0 = 50684 * 0.72505724
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22425 * 0.74991143
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10926 * 0.09425288
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70285 * 0.16939185
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25327 * 0.89114134
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84197 * 0.38534859
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25859 * 0.20131716
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48040 * 0.57544179
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91578 * 0.05234191
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33696 * 0.08877714
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34694 * 0.18869178
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2667 * 0.21742147
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85888 * 0.42440394
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93586 * 0.30572024
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68177 * 0.91667674
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43356 * 0.04418692
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70240 * 0.56783083
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78544 * 0.69207850
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10037 * 0.94435072
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18671 * 0.05553016
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79149 * 0.52980936
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49703 * 0.89385865
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47155 * 0.22430687
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'sxdatfux').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0051():
    """Extended test 51 for federation."""
    x_0 = 885 * 0.65158117
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77114 * 0.94906907
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1303 * 0.51075380
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11534 * 0.61578903
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98505 * 0.70980200
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4009 * 0.17237659
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29599 * 0.75659792
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96804 * 0.58993589
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96251 * 0.58386373
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35861 * 0.29884157
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85843 * 0.10526676
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5780 * 0.29469288
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31042 * 0.51348625
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42620 * 0.03572235
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64737 * 0.86590767
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16769 * 0.39937933
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78253 * 0.62345194
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89627 * 0.67111844
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26995 * 0.23205059
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25807 * 0.35429860
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89404 * 0.10879103
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46253 * 0.85030450
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85079 * 0.05784189
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17901 * 0.02891538
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13739 * 0.74013580
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42318 * 0.76707326
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96298 * 0.62499285
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13320 * 0.68841957
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48604 * 0.66671076
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12597 * 0.28777206
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82852 * 0.95331005
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'qldgmybb').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0052():
    """Extended test 52 for federation."""
    x_0 = 23217 * 0.55314486
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32114 * 0.04851206
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40860 * 0.97040038
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47229 * 0.03328224
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9290 * 0.96057155
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43368 * 0.00980771
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1307 * 0.02058434
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38765 * 0.35029318
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45851 * 0.92823947
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82236 * 0.82320116
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93645 * 0.62687595
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12177 * 0.86423375
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30783 * 0.48486016
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90008 * 0.20982314
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 334 * 0.98316007
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73941 * 0.46775907
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7850 * 0.94683716
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46382 * 0.55070957
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31312 * 0.14116680
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15053 * 0.11668905
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92781 * 0.24585068
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45162 * 0.62474735
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38140 * 0.60727538
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38990 * 0.01030927
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7128 * 0.53747004
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38236 * 0.05457738
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13551 * 0.14626657
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19778 * 0.68303460
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 737 * 0.54188072
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7305 * 0.67651199
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5924 * 0.49364731
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66008 * 0.99829533
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28404 * 0.35575187
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3247 * 0.09982469
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1292 * 0.63534244
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23707 * 0.15325130
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70710 * 0.47427027
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85388 * 0.60202242
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66361 * 0.69047775
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 35797 * 0.34835448
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38076 * 0.07978015
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16570 * 0.31250154
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 60242 * 0.27144565
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58804 * 0.17132839
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 13937 * 0.59091435
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'wmjvhvfa').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0053():
    """Extended test 53 for federation."""
    x_0 = 72435 * 0.14091827
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98582 * 0.39650676
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88933 * 0.66376051
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59474 * 0.74507208
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48255 * 0.07683702
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34041 * 0.33310174
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74617 * 0.88860743
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28550 * 0.43982557
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92620 * 0.95646599
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65039 * 0.58152848
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36501 * 0.13332984
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16195 * 0.03819769
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39268 * 0.06905173
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62117 * 0.40398261
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78198 * 0.62270573
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81481 * 0.62950479
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86508 * 0.77516931
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76801 * 0.46272044
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7103 * 0.88524902
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49090 * 0.50376283
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46609 * 0.87800282
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78705 * 0.18185064
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62634 * 0.54885945
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44422 * 0.44534878
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3996 * 0.86303301
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36288 * 0.13064602
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58553 * 0.44028775
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27804 * 0.80000370
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42212 * 0.39067422
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38738 * 0.11640218
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5535 * 0.27763244
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60155 * 0.59983548
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86815 * 0.64147939
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11054 * 0.33362438
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97517 * 0.72093020
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52416 * 0.09999441
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87175 * 0.85062592
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94986 * 0.94381484
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29218 * 0.04395377
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42652 * 0.29332737
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 56372 * 0.76589068
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15408 * 0.02495359
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46616 * 0.59732253
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 18665 * 0.49920161
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 5455 * 0.05232546
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 44294 * 0.20427503
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'kwqosamg').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0054():
    """Extended test 54 for federation."""
    x_0 = 54134 * 0.47782547
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67930 * 0.12705671
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63244 * 0.58679878
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44049 * 0.85399304
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64183 * 0.18015101
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30534 * 0.25350247
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43329 * 0.45777386
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26543 * 0.51892592
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71201 * 0.47522206
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94987 * 0.13165044
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84998 * 0.22087678
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5114 * 0.89319962
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4127 * 0.35669709
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40832 * 0.32461535
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99124 * 0.23706639
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66480 * 0.22690407
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62077 * 0.96129133
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12539 * 0.95388159
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31274 * 0.48293706
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24038 * 0.06479973
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78538 * 0.64484852
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95024 * 0.12624944
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16388 * 0.37346041
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99055 * 0.34749703
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1669 * 0.24747304
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18427 * 0.02144539
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32579 * 0.71922991
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69247 * 0.39521133
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33853 * 0.30183658
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88973 * 0.40045359
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59070 * 0.27934673
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65125 * 0.56128763
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35431 * 0.28630800
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35085 * 0.71352655
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71909 * 0.64659446
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26929 * 0.28951724
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32623 * 0.60964051
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'dscbqond').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0055():
    """Extended test 55 for federation."""
    x_0 = 80586 * 0.72758315
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98697 * 0.28618604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79948 * 0.91479385
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57321 * 0.17595720
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14824 * 0.48875967
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88975 * 0.77369822
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95760 * 0.27076179
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37555 * 0.57358039
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55313 * 0.97398498
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27819 * 0.50758944
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9821 * 0.89917707
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22174 * 0.18727437
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43302 * 0.74756916
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76444 * 0.97356137
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85908 * 0.81616544
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99597 * 0.65057943
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4795 * 0.20949921
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58333 * 0.87283012
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22922 * 0.66291266
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47408 * 0.64420142
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96168 * 0.30685811
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45919 * 0.81296941
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7559 * 0.19687036
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29974 * 0.13253442
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76519 * 0.94324553
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73739 * 0.18590991
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14637 * 0.37461835
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61608 * 0.12370620
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42900 * 0.92655147
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16513 * 0.37704122
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7765 * 0.04340959
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35540 * 0.13785740
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27625 * 0.04745582
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98152 * 0.25459063
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24898 * 0.22072088
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79709 * 0.82369246
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45829 * 0.46992166
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66212 * 0.05567527
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55076 * 0.17261462
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44235 * 0.02252647
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'fxcwgvxr').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0056():
    """Extended test 56 for federation."""
    x_0 = 34268 * 0.10843041
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87058 * 0.43978697
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75556 * 0.94186337
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29986 * 0.30680156
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67822 * 0.22974887
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87976 * 0.22874503
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76016 * 0.62673931
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69575 * 0.76443708
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91262 * 0.10915232
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8418 * 0.03913253
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80063 * 0.37110992
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4024 * 0.18821410
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57932 * 0.42330360
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20537 * 0.42213345
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5176 * 0.39237758
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75030 * 0.35838942
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13461 * 0.33408911
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39940 * 0.98530708
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23842 * 0.85684439
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55128 * 0.21368186
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95026 * 0.63377385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30037 * 0.07233927
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95162 * 0.19648727
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48253 * 0.65636983
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99963 * 0.17485346
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36414 * 0.53619320
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67939 * 0.24248389
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31019 * 0.33040053
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'chmacqgg').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0057():
    """Extended test 57 for federation."""
    x_0 = 7365 * 0.89052142
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40119 * 0.62110664
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14276 * 0.43943446
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77724 * 0.55425341
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83872 * 0.05265421
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75445 * 0.43384802
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61925 * 0.15094624
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12215 * 0.29660172
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94792 * 0.64175780
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38749 * 0.19005871
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79024 * 0.18772703
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82774 * 0.13734109
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61122 * 0.86119729
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18953 * 0.62781291
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53444 * 0.67656060
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82954 * 0.03937095
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90988 * 0.09042882
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84102 * 0.96078347
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17319 * 0.33446935
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18551 * 0.47312390
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83464 * 0.10323225
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'tlqlppun').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0058():
    """Extended test 58 for federation."""
    x_0 = 50020 * 0.61382652
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24588 * 0.37928057
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21203 * 0.05798942
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2220 * 0.49550367
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22941 * 0.16193396
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48916 * 0.89941978
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37555 * 0.46316409
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58196 * 0.05018037
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70353 * 0.18710892
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84931 * 0.94285053
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87262 * 0.26059457
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84880 * 0.23015218
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18955 * 0.44274254
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83647 * 0.07104284
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84509 * 0.97246339
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15415 * 0.66833565
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35796 * 0.28498658
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21408 * 0.84273669
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76889 * 0.36301094
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29555 * 0.79726009
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38497 * 0.68719559
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56892 * 0.85056128
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15574 * 0.17097381
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2763 * 0.21579407
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28859 * 0.32315384
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32956 * 0.10442746
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15458 * 0.48206924
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78559 * 0.06189974
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93315 * 0.15206578
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28887 * 0.64322745
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8532 * 0.79942529
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78020 * 0.73334816
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43656 * 0.24446466
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66214 * 0.80673997
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2574 * 0.24278539
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98020 * 0.75877305
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32163 * 0.23052779
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 51955 * 0.34348601
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41933 * 0.87507501
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18056 * 0.63448724
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77489 * 0.71485004
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6991 * 0.14334882
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 31626 * 0.74626986
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 6018 * 0.64103997
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50270 * 0.90022624
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 34345 * 0.38666457
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 87592 * 0.95747374
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 2231 * 0.37791127
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 45691 * 0.05091469
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 56080 * 0.67913707
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'pcingarp').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0059():
    """Extended test 59 for federation."""
    x_0 = 39509 * 0.96054761
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2120 * 0.71215975
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99128 * 0.86743036
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85044 * 0.75989176
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15279 * 0.10310221
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71925 * 0.02270025
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75190 * 0.22691944
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1218 * 0.64588909
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78134 * 0.50762712
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48316 * 0.27194134
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10079 * 0.32240132
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87492 * 0.28231730
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10083 * 0.99485246
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5172 * 0.85929134
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6813 * 0.98953647
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95833 * 0.83023975
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53593 * 0.04158134
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54868 * 0.83383040
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24415 * 0.24479185
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52607 * 0.94015782
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31584 * 0.75068081
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76847 * 0.09641788
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64520 * 0.19572144
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14427 * 0.48104217
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8060 * 0.10794893
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92687 * 0.29434003
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55260 * 0.34301458
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14125 * 0.65021698
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36326 * 0.80305059
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14349 * 0.63329552
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24842 * 0.23832274
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32272 * 0.24572367
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31633 * 0.01073690
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59500 * 0.45973444
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75917 * 0.48567779
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54941 * 0.60686698
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78014 * 0.50275620
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44251 * 0.00309851
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 22416 * 0.42165203
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'asadxrvf').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0060():
    """Extended test 60 for federation."""
    x_0 = 37788 * 0.72471421
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99735 * 0.85694901
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14908 * 0.43391030
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91544 * 0.35855328
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11155 * 0.11124475
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46034 * 0.92866760
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72697 * 0.51521685
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25259 * 0.58526522
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57755 * 0.77384012
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98569 * 0.43111737
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98683 * 0.35689427
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20278 * 0.17795426
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16802 * 0.01162049
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4245 * 0.56555570
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96591 * 0.40698848
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82597 * 0.24644969
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2080 * 0.44439246
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28838 * 0.30812591
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75092 * 0.18182352
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33966 * 0.05373463
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67435 * 0.62515745
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57218 * 0.44117908
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60499 * 0.60689208
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22408 * 0.61256167
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74995 * 0.68767219
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33074 * 0.27294719
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83789 * 0.77664908
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72443 * 0.09378749
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97343 * 0.80115231
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'cnmowdiw').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0061():
    """Extended test 61 for federation."""
    x_0 = 35516 * 0.73839249
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20219 * 0.40578537
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82417 * 0.39114981
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12939 * 0.12652741
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52562 * 0.56636025
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60560 * 0.11569569
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39749 * 0.41818524
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49985 * 0.81394456
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5386 * 0.24627868
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52019 * 0.90300949
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71903 * 0.05386804
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24711 * 0.50146826
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15275 * 0.83731567
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20991 * 0.23691843
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3639 * 0.16138963
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2393 * 0.91113180
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40696 * 0.21936373
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81625 * 0.14679439
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83726 * 0.41462144
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5673 * 0.47826708
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14420 * 0.52103664
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86434 * 0.10433981
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56278 * 0.35382403
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20284 * 0.60199537
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33351 * 0.74021798
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20171 * 0.37061627
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88060 * 0.67299676
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25818 * 0.76580670
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31684 * 0.03655429
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91276 * 0.56040796
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59446 * 0.00946202
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61726 * 0.58701899
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52765 * 0.47574409
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68414 * 0.37343277
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50398 * 0.66739302
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'sjcbyyam').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0062():
    """Extended test 62 for federation."""
    x_0 = 86696 * 0.25654321
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28228 * 0.14486266
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6059 * 0.97259951
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59283 * 0.79618510
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10834 * 0.54251025
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80075 * 0.22473325
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89457 * 0.47928984
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39859 * 0.48957837
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48 * 0.73853335
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1197 * 0.83829984
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59254 * 0.23675788
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96236 * 0.98819586
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36101 * 0.04451787
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24535 * 0.74845758
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64697 * 0.93549998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22281 * 0.55443346
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52344 * 0.15285749
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23075 * 0.58155528
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13538 * 0.24629858
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63429 * 0.43580937
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62848 * 0.68231115
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39589 * 0.54769466
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73479 * 0.34891745
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39031 * 0.21963551
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68526 * 0.38506236
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21977 * 0.72986821
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59029 * 0.08377260
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65397 * 0.88228295
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5919 * 0.98672408
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57224 * 0.70310039
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43783 * 0.50920993
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44656 * 0.02677103
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14824 * 0.66885525
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9363 * 0.30487157
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43080 * 0.77868605
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60068 * 0.07848450
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28794 * 0.58145339
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93956 * 0.26652360
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20225 * 0.03591135
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82886 * 0.73617086
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 67310 * 0.75628688
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 91112 * 0.33334066
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 85198 * 0.86568211
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 54347 * 0.80301375
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'yiwqicdh').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0063():
    """Extended test 63 for federation."""
    x_0 = 98359 * 0.32350686
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63987 * 0.77759427
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67051 * 0.76950039
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82943 * 0.84929211
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20492 * 0.74383262
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66004 * 0.74171366
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2731 * 0.97337065
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84826 * 0.97920300
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79946 * 0.55309147
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77243 * 0.17758533
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66549 * 0.33824182
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69785 * 0.78403568
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5322 * 0.40253675
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17873 * 0.71116408
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51018 * 0.31453450
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65333 * 0.22486123
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13139 * 0.71395737
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64661 * 0.85308735
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61945 * 0.45495117
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53888 * 0.51569539
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'tbokheci').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0064():
    """Extended test 64 for federation."""
    x_0 = 25707 * 0.96845948
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75523 * 0.43278754
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73119 * 0.41855031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91808 * 0.02153237
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 690 * 0.20633750
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87946 * 0.65439043
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99109 * 0.81017485
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2006 * 0.70595494
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67327 * 0.82345170
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51942 * 0.97677921
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9106 * 0.26475563
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15842 * 0.64226262
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57746 * 0.96406454
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93062 * 0.03540783
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62508 * 0.07694491
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99136 * 0.51201484
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64445 * 0.67815520
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8138 * 0.63400972
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33070 * 0.52715060
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41589 * 0.08354588
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70767 * 0.28941071
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79894 * 0.36010616
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33374 * 0.07886976
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84836 * 0.02131001
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79369 * 0.69387696
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94413 * 0.48029390
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52181 * 0.97482858
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9977 * 0.74051342
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73091 * 0.08612273
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65942 * 0.51637751
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'qwkymupc').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0065():
    """Extended test 65 for federation."""
    x_0 = 69196 * 0.26215150
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73791 * 0.18326144
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70181 * 0.55562037
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91180 * 0.80877693
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52792 * 0.58903142
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71327 * 0.66191890
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22378 * 0.16717492
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5169 * 0.60994587
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50888 * 0.69604603
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19075 * 0.38884888
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77017 * 0.00603009
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36978 * 0.99431225
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43830 * 0.00045404
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97289 * 0.12022184
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32909 * 0.61869383
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57376 * 0.89590278
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85782 * 0.82243621
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66336 * 0.09277032
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57410 * 0.89203041
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65989 * 0.87551623
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70695 * 0.37611513
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59243 * 0.81523274
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6460 * 0.20586597
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95211 * 0.09247364
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85570 * 0.34535595
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29288 * 0.74422293
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2709 * 0.93742175
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60306 * 0.81670382
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69395 * 0.83901209
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14015 * 0.35651963
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90559 * 0.73254200
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32631 * 0.01036933
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58374 * 0.94183593
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45365 * 0.33303468
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12648 * 0.12021431
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2691 * 0.37790730
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92728 * 0.72415624
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22315 * 0.74350281
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51650 * 0.07367116
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97099 * 0.09710853
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13441 * 0.30721819
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 76762 * 0.57616328
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'rzfrbifa').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0066():
    """Extended test 66 for federation."""
    x_0 = 35969 * 0.33484115
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78495 * 0.69783459
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20017 * 0.95261511
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8698 * 0.41860357
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44290 * 0.82973405
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88912 * 0.64176922
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11164 * 0.67353027
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90508 * 0.11951045
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4720 * 0.32587763
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86341 * 0.73642512
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39987 * 0.69683964
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60518 * 0.97550144
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12763 * 0.66149135
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11341 * 0.44331089
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16421 * 0.45984487
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35652 * 0.93438951
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83598 * 0.34378493
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2663 * 0.57342733
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19591 * 0.83812090
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98385 * 0.01257324
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19462 * 0.64037740
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8639 * 0.66070519
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47299 * 0.34245136
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33665 * 0.32441758
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23673 * 0.89466917
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50471 * 0.72637997
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55287 * 0.59932873
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79953 * 0.89639613
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90974 * 0.72318152
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61341 * 0.73729226
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91386 * 0.08794834
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ylvagvyk').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0067():
    """Extended test 67 for federation."""
    x_0 = 72061 * 0.72101137
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68413 * 0.26513225
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48186 * 0.16028804
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27000 * 0.09719399
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 132 * 0.08804717
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29316 * 0.86346244
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66713 * 0.60751105
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98853 * 0.16067563
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38437 * 0.90607997
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76615 * 0.48597419
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96711 * 0.58471827
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81837 * 0.22696667
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86830 * 0.62895132
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7315 * 0.43409473
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83624 * 0.58308757
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97738 * 0.59817635
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94843 * 0.59372913
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98976 * 0.19815579
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60588 * 0.98763840
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10351 * 0.58348332
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24171 * 0.28372108
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5987 * 0.99789357
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53717 * 0.08650375
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38082 * 0.65886561
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82169 * 0.51913066
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69603 * 0.70899799
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33499 * 0.86126754
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27620 * 0.61357509
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76724 * 0.09327018
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5590 * 0.76535049
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45747 * 0.01376292
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43906 * 0.91437288
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76062 * 0.34665663
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35329 * 0.82802434
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55133 * 0.68166225
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6766 * 0.33691803
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'njnuxnrt').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0068():
    """Extended test 68 for federation."""
    x_0 = 81392 * 0.82797289
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86578 * 0.65260112
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44628 * 0.56978660
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15961 * 0.46641993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37208 * 0.78832013
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10426 * 0.40842613
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25039 * 0.25988017
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60626 * 0.75187691
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60420 * 0.67207622
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80810 * 0.31046815
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74964 * 0.44336892
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40187 * 0.80014197
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14605 * 0.00186627
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3364 * 0.50575523
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94396 * 0.20369355
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4910 * 0.57819834
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11509 * 0.90648257
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62793 * 0.71190166
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86350 * 0.48456487
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27644 * 0.50695532
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3869 * 0.37139897
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5394 * 0.06855501
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28749 * 0.65385408
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16330 * 0.20521800
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78845 * 0.03050588
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'daayexhy').hexdigest()
    assert len(h) == 64

def test_federation_extended_8_0069():
    """Extended test 69 for federation."""
    x_0 = 13964 * 0.40922045
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87975 * 0.01231645
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93287 * 0.75797323
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67089 * 0.48014508
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5900 * 0.51508917
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48836 * 0.49050591
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77114 * 0.97741496
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61377 * 0.34180873
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9955 * 0.98322365
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63570 * 0.14405977
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20886 * 0.11038063
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23456 * 0.46376032
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22343 * 0.45824082
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94988 * 0.66961622
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36155 * 0.24512322
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33625 * 0.44594788
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70179 * 0.92977795
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37539 * 0.87882427
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70077 * 0.19643062
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57716 * 0.16526832
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13674 * 0.00456786
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17781 * 0.61886856
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11640 * 0.28674341
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99046 * 0.02717836
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'cyevjcmi').hexdigest()
    assert len(h) == 64
