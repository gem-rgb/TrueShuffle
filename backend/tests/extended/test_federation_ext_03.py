"""Extended tests for federation suite 3."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_federation_extended_3_0000():
    """Extended test 0 for federation."""
    x_0 = 7668 * 0.39553395
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10961 * 0.59970828
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50367 * 0.45044682
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40158 * 0.92929664
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63872 * 0.28051324
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49265 * 0.62907530
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66188 * 0.02523673
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89980 * 0.19772510
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16991 * 0.44120535
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15045 * 0.46155607
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9198 * 0.37467870
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89550 * 0.96026305
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65920 * 0.56515795
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59264 * 0.60817846
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44738 * 0.11061556
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54454 * 0.31330295
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71538 * 0.00171520
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85860 * 0.85658518
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1083 * 0.71949733
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39624 * 0.72567074
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27484 * 0.82702764
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67250 * 0.01346882
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72597 * 0.02285881
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36099 * 0.86016058
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59154 * 0.43937224
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1748 * 0.81370050
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45539 * 0.52521193
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39389 * 0.28212801
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54194 * 0.92847218
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'qvcmajbt').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0001():
    """Extended test 1 for federation."""
    x_0 = 25586 * 0.17722436
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3083 * 0.17087765
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2434 * 0.04868618
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70565 * 0.31668717
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40916 * 0.87679861
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57061 * 0.18842193
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97781 * 0.98283220
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5468 * 0.63283809
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34551 * 0.05520497
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7116 * 0.99438511
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74559 * 0.31009572
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44525 * 0.53847203
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62809 * 0.17861289
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54957 * 0.75680686
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29815 * 0.99309687
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78956 * 0.10529032
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54948 * 0.83118160
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44749 * 0.75958144
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93794 * 0.37238645
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38911 * 0.51020131
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5683 * 0.45964532
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77450 * 0.55764490
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66979 * 0.14501985
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56346 * 0.43820723
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88133 * 0.15493114
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'uaumypis').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0002():
    """Extended test 2 for federation."""
    x_0 = 54781 * 0.07545222
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41923 * 0.98137849
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75194 * 0.19066642
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70293 * 0.88401136
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81758 * 0.50320280
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3346 * 0.12895645
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92043 * 0.10200469
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16024 * 0.48480167
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71651 * 0.35953047
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3451 * 0.08770822
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38313 * 0.83625319
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2550 * 0.74900431
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90173 * 0.45108328
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69807 * 0.30541369
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64304 * 0.83461023
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8961 * 0.76230541
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76132 * 0.05696445
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2359 * 0.94575946
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53890 * 0.16362881
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89781 * 0.61473541
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8050 * 0.31739047
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77987 * 0.82107457
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28054 * 0.83433982
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28780 * 0.24199038
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92669 * 0.70303512
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89214 * 0.65802945
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54713 * 0.65983792
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8567 * 0.11663074
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97531 * 0.11453278
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73495 * 0.63114777
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'lowqnbjl').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0003():
    """Extended test 3 for federation."""
    x_0 = 69142 * 0.85965421
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51928 * 0.86244936
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22086 * 0.05238651
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80907 * 0.18794750
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49134 * 0.97340977
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 232 * 0.74649566
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85708 * 0.27289765
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66527 * 0.34517325
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33445 * 0.31015315
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43773 * 0.58310686
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79524 * 0.43657251
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78939 * 0.26706200
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97996 * 0.33487056
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8339 * 0.91501108
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40767 * 0.08116177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59650 * 0.86764464
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27493 * 0.08207841
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35196 * 0.66836879
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91470 * 0.19966409
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21369 * 0.84698556
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99226 * 0.27840247
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70663 * 0.87771582
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87603 * 0.48128311
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12836 * 0.38881601
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55200 * 0.73594097
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98709 * 0.03401788
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68666 * 0.08542817
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85651 * 0.33523386
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46168 * 0.92026986
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9017 * 0.14843434
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'mwyffibr').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0004():
    """Extended test 4 for federation."""
    x_0 = 11707 * 0.47784797
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79326 * 0.39972709
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69442 * 0.72571490
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55687 * 0.61384630
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92153 * 0.87403580
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67287 * 0.05752873
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27299 * 0.28764113
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18545 * 0.31176946
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65977 * 0.63140500
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81927 * 0.65275344
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16352 * 0.40183688
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86108 * 0.50908415
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43761 * 0.12583841
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15366 * 0.30394363
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66625 * 0.73862713
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67692 * 0.37680798
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24206 * 0.60229026
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83084 * 0.65375327
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60613 * 0.16878004
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89788 * 0.55554557
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78186 * 0.31508251
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49562 * 0.21022106
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 393 * 0.37372180
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35344 * 0.56476738
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 497 * 0.91806661
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95965 * 0.37492176
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8099 * 0.03334433
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1459 * 0.46637984
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13488 * 0.68458644
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78232 * 0.57438830
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43107 * 0.03337125
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82334 * 0.56081224
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4091 * 0.06067487
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24180 * 0.83379033
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91074 * 0.40551067
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95482 * 0.39222448
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5730 * 0.33146399
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69786 * 0.76205696
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 22272 * 0.06444176
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20104 * 0.34149576
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78349 * 0.47789754
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12584 * 0.39017316
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 43629 * 0.58477947
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82180 * 0.74158047
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 99197 * 0.45070771
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 60171 * 0.22005269
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 33509 * 0.71489692
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 71193 * 0.90192679
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'xxspwptj').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0005():
    """Extended test 5 for federation."""
    x_0 = 19042 * 0.74450870
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26451 * 0.80632781
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21922 * 0.19105416
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4600 * 0.16773994
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70343 * 0.49284145
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21923 * 0.38110842
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60199 * 0.28365271
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86016 * 0.59419343
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30193 * 0.97358464
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75504 * 0.36444172
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68608 * 0.04129953
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74647 * 0.85071446
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87173 * 0.51833930
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50666 * 0.33281973
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25612 * 0.56306343
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75555 * 0.01531729
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4934 * 0.65784053
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81281 * 0.19538462
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78087 * 0.87863740
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12572 * 0.17880146
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93032 * 0.41430272
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53265 * 0.62054120
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9306 * 0.21065951
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59277 * 0.29672164
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18177 * 0.99429367
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67133 * 0.84353271
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77855 * 0.20211689
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29005 * 0.75302571
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45427 * 0.77828101
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59476 * 0.14140863
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59538 * 0.38089851
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14151 * 0.60246548
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40498 * 0.36596502
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39991 * 0.18117930
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19177 * 0.28740937
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51017 * 0.63902716
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99976 * 0.05765575
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61238 * 0.21105661
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99301 * 0.66369815
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82911 * 0.96443820
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47256 * 0.06866204
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16670 * 0.97938108
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20360 * 0.04704654
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 67222 * 0.89674253
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 38449 * 0.83908742
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 17557 * 0.06778883
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 74641 * 0.66783482
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 54367 * 0.73199048
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'woggwlwf').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0006():
    """Extended test 6 for federation."""
    x_0 = 97714 * 0.10095195
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44629 * 0.18978808
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54350 * 0.53971172
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75643 * 0.39038339
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39524 * 0.37199238
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38684 * 0.94140655
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1854 * 0.39947068
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16382 * 0.57786700
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37031 * 0.25032975
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99767 * 0.92215370
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84445 * 0.97220020
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9473 * 0.53110581
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92593 * 0.21624907
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67854 * 0.21102074
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60834 * 0.36528355
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65541 * 0.94965974
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25364 * 0.37591462
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99359 * 0.63063654
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93816 * 0.41056499
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43963 * 0.54030678
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16968 * 0.54899731
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12651 * 0.77273881
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98302 * 0.27584146
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30497 * 0.07598650
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82556 * 0.39971707
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17938 * 0.58604049
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50686 * 0.67208183
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20256 * 0.05850493
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72509 * 0.22925883
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75494 * 0.24343852
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53190 * 0.44332547
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44748 * 0.02338011
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36889 * 0.76618658
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43856 * 0.04669608
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79882 * 0.82267284
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43166 * 0.04549229
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'swnqttmn').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0007():
    """Extended test 7 for federation."""
    x_0 = 93308 * 0.78987791
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24110 * 0.71702757
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67961 * 0.85220689
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26623 * 0.82995496
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91803 * 0.57315816
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84294 * 0.67914267
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98810 * 0.16900762
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88443 * 0.45294794
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61356 * 0.18762854
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23706 * 0.23387918
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69717 * 0.11662971
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25034 * 0.86236480
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45572 * 0.26405497
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75010 * 0.48793236
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25500 * 0.20557038
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46531 * 0.09314997
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40928 * 0.16486086
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46909 * 0.86119790
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6302 * 0.84748090
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54854 * 0.23475710
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65441 * 0.20050118
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48400 * 0.76305668
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87110 * 0.26451426
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53239 * 0.78457678
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34008 * 0.07322365
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40436 * 0.75116957
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84199 * 0.29385049
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43014 * 0.44537171
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13017 * 0.49758940
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9340 * 0.06337215
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89496 * 0.46134135
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74818 * 0.11413820
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45005 * 0.86257335
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87570 * 0.68877791
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1821 * 0.50708852
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47626 * 0.13424400
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71244 * 0.91473418
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4278 * 0.72523234
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42410 * 0.67951410
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47959 * 0.93128551
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 96565 * 0.87250580
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 90529 * 0.57769253
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 991 * 0.31450238
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99184 * 0.01302548
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'wkficxgf').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0008():
    """Extended test 8 for federation."""
    x_0 = 55591 * 0.03498829
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51685 * 0.48202661
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78305 * 0.17245092
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57766 * 0.36614776
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59626 * 0.33694210
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44619 * 0.30596608
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29542 * 0.38708217
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21548 * 0.07385148
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96714 * 0.98321894
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37189 * 0.89559571
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55597 * 0.80886184
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60371 * 0.41822744
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9988 * 0.27068853
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83045 * 0.91137965
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90839 * 0.02692896
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42032 * 0.61126930
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61854 * 0.75304037
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29708 * 0.48833181
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6112 * 0.47909715
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69423 * 0.16753923
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89411 * 0.71121396
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65639 * 0.49234495
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2586 * 0.52433356
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11139 * 0.01573849
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87231 * 0.83808514
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5168 * 0.71661679
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'vgjzkcfy').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0009():
    """Extended test 9 for federation."""
    x_0 = 10398 * 0.42431716
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41989 * 0.57135212
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17838 * 0.25928861
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65372 * 0.24972912
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23342 * 0.30151280
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98450 * 0.06996246
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34216 * 0.79476409
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84818 * 0.11920915
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35399 * 0.58860413
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75591 * 0.87352930
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23189 * 0.84140045
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37930 * 0.85301981
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18856 * 0.14943672
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97360 * 0.54445469
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29026 * 0.03577544
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49958 * 0.71414714
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49461 * 0.70873405
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54282 * 0.59850798
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19094 * 0.07797774
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59932 * 0.19103238
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66832 * 0.60298015
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95505 * 0.18375526
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'sidtqivb').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0010():
    """Extended test 10 for federation."""
    x_0 = 37693 * 0.61562782
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19726 * 0.56441563
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45233 * 0.42830330
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 388 * 0.18068740
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97348 * 0.07895037
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65429 * 0.66780463
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32044 * 0.91346178
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25128 * 0.84979086
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57890 * 0.43143793
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43359 * 0.90537197
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75587 * 0.37579057
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47265 * 0.11856937
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8358 * 0.51271445
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76996 * 0.14098483
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77665 * 0.46473925
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31418 * 0.76562814
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36992 * 0.26577700
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13620 * 0.15061229
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80249 * 0.24890184
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27559 * 0.15253555
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44973 * 0.29107774
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44418 * 0.93035031
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49250 * 0.48758752
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71916 * 0.42986765
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86487 * 0.01448252
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63212 * 0.49214426
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31585 * 0.21733777
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64625 * 0.35867731
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27593 * 0.60230586
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55595 * 0.34657523
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91493 * 0.10112049
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56937 * 0.79183321
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92853 * 0.33455366
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39055 * 0.94039422
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92581 * 0.29083340
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53009 * 0.89086341
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86347 * 0.51378588
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79878 * 0.12280901
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66795 * 0.24523830
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33694 * 0.48900671
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 92054 * 0.69350926
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88147 * 0.87619587
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 97213 * 0.98963065
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22123 * 0.89759288
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 67077 * 0.67803092
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 42870 * 0.31196331
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 82793 * 0.66289495
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'umplmfnz').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0011():
    """Extended test 11 for federation."""
    x_0 = 32172 * 0.15658382
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65462 * 0.04984168
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22099 * 0.81097273
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18678 * 0.53826144
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7400 * 0.78787707
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77980 * 0.26410105
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16984 * 0.03515839
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81913 * 0.89930536
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37879 * 0.59679295
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38046 * 0.87638203
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79773 * 0.59844372
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36174 * 0.96900475
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69965 * 0.96769229
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46218 * 0.77864563
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8581 * 0.16933226
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60392 * 0.70773718
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93684 * 0.19157858
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57934 * 0.69693277
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65243 * 0.36752408
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19090 * 0.89533239
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80027 * 0.39501383
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93159 * 0.60094223
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58257 * 0.74679784
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66358 * 0.45340399
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76905 * 0.81270176
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21591 * 0.63931589
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29603 * 0.24248070
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3621 * 0.82389645
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17009 * 0.85208446
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20245 * 0.40277045
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31611 * 0.57877004
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20542 * 0.62405708
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31563 * 0.08061362
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7653 * 0.88723222
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37756 * 0.83948672
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13345 * 0.44300164
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29404 * 0.07842683
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43058 * 0.91247703
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17242 * 0.04700032
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'kllsrnyy').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0012():
    """Extended test 12 for federation."""
    x_0 = 51573 * 0.17916418
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85682 * 0.28999972
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80896 * 0.01905825
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81005 * 0.41638564
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98059 * 0.22927534
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86075 * 0.65480817
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39784 * 0.66588105
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78162 * 0.06364295
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84072 * 0.63884459
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18140 * 0.83378949
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75313 * 0.33065661
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65860 * 0.94661410
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61017 * 0.90152248
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55939 * 0.00962433
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42457 * 0.73052936
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69603 * 0.64217869
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36063 * 0.62872040
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20803 * 0.02262796
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2008 * 0.09584391
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44766 * 0.74201265
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19437 * 0.60212815
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85664 * 0.26467838
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49563 * 0.51431589
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64160 * 0.00477919
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8845 * 0.44663699
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24002 * 0.36802221
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21538 * 0.06374259
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19839 * 0.17624975
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19849 * 0.84569365
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27310 * 0.03976270
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88988 * 0.46314741
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19107 * 0.52330031
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41472 * 0.25993559
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'gxreghvu').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0013():
    """Extended test 13 for federation."""
    x_0 = 14212 * 0.34861113
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83857 * 0.14202079
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49864 * 0.66957523
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89287 * 0.41786953
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74620 * 0.68141915
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92554 * 0.77333324
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39773 * 0.19962768
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2409 * 0.76659250
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14361 * 0.03453791
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16191 * 0.14703977
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49142 * 0.81366100
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33305 * 0.39942486
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1443 * 0.45278714
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2711 * 0.86844125
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1523 * 0.11212158
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3241 * 0.40120528
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39086 * 0.23272811
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77482 * 0.15757973
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17768 * 0.72048003
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67951 * 0.51224818
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'jyifyhsz').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0014():
    """Extended test 14 for federation."""
    x_0 = 31162 * 0.99318804
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33417 * 0.98681777
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50468 * 0.14507758
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59269 * 0.17896325
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76064 * 0.74601858
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67007 * 0.61298765
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90385 * 0.24815789
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81481 * 0.77623606
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18372 * 0.60208591
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77689 * 0.22913741
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67556 * 0.42754765
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15232 * 0.49060189
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99319 * 0.87065721
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11079 * 0.70369591
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97198 * 0.44186030
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88242 * 0.56842531
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27356 * 0.43848075
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91917 * 0.57949178
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86195 * 0.01750089
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24578 * 0.82461960
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78082 * 0.73823354
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82645 * 0.61648116
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62566 * 0.82502733
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76583 * 0.15044954
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60304 * 0.83788588
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85946 * 0.52713666
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44404 * 0.45320034
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43016 * 0.53776059
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76348 * 0.18560880
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62596 * 0.61867867
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53007 * 0.85445671
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 189 * 0.31471796
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2556 * 0.65839688
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24447 * 0.74310828
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19707 * 0.43488134
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38691 * 0.82821151
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20924 * 0.68450185
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56119 * 0.40438209
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96647 * 0.73965143
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23245 * 0.05083564
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38087 * 0.10517195
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 24105 * 0.83444315
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 67464 * 0.48766406
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 95938 * 0.77790293
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 16946 * 0.59156762
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26287 * 0.15896662
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 59914 * 0.03047928
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'oduzbmkd').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0015():
    """Extended test 15 for federation."""
    x_0 = 68378 * 0.41915284
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49549 * 0.32023466
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2713 * 0.37672893
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45564 * 0.92264371
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39272 * 0.30353891
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98178 * 0.33351235
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15130 * 0.22106414
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12967 * 0.92543875
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45828 * 0.82450256
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11248 * 0.62840790
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50837 * 0.87886502
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87210 * 0.38996662
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42635 * 0.96528759
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22032 * 0.81016110
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63508 * 0.77701670
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55339 * 0.80689266
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41104 * 0.99989873
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1031 * 0.94319729
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81362 * 0.16869171
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46833 * 0.93589581
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44913 * 0.25908803
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16255 * 0.69574982
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36064 * 0.17523465
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1562 * 0.44233300
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93309 * 0.10489271
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66024 * 0.45000043
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40208 * 0.01199479
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62847 * 0.27521084
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'yukrhtgp').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0016():
    """Extended test 16 for federation."""
    x_0 = 11986 * 0.19878445
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74911 * 0.45181913
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21652 * 0.76558832
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83714 * 0.86194715
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89271 * 0.37554182
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69400 * 0.14767243
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20456 * 0.90317283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86435 * 0.43994706
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14017 * 0.98034954
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81890 * 0.10496513
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24448 * 0.62432464
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56986 * 0.77147513
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59832 * 0.58113855
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75984 * 0.09696434
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31552 * 0.27667884
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89741 * 0.08529515
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61945 * 0.65777305
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58640 * 0.32988477
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48341 * 0.58075661
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10904 * 0.95054686
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15314 * 0.11174533
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17527 * 0.22088629
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60873 * 0.78463727
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61430 * 0.45449842
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60167 * 0.45381366
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86229 * 0.12214738
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48598 * 0.39145798
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12304 * 0.15722168
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79140 * 0.47934003
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54007 * 0.73918397
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8456 * 0.46376689
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60328 * 0.63143200
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22370 * 0.06114347
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29043 * 0.25130429
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82565 * 0.91192912
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70472 * 0.98446200
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 6168 * 0.08285141
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78342 * 0.85080221
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9168 * 0.89285353
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17672 * 0.50474082
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 871 * 0.84895830
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80954 * 0.99338831
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'fjssawrj').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0017():
    """Extended test 17 for federation."""
    x_0 = 53500 * 0.65864369
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9886 * 0.67487054
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72697 * 0.08771568
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18504 * 0.25804246
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5796 * 0.38578374
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2984 * 0.44328183
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13328 * 0.56079606
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59226 * 0.39258138
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75914 * 0.41116931
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83134 * 0.96468018
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50745 * 0.43338414
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72760 * 0.85311990
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70150 * 0.21122649
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67069 * 0.26899429
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31538 * 0.31628964
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41869 * 0.90356693
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74886 * 0.92394400
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19658 * 0.71891981
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48247 * 0.63400891
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11198 * 0.33077237
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13455 * 0.60271218
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63598 * 0.81365964
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'oadaatha').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0018():
    """Extended test 18 for federation."""
    x_0 = 73634 * 0.61142678
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65742 * 0.51288663
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98202 * 0.80144793
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78422 * 0.54249954
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15649 * 0.53129918
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63275 * 0.34207624
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23852 * 0.49745623
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51171 * 0.57900854
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49762 * 0.88549217
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42142 * 0.33772751
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81208 * 0.34621097
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29497 * 0.05556225
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50998 * 0.64352928
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40854 * 0.13709291
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46098 * 0.17297417
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54723 * 0.86359606
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68095 * 0.85931120
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84526 * 0.81229504
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11968 * 0.00628435
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74804 * 0.77211049
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16540 * 0.38068181
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5046 * 0.04179383
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91806 * 0.89436600
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37913 * 0.92377318
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48397 * 0.02885338
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81731 * 0.72464566
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15904 * 0.79553439
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98289 * 0.14924052
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87623 * 0.61931474
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88351 * 0.51042710
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62192 * 0.00430414
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79588 * 0.69998220
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37078 * 0.29423290
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69130 * 0.74816723
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84618 * 0.41183036
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7771 * 0.31087661
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78640 * 0.46478405
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49984 * 0.32643394
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83143 * 0.37436248
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57454 * 0.04815381
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 61016 * 0.67358509
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13348 * 0.63736520
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 78765 * 0.95444181
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39001 * 0.75979930
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 83577 * 0.47573801
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 42647 * 0.11154883
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17204 * 0.82018944
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 82746 * 0.42266940
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 10119 * 0.79380359
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 17226 * 0.51797253
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'naflkrlw').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0019():
    """Extended test 19 for federation."""
    x_0 = 65311 * 0.46763372
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28606 * 0.75147539
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10167 * 0.39806056
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90930 * 0.26222591
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21923 * 0.93622538
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63996 * 0.30417785
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17038 * 0.66219963
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65410 * 0.72588900
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85831 * 0.99503299
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85662 * 0.83854842
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31515 * 0.46066093
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62948 * 0.35416143
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 266 * 0.77277986
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78483 * 0.65925206
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89359 * 0.29496284
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49507 * 0.70889709
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1660 * 0.25332885
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22368 * 0.25758474
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28125 * 0.32854666
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26270 * 0.27909969
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36440 * 0.28821541
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8721 * 0.63629915
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60243 * 0.38860347
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72349 * 0.21901746
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62193 * 0.24332377
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69287 * 0.11032389
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21524 * 0.71748842
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14884 * 0.78553588
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15957 * 0.89385248
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99332 * 0.59619406
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35319 * 0.20545701
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75356 * 0.90257201
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49852 * 0.16064468
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79909 * 0.59113351
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11120 * 0.28084415
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23041 * 0.34074111
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21647 * 0.70011054
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65091 * 0.20765882
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48810 * 0.61887278
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3321 * 0.25631217
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69889 * 0.88763269
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70646 * 0.75058451
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'fmcvxdqe').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0020():
    """Extended test 20 for federation."""
    x_0 = 55620 * 0.98969658
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78636 * 0.65188706
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14161 * 0.34855488
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27692 * 0.96412049
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63641 * 0.98072359
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42689 * 0.29919996
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16656 * 0.69530134
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43078 * 0.87911990
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90933 * 0.06295752
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83387 * 0.11902885
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76837 * 0.27450349
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84327 * 0.91443108
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8647 * 0.14408241
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39770 * 0.60871826
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9262 * 0.88902596
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97326 * 0.28891576
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48957 * 0.87661964
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96387 * 0.59864991
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75983 * 0.40738104
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9336 * 0.01752391
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33326 * 0.63156827
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97676 * 0.54913340
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'mfbpsjdh').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0021():
    """Extended test 21 for federation."""
    x_0 = 87226 * 0.46158548
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29131 * 0.89762434
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39316 * 0.73171899
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1037 * 0.52321661
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69316 * 0.56156432
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24396 * 0.95134129
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2715 * 0.47034588
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97342 * 0.39836026
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53834 * 0.15687549
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58947 * 0.74329037
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66067 * 0.45435014
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47471 * 0.99659008
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30818 * 0.75305221
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2330 * 0.72423270
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30492 * 0.17716550
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26512 * 0.34811278
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35049 * 0.47707143
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5817 * 0.32329077
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68191 * 0.37123965
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80511 * 0.44811525
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93293 * 0.91665400
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46545 * 0.27770218
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60329 * 0.86663949
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31021 * 0.88368974
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77021 * 0.70562156
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15775 * 0.02351549
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4222 * 0.97599046
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86054 * 0.72411745
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95518 * 0.86736554
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89720 * 0.22078438
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28624 * 0.73620816
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79923 * 0.06683983
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61992 * 0.42914937
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69616 * 0.31049308
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27346 * 0.01010751
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58911 * 0.64051241
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61791 * 0.43885547
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53569 * 0.93186686
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98120 * 0.36925016
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16383 * 0.26798542
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 7295 * 0.60748687
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60405 * 0.58821201
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96288 * 0.23469775
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 59833 * 0.53801090
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 69217 * 0.58929220
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'defheolr').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0022():
    """Extended test 22 for federation."""
    x_0 = 81089 * 0.13123298
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87497 * 0.87428042
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76365 * 0.14248308
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13711 * 0.72440779
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2084 * 0.46909350
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40634 * 0.66832658
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26935 * 0.87359689
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39175 * 0.86658543
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61041 * 0.69593474
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70140 * 0.54703076
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64547 * 0.02290529
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85666 * 0.57135750
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81860 * 0.59307859
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60233 * 0.66071047
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32825 * 0.47864326
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89254 * 0.36424622
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48444 * 0.72386332
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8303 * 0.44458852
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25664 * 0.29274996
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32491 * 0.86632356
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14899 * 0.33026385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33140 * 0.52778247
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50690 * 0.55716797
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30642 * 0.15517420
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55729 * 0.82323047
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39289 * 0.26880027
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57581 * 0.43755015
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89817 * 0.63725429
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30210 * 0.40589622
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10144 * 0.63342413
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49593 * 0.63663613
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24763 * 0.06759914
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'ooztvwfz').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0023():
    """Extended test 23 for federation."""
    x_0 = 77046 * 0.54483966
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13660 * 0.76716627
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3895 * 0.62041838
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65158 * 0.25281367
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11104 * 0.83873561
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30332 * 0.28001787
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79045 * 0.55370046
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30168 * 0.30382103
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10025 * 0.17851222
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 596 * 0.34488333
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21083 * 0.37658662
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70209 * 0.36289902
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8643 * 0.55040695
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52694 * 0.02444798
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2143 * 0.19679669
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75635 * 0.74433256
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60433 * 0.32481807
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75236 * 0.05250262
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63712 * 0.81510147
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70819 * 0.39110083
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26030 * 0.53570224
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44670 * 0.37220790
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47074 * 0.93910104
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66790 * 0.66155689
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29067 * 0.40452817
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8603 * 0.27449418
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86637 * 0.82790923
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4379 * 0.72956122
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45127 * 0.43182288
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29129 * 0.70533232
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14536 * 0.69202862
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48160 * 0.90232059
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73787 * 0.13205270
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38927 * 0.12683339
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18389 * 0.08004299
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10087 * 0.95658986
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54801 * 0.20922707
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40341 * 0.99254799
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72207 * 0.76397378
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'rphinlhx').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0024():
    """Extended test 24 for federation."""
    x_0 = 72199 * 0.05907908
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48837 * 0.50923854
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73804 * 0.80408502
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77770 * 0.74062208
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76536 * 0.55896408
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84143 * 0.37178590
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49154 * 0.43941704
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80747 * 0.67962982
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47116 * 0.61089843
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42405 * 0.71575417
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25363 * 0.18520960
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56307 * 0.05035808
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57637 * 0.17142743
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75198 * 0.76678465
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81878 * 0.99997775
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39213 * 0.63867030
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75365 * 0.22522465
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83427 * 0.71381741
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79389 * 0.05244955
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64667 * 0.55379063
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23301 * 0.98457064
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29192 * 0.11812513
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79868 * 0.45537048
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37909 * 0.68088236
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16832 * 0.89661979
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17367 * 0.52479406
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5056 * 0.46672720
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8468 * 0.31529779
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88069 * 0.18510762
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91542 * 0.38223108
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97583 * 0.83580354
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11962 * 0.75493444
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44658 * 0.57629521
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60445 * 0.17746087
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89405 * 0.19511933
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76243 * 0.38026600
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12936 * 0.54662427
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17320 * 0.01814467
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81652 * 0.86452283
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62875 * 0.97008450
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3288 * 0.66335837
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25216 * 0.43650347
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65872 * 0.91603052
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'xymlcwif').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0025():
    """Extended test 25 for federation."""
    x_0 = 22988 * 0.38674457
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35528 * 0.32751748
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90591 * 0.47532211
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49817 * 0.19921959
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1968 * 0.34581362
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33218 * 0.56043697
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55947 * 0.33527141
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72519 * 0.83197542
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77292 * 0.69539466
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91148 * 0.14924539
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3023 * 0.42569418
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68736 * 0.94057846
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60083 * 0.22688136
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31646 * 0.93537370
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3106 * 0.66737498
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10056 * 0.08452766
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47824 * 0.69864653
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17601 * 0.05525521
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64012 * 0.88907592
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67784 * 0.41887969
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8877 * 0.51328520
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2877 * 0.13129355
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21171 * 0.23442619
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12145 * 0.70858238
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87362 * 0.08362294
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39139 * 0.53961359
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21342 * 0.72511963
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32919 * 0.79997512
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82179 * 0.88229372
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9454 * 0.12446079
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12728 * 0.59328821
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23172 * 0.00046064
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1146 * 0.90605159
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'jhcweytu').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0026():
    """Extended test 26 for federation."""
    x_0 = 43486 * 0.30855659
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79759 * 0.86451294
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97885 * 0.39387734
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89145 * 0.34952829
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92590 * 0.98252273
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71896 * 0.84011421
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69409 * 0.72331853
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80192 * 0.87754604
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52362 * 0.09116754
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3569 * 0.35997642
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29906 * 0.61632036
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24630 * 0.98898907
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67740 * 0.10708149
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48746 * 0.09449612
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6851 * 0.79907611
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89798 * 0.09102135
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95502 * 0.42698753
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87261 * 0.56717074
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5952 * 0.65606438
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36716 * 0.44558878
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18154 * 0.91543084
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19666 * 0.38298878
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41028 * 0.33252076
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93905 * 0.53985715
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81942 * 0.41943317
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95718 * 0.62587630
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65583 * 0.28510583
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51410 * 0.58083681
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46588 * 0.94634447
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9698 * 0.89071972
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16354 * 0.61239990
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15694 * 0.23192477
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69739 * 0.74320989
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6970 * 0.39544293
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18339 * 0.60098283
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52500 * 0.30360106
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4166 * 0.54395877
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39559 * 0.86102027
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'nsdlmecp').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0027():
    """Extended test 27 for federation."""
    x_0 = 12734 * 0.84604135
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86660 * 0.72991808
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29342 * 0.08050044
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5904 * 0.46937072
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41201 * 0.15586039
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92827 * 0.54056342
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50408 * 0.12554576
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87211 * 0.96524371
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24601 * 0.30130075
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98120 * 0.48662651
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50819 * 0.54568328
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59703 * 0.39933185
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70353 * 0.43190899
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3793 * 0.92747873
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91758 * 0.83699976
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68860 * 0.84366458
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10466 * 0.79416034
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82964 * 0.35759077
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2425 * 0.25195257
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84786 * 0.50202842
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1114 * 0.21554238
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82080 * 0.47501084
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57727 * 0.57113831
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80369 * 0.41186945
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'szuludzh').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0028():
    """Extended test 28 for federation."""
    x_0 = 60966 * 0.80049297
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2332 * 0.08280209
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37658 * 0.21596745
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86370 * 0.58637530
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80757 * 0.72724781
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74377 * 0.88948236
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86921 * 0.66273031
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73881 * 0.29363292
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84839 * 0.65583684
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30915 * 0.69898982
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83973 * 0.20407999
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3960 * 0.27509196
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9484 * 0.98216315
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20249 * 0.56928647
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34378 * 0.83989245
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81172 * 0.93293529
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95517 * 0.16869112
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74396 * 0.72391692
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80086 * 0.12637079
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47201 * 0.24558732
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26931 * 0.48840967
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34936 * 0.68220412
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3839 * 0.80112430
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77705 * 0.27557602
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96978 * 0.88827477
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79617 * 0.80041214
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15962 * 0.81987990
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6192 * 0.73560362
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97849 * 0.97679650
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38180 * 0.21234753
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79933 * 0.39500135
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42301 * 0.76861439
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4586 * 0.43184366
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62301 * 0.56293336
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'nlswqcmj').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0029():
    """Extended test 29 for federation."""
    x_0 = 25438 * 0.48471947
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42234 * 0.95443528
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7711 * 0.68093482
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42179 * 0.99370622
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17214 * 0.63861519
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9016 * 0.86926691
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57935 * 0.03343699
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31060 * 0.47475761
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40319 * 0.70129536
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 752 * 0.99070316
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2636 * 0.94529837
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73330 * 0.93595064
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59438 * 0.68333267
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14493 * 0.77909082
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21469 * 0.12625352
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74444 * 0.03026539
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68641 * 0.09306210
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8622 * 0.35692135
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97974 * 0.44044528
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55477 * 0.48422494
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'kuileygt').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0030():
    """Extended test 30 for federation."""
    x_0 = 19059 * 0.25195594
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10478 * 0.86793014
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2014 * 0.37880735
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19131 * 0.56880608
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93669 * 0.12420274
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91900 * 0.12322776
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70991 * 0.58598634
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73198 * 0.39895051
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41366 * 0.32607402
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28367 * 0.21004761
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58756 * 0.76498204
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17787 * 0.51744286
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33262 * 0.09259821
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9223 * 0.33332229
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8705 * 0.56675448
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20653 * 0.31088642
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42053 * 0.65013934
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62653 * 0.88096631
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26777 * 0.44579517
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81467 * 0.82924555
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66351 * 0.03714491
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33731 * 0.35800217
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'tmgewxoc').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0031():
    """Extended test 31 for federation."""
    x_0 = 13655 * 0.04180523
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91111 * 0.81756461
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78090 * 0.72030184
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46593 * 0.36713715
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17735 * 0.11376787
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81578 * 0.60980054
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40056 * 0.07484636
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61389 * 0.54270893
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78893 * 0.90152398
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25041 * 0.85817580
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41664 * 0.28742692
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1398 * 0.33925051
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45282 * 0.20252985
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12171 * 0.69567470
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28799 * 0.98111273
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60375 * 0.67775513
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24276 * 0.29047712
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32346 * 0.49062838
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92730 * 0.31493647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63656 * 0.16707040
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52649 * 0.92729990
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18394 * 0.29063613
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8799 * 0.59266362
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72268 * 0.84083250
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77458 * 0.58317857
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36689 * 0.07790370
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 812 * 0.56353677
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15879 * 0.04145742
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86377 * 0.55206475
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65714 * 0.10802295
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61367 * 0.25982335
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11487 * 0.02754534
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33329 * 0.71468078
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10929 * 0.69045645
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8133 * 0.52279879
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26089 * 0.93989525
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61896 * 0.72190739
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94021 * 0.60862805
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92741 * 0.58551233
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 463 * 0.38145421
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 58644 * 0.66764102
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71889 * 0.53506469
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 7511 * 0.23137034
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84999 * 0.81576905
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 19665 * 0.34229271
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 21924 * 0.71018498
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'wtnwnpcp').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0032():
    """Extended test 32 for federation."""
    x_0 = 7567 * 0.28837219
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65378 * 0.41156599
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41508 * 0.28246977
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8605 * 0.82909034
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17863 * 0.87764349
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81787 * 0.73559930
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34377 * 0.51223524
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18266 * 0.07919305
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60666 * 0.73490071
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76862 * 0.77976071
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38010 * 0.33267631
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14004 * 0.69286673
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25961 * 0.12009146
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83456 * 0.58411081
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97101 * 0.23847591
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56630 * 0.41583686
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60806 * 0.28894800
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87002 * 0.98200739
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 565 * 0.29594835
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83616 * 0.78816168
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85447 * 0.26609276
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96537 * 0.93113194
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'sjenpdeu').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0033():
    """Extended test 33 for federation."""
    x_0 = 82834 * 0.76450310
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14504 * 0.53881658
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96026 * 0.00610604
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83584 * 0.61179804
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13475 * 0.00818230
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92473 * 0.92559140
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58556 * 0.10933040
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61940 * 0.92944826
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47679 * 0.30495346
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50250 * 0.23978414
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13276 * 0.19347054
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4114 * 0.44214899
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56073 * 0.81382896
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88227 * 0.21940534
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18796 * 0.13145703
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99593 * 0.50039392
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33895 * 0.65028599
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78692 * 0.39687288
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63855 * 0.23713103
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80751 * 0.48342128
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27778 * 0.38564712
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62344 * 0.86932941
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37661 * 0.02566000
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24359 * 0.55086385
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61135 * 0.36941920
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47941 * 0.40262215
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15359 * 0.53805260
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5124 * 0.83662518
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89574 * 0.48054965
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94512 * 0.68721115
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54402 * 0.82824287
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82002 * 0.41319711
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30554 * 0.60784901
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41387 * 0.20546668
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59327 * 0.51881677
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49324 * 0.85576530
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76772 * 0.93980112
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31639 * 0.73586594
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91413 * 0.11808304
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14384 * 0.86932077
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 14648 * 0.73761051
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81771 * 0.50533050
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 94259 * 0.32281524
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99298 * 0.57902976
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89000 * 0.63976000
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 20422 * 0.21065372
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 97564 * 0.76209088
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 17837 * 0.82227264
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'faspiznb').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0034():
    """Extended test 34 for federation."""
    x_0 = 87390 * 0.54390040
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98370 * 0.65356365
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20835 * 0.78492728
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65012 * 0.79713908
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43793 * 0.22534176
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83798 * 0.63192557
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10265 * 0.80080798
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81145 * 0.01564989
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35088 * 0.25254910
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84443 * 0.67625605
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63245 * 0.46840797
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6681 * 0.99929153
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34211 * 0.05908660
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30409 * 0.76640741
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99140 * 0.56647691
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85721 * 0.13731695
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2345 * 0.76583212
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76114 * 0.74627370
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60174 * 0.61555768
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47307 * 0.89103947
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78227 * 0.28302763
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16709 * 0.62761046
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25722 * 0.59199620
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14913 * 0.70189532
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84812 * 0.16154960
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6664 * 0.06009273
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27577 * 0.30430401
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8807 * 0.55523441
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8932 * 0.04634714
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50559 * 0.16038394
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'vjotktdu').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0035():
    """Extended test 35 for federation."""
    x_0 = 21357 * 0.20701909
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46849 * 0.75373428
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69709 * 0.17528862
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94190 * 0.31129943
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36956 * 0.43370049
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29956 * 0.69600321
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23273 * 0.19598221
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68804 * 0.58644107
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5563 * 0.64434576
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75749 * 0.05442824
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25774 * 0.77454483
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74009 * 0.23858640
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12000 * 0.04657926
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37686 * 0.53959371
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69526 * 0.50472841
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17585 * 0.18204563
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62342 * 0.15159018
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79073 * 0.44938364
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47575 * 0.90544598
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35420 * 0.10755297
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52285 * 0.40849550
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 472 * 0.28029104
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73425 * 0.42464576
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55764 * 0.69914961
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37342 * 0.52122586
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53687 * 0.36515240
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9003 * 0.10699739
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26471 * 0.73961963
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46128 * 0.80724703
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1144 * 0.91347946
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6636 * 0.29888077
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32559 * 0.48974539
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71210 * 0.14898972
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61155 * 0.27087556
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5972 * 0.75763432
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58468 * 0.58633310
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4624 * 0.81693399
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97697 * 0.43660794
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47495 * 0.99146868
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67488 * 0.07375414
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83459 * 0.63764287
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15069 * 0.57092071
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 27335 * 0.22182547
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'nzarpqco').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0036():
    """Extended test 36 for federation."""
    x_0 = 31449 * 0.24658724
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64087 * 0.55613518
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58951 * 0.68974930
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79225 * 0.49126802
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38147 * 0.55522529
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27722 * 0.61481618
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8511 * 0.62789165
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87606 * 0.73555990
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6259 * 0.27439628
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33748 * 0.82231433
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80591 * 0.49549881
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46614 * 0.75387438
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43029 * 0.37536847
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83709 * 0.88675390
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89955 * 0.42058923
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78616 * 0.33475628
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78673 * 0.04139829
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65494 * 0.87902933
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62504 * 0.56193523
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29807 * 0.89202873
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57531 * 0.76802469
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3006 * 0.39393647
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34809 * 0.14288060
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65978 * 0.94716592
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22596 * 0.10855969
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33120 * 0.57143308
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59180 * 0.61352028
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35016 * 0.22204660
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40601 * 0.61290435
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60191 * 0.36305610
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52244 * 0.40825000
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76925 * 0.14870351
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2822 * 0.63851709
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64266 * 0.86673226
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43128 * 0.64030159
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21018 * 0.11800765
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13641 * 0.36906933
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'nfhonzxf').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0037():
    """Extended test 37 for federation."""
    x_0 = 10549 * 0.17413559
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33454 * 0.17800953
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1069 * 0.65967765
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10313 * 0.47546559
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64161 * 0.62358339
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83670 * 0.37822664
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59345 * 0.41559366
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38040 * 0.52356587
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19356 * 0.85792488
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70783 * 0.31493252
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97170 * 0.21608496
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78962 * 0.37939265
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87714 * 0.75168134
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46409 * 0.84588101
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4742 * 0.45193434
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9776 * 0.91543324
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52827 * 0.06092852
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70920 * 0.19438990
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94331 * 0.79231853
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94485 * 0.20250246
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27432 * 0.60316566
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2023 * 0.19555027
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91621 * 0.92487146
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33431 * 0.25931891
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17413 * 0.30020215
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11651 * 0.78057751
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55652 * 0.66849464
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99627 * 0.75138073
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9611 * 0.24465215
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13566 * 0.48217862
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18567 * 0.05879008
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84820 * 0.19890251
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8040 * 0.40982753
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93800 * 0.48623351
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63876 * 0.82824338
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ylfxictm').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0038():
    """Extended test 38 for federation."""
    x_0 = 7804 * 0.44034691
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7409 * 0.14813230
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5713 * 0.02708076
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36372 * 0.26134814
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46053 * 0.61912614
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55052 * 0.93227629
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54464 * 0.02728863
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1242 * 0.17676580
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38404 * 0.59814301
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61351 * 0.48156813
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66056 * 0.77904175
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 519 * 0.06761195
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75688 * 0.76385238
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3557 * 0.27200198
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5756 * 0.30710106
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60209 * 0.44687444
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73310 * 0.06319815
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20647 * 0.88971348
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48925 * 0.33376093
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59466 * 0.83718387
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21955 * 0.28670553
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42924 * 0.87542976
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45355 * 0.14142416
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82973 * 0.06672386
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94448 * 0.58098143
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30194 * 0.28674003
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49171 * 0.65347598
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8511 * 0.06943417
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43360 * 0.32861450
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45714 * 0.10753701
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39267 * 0.31066877
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4587 * 0.47571168
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74714 * 0.15715820
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6950 * 0.13054701
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1705 * 0.63271489
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67084 * 0.55334511
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69863 * 0.75276190
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5375 * 0.85698085
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71644 * 0.02217002
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42031 * 0.38276098
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'kbbckopb').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0039():
    """Extended test 39 for federation."""
    x_0 = 92914 * 0.42852899
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75910 * 0.58801826
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11713 * 0.41047169
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9006 * 0.45754451
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42906 * 0.20412291
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83333 * 0.51571157
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65140 * 0.18030709
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99930 * 0.46792538
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42653 * 0.21549966
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6029 * 0.01542799
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84768 * 0.62802704
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45019 * 0.86988369
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15936 * 0.09820178
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8093 * 0.04610730
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53876 * 0.51639243
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33465 * 0.45924005
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13677 * 0.03837816
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86437 * 0.82100141
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30367 * 0.29921561
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73866 * 0.82335407
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10309 * 0.15869537
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70419 * 0.36157319
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62133 * 0.02589646
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57628 * 0.46226048
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23087 * 0.23327790
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90263 * 0.58356200
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42355 * 0.44098839
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53796 * 0.19930377
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96766 * 0.92233196
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88594 * 0.52634487
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3207 * 0.16328262
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4736 * 0.56179833
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85069 * 0.15192788
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57819 * 0.78964921
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44194 * 0.56841728
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6806 * 0.96577943
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79959 * 0.38372175
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 79380 * 0.85186752
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91568 * 0.87174243
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38873 * 0.43130552
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4901 * 0.15817151
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 55005 * 0.58559649
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 50033 * 0.34489296
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 25536 * 0.68688030
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 93189 * 0.33236831
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 75745 * 0.93400633
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 40538 * 0.88617105
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 46694 * 0.65987594
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'memhrsfu').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0040():
    """Extended test 40 for federation."""
    x_0 = 17851 * 0.44490062
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11642 * 0.49919648
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11849 * 0.43168844
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85221 * 0.64717734
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10532 * 0.53724768
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2294 * 0.00183862
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63500 * 0.96878200
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66565 * 0.56504039
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21961 * 0.84563081
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56110 * 0.56614301
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43753 * 0.39902607
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73703 * 0.16875129
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18696 * 0.52675316
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93963 * 0.38157878
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88068 * 0.21850139
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84646 * 0.71867085
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28941 * 0.22646141
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19305 * 0.17415329
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85945 * 0.67599487
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18415 * 0.76311611
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39579 * 0.67744013
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38032 * 0.72005746
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30783 * 0.27526954
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18515 * 0.16989743
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53495 * 0.41220791
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21594 * 0.52009042
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7897 * 0.36237426
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'miywgsve').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0041():
    """Extended test 41 for federation."""
    x_0 = 29100 * 0.73101642
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45236 * 0.82804535
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33143 * 0.93396572
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85672 * 0.19880173
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61156 * 0.50049472
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74097 * 0.67670603
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85697 * 0.36634430
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52857 * 0.19309883
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28506 * 0.46041701
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26888 * 0.94849893
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64952 * 0.47428747
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69679 * 0.35714277
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22303 * 0.60772115
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3937 * 0.17522789
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9492 * 0.34225439
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79874 * 0.55666264
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3383 * 0.64319597
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53714 * 0.84930532
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98424 * 0.01040789
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65370 * 0.38386966
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8771 * 0.61863187
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75608 * 0.90803827
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77300 * 0.84792603
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58318 * 0.67492514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47169 * 0.19026402
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'jbazepdl').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0042():
    """Extended test 42 for federation."""
    x_0 = 51843 * 0.21300140
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43212 * 0.36365012
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6608 * 0.09284738
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42405 * 0.26030491
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1466 * 0.60261920
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52324 * 0.56072699
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14166 * 0.64993642
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35438 * 0.95669091
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18741 * 0.80667132
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4529 * 0.18396026
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88246 * 0.28429539
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70719 * 0.59094831
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46919 * 0.64221741
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68334 * 0.84535345
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69804 * 0.54932845
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99959 * 0.72075159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75703 * 0.74712140
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57037 * 0.99902285
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60544 * 0.78595617
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30168 * 0.57541877
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93071 * 0.82871819
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26373 * 0.25481621
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44261 * 0.66349582
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78584 * 0.37747304
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49907 * 0.48822404
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14671 * 0.82042185
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76550 * 0.56084354
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62584 * 0.70214224
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82996 * 0.02741374
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49389 * 0.30311669
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11303 * 0.38782494
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94883 * 0.46273670
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27643 * 0.93423643
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54565 * 0.23976347
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89000 * 0.26965858
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70175 * 0.18375240
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31841 * 0.94773677
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12128 * 0.88014265
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30730 * 0.09642650
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93364 * 0.04456060
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'pjrmpiyb').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0043():
    """Extended test 43 for federation."""
    x_0 = 3531 * 0.51591223
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40227 * 0.97837349
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96770 * 0.98427821
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27799 * 0.67037437
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95925 * 0.77970669
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2761 * 0.61695800
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12387 * 0.28139319
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55993 * 0.66268179
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32190 * 0.39891095
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74444 * 0.29408168
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27748 * 0.52018721
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2189 * 0.16372299
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26654 * 0.88566970
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73623 * 0.11958006
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29135 * 0.16031109
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77128 * 0.23205020
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16352 * 0.68930805
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15113 * 0.97927891
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48344 * 0.92725045
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16801 * 0.66207136
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17698 * 0.68392537
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78565 * 0.39491411
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87215 * 0.55279896
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4934 * 0.32587393
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75184 * 0.43909187
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34407 * 0.70812598
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81874 * 0.52960615
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65035 * 0.86091005
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7606 * 0.04375698
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41036 * 0.42538472
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89676 * 0.46792094
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9093 * 0.39853515
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33577 * 0.82402761
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50527 * 0.62938164
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25925 * 0.00277787
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15890 * 0.19017279
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10396 * 0.77249104
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34860 * 0.27271064
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67806 * 0.27008759
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13376 * 0.47591783
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2028 * 0.27456074
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6160 * 0.39528103
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57836 * 0.94123106
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'vpfnkixu').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0044():
    """Extended test 44 for federation."""
    x_0 = 19808 * 0.95009687
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93243 * 0.92554322
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33544 * 0.68714320
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16957 * 0.67589202
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44038 * 0.52238081
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87016 * 0.09574544
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1829 * 0.01517139
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9864 * 0.42509865
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54682 * 0.95498253
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99522 * 0.40933154
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38207 * 0.24237087
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46659 * 0.53070137
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53824 * 0.03239268
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3954 * 0.51804746
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36874 * 0.43400015
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15394 * 0.37309777
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52673 * 0.84056993
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4036 * 0.93183244
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38206 * 0.45963972
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70899 * 0.23278903
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66756 * 0.90797356
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46885 * 0.92293987
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23811 * 0.54545520
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71666 * 0.82055860
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65847 * 0.95980146
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52728 * 0.05488848
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38010 * 0.17232824
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32055 * 0.76080408
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61169 * 0.87865175
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10887 * 0.88715651
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74861 * 0.07016796
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44087 * 0.67273779
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'favqyzxf').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0045():
    """Extended test 45 for federation."""
    x_0 = 28877 * 0.96477782
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64814 * 0.07921957
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19286 * 0.95726078
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59086 * 0.22846759
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38820 * 0.26819847
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91943 * 0.16058030
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2928 * 0.76870683
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50364 * 0.23976481
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95499 * 0.32749919
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6586 * 0.13041732
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79828 * 0.94071204
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25926 * 0.55370582
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30928 * 0.67339906
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53442 * 0.91572176
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51516 * 0.53955973
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16040 * 0.66580991
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97301 * 0.34017013
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26049 * 0.11736422
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86072 * 0.82390092
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93125 * 0.23315757
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59812 * 0.32395139
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45373 * 0.85673758
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88355 * 0.32311358
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57058 * 0.94029855
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21536 * 0.78556375
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81256 * 0.25451548
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71382 * 0.44197124
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95941 * 0.31804675
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34827 * 0.72523681
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79008 * 0.69041081
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88760 * 0.20078403
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 88122 * 0.38998381
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56324 * 0.30486029
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45157 * 0.20691253
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19129 * 0.44976285
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74744 * 0.08819409
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10119 * 0.56710588
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'hgjrmxpx').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0046():
    """Extended test 46 for federation."""
    x_0 = 77510 * 0.05345637
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38749 * 0.44974429
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90616 * 0.41091833
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74106 * 0.17254077
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22909 * 0.96863535
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25590 * 0.02430898
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77515 * 0.79122997
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97143 * 0.91295352
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38114 * 0.78336142
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64888 * 0.42546702
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2595 * 0.33284050
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19244 * 0.62966945
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76037 * 0.55997957
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80824 * 0.12961291
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55404 * 0.66535897
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63819 * 0.39168360
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14937 * 0.26844350
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46018 * 0.26800488
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42708 * 0.06682602
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68587 * 0.51157775
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50082 * 0.57000874
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51268 * 0.14134019
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93185 * 0.95445548
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'fkejzpky').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0047():
    """Extended test 47 for federation."""
    x_0 = 42783 * 0.79666691
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75447 * 0.26110245
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70750 * 0.33271810
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73027 * 0.28334284
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8647 * 0.05202724
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29326 * 0.83799821
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84336 * 0.84474421
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79432 * 0.58111707
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67690 * 0.20617022
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61006 * 0.35016502
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5390 * 0.15128883
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1139 * 0.38992062
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46234 * 0.77609571
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32497 * 0.88953008
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8961 * 0.39549936
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41852 * 0.75205035
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46574 * 0.13281962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65534 * 0.38356436
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65547 * 0.39739800
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35097 * 0.79812008
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38025 * 0.71993782
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12916 * 0.00870033
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62244 * 0.74095980
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92920 * 0.75739900
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27269 * 0.45698147
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85165 * 0.26120549
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81249 * 0.73210037
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18293 * 0.83036145
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77116 * 0.43649753
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19325 * 0.55642272
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21795 * 0.64831114
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55907 * 0.49436830
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79021 * 0.43331973
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49640 * 0.90573950
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25750 * 0.97493414
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24045 * 0.94880353
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51538 * 0.33915251
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9695 * 0.09358323
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56643 * 0.78186020
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1593 * 0.50741155
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 58359 * 0.89869374
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59808 * 0.60548949
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29401 * 0.52618693
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'lfoyyiyj').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0048():
    """Extended test 48 for federation."""
    x_0 = 47389 * 0.80343875
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76276 * 0.05394722
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70343 * 0.53470040
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76146 * 0.73895707
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99869 * 0.45082045
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6528 * 0.16250125
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74744 * 0.28595296
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89866 * 0.67527858
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4500 * 0.06822164
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50369 * 0.52494341
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87154 * 0.78515294
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56365 * 0.39107946
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57775 * 0.61205744
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45072 * 0.36380010
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67978 * 0.74984124
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58074 * 0.35270726
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5210 * 0.00824519
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84758 * 0.04683031
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17691 * 0.37659450
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25225 * 0.86583244
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12724 * 0.80071137
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76845 * 0.75479338
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31974 * 0.57248543
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79976 * 0.64147104
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45384 * 0.41995658
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84411 * 0.83879696
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89519 * 0.66725346
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78886 * 0.78196497
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43228 * 0.67835776
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14877 * 0.97414011
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63985 * 0.39428683
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92677 * 0.00568715
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85814 * 0.77155284
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'exdhijlf').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0049():
    """Extended test 49 for federation."""
    x_0 = 28178 * 0.83904824
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26022 * 0.81758681
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24990 * 0.55880267
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78174 * 0.14869890
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27460 * 0.41994647
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81474 * 0.02431268
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25797 * 0.18899060
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13774 * 0.18536687
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13270 * 0.40147029
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60866 * 0.28987330
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2663 * 0.50783759
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13533 * 0.44620124
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46148 * 0.45270039
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3353 * 0.95638667
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52976 * 0.28150964
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15264 * 0.80474686
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78257 * 0.20408600
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73417 * 0.59286730
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97122 * 0.32934788
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68425 * 0.20698675
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87047 * 0.09485806
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56935 * 0.66788483
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75550 * 0.21368571
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40336 * 0.13564654
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60109 * 0.46107783
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88423 * 0.29064911
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11351 * 0.20872355
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23556 * 0.57057769
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99463 * 0.69826813
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76977 * 0.79650864
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90009 * 0.46804949
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43375 * 0.33435771
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75610 * 0.87983845
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83320 * 0.67169929
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21450 * 0.21034960
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7138 * 0.16360718
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13231 * 0.69500464
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78988 * 0.48625760
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19883 * 0.51877404
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47491 * 0.58555596
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99357 * 0.47318081
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71380 * 0.90074838
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93504 * 0.68838041
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 65522 * 0.86443656
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 90769 * 0.89149740
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'vmqtkbeb').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0050():
    """Extended test 50 for federation."""
    x_0 = 84765 * 0.86262433
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19124 * 0.27372699
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84227 * 0.13640010
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90844 * 0.76792209
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24718 * 0.41562215
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5712 * 0.89273969
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84394 * 0.46355056
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70882 * 0.88775051
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34178 * 0.30990241
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41383 * 0.20011507
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26698 * 0.13676987
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61526 * 0.63251929
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11960 * 0.46167814
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73032 * 0.92584242
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66454 * 0.36133507
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31636 * 0.43169415
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43772 * 0.06763939
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58720 * 0.61064582
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7283 * 0.33679567
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23220 * 0.24640876
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3033 * 0.68623246
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53906 * 0.23634791
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93662 * 0.36164572
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73739 * 0.41481248
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78366 * 0.65866452
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69961 * 0.63403802
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52840 * 0.62538088
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26949 * 0.74805831
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74519 * 0.39951349
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32854 * 0.31808853
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33766 * 0.23645278
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32384 * 0.91502516
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26598 * 0.93692156
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35921 * 0.50672001
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32117 * 0.84612404
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54232 * 0.82618891
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90457 * 0.24443639
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31383 * 0.75949195
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64390 * 0.94929592
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64527 * 0.31589955
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 12637 * 0.37941217
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52096 * 0.56482666
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 54360 * 0.49264553
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 35061 * 0.49828934
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 46075 * 0.14539513
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10240 * 0.49198750
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 83115 * 0.45422588
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ndazrcmk').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0051():
    """Extended test 51 for federation."""
    x_0 = 39106 * 0.10936667
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7670 * 0.56247842
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26090 * 0.24762672
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30885 * 0.59256962
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63729 * 0.92037424
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14590 * 0.04340091
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97818 * 0.17362567
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12621 * 0.70742528
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89244 * 0.83605786
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72494 * 0.94774889
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51384 * 0.42766216
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65486 * 0.80269179
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54828 * 0.84295635
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69212 * 0.79125444
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60781 * 0.80453405
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30111 * 0.08426654
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34921 * 0.12032470
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42295 * 0.86910994
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73859 * 0.09193358
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75421 * 0.57161020
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80543 * 0.49919460
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64869 * 0.77165058
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15368 * 0.67861702
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88525 * 0.69251670
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48220 * 0.31735576
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63567 * 0.30682007
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94109 * 0.56928673
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60121 * 0.65344690
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8438 * 0.38234655
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18471 * 0.03119091
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80888 * 0.70293680
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26082 * 0.43850283
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36225 * 0.78140871
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86061 * 0.64485389
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9549 * 0.67630734
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47390 * 0.12441524
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21069 * 0.99695520
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2495 * 0.48875935
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59158 * 0.79960293
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'qnsnureh').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0052():
    """Extended test 52 for federation."""
    x_0 = 17341 * 0.81419192
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51283 * 0.67117380
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27840 * 0.17616079
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26272 * 0.04909082
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87644 * 0.22403208
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44084 * 0.46704408
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29677 * 0.96942371
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27266 * 0.16764559
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82645 * 0.37677023
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22496 * 0.94928380
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26520 * 0.59421768
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44262 * 0.74469835
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60815 * 0.86657711
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69342 * 0.76208523
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48882 * 0.01654302
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1683 * 0.41770028
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61229 * 0.31391600
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73521 * 0.74013076
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91820 * 0.43366588
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49140 * 0.08384712
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31335 * 0.18445065
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62443 * 0.86300183
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50830 * 0.68745105
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60995 * 0.02764310
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61406 * 0.24718059
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65724 * 0.82048665
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'bfvbbxtr').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0053():
    """Extended test 53 for federation."""
    x_0 = 10818 * 0.43665608
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99575 * 0.36935352
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12420 * 0.89775838
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20198 * 0.55591122
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16677 * 0.60622216
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37221 * 0.06572897
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47918 * 0.15972262
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39630 * 0.93960748
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24696 * 0.79412551
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66024 * 0.21583087
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56685 * 0.81338616
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76945 * 0.38449786
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74613 * 0.70754092
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59165 * 0.90800093
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62571 * 0.94139394
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14499 * 0.86205317
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29653 * 0.56643878
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47744 * 0.46240945
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76097 * 0.09377993
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19136 * 0.14821771
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98678 * 0.12077913
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56110 * 0.46368005
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93690 * 0.16325271
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35211 * 0.44722203
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64592 * 0.08998254
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91384 * 0.80626478
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1735 * 0.40768632
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71848 * 0.99059474
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77018 * 0.60629000
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51912 * 0.87526579
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5306 * 0.53346392
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18705 * 0.71704148
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24072 * 0.45630156
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9154 * 0.24626800
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7223 * 0.80317536
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90402 * 0.25858086
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33533 * 0.44926734
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61361 * 0.82111337
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 89173 * 0.37472212
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86186 * 0.59426238
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78756 * 0.22347770
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15186 * 0.86555361
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71842 * 0.72656376
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 95045 * 0.37159518
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 85212 * 0.64347598
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 34178 * 0.82812502
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 66914 * 0.95042177
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'yggkwslz').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0054():
    """Extended test 54 for federation."""
    x_0 = 68849 * 0.80848649
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98475 * 0.93604805
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63705 * 0.49152978
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70867 * 0.36149925
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16045 * 0.21722027
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70730 * 0.32895583
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 314 * 0.13917835
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24029 * 0.21175674
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52106 * 0.49516216
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46611 * 0.31129770
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20558 * 0.05344643
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74676 * 0.90323574
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63786 * 0.28585909
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29524 * 0.59074889
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21649 * 0.18102000
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49211 * 0.38922127
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12352 * 0.86176694
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73401 * 0.40065238
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60309 * 0.26510354
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70641 * 0.66983537
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84971 * 0.02493239
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91043 * 0.84757812
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14697 * 0.33010895
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25329 * 0.79811874
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83643 * 0.43578603
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'kdyeelxx').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0055():
    """Extended test 55 for federation."""
    x_0 = 34127 * 0.09678726
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62248 * 0.18589716
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5148 * 0.94366684
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95446 * 0.09019684
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52383 * 0.80149352
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33890 * 0.53252871
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8471 * 0.29795097
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15335 * 0.02705917
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6107 * 0.27324528
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58875 * 0.95196851
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8918 * 0.67829407
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46149 * 0.05389093
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10922 * 0.47980113
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48069 * 0.92817462
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31342 * 0.38238810
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29124 * 0.38408981
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23365 * 0.62614144
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56548 * 0.25131838
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62002 * 0.69854755
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9851 * 0.99904471
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83684 * 0.09857355
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70992 * 0.74066971
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48867 * 0.60190996
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31973 * 0.69935624
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36668 * 0.97335035
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69368 * 0.02714156
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66729 * 0.92507599
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85016 * 0.23142740
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24560 * 0.29039411
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89711 * 0.75517643
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31331 * 0.52466775
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97618 * 0.76433444
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76211 * 0.74626499
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88880 * 0.33246787
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14942 * 0.84642930
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10630 * 0.86258351
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75669 * 0.82646104
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81016 * 0.13704375
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56774 * 0.34860486
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70511 * 0.02183655
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27582 * 0.45211408
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20626 * 0.10672529
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15855 * 0.49687989
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ullwpqmf').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0056():
    """Extended test 56 for federation."""
    x_0 = 31457 * 0.70863399
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5855 * 0.39059592
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62120 * 0.09137098
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97884 * 0.19216158
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44149 * 0.32470978
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24308 * 0.09396349
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34328 * 0.02430531
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91 * 0.03902845
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85872 * 0.25629747
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65817 * 0.28236886
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11921 * 0.39422047
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60526 * 0.84651646
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36927 * 0.17238071
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53836 * 0.33429946
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48511 * 0.84081140
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19244 * 0.84297693
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10565 * 0.65302247
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90963 * 0.52438351
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13107 * 0.56769046
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95157 * 0.21741964
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98808 * 0.84753267
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64989 * 0.24973990
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67038 * 0.11730068
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24664 * 0.79210261
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45036 * 0.07393743
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63665 * 0.37580863
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33654 * 0.74102751
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41314 * 0.07640501
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30348 * 0.74370363
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60862 * 0.85908874
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93879 * 0.16588483
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37728 * 0.30161697
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72415 * 0.41765186
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74949 * 0.44127890
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69828 * 0.99917283
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96772 * 0.89100675
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35315 * 0.25340930
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56631 * 0.88342236
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35945 * 0.07607143
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11859 * 0.53429053
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62707 * 0.38760405
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84807 * 0.66957761
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36977 * 0.76889188
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 78672 * 0.09753504
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 46822 * 0.95315606
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 24578 * 0.59909892
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'vqmormev').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0057():
    """Extended test 57 for federation."""
    x_0 = 89232 * 0.96159302
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10973 * 0.95082869
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97221 * 0.18938035
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15771 * 0.02359401
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47017 * 0.01888338
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25739 * 0.05906682
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53076 * 0.82977000
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53282 * 0.69571166
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22482 * 0.81984771
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69387 * 0.25829505
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61021 * 0.79835221
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5524 * 0.74084997
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98413 * 0.56390359
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46426 * 0.98361851
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72593 * 0.44511998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11811 * 0.87125836
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51109 * 0.78838216
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48928 * 0.65749076
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34460 * 0.26691837
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34181 * 0.54554494
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94153 * 0.48160912
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29626 * 0.47236341
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79171 * 0.36208284
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10588 * 0.32602720
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82621 * 0.38739456
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41769 * 0.45888288
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75115 * 0.95810104
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55035 * 0.73243680
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24006 * 0.97106295
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84677 * 0.70187889
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95949 * 0.72651975
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22320 * 0.33606692
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14043 * 0.43023019
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48699 * 0.08676838
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38762 * 0.77038739
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21032 * 0.23097738
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30606 * 0.89124169
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27367 * 0.65160813
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 226 * 0.51813680
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11406 * 0.42100429
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'hsjbhned').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0058():
    """Extended test 58 for federation."""
    x_0 = 85259 * 0.60948256
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88731 * 0.77065963
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20811 * 0.47060405
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94664 * 0.32956746
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21920 * 0.32015812
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82482 * 0.55147269
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19009 * 0.37840699
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29766 * 0.35825768
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22060 * 0.74746028
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5889 * 0.53009207
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2265 * 0.20233249
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58252 * 0.36163939
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16125 * 0.64010448
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66044 * 0.72732102
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48055 * 0.09121631
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76913 * 0.66592277
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61873 * 0.71705981
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85780 * 0.81900787
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49057 * 0.89026977
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11700 * 0.83586663
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96652 * 0.64273500
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64330 * 0.05965038
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93087 * 0.44471529
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61954 * 0.37471181
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25532 * 0.43010002
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89065 * 0.41469922
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93816 * 0.53314595
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31214 * 0.56082439
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65207 * 0.18520849
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44819 * 0.94510023
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9773 * 0.40436349
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25500 * 0.47228715
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'vnatsxkk').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0059():
    """Extended test 59 for federation."""
    x_0 = 8846 * 0.10110870
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91433 * 0.44559777
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69499 * 0.76859063
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9037 * 0.46508803
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81956 * 0.06222214
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92762 * 0.57735371
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16582 * 0.74724139
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34678 * 0.98335886
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81810 * 0.96579262
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46951 * 0.16201723
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24751 * 0.02674786
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85181 * 0.04206418
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83956 * 0.48546437
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59799 * 0.85576585
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41723 * 0.40854750
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14008 * 0.55021293
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41382 * 0.41102223
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15151 * 0.16861417
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17098 * 0.25081354
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87586 * 0.07446527
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2940 * 0.80063031
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89601 * 0.01105155
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23969 * 0.26203201
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65591 * 0.23492255
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63397 * 0.50931759
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43589 * 0.04285906
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37995 * 0.86891121
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32166 * 0.84190328
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60361 * 0.14945975
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73349 * 0.94058094
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65699 * 0.11027235
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'dizgcttp').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0060():
    """Extended test 60 for federation."""
    x_0 = 46232 * 0.83886101
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33656 * 0.67128320
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94507 * 0.47804734
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18909 * 0.14572796
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61292 * 0.53426192
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59405 * 0.97905031
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97205 * 0.46112891
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93696 * 0.94133584
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83688 * 0.23957273
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39316 * 0.27968262
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61735 * 0.46629943
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53508 * 0.95186980
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46321 * 0.33943435
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38023 * 0.16537364
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91310 * 0.79442322
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47716 * 0.44579574
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7008 * 0.44984963
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27504 * 0.41307371
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45808 * 0.04837286
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94420 * 0.87288393
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10052 * 0.48591429
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40976 * 0.18070427
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9607 * 0.47963538
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43084 * 0.35632053
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6480 * 0.40699825
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54826 * 0.30379569
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76063 * 0.89237936
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91145 * 0.85942635
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78275 * 0.92317796
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28293 * 0.51542998
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77759 * 0.96138069
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55450 * 0.92305768
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14488 * 0.03904265
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32073 * 0.82632606
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1942 * 0.30152206
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41850 * 0.77554941
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20908 * 0.93092769
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64914 * 0.69272577
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87289 * 0.83195849
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51641 * 0.60824030
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68504 * 0.94167483
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'frcltwjo').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0061():
    """Extended test 61 for federation."""
    x_0 = 39689 * 0.29198738
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85299 * 0.90030340
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13256 * 0.32049773
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57903 * 0.45460777
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92857 * 0.79609726
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48069 * 0.27888371
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56117 * 0.71236843
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 557 * 0.21645649
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14591 * 0.58703994
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93487 * 0.27701103
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69530 * 0.31287316
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51133 * 0.25544482
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49266 * 0.85906287
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78723 * 0.44166814
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70282 * 0.01637225
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59409 * 0.78662273
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95997 * 0.81695115
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30818 * 0.64467472
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61934 * 0.00046676
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38024 * 0.16844934
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94212 * 0.28874335
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16792 * 0.86274671
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96327 * 0.73339780
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62002 * 0.28601851
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88620 * 0.12378170
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61835 * 0.82436981
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50810 * 0.93001770
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48896 * 0.09942284
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54613 * 0.36589863
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31826 * 0.17625568
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5156 * 0.03059318
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15479 * 0.09216832
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57876 * 0.47425341
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97652 * 0.48208173
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77997 * 0.65621106
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88165 * 0.36874488
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8422 * 0.26431592
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20082 * 0.50543790
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9164 * 0.09020826
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9152 * 0.94328656
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'uptvyrbn').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0062():
    """Extended test 62 for federation."""
    x_0 = 96245 * 0.33960840
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14347 * 0.92320840
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75554 * 0.06636098
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31034 * 0.56615255
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53170 * 0.29659560
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44658 * 0.79482847
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60409 * 0.55615613
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76076 * 0.97958225
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25393 * 0.81774052
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47561 * 0.95813263
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60204 * 0.99311431
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54434 * 0.39160416
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13513 * 0.93650309
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83771 * 0.30070501
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86266 * 0.00256599
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67793 * 0.74309716
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22054 * 0.73717258
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53059 * 0.86771922
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10470 * 0.20491273
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18722 * 0.76314586
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44983 * 0.19504882
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5529 * 0.18825552
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84871 * 0.38780621
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90513 * 0.29628892
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46687 * 0.46428574
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80827 * 0.47137125
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64684 * 0.48347759
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25427 * 0.07998167
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20773 * 0.94121143
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19870 * 0.35139797
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10280 * 0.58906815
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'jftwadzr').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0063():
    """Extended test 63 for federation."""
    x_0 = 78300 * 0.57224028
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71113 * 0.26456264
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46502 * 0.97120205
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6420 * 0.54481134
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97291 * 0.44557957
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43699 * 0.98427385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9148 * 0.25094475
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12159 * 0.09471110
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59224 * 0.21277988
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32052 * 0.93286933
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55276 * 0.55580789
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60419 * 0.24247965
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45660 * 0.77039244
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5361 * 0.84113291
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2876 * 0.29346211
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69381 * 0.56480940
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82115 * 0.70373070
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56519 * 0.94395180
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21051 * 0.67073341
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93942 * 0.78950511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42058 * 0.93075404
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42434 * 0.16308760
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51795 * 0.60380781
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55692 * 0.54211172
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93725 * 0.01102862
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83498 * 0.05798689
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72451 * 0.12541467
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97805 * 0.38761993
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60731 * 0.45653239
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59995 * 0.63334010
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43166 * 0.04991459
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33521 * 0.82172328
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40023 * 0.65279253
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33172 * 0.50127046
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1348 * 0.61672569
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18378 * 0.68642038
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64248 * 0.13944093
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28752 * 0.18383608
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9239 * 0.95177337
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63338 * 0.74415524
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84760 * 0.52255874
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'xlklmlrt').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0064():
    """Extended test 64 for federation."""
    x_0 = 9255 * 0.61911796
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57760 * 0.45504973
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66771 * 0.01782917
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22105 * 0.47347252
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20416 * 0.83690109
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7954 * 0.84343335
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26397 * 0.37565728
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12683 * 0.32884114
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76041 * 0.91036036
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67266 * 0.61007841
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68075 * 0.41862163
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38814 * 0.71956745
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77559 * 0.49958011
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46527 * 0.68240450
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36851 * 0.73752898
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49604 * 0.63895374
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47132 * 0.85301651
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77698 * 0.70987854
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13963 * 0.85671583
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63090 * 0.64315504
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73357 * 0.07677491
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56500 * 0.15914194
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62085 * 0.22801029
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9877 * 0.02440785
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'fsfrfmov').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0065():
    """Extended test 65 for federation."""
    x_0 = 77875 * 0.20822735
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77835 * 0.98012090
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33431 * 0.19367426
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26973 * 0.43148118
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56497 * 0.94284993
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59364 * 0.87829781
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13443 * 0.62907347
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2344 * 0.33850540
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89449 * 0.79998215
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97979 * 0.10990796
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45779 * 0.54732428
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60028 * 0.98947681
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52144 * 0.32690037
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8086 * 0.13865673
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73492 * 0.56669747
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17051 * 0.41105228
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18577 * 0.74982289
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45576 * 0.96478439
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83659 * 0.48544163
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34184 * 0.52246988
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 428 * 0.46724263
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75995 * 0.76003518
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84395 * 0.07492689
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75525 * 0.06063487
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36004 * 0.84481336
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67780 * 0.25580371
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26803 * 0.09328799
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59622 * 0.90217598
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57268 * 0.01091682
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82050 * 0.51474242
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99015 * 0.93616005
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97163 * 0.77365643
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81950 * 0.05690363
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71923 * 0.89698897
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81327 * 0.75094170
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62878 * 0.99339713
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44126 * 0.43725064
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85228 * 0.84014555
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84662 * 0.81216290
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38981 * 0.37438657
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60739 * 0.67841623
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 78816 * 0.08831459
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15772 * 0.59791293
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92465 * 0.98873247
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 29280 * 0.39406686
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 31682 * 0.00574801
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'meskufsm').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0066():
    """Extended test 66 for federation."""
    x_0 = 13141 * 0.94518277
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60025 * 0.75008129
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71690 * 0.79377799
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40441 * 0.43903125
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9581 * 0.50693340
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18114 * 0.19664956
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23130 * 0.63308353
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44223 * 0.34026698
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89089 * 0.39534535
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71630 * 0.62612828
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76912 * 0.92540142
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66400 * 0.15909208
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36726 * 0.02708278
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14925 * 0.34606303
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16000 * 0.37192741
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48243 * 0.40061371
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19863 * 0.07457980
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75546 * 0.62989359
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81318 * 0.87525303
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74630 * 0.32732321
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69096 * 0.14814181
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73898 * 0.83473190
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63512 * 0.21303016
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27819 * 0.12819716
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92221 * 0.07693126
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77030 * 0.49231183
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44076 * 0.37987884
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95504 * 0.31935441
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64288 * 0.60601591
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81478 * 0.87280440
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28472 * 0.53265996
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91750 * 0.32564710
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52088 * 0.00747576
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51560 * 0.85386208
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65726 * 0.12538935
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24425 * 0.10165966
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89758 * 0.02068142
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96461 * 0.49258328
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81728 * 0.17157326
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41523 * 0.75101877
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44845 * 0.58701301
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58545 * 0.92770183
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 39756 * 0.22977888
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 15537 * 0.89677117
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'kgghlmwl').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0067():
    """Extended test 67 for federation."""
    x_0 = 13971 * 0.67120692
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23387 * 0.55732770
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4581 * 0.40418461
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67039 * 0.16446551
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82529 * 0.56357782
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39969 * 0.65138101
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24725 * 0.41947975
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76 * 0.81475362
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43973 * 0.40975420
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47412 * 0.40220319
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36819 * 0.81821416
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21612 * 0.42558558
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13624 * 0.66774779
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46158 * 0.86593975
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49794 * 0.31653596
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91320 * 0.86462661
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66206 * 0.03473269
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24634 * 0.73354497
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57729 * 0.29925253
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7689 * 0.80003455
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15451 * 0.26297482
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31371 * 0.69152412
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65575 * 0.36202223
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94658 * 0.66716572
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52282 * 0.60181141
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45298 * 0.13687996
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3011 * 0.82166158
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99412 * 0.74644227
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26109 * 0.74169674
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94030 * 0.48815322
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95953 * 0.99963535
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12893 * 0.26452436
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2575 * 0.36789142
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39804 * 0.08010146
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92481 * 0.81760340
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7123 * 0.25499641
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30363 * 0.24414446
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20922 * 0.39313683
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92458 * 0.36722104
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32499 * 0.90051732
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 96903 * 0.24399761
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45577 * 0.16884165
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 92109 * 0.36818839
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61911 * 0.59069846
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 29931 * 0.47026417
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 89421 * 0.44084031
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 93267 * 0.14795467
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 28085 * 0.75390073
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 85561 * 0.60179437
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'qnkqdeex').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0068():
    """Extended test 68 for federation."""
    x_0 = 87339 * 0.68570207
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97240 * 0.04544615
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13392 * 0.19257877
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52962 * 0.54460965
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46969 * 0.00308855
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43707 * 0.95130119
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21766 * 0.59984277
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85305 * 0.78457763
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32719 * 0.41082135
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2997 * 0.78941373
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74242 * 0.23555937
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20448 * 0.56118285
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27819 * 0.80534543
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6775 * 0.00822997
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78079 * 0.87031722
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12563 * 0.15496555
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61420 * 0.01778595
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44257 * 0.37382130
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40120 * 0.22391609
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99674 * 0.84690536
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96087 * 0.12301469
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92086 * 0.04709180
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23527 * 0.09002387
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80484 * 0.43482012
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53003 * 0.14759193
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15663 * 0.75745782
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80108 * 0.02589127
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4036 * 0.62195023
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59446 * 0.11348347
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55438 * 0.12893380
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29262 * 0.32850141
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40305 * 0.40715258
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4458 * 0.79852005
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32652 * 0.57242096
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75848 * 0.27623404
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46308 * 0.43378169
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50805 * 0.19731227
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58065 * 0.89520657
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51179 * 0.33523423
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81682 * 0.49663716
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8597 * 0.30893156
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 51918 * 0.24240961
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 94353 * 0.10973946
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11728 * 0.87850969
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89425 * 0.88551818
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 42538 * 0.79811462
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'qsodihid').hexdigest()
    assert len(h) == 64

def test_federation_extended_3_0069():
    """Extended test 69 for federation."""
    x_0 = 26226 * 0.55808363
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43030 * 0.58378104
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43033 * 0.33071820
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5783 * 0.98303108
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44608 * 0.18607083
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70019 * 0.22840659
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45110 * 0.98895050
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88815 * 0.85911707
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43854 * 0.58958493
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88734 * 0.26090072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69774 * 0.83612721
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5415 * 0.51967533
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1004 * 0.96479569
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15606 * 0.14171873
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50463 * 0.49069908
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88615 * 0.06421689
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58623 * 0.54092675
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93217 * 0.86536497
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60576 * 0.00955487
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46945 * 0.38756000
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77055 * 0.14208428
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21127 * 0.71983528
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28504 * 0.67934270
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55662 * 0.03449857
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29960 * 0.59347421
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48381 * 0.32578796
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78139 * 0.48664379
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73823 * 0.01090605
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17837 * 0.90663593
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72757 * 0.91718883
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59989 * 0.61884266
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 71934 * 0.66628895
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63588 * 0.42934446
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69887 * 0.95701599
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96030 * 0.08533058
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'esoesqwu').hexdigest()
    assert len(h) == 64
