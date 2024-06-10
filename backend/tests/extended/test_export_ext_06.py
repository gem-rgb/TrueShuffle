"""Extended tests for export suite 6."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_export_extended_6_0000():
    """Extended test 0 for export."""
    x_0 = 9263 * 0.80839669
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73024 * 0.54606372
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67045 * 0.33521566
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87781 * 0.72925849
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25128 * 0.34389944
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83973 * 0.33518628
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87171 * 0.59418969
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19890 * 0.06414560
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80216 * 0.77796648
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21939 * 0.58059909
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88017 * 0.86186017
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16215 * 0.05047514
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85879 * 0.73603745
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16365 * 0.16957948
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19107 * 0.47162022
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82593 * 0.76408008
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38057 * 0.41357634
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18740 * 0.53928855
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9520 * 0.78240961
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21796 * 0.06240470
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17062 * 0.14089064
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ftjkjehy').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0001():
    """Extended test 1 for export."""
    x_0 = 87391 * 0.07446245
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40994 * 0.25504867
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64195 * 0.94915717
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69227 * 0.63761381
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34524 * 0.66018325
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12769 * 0.70411300
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71629 * 0.46421982
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47109 * 0.32611518
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12530 * 0.40125413
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82491 * 0.33798840
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48228 * 0.44605262
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60817 * 0.33331952
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74687 * 0.07358293
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93599 * 0.38132460
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75248 * 0.97473143
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5485 * 0.61236009
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55555 * 0.23226025
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15279 * 0.86687513
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3324 * 0.04432338
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56833 * 0.92081147
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18536 * 0.78994702
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11820 * 0.20492141
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11150 * 0.71893584
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11937 * 0.23963675
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77356 * 0.10610017
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61914 * 0.29028797
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56921 * 0.07223795
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97021 * 0.08004347
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96777 * 0.42762452
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79958 * 0.62582988
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47471 * 0.34299446
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94806 * 0.50881365
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30540 * 0.03384396
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8194 * 0.40343415
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36588 * 0.94567224
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98851 * 0.96900484
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63070 * 0.30966736
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91800 * 0.47232152
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23715 * 0.11631336
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7532 * 0.45491781
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82239 * 0.99199119
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25746 * 0.30913008
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 69824 * 0.85176671
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92316 * 0.52929361
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 46223 * 0.19956841
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'mfvambmp').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0002():
    """Extended test 2 for export."""
    x_0 = 82142 * 0.12510540
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3984 * 0.00991803
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82625 * 0.41386288
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34853 * 0.47891906
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93960 * 0.59564539
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97515 * 0.23121860
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23790 * 0.99977568
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26237 * 0.88384585
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5636 * 0.09721911
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54179 * 0.43125971
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55352 * 0.78712823
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75392 * 0.42800950
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9095 * 0.89396285
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70739 * 0.67247015
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20579 * 0.89661466
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54897 * 0.89915807
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4790 * 0.41523507
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94985 * 0.57897038
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66015 * 0.11350719
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79908 * 0.74542760
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1853 * 0.02786778
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38658 * 0.83499200
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11754 * 0.31536291
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13222 * 0.02002503
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69995 * 0.29434615
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83006 * 0.56482485
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38460 * 0.39484426
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'zxpelvyd').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0003():
    """Extended test 3 for export."""
    x_0 = 38876 * 0.02283118
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77402 * 0.01995860
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5431 * 0.92666075
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77535 * 0.10328444
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52419 * 0.73088769
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70540 * 0.56810773
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55785 * 0.78394127
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34227 * 0.12855217
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43015 * 0.05098408
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30825 * 0.91407616
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12304 * 0.44616601
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72093 * 0.00395154
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98923 * 0.08051410
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15404 * 0.50494306
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98469 * 0.06095142
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30723 * 0.77608024
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64987 * 0.20524739
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9199 * 0.78907567
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99735 * 0.45897742
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78814 * 0.78212910
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19008 * 0.37855249
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75049 * 0.55567593
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16002 * 0.32008600
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76832 * 0.15013375
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39575 * 0.21345993
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50828 * 0.38964543
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78319 * 0.06241534
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37712 * 0.42295140
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26953 * 0.59532585
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72314 * 0.61796317
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67777 * 0.46286391
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46200 * 0.16420301
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72073 * 0.31769815
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53623 * 0.37786971
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20258 * 0.81051466
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64936 * 0.11191054
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93402 * 0.60084689
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36713 * 0.62687316
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96268 * 0.51368563
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 53986 * 0.80622237
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64914 * 0.52063385
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69200 * 0.40237578
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81348 * 0.37262623
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 42334 * 0.85340844
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 9985 * 0.52999773
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 72696 * 0.41268841
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 15943 * 0.85355227
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'hydfafvp').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0004():
    """Extended test 4 for export."""
    x_0 = 96153 * 0.02937275
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57033 * 0.48670147
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41707 * 0.65322754
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24938 * 0.49741475
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19071 * 0.50128210
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61969 * 0.29288520
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62642 * 0.17905660
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4702 * 0.77926214
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36745 * 0.48557399
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21774 * 0.35370584
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59203 * 0.28498136
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21142 * 0.87454392
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32847 * 0.56582830
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46723 * 0.57328220
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71522 * 0.75412031
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91988 * 0.70673772
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94792 * 0.21443352
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39818 * 0.40947356
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58230 * 0.13073801
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76610 * 0.54821999
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61170 * 0.62785266
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81690 * 0.15686352
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49272 * 0.83364266
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45165 * 0.48689080
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62802 * 0.97805783
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7775 * 0.95948221
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48674 * 0.43427584
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67485 * 0.18903224
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27846 * 0.89649843
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43279 * 0.25612173
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51736 * 0.06807593
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4773 * 0.45646520
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45569 * 0.20886946
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81596 * 0.17507797
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82814 * 0.11625857
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31066 * 0.88311630
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95574 * 0.28949065
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61692 * 0.56949619
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'aptvrcyh').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0005():
    """Extended test 5 for export."""
    x_0 = 47803 * 0.31667276
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23957 * 0.22025327
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44773 * 0.51069674
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98584 * 0.20327296
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94398 * 0.51564684
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82754 * 0.42788235
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86916 * 0.01081395
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67891 * 0.55172618
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26629 * 0.42564337
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52978 * 0.56391362
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79951 * 0.92626242
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49724 * 0.83810605
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29540 * 0.37631270
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59404 * 0.47717571
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82792 * 0.59542941
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57463 * 0.53319689
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92702 * 0.95943752
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41054 * 0.01746464
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30214 * 0.86101029
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5128 * 0.50674016
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96549 * 0.79002802
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46320 * 0.82462245
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95040 * 0.27215583
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77252 * 0.60215401
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25726 * 0.83963165
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64206 * 0.30366010
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23743 * 0.98265980
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89226 * 0.50328716
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79267 * 0.13050045
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50291 * 0.57943662
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17680 * 0.56771448
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8545 * 0.37186035
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14963 * 0.37545291
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14950 * 0.41604857
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77688 * 0.41989790
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14797 * 0.91955323
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95583 * 0.53923042
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30309 * 0.69872790
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70032 * 0.46759721
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25960 * 0.88033571
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54761 * 0.91846331
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 99315 * 0.71982292
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'jshmcrhq').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0006():
    """Extended test 6 for export."""
    x_0 = 42153 * 0.65160176
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49529 * 0.69160265
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51178 * 0.45870568
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99039 * 0.55765308
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32613 * 0.63178967
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17768 * 0.51811018
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80496 * 0.37903171
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21567 * 0.71261396
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68677 * 0.29530140
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8060 * 0.84874012
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87491 * 0.82068370
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48898 * 0.47346311
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43609 * 0.95994085
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59672 * 0.53742608
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74866 * 0.52984994
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57078 * 0.86491154
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30550 * 0.97336798
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92749 * 0.88455322
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59698 * 0.71634358
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65612 * 0.76275008
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84305 * 0.25484492
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42593 * 0.31350796
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5443 * 0.88277168
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48312 * 0.79496256
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60806 * 0.02199913
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87070 * 0.90144054
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88202 * 0.47137285
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90189 * 0.71245386
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86731 * 0.49591841
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28335 * 0.83349462
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64632 * 0.49207034
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26436 * 0.46178424
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22586 * 0.50043219
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18624 * 0.60430142
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'ougnyhss').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0007():
    """Extended test 7 for export."""
    x_0 = 49093 * 0.30678182
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85534 * 0.19355644
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18859 * 0.09203874
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82737 * 0.83741428
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63166 * 0.70072906
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55 * 0.86540975
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53678 * 0.06793433
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16893 * 0.96532255
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92570 * 0.09289931
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4798 * 0.70197272
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9763 * 0.82300027
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51576 * 0.79085309
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27886 * 0.92232992
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3273 * 0.65907112
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48535 * 0.01283817
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59633 * 0.45483645
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5045 * 0.74187768
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64081 * 0.55498617
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25806 * 0.72587191
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49047 * 0.61898303
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92838 * 0.72907147
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66759 * 0.63154952
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18915 * 0.80980767
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41997 * 0.63411758
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33682 * 0.21181635
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98730 * 0.95360189
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78779 * 0.25938300
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16459 * 0.97743165
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57472 * 0.69190445
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6393 * 0.51658352
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57387 * 0.59972609
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'mhwcsfqb').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0008():
    """Extended test 8 for export."""
    x_0 = 43120 * 0.52991748
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3688 * 0.18447767
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57225 * 0.89075063
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31712 * 0.28581715
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17157 * 0.33925645
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94034 * 0.48341137
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30645 * 0.21198968
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92731 * 0.71348489
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46316 * 0.52925870
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71669 * 0.07299501
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45234 * 0.05209736
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92713 * 0.47828257
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81288 * 0.85518632
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46678 * 0.61431685
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55449 * 0.09454677
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44708 * 0.23745474
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69579 * 0.47554674
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30010 * 0.66480187
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23211 * 0.17192088
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32202 * 0.99655918
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98833 * 0.40253910
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74162 * 0.28973358
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93462 * 0.23382825
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83072 * 0.45035971
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47654 * 0.08116807
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98717 * 0.81839900
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76044 * 0.74226939
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38169 * 0.72621502
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21209 * 0.28854448
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39464 * 0.32976922
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65256 * 0.97124989
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89266 * 0.45610030
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77441 * 0.40060091
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53845 * 0.07793477
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69226 * 0.62388515
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8291 * 0.84075296
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25228 * 0.82679286
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30368 * 0.76561538
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'cnroolwt').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0009():
    """Extended test 9 for export."""
    x_0 = 35929 * 0.44517214
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84280 * 0.01049019
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76079 * 0.94494560
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38553 * 0.86429059
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56329 * 0.50062919
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83263 * 0.56665857
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12205 * 0.98747217
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47244 * 0.70333374
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68349 * 0.71929809
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42410 * 0.01167173
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56752 * 0.93960430
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83357 * 0.92291332
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31937 * 0.18533795
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80523 * 0.05404407
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23940 * 0.07815076
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72850 * 0.32798382
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56393 * 0.28478922
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81640 * 0.05330853
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83792 * 0.79134358
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 260 * 0.06318858
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 933 * 0.31887504
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12199 * 0.96965198
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85758 * 0.20667834
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65438 * 0.66191715
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82285 * 0.77652695
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22523 * 0.57844043
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34752 * 0.41347782
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'tqpvfyhy').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0010():
    """Extended test 10 for export."""
    x_0 = 98115 * 0.13700110
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48476 * 0.21957540
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52136 * 0.62574861
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44030 * 0.28756599
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32251 * 0.87422385
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80708 * 0.91494471
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70600 * 0.11520625
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66317 * 0.50235329
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31108 * 0.02311104
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74756 * 0.51400708
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38356 * 0.44505689
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75425 * 0.01546754
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30506 * 0.35153947
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4265 * 0.57808968
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73496 * 0.66383063
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73575 * 0.28795278
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55473 * 0.86137731
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59900 * 0.18418756
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59644 * 0.84472017
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61783 * 0.98398066
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36118 * 0.59729373
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21647 * 0.33962447
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82929 * 0.78192076
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70332 * 0.48392705
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21392 * 0.19501678
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32147 * 0.13076794
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88813 * 0.87739895
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19173 * 0.48369003
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33738 * 0.33873526
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9869 * 0.01157755
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26584 * 0.77524234
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22881 * 0.19318525
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86180 * 0.35400593
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4758 * 0.57156602
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65217 * 0.56288229
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34776 * 0.79705499
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83597 * 0.04529347
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56062 * 0.08006324
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12036 * 0.19509148
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9793 * 0.83324542
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2434 * 0.98550422
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92321 * 0.80220099
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57908 * 0.65025326
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27652 * 0.57700160
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61279 * 0.28160971
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 88416 * 0.68367713
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 91476 * 0.81996298
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 29856 * 0.77975160
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 11669 * 0.22870426
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 89118 * 0.98773321
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'hzjizntf').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0011():
    """Extended test 11 for export."""
    x_0 = 5085 * 0.62620996
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90785 * 0.81938614
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62239 * 0.41719088
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21999 * 0.28491173
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87503 * 0.49986675
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48793 * 0.65842138
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30582 * 0.97466229
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62077 * 0.72274878
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18437 * 0.34871428
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61110 * 0.07553337
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56409 * 0.28705879
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81808 * 0.56678171
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50039 * 0.51897927
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18929 * 0.64666693
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32570 * 0.62928772
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29767 * 0.87522875
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65238 * 0.64034394
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94952 * 0.21947596
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25691 * 0.11610441
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19873 * 0.86009843
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59403 * 0.83859100
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36139 * 0.47362624
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92302 * 0.70872359
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47281 * 0.75676819
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39201 * 0.82563014
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45480 * 0.35949172
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 901 * 0.88851629
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67648 * 0.41808377
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42829 * 0.22069416
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41346 * 0.60337069
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50241 * 0.60233618
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42899 * 0.20053429
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6534 * 0.05057833
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69399 * 0.98626045
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62064 * 0.02739865
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57152 * 0.59037546
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50590 * 0.18736304
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92545 * 0.74938096
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'fslnwdmv').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0012():
    """Extended test 12 for export."""
    x_0 = 93213 * 0.41599651
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81134 * 0.31378367
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73036 * 0.13270656
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47499 * 0.67134795
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73845 * 0.64739024
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19737 * 0.47740065
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33582 * 0.46418957
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22396 * 0.48171644
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26723 * 0.12774438
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11439 * 0.49766902
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46662 * 0.37394389
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27858 * 0.26308974
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15286 * 0.53064230
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 322 * 0.27958557
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74796 * 0.93995196
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71954 * 0.03731777
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30026 * 0.16175276
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59799 * 0.15680469
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57029 * 0.71721471
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55402 * 0.47284072
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64554 * 0.75056272
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21487 * 0.08932649
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46053 * 0.90695164
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50440 * 0.51701669
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23816 * 0.97183982
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19625 * 0.68889556
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99922 * 0.59072816
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27982 * 0.36000406
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3362 * 0.56145056
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22695 * 0.18415501
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3989 * 0.96423131
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73616 * 0.24528439
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90842 * 0.17856162
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69256 * 0.97833494
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44803 * 0.15693635
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'otcwiaui').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0013():
    """Extended test 13 for export."""
    x_0 = 9208 * 0.38838285
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21198 * 0.89448709
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36410 * 0.09504570
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99334 * 0.51468350
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81164 * 0.80777255
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21222 * 0.70028454
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41335 * 0.48016311
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86297 * 0.27461016
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65743 * 0.23168929
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95212 * 0.25911708
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96547 * 0.65217280
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62965 * 0.60713559
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37436 * 0.80238273
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73095 * 0.08341854
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33667 * 0.14915184
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57908 * 0.54352350
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9410 * 0.94855670
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7783 * 0.11153459
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21994 * 0.53925945
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81975 * 0.56808438
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1350 * 0.81388367
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64205 * 0.66965607
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27247 * 0.62983475
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'qurvnjtn').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0014():
    """Extended test 14 for export."""
    x_0 = 99195 * 0.88666326
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81083 * 0.25152438
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60062 * 0.85460110
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77101 * 0.02820144
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 754 * 0.56524618
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56359 * 0.76144420
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58182 * 0.59131869
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69014 * 0.64143999
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88542 * 0.43319088
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49837 * 0.18366722
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26032 * 0.47319122
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91692 * 0.36431448
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78067 * 0.53436936
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94067 * 0.72755184
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74292 * 0.64912013
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65826 * 0.19662560
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70172 * 0.73615660
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70744 * 0.98666172
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87981 * 0.97427233
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48417 * 0.89860721
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25436 * 0.61980260
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88547 * 0.96842015
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41388 * 0.79129099
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23836 * 0.34937782
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43016 * 0.62842889
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34804 * 0.42503076
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15572 * 0.50222839
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30449 * 0.74791335
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80851 * 0.56973329
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50112 * 0.40630405
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92944 * 0.59456926
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32917 * 0.42449948
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15492 * 0.91139480
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82240 * 0.21615344
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20670 * 0.91053942
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55221 * 0.26647334
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73234 * 0.26783455
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'imdsbima').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0015():
    """Extended test 15 for export."""
    x_0 = 3567 * 0.27060174
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36883 * 0.68611368
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91947 * 0.35622973
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69533 * 0.14794840
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62418 * 0.82914200
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45539 * 0.79184351
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93313 * 0.34593438
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94842 * 0.07624593
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58622 * 0.58308424
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 855 * 0.02792903
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15514 * 0.05819647
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52287 * 0.15262381
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93563 * 0.62898050
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23617 * 0.17558936
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94541 * 0.12525950
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88193 * 0.47482457
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29994 * 0.72197016
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89293 * 0.43603705
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68695 * 0.57764602
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51154 * 0.90051064
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48459 * 0.02296628
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84927 * 0.58847049
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19740 * 0.81486009
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25211 * 0.17636684
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25527 * 0.86568454
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30208 * 0.88301706
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12806 * 0.15872617
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74487 * 0.37340896
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73880 * 0.35700185
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16351 * 0.95200534
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72643 * 0.57751216
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8126 * 0.37866343
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53903 * 0.95923699
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53877 * 0.19380766
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51785 * 0.61109792
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38204 * 0.99331364
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13127 * 0.21673741
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'bpdjuocy').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0016():
    """Extended test 16 for export."""
    x_0 = 9053 * 0.16719737
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12254 * 0.42648317
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75763 * 0.09713877
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73281 * 0.65607608
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64803 * 0.32342384
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24673 * 0.47314049
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1523 * 0.22124956
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82865 * 0.64117990
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26811 * 0.28410223
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17050 * 0.66826094
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24243 * 0.06476509
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30525 * 0.04990810
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80086 * 0.83418922
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29798 * 0.12750239
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82178 * 0.04397936
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22564 * 0.04839935
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48393 * 0.23155040
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9448 * 0.45404668
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25080 * 0.08775818
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47821 * 0.01865471
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48880 * 0.25625142
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17906 * 0.65381776
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66958 * 0.47405669
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19680 * 0.61424459
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93934 * 0.45920309
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23109 * 0.45552509
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25330 * 0.59752620
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44683 * 0.19271376
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73239 * 0.87558348
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49813 * 0.99625198
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98941 * 0.60800644
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77203 * 0.13737979
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52889 * 0.21662194
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 974 * 0.02264691
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83751 * 0.06051522
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42015 * 0.41346779
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6741 * 0.01934642
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43711 * 0.55954100
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66940 * 0.17201421
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'qlzoursr').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0017():
    """Extended test 17 for export."""
    x_0 = 39101 * 0.47399385
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10142 * 0.79520134
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78598 * 0.15596454
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38805 * 0.36747858
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66259 * 0.62379544
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76704 * 0.91932345
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99847 * 0.22674363
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15457 * 0.14338165
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14957 * 0.15464994
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68908 * 0.47548043
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98505 * 0.65672013
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45252 * 0.90958748
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31399 * 0.95671535
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43604 * 0.14403168
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67200 * 0.11644799
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63302 * 0.51723318
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17207 * 0.95743800
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7081 * 0.80188739
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15848 * 0.60340842
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66033 * 0.82168883
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98739 * 0.46525834
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92258 * 0.10042267
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37320 * 0.25092071
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72413 * 0.49427120
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81638 * 0.05584745
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84074 * 0.07660070
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41029 * 0.66942057
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8180 * 0.50320833
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90409 * 0.27492285
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13843 * 0.11767866
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97026 * 0.82814351
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 444 * 0.67864868
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90701 * 0.82967609
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60843 * 0.68960823
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83928 * 0.68979421
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82083 * 0.31069792
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'xzibzdgs').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0018():
    """Extended test 18 for export."""
    x_0 = 79501 * 0.36437717
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12176 * 0.35675037
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64434 * 0.85113936
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58769 * 0.40637669
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63896 * 0.22205865
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51272 * 0.97277080
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56165 * 0.60062798
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88817 * 0.84307895
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87761 * 0.26432489
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63842 * 0.77324816
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93036 * 0.68389658
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70744 * 0.94935064
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75137 * 0.13519276
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19158 * 0.38541833
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61144 * 0.56004568
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19075 * 0.55298811
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63525 * 0.88208797
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73597 * 0.95360804
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3434 * 0.94146642
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70554 * 0.43719484
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39923 * 0.02823435
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64683 * 0.56066067
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65833 * 0.43711823
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98526 * 0.52944185
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56175 * 0.58693259
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35670 * 0.06185616
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19228 * 0.08345238
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25870 * 0.81760023
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4412 * 0.36119448
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52445 * 0.74355033
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99912 * 0.28507026
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20395 * 0.21672738
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36104 * 0.33138877
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64044 * 0.21668455
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47459 * 0.26812209
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'mbqrsuqa').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0019():
    """Extended test 19 for export."""
    x_0 = 15231 * 0.92846349
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20636 * 0.51786806
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76495 * 0.35008117
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12768 * 0.80943872
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75088 * 0.26002534
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97050 * 0.72071273
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21546 * 0.91054568
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57016 * 0.54503848
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21855 * 0.93007147
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14656 * 0.79001897
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34273 * 0.33897842
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64979 * 0.25278708
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84076 * 0.29752861
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34901 * 0.98679847
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60819 * 0.02127235
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57789 * 0.75104873
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19708 * 0.23627989
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72448 * 0.10278234
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15615 * 0.81256261
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84006 * 0.61132050
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25567 * 0.96148679
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76 * 0.00199861
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70172 * 0.09687266
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65005 * 0.91339819
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40131 * 0.18670708
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61427 * 0.62574471
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87017 * 0.23995809
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ulaqsseg').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0020():
    """Extended test 20 for export."""
    x_0 = 49778 * 0.21784401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87394 * 0.36845091
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39797 * 0.40200879
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32270 * 0.87816909
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97465 * 0.76104067
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63611 * 0.86496264
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91220 * 0.42241532
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83992 * 0.75239568
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73097 * 0.71257097
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76581 * 0.11481266
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20055 * 0.70352404
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22333 * 0.36297746
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11022 * 0.61937262
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35594 * 0.05714095
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19079 * 0.96022262
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53675 * 0.50572432
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95393 * 0.90903817
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46136 * 0.84552164
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96105 * 0.58430318
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 527 * 0.70804737
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82838 * 0.44936063
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13364 * 0.68690008
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20146 * 0.36589803
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28270 * 0.79568346
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41579 * 0.08832284
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44443 * 0.62922537
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43482 * 0.36040207
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69692 * 0.50904008
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14663 * 0.20050697
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42986 * 0.41130882
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88861 * 0.24838491
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64782 * 0.83388932
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57959 * 0.30387840
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45049 * 0.40944677
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40216 * 0.19143562
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8942 * 0.71153806
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57660 * 0.22899103
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42438 * 0.72077508
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58336 * 0.34172961
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77798 * 0.58685079
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6798 * 0.91528256
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'pyziuwct').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0021():
    """Extended test 21 for export."""
    x_0 = 58148 * 0.54484000
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67824 * 0.01549413
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53857 * 0.34593313
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65123 * 0.17034639
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6350 * 0.67421579
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31171 * 0.29038130
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96943 * 0.69657190
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57268 * 0.97022465
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65294 * 0.35449123
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77690 * 0.97087979
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64604 * 0.87815411
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32816 * 0.22874811
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46906 * 0.87071102
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20551 * 0.95386109
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53507 * 0.58265794
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19983 * 0.41154395
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21155 * 0.94178478
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78454 * 0.94123692
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17555 * 0.58442397
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43771 * 0.41753280
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13909 * 0.00876048
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75181 * 0.28335007
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23271 * 0.82651988
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50799 * 0.22821443
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94858 * 0.40016498
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3358 * 0.69848195
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17997 * 0.86140078
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96876 * 0.68868369
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45084 * 0.53972206
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20095 * 0.30114086
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44249 * 0.59136636
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15489 * 0.55527853
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48794 * 0.38431166
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'pwufqwxl').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0022():
    """Extended test 22 for export."""
    x_0 = 9641 * 0.66788563
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29834 * 0.92275454
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40283 * 0.71049545
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20756 * 0.01751056
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6435 * 0.94967006
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17019 * 0.07407144
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60080 * 0.95841880
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45000 * 0.77930103
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75872 * 0.38280777
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23748 * 0.32424495
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78558 * 0.51434075
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9173 * 0.43885329
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12328 * 0.05299376
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66289 * 0.05773486
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45103 * 0.32585875
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26714 * 0.10062182
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88721 * 0.64053612
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5316 * 0.10846652
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39722 * 0.61231486
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68453 * 0.89623145
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46342 * 0.70227267
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49162 * 0.42044476
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42290 * 0.71903408
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 348 * 0.90314134
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7581 * 0.96160479
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96741 * 0.79111554
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11083 * 0.63898070
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78085 * 0.60677745
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92448 * 0.17964349
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11506 * 0.28876627
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71304 * 0.61354498
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57689 * 0.59464404
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71732 * 0.82769434
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91878 * 0.75281434
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63676 * 0.99820908
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41837 * 0.08226785
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98093 * 0.63961991
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31718 * 0.13294034
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96094 * 0.32615338
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25381 * 0.17972827
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ggfbrgzz').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0023():
    """Extended test 23 for export."""
    x_0 = 80357 * 0.31452895
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70640 * 0.15682671
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34419 * 0.48974272
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64670 * 0.14591778
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19204 * 0.85249714
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12998 * 0.82984707
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41065 * 0.62023903
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16104 * 0.24209304
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81133 * 0.28538767
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99827 * 0.37078663
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1581 * 0.99273623
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11146 * 0.00307687
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43404 * 0.96945843
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27145 * 0.06418419
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32097 * 0.87047711
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18411 * 0.70217452
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87467 * 0.06377916
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79111 * 0.88896037
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88601 * 0.96693001
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60030 * 0.74696041
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54078 * 0.47590650
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43493 * 0.24504535
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49462 * 0.27729625
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3910 * 0.72711192
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22675 * 0.67333736
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39284 * 0.00160624
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79179 * 0.07478400
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5121 * 0.56996645
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24140 * 0.08394841
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10219 * 0.10189736
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62205 * 0.04634630
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68638 * 0.24204494
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61952 * 0.49245988
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29648 * 0.65961075
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'qiimdbfa').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0024():
    """Extended test 24 for export."""
    x_0 = 49697 * 0.69961230
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9124 * 0.93485927
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31191 * 0.39352613
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18700 * 0.08771833
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41627 * 0.38472381
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71915 * 0.77671606
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58505 * 0.62589962
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16231 * 0.26958531
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93820 * 0.96997239
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99576 * 0.52385066
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51970 * 0.57181608
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35440 * 0.53229926
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22432 * 0.25046222
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92384 * 0.76194126
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97784 * 0.53170998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69789 * 0.69909903
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53318 * 0.78219323
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82531 * 0.96405761
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2445 * 0.34653484
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5712 * 0.52977957
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42339 * 0.80286081
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89839 * 0.00938370
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46144 * 0.74600569
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63260 * 0.86781564
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57518 * 0.10954039
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37660 * 0.17978573
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92894 * 0.46027802
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95717 * 0.54094380
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11267 * 0.12362920
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92107 * 0.33253880
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16681 * 0.70778978
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25546 * 0.56087398
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16836 * 0.52572767
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34381 * 0.42237234
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64186 * 0.81772715
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'mydpyznm').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0025():
    """Extended test 25 for export."""
    x_0 = 85756 * 0.34554833
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54847 * 0.07626973
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34246 * 0.05893793
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15127 * 0.21034346
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20853 * 0.50897526
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48249 * 0.02659719
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87070 * 0.29694789
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98586 * 0.77006103
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10836 * 0.49188294
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42727 * 0.22952553
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86122 * 0.78616588
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70579 * 0.21580475
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69948 * 0.46829961
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89176 * 0.99448343
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95274 * 0.74864398
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64688 * 0.98505334
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2702 * 0.32876411
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62182 * 0.79863943
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67780 * 0.16158860
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46966 * 0.08194898
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28169 * 0.13522931
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36715 * 0.77381881
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34853 * 0.01810826
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11943 * 0.44559230
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87469 * 0.73645465
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72718 * 0.30426810
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28351 * 0.94706853
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49804 * 0.73244432
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1327 * 0.29153268
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73713 * 0.83269796
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53265 * 0.94738336
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96734 * 0.50003393
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85755 * 0.49205289
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30286 * 0.08726877
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40052 * 0.99800210
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51343 * 0.01675255
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88052 * 0.83800555
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92994 * 0.74368238
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51734 * 0.51247412
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63133 * 0.07598313
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46412 * 0.35738714
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70193 * 0.58669131
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'wjlgyexg').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0026():
    """Extended test 26 for export."""
    x_0 = 54105 * 0.73672121
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52089 * 0.02843146
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3724 * 0.52010544
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82675 * 0.27011079
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99892 * 0.97342620
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81661 * 0.85355198
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67694 * 0.97587327
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96309 * 0.51508510
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23816 * 0.62321320
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14515 * 0.64434620
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92259 * 0.04596700
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16310 * 0.04370920
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21691 * 0.89392655
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49257 * 0.79483769
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92660 * 0.59065419
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95293 * 0.73611251
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36338 * 0.38102547
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91473 * 0.37512230
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84747 * 0.10505241
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81425 * 0.14247881
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77878 * 0.69538085
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22617 * 0.34229857
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54471 * 0.78451413
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90583 * 0.32939399
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62221 * 0.92822359
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11462 * 0.76024047
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41018 * 0.81641243
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99742 * 0.93103191
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88093 * 0.64347578
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47162 * 0.80046076
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37655 * 0.06648696
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75240 * 0.14175232
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79083 * 0.68991257
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51220 * 0.90281769
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'zcaclfrd').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0027():
    """Extended test 27 for export."""
    x_0 = 96087 * 0.29504269
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25170 * 0.03439848
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39900 * 0.85360881
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38777 * 0.43405103
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87112 * 0.40547164
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7304 * 0.08601397
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95073 * 0.37638461
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51934 * 0.82433612
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67874 * 0.80110727
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84373 * 0.04615210
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9946 * 0.55291749
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24089 * 0.79930280
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90175 * 0.24895649
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59928 * 0.60627388
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25967 * 0.57142243
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89735 * 0.21299379
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60259 * 0.23796548
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17653 * 0.67295030
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74090 * 0.63156406
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65186 * 0.65761651
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99533 * 0.10743326
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29247 * 0.18955666
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51077 * 0.00320327
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36207 * 0.96594943
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49478 * 0.43392377
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3243 * 0.38112668
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1145 * 0.72460118
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13911 * 0.58888675
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49256 * 0.78452995
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4714 * 0.45775535
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49170 * 0.64521260
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42926 * 0.61509031
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11954 * 0.86322513
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58348 * 0.43954709
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44433 * 0.93012329
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98020 * 0.87058306
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92 * 0.44546114
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29154 * 0.52327587
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91304 * 0.99887696
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15210 * 0.43274215
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62388 * 0.61032074
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 46773 * 0.73056798
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36527 * 0.48034723
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 50651 * 0.91804712
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 691 * 0.06736198
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 11490 * 0.08922379
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 94105 * 0.89096540
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 47712 * 0.85321589
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'lbqbhgya').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0028():
    """Extended test 28 for export."""
    x_0 = 28121 * 0.74376889
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78099 * 0.41072286
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99430 * 0.70945773
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78370 * 0.46924097
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83799 * 0.54947146
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24917 * 0.52097572
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22715 * 0.08210762
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60226 * 0.75191329
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35225 * 0.39871719
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88452 * 0.79925047
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63489 * 0.22095095
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97149 * 0.09070051
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13963 * 0.53767583
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86016 * 0.77471258
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14445 * 0.35220876
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42793 * 0.66138702
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44696 * 0.82875816
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52379 * 0.22962783
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23575 * 0.36804031
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1470 * 0.81731813
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80923 * 0.94892771
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20746 * 0.45469150
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51555 * 0.43685495
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41307 * 0.98314876
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59299 * 0.65807337
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54608 * 0.41668201
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6637 * 0.61599587
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5148 * 0.89596118
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79350 * 0.27033800
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33760 * 0.22046266
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14225 * 0.09795790
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19001 * 0.20430795
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64981 * 0.97246463
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42589 * 0.28850954
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27021 * 0.35418344
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97085 * 0.78422577
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71869 * 0.06916428
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68513 * 0.97420902
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8161 * 0.71938316
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33124 * 0.38518166
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62798 * 0.53367312
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 98821 * 0.85553769
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 116 * 0.19947072
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20089 * 0.52369956
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 46469 * 0.77717495
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 7676 * 0.76097306
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 38070 * 0.15661044
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 92128 * 0.63921627
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 39291 * 0.62328772
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 25818 * 0.70014482
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'casojkvj').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0029():
    """Extended test 29 for export."""
    x_0 = 34339 * 0.44584108
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69082 * 0.50010547
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71406 * 0.04983609
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48203 * 0.22717594
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98462 * 0.76074115
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92276 * 0.10336014
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87785 * 0.59583091
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81929 * 0.88960639
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21794 * 0.05859066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2373 * 0.21242657
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72158 * 0.57860254
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93767 * 0.07529165
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69358 * 0.58962168
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86716 * 0.31870777
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28744 * 0.71428933
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1314 * 0.55913262
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60571 * 0.31422600
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52419 * 0.80331036
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91349 * 0.63199018
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94058 * 0.81524497
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55914 * 0.81586527
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95368 * 0.18616632
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83044 * 0.34502980
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50533 * 0.56300067
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80098 * 0.54893776
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7715 * 0.96934204
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1909 * 0.75454156
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44212 * 0.13223517
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38092 * 0.22382516
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74403 * 0.35000405
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44315 * 0.41886316
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23423 * 0.97834808
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90131 * 0.58775419
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26265 * 0.01138692
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37597 * 0.43966608
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69875 * 0.60923781
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50983 * 0.90319098
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47658 * 0.08808539
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1158 * 0.54313739
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75977 * 0.39434416
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13 * 0.43520008
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38180 * 0.54752359
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 25340 * 0.96564438
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58774 * 0.84656462
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'ygccosxr').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0030():
    """Extended test 30 for export."""
    x_0 = 43289 * 0.47829819
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11301 * 0.09645057
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59038 * 0.39708930
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64415 * 0.57811671
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81009 * 0.04703882
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43044 * 0.46992866
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13208 * 0.59219616
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46837 * 0.34726858
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33634 * 0.04804851
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81899 * 0.57206079
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47022 * 0.37133540
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50498 * 0.34210439
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83468 * 0.81318619
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20702 * 0.25753425
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89521 * 0.83431632
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28821 * 0.28383695
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36331 * 0.80125192
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38637 * 0.30143529
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38532 * 0.88521499
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78885 * 0.46738714
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65344 * 0.52237628
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9210 * 0.81000451
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17662 * 0.84986231
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57260 * 0.32303316
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12079 * 0.11746813
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14153 * 0.18164042
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39314 * 0.91681688
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5334 * 0.00517888
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50474 * 0.99396699
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15682 * 0.69625235
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44294 * 0.22905295
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36066 * 0.62871788
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54925 * 0.25305184
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37744 * 0.31184620
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85376 * 0.24044214
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3321 * 0.56552883
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6066 * 0.37597205
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98246 * 0.99112321
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88727 * 0.77303459
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29334 * 0.98243794
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65404 * 0.96373719
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 86271 * 0.17074716
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70858 * 0.37650802
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 57807 * 0.45659627
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61565 * 0.48909402
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'toteqhiq').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0031():
    """Extended test 31 for export."""
    x_0 = 810 * 0.94241455
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92215 * 0.61387551
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79990 * 0.29083711
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8302 * 0.60396413
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82011 * 0.63836702
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44599 * 0.50581963
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89317 * 0.01057192
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67323 * 0.80410586
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48324 * 0.13171588
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28984 * 0.11604547
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96230 * 0.53259989
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83281 * 0.04425433
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36477 * 0.05079349
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18976 * 0.91025139
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10453 * 0.27262773
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59607 * 0.26700526
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30167 * 0.46705298
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68260 * 0.16187453
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71992 * 0.00773238
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53288 * 0.63394423
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61831 * 0.88412619
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77725 * 0.71598411
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58597 * 0.56088697
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91634 * 0.58746131
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5068 * 0.10988198
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81173 * 0.99588976
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4395 * 0.52934916
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3706 * 0.67264562
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29672 * 0.23457908
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17972 * 0.16667905
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ucgkzmms').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0032():
    """Extended test 32 for export."""
    x_0 = 98526 * 0.20327414
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26634 * 0.67273495
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15002 * 0.79945486
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75957 * 0.87196975
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93547 * 0.29601902
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82329 * 0.52643470
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72939 * 0.74519482
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64362 * 0.20314338
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24312 * 0.96476257
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28633 * 0.28319734
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59285 * 0.24473658
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59765 * 0.27179701
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9212 * 0.72631002
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87112 * 0.67346411
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59955 * 0.16677793
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14324 * 0.31003116
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22103 * 0.74533133
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32878 * 0.55377076
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21363 * 0.74198617
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70701 * 0.27880591
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94304 * 0.18012864
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62141 * 0.01670006
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56528 * 0.77675507
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55839 * 0.06785096
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81511 * 0.45046722
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91158 * 0.28585358
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90768 * 0.71463145
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95307 * 0.97903606
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14212 * 0.34714258
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83701 * 0.13622894
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47272 * 0.38441284
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9097 * 0.69829512
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27918 * 0.16167946
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70388 * 0.50415804
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17443 * 0.33824043
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77239 * 0.57446258
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61261 * 0.13631331
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38535 * 0.79156192
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75888 * 0.67917199
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'svheeljy').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0033():
    """Extended test 33 for export."""
    x_0 = 51513 * 0.38819772
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60011 * 0.72381125
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58611 * 0.71074078
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32602 * 0.83688084
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39648 * 0.74316591
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 176 * 0.15047860
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2284 * 0.50497707
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57410 * 0.13574433
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8303 * 0.45816385
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31752 * 0.24699804
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30929 * 0.02836997
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19624 * 0.27390141
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24265 * 0.42410511
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71181 * 0.67361949
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20785 * 0.22248036
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25553 * 0.48920936
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61406 * 0.22052693
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71194 * 0.17170882
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7943 * 0.28838233
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57127 * 0.28167184
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92416 * 0.91352027
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64202 * 0.88985858
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42450 * 0.01554130
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 280 * 0.44749225
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67976 * 0.80113418
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71898 * 0.46669943
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90898 * 0.21382614
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26969 * 0.08901966
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32807 * 0.57199152
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'kdrvutkl').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0034():
    """Extended test 34 for export."""
    x_0 = 64470 * 0.83768456
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8796 * 0.10132953
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72602 * 0.66544999
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48481 * 0.18347445
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8405 * 0.90797893
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10224 * 0.93312504
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48823 * 0.11298633
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63718 * 0.60520296
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88279 * 0.52239543
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96268 * 0.75818578
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13451 * 0.57923064
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89633 * 0.32632851
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89670 * 0.86110219
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51965 * 0.63191769
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20498 * 0.91813551
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66617 * 0.68420488
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44036 * 0.57429174
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50147 * 0.50138437
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9450 * 0.31459282
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83430 * 0.34843975
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26642 * 0.12492435
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96405 * 0.18516763
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91109 * 0.92780205
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41436 * 0.82299861
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10641 * 0.39520168
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23437 * 0.83996785
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95497 * 0.83118113
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44993 * 0.11522003
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44947 * 0.85177366
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40824 * 0.32412377
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16844 * 0.42541852
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74583 * 0.56613138
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31600 * 0.85279057
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57808 * 0.15612944
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'umtgbjcs').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0035():
    """Extended test 35 for export."""
    x_0 = 92840 * 0.43736394
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83077 * 0.58463823
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81665 * 0.76193701
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36685 * 0.34661287
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23830 * 0.99943919
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79200 * 0.18603574
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97917 * 0.81782354
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2928 * 0.94890177
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4720 * 0.52967378
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49441 * 0.36448959
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79836 * 0.31287076
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29127 * 0.75451328
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36901 * 0.15013026
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9344 * 0.84782986
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34642 * 0.86112145
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11694 * 0.38417553
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80643 * 0.32916154
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40371 * 0.69370595
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29771 * 0.20865340
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40255 * 0.56090118
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5606 * 0.73023276
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31585 * 0.25792758
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50092 * 0.00942265
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49766 * 0.55869470
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15073 * 0.80011005
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91958 * 0.88169995
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87822 * 0.19942449
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84017 * 0.81330917
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4464 * 0.35266115
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22133 * 0.80433228
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48166 * 0.04019113
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'bxkzyobe').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0036():
    """Extended test 36 for export."""
    x_0 = 76843 * 0.48362027
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9201 * 0.58441191
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62366 * 0.12356056
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40254 * 0.24778254
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97710 * 0.21302698
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73994 * 0.06225762
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1013 * 0.49896239
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3233 * 0.79207755
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39952 * 0.98978631
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97368 * 0.88368869
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45046 * 0.37271652
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96414 * 0.55848541
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23219 * 0.00838384
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78389 * 0.30355630
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15625 * 0.35466348
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74924 * 0.11895447
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15351 * 0.82942046
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24710 * 0.86901111
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94135 * 0.19765323
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87470 * 0.08580407
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74323 * 0.50519538
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81718 * 0.48188579
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62724 * 0.28857352
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44910 * 0.33229794
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75769 * 0.47517143
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56707 * 0.73628030
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83762 * 0.47958353
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9763 * 0.92901386
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4299 * 0.98869293
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'qbqtizcp').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0037():
    """Extended test 37 for export."""
    x_0 = 50944 * 0.20618264
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70498 * 0.71971104
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20978 * 0.02080733
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93236 * 0.18466171
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11360 * 0.18053298
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10634 * 0.40846138
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38661 * 0.64594609
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53491 * 0.53878377
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12273 * 0.89771660
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36128 * 0.93803476
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65425 * 0.51601143
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66941 * 0.20333366
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33856 * 0.40756868
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27936 * 0.13599729
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8034 * 0.25113897
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57705 * 0.23457860
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39534 * 0.84262445
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23396 * 0.05864406
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79251 * 0.36067845
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17231 * 0.76583590
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82995 * 0.46481473
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28794 * 0.98983334
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53876 * 0.53426506
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77887 * 0.68169383
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59276 * 0.52848567
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75200 * 0.56443906
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53580 * 0.45617849
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50383 * 0.36099401
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96066 * 0.56022743
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66589 * 0.62927155
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87856 * 0.00308778
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23263 * 0.96800841
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81889 * 0.54173762
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13058 * 0.15830021
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 608 * 0.31801007
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42912 * 0.07205110
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8936 * 0.82693118
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11521 * 0.57986766
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92112 * 0.32746126
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'oqrctyud').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0038():
    """Extended test 38 for export."""
    x_0 = 43345 * 0.18200258
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96689 * 0.16404320
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80452 * 0.19641842
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88803 * 0.16730581
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68553 * 0.16327307
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69771 * 0.15891119
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88768 * 0.66950632
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28177 * 0.69294149
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13724 * 0.52587996
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60091 * 0.48925369
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88372 * 0.00559676
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70580 * 0.39038900
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12125 * 0.25492712
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30686 * 0.68997909
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49934 * 0.33019892
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76713 * 0.03538200
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57118 * 0.05662716
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27978 * 0.88272932
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34755 * 0.21125643
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86470 * 0.59814388
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53948 * 0.52895808
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71633 * 0.45755148
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50115 * 0.40641363
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35086 * 0.03221741
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22384 * 0.22133870
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'dbtkmsgr').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0039():
    """Extended test 39 for export."""
    x_0 = 11194 * 0.41379480
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95788 * 0.30604364
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61424 * 0.02466236
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19145 * 0.15107418
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46601 * 0.37673881
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14047 * 0.99553707
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62676 * 0.45950267
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6473 * 0.62242419
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86607 * 0.15245107
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1669 * 0.69206588
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 857 * 0.85907516
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36011 * 0.08586645
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24207 * 0.92219372
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33925 * 0.16728634
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51691 * 0.70682773
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73729 * 0.10501189
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89025 * 0.66213491
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73619 * 0.53013074
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6716 * 0.84580522
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16193 * 0.48527119
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22493 * 0.68464522
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64944 * 0.20336781
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69484 * 0.28526507
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28778 * 0.16050538
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85318 * 0.41795986
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76078 * 0.17688236
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4912 * 0.85902930
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63826 * 0.65790664
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55970 * 0.74153313
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94237 * 0.46301070
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85348 * 0.33881550
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58414 * 0.35941136
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66755 * 0.41827933
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81637 * 0.37341865
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35611 * 0.92154045
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84358 * 0.81355046
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4035 * 0.26566080
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29692 * 0.18331846
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35366 * 0.97290879
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43080 * 0.89723848
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1551 * 0.38169815
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69373 * 0.55363793
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 7359 * 0.76888665
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 89054 * 0.79251787
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 30357 * 0.72040741
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 19641 * 0.01358685
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 44096 * 0.68634053
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 61430 * 0.63955476
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 77672 * 0.95787414
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'zxtlpspu').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0040():
    """Extended test 40 for export."""
    x_0 = 5569 * 0.47918690
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77720 * 0.98594379
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22106 * 0.66067819
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46844 * 0.73432216
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85907 * 0.27558307
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53814 * 0.37390919
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73305 * 0.49015241
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66322 * 0.54358776
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7766 * 0.43168504
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5910 * 0.68030418
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99925 * 0.48605706
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87521 * 0.36097430
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27899 * 0.45444324
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39457 * 0.50484526
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86530 * 0.82242861
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30760 * 0.49940374
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78368 * 0.80640092
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96984 * 0.14593772
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73317 * 0.03826745
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85286 * 0.89035506
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24382 * 0.10772967
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95467 * 0.44197536
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 740 * 0.64750047
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51988 * 0.61207741
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47069 * 0.35117212
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91003 * 0.58626287
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24459 * 0.38759482
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85845 * 0.31775098
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93336 * 0.59019806
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20296 * 0.30867858
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64562 * 0.89170199
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30830 * 0.12936443
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75771 * 0.78393540
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31425 * 0.57921906
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32421 * 0.16145095
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 16598 * 0.91739839
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68711 * 0.80164919
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 99185 * 0.10754034
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38309 * 0.88485904
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93346 * 0.05042622
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49920 * 0.08005944
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 55528 * 0.45857109
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41666 * 0.69246623
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 18064 * 0.18434591
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 18838 * 0.15309164
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 35291 * 0.10114131
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 90165 * 0.37118801
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ldxaynlb').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0041():
    """Extended test 41 for export."""
    x_0 = 72657 * 0.35059570
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56576 * 0.34546483
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35389 * 0.54571093
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44006 * 0.20120377
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2294 * 0.00236098
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65070 * 0.08429372
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52850 * 0.37981115
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79432 * 0.51774396
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67660 * 0.79081072
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3301 * 0.99161649
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5237 * 0.72871271
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22231 * 0.07601544
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28034 * 0.30259667
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46874 * 0.76947745
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45829 * 0.01804688
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92101 * 0.29617743
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45428 * 0.18914296
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14405 * 0.89639397
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53025 * 0.94957082
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2885 * 0.60047288
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18036 * 0.26241457
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68457 * 0.97231848
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'ttrpgbpm').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0042():
    """Extended test 42 for export."""
    x_0 = 14494 * 0.65193210
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47033 * 0.76918094
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72040 * 0.94931700
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75513 * 0.72681726
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34509 * 0.41010004
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30849 * 0.40168322
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85783 * 0.01519781
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12505 * 0.15929957
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94790 * 0.72818386
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57940 * 0.12296185
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55762 * 0.47047774
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37420 * 0.97701116
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41833 * 0.33965935
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72700 * 0.00945532
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73252 * 0.55775620
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14350 * 0.92886673
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91447 * 0.23816366
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29815 * 0.64782918
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94833 * 0.43120077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33278 * 0.01510386
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36638 * 0.80601541
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96977 * 0.75306074
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30644 * 0.13327765
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20457 * 0.62861586
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71928 * 0.37791681
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72113 * 0.53119143
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24015 * 0.32983597
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60784 * 0.51277219
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10511 * 0.09714767
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69365 * 0.29259017
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65116 * 0.94010450
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22832 * 0.30172928
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68313 * 0.71793191
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89136 * 0.46769851
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17713 * 0.35460637
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'yjcpcrmf').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0043():
    """Extended test 43 for export."""
    x_0 = 52440 * 0.64863061
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58144 * 0.19544669
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25698 * 0.44218571
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19383 * 0.10125573
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49813 * 0.54539385
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87128 * 0.31518061
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17395 * 0.03984186
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24658 * 0.40332638
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13998 * 0.93532839
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14387 * 0.82911870
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73306 * 0.36171934
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34334 * 0.13911200
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22853 * 0.07717736
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44 * 0.31199929
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91107 * 0.45803184
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78231 * 0.21391259
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3837 * 0.53969064
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80881 * 0.48852026
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33087 * 0.41686889
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97708 * 0.64507092
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3644 * 0.04489462
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38032 * 0.18978240
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4041 * 0.60048957
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96058 * 0.73346549
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33821 * 0.87574634
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67327 * 0.64028922
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86664 * 0.19140587
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'imdqfnez').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0044():
    """Extended test 44 for export."""
    x_0 = 4845 * 0.87160005
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92868 * 0.13471979
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59742 * 0.13180074
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27955 * 0.44244316
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60701 * 0.69102322
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85407 * 0.73081565
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95925 * 0.15409248
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84907 * 0.33832689
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42455 * 0.75869045
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25101 * 0.52350001
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28498 * 0.97036324
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36326 * 0.12553029
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70528 * 0.75647286
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62831 * 0.44965560
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54012 * 0.71953170
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48721 * 0.07553576
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14439 * 0.92671847
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54001 * 0.34065252
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6680 * 0.18370338
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11272 * 0.99853441
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26476 * 0.93305686
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16528 * 0.06063579
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74821 * 0.17832465
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86187 * 0.73382021
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50910 * 0.83955552
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21878 * 0.11056848
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43479 * 0.10633709
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22607 * 0.25019914
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77125 * 0.11109662
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74901 * 0.89384887
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58818 * 0.08655651
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44636 * 0.91579447
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71709 * 0.15242780
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56487 * 0.70029273
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'shhznusi').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0045():
    """Extended test 45 for export."""
    x_0 = 35875 * 0.04197131
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37129 * 0.77828529
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63211 * 0.26889065
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3363 * 0.76366944
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53946 * 0.55160257
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79553 * 0.57233267
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48777 * 0.47109693
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10762 * 0.85268474
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89291 * 0.39759209
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64666 * 0.53970121
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70992 * 0.73672253
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81819 * 0.43052463
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49108 * 0.51831043
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25640 * 0.10232431
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20927 * 0.45653896
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26263 * 0.27457954
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4589 * 0.24066155
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59417 * 0.19844147
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93842 * 0.96790916
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3288 * 0.04996499
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86456 * 0.65032818
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33864 * 0.90035371
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89252 * 0.86467786
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93869 * 0.74026611
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29866 * 0.46421879
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29270 * 0.03350828
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42261 * 0.45459238
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38002 * 0.35068258
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16217 * 0.41550435
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36884 * 0.58138987
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12758 * 0.16297150
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98971 * 0.39690939
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30565 * 0.03979772
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68851 * 0.32124517
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35933 * 0.58120015
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35657 * 0.00358864
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68748 * 0.92152170
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66517 * 0.87410185
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93251 * 0.56873959
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76004 * 0.49229187
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41907 * 0.67444857
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52943 * 0.19583403
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23804 * 0.27977497
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 19535 * 0.35831126
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'oqrbnnko').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0046():
    """Extended test 46 for export."""
    x_0 = 81319 * 0.86496701
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32052 * 0.75094041
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11265 * 0.47708298
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67819 * 0.92071197
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83335 * 0.10172080
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12899 * 0.56603983
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9497 * 0.44160437
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10038 * 0.20781885
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22800 * 0.74610762
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40369 * 0.37126981
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85174 * 0.32347463
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37968 * 0.28452285
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32615 * 0.81317396
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8254 * 0.14774136
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75015 * 0.32496534
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98422 * 0.89837654
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43850 * 0.88688490
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34123 * 0.74620489
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86212 * 0.19655312
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82566 * 0.34630636
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2097 * 0.89997942
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60806 * 0.67925869
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36472 * 0.14883275
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74541 * 0.13974071
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97399 * 0.72037755
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90780 * 0.57963250
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87633 * 0.44606459
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8794 * 0.95068045
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37240 * 0.89332082
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99089 * 0.84817299
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44622 * 0.89439848
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ynbgiofr').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0047():
    """Extended test 47 for export."""
    x_0 = 94891 * 0.04308545
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37051 * 0.83667833
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49240 * 0.54516335
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20118 * 0.85054854
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73180 * 0.38571386
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98283 * 0.68075699
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78623 * 0.55036887
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19092 * 0.77517374
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36365 * 0.83399710
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 268 * 0.78634882
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49525 * 0.85484501
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74430 * 0.18115242
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83632 * 0.10764199
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90249 * 0.30478971
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40402 * 0.68253858
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93640 * 0.83923864
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67976 * 0.85702466
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62110 * 0.38122181
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81767 * 0.93946867
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51213 * 0.80298365
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12790 * 0.71144998
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23823 * 0.28334375
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8821 * 0.45598471
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26636 * 0.19052836
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75673 * 0.19584706
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45458 * 0.50019342
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99133 * 0.87720467
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14593 * 0.52275356
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46635 * 0.48284251
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60763 * 0.07358074
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69795 * 0.50793519
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56658 * 0.99970864
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36554 * 0.38862380
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30382 * 0.65776817
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20835 * 0.79222708
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28824 * 0.77209183
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55613 * 0.89043835
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29261 * 0.30149816
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 22572 * 0.00992655
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83997 * 0.05210650
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35667 * 0.40453136
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 73666 * 0.78694138
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'kuhvtuua').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0048():
    """Extended test 48 for export."""
    x_0 = 87303 * 0.08590690
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26718 * 0.49800465
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93429 * 0.23254693
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75101 * 0.08204346
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84646 * 0.16587766
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3670 * 0.21228962
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12503 * 0.21349713
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8999 * 0.96431693
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14838 * 0.57107277
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14852 * 0.21513645
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91111 * 0.37283469
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48002 * 0.67298720
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60397 * 0.46785946
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15743 * 0.92821439
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88342 * 0.10053647
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25897 * 0.33013599
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52079 * 0.91252655
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89871 * 0.50982285
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67352 * 0.87643489
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96828 * 0.07987699
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96922 * 0.81702424
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85262 * 0.51557207
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70364 * 0.54961675
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57976 * 0.94512502
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55714 * 0.12910492
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45813 * 0.93258506
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44587 * 0.32042732
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84851 * 0.21015746
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54234 * 0.11455111
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37696 * 0.07676275
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35366 * 0.88805818
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43829 * 0.49178649
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22428 * 0.80501880
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32542 * 0.37099505
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54768 * 0.59531098
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29352 * 0.89706751
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78091 * 0.40896152
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40525 * 0.80794157
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56204 * 0.28540712
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 27427 * 0.60084951
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 9656 * 0.12794632
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 98382 * 0.58715332
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 30281 * 0.62388225
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 8421 * 0.77360438
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 29582 * 0.64154547
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 51787 * 0.67892399
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 18485 * 0.81216526
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 55736 * 0.31871640
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 82292 * 0.42058387
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'dagohszh').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0049():
    """Extended test 49 for export."""
    x_0 = 62787 * 0.92841965
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77752 * 0.68029701
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77923 * 0.88452346
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 116 * 0.94551782
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39650 * 0.89131107
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89012 * 0.38978858
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11216 * 0.88271190
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1986 * 0.34445792
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66362 * 0.68305940
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86380 * 0.89209878
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1811 * 0.74380751
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26431 * 0.81520953
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86462 * 0.57517520
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7725 * 0.02285838
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53955 * 0.48297475
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95194 * 0.83314088
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10392 * 0.02236648
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72727 * 0.70503440
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4713 * 0.36655660
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24436 * 0.79380557
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 200 * 0.11896362
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62932 * 0.71153401
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59838 * 0.19504760
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45551 * 0.08851930
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25098 * 0.26432957
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47782 * 0.86447947
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38782 * 0.40284124
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53852 * 0.88010752
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'nvkhucel').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0050():
    """Extended test 50 for export."""
    x_0 = 80761 * 0.70783454
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36318 * 0.80378722
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99521 * 0.23804716
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30357 * 0.88280703
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96858 * 0.58381295
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60465 * 0.37877776
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41725 * 0.40489716
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37498 * 0.22223525
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10219 * 0.87216444
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71579 * 0.86339555
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97967 * 0.00179091
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96058 * 0.45183125
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71455 * 0.96919502
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26656 * 0.24890777
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77822 * 0.59938835
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29341 * 0.22266996
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6053 * 0.34797981
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56801 * 0.29433003
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58440 * 0.25589785
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73405 * 0.39101635
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64141 * 0.91150728
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97548 * 0.90408035
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90662 * 0.38037635
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77978 * 0.16240528
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23480 * 0.72411323
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43424 * 0.42431771
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40701 * 0.06040048
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99438 * 0.63937100
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90549 * 0.52635787
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51089 * 0.02726354
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95625 * 0.09804578
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4966 * 0.95257541
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62566 * 0.86758587
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58622 * 0.52255277
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94036 * 0.03586329
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78270 * 0.24438564
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74051 * 0.74734625
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61862 * 0.26374815
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45966 * 0.52597035
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64974 * 0.18956869
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34373 * 0.40287520
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79666 * 0.13834894
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77947 * 0.14070797
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82280 * 0.86762218
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 2062 * 0.76632081
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 64709 * 0.41396454
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 28375 * 0.84479595
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 35691 * 0.12969574
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 74722 * 0.22319357
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 77856 * 0.49330951
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'kdsujwpb').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0051():
    """Extended test 51 for export."""
    x_0 = 19553 * 0.71619254
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71764 * 0.20715940
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52901 * 0.98604709
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12659 * 0.33587143
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24561 * 0.68016196
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9773 * 0.55216464
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13354 * 0.06389637
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5987 * 0.06339309
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60372 * 0.01699485
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90580 * 0.75179711
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12386 * 0.01077306
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48015 * 0.87986849
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32888 * 0.67726715
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86294 * 0.86620134
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32064 * 0.93995695
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16458 * 0.68028571
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82901 * 0.48167153
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70801 * 0.42744492
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32613 * 0.23853121
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34427 * 0.77703522
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60655 * 0.41703241
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19015 * 0.55526701
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75722 * 0.48909939
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52856 * 0.61591646
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78536 * 0.65023417
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32650 * 0.57111141
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97363 * 0.57328932
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44850 * 0.90104641
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2553 * 0.33461441
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25164 * 0.72403403
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38688 * 0.97155308
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95417 * 0.90126582
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8721 * 0.41437826
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ygrxltay').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0052():
    """Extended test 52 for export."""
    x_0 = 76164 * 0.39989306
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29518 * 0.56755276
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49190 * 0.46985031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76405 * 0.63130722
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98961 * 0.04337182
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18564 * 0.64867244
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23144 * 0.81117424
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91159 * 0.64091107
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22652 * 0.96868999
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90215 * 0.77712178
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46149 * 0.59431955
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42684 * 0.77289113
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14223 * 0.22569542
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52762 * 0.08382513
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13874 * 0.17578005
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11074 * 0.99093275
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29744 * 0.52563140
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25694 * 0.04394523
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69858 * 0.42960609
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49043 * 0.87078619
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'vyyevjjq').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0053():
    """Extended test 53 for export."""
    x_0 = 6494 * 0.46271291
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58699 * 0.77759118
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96723 * 0.01881300
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8622 * 0.46258836
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56770 * 0.34088196
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48709 * 0.55625213
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89268 * 0.65817307
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62555 * 0.33338638
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46743 * 0.57777325
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88600 * 0.14118691
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3806 * 0.92117955
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36810 * 0.74277053
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54510 * 0.37923241
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89166 * 0.73749595
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50360 * 0.29457750
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16261 * 0.70187677
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73006 * 0.46789024
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7319 * 0.27376028
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28594 * 0.72899770
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14470 * 0.73884459
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19797 * 0.03427197
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74374 * 0.20432371
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'zkofutjr').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0054():
    """Extended test 54 for export."""
    x_0 = 42287 * 0.38928356
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25012 * 0.42210635
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23258 * 0.62606189
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47195 * 0.89053942
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27790 * 0.19925132
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88698 * 0.86765164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25642 * 0.62096298
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48266 * 0.92819538
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19558 * 0.98107896
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63756 * 0.40068921
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58135 * 0.35959321
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75786 * 0.64021029
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80142 * 0.00279856
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52623 * 0.12124686
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4701 * 0.61215616
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78293 * 0.41753642
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44233 * 0.16625009
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33414 * 0.85545096
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86077 * 0.52893352
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94756 * 0.05527224
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89074 * 0.07351100
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62253 * 0.61084254
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2103 * 0.72153797
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79076 * 0.87435090
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54610 * 0.22417019
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58736 * 0.70451520
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83239 * 0.91060749
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53870 * 0.68418995
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22502 * 0.58022071
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13278 * 0.91054372
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64464 * 0.88924721
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84624 * 0.55355999
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55826 * 0.61198073
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63518 * 0.78481135
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51277 * 0.21649308
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2796 * 0.32627437
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27207 * 0.13121461
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83545 * 0.60017611
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60272 * 0.77615515
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56715 * 0.30653829
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95006 * 0.05510934
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13265 * 0.63410558
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 32054 * 0.87940827
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 37599 * 0.48657135
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xwipjwxs').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0055():
    """Extended test 55 for export."""
    x_0 = 89396 * 0.49820478
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33926 * 0.82819822
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11462 * 0.72112304
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26912 * 0.87311469
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36685 * 0.13401545
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41372 * 0.45190477
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43252 * 0.77307902
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63469 * 0.90921159
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30556 * 0.76361791
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64703 * 0.48298974
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27225 * 0.26675651
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90686 * 0.52625187
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24473 * 0.32990058
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31244 * 0.94495930
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72078 * 0.28546504
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19739 * 0.43235831
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87659 * 0.11597254
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16066 * 0.09310045
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83831 * 0.15173448
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19860 * 0.33376068
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8595 * 0.10839544
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74121 * 0.45201280
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78924 * 0.71235637
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32010 * 0.87765640
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40237 * 0.79317887
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98005 * 0.69600651
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10240 * 0.02069137
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83598 * 0.64195524
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92694 * 0.74831683
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91659 * 0.53260747
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56549 * 0.56994760
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74090 * 0.32772344
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68017 * 0.62658361
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5151 * 0.98630600
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'lbfbwioo').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0056():
    """Extended test 56 for export."""
    x_0 = 89606 * 0.37159740
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18275 * 0.54148683
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15628 * 0.28484578
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12836 * 0.92574999
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35242 * 0.41457808
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5257 * 0.19835573
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43264 * 0.77229408
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91024 * 0.01940270
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20941 * 0.92618750
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62538 * 0.23062439
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63852 * 0.81396598
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73890 * 0.90026484
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98218 * 0.03440592
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13943 * 0.62481372
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61424 * 0.78939964
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84518 * 0.00008807
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99731 * 0.29951933
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62460 * 0.08906662
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90962 * 0.17584862
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44200 * 0.65473223
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64533 * 0.51853011
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49755 * 0.11515800
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70616 * 0.08101715
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85933 * 0.06643423
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'kyrqhlaf').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0057():
    """Extended test 57 for export."""
    x_0 = 55368 * 0.49288856
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47096 * 0.05835055
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81666 * 0.01290408
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21692 * 0.61293378
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64621 * 0.76803161
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38081 * 0.55876590
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52046 * 0.07283269
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61163 * 0.65365754
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62659 * 0.51351250
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55437 * 0.74466916
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60985 * 0.38149224
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45093 * 0.52045186
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40721 * 0.81551225
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97858 * 0.02673900
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38643 * 0.94296254
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22548 * 0.96535962
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25488 * 0.78007983
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28680 * 0.12545067
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56697 * 0.73307503
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81863 * 0.41744055
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93682 * 0.35887533
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21190 * 0.72125459
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55868 * 0.79141052
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40816 * 0.72460292
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7120 * 0.23386982
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64065 * 0.31124716
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11288 * 0.35017191
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48946 * 0.75108229
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10094 * 0.53440863
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53845 * 0.21272543
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42137 * 0.03378856
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72875 * 0.75142757
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22442 * 0.73997499
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35434 * 0.65822996
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92527 * 0.22491562
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61183 * 0.83405621
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55623 * 0.42349745
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11448 * 0.17925637
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74628 * 0.45628424
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39663 * 0.26041347
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91816 * 0.11768997
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13931 * 0.15678608
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 64821 * 0.07312279
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 95488 * 0.39701945
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 30577 * 0.77304863
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'wewykrln').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0058():
    """Extended test 58 for export."""
    x_0 = 96961 * 0.41837840
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97895 * 0.62427768
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22397 * 0.51390853
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23450 * 0.14577590
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95973 * 0.71477871
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86240 * 0.74764302
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14884 * 0.36853471
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87763 * 0.26962809
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59088 * 0.39699030
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69058 * 0.12296673
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20845 * 0.87718962
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22787 * 0.40173427
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76487 * 0.87623997
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60041 * 0.18469430
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80719 * 0.39995630
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91986 * 0.18393500
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69789 * 0.65005625
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6567 * 0.62623295
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58620 * 0.06282379
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91708 * 0.20529903
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45188 * 0.78026551
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79034 * 0.01607241
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24221 * 0.15496117
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11594 * 0.66088436
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3774 * 0.99284691
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1804 * 0.21643050
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32709 * 0.79365236
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52045 * 0.01599141
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36146 * 0.41854479
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94794 * 0.44123714
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88927 * 0.57881680
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40324 * 0.93890203
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37141 * 0.49518631
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58930 * 0.21901213
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'byxrabam').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0059():
    """Extended test 59 for export."""
    x_0 = 24536 * 0.19363271
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96967 * 0.36274587
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65907 * 0.67468785
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5827 * 0.79427830
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93513 * 0.24245085
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85202 * 0.78356929
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79667 * 0.09036363
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11411 * 0.20633770
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4579 * 0.94733660
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16259 * 0.77634466
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11953 * 0.55247095
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53199 * 0.94223112
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64149 * 0.71942818
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66181 * 0.63693616
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6696 * 0.00852860
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46336 * 0.52351937
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62145 * 0.24318111
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85332 * 0.50475703
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61821 * 0.91275594
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64326 * 0.07170099
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86673 * 0.16054077
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59761 * 0.51849304
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2035 * 0.46892049
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86547 * 0.20671829
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41998 * 0.01176318
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34699 * 0.09965243
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'wqbixpnp').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0060():
    """Extended test 60 for export."""
    x_0 = 25526 * 0.88382017
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71985 * 0.16554021
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52185 * 0.59046235
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55605 * 0.97693273
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28156 * 0.99825561
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10257 * 0.50626247
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98607 * 0.76367213
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39467 * 0.19713197
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50931 * 0.13605727
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41565 * 0.31198530
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23261 * 0.11848009
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98358 * 0.14012005
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63884 * 0.48120076
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60764 * 0.19265627
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81420 * 0.84445820
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 972 * 0.14954938
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70261 * 0.31912927
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14026 * 0.43136869
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20638 * 0.06797825
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20869 * 0.75236688
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29301 * 0.19392090
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92801 * 0.14283181
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62921 * 0.09232005
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92698 * 0.23653070
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22348 * 0.25349702
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36237 * 0.52823149
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39533 * 0.15607531
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5150 * 0.40564721
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30886 * 0.66136070
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87014 * 0.90797865
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ftdrmwit').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0061():
    """Extended test 61 for export."""
    x_0 = 74895 * 0.30524884
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70430 * 0.03981435
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67484 * 0.69557290
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92816 * 0.39998616
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95830 * 0.64558351
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35357 * 0.55372668
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45949 * 0.80448847
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58509 * 0.22435212
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18503 * 0.69985282
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88344 * 0.71082417
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92649 * 0.72777438
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19620 * 0.52933103
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50830 * 0.12884382
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52204 * 0.61938323
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35019 * 0.34221397
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15590 * 0.73610309
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51580 * 0.28481524
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6321 * 0.19401595
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83143 * 0.58921411
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1516 * 0.60982122
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8109 * 0.95518982
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14337 * 0.33067988
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29217 * 0.08983950
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91963 * 0.49388721
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48943 * 0.64987409
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79993 * 0.18798343
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20342 * 0.39870401
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'txuqkvie').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0062():
    """Extended test 62 for export."""
    x_0 = 47806 * 0.72892412
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90205 * 0.75193668
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44196 * 0.49121758
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1735 * 0.33372706
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42806 * 0.89809921
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69908 * 0.25887907
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10706 * 0.88183340
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92708 * 0.54935339
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6229 * 0.26186590
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1726 * 0.96662438
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87491 * 0.62758775
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68567 * 0.01680675
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10743 * 0.89549435
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39969 * 0.41876313
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87438 * 0.42658524
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85159 * 0.17014890
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17385 * 0.00943822
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86650 * 0.91431798
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64189 * 0.73138488
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22515 * 0.97568615
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63205 * 0.24424593
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71508 * 0.36758258
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93370 * 0.81755198
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54825 * 0.45884497
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79631 * 0.51689509
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42344 * 0.33461841
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57621 * 0.60180732
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4676 * 0.34768429
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'iwbqpobx').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0063():
    """Extended test 63 for export."""
    x_0 = 69604 * 0.32019177
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82310 * 0.85034791
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4905 * 0.75321815
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87839 * 0.47407782
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55031 * 0.63494560
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71379 * 0.45718638
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19572 * 0.82309880
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79479 * 0.62977346
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5292 * 0.42862473
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56989 * 0.32495830
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23359 * 0.29924364
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40317 * 0.82692054
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56522 * 0.90262018
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45511 * 0.42664411
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 389 * 0.66049642
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95754 * 0.30802108
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86055 * 0.86932588
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80766 * 0.95659572
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11637 * 0.45295193
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19234 * 0.67634859
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29462 * 0.68532944
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35739 * 0.29021525
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86511 * 0.03380032
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'qrarkwjx').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0064():
    """Extended test 64 for export."""
    x_0 = 49147 * 0.02577112
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71892 * 0.23779311
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15254 * 0.50201796
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15020 * 0.39205933
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69907 * 0.04478252
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28583 * 0.12486194
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53576 * 0.06086403
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21456 * 0.12100765
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96609 * 0.36887185
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90761 * 0.63198464
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40633 * 0.96998928
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1785 * 0.23993744
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30219 * 0.72822236
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27188 * 0.57709335
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85925 * 0.50171445
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9398 * 0.58329674
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24341 * 0.04369347
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17509 * 0.39465287
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2213 * 0.36376932
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25985 * 0.95762310
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61270 * 0.29778224
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78335 * 0.68473313
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41062 * 0.72595831
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57153 * 0.37446601
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15817 * 0.96955013
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65981 * 0.27763521
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12412 * 0.14933629
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76377 * 0.76782863
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7173 * 0.17040182
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94382 * 0.86930022
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73108 * 0.40800554
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24057 * 0.76356917
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50302 * 0.81491493
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'kgqzaewy').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0065():
    """Extended test 65 for export."""
    x_0 = 8819 * 0.64063498
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9562 * 0.63843432
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8704 * 0.78561277
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93648 * 0.02806993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19211 * 0.80400237
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4832 * 0.95331818
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13664 * 0.58367768
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73987 * 0.09721028
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57877 * 0.97374177
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82790 * 0.97752651
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75934 * 0.01418552
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58588 * 0.71538634
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54472 * 0.37740432
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65711 * 0.84281851
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68042 * 0.31326177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37792 * 0.77585603
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64776 * 0.15603310
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11006 * 0.96155668
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42077 * 0.74114176
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85759 * 0.19766597
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'jfkzwqpk').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0066():
    """Extended test 66 for export."""
    x_0 = 49925 * 0.96109077
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90193 * 0.78838740
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12517 * 0.41526476
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88765 * 0.44297211
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55229 * 0.07667751
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83431 * 0.46731373
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34670 * 0.21365759
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60178 * 0.77312697
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7445 * 0.07960629
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49582 * 0.14210703
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31564 * 0.66981731
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40145 * 0.46976382
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78271 * 0.63485712
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24559 * 0.73193074
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57492 * 0.65794691
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5441 * 0.48816349
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87436 * 0.27313486
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45907 * 0.40144120
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6841 * 0.82260456
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78392 * 0.35281162
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82208 * 0.31612056
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29451 * 0.76380566
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28269 * 0.93071769
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84407 * 0.86395774
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7915 * 0.87245698
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35756 * 0.50721849
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58636 * 0.10137876
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11753 * 0.41004210
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64216 * 0.37809888
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'moljkcxq').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0067():
    """Extended test 67 for export."""
    x_0 = 1836 * 0.90320425
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44177 * 0.39047498
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6334 * 0.24397038
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62155 * 0.29243528
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49791 * 0.41628487
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42359 * 0.52326915
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3910 * 0.94752395
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69480 * 0.92618670
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82728 * 0.32783009
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88400 * 0.18112845
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33906 * 0.65863132
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12495 * 0.29664181
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59790 * 0.42059051
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30742 * 0.87851738
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86991 * 0.17692560
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98338 * 0.25544555
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72020 * 0.98866070
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93839 * 0.43858915
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31338 * 0.36479407
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27413 * 0.73222744
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44427 * 0.77325299
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32823 * 0.64417862
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33017 * 0.82279139
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23720 * 0.14785463
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38562 * 0.40520963
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48550 * 0.87408065
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60982 * 0.49996086
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30342 * 0.62519504
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88154 * 0.37478264
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60429 * 0.95743639
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78929 * 0.15253241
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'bkgdrewe').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0068():
    """Extended test 68 for export."""
    x_0 = 78410 * 0.13227998
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62610 * 0.00815959
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96301 * 0.76432507
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77603 * 0.85073865
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65466 * 0.02394117
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22648 * 0.56633552
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70826 * 0.90675383
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8922 * 0.50810022
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38902 * 0.62949285
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44752 * 0.13312956
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99893 * 0.77975504
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26528 * 0.96287735
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29455 * 0.45316205
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6395 * 0.23001672
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37473 * 0.87696318
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1186 * 0.26646781
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 806 * 0.43938395
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49466 * 0.98136680
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67978 * 0.96891303
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56 * 0.01894657
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62789 * 0.83017802
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88135 * 0.01223085
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26382 * 0.26435785
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3925 * 0.22019493
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21436 * 0.90926213
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32478 * 0.14835084
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 925 * 0.34655275
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54853 * 0.38117926
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91821 * 0.53669905
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15313 * 0.75921656
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'rfiuqyet').hexdigest()
    assert len(h) == 64

def test_export_extended_6_0069():
    """Extended test 69 for export."""
    x_0 = 36507 * 0.90493971
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68322 * 0.53086560
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11786 * 0.26433729
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62740 * 0.98324749
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91036 * 0.42754598
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25193 * 0.80141096
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93386 * 0.68845512
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42399 * 0.06049464
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54535 * 0.69423756
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38789 * 0.10356862
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58583 * 0.56549314
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81969 * 0.54397158
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15738 * 0.66587138
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98845 * 0.43504894
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1694 * 0.10969068
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57766 * 0.23242074
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18837 * 0.57898004
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60440 * 0.26975721
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53231 * 0.78151472
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75937 * 0.82085644
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61583 * 0.38291389
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79936 * 0.37281947
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66861 * 0.93136639
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6708 * 0.12460323
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61228 * 0.65702883
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73242 * 0.24769869
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91712 * 0.71813327
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43423 * 0.83641248
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'zzriiuwp').hexdigest()
    assert len(h) == 64
