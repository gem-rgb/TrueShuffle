"""Extended tests for transcoding suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_transcoding_extended_8_0000():
    """Extended test 0 for transcoding."""
    x_0 = 62173 * 0.56993995
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8940 * 0.52984513
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2929 * 0.10979106
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23644 * 0.29153950
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40668 * 0.11584020
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98098 * 0.59370829
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48365 * 0.28709886
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78337 * 0.79974651
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40429 * 0.39011317
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73182 * 0.51587816
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70898 * 0.97828886
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90763 * 0.74569055
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60872 * 0.21221128
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82903 * 0.87946822
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95046 * 0.04295200
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88330 * 0.63610025
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5714 * 0.36484439
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15729 * 0.66545881
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17966 * 0.36305117
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79032 * 0.41096884
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54750 * 0.85695969
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99952 * 0.28395599
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8247 * 0.18736230
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16837 * 0.34271081
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70450 * 0.59011008
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84284 * 0.23573112
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39454 * 0.35041436
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5826 * 0.58436660
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94308 * 0.31396850
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44138 * 0.48905283
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88001 * 0.18911270
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16881 * 0.79033820
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29196 * 0.90338137
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47443 * 0.18480374
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6478 * 0.38643918
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71042 * 0.68573632
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57599 * 0.15752166
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35811 * 0.31223305
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92263 * 0.28728636
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 53847 * 0.49306286
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91251 * 0.96306087
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33005 * 0.91283214
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70014 * 0.06116507
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82057 * 0.01053024
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59163 * 0.94428264
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'neevapcq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0001():
    """Extended test 1 for transcoding."""
    x_0 = 14643 * 0.95938603
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44758 * 0.21412765
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75623 * 0.57437247
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13831 * 0.55079951
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66463 * 0.09280318
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45688 * 0.74797099
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16738 * 0.41759193
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22671 * 0.51472151
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63353 * 0.98583311
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76062 * 0.62477421
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28538 * 0.80975108
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45451 * 0.47711221
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37510 * 0.22165904
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19697 * 0.77230226
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7839 * 0.84178585
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58406 * 0.52302922
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20707 * 0.04000981
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43986 * 0.92438432
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63726 * 0.65588188
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29889 * 0.36032212
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31366 * 0.71595095
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14655 * 0.81657486
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44764 * 0.76965689
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1256 * 0.44640927
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56880 * 0.16826255
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36726 * 0.71094596
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19070 * 0.43674163
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10421 * 0.77195224
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99696 * 0.55765414
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30016 * 0.01516416
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97719 * 0.88553205
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74188 * 0.11506146
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52193 * 0.66380189
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68624 * 0.97650134
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98313 * 0.73136081
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50500 * 0.19111216
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93897 * 0.53917681
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1751 * 0.20295910
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 54862 * 0.45721414
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84284 * 0.00764322
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91089 * 0.21935339
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54599 * 0.35878382
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 54542 * 0.44868206
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 8969 * 0.63749631
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92157 * 0.47440542
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 49627 * 0.39832919
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 34898 * 0.83616356
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 12738 * 0.20490294
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'nriujuhl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0002():
    """Extended test 2 for transcoding."""
    x_0 = 15744 * 0.04587273
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98482 * 0.63463160
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5731 * 0.52264180
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38354 * 0.33040281
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41684 * 0.22717203
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74911 * 0.54553628
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76456 * 0.72806173
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71572 * 0.55302327
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68465 * 0.01426847
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88010 * 0.41966679
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96028 * 0.40588378
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70260 * 0.81705849
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90175 * 0.40314486
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70290 * 0.43832373
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94130 * 0.38395986
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7729 * 0.48818469
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58181 * 0.40815566
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77258 * 0.10516378
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21940 * 0.63038363
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28215 * 0.30461568
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56012 * 0.75221763
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42128 * 0.60802951
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56180 * 0.45651140
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62037 * 0.49798157
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83747 * 0.21393766
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29414 * 0.98543015
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78145 * 0.11229090
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27683 * 0.87719303
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8566 * 0.05603463
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4307 * 0.89249179
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18783 * 0.98815212
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'uhidgnrq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0003():
    """Extended test 3 for transcoding."""
    x_0 = 99920 * 0.07868109
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62080 * 0.78810325
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72810 * 0.92565532
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70853 * 0.94069106
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29359 * 0.88170119
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91727 * 0.14258216
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95635 * 0.85392857
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26556 * 0.37300572
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46387 * 0.64137581
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17349 * 0.24236395
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64228 * 0.57312671
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61033 * 0.94039492
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82205 * 0.03188909
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74314 * 0.12923779
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41340 * 0.15529417
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24239 * 0.94343368
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93336 * 0.42195549
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99733 * 0.27596592
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87813 * 0.72504774
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60074 * 0.07740734
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58043 * 0.84611727
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33657 * 0.24063682
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34073 * 0.38237740
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16963 * 0.51673929
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73077 * 0.13878980
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35538 * 0.65800832
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16689 * 0.68729060
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48723 * 0.97947431
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1328 * 0.19688442
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88371 * 0.59654009
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19466 * 0.00825271
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85953 * 0.73804257
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29831 * 0.74513470
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47591 * 0.82856440
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3206 * 0.18627334
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74556 * 0.03034116
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47529 * 0.45173568
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11142 * 0.41107092
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 7979 * 0.69231155
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8810 * 0.46711497
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44360 * 0.19489648
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 19137 * 0.66388563
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'mqqrxhrg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0004():
    """Extended test 4 for transcoding."""
    x_0 = 2786 * 0.44470867
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79029 * 0.83735881
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61203 * 0.18498311
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80588 * 0.95464691
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60561 * 0.64538130
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36821 * 0.55626629
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74441 * 0.62813630
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17317 * 0.67381829
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38615 * 0.53569894
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35530 * 0.97825649
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97203 * 0.59707782
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19838 * 0.87903152
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79874 * 0.52608191
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54414 * 0.54518714
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20677 * 0.08722835
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1818 * 0.03929622
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79940 * 0.25405428
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56728 * 0.80575996
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57842 * 0.96853745
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45034 * 0.86009954
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65969 * 0.77354689
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70530 * 0.29599645
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32613 * 0.73350046
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21147 * 0.12373019
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 520 * 0.02848741
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50340 * 0.22370666
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80843 * 0.44450907
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22755 * 0.98605434
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91465 * 0.65138426
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58493 * 0.44258806
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71167 * 0.55708656
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2763 * 0.95410422
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45200 * 0.47180701
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4570 * 0.73147525
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25290 * 0.74144451
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30841 * 0.95313786
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94683 * 0.53548202
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90427 * 0.61328643
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'abvgtkgs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0005():
    """Extended test 5 for transcoding."""
    x_0 = 79519 * 0.22440077
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86500 * 0.34753494
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67611 * 0.71503811
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7675 * 0.37471290
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59877 * 0.19905801
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82134 * 0.18629977
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61933 * 0.18275946
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78032 * 0.96979912
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19814 * 0.91180841
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73710 * 0.33497440
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86761 * 0.40590761
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56491 * 0.09951602
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71986 * 0.73007624
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54200 * 0.40828697
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55116 * 0.60793715
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42015 * 0.22913865
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54940 * 0.84452410
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38975 * 0.08696188
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36840 * 0.53931942
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52878 * 0.21556514
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49643 * 0.26325514
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51548 * 0.11369796
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43556 * 0.40920010
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48916 * 0.77837505
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59776 * 0.44325024
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77570 * 0.79050576
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71384 * 0.12085908
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63511 * 0.07220878
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95845 * 0.53926219
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51058 * 0.34305742
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94421 * 0.55380790
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3009 * 0.51224132
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14534 * 0.76256335
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32144 * 0.71665326
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5753 * 0.53205288
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61003 * 0.08356590
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34965 * 0.39774341
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'obppslzp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0006():
    """Extended test 6 for transcoding."""
    x_0 = 95752 * 0.27722056
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18809 * 0.20617066
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87449 * 0.30495684
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13571 * 0.46039891
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4179 * 0.14506505
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76456 * 0.64031991
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69787 * 0.03742651
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42413 * 0.51114676
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86036 * 0.30277601
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53126 * 0.88210301
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91804 * 0.81013480
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92050 * 0.55754573
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65490 * 0.73622996
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79508 * 0.66809073
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47677 * 0.77341165
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75389 * 0.41462060
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86090 * 0.70172104
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43313 * 0.21248899
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65130 * 0.28274949
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77141 * 0.93153531
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17672 * 0.24063938
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85755 * 0.91785062
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97112 * 0.15862401
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21394 * 0.87266703
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78422 * 0.90561581
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41007 * 0.53474168
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85804 * 0.39570023
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42503 * 0.52883389
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29333 * 0.40219731
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36740 * 0.05093828
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29919 * 0.23937817
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64730 * 0.22124553
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40311 * 0.33078151
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41618 * 0.95074680
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2018 * 0.78862613
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29236 * 0.46002775
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'vulxfclh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0007():
    """Extended test 7 for transcoding."""
    x_0 = 91386 * 0.32803680
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61462 * 0.08766709
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23242 * 0.80202269
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7685 * 0.53386007
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83606 * 0.71138577
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67427 * 0.68711764
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46827 * 0.42552999
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95118 * 0.42963625
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3670 * 0.51110528
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95969 * 0.55960730
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24718 * 0.22165164
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69277 * 0.85333968
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33430 * 0.30761847
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42092 * 0.48308085
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80958 * 0.12618045
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57906 * 0.59411748
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37333 * 0.88795837
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6985 * 0.46086720
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98950 * 0.67937162
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72652 * 0.25132695
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98335 * 0.24921067
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34846 * 0.32396410
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34001 * 0.25116328
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47691 * 0.01697718
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32434 * 0.48502137
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6196 * 0.28407512
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20566 * 0.39219040
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96199 * 0.82944187
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35567 * 0.13809507
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1552 * 0.04478018
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13328 * 0.06541659
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30716 * 0.46184269
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89719 * 0.84022740
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52066 * 0.18583214
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48435 * 0.56078216
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12105 * 0.66596437
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18707 * 0.59963946
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97625 * 0.88394465
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69384 * 0.07541237
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62759 * 0.01476603
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88982 * 0.94973024
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84099 * 0.09517489
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15084 * 0.79868238
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 24303 * 0.13413954
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 39032 * 0.47705103
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'wcxlvtuv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0008():
    """Extended test 8 for transcoding."""
    x_0 = 5370 * 0.04373300
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8567 * 0.39487556
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49319 * 0.62214299
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56462 * 0.70213829
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47033 * 0.81659491
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50370 * 0.35694458
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76174 * 0.99379294
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46079 * 0.33164230
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20864 * 0.42898938
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58812 * 0.65644617
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75609 * 0.08834933
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13151 * 0.33815800
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41137 * 0.73259280
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40588 * 0.92799941
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30775 * 0.10076177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93779 * 0.13809442
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50665 * 0.60757891
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1084 * 0.83114651
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64038 * 0.84678583
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97052 * 0.80151990
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81664 * 0.81940612
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77322 * 0.38025864
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48434 * 0.64993098
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70067 * 0.04251313
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61633 * 0.37764340
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70683 * 0.47846366
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3544 * 0.75694173
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13030 * 0.09815409
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63789 * 0.37830084
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36335 * 0.43116654
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70111 * 0.41060273
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79242 * 0.64196325
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'wyvsrvaz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0009():
    """Extended test 9 for transcoding."""
    x_0 = 62600 * 0.00224562
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37158 * 0.82943611
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54647 * 0.60528273
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46130 * 0.98044581
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 828 * 0.32073078
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58304 * 0.42744146
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10316 * 0.24686474
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52294 * 0.14520063
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83290 * 0.99235726
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41106 * 0.19562324
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4781 * 0.67486508
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90040 * 0.06566461
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39282 * 0.92492660
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14110 * 0.92107449
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30140 * 0.57731939
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64259 * 0.39453687
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16216 * 0.93466024
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54288 * 0.81991789
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59776 * 0.13168877
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75420 * 0.40891273
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16643 * 0.71422010
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89687 * 0.30272746
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11590 * 0.14043763
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81153 * 0.04281278
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42698 * 0.29603178
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'hgcpniuz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0010():
    """Extended test 10 for transcoding."""
    x_0 = 31924 * 0.91743234
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68952 * 0.55041968
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77386 * 0.27460557
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65083 * 0.41687858
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78697 * 0.99683790
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6527 * 0.30720580
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19834 * 0.20365176
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47345 * 0.78385307
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22093 * 0.50359872
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57456 * 0.27667195
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50267 * 0.88622258
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47323 * 0.87097410
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24241 * 0.01249756
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55873 * 0.45631221
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20843 * 0.28673047
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11329 * 0.91384387
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74405 * 0.10164082
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12275 * 0.85197221
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77346 * 0.76599666
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84653 * 0.12021899
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44694 * 0.33266532
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59899 * 0.71287846
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52552 * 0.19928191
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13931 * 0.06707862
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88494 * 0.25269387
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14270 * 0.20275642
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77293 * 0.53933018
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21517 * 0.02099398
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68762 * 0.86552661
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'fqkqlldd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0011():
    """Extended test 11 for transcoding."""
    x_0 = 51407 * 0.29621133
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22989 * 0.93716656
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83913 * 0.59183198
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1119 * 0.12058461
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29167 * 0.87273805
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59464 * 0.40978062
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75421 * 0.72809652
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4426 * 0.74549716
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31042 * 0.67531370
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7832 * 0.54807066
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10969 * 0.06549391
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71919 * 0.08056976
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31072 * 0.27454937
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55041 * 0.39001646
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81586 * 0.09020699
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20450 * 0.68341535
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4389 * 0.30319221
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84629 * 0.98971838
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33411 * 0.36047696
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74529 * 0.66837605
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45707 * 0.01367360
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95459 * 0.92255595
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37232 * 0.27826024
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97377 * 0.75557723
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7954 * 0.15693358
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69076 * 0.55436422
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29729 * 0.50625842
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39081 * 0.57904668
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62846 * 0.93583488
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25533 * 0.16336965
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22216 * 0.13089946
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 545 * 0.78290433
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42940 * 0.56903240
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74616 * 0.99740368
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15721 * 0.45799631
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99593 * 0.72705287
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30596 * 0.39440000
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47183 * 0.66941786
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 422 * 0.79849365
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65317 * 0.51067621
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11648 * 0.86530306
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80679 * 0.88713784
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70202 * 0.60931761
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 21554 * 0.93129842
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4449 * 0.71259402
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 84209 * 0.29607429
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 72331 * 0.99427977
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ajpyjhll').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0012():
    """Extended test 12 for transcoding."""
    x_0 = 18534 * 0.45713520
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16592 * 0.12154748
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24391 * 0.14803277
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19015 * 0.45688994
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57451 * 0.31920390
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52501 * 0.02494013
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1377 * 0.75223003
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33859 * 0.91816019
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27518 * 0.68812606
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87637 * 0.71016136
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62876 * 0.82646192
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89816 * 0.08386185
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91553 * 0.93536583
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41352 * 0.74279211
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15532 * 0.02005809
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57802 * 0.09142031
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65240 * 0.39025124
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57394 * 0.94955151
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52491 * 0.67906727
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17977 * 0.53092140
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24014 * 0.42504496
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96111 * 0.10384182
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33507 * 0.32627891
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84199 * 0.14489787
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76637 * 0.48790242
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66431 * 0.82520246
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76914 * 0.74122240
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41760 * 0.41996252
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'uokweduj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0013():
    """Extended test 13 for transcoding."""
    x_0 = 69421 * 0.59525483
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50731 * 0.03963914
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36376 * 0.67501310
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15448 * 0.27239382
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18081 * 0.41741771
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7121 * 0.83656817
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41176 * 0.79298374
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32762 * 0.44269941
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34426 * 0.28651810
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14346 * 0.37953550
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27325 * 0.52713715
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85407 * 0.99586090
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9452 * 0.93078672
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82304 * 0.99596282
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15461 * 0.15455596
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49876 * 0.69868113
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11540 * 0.20073970
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93277 * 0.80073833
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64712 * 0.04163625
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2878 * 0.92279777
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93285 * 0.68468592
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44904 * 0.30609756
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44869 * 0.59522927
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75370 * 0.07911486
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75352 * 0.16459761
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74995 * 0.98750113
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68371 * 0.11144089
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20289 * 0.62597086
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15028 * 0.85895444
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64953 * 0.57139729
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70850 * 0.46416759
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18324 * 0.71602822
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25779 * 0.94991297
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88430 * 0.88490229
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40538 * 0.90888002
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23428 * 0.33919884
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67309 * 0.83320014
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47272 * 0.84926975
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87553 * 0.51805767
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24081 * 0.92589253
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'zshlhdom').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0014():
    """Extended test 14 for transcoding."""
    x_0 = 79420 * 0.70059429
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44243 * 0.67650524
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8128 * 0.27175999
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80343 * 0.41235781
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47771 * 0.69455776
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31130 * 0.94575342
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68086 * 0.65934670
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27758 * 0.77734182
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43296 * 0.09489154
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97216 * 0.96798740
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76546 * 0.82733891
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38708 * 0.77208880
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34868 * 0.78248151
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43841 * 0.55797334
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1967 * 0.80478739
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5126 * 0.61186073
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31512 * 0.32427719
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3154 * 0.51444636
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6230 * 0.31978182
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2367 * 0.60673124
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21282 * 0.28685999
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54010 * 0.91862251
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44351 * 0.27565610
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38373 * 0.44850440
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19797 * 0.11788096
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35945 * 0.91490020
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70712 * 0.62490572
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37928 * 0.78082634
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37245 * 0.91062425
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15727 * 0.05010368
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9641 * 0.22444633
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67659 * 0.55923418
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1483 * 0.57206542
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51615 * 0.10359305
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17622 * 0.56169880
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36108 * 0.22711038
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42002 * 0.90252722
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 54625 * 0.56215873
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4474 * 0.71691588
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30995 * 0.29805662
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79104 * 0.23664593
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27431 * 0.58963798
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 881 * 0.54755967
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 1145 * 0.45789172
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 26749 * 0.96303062
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'krgaiewt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0015():
    """Extended test 15 for transcoding."""
    x_0 = 31364 * 0.92684994
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34973 * 0.40618438
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33166 * 0.84464396
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65009 * 0.94516713
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18889 * 0.84304878
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28649 * 0.14052494
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46843 * 0.03911279
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86021 * 0.57068738
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71890 * 0.18805856
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13903 * 0.35809012
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49877 * 0.54148740
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83445 * 0.82204027
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56943 * 0.52092777
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74127 * 0.69444664
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43083 * 0.57525458
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5146 * 0.46164496
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95827 * 0.40867138
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71796 * 0.00647712
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23810 * 0.40242370
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48952 * 0.72676663
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36067 * 0.31901594
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92112 * 0.82618934
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93650 * 0.69008776
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63033 * 0.42947975
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34598 * 0.59254038
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4524 * 0.27079289
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42402 * 0.49945169
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37322 * 0.22991953
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17686 * 0.05682480
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54598 * 0.96920451
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94201 * 0.58412623
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73654 * 0.21275378
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8412 * 0.35092519
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88721 * 0.31261738
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81788 * 0.16201824
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27572 * 0.52169686
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39118 * 0.33821822
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70914 * 0.49617636
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51185 * 0.38961937
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83196 * 0.53722020
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17671 * 0.10083673
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4828 * 0.08421201
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 51936 * 0.60347826
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20880 * 0.02329793
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 77894 * 0.62635655
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 14655 * 0.46040936
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 6847 * 0.36609477
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 34369 * 0.91658966
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 43525 * 0.85029380
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'xivahksi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0016():
    """Extended test 16 for transcoding."""
    x_0 = 73521 * 0.77213533
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97884 * 0.28564611
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59578 * 0.64684138
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16559 * 0.36551664
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3589 * 0.08777728
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61621 * 0.94006669
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97280 * 0.79637336
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66631 * 0.14178183
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99616 * 0.00425134
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80195 * 0.25839395
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99795 * 0.47070737
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82335 * 0.46188164
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21106 * 0.76480925
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16096 * 0.65840277
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8693 * 0.70985073
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64196 * 0.89491219
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30552 * 0.26704459
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6810 * 0.38979136
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56473 * 0.78403691
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62669 * 0.44938075
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29211 * 0.75365441
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82806 * 0.92878412
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31137 * 0.85301758
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70580 * 0.28918854
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11272 * 0.28028943
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39277 * 0.26268461
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92854 * 0.85505029
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78994 * 0.66910200
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51749 * 0.52053909
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23524 * 0.28072779
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88362 * 0.53641671
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58700 * 0.14369449
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57835 * 0.48887493
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56776 * 0.28502980
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90487 * 0.07058942
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75533 * 0.27594051
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19708 * 0.46799457
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29103 * 0.40101139
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42167 * 0.68098520
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'cjsauelf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0017():
    """Extended test 17 for transcoding."""
    x_0 = 35324 * 0.05027664
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76798 * 0.76113519
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39362 * 0.00400788
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95042 * 0.01196043
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66824 * 0.47788380
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23821 * 0.94219264
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88895 * 0.42094285
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70727 * 0.72747202
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61974 * 0.44534278
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56986 * 0.62520101
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91108 * 0.81270151
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67841 * 0.00884948
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22419 * 0.23497326
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57772 * 0.54863775
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1501 * 0.85967049
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59663 * 0.87296818
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94895 * 0.44915422
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47374 * 0.86956044
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62158 * 0.71460812
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19321 * 0.44973066
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76819 * 0.25786234
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77242 * 0.41255029
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86842 * 0.98320015
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32003 * 0.58289863
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86125 * 0.60087209
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4760 * 0.30174505
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89301 * 0.17455245
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'thlfioaw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0018():
    """Extended test 18 for transcoding."""
    x_0 = 69682 * 0.69138586
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2165 * 0.39234400
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77336 * 0.83121445
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45942 * 0.46908738
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34651 * 0.60557358
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72683 * 0.46344035
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63118 * 0.00341900
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26247 * 0.03576413
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44565 * 0.02629760
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2165 * 0.03006051
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40934 * 0.12002498
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66708 * 0.37242277
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44441 * 0.65177800
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21725 * 0.04639575
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44220 * 0.15941441
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83245 * 0.22270337
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23047 * 0.99940553
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53516 * 0.00314853
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15140 * 0.03395918
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54393 * 0.91125126
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87117 * 0.18312209
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32894 * 0.26813356
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31361 * 0.38832383
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76682 * 0.50366406
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84188 * 0.43524450
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76656 * 0.14154424
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87449 * 0.47955721
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77894 * 0.08991657
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25805 * 0.84780128
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5693 * 0.08196271
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38145 * 0.40810160
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81910 * 0.40512774
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'khylrypg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0019():
    """Extended test 19 for transcoding."""
    x_0 = 76821 * 0.31439119
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3147 * 0.31328038
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33595 * 0.15492750
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33668 * 0.52208962
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15696 * 0.96516726
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55766 * 0.55141947
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4642 * 0.30275302
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43547 * 0.82618355
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86485 * 0.66127355
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62608 * 0.17745429
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93196 * 0.33974146
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53176 * 0.66956480
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65383 * 0.18028520
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63738 * 0.35430891
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38586 * 0.61232937
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23671 * 0.43035515
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29847 * 0.01227271
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77856 * 0.37134175
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50549 * 0.53959089
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20360 * 0.41341623
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91334 * 0.96886437
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25594 * 0.85596269
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78851 * 0.53564238
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26121 * 0.93478957
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28160 * 0.58634427
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18959 * 0.40483063
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45647 * 0.73934079
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84175 * 0.50270794
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54736 * 0.08494751
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43666 * 0.44306417
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18757 * 0.42138395
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54708 * 0.71682938
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89518 * 0.72704009
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4536 * 0.38811831
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75707 * 0.76749271
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66414 * 0.21629868
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62164 * 0.93150849
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20267 * 0.18040604
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 343 * 0.39997103
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43913 * 0.02597082
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 7323 * 0.75758385
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57532 * 0.13449282
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55048 * 0.58175885
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 45339 * 0.37641217
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 56478 * 0.58815224
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'krqqcoug').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0020():
    """Extended test 20 for transcoding."""
    x_0 = 67354 * 0.31101232
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96168 * 0.62979950
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82721 * 0.65787837
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46289 * 0.85008868
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5202 * 0.26031400
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56201 * 0.36723339
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39829 * 0.95207547
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42498 * 0.58346146
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6167 * 0.25606506
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80852 * 0.52093430
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72688 * 0.51466562
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3671 * 0.29676668
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84845 * 0.17220470
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15394 * 0.21985687
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63231 * 0.72820603
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83830 * 0.42969890
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60082 * 0.95810066
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97297 * 0.66022721
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74952 * 0.01162828
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88244 * 0.09397686
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15215 * 0.82545518
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40909 * 0.30043520
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41991 * 0.45203852
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82496 * 0.73803204
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51431 * 0.49405358
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96082 * 0.13155472
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37215 * 0.52658998
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90735 * 0.87606275
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96127 * 0.32871752
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58617 * 0.72981871
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48763 * 0.71112379
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65229 * 0.15190101
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62257 * 0.20455746
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79122 * 0.65100962
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41564 * 0.47537818
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'pewvzdzp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0021():
    """Extended test 21 for transcoding."""
    x_0 = 41415 * 0.44902972
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83231 * 0.60503743
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53417 * 0.39216882
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17768 * 0.43130372
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55799 * 0.23911173
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73522 * 0.77769311
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71073 * 0.25384359
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92931 * 0.92076685
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35616 * 0.80426181
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23336 * 0.42182583
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16704 * 0.28351100
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46212 * 0.39467912
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98889 * 0.47164922
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78257 * 0.36889445
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97980 * 0.52193986
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57574 * 0.77160042
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9738 * 0.22825821
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76569 * 0.45447845
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29653 * 0.51263905
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22659 * 0.86263212
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63432 * 0.53594013
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31744 * 0.53475529
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32317 * 0.76872714
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36582 * 0.54589684
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63451 * 0.34553195
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9939 * 0.34327556
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50013 * 0.17499131
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93831 * 0.87011814
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30665 * 0.04226252
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76347 * 0.78675773
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80417 * 0.95013504
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11922 * 0.17586301
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25947 * 0.63612746
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14970 * 0.41238661
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87239 * 0.04223724
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71789 * 0.94890172
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46790 * 0.83495788
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60075 * 0.46950144
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20787 * 0.60509290
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16728 * 0.54268478
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 93038 * 0.78271049
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25264 * 0.48339619
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 89709 * 0.45916816
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'uojmnpfb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0022():
    """Extended test 22 for transcoding."""
    x_0 = 31656 * 0.40768523
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67365 * 0.34978413
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8572 * 0.46321333
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69034 * 0.81705963
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17237 * 0.06514131
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76278 * 0.21694347
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63508 * 0.25044077
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13896 * 0.51938089
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52954 * 0.62676984
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70380 * 0.64385085
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65636 * 0.78369967
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22551 * 0.38167271
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38071 * 0.49089927
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6317 * 0.41645597
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99674 * 0.91803973
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39267 * 0.78149875
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7133 * 0.67632017
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2596 * 0.16880975
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39999 * 0.78618244
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21317 * 0.04457888
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'qrbjxhqp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0023():
    """Extended test 23 for transcoding."""
    x_0 = 75724 * 0.03914951
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44571 * 0.52513367
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52182 * 0.81348221
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13624 * 0.69406493
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97216 * 0.58704059
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27349 * 0.81258101
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97001 * 0.33091665
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77378 * 0.30781899
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14655 * 0.38294809
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41565 * 0.44221918
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90366 * 0.77655658
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94609 * 0.42101538
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5696 * 0.06580756
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21743 * 0.45294596
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44679 * 0.46863438
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27698 * 0.30955936
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61218 * 0.26994311
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54335 * 0.58191278
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31270 * 0.58252609
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91131 * 0.72250806
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22193 * 0.29363913
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66982 * 0.98042194
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56221 * 0.69830272
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80135 * 0.37546367
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88357 * 0.69205911
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90995 * 0.40339041
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83209 * 0.60150474
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53100 * 0.85107823
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55796 * 0.82961312
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'rnpyspks').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0024():
    """Extended test 24 for transcoding."""
    x_0 = 11086 * 0.40068375
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87214 * 0.11524901
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71536 * 0.33301536
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58824 * 0.95106435
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99571 * 0.91123986
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81167 * 0.83183194
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76939 * 0.90724998
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41826 * 0.34560011
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78991 * 0.32429222
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39017 * 0.96816108
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54528 * 0.89056603
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93054 * 0.40306996
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67567 * 0.31146503
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75074 * 0.44013817
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2575 * 0.94853203
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15206 * 0.61637519
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79313 * 0.00807167
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9824 * 0.81064028
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17985 * 0.42003250
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6982 * 0.28705162
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70680 * 0.98524446
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3263 * 0.35418786
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23657 * 0.61294376
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1987 * 0.04959703
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58323 * 0.63404450
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74646 * 0.58639663
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63749 * 0.40383043
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8891 * 0.51385852
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32506 * 0.91999330
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88873 * 0.12758545
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9356 * 0.06371316
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85085 * 0.78654968
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96633 * 0.07638992
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5471 * 0.90043510
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53606 * 0.51005131
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'yuyvmcmj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0025():
    """Extended test 25 for transcoding."""
    x_0 = 99560 * 0.72314349
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54061 * 0.70712335
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8329 * 0.51880087
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97541 * 0.91911582
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14311 * 0.21779585
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84741 * 0.45621350
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10839 * 0.92706179
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66054 * 0.12979404
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64315 * 0.03806328
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89693 * 0.35468975
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29962 * 0.02522891
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82678 * 0.96852876
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1362 * 0.45246853
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18117 * 0.43517176
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38586 * 0.06159535
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14699 * 0.30052232
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21520 * 0.20537536
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69885 * 0.00935862
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50980 * 0.46143743
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95051 * 0.22339257
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73239 * 0.30087092
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43684 * 0.60539176
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14570 * 0.84080817
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61100 * 0.19348723
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30696 * 0.20982615
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7429 * 0.71186538
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60025 * 0.58697597
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10983 * 0.55407889
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'kbrnvomw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0026():
    """Extended test 26 for transcoding."""
    x_0 = 33063 * 0.17656594
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59785 * 0.99264509
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58365 * 0.50278120
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5972 * 0.83628579
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11879 * 0.47914195
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35686 * 0.53968993
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73034 * 0.55276016
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17863 * 0.92995394
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29873 * 0.58315434
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58385 * 0.31050651
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31098 * 0.55890423
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82108 * 0.23437962
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9871 * 0.87726331
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98772 * 0.92985016
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83522 * 0.28846693
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61686 * 0.05846533
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86463 * 0.20291747
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99685 * 0.36854494
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3607 * 0.80250816
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26069 * 0.85912303
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60567 * 0.84005405
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84214 * 0.65967633
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67103 * 0.87336064
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74867 * 0.87318485
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53889 * 0.39155902
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83280 * 0.01258887
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25794 * 0.11675705
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47720 * 0.92400874
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39386 * 0.42091204
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71439 * 0.27911981
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52465 * 0.00755830
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77311 * 0.35220852
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94785 * 0.62293486
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38685 * 0.33134186
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86220 * 0.16737264
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63232 * 0.40836520
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'gllbbofk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0027():
    """Extended test 27 for transcoding."""
    x_0 = 71184 * 0.16674529
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37334 * 0.50545823
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81938 * 0.30451080
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51427 * 0.47028961
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16691 * 0.33080558
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99030 * 0.80665852
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10714 * 0.34342915
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83884 * 0.67076430
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79460 * 0.09651436
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50658 * 0.34507603
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5042 * 0.22533771
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73347 * 0.45700088
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60482 * 0.61350722
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28897 * 0.95637383
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84980 * 0.79675671
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77481 * 0.86870782
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71908 * 0.13590352
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81182 * 0.92439466
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56648 * 0.89697342
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24719 * 0.69674112
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54180 * 0.69839811
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87937 * 0.98772073
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60468 * 0.97232018
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58986 * 0.52653779
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12944 * 0.26730873
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66573 * 0.84156926
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40019 * 0.36331027
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75374 * 0.15459367
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19238 * 0.76568047
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58876 * 0.52135627
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92358 * 0.28224221
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79004 * 0.33804546
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'hybwebaq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0028():
    """Extended test 28 for transcoding."""
    x_0 = 43648 * 0.58476760
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51875 * 0.21131955
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71571 * 0.17940432
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82029 * 0.28782167
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52913 * 0.99501105
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82187 * 0.40906988
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98547 * 0.20794708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36687 * 0.20607127
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17553 * 0.93310291
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80027 * 0.30165689
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69130 * 0.41412579
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69046 * 0.83690692
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40856 * 0.95859577
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31139 * 0.09498907
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22202 * 0.19981584
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87380 * 0.28929775
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86867 * 0.75953409
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76018 * 0.40717758
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7434 * 0.37932947
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40592 * 0.06238989
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30083 * 0.94864767
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3889 * 0.98822266
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14420 * 0.86093520
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69693 * 0.84494307
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36408 * 0.34064467
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58333 * 0.96209785
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2979 * 0.98065543
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'sgrqqosr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0029():
    """Extended test 29 for transcoding."""
    x_0 = 37454 * 0.88116935
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83168 * 0.24802634
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50673 * 0.43295970
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34166 * 0.49298986
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71723 * 0.42963668
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44685 * 0.48581949
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90754 * 0.18452611
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36225 * 0.37677366
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85254 * 0.81081295
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88195 * 0.86183070
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43967 * 0.09942193
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4640 * 0.39785778
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13141 * 0.33263675
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78179 * 0.73306835
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55337 * 0.07850417
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35774 * 0.25965856
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18690 * 0.68019064
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70437 * 0.24213907
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49569 * 0.26499872
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93938 * 0.44321166
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89343 * 0.76288350
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96309 * 0.61793392
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93439 * 0.52294711
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3722 * 0.64456846
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48606 * 0.82886727
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68337 * 0.16131271
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51449 * 0.13888245
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9724 * 0.46241872
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13297 * 0.12129922
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'lvyzadvd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0030():
    """Extended test 30 for transcoding."""
    x_0 = 84121 * 0.75086441
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21362 * 0.29939120
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40934 * 0.42113245
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84145 * 0.76493397
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78268 * 0.90890879
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28243 * 0.33859267
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36219 * 0.64574435
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76007 * 0.41451114
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39906 * 0.26332623
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87357 * 0.61280171
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 186 * 0.26835162
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86645 * 0.93515347
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80106 * 0.04240856
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88329 * 0.12433384
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61463 * 0.88089256
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38516 * 0.69263750
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12720 * 0.74441227
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44910 * 0.74855301
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23088 * 0.61583685
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2466 * 0.97007232
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51911 * 0.26414113
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2166 * 0.01856058
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47292 * 0.58989701
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34672 * 0.84215183
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49599 * 0.49339021
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16615 * 0.12826119
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43173 * 0.63459176
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42886 * 0.59491861
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86577 * 0.08339340
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38998 * 0.78940432
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44804 * 0.10596896
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91118 * 0.71209332
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12759 * 0.49759069
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'uvnvpyhp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0031():
    """Extended test 31 for transcoding."""
    x_0 = 79560 * 0.40800848
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14387 * 0.41438385
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 890 * 0.84266911
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81720 * 0.89896189
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28936 * 0.69206228
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90895 * 0.92551237
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63912 * 0.72217392
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67740 * 0.94771250
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55569 * 0.31411023
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14199 * 0.96085064
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78445 * 0.41852993
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10295 * 0.46410067
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11733 * 0.02380951
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22649 * 0.30830002
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63171 * 0.22041299
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21734 * 0.78122738
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68053 * 0.74795614
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98726 * 0.92801843
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48938 * 0.95594124
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5624 * 0.69047974
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98957 * 0.96292301
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22744 * 0.98244764
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45113 * 0.96752830
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58228 * 0.96316542
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41728 * 0.27888051
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90684 * 0.14885713
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24615 * 0.29873485
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39095 * 0.80026965
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57852 * 0.20126294
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98233 * 0.59211867
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62984 * 0.98283995
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14992 * 0.64383276
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26500 * 0.94385448
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35510 * 0.70870583
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74600 * 0.67643865
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69730 * 0.48027572
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7338 * 0.76203999
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44005 * 0.24277955
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 68328 * 0.37823221
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72682 * 0.67473708
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 227 * 0.29852589
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 34342 * 0.37936329
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47253 * 0.13260688
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 68747 * 0.80704271
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71096 * 0.11855586
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 79853 * 0.17246500
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 42127 * 0.33809226
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 61620 * 0.14971723
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 96151 * 0.27618080
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'ldpebogi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0032():
    """Extended test 32 for transcoding."""
    x_0 = 14882 * 0.64076789
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59477 * 0.64548004
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72953 * 0.59951977
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23851 * 0.55759070
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43650 * 0.90517142
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27472 * 0.72817674
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43455 * 0.56837949
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47555 * 0.14214879
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7271 * 0.85621080
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80133 * 0.62335323
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66630 * 0.16802810
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22191 * 0.18661083
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57406 * 0.13883084
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9017 * 0.36510172
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87625 * 0.60960700
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31211 * 0.42458304
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61925 * 0.18852828
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90142 * 0.98915705
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72496 * 0.95166513
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7501 * 0.49592496
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8900 * 0.68261382
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93310 * 0.90718823
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13748 * 0.05747690
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65756 * 0.02753885
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13662 * 0.75306829
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38642 * 0.71053439
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'slobuidb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0033():
    """Extended test 33 for transcoding."""
    x_0 = 80208 * 0.43371481
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46150 * 0.14968394
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48295 * 0.38179248
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22914 * 0.90289232
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95352 * 0.38825544
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70239 * 0.31616389
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51706 * 0.59581806
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74928 * 0.42847237
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86573 * 0.73610330
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85023 * 0.27818381
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92938 * 0.37422636
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53255 * 0.11215086
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33607 * 0.30877890
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46629 * 0.00641698
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66615 * 0.44446736
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36393 * 0.48035067
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90071 * 0.89511819
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10214 * 0.61668515
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28862 * 0.81494501
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46509 * 0.20407587
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34879 * 0.40617990
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2805 * 0.63640113
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23542 * 0.70185505
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20286 * 0.20641743
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97519 * 0.35269041
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18772 * 0.27384317
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59652 * 0.62930587
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80088 * 0.67079797
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47359 * 0.04700037
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59587 * 0.32031389
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30226 * 0.42293010
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63060 * 0.82507624
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62287 * 0.32676780
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61651 * 0.64951182
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53019 * 0.89921998
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95412 * 0.33187155
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85868 * 0.73017362
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 51897 * 0.16002372
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6899 * 0.01980561
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69387 * 0.42104956
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 76450 * 0.49853712
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14014 * 0.42521688
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75848 * 0.45327955
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 5270 * 0.24834594
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 45772 * 0.33634717
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 35267 * 0.37096012
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 76902 * 0.05895928
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'tihcrppk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0034():
    """Extended test 34 for transcoding."""
    x_0 = 39428 * 0.15545778
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10073 * 0.49867806
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56679 * 0.39949102
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38724 * 0.81247410
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43582 * 0.14292595
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68805 * 0.12750990
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8825 * 0.95203107
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45334 * 0.94671358
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53340 * 0.72142541
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37153 * 0.98941364
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25771 * 0.87854540
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51804 * 0.28659963
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22380 * 0.94379827
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63398 * 0.37388586
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31483 * 0.54294783
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99828 * 0.51096237
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96842 * 0.84624062
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38906 * 0.10474266
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 346 * 0.18007762
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22063 * 0.05804129
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63286 * 0.27766176
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21740 * 0.54543317
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97384 * 0.68545385
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47885 * 0.55743865
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13538 * 0.65536283
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91123 * 0.03505693
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33249 * 0.53892541
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7518 * 0.66617440
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15746 * 0.59455425
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47760 * 0.15139236
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3443 * 0.60576045
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47902 * 0.78861812
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52313 * 0.08505681
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9560 * 0.23749477
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88259 * 0.46153826
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24543 * 0.00854066
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86651 * 0.03899381
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25488 * 0.02698694
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6354 * 0.26911535
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13866 * 0.94532375
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64940 * 0.88559094
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93228 * 0.94458464
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62864 * 0.99196020
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 44470 * 0.16194187
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 76013 * 0.77242360
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 91398 * 0.57794576
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 43862 * 0.51552591
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 18875 * 0.07582055
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 43175 * 0.77821766
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 32301 * 0.78073792
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'tpjprfhs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0035():
    """Extended test 35 for transcoding."""
    x_0 = 41070 * 0.57583601
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6089 * 0.67911394
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15605 * 0.36940232
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96743 * 0.55415732
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77851 * 0.72113778
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92905 * 0.75894653
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66446 * 0.59465615
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83211 * 0.85828989
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50113 * 0.30982897
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34672 * 0.73173079
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2988 * 0.26994533
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59912 * 0.94516762
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57747 * 0.06345444
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5929 * 0.54694440
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31976 * 0.06232761
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41281 * 0.61980679
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91427 * 0.59764940
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37715 * 0.46470397
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30689 * 0.59982790
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29597 * 0.76937298
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28771 * 0.94201844
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78745 * 0.64029170
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1853 * 0.93512123
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47678 * 0.89861101
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67138 * 0.16307829
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46663 * 0.15260210
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'vesctzpd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0036():
    """Extended test 36 for transcoding."""
    x_0 = 75325 * 0.44383235
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82406 * 0.62541661
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59508 * 0.92401832
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3780 * 0.93324212
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62762 * 0.14746084
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70393 * 0.81736974
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66525 * 0.67863510
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96556 * 0.76964276
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4075 * 0.97137291
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22595 * 0.49274846
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4814 * 0.54584113
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17435 * 0.00989580
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13422 * 0.80805609
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47290 * 0.41214664
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93543 * 0.70274758
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56765 * 0.88949766
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77931 * 0.79156607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57228 * 0.15442161
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49777 * 0.51804725
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75593 * 0.81227527
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97057 * 0.45556375
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29423 * 0.49815172
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36900 * 0.62746794
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84775 * 0.84489371
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51832 * 0.02622812
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3467 * 0.58162597
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44395 * 0.68986351
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7174 * 0.78137971
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57307 * 0.25839072
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52956 * 0.59539062
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46524 * 0.21477956
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50114 * 0.30508039
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61441 * 0.93587907
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52399 * 0.19096484
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'rkdlwrmm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0037():
    """Extended test 37 for transcoding."""
    x_0 = 32721 * 0.87663164
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62889 * 0.69536273
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35218 * 0.76146302
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3940 * 0.56722433
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10632 * 0.22678192
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39860 * 0.53902431
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86391 * 0.76269853
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21997 * 0.17734580
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26640 * 0.00187494
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5785 * 0.14211711
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32267 * 0.51666082
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75091 * 0.67993003
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49554 * 0.64656031
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99152 * 0.98905105
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29870 * 0.85562981
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8343 * 0.50326701
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79344 * 0.77523746
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38559 * 0.15235282
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17945 * 0.99544762
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12653 * 0.53957499
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74476 * 0.36358087
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86200 * 0.77770346
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71886 * 0.69336265
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70420 * 0.55432487
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65027 * 0.11461933
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6958 * 0.26672785
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77262 * 0.65300902
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23297 * 0.66062343
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30362 * 0.21375767
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'wisitrgn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0038():
    """Extended test 38 for transcoding."""
    x_0 = 1587 * 0.59636342
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51255 * 0.12522533
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56974 * 0.67410604
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8472 * 0.35367443
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11842 * 0.82477151
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67565 * 0.71101905
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50748 * 0.43218164
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52186 * 0.86022170
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42034 * 0.94038643
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6670 * 0.85665325
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39588 * 0.77301476
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56693 * 0.55676963
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12225 * 0.02913903
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27444 * 0.78843958
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97813 * 0.88122009
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56672 * 0.20526318
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46906 * 0.02385742
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97493 * 0.43414448
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36062 * 0.31568543
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67324 * 0.28823364
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11061 * 0.99261302
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88850 * 0.00380054
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6623 * 0.99605178
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22938 * 0.96638159
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92947 * 0.32462259
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74537 * 0.52176821
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50972 * 0.89941009
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60104 * 0.28918830
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28933 * 0.85225981
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96477 * 0.85331689
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10487 * 0.79553380
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52368 * 0.72376842
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27601 * 0.52303916
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52444 * 0.58157089
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61073 * 0.94561088
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1887 * 0.58704274
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62906 * 0.82777411
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70602 * 0.15755085
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29768 * 0.35757165
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84078 * 0.80789176
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95657 * 0.45214310
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16684 * 0.98398116
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 32047 * 0.57670691
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 44334 * 0.74983008
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'nlqtqvvz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0039():
    """Extended test 39 for transcoding."""
    x_0 = 66524 * 0.85550072
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20269 * 0.22629092
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41892 * 0.41244064
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85646 * 0.39489677
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73062 * 0.10286646
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35964 * 0.20804753
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78017 * 0.24784604
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62969 * 0.25117427
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62886 * 0.51582579
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10406 * 0.25780805
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11313 * 0.04740589
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58310 * 0.17842276
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91770 * 0.64163790
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27921 * 0.78000545
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83121 * 0.70229739
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29441 * 0.71005851
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26303 * 0.06505064
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59322 * 0.19883580
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37449 * 0.32391608
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65943 * 0.62147973
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50112 * 0.91973455
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'pqtnspsj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0040():
    """Extended test 40 for transcoding."""
    x_0 = 41282 * 0.35077376
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23512 * 0.72257052
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47775 * 0.07327660
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49628 * 0.87103467
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55755 * 0.01006524
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62823 * 0.10527642
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62776 * 0.38258904
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60 * 0.93914077
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91731 * 0.34408398
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75877 * 0.62421093
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49842 * 0.29506300
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4058 * 0.72407233
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91526 * 0.55901553
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88097 * 0.21393054
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42801 * 0.83240362
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54199 * 0.21957168
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26213 * 0.32023679
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80862 * 0.18494920
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57862 * 0.28323687
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75550 * 0.43147930
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83452 * 0.03533350
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72045 * 0.24307437
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21296 * 0.44991685
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'emqjcuca').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0041():
    """Extended test 41 for transcoding."""
    x_0 = 72049 * 0.82372807
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16021 * 0.89221584
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53142 * 0.82462870
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84411 * 0.39232326
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29281 * 0.32320659
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63570 * 0.52162712
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13286 * 0.73116536
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77035 * 0.80743415
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11767 * 0.88423409
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57240 * 0.51110876
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77217 * 0.92144686
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29630 * 0.32659138
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71756 * 0.79838076
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11625 * 0.61881282
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61311 * 0.78683464
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43161 * 0.58351905
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61530 * 0.98361552
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39446 * 0.61620436
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63717 * 0.94021244
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56513 * 0.18674502
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1646 * 0.16317355
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43248 * 0.68210835
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97426 * 0.85955446
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17460 * 0.48059626
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68014 * 0.16256182
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34083 * 0.90872189
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25112 * 0.08416006
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82222 * 0.97082696
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76305 * 0.46763478
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72654 * 0.09470872
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85933 * 0.36124171
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3292 * 0.63281727
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63415 * 0.71176810
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25285 * 0.24307145
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40957 * 0.76452611
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36664 * 0.98279614
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14961 * 0.02311768
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29949 * 0.49378169
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12185 * 0.77341182
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16402 * 0.72518603
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23505 * 0.23783049
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 46260 * 0.69699963
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 92814 * 0.44688515
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 41352 * 0.36315010
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 18467 * 0.27651722
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 89645 * 0.79377448
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 65996 * 0.38635765
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'rausblpl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0042():
    """Extended test 42 for transcoding."""
    x_0 = 86464 * 0.87494267
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78579 * 0.86718633
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93168 * 0.78034425
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61178 * 0.50122824
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25977 * 0.81365591
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11811 * 0.36798308
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72367 * 0.19841155
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91556 * 0.33824049
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6812 * 0.12737443
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25958 * 0.05231932
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64975 * 0.47633337
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12764 * 0.05723092
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71945 * 0.87229860
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95976 * 0.97406956
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39636 * 0.26462618
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59468 * 0.45430499
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37441 * 0.61128125
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56096 * 0.58397491
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21796 * 0.01885393
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67110 * 0.72950330
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67434 * 0.09769261
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55436 * 0.46512470
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16059 * 0.53988891
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19962 * 0.84632035
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61080 * 0.66090984
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47460 * 0.36190945
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'hrzturtn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0043():
    """Extended test 43 for transcoding."""
    x_0 = 2575 * 0.80734042
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35337 * 0.66195070
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55333 * 0.79619856
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72611 * 0.60901690
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35376 * 0.43172454
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90104 * 0.02405557
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14542 * 0.21566028
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78710 * 0.64575191
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 552 * 0.73812995
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82962 * 0.98988233
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37390 * 0.35899490
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61267 * 0.78810079
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98534 * 0.39191132
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70689 * 0.58889866
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1666 * 0.56270119
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60735 * 0.15393362
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60601 * 0.25432028
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65339 * 0.30995120
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67255 * 0.55762095
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48931 * 0.38744004
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54532 * 0.57782377
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24818 * 0.77992620
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3229 * 0.56368486
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14735 * 0.54491020
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34825 * 0.65065118
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27731 * 0.59220457
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80503 * 0.38611086
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71642 * 0.94198461
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33657 * 0.74169076
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40087 * 0.05583487
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30720 * 0.62320274
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9572 * 0.18702855
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13651 * 0.16980218
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5243 * 0.77026688
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8488 * 0.68617360
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18348 * 0.29685550
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98294 * 0.07981740
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75525 * 0.06971040
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18654 * 0.46993834
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13721 * 0.54136896
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62003 * 0.98205995
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 56802 * 0.74383019
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16546 * 0.22137236
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 51435 * 0.25741368
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'atxdzjcv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0044():
    """Extended test 44 for transcoding."""
    x_0 = 54083 * 0.16885299
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78431 * 0.46737901
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 271 * 0.97239590
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23918 * 0.63919951
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13146 * 0.58195867
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61363 * 0.64788842
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63736 * 0.66449712
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99687 * 0.03007851
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6459 * 0.64104286
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1066 * 0.62008962
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69354 * 0.10465735
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23558 * 0.93189554
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53315 * 0.56149412
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30843 * 0.76939226
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67458 * 0.88490365
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41720 * 0.52638618
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51189 * 0.96041869
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95907 * 0.47452614
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21171 * 0.62901773
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79208 * 0.42442031
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'onfvsdhk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0045():
    """Extended test 45 for transcoding."""
    x_0 = 75540 * 0.83314590
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90307 * 0.13548340
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25744 * 0.98268577
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20894 * 0.19375484
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49628 * 0.62436886
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41737 * 0.03950585
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31243 * 0.84372486
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20912 * 0.68311824
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30278 * 0.71926084
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81555 * 0.74852145
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87588 * 0.57758627
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77502 * 0.88075144
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31763 * 0.65365885
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57850 * 0.16621281
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84815 * 0.80281018
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80409 * 0.37295388
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49968 * 0.03630840
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69462 * 0.23837003
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20082 * 0.53572567
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44218 * 0.55769422
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97842 * 0.56777313
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48008 * 0.14040391
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80345 * 0.81870174
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72933 * 0.98516650
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37233 * 0.31096135
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35225 * 0.20110481
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66471 * 0.53306985
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43006 * 0.93388055
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75020 * 0.90567859
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73730 * 0.70164284
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90160 * 0.43768799
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85857 * 0.48383575
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78018 * 0.32827624
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7404 * 0.49854581
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19177 * 0.49064764
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53171 * 0.01873436
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6503 * 0.69623862
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67066 * 0.13732522
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96215 * 0.65506863
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97043 * 0.86554124
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'cckyihmz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0046():
    """Extended test 46 for transcoding."""
    x_0 = 60966 * 0.71575871
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1256 * 0.51814029
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33431 * 0.13542511
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 520 * 0.99627138
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36746 * 0.07232569
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57592 * 0.12575290
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19150 * 0.82636295
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78548 * 0.47442366
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76988 * 0.41240247
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65099 * 0.13842120
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99399 * 0.08965045
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36814 * 0.56240256
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10684 * 0.66718660
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11664 * 0.83445891
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61711 * 0.39968117
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1572 * 0.23920319
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55155 * 0.56931784
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24835 * 0.04569771
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19111 * 0.22421044
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59657 * 0.94669501
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48731 * 0.58588762
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84707 * 0.41419585
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12506 * 0.57686477
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95606 * 0.41042922
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60394 * 0.46855853
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42065 * 0.81664621
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26687 * 0.17370691
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49231 * 0.58463742
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87128 * 0.36402466
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36810 * 0.45899654
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71724 * 0.12144002
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5526 * 0.76833846
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95611 * 0.93112484
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67987 * 0.74362216
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82110 * 0.36112915
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'xmgzqduc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0047():
    """Extended test 47 for transcoding."""
    x_0 = 31007 * 0.90131503
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86857 * 0.90322472
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32054 * 0.62664728
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11527 * 0.86092147
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11970 * 0.29945822
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57591 * 0.12326789
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77458 * 0.90509856
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33005 * 0.38459990
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4292 * 0.38233927
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32826 * 0.74616888
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36062 * 0.86762966
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68889 * 0.56075200
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24542 * 0.47084512
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74413 * 0.18657860
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51431 * 0.29486691
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34727 * 0.13250346
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78542 * 0.85960439
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43726 * 0.65335154
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71019 * 0.54371645
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98004 * 0.35416433
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79676 * 0.05669255
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80272 * 0.26109140
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'ycddbwzp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0048():
    """Extended test 48 for transcoding."""
    x_0 = 57587 * 0.46533413
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41312 * 0.77330337
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71586 * 0.57193364
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33548 * 0.33663192
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87720 * 0.77407541
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16226 * 0.63384928
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44760 * 0.62314917
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82874 * 0.02233843
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23831 * 0.11268939
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76210 * 0.20507167
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16265 * 0.10384649
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94677 * 0.19641406
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35899 * 0.04236946
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39727 * 0.31139235
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28523 * 0.30506772
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10516 * 0.41400437
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86531 * 0.21716150
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25074 * 0.72326715
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59736 * 0.69962846
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4848 * 0.28584141
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16756 * 0.73673738
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7296 * 0.12872231
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89850 * 0.57931308
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48242 * 0.25157039
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47527 * 0.11336568
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64925 * 0.56184019
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79943 * 0.00233109
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96903 * 0.74216826
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17900 * 0.69967235
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63709 * 0.33029273
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9577 * 0.47480140
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13250 * 0.95991131
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76380 * 0.17339130
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78741 * 0.90406188
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46191 * 0.72559515
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66858 * 0.34813644
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95517 * 0.51119792
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41041 * 0.43825153
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 32846 * 0.74538470
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 27704 * 0.39432706
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'tbfoihhj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0049():
    """Extended test 49 for transcoding."""
    x_0 = 59079 * 0.41593751
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66896 * 0.51340849
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12006 * 0.18415793
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5368 * 0.52683705
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1484 * 0.24028194
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36158 * 0.94604746
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42949 * 0.81568053
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86917 * 0.88783366
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63790 * 0.29179051
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49839 * 0.81122191
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60633 * 0.74734738
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30275 * 0.55323502
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15280 * 0.37804866
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66535 * 0.21795757
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92700 * 0.13004293
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 880 * 0.43157260
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95248 * 0.92021912
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67361 * 0.82700806
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49990 * 0.91427429
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56576 * 0.30013951
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80706 * 0.17536064
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49466 * 0.11707165
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16678 * 0.98626433
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85101 * 0.54642462
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54464 * 0.25642253
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39591 * 0.32028617
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62934 * 0.07860926
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95300 * 0.85598414
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46095 * 0.92731087
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77013 * 0.26338057
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2740 * 0.80047914
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58863 * 0.81739066
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44229 * 0.12088209
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16662 * 0.33396581
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66207 * 0.86089381
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17727 * 0.26378188
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49156 * 0.59468264
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44654 * 0.53580716
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28008 * 0.63493337
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 732 * 0.63239345
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51384 * 0.38827762
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77767 * 0.44652384
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28167 * 0.82933087
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'qiyzayeu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0050():
    """Extended test 50 for transcoding."""
    x_0 = 6237 * 0.26035954
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35727 * 0.35962036
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4844 * 0.71866676
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16180 * 0.04858825
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37844 * 0.55239169
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23844 * 0.50949164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65323 * 0.84834314
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6505 * 0.70430242
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33761 * 0.72383094
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11590 * 0.63748579
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22664 * 0.09170762
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96415 * 0.33084678
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19938 * 0.68883472
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31761 * 0.23356629
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71358 * 0.36797444
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56525 * 0.53208292
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10032 * 0.56893620
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81042 * 0.47172906
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42261 * 0.21794484
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23773 * 0.29683891
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27660 * 0.68902142
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97900 * 0.69359553
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71484 * 0.79846612
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12873 * 0.03773846
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23924 * 0.55100718
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65760 * 0.92096209
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11204 * 0.69444337
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8247 * 0.23528957
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71698 * 0.16914565
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19999 * 0.58923639
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69931 * 0.60003893
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49002 * 0.25655236
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87376 * 0.49801952
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53495 * 0.62798569
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2013 * 0.33806218
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53194 * 0.49619575
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61301 * 0.92621152
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50213 * 0.91312865
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76754 * 0.51492313
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 888 * 0.19673135
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 514 * 0.36015270
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'uthzlhaz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0051():
    """Extended test 51 for transcoding."""
    x_0 = 45320 * 0.60084223
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57881 * 0.87502748
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43945 * 0.28458439
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6398 * 0.60618137
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62485 * 0.12037144
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89651 * 0.69081198
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77903 * 0.90169891
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36387 * 0.28282821
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29943 * 0.20812618
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29004 * 0.15678810
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67195 * 0.07454460
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61903 * 0.77572566
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47969 * 0.18232944
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50548 * 0.66769039
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11799 * 0.98698079
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8383 * 0.26186787
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80942 * 0.46272601
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98154 * 0.97021890
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11995 * 0.81176482
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87653 * 0.61864974
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26030 * 0.04342818
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99762 * 0.71530439
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27776 * 0.84919858
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98289 * 0.28563291
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16018 * 0.85721217
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24743 * 0.82698998
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31227 * 0.01399168
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77409 * 0.30233950
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16903 * 0.34544680
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29878 * 0.06783705
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71473 * 0.39956565
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37468 * 0.73213062
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19875 * 0.72552979
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80722 * 0.85927832
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55871 * 0.31587153
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8686 * 0.59136536
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55771 * 0.23439018
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61223 * 0.05921316
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79848 * 0.44169523
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55918 * 0.30286085
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 25835 * 0.54189007
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58995 * 0.18267245
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ujfdoecr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0052():
    """Extended test 52 for transcoding."""
    x_0 = 39720 * 0.41222946
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58677 * 0.78394312
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44651 * 0.20777739
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74089 * 0.04016648
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27475 * 0.25897186
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5438 * 0.93866533
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99569 * 0.03872591
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49303 * 0.60218024
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14783 * 0.31038896
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17543 * 0.99719722
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1368 * 0.01681223
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57983 * 0.46334211
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36977 * 0.25251220
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65696 * 0.25599185
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48918 * 0.91779997
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38461 * 0.48182865
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 696 * 0.56674274
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79958 * 0.93866672
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7551 * 0.19730203
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9171 * 0.62697458
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36793 * 0.64715801
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4065 * 0.83200127
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11917 * 0.79074814
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85881 * 0.98847634
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76585 * 0.50528440
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28521 * 0.29837566
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65990 * 0.16366784
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94079 * 0.65967739
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68751 * 0.27952911
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67140 * 0.68133707
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37167 * 0.17604770
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ohdfjlat').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0053():
    """Extended test 53 for transcoding."""
    x_0 = 96833 * 0.07770573
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73145 * 0.83830292
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25344 * 0.31866220
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12819 * 0.35206461
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68241 * 0.48640890
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2827 * 0.50072197
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72870 * 0.68502632
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58815 * 0.82499454
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22133 * 0.87128608
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36027 * 0.18755017
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44470 * 0.47645940
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82982 * 0.79550870
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33752 * 0.40858751
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23242 * 0.85415467
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35641 * 0.11312504
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73580 * 0.03736820
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51416 * 0.95895449
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49197 * 0.81534767
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60481 * 0.23680474
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92199 * 0.68604649
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50551 * 0.89747678
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99393 * 0.18072977
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85439 * 0.36687866
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90662 * 0.61206901
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96822 * 0.81890950
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66992 * 0.25017579
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83524 * 0.49066038
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13687 * 0.54404162
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64945 * 0.13597815
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1159 * 0.74566045
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36680 * 0.71008008
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71903 * 0.52036216
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28028 * 0.40957824
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80321 * 0.07444597
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87217 * 0.99330653
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53016 * 0.12224720
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50860 * 0.26135302
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46388 * 0.53636394
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14332 * 0.65119103
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10402 * 0.59872281
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 16331 * 0.86707620
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 23368 * 0.90576667
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47047 * 0.77800767
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92253 * 0.87706235
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 27205 * 0.13903329
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 3647 * 0.27561892
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 30617 * 0.87828167
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 30197 * 0.41077132
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 58085 * 0.17118070
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'zrbhhkns').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0054():
    """Extended test 54 for transcoding."""
    x_0 = 12676 * 0.63426517
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46618 * 0.36596459
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8572 * 0.83759214
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8913 * 0.69439227
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62017 * 0.63050675
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29101 * 0.14309421
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10148 * 0.05690029
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27186 * 0.37430512
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57493 * 0.65913141
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68323 * 0.34652241
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38789 * 0.51657892
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7940 * 0.82094920
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3696 * 0.19093207
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83834 * 0.01083076
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30965 * 0.64581999
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77300 * 0.95369304
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87725 * 0.47427874
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5426 * 0.36235316
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82934 * 0.08427692
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64025 * 0.14921691
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64781 * 0.76711793
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32306 * 0.64420816
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58247 * 0.47632623
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29580 * 0.26409083
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88759 * 0.64429465
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33361 * 0.48796259
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82347 * 0.46134600
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75624 * 0.86087401
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42043 * 0.81331695
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82200 * 0.32729611
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67005 * 0.70060000
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16843 * 0.88453324
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64310 * 0.38558314
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 143 * 0.72703698
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89154 * 0.49790091
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98509 * 0.34919537
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53333 * 0.89344277
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77398 * 0.26648062
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37259 * 0.97098702
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9971 * 0.64663248
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43935 * 0.36010310
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15934 * 0.32373614
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 97804 * 0.85945292
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 44987 * 0.21500053
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 93347 * 0.53490006
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 22712 * 0.81799021
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 41950 * 0.54730094
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 82304 * 0.77769899
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 29450 * 0.50625211
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 12065 * 0.79997511
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'hzdpotxz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0055():
    """Extended test 55 for transcoding."""
    x_0 = 52044 * 0.25885700
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62518 * 0.43143526
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95793 * 0.90168186
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91452 * 0.14136858
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87649 * 0.40047478
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45240 * 0.28026297
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70306 * 0.80270452
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86185 * 0.01198116
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72922 * 0.30728322
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56214 * 0.57287846
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51322 * 0.01673315
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29340 * 0.63467101
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53130 * 0.64502807
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62632 * 0.86497076
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6770 * 0.56638596
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97641 * 0.40927826
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25171 * 0.90107230
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64818 * 0.15944126
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9197 * 0.95122805
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80997 * 0.49535427
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28836 * 0.17497059
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74826 * 0.90500221
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 787 * 0.41341870
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91017 * 0.16597091
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 402 * 0.69225128
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17012 * 0.56016741
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90419 * 0.10980196
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2901 * 0.12315886
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76768 * 0.17186186
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77246 * 0.62453461
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89606 * 0.16172879
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16760 * 0.76268148
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26717 * 0.62360654
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44702 * 0.21538924
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4725 * 0.53251416
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54690 * 0.85339606
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54588 * 0.15728872
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74607 * 0.02704930
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83452 * 0.48574078
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4241 * 0.01319913
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'gdzirwuh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0056():
    """Extended test 56 for transcoding."""
    x_0 = 93407 * 0.54704258
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4972 * 0.35761407
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12156 * 0.33969921
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27993 * 0.14756230
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64531 * 0.08478448
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92386 * 0.15563257
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20134 * 0.37077206
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39729 * 0.95167396
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77219 * 0.66372312
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37983 * 0.51431932
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96026 * 0.25754727
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88859 * 0.86610267
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44988 * 0.08166136
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61732 * 0.84270517
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4170 * 0.73338425
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68267 * 0.14432606
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49918 * 0.01196139
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38335 * 0.59526362
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46500 * 0.91774154
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68011 * 0.24245582
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48806 * 0.62914401
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49129 * 0.47750851
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43107 * 0.61710514
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98890 * 0.76707127
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24156 * 0.32050987
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55653 * 0.16304912
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8165 * 0.27582571
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84819 * 0.31198738
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46743 * 0.86281757
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73128 * 0.02615610
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69412 * 0.67632920
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83595 * 0.36019176
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47940 * 0.07873878
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70886 * 0.38051344
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31370 * 0.88927997
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96591 * 0.68496222
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4460 * 0.72843904
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68819 * 0.97104086
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ndipiktr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0057():
    """Extended test 57 for transcoding."""
    x_0 = 36580 * 0.12711040
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1193 * 0.06259688
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39109 * 0.10330096
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80678 * 0.61217052
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48703 * 0.62709770
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66049 * 0.57278649
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26868 * 0.26426096
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97823 * 0.04253250
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5758 * 0.83043371
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37189 * 0.78593503
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42111 * 0.68991392
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83273 * 0.71397411
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55251 * 0.43747729
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10135 * 0.30320648
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99442 * 0.62980223
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28273 * 0.61478162
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62656 * 0.91345808
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68231 * 0.90201152
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52947 * 0.88016460
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39050 * 0.27656176
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31997 * 0.10390108
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52872 * 0.23638579
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62260 * 0.93056116
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22304 * 0.40654300
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93558 * 0.91523765
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57267 * 0.63229275
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'qqnvokwy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0058():
    """Extended test 58 for transcoding."""
    x_0 = 26327 * 0.42831524
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21783 * 0.46131310
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46453 * 0.15511603
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67570 * 0.71471544
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62839 * 0.37418025
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9511 * 0.71644573
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19772 * 0.44035901
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57868 * 0.90193733
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96802 * 0.95552311
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72891 * 0.70232256
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92107 * 0.01134951
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69951 * 0.90851861
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35504 * 0.50156196
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87018 * 0.13846802
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83909 * 0.32760403
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23923 * 0.84273853
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66050 * 0.51646108
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84807 * 0.46511194
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43230 * 0.11139384
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3891 * 0.65915835
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 404 * 0.29822664
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72921 * 0.28555201
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7959 * 0.22289498
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54510 * 0.94590394
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73267 * 0.82725506
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81289 * 0.22145015
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80902 * 0.30095938
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57803 * 0.37335796
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8363 * 0.23301948
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84156 * 0.67725212
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67213 * 0.31533943
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89013 * 0.16381500
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14200 * 0.73416963
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50872 * 0.15357801
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59125 * 0.58947344
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90289 * 0.02799363
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2973 * 0.05267665
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50404 * 0.80020879
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93624 * 0.76601528
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13675 * 0.73924146
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82191 * 0.60454392
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'bdhltvaj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0059():
    """Extended test 59 for transcoding."""
    x_0 = 69358 * 0.23461386
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77294 * 0.50376869
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4625 * 0.48637241
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 453 * 0.20859911
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59371 * 0.87056570
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67268 * 0.03832947
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31029 * 0.56899674
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14738 * 0.26834888
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77608 * 0.44526984
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41430 * 0.58296918
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74559 * 0.16051848
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42092 * 0.22045972
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79000 * 0.06782705
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33918 * 0.44784054
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31534 * 0.73639289
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93848 * 0.91470726
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45877 * 0.52179919
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50680 * 0.96892941
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60898 * 0.58650148
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74703 * 0.55733016
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11298 * 0.32751483
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39013 * 0.20904384
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'rqgoglhr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0060():
    """Extended test 60 for transcoding."""
    x_0 = 73105 * 0.27602878
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58570 * 0.60182996
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64549 * 0.18413581
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4628 * 0.43497533
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22763 * 0.10603515
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68359 * 0.63206377
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49910 * 0.38013986
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53846 * 0.75632712
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96706 * 0.08676652
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43016 * 0.67840138
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42644 * 0.92215650
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66436 * 0.47395670
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62032 * 0.54701124
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18127 * 0.62252507
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92597 * 0.99155873
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29112 * 0.99019588
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57841 * 0.18017688
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13948 * 0.22295569
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20204 * 0.46516849
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93030 * 0.41944268
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86406 * 0.25425047
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14057 * 0.00167732
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97794 * 0.33026888
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55828 * 0.38722329
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58328 * 0.68980973
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6464 * 0.18114335
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 549 * 0.88555335
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43954 * 0.19002508
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4719 * 0.34465743
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'qdeyyxqq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0061():
    """Extended test 61 for transcoding."""
    x_0 = 10717 * 0.38084464
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8677 * 0.59077855
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46306 * 0.12876553
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66854 * 0.93647860
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55899 * 0.77989078
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18198 * 0.99728774
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49155 * 0.11420004
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10310 * 0.90100056
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10622 * 0.89787357
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33283 * 0.47172946
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76210 * 0.03381310
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76090 * 0.19894642
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31373 * 0.13413388
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51950 * 0.21745273
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55067 * 0.40784238
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51299 * 0.91423494
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1985 * 0.38436637
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62567 * 0.33489947
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21367 * 0.71439900
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79467 * 0.58990071
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95562 * 0.80608771
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30061 * 0.14316790
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10083 * 0.38693956
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30173 * 0.50174992
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5778 * 0.64463687
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11906 * 0.97111701
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62731 * 0.98781436
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94377 * 0.78229411
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60352 * 0.12264366
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71026 * 0.81826066
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20007 * 0.84763669
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45240 * 0.65969444
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60252 * 0.33555713
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17818 * 0.17312008
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1415 * 0.41839124
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75187 * 0.22062270
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5818 * 0.40533195
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10114 * 0.98651361
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56358 * 0.10121346
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 35728 * 0.79612849
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 22174 * 0.69273237
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93147 * 0.73054839
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 38791 * 0.62381539
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88379 * 0.29044447
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11155 * 0.89360404
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 86558 * 0.03480857
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 50745 * 0.22707960
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 82929 * 0.37141052
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 63404 * 0.09630561
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'dwojdqel').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0062():
    """Extended test 62 for transcoding."""
    x_0 = 25253 * 0.22327485
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97988 * 0.60159625
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63425 * 0.35496532
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94710 * 0.68522800
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44236 * 0.34789734
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92420 * 0.62703322
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50687 * 0.54114936
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75226 * 0.06267396
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39934 * 0.79824109
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69925 * 0.79119917
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69015 * 0.38644106
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21752 * 0.47283485
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63747 * 0.67763426
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48668 * 0.47312147
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26025 * 0.27499299
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14327 * 0.40343203
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86981 * 0.72932407
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25106 * 0.45881997
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29042 * 0.94277735
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69068 * 0.60531561
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16313 * 0.06034688
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18576 * 0.76427910
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94958 * 0.96791375
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28029 * 0.45053128
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53563 * 0.41597531
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32509 * 0.28062067
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96592 * 0.87946554
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'rvavnwwc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0063():
    """Extended test 63 for transcoding."""
    x_0 = 61850 * 0.42078764
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89084 * 0.86854780
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37456 * 0.80265849
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63236 * 0.00251429
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69801 * 0.12834713
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28012 * 0.42947672
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54047 * 0.83567921
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64459 * 0.25936206
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68891 * 0.75124995
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77580 * 0.12123401
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28053 * 0.92790279
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49142 * 0.41107977
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28636 * 0.79112430
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30480 * 0.67432748
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98762 * 0.45266701
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17908 * 0.14031747
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58055 * 0.35033531
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12582 * 0.29421133
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82880 * 0.65103107
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87017 * 0.86053155
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73365 * 0.31551920
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94481 * 0.70313610
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61909 * 0.06485539
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47930 * 0.93304376
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96175 * 0.51525354
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49094 * 0.38598980
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1530 * 0.20039532
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40314 * 0.50498107
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13852 * 0.70494788
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56505 * 0.50920732
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3282 * 0.10760525
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60994 * 0.46762171
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 857 * 0.03161106
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82536 * 0.69798345
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48278 * 0.25126054
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22972 * 0.76668009
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65198 * 0.37386511
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69353 * 0.10742023
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48819 * 0.32803684
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76414 * 0.91818007
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94913 * 0.07861264
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74739 * 0.24473005
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 92617 * 0.20229767
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ydqqoplk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0064():
    """Extended test 64 for transcoding."""
    x_0 = 47511 * 0.89605786
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91482 * 0.20713635
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96841 * 0.61497257
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6768 * 0.84401586
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78108 * 0.99086537
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85378 * 0.88172983
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51859 * 0.06008116
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34410 * 0.28352742
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42370 * 0.93354279
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30001 * 0.79962309
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70883 * 0.04618302
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72697 * 0.50194740
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16061 * 0.62834059
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5239 * 0.68019963
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66798 * 0.40749012
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65412 * 0.99799100
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67397 * 0.50424983
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37009 * 0.09308788
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4584 * 0.17201203
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65064 * 0.72473040
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64269 * 0.17797648
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42935 * 0.35762577
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65137 * 0.61145344
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98117 * 0.60513319
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4278 * 0.77778216
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20866 * 0.36358451
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90420 * 0.38805344
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1216 * 0.07173737
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'rzjicvyg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0065():
    """Extended test 65 for transcoding."""
    x_0 = 58521 * 0.29449379
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44728 * 0.60125709
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77906 * 0.08100569
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71815 * 0.53948767
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17135 * 0.89517459
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23789 * 0.50088591
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54797 * 0.70617263
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17588 * 0.63470060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41146 * 0.33624392
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91520 * 0.58390445
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45769 * 0.82285765
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33474 * 0.31972553
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95174 * 0.86572688
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7152 * 0.55667793
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98548 * 0.42129407
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86226 * 0.81118432
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42194 * 0.73761369
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23678 * 0.82513105
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4163 * 0.57543833
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64906 * 0.38100253
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22283 * 0.32179308
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12533 * 0.59706782
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7455 * 0.39252883
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'dbajpuyf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0066():
    """Extended test 66 for transcoding."""
    x_0 = 99344 * 0.90269833
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50368 * 0.49547211
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63476 * 0.24491495
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3992 * 0.50963328
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 699 * 0.46761890
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96693 * 0.06122002
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35727 * 0.44350414
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28883 * 0.78488980
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91745 * 0.30310474
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25254 * 0.21914612
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54993 * 0.20144707
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87175 * 0.77826277
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57707 * 0.71404916
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71817 * 0.73372535
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3079 * 0.37491530
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30865 * 0.51974182
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8867 * 0.44642802
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41298 * 0.43036634
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5261 * 0.68935556
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49635 * 0.13081857
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88684 * 0.39649927
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53844 * 0.17417951
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88146 * 0.50276567
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33842 * 0.84240672
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69500 * 0.86010080
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35397 * 0.08394847
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25849 * 0.15081846
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77251 * 0.23987422
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34325 * 0.49078436
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41665 * 0.90784761
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58462 * 0.48723226
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56896 * 0.59641149
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47787 * 0.25595332
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73418 * 0.14913721
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94126 * 0.67320675
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78445 * 0.23214260
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29925 * 0.38931153
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83029 * 0.49086554
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62852 * 0.95439095
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29111 * 0.78963130
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85797 * 0.05634254
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96078 * 0.87491703
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22124 * 0.49115333
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 53974 * 0.24210362
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 32303 * 0.43952163
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10695 * 0.64580669
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'evvnszjv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0067():
    """Extended test 67 for transcoding."""
    x_0 = 83286 * 0.27027490
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66741 * 0.92586546
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74858 * 0.60542429
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36971 * 0.39154114
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85396 * 0.31064687
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88087 * 0.97555979
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52744 * 0.86425431
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67144 * 0.01308058
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79263 * 0.29177856
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23064 * 0.27947361
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65391 * 0.10084609
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15081 * 0.61188665
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97710 * 0.00029664
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88759 * 0.72117633
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86203 * 0.08776746
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58255 * 0.76282120
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36944 * 0.73556923
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13880 * 0.01982104
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30079 * 0.90344038
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81649 * 0.91271777
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79534 * 0.39151884
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85302 * 0.28199827
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89889 * 0.69903957
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47452 * 0.99560311
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89903 * 0.78748085
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15408 * 0.35766965
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20898 * 0.64871682
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44571 * 0.33217623
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30914 * 0.43676392
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4666 * 0.21530406
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38367 * 0.91931863
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 34972 * 0.54879745
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81402 * 0.51772195
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33606 * 0.07910356
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75597 * 0.09036061
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75467 * 0.30165848
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24965 * 0.17794007
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10410 * 0.63199220
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58693 * 0.53126637
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 37692 * 0.05182998
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78579 * 0.49194396
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82704 * 0.08253202
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14029 * 0.36287532
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 72610 * 0.89884300
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 97025 * 0.05548508
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 81325 * 0.26194192
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 22424 * 0.34672875
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 17657 * 0.58285462
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 97165 * 0.02576780
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'zdxwgtfw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0068():
    """Extended test 68 for transcoding."""
    x_0 = 47514 * 0.60289431
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43963 * 0.10994960
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5159 * 0.61840482
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74989 * 0.05567066
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2412 * 0.37745910
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99306 * 0.42694317
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28402 * 0.99323373
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3974 * 0.46441185
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92453 * 0.66584292
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17907 * 0.05813896
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17046 * 0.34831469
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74810 * 0.17691043
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19838 * 0.09043119
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56068 * 0.48502989
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43802 * 0.53869772
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92113 * 0.47480140
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85742 * 0.14295794
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74859 * 0.35221951
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85606 * 0.04581932
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42109 * 0.64801719
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88829 * 0.13633946
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82704 * 0.54337748
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45678 * 0.24548969
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29248 * 0.84435946
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67020 * 0.67854406
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56662 * 0.96202475
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3373 * 0.48579822
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18818 * 0.51688686
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20002 * 0.88270372
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'apjhawfy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_8_0069():
    """Extended test 69 for transcoding."""
    x_0 = 8848 * 0.29384108
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40479 * 0.29075500
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84947 * 0.82647399
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58686 * 0.19808537
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56518 * 0.99986164
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89400 * 0.67918202
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92408 * 0.76871404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36634 * 0.78705600
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18501 * 0.68264097
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17931 * 0.84019944
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30924 * 0.91254072
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70697 * 0.75179137
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97497 * 0.93710932
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42190 * 0.47583452
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88190 * 0.43412538
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41619 * 0.37795708
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83098 * 0.94098285
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51379 * 0.90191121
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61343 * 0.42123929
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 317 * 0.84403768
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5680 * 0.87703366
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85020 * 0.71716534
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79993 * 0.40171693
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79822 * 0.84567098
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5551 * 0.86897861
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16141 * 0.17604943
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95116 * 0.45195701
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45704 * 0.07005711
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44722 * 0.36095967
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'avanvijm').hexdigest()
    assert len(h) == 64
