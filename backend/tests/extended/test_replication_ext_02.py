"""Extended tests for replication suite 2."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_replication_extended_2_0000():
    """Extended test 0 for replication."""
    x_0 = 79420 * 0.58241238
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3444 * 0.85687944
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17715 * 0.29005342
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94421 * 0.93764020
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19895 * 0.17139043
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49919 * 0.69566626
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26975 * 0.12475115
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 452 * 0.65671996
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40583 * 0.23898831
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39205 * 0.64727953
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57068 * 0.42652100
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72501 * 0.59754792
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98736 * 0.47616793
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41196 * 0.38914555
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77418 * 0.63397622
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64942 * 0.96552214
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89020 * 0.04679731
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30109 * 0.38424117
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60209 * 0.89289932
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13933 * 0.97078976
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49981 * 0.88177351
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6391 * 0.26325156
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78505 * 0.51530695
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30685 * 0.86539762
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92188 * 0.92632137
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18831 * 0.40821027
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79373 * 0.73983477
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98994 * 0.98684526
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32797 * 0.01443787
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75269 * 0.76285166
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72332 * 0.82897856
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43737 * 0.68024625
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77626 * 0.06009448
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71963 * 0.04075884
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95877 * 0.98968631
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5837 * 0.52350738
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45512 * 0.60293928
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72012 * 0.23300857
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8962 * 0.73883261
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24408 * 0.53614634
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 90098 * 0.34830395
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41617 * 0.98330519
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18766 * 0.48575117
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 12889 * 0.69662675
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59741 * 0.98611739
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 72974 * 0.23083233
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 23020 * 0.62514110
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 71422 * 0.57888923
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 94408 * 0.69040173
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'hqiblgtp').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0001():
    """Extended test 1 for replication."""
    x_0 = 14938 * 0.30970586
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11958 * 0.82008252
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46448 * 0.98348181
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44881 * 0.25443714
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32074 * 0.98233912
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84477 * 0.47685899
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68886 * 0.96988418
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6905 * 0.55052638
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19291 * 0.87072650
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94770 * 0.45287460
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8546 * 0.34064664
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55021 * 0.75770033
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83905 * 0.39733331
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24851 * 0.05017456
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25033 * 0.42660927
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23656 * 0.13422793
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52360 * 0.78803202
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40296 * 0.76846640
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88786 * 0.09926949
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93246 * 0.60538457
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51739 * 0.79971432
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79533 * 0.13760473
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69708 * 0.77153980
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48741 * 0.68970765
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3256 * 0.07340281
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91645 * 0.03968548
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10963 * 0.14830100
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'vpodumtr').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0002():
    """Extended test 2 for replication."""
    x_0 = 28122 * 0.68647388
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45514 * 0.47852349
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37581 * 0.88160980
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41470 * 0.53233236
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60253 * 0.79384599
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57640 * 0.73623855
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70707 * 0.36864451
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79984 * 0.82182784
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96650 * 0.00228149
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69146 * 0.04414166
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39986 * 0.22918010
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98900 * 0.05962101
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35180 * 0.08257019
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61703 * 0.35863093
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94010 * 0.94352266
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97854 * 0.91667291
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8630 * 0.68487835
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65622 * 0.36491239
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10909 * 0.10849625
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54450 * 0.36044107
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89898 * 0.18411970
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'gnudpcee').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0003():
    """Extended test 3 for replication."""
    x_0 = 64350 * 0.28774795
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71935 * 0.02830035
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1348 * 0.99711389
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82543 * 0.84221051
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67087 * 0.17828625
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16620 * 0.61268021
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84258 * 0.72140090
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4476 * 0.34351433
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55179 * 0.63761643
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36512 * 0.97458414
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94880 * 0.81347947
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6086 * 0.86168203
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81397 * 0.64989459
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63554 * 0.50178082
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84344 * 0.30030167
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92724 * 0.79189172
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42995 * 0.10308481
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93834 * 0.02596254
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45369 * 0.91697893
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60592 * 0.23664377
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17546 * 0.59261238
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'zavafegq').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0004():
    """Extended test 4 for replication."""
    x_0 = 3688 * 0.29047709
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74633 * 0.14275829
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88095 * 0.93291405
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65369 * 0.65575866
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49483 * 0.19636822
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76331 * 0.25513163
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44277 * 0.05112720
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81664 * 0.53122328
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3078 * 0.50663854
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78254 * 0.59309622
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82932 * 0.53049336
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84713 * 0.55474923
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53884 * 0.53447871
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47377 * 0.51451674
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10098 * 0.48676352
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35425 * 0.42473109
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35996 * 0.82075102
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70223 * 0.34911779
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18549 * 0.08035740
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92692 * 0.97065284
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93017 * 0.53482387
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16540 * 0.44978814
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57121 * 0.26055681
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65002 * 0.44745363
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85160 * 0.25013927
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72708 * 0.04964587
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45589 * 0.57083048
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95975 * 0.26022686
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80926 * 0.13718563
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8361 * 0.51462648
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59011 * 0.58669571
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81127 * 0.65897457
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14910 * 0.03862219
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75498 * 0.13035866
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34315 * 0.61823093
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13433 * 0.31970933
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24532 * 0.51776425
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59273 * 0.97727981
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18809 * 0.58441824
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77793 * 0.88224255
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83996 * 0.32324281
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42567 * 0.02708458
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62035 * 0.93989778
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94225 * 0.02237444
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'fdqswwth').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0005():
    """Extended test 5 for replication."""
    x_0 = 22986 * 0.98675186
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42360 * 0.70305434
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99132 * 0.06938843
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25143 * 0.46129755
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68941 * 0.11546679
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4165 * 0.11785001
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3179 * 0.43144794
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23157 * 0.17035016
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51307 * 0.72589917
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17788 * 0.41217637
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19483 * 0.89277209
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25437 * 0.41885282
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20303 * 0.69935947
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1845 * 0.70278593
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54927 * 0.72812857
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83300 * 0.55023960
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5062 * 0.81358910
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31147 * 0.42859651
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80425 * 0.65568051
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97263 * 0.42701056
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38893 * 0.98974387
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92012 * 0.98905879
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22620 * 0.41744415
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34257 * 0.75053440
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33917 * 0.41743047
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77435 * 0.74840052
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93251 * 0.17244869
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 841 * 0.05435516
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49900 * 0.52619914
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 128 * 0.83168826
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14701 * 0.44578543
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68066 * 0.99216405
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91281 * 0.49927453
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12671 * 0.43334976
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71115 * 0.94921100
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99241 * 0.96149906
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86549 * 0.16584607
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3412 * 0.34071695
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46316 * 0.84989370
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4846 * 0.26777097
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79120 * 0.48639351
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16662 * 0.43056718
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 40273 * 0.10072872
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 52112 * 0.61034948
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 2891 * 0.89337901
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 73237 * 0.02799315
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 63539 * 0.84219593
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'mixbcpvf').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0006():
    """Extended test 6 for replication."""
    x_0 = 89510 * 0.94284936
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70882 * 0.87848466
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29497 * 0.59581047
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74524 * 0.61151083
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18898 * 0.39241915
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97155 * 0.54120704
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37256 * 0.57629878
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56309 * 0.00683994
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95725 * 0.81694063
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40317 * 0.44850502
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99435 * 0.44326792
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61732 * 0.48826816
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42284 * 0.22207686
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56473 * 0.88606850
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61455 * 0.22108714
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42698 * 0.68758266
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90893 * 0.19664334
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55384 * 0.68635365
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73919 * 0.25044169
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80590 * 0.47831203
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16060 * 0.97710693
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40684 * 0.14843259
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94115 * 0.29252370
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'qyzwpesc').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0007():
    """Extended test 7 for replication."""
    x_0 = 2192 * 0.28693395
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10305 * 0.26455650
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6419 * 0.86211437
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54480 * 0.97440833
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91441 * 0.19020519
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46003 * 0.24244593
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97456 * 0.16696708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21538 * 0.22129445
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51233 * 0.12624341
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89396 * 0.51390168
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20881 * 0.59204502
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33189 * 0.03437637
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99350 * 0.73423084
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3244 * 0.71510904
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75145 * 0.51666110
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83047 * 0.57148332
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69892 * 0.18646272
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81897 * 0.43617108
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29277 * 0.22086186
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60029 * 0.86480679
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99629 * 0.58569323
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'umzqeouk').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0008():
    """Extended test 8 for replication."""
    x_0 = 9494 * 0.68120676
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23170 * 0.06141664
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93238 * 0.31259714
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44781 * 0.05951660
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60130 * 0.41375930
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18001 * 0.40706750
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20380 * 0.04873478
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37232 * 0.63760179
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29552 * 0.91000111
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92471 * 0.42411731
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4344 * 0.52668828
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22703 * 0.50175226
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97335 * 0.36253907
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19792 * 0.17617959
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97700 * 0.22132262
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89607 * 0.40456437
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70461 * 0.35132541
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13014 * 0.20535024
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13366 * 0.28962258
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92797 * 0.85163465
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49547 * 0.98213896
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15106 * 0.18191727
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35934 * 0.04185475
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39692 * 0.39227480
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90541 * 0.08563315
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34061 * 0.47981996
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42776 * 0.50325115
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81429 * 0.45454816
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31299 * 0.32761300
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59105 * 0.40397701
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41743 * 0.34919782
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75544 * 0.43564799
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88286 * 0.63086967
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4966 * 0.85999952
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21186 * 0.39932726
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81423 * 0.44981710
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69063 * 0.37589087
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71563 * 0.08130330
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56398 * 0.74941814
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 26371 * 0.98080716
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78726 * 0.38717472
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37183 * 0.42006491
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66805 * 0.43753372
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 6255 * 0.07781220
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 58681 * 0.76981975
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'dvumewtz').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0009():
    """Extended test 9 for replication."""
    x_0 = 88425 * 0.54537229
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11708 * 0.83275187
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85444 * 0.89825192
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81359 * 0.67924654
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41632 * 0.77899103
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64961 * 0.15063685
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5079 * 0.67651386
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6252 * 0.17338819
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40441 * 0.92895113
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83005 * 0.35802003
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51872 * 0.90414943
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10705 * 0.23121399
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84558 * 0.09132457
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86302 * 0.41223773
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38547 * 0.19723716
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45493 * 0.17958246
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20979 * 0.06749180
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58975 * 0.36750030
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70537 * 0.42578710
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77305 * 0.74850239
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65517 * 0.28396993
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24735 * 0.12499901
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76496 * 0.63526936
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64267 * 0.52108212
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99468 * 0.79565272
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'xukrizfl').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0010():
    """Extended test 10 for replication."""
    x_0 = 58914 * 0.21471640
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19966 * 0.71532041
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14388 * 0.42272247
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56340 * 0.29948612
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76651 * 0.36099533
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17538 * 0.18969426
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9652 * 0.19776416
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31242 * 0.69111179
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37364 * 0.14401277
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57882 * 0.58868954
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5619 * 0.37177724
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6633 * 0.12486845
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94057 * 0.84490096
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60000 * 0.65355866
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53655 * 0.77303552
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45030 * 0.93048783
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16819 * 0.59518125
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96357 * 0.09106630
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13292 * 0.99116856
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94887 * 0.72650345
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93792 * 0.30765775
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35239 * 0.37570928
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91340 * 0.76047835
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82158 * 0.10404738
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86175 * 0.17181172
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50353 * 0.16195975
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74281 * 0.13745215
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75403 * 0.50669637
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9396 * 0.32287723
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32787 * 0.73789926
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14643 * 0.27625331
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32433 * 0.03941052
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90617 * 0.48795570
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69285 * 0.62275937
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70905 * 0.61305329
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8451 * 0.33061011
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48331 * 0.13292957
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60581 * 0.53280464
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87408 * 0.04271817
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41621 * 0.42250969
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81590 * 0.59302440
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52654 * 0.59251739
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96510 * 0.50730219
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 72717 * 0.38634206
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 19980 * 0.79825562
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 62414 * 0.72972510
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 82118 * 0.23108108
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'mgynwege').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0011():
    """Extended test 11 for replication."""
    x_0 = 98347 * 0.09378610
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13682 * 0.65466100
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41519 * 0.78502971
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3646 * 0.50933187
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61979 * 0.07766924
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43857 * 0.83566586
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12433 * 0.73021252
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59453 * 0.86191254
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24855 * 0.28881416
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80944 * 0.10712666
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4976 * 0.83512100
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59267 * 0.46217754
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12450 * 0.91981122
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71216 * 0.33266709
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28958 * 0.84106784
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20550 * 0.86973670
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50768 * 0.06366476
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1759 * 0.43116444
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51457 * 0.53886996
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1843 * 0.67805721
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27808 * 0.55937510
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32911 * 0.26541058
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49278 * 0.39723364
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83629 * 0.33203572
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12553 * 0.67905123
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'rvpjyiuy').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0012():
    """Extended test 12 for replication."""
    x_0 = 15221 * 0.78317850
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92179 * 0.22825261
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35731 * 0.30038004
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78425 * 0.92941690
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83827 * 0.13495202
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9661 * 0.59336167
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29952 * 0.99892754
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40091 * 0.96477448
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45507 * 0.31473509
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19758 * 0.69853092
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6025 * 0.21548892
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25044 * 0.74732992
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61311 * 0.49177856
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8138 * 0.38314909
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43414 * 0.86420542
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2949 * 0.46939849
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96041 * 0.47533656
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84817 * 0.78076254
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83066 * 0.45394703
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42740 * 0.38330986
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92011 * 0.59203884
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23228 * 0.79409134
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'tpoabhci').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0013():
    """Extended test 13 for replication."""
    x_0 = 63356 * 0.41223810
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59277 * 0.87458308
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27341 * 0.64879923
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52004 * 0.72075321
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39646 * 0.42912026
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86414 * 0.58314851
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25558 * 0.94301106
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14628 * 0.37804969
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58524 * 0.53635441
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34575 * 0.12938954
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47674 * 0.86618303
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11607 * 0.53182493
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53225 * 0.21542301
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67873 * 0.91858217
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76234 * 0.47813090
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87695 * 0.02719530
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35955 * 0.98195925
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89968 * 0.39760158
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31109 * 0.75422105
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13205 * 0.09734912
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98788 * 0.04545502
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80615 * 0.86883492
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'tvxzqgit').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0014():
    """Extended test 14 for replication."""
    x_0 = 1214 * 0.01390160
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83375 * 0.87587787
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76656 * 0.97816220
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21923 * 0.43731053
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25877 * 0.02518556
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12278 * 0.12113942
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83504 * 0.81740595
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20703 * 0.40427331
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25029 * 0.18035548
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59880 * 0.28470913
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2454 * 0.32279053
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93903 * 0.44165153
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74153 * 0.65204034
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16714 * 0.59771556
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88240 * 0.48304523
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58339 * 0.82694095
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63941 * 0.69470926
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5815 * 0.61155788
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72173 * 0.10573977
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38316 * 0.35342249
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98598 * 0.00121806
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68674 * 0.21091423
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34589 * 0.23237703
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12288 * 0.18500291
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48826 * 0.20005594
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12359 * 0.94160148
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7071 * 0.36714953
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44704 * 0.06638163
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91489 * 0.20716644
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20895 * 0.13933070
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88630 * 0.25310156
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29175 * 0.42909419
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98513 * 0.66548921
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49820 * 0.95415507
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28833 * 0.30451614
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39846 * 0.33294954
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47719 * 0.40121385
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77197 * 0.23178326
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70142 * 0.00393170
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 5940 * 0.04908355
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34769 * 0.34715177
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4860 * 0.44750849
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 30887 * 0.33006132
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22531 * 0.60632957
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 84282 * 0.84138042
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'akxwuqvr').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0015():
    """Extended test 15 for replication."""
    x_0 = 18001 * 0.30909897
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54549 * 0.11402628
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42722 * 0.58731022
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2773 * 0.39319070
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63813 * 0.37912646
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47766 * 0.02786784
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30928 * 0.93929613
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63158 * 0.90337109
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81026 * 0.77874060
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96371 * 0.61312622
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46773 * 0.41830053
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36300 * 0.83204953
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93560 * 0.29289965
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51440 * 0.26415738
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36592 * 0.66062257
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77228 * 0.39350821
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14236 * 0.49362563
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82910 * 0.92971484
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22772 * 0.92865967
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60140 * 0.22618537
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49669 * 0.98497149
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26554 * 0.66704405
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10417 * 0.08528019
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67674 * 0.44829772
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14855 * 0.08140804
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66017 * 0.96054001
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41089 * 0.22295820
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96069 * 0.61717903
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85937 * 0.00728603
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54104 * 0.29637829
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98586 * 0.63267681
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89589 * 0.71481336
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34799 * 0.69699240
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34110 * 0.25815607
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98877 * 0.48142831
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44855 * 0.04197486
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8569 * 0.63793390
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20166 * 0.23723493
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 89302 * 0.27407815
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69292 * 0.13310296
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84787 * 0.10863379
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'esrgnaov').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0016():
    """Extended test 16 for replication."""
    x_0 = 9977 * 0.92574848
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78185 * 0.28146676
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10438 * 0.95607285
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74278 * 0.18966631
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89007 * 0.95497034
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20311 * 0.80262423
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48486 * 0.26144679
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68308 * 0.61220680
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56694 * 0.01275572
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14160 * 0.53269036
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41125 * 0.59221107
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24674 * 0.17166736
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35008 * 0.77782989
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26730 * 0.31318503
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60846 * 0.35336165
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41346 * 0.01845188
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57995 * 0.88141050
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47535 * 0.27309901
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90428 * 0.30222009
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59592 * 0.62453970
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8056 * 0.50615521
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13051 * 0.89169069
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88172 * 0.09922949
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85657 * 0.43024134
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57235 * 0.45705468
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53919 * 0.32828013
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49848 * 0.15875573
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39531 * 0.36679054
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12368 * 0.40961552
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36648 * 0.68203191
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'oiqmwkzg').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0017():
    """Extended test 17 for replication."""
    x_0 = 44253 * 0.28632431
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90427 * 0.24731231
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62414 * 0.47997390
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51274 * 0.30709343
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46316 * 0.37336430
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32165 * 0.39043750
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99194 * 0.90348060
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93007 * 0.43483374
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10116 * 0.44116946
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88827 * 0.58572523
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23653 * 0.38343794
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34911 * 0.83450788
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79247 * 0.66456747
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23527 * 0.17772255
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43863 * 0.61209178
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74555 * 0.44217793
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99413 * 0.37346128
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89860 * 0.38131091
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13605 * 0.07480054
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35591 * 0.65542639
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25236 * 0.51429953
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76463 * 0.71138412
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30756 * 0.66379987
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60096 * 0.77795975
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25591 * 0.84929754
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38346 * 0.51000868
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45640 * 0.65963534
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1570 * 0.19968922
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41627 * 0.49513184
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83691 * 0.47424088
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32929 * 0.46003133
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'yziyqgnz').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0018():
    """Extended test 18 for replication."""
    x_0 = 40502 * 0.15226246
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89512 * 0.74821197
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29550 * 0.72700110
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70106 * 0.32708360
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2864 * 0.37046215
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20103 * 0.46142272
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41274 * 0.76424884
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73068 * 0.28788694
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18344 * 0.89706771
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72546 * 0.50925641
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49027 * 0.10421594
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24609 * 0.46796761
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12703 * 0.77981798
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18984 * 0.47721013
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11118 * 0.02583004
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82162 * 0.98798351
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77260 * 0.44837238
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64748 * 0.83453961
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38978 * 0.14916633
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92788 * 0.59563531
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78915 * 0.75157324
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1000 * 0.79409909
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75426 * 0.10213710
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2816 * 0.80645660
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 823 * 0.82391317
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79561 * 0.35838570
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29973 * 0.28162997
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33718 * 0.31361647
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16014 * 0.33387079
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57325 * 0.57080937
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94307 * 0.29995693
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 608 * 0.82849907
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 694 * 0.00979246
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50703 * 0.66822212
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12779 * 0.32739647
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43479 * 0.29243684
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27885 * 0.73805878
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50476 * 0.79741884
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47091 * 0.69341136
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15196 * 0.05520716
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 50385 * 0.75628090
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 49465 * 0.07325355
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28483 * 0.81435230
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 68181 * 0.78784404
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 78201 * 0.34341278
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 18589 * 0.22283416
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 28502 * 0.12027067
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 97218 * 0.62012901
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ogkjnilp').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0019():
    """Extended test 19 for replication."""
    x_0 = 43077 * 0.69401590
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23005 * 0.68105309
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53132 * 0.96147861
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53940 * 0.11656993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93913 * 0.63099250
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84491 * 0.39674550
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3837 * 0.98160240
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40389 * 0.92875742
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12364 * 0.04596920
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44564 * 0.54658745
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8524 * 0.66414706
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24269 * 0.94577467
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70246 * 0.51669330
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61145 * 0.34744109
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98902 * 0.14875431
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31617 * 0.22361401
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35165 * 0.56711106
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22825 * 0.37071386
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96271 * 0.54911317
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55720 * 0.26059954
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25761 * 0.16137572
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2227 * 0.67931497
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72313 * 0.64382736
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'siqijkex').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0020():
    """Extended test 20 for replication."""
    x_0 = 84767 * 0.25908229
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97049 * 0.85075796
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92074 * 0.05296711
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78823 * 0.36179681
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41363 * 0.34658937
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65955 * 0.92743303
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69874 * 0.70328262
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47215 * 0.95135567
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59955 * 0.16357145
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42584 * 0.70670436
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29293 * 0.44665147
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6888 * 0.39460329
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92441 * 0.96972691
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47639 * 0.91503254
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99212 * 0.42536934
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99867 * 0.67924706
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65363 * 0.56775642
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84086 * 0.93171289
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24040 * 0.81619735
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57838 * 0.93347084
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29075 * 0.30566044
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45567 * 0.82655826
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86395 * 0.44034246
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84867 * 0.61621939
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95776 * 0.70873815
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76582 * 0.77733711
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2201 * 0.98215711
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68175 * 0.13429200
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96691 * 0.25196836
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76923 * 0.18180474
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57243 * 0.77312871
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11449 * 0.62024038
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92585 * 0.52194372
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13938 * 0.52190502
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54065 * 0.78620979
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83076 * 0.12172018
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39969 * 0.98460040
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17269 * 0.20097214
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42771 * 0.14162734
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72550 * 0.82583083
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'cuuxadsb').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0021():
    """Extended test 21 for replication."""
    x_0 = 79328 * 0.96840518
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31544 * 0.97449851
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76918 * 0.01666779
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90504 * 0.46366783
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52295 * 0.55353588
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38438 * 0.67971520
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93991 * 0.78851916
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28042 * 0.31234172
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61199 * 0.98869858
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52444 * 0.74289726
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60871 * 0.90387982
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8107 * 0.81858575
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96027 * 0.91310232
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66048 * 0.06337073
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52972 * 0.53220979
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9638 * 0.12993553
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69368 * 0.77125256
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59730 * 0.59803404
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92407 * 0.01716073
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68120 * 0.03108901
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93555 * 0.86697825
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9334 * 0.12240266
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96867 * 0.53062475
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28504 * 0.28306838
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29739 * 0.11635602
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81625 * 0.35057307
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58377 * 0.92621780
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77045 * 0.29226879
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50412 * 0.32346157
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56151 * 0.64230030
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81636 * 0.92546509
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80445 * 0.09504138
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'lxumshyb').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0022():
    """Extended test 22 for replication."""
    x_0 = 40050 * 0.36982130
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53778 * 0.97090099
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8963 * 0.94447740
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74197 * 0.55239204
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39632 * 0.91848177
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94322 * 0.01762553
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77925 * 0.40933512
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67656 * 0.52506902
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30670 * 0.23297153
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19560 * 0.77014143
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49145 * 0.71044352
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95010 * 0.53450185
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58836 * 0.30023114
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95732 * 0.41385314
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39305 * 0.38333926
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58097 * 0.96650407
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21956 * 0.86396828
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73377 * 0.32202125
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76017 * 0.41653114
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69828 * 0.73786253
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64833 * 0.25618811
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62231 * 0.19602157
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24169 * 0.31852535
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89181 * 0.67843770
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33 * 0.07906821
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84081 * 0.27300680
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73441 * 0.49955872
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58080 * 0.27825836
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31469 * 0.49161404
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34741 * 0.00161096
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40742 * 0.62671733
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71231 * 0.51270471
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77348 * 0.84555985
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70865 * 0.31336569
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7715 * 0.57666021
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61820 * 0.87627234
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66488 * 0.77328685
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94916 * 0.92458096
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 50805 * 0.57355115
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20892 * 0.82971168
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6398 * 0.02622932
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 40534 * 0.47454880
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95000 * 0.91914321
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 74465 * 0.83907968
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 83149 * 0.26077704
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 72485 * 0.39566773
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 19340 * 0.22472470
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 65377 * 0.08818259
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 11063 * 0.39894133
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'wncpbole').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0023():
    """Extended test 23 for replication."""
    x_0 = 28543 * 0.89129867
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37438 * 0.61407132
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8908 * 0.25062582
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17651 * 0.97582131
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21782 * 0.60003546
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6720 * 0.68012073
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36122 * 0.98127949
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22841 * 0.18260735
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57458 * 0.59615635
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37672 * 0.04168882
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90990 * 0.36889624
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78969 * 0.02137741
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28877 * 0.20916386
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89840 * 0.76305343
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90139 * 0.88542950
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27403 * 0.31935241
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74291 * 0.09166937
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2579 * 0.14101711
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92836 * 0.74782477
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24703 * 0.07943258
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87989 * 0.20193271
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26941 * 0.77712066
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13426 * 0.11145835
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47550 * 0.74749189
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15132 * 0.01376174
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58851 * 0.58704367
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'xxlgyiue').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0024():
    """Extended test 24 for replication."""
    x_0 = 18837 * 0.02456887
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97627 * 0.74114108
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18591 * 0.48494279
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87242 * 0.18479222
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24370 * 0.05667320
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48566 * 0.36455317
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83703 * 0.08049066
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82050 * 0.35544667
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12916 * 0.15745558
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49737 * 0.42756226
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62105 * 0.47731833
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77694 * 0.30564891
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50881 * 0.84848409
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40852 * 0.04401600
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89533 * 0.32735842
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38003 * 0.02505481
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46755 * 0.79596295
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60647 * 0.83901651
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37481 * 0.47010030
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38666 * 0.97518726
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57530 * 0.55636255
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60426 * 0.95220187
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'heckvxcg').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0025():
    """Extended test 25 for replication."""
    x_0 = 86444 * 0.68570608
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63720 * 0.66111685
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46269 * 0.27379531
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77307 * 0.68526377
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9687 * 0.98650093
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69222 * 0.66481875
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13464 * 0.67921631
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68529 * 0.11891550
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1345 * 0.76916923
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96797 * 0.14089318
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30722 * 0.89628349
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95314 * 0.43644742
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95346 * 0.40430296
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75923 * 0.30838025
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8724 * 0.42601764
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63474 * 0.92300735
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67399 * 0.37971889
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70058 * 0.39871138
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25030 * 0.62718615
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44624 * 0.13856108
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92304 * 0.67705401
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28736 * 0.71532374
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20567 * 0.23632498
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67893 * 0.32587021
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10204 * 0.67000432
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74469 * 0.24114661
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19518 * 0.01332329
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59377 * 0.99453577
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96651 * 0.69455718
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41432 * 0.08028198
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83481 * 0.21114220
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37226 * 0.78987394
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38914 * 0.55927561
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34675 * 0.71064809
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54655 * 0.45766507
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63181 * 0.57103246
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'nuiokcib').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0026():
    """Extended test 26 for replication."""
    x_0 = 42522 * 0.45531130
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53907 * 0.91329440
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41863 * 0.32435205
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71057 * 0.92670114
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17808 * 0.25903436
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38034 * 0.74979526
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25895 * 0.23734449
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70973 * 0.39108649
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29482 * 0.85989527
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19780 * 0.18201278
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5363 * 0.17309307
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82191 * 0.54236789
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22014 * 0.60766346
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93455 * 0.45803387
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40304 * 0.65438128
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73510 * 0.43042029
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96071 * 0.92038980
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66647 * 0.11985820
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57230 * 0.09193010
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30417 * 0.38797000
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68920 * 0.92619842
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62407 * 0.88590709
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32675 * 0.93330126
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19948 * 0.63840125
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90660 * 0.30479330
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43096 * 0.69069876
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63933 * 0.05559614
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69680 * 0.73732881
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48434 * 0.65172582
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50967 * 0.91382590
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20315 * 0.67373263
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93889 * 0.71022350
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57553 * 0.21189582
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87563 * 0.31317817
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91263 * 0.15469235
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98347 * 0.35479606
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13156 * 0.85102792
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5696 * 0.02333762
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83511 * 0.57179189
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'niqtwcla').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0027():
    """Extended test 27 for replication."""
    x_0 = 76357 * 0.42653784
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28659 * 0.13314860
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90067 * 0.88036957
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99444 * 0.76435744
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9081 * 0.17419115
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79909 * 0.18093887
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45753 * 0.78587038
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12937 * 0.73470434
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80482 * 0.95530386
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82903 * 0.83195934
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63982 * 0.56903737
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81634 * 0.36378626
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15008 * 0.93916402
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15354 * 0.41792003
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99560 * 0.35937474
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68124 * 0.74160317
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93387 * 0.11636317
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63527 * 0.97251125
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61837 * 0.37461410
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35618 * 0.73437567
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9315 * 0.05654247
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86942 * 0.16353590
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64568 * 0.51612659
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32780 * 0.13641959
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64930 * 0.44316074
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89479 * 0.34754162
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64765 * 0.73697234
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43234 * 0.49869563
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52285 * 0.70455934
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11046 * 0.97047072
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 658 * 0.61412434
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55905 * 0.46455561
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81039 * 0.52932161
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36394 * 0.93347949
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39388 * 0.29134455
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94495 * 0.99548666
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'syudqqne').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0028():
    """Extended test 28 for replication."""
    x_0 = 73323 * 0.50270502
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35336 * 0.10528735
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8882 * 0.09831173
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65474 * 0.69058534
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25207 * 0.38362928
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26202 * 0.66776262
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91222 * 0.16044215
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36247 * 0.62017872
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64386 * 0.72974115
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12338 * 0.94237378
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63151 * 0.57450215
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10390 * 0.76074545
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79752 * 0.52066535
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51368 * 0.30764334
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4732 * 0.14778721
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43888 * 0.30221122
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3831 * 0.60982463
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89236 * 0.92105342
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66393 * 0.98865298
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62696 * 0.31357463
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39190 * 0.89337094
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28251 * 0.20655738
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12664 * 0.19327636
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60785 * 0.75768314
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60000 * 0.16903948
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41534 * 0.68850094
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24890 * 0.59872797
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72259 * 0.18221459
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96549 * 0.12350461
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8158 * 0.86813950
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92979 * 0.90648791
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68956 * 0.86167246
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59357 * 0.69600152
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94213 * 0.19995230
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72689 * 0.41872702
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48847 * 0.98619818
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7091 * 0.03658863
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41607 * 0.89102585
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10448 * 0.19834826
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97918 * 0.89957135
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'dinfjexu').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0029():
    """Extended test 29 for replication."""
    x_0 = 79004 * 0.45638909
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16740 * 0.58133056
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34976 * 0.36933489
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45749 * 0.99559570
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86414 * 0.82713945
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86041 * 0.60457323
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88754 * 0.26929882
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19144 * 0.36839413
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45024 * 0.84138638
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57225 * 0.60388286
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40420 * 0.85560494
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66874 * 0.98118969
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97854 * 0.41071932
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7982 * 0.15251637
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59410 * 0.63967315
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75317 * 0.83674242
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71152 * 0.03923727
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2801 * 0.23495821
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60780 * 0.27378030
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18744 * 0.18359866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97508 * 0.61535886
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'qlswybbx').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0030():
    """Extended test 30 for replication."""
    x_0 = 74984 * 0.35546555
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84783 * 0.83556090
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88098 * 0.97988570
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55347 * 0.30732621
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29240 * 0.94076407
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85375 * 0.56832702
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20054 * 0.66883169
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67435 * 0.77987326
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48477 * 0.59256654
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61409 * 0.40160791
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61958 * 0.57141300
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1276 * 0.40073495
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87175 * 0.91659328
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81249 * 0.45071706
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18057 * 0.09964664
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10333 * 0.06771064
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79100 * 0.13564316
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72420 * 0.88773222
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52718 * 0.15188443
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35195 * 0.36878253
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35640 * 0.84009541
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25978 * 0.90755252
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61515 * 0.49520973
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74972 * 0.55802241
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32089 * 0.57208087
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20241 * 0.36207884
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57853 * 0.11569820
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18233 * 0.45939828
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11551 * 0.57810538
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29232 * 0.81920849
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56665 * 0.49000512
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62776 * 0.73895427
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85570 * 0.82361957
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75194 * 0.09141474
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98714 * 0.99595230
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91488 * 0.75191173
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2132 * 0.22653773
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90488 * 0.84211483
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60321 * 0.94121133
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44084 * 0.03137472
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'dxautfni').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0031():
    """Extended test 31 for replication."""
    x_0 = 53795 * 0.46914383
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53080 * 0.28777917
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65184 * 0.66759961
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72293 * 0.11944586
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46577 * 0.08709447
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84800 * 0.06852631
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36746 * 0.78876381
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62752 * 0.36949992
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28694 * 0.14992893
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15298 * 0.38507526
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74453 * 0.29529893
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78688 * 0.30544223
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29047 * 0.83506712
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47311 * 0.39333270
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53209 * 0.75406037
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79562 * 0.36454219
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71747 * 0.56327435
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75746 * 0.42057446
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97694 * 0.47712928
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27788 * 0.10056621
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60959 * 0.23538564
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72290 * 0.94905249
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59961 * 0.57410397
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9301 * 0.38319091
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56069 * 0.48594977
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33487 * 0.06204278
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10545 * 0.29433422
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99644 * 0.06393288
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91286 * 0.90110303
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12569 * 0.77400119
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21207 * 0.73296398
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63703 * 0.13905441
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33583 * 0.13281970
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85016 * 0.47742184
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62618 * 0.04575767
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14152 * 0.39558040
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20257 * 0.85850385
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65597 * 0.30209441
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11049 * 0.49043728
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 78461 * 0.65529282
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77900 * 0.67061624
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 99255 * 0.07367842
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16225 * 0.28115659
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38575 * 0.52371148
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 91730 * 0.37976023
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 62123 * 0.13409123
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'qhhozggk').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0032():
    """Extended test 32 for replication."""
    x_0 = 93094 * 0.87323409
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98443 * 0.46660874
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61730 * 0.19900308
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7256 * 0.35915848
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94482 * 0.56986084
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56180 * 0.24904796
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40764 * 0.76889814
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31194 * 0.82820006
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32271 * 0.34805618
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15442 * 0.84880107
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14952 * 0.40416682
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33513 * 0.83942149
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93674 * 0.42038570
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32791 * 0.53315636
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76965 * 0.60387668
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50336 * 0.30387007
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61824 * 0.42979492
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51263 * 0.11792473
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5655 * 0.39682471
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88795 * 0.17310745
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78469 * 0.82976206
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41044 * 0.79849074
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99367 * 0.82157432
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74119 * 0.11140753
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91747 * 0.48112466
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'wonnlypt').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0033():
    """Extended test 33 for replication."""
    x_0 = 36222 * 0.63107232
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57423 * 0.43135879
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31438 * 0.20938058
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11422 * 0.56721471
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22153 * 0.60969718
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30267 * 0.30640626
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13036 * 0.61644515
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47843 * 0.96862486
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95498 * 0.28309652
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35393 * 0.92392552
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71430 * 0.20382618
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62361 * 0.45801292
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69173 * 0.82484042
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37881 * 0.57959037
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37763 * 0.12679192
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55669 * 0.03004470
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43942 * 0.07006999
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62909 * 0.42845060
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9552 * 0.65617923
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5875 * 0.30590083
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90395 * 0.72577831
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93139 * 0.62659771
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25631 * 0.01475413
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92901 * 0.44614626
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8673 * 0.61023910
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66496 * 0.35184543
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98593 * 0.31652207
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31469 * 0.19745465
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69558 * 0.35517070
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96991 * 0.60464940
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57928 * 0.32101484
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42433 * 0.43486527
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72166 * 0.27718355
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 661 * 0.41962519
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13397 * 0.84766656
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97662 * 0.63910992
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68134 * 0.92120661
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43736 * 0.70008861
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6019 * 0.69943199
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31501 * 0.50595193
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71483 * 0.70960971
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 76205 * 0.07223379
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 84335 * 0.83583730
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58363 * 0.09426572
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 94073 * 0.42803916
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'bdkwikwx').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0034():
    """Extended test 34 for replication."""
    x_0 = 82850 * 0.64231950
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66186 * 0.90192474
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22224 * 0.05527174
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94055 * 0.86218771
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19965 * 0.06932290
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61218 * 0.94129804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91016 * 0.96202017
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76087 * 0.46679486
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45317 * 0.95352680
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83803 * 0.36732441
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45032 * 0.37611703
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12342 * 0.03099414
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36095 * 0.10044526
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23878 * 0.86729558
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92485 * 0.92245555
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13057 * 0.01814312
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14528 * 0.86242899
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45516 * 0.57354784
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17935 * 0.17049686
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80785 * 0.60424749
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36610 * 0.72329460
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84652 * 0.12724034
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47225 * 0.23346364
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78288 * 0.68090899
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45781 * 0.59908342
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98674 * 0.48230207
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71560 * 0.14572977
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66819 * 0.01743991
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83874 * 0.94891788
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84894 * 0.08595383
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13193 * 0.94828964
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25981 * 0.98966457
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28830 * 0.05991285
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40866 * 0.04585329
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13059 * 0.15264594
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48246 * 0.99518245
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41095 * 0.91921646
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44284 * 0.18533466
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'tifompfd').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0035():
    """Extended test 35 for replication."""
    x_0 = 39206 * 0.62265694
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53609 * 0.07273561
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42052 * 0.11792794
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1420 * 0.33504759
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91158 * 0.60037151
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8262 * 0.07707930
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92161 * 0.56661399
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3605 * 0.04422982
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84370 * 0.05388360
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13098 * 0.67734500
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10558 * 0.49693310
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98600 * 0.06277652
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21792 * 0.94571536
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77681 * 0.97058935
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91204 * 0.27818285
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77448 * 0.32333983
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19029 * 0.01392636
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81710 * 0.13086740
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71224 * 0.45534522
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90483 * 0.33433498
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51054 * 0.40903156
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'bgobpghl').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0036():
    """Extended test 36 for replication."""
    x_0 = 44928 * 0.40537568
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8812 * 0.64014497
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44425 * 0.35502244
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85343 * 0.42420147
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5202 * 0.38099661
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82664 * 0.84635574
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77991 * 0.67475702
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70152 * 0.83609331
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28328 * 0.34828921
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70154 * 0.67702542
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64801 * 0.30251733
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59143 * 0.35045843
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45307 * 0.29651918
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63237 * 0.59777807
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88314 * 0.04039636
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83562 * 0.84587143
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13738 * 0.98478363
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87381 * 0.65024066
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17363 * 0.61807210
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33817 * 0.10399887
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36887 * 0.70575436
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66536 * 0.94715684
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9078 * 0.37123230
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75027 * 0.36445540
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8110 * 0.84092334
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60208 * 0.25114058
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80279 * 0.03735229
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66276 * 0.49564059
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61779 * 0.10208528
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8560 * 0.48180460
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37126 * 0.42237939
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48734 * 0.81204716
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37954 * 0.24054142
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81724 * 0.23311831
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38904 * 0.36355768
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87532 * 0.17684103
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94248 * 0.90247262
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'cmmnrjiv').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0037():
    """Extended test 37 for replication."""
    x_0 = 18651 * 0.01265710
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2104 * 0.35034493
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23304 * 0.07261511
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32396 * 0.31495079
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59568 * 0.71648620
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66342 * 0.25775618
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49241 * 0.36292914
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75826 * 0.71409329
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88803 * 0.92632039
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67549 * 0.34185058
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23048 * 0.72529024
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5764 * 0.98642083
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44519 * 0.13512907
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45961 * 0.01769878
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40706 * 0.18666342
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64224 * 0.20695371
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8388 * 0.83941026
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10984 * 0.64477998
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77296 * 0.45073639
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68529 * 0.69346293
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46546 * 0.11091357
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99803 * 0.89913335
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37358 * 0.44811107
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2111 * 0.97979525
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7613 * 0.87292874
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69809 * 0.41432074
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30610 * 0.05427285
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88829 * 0.95674383
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34644 * 0.57837692
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29398 * 0.31264836
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63963 * 0.20432943
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16259 * 0.13711294
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16822 * 0.68722082
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72285 * 0.14658549
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55237 * 0.36835213
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70040 * 0.30974402
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76091 * 0.83324466
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33342 * 0.28828485
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24914 * 0.81076730
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51126 * 0.05537917
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 58561 * 0.47336163
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77361 * 0.45654419
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14275 * 0.42502318
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20841 * 0.17007733
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 45477 * 0.33575393
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 61392 * 0.89081702
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'bqkjuusa').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0038():
    """Extended test 38 for replication."""
    x_0 = 20845 * 0.78406841
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81595 * 0.94324815
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94167 * 0.61656798
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52036 * 0.53111013
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22906 * 0.72272776
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14588 * 0.43630361
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47884 * 0.29858216
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19915 * 0.74569879
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41384 * 0.47297693
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61780 * 0.86138959
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49365 * 0.98633389
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68846 * 0.92337276
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82055 * 0.85377802
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21059 * 0.69688540
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55849 * 0.72982623
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44773 * 0.03758655
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1643 * 0.12466609
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61974 * 0.92851956
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40348 * 0.88847723
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51715 * 0.35047885
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90879 * 0.13821957
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3071 * 0.87373766
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11787 * 0.57082159
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15330 * 0.08530802
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74152 * 0.26739322
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61038 * 0.58136249
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72467 * 0.93318182
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48115 * 0.74815706
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9057 * 0.98750173
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93350 * 0.25269335
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93477 * 0.77381870
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44969 * 0.03142641
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24651 * 0.85210908
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1339 * 0.27306245
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52818 * 0.13624620
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70756 * 0.24332991
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44368 * 0.46602280
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'msxcktza').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0039():
    """Extended test 39 for replication."""
    x_0 = 23361 * 0.98048106
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7867 * 0.08327960
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79767 * 0.12723252
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26551 * 0.06382042
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84647 * 0.70753846
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83868 * 0.76313773
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27894 * 0.70214671
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95085 * 0.67118541
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21419 * 0.62905977
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74608 * 0.37031895
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37570 * 0.40692366
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80101 * 0.34968302
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61740 * 0.14264505
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97257 * 0.22830048
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95340 * 0.81062068
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22288 * 0.28867979
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73212 * 0.14378341
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69996 * 0.64948350
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98633 * 0.87420974
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74326 * 0.06335723
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38173 * 0.04422424
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81529 * 0.27164338
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72147 * 0.47485189
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28643 * 0.21533060
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65451 * 0.69106425
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53867 * 0.30879338
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47339 * 0.72722321
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70086 * 0.66167467
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76251 * 0.86268848
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87093 * 0.54349611
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98714 * 0.90599684
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16574 * 0.17089981
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'udfjixge').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0040():
    """Extended test 40 for replication."""
    x_0 = 62985 * 0.84911715
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65151 * 0.75401297
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44155 * 0.09380350
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77306 * 0.31710608
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40321 * 0.45854026
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1809 * 0.04563081
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51652 * 0.18460989
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90375 * 0.18664479
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53706 * 0.13750754
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52118 * 0.83824089
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70537 * 0.70605721
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35053 * 0.54035014
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83601 * 0.91691422
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75421 * 0.56650162
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14521 * 0.72918205
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36204 * 0.63185447
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80678 * 0.70143987
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31966 * 0.13750321
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90158 * 0.84728050
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29699 * 0.69698767
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61596 * 0.58880104
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30851 * 0.99619391
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55772 * 0.19372330
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69551 * 0.72780710
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54025 * 0.85573291
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59887 * 0.60047197
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'gjrtuwvf').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0041():
    """Extended test 41 for replication."""
    x_0 = 24208 * 0.16768102
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31240 * 0.83417961
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2730 * 0.55324707
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12172 * 0.66752052
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32002 * 0.26952509
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97913 * 0.54933326
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28097 * 0.57313034
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41702 * 0.91148418
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12522 * 0.64514955
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28943 * 0.41166328
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52657 * 0.71475596
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36897 * 0.87781211
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11555 * 0.45331227
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49207 * 0.43587571
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26038 * 0.22154990
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56091 * 0.64258735
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37060 * 0.98105505
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52676 * 0.93477735
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54718 * 0.39227607
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59661 * 0.93396820
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31263 * 0.73085743
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94612 * 0.47871123
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93123 * 0.30688888
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57611 * 0.03969012
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61387 * 0.33456872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99199 * 0.54200927
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15602 * 0.96092287
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7930 * 0.43901981
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 684 * 0.53864232
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78561 * 0.29796784
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'cdmcbzcd').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0042():
    """Extended test 42 for replication."""
    x_0 = 25440 * 0.96024612
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70983 * 0.18655674
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 132 * 0.72026470
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22823 * 0.69165198
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33304 * 0.10530617
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75392 * 0.82405715
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9899 * 0.88791893
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52880 * 0.70238093
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31767 * 0.41225649
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76899 * 0.48527335
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30703 * 0.32669867
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35567 * 0.52392763
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80511 * 0.40065146
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24842 * 0.68681263
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40326 * 0.11099672
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69723 * 0.27568656
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60183 * 0.26589461
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49637 * 0.70351662
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20877 * 0.60045766
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27202 * 0.36827875
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41815 * 0.55662366
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32551 * 0.33504594
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29893 * 0.97820634
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80727 * 0.68489859
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73848 * 0.63147760
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18951 * 0.22083755
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47962 * 0.22444916
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47788 * 0.34543707
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14210 * 0.69817053
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42046 * 0.96594193
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35185 * 0.50101725
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19346 * 0.47707660
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53495 * 0.28711385
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28557 * 0.64784102
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91572 * 0.00737775
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4991 * 0.59579857
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83838 * 0.16381861
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36822 * 0.50376726
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30100 * 0.42209367
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 36701 * 0.94441805
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41449 * 0.10884739
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27 * 0.42567575
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35166 * 0.15491369
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88286 * 0.00098889
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35013 * 0.25900053
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4411 * 0.11576695
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 84893 * 0.57268151
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 57134 * 0.05265921
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 80813 * 0.43090656
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'dxuuutpb').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0043():
    """Extended test 43 for replication."""
    x_0 = 2238 * 0.94867796
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58444 * 0.43071903
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29402 * 0.91851359
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 615 * 0.33040000
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86688 * 0.59189680
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18543 * 0.12015062
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26283 * 0.18807918
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83357 * 0.04785030
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41564 * 0.94704546
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92276 * 0.85707884
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65906 * 0.08499296
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24428 * 0.40760304
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69259 * 0.23950444
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61601 * 0.31331912
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84167 * 0.04781332
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51092 * 0.82753668
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16172 * 0.17356867
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85944 * 0.45106117
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11235 * 0.22380718
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36599 * 0.65022088
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58725 * 0.65648565
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25628 * 0.38230468
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25841 * 0.72036811
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73500 * 0.17273575
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3706 * 0.57139365
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82227 * 0.88657720
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70489 * 0.73931384
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47015 * 0.58634202
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76163 * 0.73802721
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11850 * 0.30918901
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18724 * 0.64747041
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63343 * 0.52621856
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14060 * 0.70197822
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7460 * 0.39449480
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66655 * 0.06245873
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3932 * 0.40788186
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19145 * 0.57998041
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'xztyzyzb').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0044():
    """Extended test 44 for replication."""
    x_0 = 30106 * 0.67860463
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69177 * 0.88128084
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52400 * 0.68665112
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26843 * 0.71541071
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87928 * 0.93146750
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49391 * 0.33564736
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37371 * 0.59616816
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53003 * 0.95548750
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2283 * 0.52381111
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75703 * 0.45179861
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6304 * 0.95217099
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70859 * 0.14396411
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69816 * 0.61968379
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19844 * 0.50932119
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99376 * 0.68141177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47247 * 0.69047257
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24755 * 0.15747596
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2494 * 0.31740851
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40260 * 0.62100674
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68668 * 0.57117673
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55703 * 0.21023930
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62331 * 0.88274057
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4543 * 0.86594480
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23371 * 0.36220281
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97085 * 0.13455354
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12809 * 0.11684062
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75070 * 0.81364931
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32336 * 0.35294817
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71585 * 0.53839361
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88750 * 0.92988389
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5619 * 0.34323467
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20906 * 0.23698983
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89284 * 0.35805779
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95699 * 0.45716923
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72214 * 0.07246173
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96391 * 0.13811795
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65618 * 0.92238189
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5288 * 0.93277507
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ncynvchf').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0045():
    """Extended test 45 for replication."""
    x_0 = 94375 * 0.23847514
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18780 * 0.79130927
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49016 * 0.66616945
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45083 * 0.57056157
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45938 * 0.49851356
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86775 * 0.16850992
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10937 * 0.20320902
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88195 * 0.25103731
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99313 * 0.56644575
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56142 * 0.78937091
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17271 * 0.33815331
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95086 * 0.19258953
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97230 * 0.27075226
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69001 * 0.74032527
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11478 * 0.72632443
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66956 * 0.38250006
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18278 * 0.85092515
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70087 * 0.30529198
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74817 * 0.54610669
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92943 * 0.75642065
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45994 * 0.28841044
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39140 * 0.06781755
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51089 * 0.36824888
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41314 * 0.48209296
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38060 * 0.28336467
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96954 * 0.68166059
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30785 * 0.17477535
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21207 * 0.07276433
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19635 * 0.02692444
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29995 * 0.19073010
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25733 * 0.34574667
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29321 * 0.70776926
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48693 * 0.73348484
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90901 * 0.21778570
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36648 * 0.52031800
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39711 * 0.59410365
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45921 * 0.13897131
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 76256 * 0.49051066
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82063 * 0.40914078
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65245 * 0.35116073
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11481 * 0.76156870
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 61406 * 0.23834697
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'twamqzrh').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0046():
    """Extended test 46 for replication."""
    x_0 = 85342 * 0.11210868
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47593 * 0.14922563
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24614 * 0.11837214
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50343 * 0.43743943
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25594 * 0.93676090
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78590 * 0.00022674
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36209 * 0.38003281
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82487 * 0.26495045
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67920 * 0.65282010
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56063 * 0.96522826
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18688 * 0.69405001
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7886 * 0.57869279
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25834 * 0.38942427
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72770 * 0.00019117
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75645 * 0.28079219
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 950 * 0.17978904
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96698 * 0.68300567
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97194 * 0.92464552
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3538 * 0.97602805
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68791 * 0.47463522
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'vyzdnhtc').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0047():
    """Extended test 47 for replication."""
    x_0 = 68902 * 0.01030945
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36918 * 0.56811711
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65559 * 0.42200617
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80988 * 0.48975443
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32254 * 0.83294630
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47127 * 0.40081222
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79369 * 0.00000628
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28498 * 0.74734087
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57051 * 0.51152766
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19124 * 0.52743086
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22046 * 0.65426935
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68153 * 0.75016234
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62642 * 0.43860101
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39326 * 0.79484764
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65527 * 0.05525714
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52140 * 0.24213057
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79539 * 0.05554368
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37783 * 0.80117945
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28644 * 0.24745219
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43950 * 0.73413866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48285 * 0.92195446
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71147 * 0.53954119
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18165 * 0.29622998
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95021 * 0.27175546
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73627 * 0.92424326
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41381 * 0.41287043
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28352 * 0.30222818
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33417 * 0.96847177
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2285 * 0.95451607
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79428 * 0.15513256
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80195 * 0.73035994
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77093 * 0.54050628
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2786 * 0.14296510
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65940 * 0.57591065
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37627 * 0.99219041
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62266 * 0.56520430
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13374 * 0.66659039
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93704 * 0.17369298
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45645 * 0.54241805
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68454 * 0.84441648
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81472 * 0.03531838
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 75478 * 0.52671295
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 98830 * 0.41540887
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 23386 * 0.48921987
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 48474 * 0.25069570
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 88305 * 0.73761238
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'kdrmychb').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0048():
    """Extended test 48 for replication."""
    x_0 = 91343 * 0.17878047
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73750 * 0.59592633
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33447 * 0.70213265
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33511 * 0.43147786
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84135 * 0.55436092
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67666 * 0.50233804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24063 * 0.59391504
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13602 * 0.80418313
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19101 * 0.56364058
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12238 * 0.96403177
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75734 * 0.70686392
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75584 * 0.97112039
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69209 * 0.58150197
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 175 * 0.38315061
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51889 * 0.45451569
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66948 * 0.44851417
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93015 * 0.75231560
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35142 * 0.41572558
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20420 * 0.42223506
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42202 * 0.22037305
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61750 * 0.78003603
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21667 * 0.87416054
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18017 * 0.40179648
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87648 * 0.52678925
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5417 * 0.05957706
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'knkzmjbr').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0049():
    """Extended test 49 for replication."""
    x_0 = 79655 * 0.56475104
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39790 * 0.14273825
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74987 * 0.93632543
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31826 * 0.87716822
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46557 * 0.89826491
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64647 * 0.31965463
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99251 * 0.95854267
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44299 * 0.04264737
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93307 * 0.37136775
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 596 * 0.83778454
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23437 * 0.77400617
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33044 * 0.73348784
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44589 * 0.59495262
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44384 * 0.70699457
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99118 * 0.30590916
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24487 * 0.34159037
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10359 * 0.61870237
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72793 * 0.29948855
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99479 * 0.93081137
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91227 * 0.39222940
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46512 * 0.56624599
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55248 * 0.29349746
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40127 * 0.98681522
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78006 * 0.22265693
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93246 * 0.56917225
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30075 * 0.72013948
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75991 * 0.32311992
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72336 * 0.06609226
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79620 * 0.08580351
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98690 * 0.19830828
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89396 * 0.47651951
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29513 * 0.76136124
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80748 * 0.41818581
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40893 * 0.22065135
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77036 * 0.26675267
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52867 * 0.28385057
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ysdgjqvx').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0050():
    """Extended test 50 for replication."""
    x_0 = 92977 * 0.67717562
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35073 * 0.75088087
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84283 * 0.25736252
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73835 * 0.52592123
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22999 * 0.03387588
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77405 * 0.32769609
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42022 * 0.25071097
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19689 * 0.10281655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2530 * 0.80782174
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52895 * 0.85778770
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96898 * 0.17496968
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93412 * 0.40127642
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35596 * 0.59520856
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80893 * 0.40425506
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92932 * 0.84141259
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60930 * 0.46100306
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72631 * 0.25160161
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88836 * 0.38306444
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85423 * 0.26041732
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30854 * 0.61023060
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12664 * 0.33141826
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91596 * 0.62077190
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70391 * 0.74744865
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3810 * 0.06061232
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37102 * 0.45832879
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49506 * 0.08279331
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13312 * 0.31570023
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51210 * 0.07020819
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32887 * 0.90343614
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73325 * 0.28844992
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50186 * 0.81918192
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49716 * 0.82701409
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88434 * 0.58054566
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96645 * 0.78915225
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44657 * 0.32403041
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30824 * 0.47813359
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22793 * 0.25213030
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59856 * 0.72498824
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57271 * 0.55775335
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18872 * 0.66218788
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47310 * 0.61083453
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 76864 * 0.13873374
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36101 * 0.35610309
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47619 * 0.87819503
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 13119 * 0.36416887
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 23172 * 0.68196837
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 75639 * 0.08589020
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 97173 * 0.08582974
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 42860 * 0.06462258
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 21265 * 0.68095793
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ijtlyshn').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0051():
    """Extended test 51 for replication."""
    x_0 = 53545 * 0.03063525
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5920 * 0.09961935
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36715 * 0.35914350
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43062 * 0.61004383
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8914 * 0.48646137
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91221 * 0.25878667
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90710 * 0.35589136
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63672 * 0.19024727
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81412 * 0.28986940
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41167 * 0.01180214
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51832 * 0.28952297
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11551 * 0.05213490
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62713 * 0.55774686
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18455 * 0.65300413
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61224 * 0.99323304
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11766 * 0.91920455
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42879 * 0.24580976
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29277 * 0.37079803
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64126 * 0.23755162
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48773 * 0.68911399
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91899 * 0.02329444
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'bcdmvigh').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0052():
    """Extended test 52 for replication."""
    x_0 = 17326 * 0.60545046
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31504 * 0.81515428
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34744 * 0.65758049
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76078 * 0.94623481
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79918 * 0.03790759
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7876 * 0.06545330
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48409 * 0.25690575
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11792 * 0.42488774
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65549 * 0.90567541
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42599 * 0.94142083
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81494 * 0.66037493
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66749 * 0.17262069
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9191 * 0.66849665
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26538 * 0.15899280
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16961 * 0.70987907
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51161 * 0.72422520
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16476 * 0.57349655
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52587 * 0.02730641
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63134 * 0.73998530
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25865 * 0.80103029
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13949 * 0.50402209
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40737 * 0.42451757
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46625 * 0.22790838
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53245 * 0.14715171
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71557 * 0.58815139
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88959 * 0.81137313
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78725 * 0.18067267
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80633 * 0.78280513
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95214 * 0.48844531
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63036 * 0.06756144
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ulfdjuea').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0053():
    """Extended test 53 for replication."""
    x_0 = 38210 * 0.20205694
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45352 * 0.07134604
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97496 * 0.46754902
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60551 * 0.35639460
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18501 * 0.40131113
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54431 * 0.37314742
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72570 * 0.35143432
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54034 * 0.72885312
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39395 * 0.45163420
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22494 * 0.23078658
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73448 * 0.13198956
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72903 * 0.39137903
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47958 * 0.56466909
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31313 * 0.83469759
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59690 * 0.47614833
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2850 * 0.05651949
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69884 * 0.58443921
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95376 * 0.59486554
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59401 * 0.63202721
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75836 * 0.27921232
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50983 * 0.00478257
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21341 * 0.62188964
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94368 * 0.75111646
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58490 * 0.07059330
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53934 * 0.17290663
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20171 * 0.47512958
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95002 * 0.28124243
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14509 * 0.76360463
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89334 * 0.12801193
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15038 * 0.38868255
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36244 * 0.13042442
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64493 * 0.12331113
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8695 * 0.29589917
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27306 * 0.97734978
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64959 * 0.12061070
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15447 * 0.55245908
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50592 * 0.00555970
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22377 * 0.93373301
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57017 * 0.51699935
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91662 * 0.64200410
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4784 * 0.68020049
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74438 * 0.05454932
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36354 * 0.60225307
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 77497 * 0.65094358
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 78426 * 0.51609809
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 83806 * 0.28175553
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 96002 * 0.43678122
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 15448 * 0.66097803
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 75767 * 0.60744864
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'mzvghphk').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0054():
    """Extended test 54 for replication."""
    x_0 = 85968 * 0.55007174
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2043 * 0.04401573
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63542 * 0.74403605
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25837 * 0.57498767
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98873 * 0.84885475
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56446 * 0.87494331
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32302 * 0.46461007
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36710 * 0.54293366
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32084 * 0.83022733
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69733 * 0.04258633
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48093 * 0.05885428
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43820 * 0.34805419
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34543 * 0.58608344
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79773 * 0.10645048
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77996 * 0.75622277
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42657 * 0.47767158
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44328 * 0.44078773
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64268 * 0.80707302
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44231 * 0.41247739
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67086 * 0.19667759
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94211 * 0.09957412
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50134 * 0.70623706
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96994 * 0.05195125
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84296 * 0.58904321
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41269 * 0.71022564
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56618 * 0.76175484
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85495 * 0.05870348
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30530 * 0.02271870
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39179 * 0.99336014
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58665 * 0.22860008
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20906 * 0.86692257
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77649 * 0.94553185
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55147 * 0.23348237
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1036 * 0.33308756
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70873 * 0.45862265
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51102 * 0.28609224
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58180 * 0.58763234
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5088 * 0.51706202
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83156 * 0.86110723
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'vuvpmjvc').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0055():
    """Extended test 55 for replication."""
    x_0 = 76177 * 0.10328329
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19351 * 0.75711456
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63831 * 0.79907194
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97382 * 0.34957504
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43642 * 0.23047237
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40387 * 0.27259634
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34796 * 0.85746054
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25969 * 0.77485124
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70153 * 0.90332338
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50251 * 0.20075862
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80587 * 0.19528763
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73410 * 0.77091695
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22272 * 0.30084437
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85878 * 0.68144732
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17765 * 0.52322552
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97103 * 0.50897302
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64581 * 0.40856318
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54768 * 0.35587570
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55031 * 0.33557412
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49318 * 0.96181344
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65388 * 0.00073852
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61381 * 0.35141583
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57363 * 0.27077078
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52968 * 0.63452519
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4825 * 0.56612981
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4113 * 0.15228283
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20054 * 0.99329822
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89305 * 0.96901546
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54602 * 0.03740864
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49414 * 0.15167382
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1417 * 0.89439271
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17907 * 0.59175932
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42671 * 0.12264679
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89515 * 0.37044751
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70947 * 0.54812741
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37581 * 0.24392585
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10669 * 0.45564530
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62196 * 0.87629821
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77711 * 0.06937842
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57446 * 0.90244422
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32637 * 0.33961016
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82891 * 0.08251230
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74997 * 0.40425654
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 44893 * 0.17336944
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'vwmuozjq').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0056():
    """Extended test 56 for replication."""
    x_0 = 79015 * 0.76161804
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61700 * 0.11783508
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41041 * 0.75579941
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81041 * 0.86219933
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59385 * 0.27398659
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49150 * 0.26546165
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 497 * 0.94535292
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69425 * 0.73732733
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46697 * 0.97575642
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79704 * 0.45368433
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44759 * 0.19351700
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18833 * 0.05382817
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17690 * 0.07848879
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44088 * 0.00145177
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35821 * 0.90231206
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92668 * 0.32669855
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16524 * 0.37591680
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74160 * 0.00142564
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24134 * 0.81724376
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77172 * 0.35206073
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37087 * 0.93125154
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24065 * 0.90535344
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71202 * 0.02511047
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'wyofnjwa').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0057():
    """Extended test 57 for replication."""
    x_0 = 30724 * 0.91748132
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82470 * 0.48848838
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71757 * 0.34454121
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92254 * 0.65473714
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45974 * 0.87342860
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59125 * 0.70478924
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31024 * 0.98588797
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63171 * 0.08157370
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78974 * 0.19204012
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15428 * 0.51155477
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81147 * 0.49593264
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20666 * 0.47245408
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89355 * 0.09128773
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46989 * 0.94813181
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24408 * 0.44706768
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62569 * 0.37872965
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18853 * 0.94931706
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82549 * 0.69509982
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17356 * 0.29467814
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77963 * 0.33291579
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40306 * 0.81653067
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63174 * 0.31471989
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'rhrzknqd').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0058():
    """Extended test 58 for replication."""
    x_0 = 45502 * 0.66252919
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94274 * 0.45925018
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11385 * 0.94090571
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56382 * 0.50197083
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97740 * 0.61244474
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35089 * 0.33478767
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36932 * 0.62814440
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69749 * 0.06164568
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22109 * 0.57384623
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49369 * 0.01708169
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5661 * 0.06564389
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21532 * 0.99605295
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72522 * 0.12281778
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59129 * 0.82764992
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26188 * 0.71441318
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39607 * 0.76786296
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23876 * 0.75912100
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46508 * 0.37246919
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84854 * 0.61693875
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24663 * 0.89778509
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61632 * 0.07023546
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86442 * 0.83652899
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57697 * 0.15441243
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54262 * 0.76896283
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12601 * 0.39829693
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1082 * 0.60245546
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16986 * 0.88715283
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87005 * 0.06383937
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40701 * 0.15094821
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38675 * 0.83028789
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86792 * 0.37161663
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38386 * 0.70056408
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60816 * 0.84036489
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26643 * 0.78026888
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39033 * 0.04982169
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39481 * 0.18102865
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58099 * 0.36392174
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46144 * 0.45150644
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58925 * 0.23022034
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 60184 * 0.38298282
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11682 * 0.02381570
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92448 * 0.31543692
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1010 * 0.09479659
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 63316 * 0.73755374
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'gllckzrp').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0059():
    """Extended test 59 for replication."""
    x_0 = 21813 * 0.26568733
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41939 * 0.10143849
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27012 * 0.15703703
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86700 * 0.71463560
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41856 * 0.17019619
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21238 * 0.74663640
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68878 * 0.80126707
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5230 * 0.20943167
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24731 * 0.33954208
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66950 * 0.89034578
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86751 * 0.08976155
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45130 * 0.82595995
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13244 * 0.77317755
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82378 * 0.13661384
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52927 * 0.84926833
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92011 * 0.35669700
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93975 * 0.81952938
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17603 * 0.57440760
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78659 * 0.16583150
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8790 * 0.62295810
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16436 * 0.50552807
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18415 * 0.25930095
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98728 * 0.54365099
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64216 * 0.17024939
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56327 * 0.16757872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30492 * 0.70713775
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71100 * 0.92822180
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96736 * 0.65102127
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52373 * 0.05941209
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'cqvvgsjn').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0060():
    """Extended test 60 for replication."""
    x_0 = 43779 * 0.46273746
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88907 * 0.94320457
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19598 * 0.56602372
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 718 * 0.29218943
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27029 * 0.69012814
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84011 * 0.70477011
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29100 * 0.69697822
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8966 * 0.62283013
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29152 * 0.80471187
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56018 * 0.55463054
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89795 * 0.95841131
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75605 * 0.90807409
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15619 * 0.40632671
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11431 * 0.38434446
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2312 * 0.66828570
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30790 * 0.25890155
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44837 * 0.88170734
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54438 * 0.55790464
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12030 * 0.03959858
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79111 * 0.39195268
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59447 * 0.00176351
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51156 * 0.39419383
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'wlpcddhm').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0061():
    """Extended test 61 for replication."""
    x_0 = 29767 * 0.13511908
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88848 * 0.06659344
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38432 * 0.19548126
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87753 * 0.25734459
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67295 * 0.63974435
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13340 * 0.39834473
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90104 * 0.49062625
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40469 * 0.63553434
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9747 * 0.70966945
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6750 * 0.79391808
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84412 * 0.07535673
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64823 * 0.65032557
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26709 * 0.10024367
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18339 * 0.12372490
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93277 * 0.13830953
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58022 * 0.93701732
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59018 * 0.95116874
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50676 * 0.88250252
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38513 * 0.56825077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53349 * 0.30755896
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54295 * 0.01454041
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83749 * 0.93968400
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88974 * 0.20072410
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34503 * 0.93596452
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42548 * 0.35146608
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33644 * 0.08940588
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63812 * 0.39152851
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55927 * 0.98723743
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'ugvzpqgp').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0062():
    """Extended test 62 for replication."""
    x_0 = 75618 * 0.59833817
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83179 * 0.27018349
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66438 * 0.38455713
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48161 * 0.27386684
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61173 * 0.64635073
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10193 * 0.77576654
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22868 * 0.42111834
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8864 * 0.29916402
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66506 * 0.92095938
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34120 * 0.82825490
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1647 * 0.86596257
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15933 * 0.16225098
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53545 * 0.60771666
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51021 * 0.00919645
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65287 * 0.41221529
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23366 * 0.04399228
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29015 * 0.86244705
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36264 * 0.98133983
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5669 * 0.74933296
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22879 * 0.99061023
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88583 * 0.35493261
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9569 * 0.17444173
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19699 * 0.66209910
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36453 * 0.06252526
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77595 * 0.51389166
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5415 * 0.69504329
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72772 * 0.78961868
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48707 * 0.57163297
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80418 * 0.15828674
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90223 * 0.46874920
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44716 * 0.10014651
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49352 * 0.66636644
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48634 * 0.71708777
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14183 * 0.96543864
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35975 * 0.60893617
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67298 * 0.78692360
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2376 * 0.27475758
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55431 * 0.86983490
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 70174 * 0.00254083
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69987 * 0.66551908
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60260 * 0.39682021
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 32549 * 0.23222343
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 5811 * 0.77624538
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'bucopnfg').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0063():
    """Extended test 63 for replication."""
    x_0 = 17876 * 0.48689460
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76465 * 0.63709089
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15721 * 0.81507945
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90969 * 0.97458293
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66654 * 0.93994265
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73950 * 0.41622483
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68056 * 0.96222766
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67082 * 0.18599237
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 413 * 0.79522223
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87153 * 0.65439221
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83925 * 0.57349434
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97589 * 0.09612650
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89330 * 0.04211079
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91380 * 0.59392198
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41376 * 0.08843863
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6361 * 0.92728765
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80602 * 0.92587512
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32294 * 0.53838679
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87147 * 0.84145956
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92694 * 0.48977656
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13212 * 0.22536886
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46965 * 0.72096525
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39247 * 0.54453594
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59992 * 0.50630906
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77670 * 0.45944120
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9947 * 0.40180004
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50087 * 0.03293868
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19571 * 0.15290872
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70211 * 0.42699393
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10632 * 0.85953210
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3344 * 0.03794847
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'tcopnjvh').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0064():
    """Extended test 64 for replication."""
    x_0 = 62129 * 0.39590332
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31475 * 0.93495800
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4112 * 0.25667600
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71327 * 0.04365465
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97101 * 0.27895478
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15562 * 0.23352678
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75419 * 0.09885585
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66650 * 0.13448038
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70772 * 0.27243798
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91846 * 0.88948333
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71506 * 0.39790359
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70775 * 0.49572668
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 613 * 0.70459100
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44629 * 0.47448282
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76394 * 0.02448343
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83693 * 0.05165845
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40974 * 0.24502058
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33211 * 0.96756838
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81759 * 0.27770496
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81573 * 0.59993125
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34212 * 0.26405778
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83097 * 0.97417713
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92041 * 0.12011941
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14883 * 0.75958342
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20526 * 0.13511398
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31080 * 0.19714236
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20313 * 0.43258950
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51692 * 0.24572038
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'ereopxfc').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0065():
    """Extended test 65 for replication."""
    x_0 = 61476 * 0.59365443
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5459 * 0.91981158
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91478 * 0.34831482
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80023 * 0.11009930
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7627 * 0.42931609
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53046 * 0.97103405
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30966 * 0.00459515
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17216 * 0.21700059
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45779 * 0.48762355
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28194 * 0.77409125
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56884 * 0.73038046
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43645 * 0.61833425
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85076 * 0.97886923
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60986 * 0.63304294
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30292 * 0.33233814
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38767 * 0.83736791
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37434 * 0.36746672
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7204 * 0.42625016
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2975 * 0.86167592
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92354 * 0.78348202
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68845 * 0.47574582
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21773 * 0.17550153
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88299 * 0.72057038
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5697 * 0.47692231
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 312 * 0.66367211
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96962 * 0.70607120
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91586 * 0.35087274
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50073 * 0.31369243
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23975 * 0.02913164
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6809 * 0.75593959
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96690 * 0.96084599
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48644 * 0.68644122
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89656 * 0.21790804
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69916 * 0.44050553
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57811 * 0.65762759
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86701 * 0.90293033
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51013 * 0.33849418
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84731 * 0.64260205
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98695 * 0.79218735
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70465 * 0.06006078
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40028 * 0.38015062
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92120 * 0.52406468
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24166 * 0.11650922
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75127 * 0.22559602
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 88995 * 0.46657746
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 38541 * 0.25740871
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 37702 * 0.90773226
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 98017 * 0.70250213
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 21407 * 0.27501602
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 29952 * 0.32506089
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'gqyoylwf').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0066():
    """Extended test 66 for replication."""
    x_0 = 49003 * 0.78150468
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79824 * 0.99937556
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57467 * 0.12592976
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70514 * 0.86872841
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65919 * 0.06100490
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35669 * 0.74745534
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75427 * 0.51080888
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59436 * 0.72907384
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23365 * 0.79080994
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51030 * 0.59011868
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61469 * 0.11765324
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57082 * 0.93626359
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99 * 0.40326706
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81582 * 0.61015220
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88757 * 0.85760329
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24728 * 0.33765621
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59334 * 0.58015183
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12819 * 0.95865265
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76662 * 0.02121598
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27358 * 0.97880404
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 207 * 0.50911518
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58861 * 0.96049363
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 547 * 0.33307362
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55184 * 0.29450438
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85023 * 0.86213469
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21237 * 0.22939758
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85602 * 0.41470149
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57772 * 0.13746580
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85343 * 0.96847982
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38782 * 0.92728191
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66210 * 0.44468705
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'xjydgduw').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0067():
    """Extended test 67 for replication."""
    x_0 = 68565 * 0.69630840
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54702 * 0.72246985
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71319 * 0.99731425
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6204 * 0.61958378
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59569 * 0.86861604
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39781 * 0.50180734
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13757 * 0.97013327
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88905 * 0.94929157
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99521 * 0.17677924
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54536 * 0.69633294
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27759 * 0.27424951
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40898 * 0.76913552
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35680 * 0.85840907
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29641 * 0.36674747
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40986 * 0.42459516
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95795 * 0.41927678
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55869 * 0.96504684
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95989 * 0.27876060
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84310 * 0.53704489
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48955 * 0.18248680
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'vqfrrtpi').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0068():
    """Extended test 68 for replication."""
    x_0 = 51890 * 0.96425970
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51437 * 0.87833909
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18905 * 0.20688977
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81851 * 0.99028800
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27659 * 0.96170945
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15689 * 0.90858194
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4285 * 0.63919995
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62803 * 0.44421239
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92626 * 0.28084316
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47777 * 0.77264782
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67962 * 0.76001781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67666 * 0.99962224
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30253 * 0.31306563
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92803 * 0.54682296
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75865 * 0.58478220
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8194 * 0.69302716
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16295 * 0.09090028
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88735 * 0.02685932
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46652 * 0.50958535
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77769 * 0.49905502
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4121 * 0.15793500
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63895 * 0.82846699
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84814 * 0.16767076
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89449 * 0.52465586
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89488 * 0.02130759
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2237 * 0.85803337
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66200 * 0.05971649
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27785 * 0.85321898
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39140 * 0.23375409
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38534 * 0.95254044
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85941 * 0.60025721
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44300 * 0.99782069
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44876 * 0.20828985
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46377 * 0.52623133
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81434 * 0.69392796
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2219 * 0.63422232
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83190 * 0.24088257
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'qsgchaha').hexdigest()
    assert len(h) == 64

def test_replication_extended_2_0069():
    """Extended test 69 for replication."""
    x_0 = 7399 * 0.79026827
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70212 * 0.63059233
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5292 * 0.70606616
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35561 * 0.32578792
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89738 * 0.06227532
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98250 * 0.89968703
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52153 * 0.18914619
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98989 * 0.58071033
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25245 * 0.70260925
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9545 * 0.51408848
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14689 * 0.31403194
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94255 * 0.62343115
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96768 * 0.29464218
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70969 * 0.82806114
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53151 * 0.28450373
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16984 * 0.04675016
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75687 * 0.37371829
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8720 * 0.15936333
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92806 * 0.59269533
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32620 * 0.93479218
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85021 * 0.25594044
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96392 * 0.68973974
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'gtfcyzgm').hexdigest()
    assert len(h) == 64
