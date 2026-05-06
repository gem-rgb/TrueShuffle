"""Extended tests for api suite 5."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_api_extended_5_0000():
    """Extended test 0 for api."""
    x_0 = 85258 * 0.97046724
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82686 * 0.16488429
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25833 * 0.40217514
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42237 * 0.94102327
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95466 * 0.73351230
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52866 * 0.80138557
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6807 * 0.52706145
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77704 * 0.86469525
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 990 * 0.84578190
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48583 * 0.78179866
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12273 * 0.56473563
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68613 * 0.89067129
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3552 * 0.15625809
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47402 * 0.70286324
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6143 * 0.33101058
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79641 * 0.21878380
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96090 * 0.29367658
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67170 * 0.45292792
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2469 * 0.39560779
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82355 * 0.55210634
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8666 * 0.67453121
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83075 * 0.93967683
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12043 * 0.23212183
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59133 * 0.18049454
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36343 * 0.28828977
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59568 * 0.35735561
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6445 * 0.95452082
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ycmnnsky').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0001():
    """Extended test 1 for api."""
    x_0 = 23753 * 0.19301801
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94786 * 0.87118404
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30483 * 0.41581940
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37011 * 0.99790809
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99976 * 0.76783711
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39231 * 0.57721274
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64521 * 0.15126988
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34132 * 0.61987078
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49182 * 0.47505271
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42804 * 0.92353468
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78088 * 0.17816129
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57503 * 0.88717234
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68893 * 0.09837662
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10604 * 0.67887945
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79733 * 0.63870077
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65929 * 0.34608027
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42816 * 0.78658334
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44208 * 0.94917841
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75712 * 0.33025650
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37601 * 0.75662841
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23232 * 0.96937252
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30958 * 0.99196741
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 189 * 0.29113077
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41809 * 0.28024463
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67158 * 0.27529667
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87352 * 0.94537724
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72548 * 0.43059657
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60671 * 0.88616205
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40316 * 0.65142058
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27125 * 0.76876109
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32627 * 0.72486524
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39909 * 0.67037225
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92540 * 0.41206252
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61775 * 0.64225649
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71612 * 0.55193920
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63292 * 0.31837346
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1444 * 0.53874142
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64298 * 0.17318198
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74113 * 0.78345386
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94193 * 0.61660096
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98219 * 0.25713970
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81655 * 0.40596830
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 3995 * 0.37867441
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ynbtfbda').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0002():
    """Extended test 2 for api."""
    x_0 = 75534 * 0.38977014
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35037 * 0.23630698
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13485 * 0.12613889
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63365 * 0.77250384
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9204 * 0.82222692
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8906 * 0.75686811
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41590 * 0.79191509
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96893 * 0.33956270
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56073 * 0.61741569
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34560 * 0.28894378
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77470 * 0.60975951
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78561 * 0.77090122
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24358 * 0.12209864
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15506 * 0.23465113
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47156 * 0.25994973
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14589 * 0.83732158
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40284 * 0.24644724
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92729 * 0.57971625
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71037 * 0.90885115
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87982 * 0.78447816
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81052 * 0.75894309
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'zpwdmads').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0003():
    """Extended test 3 for api."""
    x_0 = 74095 * 0.54142349
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84952 * 0.52838018
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76231 * 0.83474523
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26871 * 0.34982861
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86669 * 0.45287178
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88851 * 0.21560448
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60957 * 0.55860302
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45502 * 0.26842622
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6290 * 0.05348374
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39629 * 0.61271601
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62884 * 0.66421344
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12283 * 0.37071261
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5400 * 0.87510622
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31697 * 0.91566162
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89388 * 0.13410579
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15954 * 0.26867532
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94622 * 0.98466308
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98939 * 0.82966929
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31512 * 0.13396471
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54770 * 0.98287107
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27370 * 0.87935596
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75132 * 0.35981192
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96513 * 0.07616615
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36655 * 0.79989187
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79825 * 0.24754556
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64013 * 0.08700146
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93985 * 0.65644110
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38351 * 0.41078191
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19086 * 0.41490155
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51851 * 0.14300047
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79444 * 0.06473026
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85202 * 0.00961147
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50151 * 0.40055497
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56683 * 0.27246479
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 49159 * 0.63782146
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14606 * 0.77482070
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25992 * 0.46972483
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28646 * 0.35625988
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79561 * 0.40249888
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98181 * 0.88255280
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32822 * 0.60870022
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13020 * 0.38672628
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28385 * 0.02822001
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 66026 * 0.42518889
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61410 * 0.45770565
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 28343 * 0.67829571
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 75747 * 0.80400428
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 58467 * 0.09230699
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 33948 * 0.64782866
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'crczqclk').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0004():
    """Extended test 4 for api."""
    x_0 = 5704 * 0.92464644
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14230 * 0.61593898
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39737 * 0.58403232
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91721 * 0.08561700
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57912 * 0.82599926
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67451 * 0.24058332
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79131 * 0.88452977
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61691 * 0.21860257
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21798 * 0.57533528
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50880 * 0.03901538
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68892 * 0.41333177
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53626 * 0.59827238
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99108 * 0.76887338
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86746 * 0.29377006
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55949 * 0.36987715
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19500 * 0.17756633
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1993 * 0.14927415
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58593 * 0.05544763
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40415 * 0.84155356
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12448 * 0.37572164
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7006 * 0.47210005
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90603 * 0.51160124
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1575 * 0.21381401
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'rajktkaj').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0005():
    """Extended test 5 for api."""
    x_0 = 3542 * 0.75457008
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7011 * 0.07038376
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6593 * 0.89031008
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78074 * 0.44635294
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93943 * 0.87119943
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34057 * 0.14395717
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15968 * 0.80004469
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76361 * 0.27702731
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39463 * 0.49536594
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4617 * 0.13677884
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37389 * 0.97911991
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96298 * 0.10644576
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54542 * 0.35371012
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85120 * 0.90606542
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20709 * 0.15216338
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91494 * 0.14109338
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65375 * 0.68635105
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44102 * 0.05664848
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3746 * 0.49706815
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3562 * 0.02293057
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81952 * 0.40116791
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59615 * 0.25611547
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69411 * 0.97062101
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25721 * 0.94315351
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98550 * 0.59027035
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77787 * 0.13900474
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52841 * 0.85594561
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19148 * 0.14503245
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68227 * 0.91015728
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66706 * 0.40391671
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30742 * 0.13907050
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69914 * 0.61922261
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81685 * 0.04793030
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88513 * 0.99174527
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10569 * 0.70534283
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6670 * 0.84773089
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92846 * 0.01521141
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91181 * 0.56387046
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47893 * 0.39173978
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64233 * 0.28976954
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 93298 * 0.67117480
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 95956 * 0.80758855
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77133 * 0.12247248
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 59680 * 0.88975937
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 87162 * 0.32797298
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 92206 * 0.98580975
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 21105 * 0.10700253
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 78108 * 0.83901406
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 68056 * 0.96401437
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 36753 * 0.21240360
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'cwawqkol').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0006():
    """Extended test 6 for api."""
    x_0 = 38578 * 0.61130085
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64611 * 0.05288237
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76221 * 0.13399384
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1334 * 0.27356124
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26138 * 0.43039603
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2537 * 0.27770364
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49698 * 0.12702907
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32763 * 0.76554017
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73142 * 0.29775545
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23412 * 0.54964957
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93895 * 0.67222469
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65199 * 0.60925589
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33951 * 0.35568179
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34124 * 0.55934718
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99556 * 0.17497400
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49710 * 0.96710709
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17350 * 0.57110959
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28898 * 0.32294041
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90291 * 0.13637989
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94272 * 0.55092397
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27004 * 0.41900059
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57425 * 0.08814819
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'xtztqmjf').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0007():
    """Extended test 7 for api."""
    x_0 = 37781 * 0.79908743
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44051 * 0.74591458
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30716 * 0.20051328
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77561 * 0.55291630
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4405 * 0.46510394
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28612 * 0.71474448
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23173 * 0.30756816
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93224 * 0.44404645
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95429 * 0.77445427
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44339 * 0.46913166
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1993 * 0.50483226
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3394 * 0.42965560
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30148 * 0.02921569
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84470 * 0.46777742
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83707 * 0.26106997
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42857 * 0.01542125
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69030 * 0.63638785
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93556 * 0.71689123
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46920 * 0.54694572
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58576 * 0.10967746
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75700 * 0.39799023
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16069 * 0.89358593
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86179 * 0.00772891
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35431 * 0.86211384
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28791 * 0.59899422
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4553 * 0.00173618
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60385 * 0.48323629
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36268 * 0.19403289
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98565 * 0.91324993
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'baexafui').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0008():
    """Extended test 8 for api."""
    x_0 = 8361 * 0.81345675
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45355 * 0.13353413
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47491 * 0.81355691
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98368 * 0.83214873
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41020 * 0.85275036
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72994 * 0.21273939
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57587 * 0.09003156
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94055 * 0.16525858
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84480 * 0.74656813
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5574 * 0.46670494
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30813 * 0.63962511
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91149 * 0.58489924
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55504 * 0.34266762
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3987 * 0.24504338
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64310 * 0.80513864
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15718 * 0.86791683
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66222 * 0.96340235
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48633 * 0.98867161
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76793 * 0.93835556
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54917 * 0.14960885
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33880 * 0.01732921
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6487 * 0.51649829
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31843 * 0.98939217
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10946 * 0.38974537
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26651 * 0.61203051
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72605 * 0.54456941
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57289 * 0.92165408
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23989 * 0.22286159
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33924 * 0.21531264
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26699 * 0.54622458
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96391 * 0.16557363
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8512 * 0.50474859
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66772 * 0.71002914
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53793 * 0.92648677
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30971 * 0.00370918
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20248 * 0.10528565
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32705 * 0.81244019
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67018 * 0.11510534
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96244 * 0.31805910
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67216 * 0.89690110
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41344 * 0.27321325
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58642 * 0.60288453
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 59486 * 0.48913134
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75521 * 0.43101143
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 30101 * 0.03243579
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 34294 * 0.38750089
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 82510 * 0.56172310
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 13140 * 0.48959072
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 2294 * 0.28320746
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'sntilbnl').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0009():
    """Extended test 9 for api."""
    x_0 = 22596 * 0.42563279
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88476 * 0.61292920
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51089 * 0.96569750
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17410 * 0.19936184
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88816 * 0.75745350
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37195 * 0.25669206
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24327 * 0.27049968
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67794 * 0.52503490
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41814 * 0.22756206
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89597 * 0.64471370
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95597 * 0.39253804
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35283 * 0.57604827
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87026 * 0.72786504
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61139 * 0.60917055
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98496 * 0.43842091
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29902 * 0.95102333
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73806 * 0.38741139
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18221 * 0.74959132
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87461 * 0.04827784
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53103 * 0.02944201
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94905 * 0.75583926
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15639 * 0.09586577
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44903 * 0.48554590
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98151 * 0.89066466
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55377 * 0.64274192
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72185 * 0.87523491
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74003 * 0.33432854
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6940 * 0.08544443
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75406 * 0.94654581
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44695 * 0.87965522
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57381 * 0.99546840
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2521 * 0.14142005
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88275 * 0.60348853
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18678 * 0.40522276
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86543 * 0.24618677
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75802 * 0.76996789
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 77527 * 0.98648383
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22372 * 0.15526436
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34005 * 0.29043023
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22394 * 0.63303195
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86494 * 0.60892812
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26649 * 0.68169791
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 98390 * 0.94901508
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 71773 * 0.41614074
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 42112 * 0.22660883
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 40265 * 0.95672088
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 83452 * 0.10076824
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'jzjosxgo').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0010():
    """Extended test 10 for api."""
    x_0 = 47993 * 0.60333626
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57701 * 0.10850181
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24333 * 0.91155723
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61305 * 0.84605371
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93227 * 0.93988915
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41683 * 0.84648453
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90975 * 0.76556822
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75820 * 0.90859268
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64980 * 0.00987614
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74684 * 0.49398755
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9141 * 0.93646458
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24684 * 0.95004482
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5730 * 0.01500375
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66573 * 0.54867726
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27688 * 0.71404072
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43625 * 0.03143833
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95873 * 0.34139073
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47667 * 0.61143940
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12165 * 0.74972061
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84948 * 0.45727382
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55108 * 0.81201851
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25281 * 0.45165516
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36559 * 0.40273155
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9363 * 0.95592998
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26086 * 0.20091375
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53241 * 0.75184406
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8634 * 0.91393160
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75175 * 0.55205333
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52533 * 0.93231665
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48492 * 0.52081909
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21866 * 0.33136792
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36180 * 0.81739348
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25948 * 0.25989983
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'zvhvshnh').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0011():
    """Extended test 11 for api."""
    x_0 = 53481 * 0.69428301
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51879 * 0.41207284
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4312 * 0.13105968
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26947 * 0.05578465
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74789 * 0.73368267
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79692 * 0.03105034
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68642 * 0.39169316
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65702 * 0.05120404
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34602 * 0.44255822
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96423 * 0.41341947
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76629 * 0.41651228
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15827 * 0.26106629
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8255 * 0.51195168
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45843 * 0.41025236
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26833 * 0.35332513
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68438 * 0.96714638
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73780 * 0.43223216
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33998 * 0.34765433
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35531 * 0.14463095
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48928 * 0.36715533
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12044 * 0.66263963
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21791 * 0.98309712
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72295 * 0.70093485
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47594 * 0.05286308
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82685 * 0.80432468
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49125 * 0.53518069
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81432 * 0.56807615
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68335 * 0.21664065
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98096 * 0.68289626
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83990 * 0.67238413
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78972 * 0.26696598
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46486 * 0.02446983
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69442 * 0.77507165
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55657 * 0.71233486
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63906 * 0.22753297
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88918 * 0.14289902
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71167 * 0.08778273
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'jidtcrex').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0012():
    """Extended test 12 for api."""
    x_0 = 6797 * 0.92756689
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54434 * 0.81406547
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90002 * 0.43301784
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16133 * 0.11017432
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56895 * 0.81874632
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79190 * 0.25814086
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33849 * 0.57804857
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55379 * 0.28527458
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94280 * 0.01152866
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95371 * 0.28919123
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31505 * 0.83441994
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74708 * 0.00196486
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53312 * 0.19871800
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30307 * 0.89008648
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18819 * 0.22910759
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38129 * 0.71406338
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41820 * 0.35624314
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71162 * 0.90839545
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14079 * 0.16941670
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69834 * 0.68535196
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73733 * 0.44272317
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71576 * 0.23298486
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87532 * 0.12746777
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46526 * 0.01710267
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31742 * 0.94075534
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93306 * 0.32107598
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98353 * 0.52305374
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63811 * 0.66725615
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49558 * 0.33066690
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41457 * 0.13997941
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99832 * 0.72146988
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16222 * 0.57235932
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1564 * 0.69979697
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69418 * 0.77820719
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13967 * 0.63685285
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65716 * 0.59588190
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71684 * 0.36842358
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55060 * 0.14604046
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43417 * 0.22533089
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75501 * 0.55947494
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88570 * 0.88594810
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97778 * 0.70520349
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 38855 * 0.87015197
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 98329 * 0.48968891
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 3549 * 0.86129251
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 77872 * 0.58485806
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 5407 * 0.34556163
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'csleukyl').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0013():
    """Extended test 13 for api."""
    x_0 = 47447 * 0.61949223
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26515 * 0.31458621
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82090 * 0.92541275
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62528 * 0.79292294
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78890 * 0.10193701
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46933 * 0.49773666
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2040 * 0.07746316
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48520 * 0.45420760
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2226 * 0.63708522
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2019 * 0.69215465
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61803 * 0.88189458
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45334 * 0.66042915
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73169 * 0.11650138
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54113 * 0.82089885
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17752 * 0.79353504
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64067 * 0.00795686
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35830 * 0.84812075
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56771 * 0.68885558
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56719 * 0.61877796
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58658 * 0.45529630
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37225 * 0.72828180
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9127 * 0.21566475
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97032 * 0.31558859
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6304 * 0.38750901
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83738 * 0.73258014
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70767 * 0.58203814
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80856 * 0.25001590
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88783 * 0.66369420
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99871 * 0.38079535
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5692 * 0.84224276
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41672 * 0.57610790
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32440 * 0.64057738
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72891 * 0.36558053
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61326 * 0.87314165
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23413 * 0.42808585
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32643 * 0.16453738
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'badavplh').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0014():
    """Extended test 14 for api."""
    x_0 = 33149 * 0.74027751
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14871 * 0.78383344
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48739 * 0.76071608
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59852 * 0.35073258
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61215 * 0.94734967
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26968 * 0.27224323
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48399 * 0.93526540
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76817 * 0.10859597
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43181 * 0.03404201
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31261 * 0.20176734
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63305 * 0.88185215
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1506 * 0.73671458
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52262 * 0.25553870
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46836 * 0.87892633
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91697 * 0.56921232
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43676 * 0.57930275
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60292 * 0.70904839
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39478 * 0.30054680
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77576 * 0.10221468
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44738 * 0.47224933
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55154 * 0.98309148
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33960 * 0.38955329
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67050 * 0.30323817
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56314 * 0.97625796
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46505 * 0.45373856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8331 * 0.60592048
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88006 * 0.95803766
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70859 * 0.48245428
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83563 * 0.64547273
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28126 * 0.17992223
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60858 * 0.71769184
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'frpxxpuh').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0015():
    """Extended test 15 for api."""
    x_0 = 30719 * 0.79312853
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74417 * 0.73562417
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46206 * 0.42696500
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70812 * 0.27470323
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97859 * 0.69623960
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56583 * 0.39170898
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2858 * 0.36019548
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22153 * 0.27611314
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18919 * 0.32074916
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55354 * 0.11613370
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2602 * 0.12186549
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10967 * 0.62960295
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88113 * 0.57446367
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74996 * 0.96357271
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15168 * 0.08444025
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79147 * 0.25219486
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40556 * 0.25021795
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7970 * 0.58727107
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88655 * 0.31027239
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77850 * 0.87860529
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94374 * 0.26580822
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19949 * 0.69890300
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30348 * 0.89004203
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1266 * 0.09024916
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87418 * 0.43825673
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97339 * 0.53691217
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14251 * 0.98419326
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37225 * 0.22092671
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28067 * 0.39311367
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58156 * 0.18954096
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70698 * 0.82508200
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75478 * 0.51280958
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80413 * 0.74497233
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8511 * 0.84469553
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'mhjlrqqg').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0016():
    """Extended test 16 for api."""
    x_0 = 68282 * 0.31009816
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69722 * 0.31515791
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16052 * 0.74565911
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72412 * 0.29223720
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40722 * 0.03572692
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46397 * 0.62513908
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2781 * 0.58506060
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82647 * 0.17621389
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52736 * 0.98521425
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85215 * 0.05116436
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36567 * 0.24253859
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58354 * 0.65946256
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30147 * 0.80614691
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93644 * 0.71942094
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61267 * 0.15861894
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71436 * 0.55566131
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67798 * 0.99928567
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35242 * 0.29895058
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60596 * 0.16500388
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87264 * 0.64800348
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40617 * 0.46259483
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80458 * 0.65020134
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65720 * 0.51930226
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51006 * 0.00975826
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65847 * 0.09349692
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78172 * 0.34425095
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54813 * 0.31445273
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89677 * 0.69967812
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67064 * 0.31108107
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27852 * 0.27448811
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55898 * 0.60057990
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12130 * 0.25902877
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68936 * 0.72450812
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81702 * 0.71903380
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5510 * 0.95446312
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36735 * 0.36236301
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7055 * 0.18292523
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95481 * 0.33650393
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'rcxqsorb').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0017():
    """Extended test 17 for api."""
    x_0 = 97993 * 0.48304447
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54772 * 0.71878062
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10870 * 0.52420811
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46364 * 0.80430084
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35349 * 0.82211339
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30601 * 0.07190589
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29670 * 0.77555258
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39299 * 0.73299091
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15469 * 0.44822922
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93903 * 0.69564448
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33787 * 0.44506561
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71515 * 0.96348995
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51695 * 0.84975488
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38607 * 0.59220602
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23629 * 0.05281983
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75393 * 0.54454301
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66198 * 0.90601272
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92868 * 0.82934782
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83628 * 0.56944677
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68338 * 0.15454758
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74247 * 0.26889995
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14343 * 0.80156696
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80747 * 0.36122899
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51879 * 0.39344586
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55120 * 0.82382510
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96683 * 0.15501512
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2812 * 0.49542650
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'nbpcbqti').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0018():
    """Extended test 18 for api."""
    x_0 = 42665 * 0.55814701
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53894 * 0.25129492
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25260 * 0.82469358
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14645 * 0.84806320
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6478 * 0.65413667
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67242 * 0.75849418
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 590 * 0.93622802
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69356 * 0.99003323
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25864 * 0.08331276
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55111 * 0.04929839
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73487 * 0.06868423
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94573 * 0.39681954
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97250 * 0.53842258
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61768 * 0.15246441
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37285 * 0.40401635
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19929 * 0.22082710
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2553 * 0.79371409
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39021 * 0.11014410
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37088 * 0.38044460
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12167 * 0.02842740
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81737 * 0.96773767
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6774 * 0.27979379
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17818 * 0.57340210
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81835 * 0.92099851
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75500 * 0.21476027
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71720 * 0.53030660
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12309 * 0.63887734
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30998 * 0.25306481
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67775 * 0.64379289
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51252 * 0.15054700
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16772 * 0.38962533
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50447 * 0.16997284
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22084 * 0.49989073
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54741 * 0.38953466
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92835 * 0.07168200
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15316 * 0.19260086
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56962 * 0.28695807
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 77202 * 0.91177228
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12256 * 0.85423860
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79795 * 0.25336856
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18990 * 0.00130966
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97276 * 0.00584383
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88821 * 0.80261210
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47017 * 0.08122318
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 75037 * 0.36730208
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'ipekwaso').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0019():
    """Extended test 19 for api."""
    x_0 = 41383 * 0.09387493
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58026 * 0.80003489
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43297 * 0.09041862
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64228 * 0.76152737
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29514 * 0.06277440
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11688 * 0.17481349
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19522 * 0.26640231
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5398 * 0.78357590
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3270 * 0.47097197
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 787 * 0.90067515
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57156 * 0.07765516
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24016 * 0.65674459
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57067 * 0.31320806
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14436 * 0.71380961
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22761 * 0.10398684
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68924 * 0.82738330
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12022 * 0.84990127
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99849 * 0.03328330
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80223 * 0.09268827
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11662 * 0.23433350
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38865 * 0.64403695
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71212 * 0.97196602
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3197 * 0.84539381
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87832 * 0.64316475
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80972 * 0.91711267
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64512 * 0.93569471
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30531 * 0.26974474
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95458 * 0.47975747
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19399 * 0.51077578
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93333 * 0.34654418
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22675 * 0.47309339
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8055 * 0.52400490
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58654 * 0.86662655
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30810 * 0.22154600
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73976 * 0.03387228
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95219 * 0.62025096
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94849 * 0.20369020
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55453 * 0.55625296
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98319 * 0.57894975
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25460 * 0.96927387
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29636 * 0.48348680
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 62443 * 0.61249479
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 5059 * 0.93645248
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 43774 * 0.56911460
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 67106 * 0.45845160
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 22300 * 0.65758270
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 35520 * 0.74409589
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 53843 * 0.35353343
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 10958 * 0.41167738
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 5346 * 0.40592149
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'dbbxhpkz').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0020():
    """Extended test 20 for api."""
    x_0 = 54870 * 0.20781715
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50192 * 0.28846111
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35229 * 0.41312789
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55301 * 0.47933672
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24265 * 0.92725983
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14221 * 0.47482557
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88747 * 0.19176740
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26778 * 0.48740999
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73106 * 0.68571090
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7077 * 0.13725419
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42206 * 0.80171655
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33934 * 0.75178637
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83892 * 0.97375439
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73235 * 0.17834015
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61070 * 0.37951724
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17723 * 0.08199512
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61447 * 0.70415778
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42094 * 0.08407451
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78452 * 0.16064316
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6195 * 0.96980385
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69296 * 0.59770811
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73250 * 0.57820825
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'hqqscwzi').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0021():
    """Extended test 21 for api."""
    x_0 = 93796 * 0.67847710
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13482 * 0.33674213
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8880 * 0.82825670
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13229 * 0.42137487
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2892 * 0.76688736
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71397 * 0.11924516
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78249 * 0.43510635
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85304 * 0.10674355
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38542 * 0.28712981
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27450 * 0.76612202
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54517 * 0.94994474
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28480 * 0.61991742
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83430 * 0.86791411
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93663 * 0.29937407
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34763 * 0.16804137
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92874 * 0.39786406
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49237 * 0.72964855
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83373 * 0.18580044
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63677 * 0.70554189
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30948 * 0.18685497
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41453 * 0.14566519
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60438 * 0.64413382
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11234 * 0.09489245
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73973 * 0.66598085
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65141 * 0.26895601
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1436 * 0.52750152
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14755 * 0.67136781
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81307 * 0.55108483
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97644 * 0.41984765
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68513 * 0.81339677
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64160 * 0.95228322
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8356 * 0.93228997
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46215 * 0.06470023
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28692 * 0.23650866
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68612 * 0.95815430
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 9570 * 0.00400689
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9192 * 0.79972383
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33267 * 0.90378557
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86026 * 0.91028773
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 28598 * 0.91734161
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 56122 * 0.54319839
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25834 * 0.27660209
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23521 * 0.96124214
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 17414 * 0.91581011
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 73769 * 0.30726514
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'pjpjjtdg').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0022():
    """Extended test 22 for api."""
    x_0 = 91511 * 0.84330018
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57455 * 0.18721503
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52851 * 0.76873536
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67668 * 0.40960223
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91167 * 0.35580635
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1888 * 0.08561698
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62424 * 0.95932814
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13845 * 0.40611382
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53773 * 0.86848310
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57400 * 0.49443771
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83872 * 0.91962256
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45563 * 0.78690336
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97846 * 0.18232946
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67374 * 0.19725454
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 455 * 0.11129098
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77997 * 0.06286548
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48863 * 0.00716596
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42749 * 0.22547895
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95131 * 0.48623487
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95877 * 0.11133874
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64772 * 0.78836472
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'cvwfgaak').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0023():
    """Extended test 23 for api."""
    x_0 = 61824 * 0.92738377
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38562 * 0.74648599
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59452 * 0.94525860
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88986 * 0.29581006
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2704 * 0.90068516
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46894 * 0.79482697
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61391 * 0.77949843
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64546 * 0.25226021
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99330 * 0.80258115
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97465 * 0.39876968
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6993 * 0.14603084
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88849 * 0.30741150
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50881 * 0.26062578
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26959 * 0.85483799
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91432 * 0.91053285
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88776 * 0.63019919
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52447 * 0.40013968
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90350 * 0.66713665
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54585 * 0.54714776
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4977 * 0.09398894
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84863 * 0.08095635
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50697 * 0.45323007
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69231 * 0.57426589
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63543 * 0.96942260
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31194 * 0.09909125
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70541 * 0.47203489
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80527 * 0.86057366
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55723 * 0.43321797
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65805 * 0.73579596
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69248 * 0.82367046
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4842 * 0.29007112
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5686 * 0.20669772
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45863 * 0.09568650
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6705 * 0.57550086
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61176 * 0.93035444
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42318 * 0.29843322
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61420 * 0.66753401
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12358 * 0.16097457
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'umvfimch').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0024():
    """Extended test 24 for api."""
    x_0 = 26511 * 0.63563614
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48821 * 0.47772020
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21926 * 0.37613620
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54157 * 0.35156137
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74177 * 0.23560154
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9912 * 0.83534461
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22164 * 0.95158759
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16740 * 0.65951675
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6777 * 0.13568471
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58520 * 0.49884759
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58311 * 0.33526292
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71524 * 0.43842045
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49716 * 0.72497947
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5104 * 0.01461902
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44746 * 0.69870546
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43098 * 0.12609412
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9056 * 0.82611734
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7398 * 0.60484053
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8924 * 0.72296361
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70881 * 0.42222574
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15608 * 0.37760787
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5795 * 0.84582924
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31925 * 0.86476847
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 321 * 0.65474994
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57547 * 0.51151482
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74967 * 0.79731519
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17351 * 0.51851390
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86638 * 0.15204789
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64160 * 0.81768514
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73541 * 0.24785989
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25360 * 0.74298111
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54499 * 0.92438973
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58357 * 0.09997795
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56067 * 0.39693219
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61281 * 0.39581598
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54767 * 0.94161050
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50520 * 0.67228290
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83051 * 0.12822417
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24768 * 0.09409752
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38802 * 0.79651435
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 33037 * 0.04677502
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14626 * 0.65648709
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18193 * 0.79425466
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38510 * 0.48119464
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'vsdbitdj').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0025():
    """Extended test 25 for api."""
    x_0 = 42622 * 0.90780256
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53341 * 0.60610808
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75591 * 0.16535050
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88896 * 0.11491364
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12758 * 0.62237113
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51554 * 0.72768381
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3645 * 0.30496497
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86099 * 0.44730622
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28373 * 0.01811403
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33608 * 0.01481259
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49313 * 0.56938086
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83035 * 0.08484454
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 174 * 0.65251660
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45273 * 0.36433320
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72255 * 0.27594919
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 496 * 0.69130036
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77224 * 0.88929078
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38358 * 0.26020942
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9843 * 0.57070197
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88802 * 0.60414862
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18262 * 0.23317562
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'vycupceo').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0026():
    """Extended test 26 for api."""
    x_0 = 67593 * 0.78320240
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49152 * 0.51574512
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76912 * 0.21066168
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87762 * 0.53672073
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38868 * 0.67178828
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47258 * 0.10024879
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78193 * 0.69330864
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94865 * 0.12968890
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49723 * 0.04703049
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60248 * 0.67472728
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88616 * 0.00496736
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59830 * 0.73594856
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35298 * 0.87891094
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90390 * 0.09045410
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3476 * 0.96409190
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42012 * 0.41082138
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71118 * 0.57954663
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3556 * 0.55440935
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91050 * 0.81065376
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96678 * 0.00345288
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71290 * 0.69848767
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91165 * 0.55861651
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'fqjajuat').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0027():
    """Extended test 27 for api."""
    x_0 = 13505 * 0.42754199
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4952 * 0.20489897
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60844 * 0.26634108
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48779 * 0.44462112
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64391 * 0.38855323
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85758 * 0.94952045
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98496 * 0.60295651
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47938 * 0.26031450
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67853 * 0.80273135
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98512 * 0.22490198
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38157 * 0.62479882
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55949 * 0.72562986
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58508 * 0.51619807
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25914 * 0.47073393
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29215 * 0.23763223
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69600 * 0.14150861
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81498 * 0.30281036
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29904 * 0.54870680
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69830 * 0.18934714
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12047 * 0.66106305
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6277 * 0.29374335
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69108 * 0.09900871
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67171 * 0.29863257
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21250 * 0.51498682
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83854 * 0.96369880
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91760 * 0.30217487
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66965 * 0.06212329
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21149 * 0.76058705
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49817 * 0.13974282
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49681 * 0.64083078
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12600 * 0.02967830
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23658 * 0.39571557
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71927 * 0.71661886
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74178 * 0.17455133
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66231 * 0.34324443
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40135 * 0.29875425
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63975 * 0.51671455
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89068 * 0.88351672
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78771 * 0.71958179
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56720 * 0.98420772
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78010 * 0.97031402
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89353 * 0.08833487
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'tqgvkden').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0028():
    """Extended test 28 for api."""
    x_0 = 93948 * 0.60440892
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67228 * 0.14378417
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16735 * 0.33473619
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34621 * 0.14265800
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32817 * 0.62325499
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17134 * 0.78487759
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96642 * 0.11653335
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83469 * 0.58392681
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51254 * 0.14763766
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29860 * 0.72057574
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86663 * 0.74019733
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 592 * 0.60778424
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34273 * 0.28373195
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 410 * 0.17000603
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81952 * 0.43164432
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40536 * 0.44482238
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11355 * 0.79323356
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10666 * 0.62910998
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6392 * 0.51794001
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87068 * 0.74393833
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86421 * 0.53383790
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95986 * 0.34903042
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38178 * 0.64793366
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1098 * 0.58925068
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21473 * 0.03833549
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78572 * 0.93395767
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87455 * 0.03931813
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36616 * 0.27703051
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9035 * 0.28678569
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38504 * 0.50088944
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60692 * 0.08453237
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87910 * 0.86890271
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84979 * 0.14515676
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47763 * 0.79916389
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92582 * 0.02352295
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2623 * 0.43271086
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43517 * 0.42131518
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35429 * 0.64946859
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49640 * 0.16852209
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31780 * 0.56689725
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 72823 * 0.83556918
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 64108 * 0.46760432
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 53524 * 0.03925825
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'fbghqhig').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0029():
    """Extended test 29 for api."""
    x_0 = 19708 * 0.76452662
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52169 * 0.06114626
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47110 * 0.40214624
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74689 * 0.21590192
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95131 * 0.28764406
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87173 * 0.00992784
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47701 * 0.20843395
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35530 * 0.10479894
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47140 * 0.24199349
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15439 * 0.38096869
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40215 * 0.02561187
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14485 * 0.13265466
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88058 * 0.82181966
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61961 * 0.43325324
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48647 * 0.89449759
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48414 * 0.34311444
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73148 * 0.08366053
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87256 * 0.81382093
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31475 * 0.15750101
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51964 * 0.66379835
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90786 * 0.85881580
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22563 * 0.26646897
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73290 * 0.64454714
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23704 * 0.16536105
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97340 * 0.51103748
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58639 * 0.14712938
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41457 * 0.50345929
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96144 * 0.83625993
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26485 * 0.10443167
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22970 * 0.94792666
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94209 * 0.43611282
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27675 * 0.88744659
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92891 * 0.93981892
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'pfluqaya').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0030():
    """Extended test 30 for api."""
    x_0 = 42760 * 0.89983596
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35810 * 0.54731671
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19240 * 0.78252844
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22091 * 0.98027576
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62816 * 0.35082436
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44010 * 0.58866872
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98754 * 0.89168857
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93034 * 0.83826668
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54904 * 0.07774539
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74156 * 0.00807353
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9898 * 0.44329803
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66406 * 0.81816695
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28590 * 0.13337391
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7610 * 0.47463796
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4264 * 0.15542858
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5645 * 0.87134824
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74177 * 0.43615857
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86603 * 0.55799300
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89798 * 0.33842444
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37689 * 0.07331970
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12562 * 0.89999957
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88717 * 0.47273776
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55549 * 0.36325952
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20186 * 0.60620570
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30421 * 0.63175365
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70515 * 0.48251199
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47579 * 0.99328245
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16587 * 0.76118303
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4098 * 0.58168574
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49627 * 0.30535157
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25227 * 0.58346991
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98213 * 0.37616785
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95254 * 0.56464671
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60802 * 0.71801986
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12016 * 0.64698796
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17297 * 0.18037700
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14806 * 0.35992413
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52116 * 0.56951636
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96814 * 0.86122064
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2046 * 0.34670597
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'cgfoyjxh').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0031():
    """Extended test 31 for api."""
    x_0 = 87205 * 0.03258898
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72033 * 0.20198374
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60859 * 0.89112864
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29228 * 0.18393333
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37615 * 0.90292988
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62868 * 0.06299071
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73481 * 0.89352361
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35801 * 0.31012840
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91374 * 0.08931366
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66667 * 0.28606001
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91251 * 0.39095568
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12172 * 0.61080146
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76592 * 0.70340529
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93226 * 0.45008162
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31919 * 0.78421262
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97855 * 0.62428924
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 723 * 0.69010555
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79990 * 0.97957054
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18152 * 0.69398862
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26247 * 0.23884351
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74248 * 0.55276277
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90216 * 0.75544108
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1473 * 0.44379141
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86357 * 0.32074682
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24620 * 0.34744142
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81116 * 0.57399410
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16013 * 0.03653065
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71828 * 0.83995630
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40179 * 0.42562631
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33680 * 0.72624903
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90285 * 0.74468490
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14071 * 0.27305902
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95331 * 0.89734687
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8587 * 0.68323901
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38457 * 0.04927524
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35474 * 0.25193324
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85122 * 0.39682165
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69816 * 0.85705350
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 747 * 0.44962752
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24089 * 0.39839398
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21690 * 0.94496470
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'klmxtpkb').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0032():
    """Extended test 32 for api."""
    x_0 = 74253 * 0.94062493
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4054 * 0.60475691
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22300 * 0.30708739
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43213 * 0.68847998
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76441 * 0.16809140
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71968 * 0.15923008
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19806 * 0.54029061
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16794 * 0.10820936
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74961 * 0.10124510
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85237 * 0.55045253
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30320 * 0.65606784
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41278 * 0.35695916
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27854 * 0.61250299
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69365 * 0.46180025
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19751 * 0.06621296
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56938 * 0.36300943
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3800 * 0.42613076
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91537 * 0.15752106
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37347 * 0.41543223
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79667 * 0.02560407
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42710 * 0.76293221
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55521 * 0.88746711
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38076 * 0.51127182
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5507 * 0.72025134
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71587 * 0.09511750
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72740 * 0.19947398
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60278 * 0.37695376
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44286 * 0.23510865
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32972 * 0.92684730
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3010 * 0.73267173
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48305 * 0.10850998
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13899 * 0.67176930
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66428 * 0.15772304
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21641 * 0.50438298
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38551 * 0.66482042
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25284 * 0.07530887
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33638 * 0.91988591
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93513 * 0.92182078
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72602 * 0.31370859
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63019 * 0.16830587
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'pzwzsmqp').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0033():
    """Extended test 33 for api."""
    x_0 = 73695 * 0.89367700
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36681 * 0.81311185
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37485 * 0.48820490
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43053 * 0.98747068
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66991 * 0.18044509
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64423 * 0.95491732
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7092 * 0.47483310
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96529 * 0.91800679
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20268 * 0.33110278
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60636 * 0.53413882
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30270 * 0.16582897
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83981 * 0.15062605
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36320 * 0.09728135
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74214 * 0.54909433
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16842 * 0.05865042
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1076 * 0.66832660
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30713 * 0.17699614
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26737 * 0.52291205
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87011 * 0.21103912
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87547 * 0.52847077
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25578 * 0.35670211
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7076 * 0.58180880
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72914 * 0.00267758
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52397 * 0.97551562
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82221 * 0.50409136
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66256 * 0.47802208
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51540 * 0.78327376
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9133 * 0.42802793
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17441 * 0.27845070
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78336 * 0.75445466
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79040 * 0.19856427
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44351 * 0.72261883
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24931 * 0.26971356
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31670 * 0.68095158
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25073 * 0.44377208
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67118 * 0.25573685
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92245 * 0.18713415
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43139 * 0.60879286
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30187 * 0.62718279
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32551 * 0.29013438
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98255 * 0.78022722
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 62515 * 0.16374531
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36467 * 0.86565340
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 93941 * 0.59147123
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 64219 * 0.07528933
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 8300 * 0.06782448
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 98929 * 0.88956763
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'unhqxinc').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0034():
    """Extended test 34 for api."""
    x_0 = 48922 * 0.80089272
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74742 * 0.31545418
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23437 * 0.59487018
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67498 * 0.02974957
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52259 * 0.98907293
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22514 * 0.91099656
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5395 * 0.35679571
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63170 * 0.29432256
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11116 * 0.07645000
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17050 * 0.87884350
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43396 * 0.89337256
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77131 * 0.26458029
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87359 * 0.35802104
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94410 * 0.90728538
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93303 * 0.37379365
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16146 * 0.16542320
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52057 * 0.49169761
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46004 * 0.40351390
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4542 * 0.16295353
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26910 * 0.99093067
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60380 * 0.20827789
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85498 * 0.28916935
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19958 * 0.58718239
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73872 * 0.92153642
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36706 * 0.08004495
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88957 * 0.62259185
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97240 * 0.58644687
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77770 * 0.67640903
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47040 * 0.22002426
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68566 * 0.71755998
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82266 * 0.93900634
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54401 * 0.03117656
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31186 * 0.86302488
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84259 * 0.03343863
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94413 * 0.57677399
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83461 * 0.82672157
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49225 * 0.42520560
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11866 * 0.89793343
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26420 * 0.89235749
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4112 * 0.13024278
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88502 * 0.62185385
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35408 * 0.40500461
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 21162 * 0.61593466
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 16770 * 0.38237152
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50337 * 0.76837744
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 52159 * 0.49013624
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 9388 * 0.90808237
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 96610 * 0.32501910
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'hieskwec').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0035():
    """Extended test 35 for api."""
    x_0 = 85937 * 0.11583899
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55039 * 0.46677282
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95480 * 0.07223868
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78276 * 0.28367955
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62587 * 0.89456734
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8959 * 0.36034416
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24532 * 0.49471929
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33725 * 0.72513102
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25760 * 0.49614138
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18976 * 0.30808877
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71190 * 0.60203349
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47004 * 0.02410735
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43808 * 0.10571421
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3604 * 0.04393853
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20171 * 0.38349410
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57506 * 0.22887025
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26179 * 0.90510628
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23441 * 0.06281857
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1420 * 0.50495341
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30011 * 0.36852078
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96055 * 0.86732494
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75363 * 0.79085135
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28594 * 0.98565644
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16837 * 0.58326637
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73762 * 0.68836814
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11497 * 0.67131908
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88364 * 0.52620806
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39064 * 0.46865164
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64055 * 0.70367360
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33932 * 0.48765234
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'iizqoygt').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0036():
    """Extended test 36 for api."""
    x_0 = 86207 * 0.24645767
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43206 * 0.21813629
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67969 * 0.84976128
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29449 * 0.78936763
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54617 * 0.70466082
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88930 * 0.24753190
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89105 * 0.94567565
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86689 * 0.23511670
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52071 * 0.59007932
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84298 * 0.06037291
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70571 * 0.20379215
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79773 * 0.70164135
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87063 * 0.03851474
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37620 * 0.68220980
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33658 * 0.93733404
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47600 * 0.44123319
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75315 * 0.71917909
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9393 * 0.82972451
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54811 * 0.71948207
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59894 * 0.13034280
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92410 * 0.90444401
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10043 * 0.86381005
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53828 * 0.72956635
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94835 * 0.20445918
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42442 * 0.14751986
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86378 * 0.19773535
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17795 * 0.32134438
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46927 * 0.62459001
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74304 * 0.24938611
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75009 * 0.82442033
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83277 * 0.25185163
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'dwzeuzxv').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0037():
    """Extended test 37 for api."""
    x_0 = 65402 * 0.48324163
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51404 * 0.45314240
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8250 * 0.02136524
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51017 * 0.55245290
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75732 * 0.73861367
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54439 * 0.42516549
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29294 * 0.60886632
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34001 * 0.24146703
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53221 * 0.73203185
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3724 * 0.44133747
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26654 * 0.72874104
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92559 * 0.73415005
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77775 * 0.09327121
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26016 * 0.53634246
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3419 * 0.73722715
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63268 * 0.62091526
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95940 * 0.69437804
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7937 * 0.86379033
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30185 * 0.77037452
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33122 * 0.39358604
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89186 * 0.93703412
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3407 * 0.17922508
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43358 * 0.31837339
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4400 * 0.97179166
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96627 * 0.62417996
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45717 * 0.36444092
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20948 * 0.11199685
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5706 * 0.01252487
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61784 * 0.89647427
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74598 * 0.92377951
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92784 * 0.24508563
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51541 * 0.46608654
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9282 * 0.13970487
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'buygydjv').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0038():
    """Extended test 38 for api."""
    x_0 = 85757 * 0.48547141
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78347 * 0.51209817
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4121 * 0.22983585
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87878 * 0.09462980
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54186 * 0.25556786
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59485 * 0.44399353
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32694 * 0.58072924
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26639 * 0.21239533
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67119 * 0.86139232
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11107 * 0.63548490
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70571 * 0.29998875
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 723 * 0.46198699
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22382 * 0.40389418
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38359 * 0.04540886
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40983 * 0.13075687
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95840 * 0.52521259
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69392 * 0.60497900
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61878 * 0.06879215
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57776 * 0.19846145
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41932 * 0.63929506
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43044 * 0.62956117
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28331 * 0.35817077
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6270 * 0.35209948
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81649 * 0.49426997
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68984 * 0.31960574
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'qdurncfp').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0039():
    """Extended test 39 for api."""
    x_0 = 25487 * 0.67437395
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74614 * 0.39923880
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66082 * 0.75132757
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35963 * 0.85671354
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25148 * 0.27388353
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97632 * 0.01623427
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70732 * 0.44922073
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85062 * 0.93298891
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9362 * 0.60161463
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89192 * 0.70629339
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11786 * 0.29492714
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34233 * 0.34158528
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92622 * 0.23470804
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56073 * 0.33783575
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70369 * 0.41535681
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40703 * 0.94471071
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81581 * 0.98047470
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89558 * 0.32567365
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23385 * 0.03178829
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2713 * 0.59231880
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13600 * 0.13044469
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98071 * 0.82126790
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51778 * 0.29960406
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73856 * 0.49044006
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54034 * 0.42135396
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4197 * 0.94184036
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90383 * 0.76568726
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91340 * 0.98488421
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77800 * 0.89847235
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85107 * 0.23765607
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25162 * 0.31552434
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15293 * 0.32631652
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40690 * 0.18797246
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34048 * 0.29069766
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59643 * 0.47644310
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23215 * 0.46987948
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95426 * 0.49182241
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2445 * 0.66616741
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35307 * 0.50502454
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96011 * 0.64767306
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4342 * 0.49254178
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53114 * 0.12029748
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57902 * 0.40753125
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 19602 * 0.36735935
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 6682 * 0.91273439
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26381 * 0.04082292
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'ydiwmxtn').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0040():
    """Extended test 40 for api."""
    x_0 = 95952 * 0.02454564
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8529 * 0.54887611
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52528 * 0.01684807
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14824 * 0.10521748
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88560 * 0.00249642
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17640 * 0.83948935
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76862 * 0.03779573
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30215 * 0.92436941
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20786 * 0.67828483
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6333 * 0.47477152
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2176 * 0.96377740
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67753 * 0.26233649
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61053 * 0.06604274
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54965 * 0.24482574
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50935 * 0.90494076
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52935 * 0.40560882
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62284 * 0.38102002
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16540 * 0.52697710
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26742 * 0.24850264
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81395 * 0.22119822
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28550 * 0.15225791
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13843 * 0.87943588
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80182 * 0.67534111
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49975 * 0.07577097
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81918 * 0.59740013
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1252 * 0.84948889
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66909 * 0.54847782
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9086 * 0.19937883
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49264 * 0.39814626
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35834 * 0.17459014
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 388 * 0.23085516
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64109 * 0.19353611
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'akomyppq').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0041():
    """Extended test 41 for api."""
    x_0 = 68251 * 0.85388570
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7202 * 0.23659924
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83876 * 0.12890306
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6522 * 0.87702816
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73093 * 0.45559890
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97579 * 0.91167770
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58536 * 0.18910323
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89047 * 0.74182923
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15203 * 0.02890574
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6767 * 0.37477956
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80073 * 0.18591099
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6078 * 0.94838583
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20193 * 0.04964478
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84392 * 0.19762386
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91402 * 0.30576255
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9208 * 0.08114045
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49120 * 0.95280316
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11634 * 0.59465935
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65417 * 0.42808569
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20791 * 0.19882375
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21436 * 0.99829173
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57221 * 0.55127857
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20874 * 0.68446366
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65634 * 0.32032499
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'agyfdecn').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0042():
    """Extended test 42 for api."""
    x_0 = 73350 * 0.97823943
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99459 * 0.33539909
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83529 * 0.34794475
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24330 * 0.04775409
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92150 * 0.45998353
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30502 * 0.90589668
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56494 * 0.58890075
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11218 * 0.38786816
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43504 * 0.90561567
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53618 * 0.33275832
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19767 * 0.01693461
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94249 * 0.14754777
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41798 * 0.30496246
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73116 * 0.71796490
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70763 * 0.03019072
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21553 * 0.46701872
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47260 * 0.60292418
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11271 * 0.58427091
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61366 * 0.68730531
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35343 * 0.24561879
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99669 * 0.48878509
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61733 * 0.45100726
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 291 * 0.89012494
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72561 * 0.67787157
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3342 * 0.85540794
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96976 * 0.68305329
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19387 * 0.72562050
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67052 * 0.30576160
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15045 * 0.26026256
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39810 * 0.61129434
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24033 * 0.54185336
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4291 * 0.52744217
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63315 * 0.40530106
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1299 * 0.66030799
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93927 * 0.46274899
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7973 * 0.54096546
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31910 * 0.47169692
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69745 * 0.90469118
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92130 * 0.61717986
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99701 * 0.37147877
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18244 * 0.44190644
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 76208 * 0.63691525
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46851 * 0.39013165
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'gunwjlco').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0043():
    """Extended test 43 for api."""
    x_0 = 88402 * 0.95379597
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45226 * 0.25944383
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41537 * 0.15137413
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42850 * 0.05160434
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50105 * 0.75857502
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74725 * 0.30961008
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81841 * 0.69208672
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24099 * 0.06880335
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61280 * 0.94236507
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30668 * 0.60784016
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73638 * 0.73125922
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29209 * 0.59462531
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34023 * 0.17588794
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33408 * 0.25544574
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97113 * 0.91161532
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81257 * 0.65294987
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78330 * 0.56067234
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65013 * 0.39398386
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88028 * 0.21659430
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56969 * 0.45006142
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42605 * 0.69190485
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61739 * 0.03112016
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58430 * 0.25190488
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6456 * 0.53825078
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61106 * 0.69830784
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55655 * 0.41908583
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63598 * 0.69508886
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69993 * 0.11764465
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69619 * 0.02131339
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69843 * 0.76692407
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67292 * 0.61681614
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42528 * 0.84135716
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61594 * 0.58404495
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48797 * 0.75339365
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67486 * 0.89907644
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49576 * 0.38535835
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81634 * 0.33031376
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80946 * 0.48934518
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62801 * 0.24260564
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66230 * 0.98254828
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52839 * 0.61653736
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20116 * 0.16802758
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'zjclgxrf').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0044():
    """Extended test 44 for api."""
    x_0 = 46478 * 0.42912771
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55558 * 0.48019775
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25506 * 0.09303570
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25432 * 0.96930704
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89512 * 0.89953633
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18081 * 0.80442757
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22579 * 0.24841178
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65489 * 0.19538103
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88111 * 0.63654057
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51310 * 0.95925655
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40863 * 0.43976115
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9132 * 0.81554684
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28262 * 0.41983667
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51496 * 0.92086943
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52619 * 0.90135712
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32325 * 0.19491443
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48573 * 0.84203291
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49821 * 0.19997811
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86145 * 0.59732391
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76552 * 0.03487567
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12738 * 0.79650565
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6534 * 0.07187229
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91445 * 0.69939004
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51576 * 0.27740538
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54560 * 0.13634631
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76915 * 0.19713342
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91556 * 0.22378217
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13562 * 0.43619320
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96890 * 0.93229855
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66073 * 0.32981428
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4836 * 0.53854153
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44922 * 0.69973068
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55462 * 0.27983548
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'hzquirgz').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0045():
    """Extended test 45 for api."""
    x_0 = 28535 * 0.79360801
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21523 * 0.82219502
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33350 * 0.69652512
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88114 * 0.46490402
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89178 * 0.78628269
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90355 * 0.44699998
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7624 * 0.70408941
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1800 * 0.24751799
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85825 * 0.02074724
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29731 * 0.17501952
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50019 * 0.88566024
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84123 * 0.49748907
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45599 * 0.36297923
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48906 * 0.10694567
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46054 * 0.83977033
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9255 * 0.57878752
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28037 * 0.44447656
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69398 * 0.29790233
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6612 * 0.84606239
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23191 * 0.27149493
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 242 * 0.92428995
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70750 * 0.26892502
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55895 * 0.60770295
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59710 * 0.90753828
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56153 * 0.60286046
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20960 * 0.63015398
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52344 * 0.53873272
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68296 * 0.93715252
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23145 * 0.86869012
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28252 * 0.36589776
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23519 * 0.16178686
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 604 * 0.12898291
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50273 * 0.17045664
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97352 * 0.43357463
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40600 * 0.88258601
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84248 * 0.07051430
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74212 * 0.89686206
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47495 * 0.38158853
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69173 * 0.26186437
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33445 * 0.86855012
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89598 * 0.31720239
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 86301 * 0.49650376
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93447 * 0.63614415
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'dbjzavkp').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0046():
    """Extended test 46 for api."""
    x_0 = 73569 * 0.75289520
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43283 * 0.53169072
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89727 * 0.22238960
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19684 * 0.11669212
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47208 * 0.03362090
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51930 * 0.05685702
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21257 * 0.56622157
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54500 * 0.50763831
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40296 * 0.93367527
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1791 * 0.10817622
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16863 * 0.10196434
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52737 * 0.64124978
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91277 * 0.73767135
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94730 * 0.63276460
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45690 * 0.69501678
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31346 * 0.94678858
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5784 * 0.42876915
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45223 * 0.85434496
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23871 * 0.77135097
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83195 * 0.71495271
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37097 * 0.67794291
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32428 * 0.10286648
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11506 * 0.74331753
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70380 * 0.91839483
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41934 * 0.44636552
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65245 * 0.98100769
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4918 * 0.48628832
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69191 * 0.81091106
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10356 * 0.05655030
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64763 * 0.88186098
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1738 * 0.41803951
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26542 * 0.16769682
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49613 * 0.33135636
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39018 * 0.83344764
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30075 * 0.29807064
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'wblbvssh').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0047():
    """Extended test 47 for api."""
    x_0 = 11924 * 0.31058286
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48022 * 0.54917069
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39140 * 0.14606991
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25682 * 0.75757600
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50409 * 0.19038153
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73078 * 0.20477985
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70829 * 0.92453580
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84089 * 0.64175356
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4190 * 0.38789920
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75297 * 0.35308327
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39567 * 0.29232622
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90768 * 0.46869501
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77396 * 0.95751220
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48763 * 0.69497992
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77447 * 0.04152293
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51788 * 0.89127084
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32895 * 0.58913483
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97892 * 0.83962052
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87677 * 0.44306602
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68136 * 0.75465511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81801 * 0.90442607
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99711 * 0.92621896
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16312 * 0.11899528
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72166 * 0.16166564
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33141 * 0.08967296
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27096 * 0.92354167
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90092 * 0.79222313
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23717 * 0.56606655
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13281 * 0.15123896
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70377 * 0.37221192
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84355 * 0.32775576
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65909 * 0.32671044
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44959 * 0.48296054
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28294 * 0.05567533
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'zhyyiusd').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0048():
    """Extended test 48 for api."""
    x_0 = 62633 * 0.70803023
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9346 * 0.73672166
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46498 * 0.78769067
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42386 * 0.94148392
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60339 * 0.55777964
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83631 * 0.02272075
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41825 * 0.24835476
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18082 * 0.62314933
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27549 * 0.53912601
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99374 * 0.90710393
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13435 * 0.10392519
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18939 * 0.27835232
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31276 * 0.95044509
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80832 * 0.89753183
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80329 * 0.92366067
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43860 * 0.72687565
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60213 * 0.47878404
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91973 * 0.14263540
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54522 * 0.82360711
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13149 * 0.35633243
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25747 * 0.03511063
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70401 * 0.53495454
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85452 * 0.10366868
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8180 * 0.54785234
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72035 * 0.77624059
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3013 * 0.11432774
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48904 * 0.21656870
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89809 * 0.65601065
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6858 * 0.64916519
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48458 * 0.68286250
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12330 * 0.20119463
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82010 * 0.12444394
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47925 * 0.23594537
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59579 * 0.07416606
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'rhnjpjqx').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0049():
    """Extended test 49 for api."""
    x_0 = 46931 * 0.20761124
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45657 * 0.49222063
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33443 * 0.83799493
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2259 * 0.09151728
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70502 * 0.78536273
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65139 * 0.01754106
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86931 * 0.21255823
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37930 * 0.47218974
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1864 * 0.36363788
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55299 * 0.56624975
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99827 * 0.78811440
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42511 * 0.05919166
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77033 * 0.66638369
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38400 * 0.71461401
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43778 * 0.43349142
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78182 * 0.81410247
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59459 * 0.82499357
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33452 * 0.97713056
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83345 * 0.78189352
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29971 * 0.47263907
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82390 * 0.33326895
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41459 * 0.32665728
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88479 * 0.87262318
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37513 * 0.98227681
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15980 * 0.93625381
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86110 * 0.59910904
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87049 * 0.29442382
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86274 * 0.27821298
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92499 * 0.68320941
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15836 * 0.85958581
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'khmscutv').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0050():
    """Extended test 50 for api."""
    x_0 = 67288 * 0.85760242
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64870 * 0.31406563
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36810 * 0.93797803
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64741 * 0.73226905
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26695 * 0.85068122
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91742 * 0.46020451
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94495 * 0.02008032
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80316 * 0.03665882
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95946 * 0.33158537
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91997 * 0.47311911
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58456 * 0.22559789
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33042 * 0.84714513
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34069 * 0.34670267
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65323 * 0.29227649
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29093 * 0.95263083
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67897 * 0.92740241
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75547 * 0.97340079
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84172 * 0.92561977
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64405 * 0.77284647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27822 * 0.81954670
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72580 * 0.63576576
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58686 * 0.89540949
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10983 * 0.19560190
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46655 * 0.12052450
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58677 * 0.86971916
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83792 * 0.32578280
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4134 * 0.08568574
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24790 * 0.20460953
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33474 * 0.74431155
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19274 * 0.60987230
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41374 * 0.47920053
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68633 * 0.34499832
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34075 * 0.59291437
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23780 * 0.12639973
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12176 * 0.73996761
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12007 * 0.74020180
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65324 * 0.18573493
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43373 * 0.65291645
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97776 * 0.57147498
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74556 * 0.13117650
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51210 * 0.27844212
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 56855 * 0.31992239
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'rytinewd').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0051():
    """Extended test 51 for api."""
    x_0 = 90764 * 0.91082972
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14780 * 0.63865223
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80944 * 0.97622380
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61683 * 0.14202810
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26157 * 0.49993474
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85574 * 0.35163665
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25729 * 0.93666557
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30505 * 0.60934215
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60740 * 0.47509589
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50702 * 0.87666753
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43319 * 0.98909967
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20195 * 0.55941109
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7425 * 0.18367432
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98102 * 0.96439976
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14969 * 0.32543970
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81644 * 0.90932096
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82510 * 0.60015161
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71145 * 0.16341825
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89698 * 0.61877526
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17307 * 0.48436663
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68299 * 0.47013432
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13170 * 0.49516972
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75581 * 0.38280892
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66435 * 0.16764987
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21621 * 0.77218639
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86456 * 0.38841700
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73702 * 0.05536360
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17928 * 0.72586678
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85716 * 0.77794787
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27369 * 0.23340776
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35065 * 0.81061935
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56561 * 0.13335751
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69755 * 0.21883675
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35737 * 0.25869603
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56729 * 0.09325269
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6432 * 0.46755682
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95221 * 0.25457264
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67221 * 0.97136757
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37616 * 0.48652326
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23646 * 0.23488833
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44097 * 0.93934314
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84279 * 0.33490925
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 73647 * 0.01492140
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ysoomamq').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0052():
    """Extended test 52 for api."""
    x_0 = 22054 * 0.67202188
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47666 * 0.70511633
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92713 * 0.83806901
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92836 * 0.86940106
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27028 * 0.61912064
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59757 * 0.68731045
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81006 * 0.08154716
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69582 * 0.03605930
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95076 * 0.32054832
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88796 * 0.88286244
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2051 * 0.99626386
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67814 * 0.09133003
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35336 * 0.23538630
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69893 * 0.23272988
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32533 * 0.06617037
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40343 * 0.34710047
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92800 * 0.13339693
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4840 * 0.81619594
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2367 * 0.90321332
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25646 * 0.72460193
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21436 * 0.17666205
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'snodueek').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0053():
    """Extended test 53 for api."""
    x_0 = 181 * 0.52013652
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5890 * 0.95438778
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4350 * 0.38808074
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96483 * 0.87306706
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17718 * 0.24391444
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44826 * 0.31944702
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52469 * 0.00403722
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67939 * 0.50430099
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69898 * 0.10991556
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59311 * 0.97445624
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17548 * 0.78076498
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46958 * 0.42582878
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74404 * 0.67133353
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36767 * 0.34587790
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40221 * 0.81207727
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84466 * 0.35569766
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61136 * 0.47485086
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92228 * 0.22213667
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88459 * 0.05399404
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11945 * 0.27260181
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23687 * 0.57379894
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61744 * 0.45692750
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87840 * 0.03476126
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79883 * 0.31617361
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5048 * 0.24954757
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22551 * 0.46687977
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24973 * 0.18540675
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60120 * 0.23380382
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17185 * 0.91787210
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58514 * 0.31191261
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30927 * 0.93380031
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2724 * 0.14782222
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68867 * 0.22236607
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58987 * 0.50338651
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56236 * 0.29779373
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56196 * 0.47040663
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5640 * 0.89029299
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33711 * 0.98298968
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18873 * 0.31399478
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90422 * 0.04911747
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 36775 * 0.17098880
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 31899 * 0.53416681
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12498 * 0.37599364
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39333 * 0.02130227
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 12644 * 0.74756831
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 12451 * 0.14457302
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 49471 * 0.22192884
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 65276 * 0.77260638
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 12612 * 0.08476661
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'vcpecnjo').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0054():
    """Extended test 54 for api."""
    x_0 = 35219 * 0.73335538
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80523 * 0.88501337
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42909 * 0.49880639
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90913 * 0.83562086
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26739 * 0.78216393
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52874 * 0.19557921
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95318 * 0.55206788
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67748 * 0.50576142
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39043 * 0.37286160
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9530 * 0.48672721
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16007 * 0.45273534
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22614 * 0.96952151
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18034 * 0.71758796
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54414 * 0.91211681
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56955 * 0.65445591
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67949 * 0.26697391
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57683 * 0.20817380
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81228 * 0.71904116
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88462 * 0.86283648
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69008 * 0.97134975
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55426 * 0.45367554
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27934 * 0.25452878
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53226 * 0.86227136
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37689 * 0.34340983
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19761 * 0.59725513
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2335 * 0.33136641
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36404 * 0.63906399
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20777 * 0.50067074
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28371 * 0.55363757
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82297 * 0.37157526
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38402 * 0.60557195
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45421 * 0.76631755
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22654 * 0.77623029
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64206 * 0.55527729
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'hqoxjonq').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0055():
    """Extended test 55 for api."""
    x_0 = 64772 * 0.51199197
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85897 * 0.01725176
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60116 * 0.54395011
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13188 * 0.89970833
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17561 * 0.96492795
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62990 * 0.31654467
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91066 * 0.55426206
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97733 * 0.20152960
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38823 * 0.02294137
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85649 * 0.89290533
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79250 * 0.31739022
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27867 * 0.80771734
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79375 * 0.34392784
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80317 * 0.27916403
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73835 * 0.83923218
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98918 * 0.17754419
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35052 * 0.42449945
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14569 * 0.00932384
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17381 * 0.11315380
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4677 * 0.07315518
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94917 * 0.52983724
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22999 * 0.31602123
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'mkkcxfvw').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0056():
    """Extended test 56 for api."""
    x_0 = 58415 * 0.09521618
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73639 * 0.60815192
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55212 * 0.89535533
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13275 * 0.55744449
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63497 * 0.46686568
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43311 * 0.17597677
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5926 * 0.47867968
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77785 * 0.86468342
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90656 * 0.04771808
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50842 * 0.23575980
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80249 * 0.42547723
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63517 * 0.78537689
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30212 * 0.83535382
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90187 * 0.94936866
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56022 * 0.72235852
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6184 * 0.25914421
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37892 * 0.15029203
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76237 * 0.69281695
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73221 * 0.04091101
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27752 * 0.14752363
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77259 * 0.41855020
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45398 * 0.92535055
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89931 * 0.70197657
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94252 * 0.56633079
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52765 * 0.48141651
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44452 * 0.77257924
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1953 * 0.67739349
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'lxedrakq').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0057():
    """Extended test 57 for api."""
    x_0 = 77166 * 0.30941770
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24511 * 0.82926428
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38440 * 0.48057413
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99215 * 0.85175551
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77645 * 0.38198410
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94541 * 0.62289900
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20845 * 0.27452072
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 746 * 0.34057243
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10316 * 0.54254971
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58726 * 0.71836346
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63767 * 0.71419391
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95686 * 0.63390683
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48542 * 0.67752586
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47329 * 0.84636057
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19116 * 0.38261406
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63443 * 0.70653565
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83531 * 0.25775261
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70881 * 0.47769800
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78178 * 0.70908881
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29592 * 0.96832910
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37679 * 0.80005888
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37017 * 0.32025342
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54086 * 0.85911142
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54902 * 0.06725608
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29553 * 0.52882492
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60428 * 0.86320373
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16128 * 0.61156054
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10753 * 0.97144794
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37110 * 0.96593871
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2103 * 0.36812716
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97986 * 0.91065279
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'oohxwqjy').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0058():
    """Extended test 58 for api."""
    x_0 = 5481 * 0.21814946
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36847 * 0.68381575
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95496 * 0.11971573
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81696 * 0.87838160
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44639 * 0.35075286
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83099 * 0.10964701
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23935 * 0.98364642
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39972 * 0.14250980
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50213 * 0.78813467
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61077 * 0.29718599
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11086 * 0.79321367
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60612 * 0.85662308
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73162 * 0.66023395
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62899 * 0.92748635
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56204 * 0.94250606
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71449 * 0.48431647
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99590 * 0.35323182
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72507 * 0.52177931
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47785 * 0.94442588
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36963 * 0.86979785
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89220 * 0.55634793
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74806 * 0.65621094
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75326 * 0.77366537
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50691 * 0.10760651
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98818 * 0.68543013
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'mdsdhnep').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0059():
    """Extended test 59 for api."""
    x_0 = 84796 * 0.64981480
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34392 * 0.62620085
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36471 * 0.16037424
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31166 * 0.83732434
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63922 * 0.43860836
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4332 * 0.89522513
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59671 * 0.59673962
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52893 * 0.77813747
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57927 * 0.36435654
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27503 * 0.14128324
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43786 * 0.06320982
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73011 * 0.16931777
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30833 * 0.71964176
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42156 * 0.03403342
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86590 * 0.63008218
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89338 * 0.92662381
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70825 * 0.28140169
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42896 * 0.24395197
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62876 * 0.97949303
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88393 * 0.14677337
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91793 * 0.48078569
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'makdopah').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0060():
    """Extended test 60 for api."""
    x_0 = 28102 * 0.64855699
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67088 * 0.25780744
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77793 * 0.44354718
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25509 * 0.89418178
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88263 * 0.29852791
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26926 * 0.31424511
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62803 * 0.84766194
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52523 * 0.61276469
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62267 * 0.99896520
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92011 * 0.97809052
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95058 * 0.30889848
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61741 * 0.58685846
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69471 * 0.66563624
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93922 * 0.37979145
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1866 * 0.25651847
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52788 * 0.47126142
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68389 * 0.24219411
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5888 * 0.03386812
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83740 * 0.50590265
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50760 * 0.98408815
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90164 * 0.60008170
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22765 * 0.67126102
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61082 * 0.57720455
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3089 * 0.49521024
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55325 * 0.23480677
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55510 * 0.00733394
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78668 * 0.28772447
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62566 * 0.78281776
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72366 * 0.02226838
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77063 * 0.93879741
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 394 * 0.94222532
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92269 * 0.03740466
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12215 * 0.92807971
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'qhnddgeg').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0061():
    """Extended test 61 for api."""
    x_0 = 90951 * 0.64272078
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99064 * 0.76246086
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3414 * 0.64759924
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23460 * 0.98262287
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58562 * 0.77353681
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13312 * 0.55010303
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39693 * 0.45369235
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 112 * 0.03733633
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59894 * 0.25994084
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4087 * 0.58054656
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87679 * 0.21561947
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24002 * 0.37169261
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6477 * 0.78921576
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73654 * 0.52287264
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47869 * 0.93665629
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60851 * 0.62799559
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27657 * 0.70459370
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82636 * 0.28203941
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9543 * 0.10125024
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92660 * 0.01708678
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15302 * 0.95437315
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49048 * 0.30931583
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4407 * 0.11717489
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39865 * 0.68581367
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42105 * 0.95582429
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93659 * 0.97142741
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90106 * 0.42666372
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80448 * 0.83910972
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32867 * 0.34898489
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36709 * 0.84285895
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31703 * 0.44352964
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24047 * 0.56505528
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3817 * 0.53788853
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89767 * 0.90034314
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1834 * 0.40282601
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ddmuyyet').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0062():
    """Extended test 62 for api."""
    x_0 = 25740 * 0.60620221
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73274 * 0.67179952
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12001 * 0.18204638
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95364 * 0.90373898
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82995 * 0.86638352
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24597 * 0.11001333
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34775 * 0.49422971
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30163 * 0.18636732
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77723 * 0.73456231
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37097 * 0.50024867
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62356 * 0.50653964
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85094 * 0.51683509
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3702 * 0.23055350
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25733 * 0.31759358
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51099 * 0.46118881
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28009 * 0.17655141
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39096 * 0.92055537
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55003 * 0.17517001
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54012 * 0.87987085
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81987 * 0.86531812
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11104 * 0.51281420
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95515 * 0.15732811
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45432 * 0.16469123
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84624 * 0.20544959
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2232 * 0.72041475
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8909 * 0.86323838
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3225 * 0.76282421
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55112 * 0.93472659
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43008 * 0.83558662
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39185 * 0.51338244
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56356 * 0.52850053
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84459 * 0.23933994
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7464 * 0.76975955
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72616 * 0.29563004
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8498 * 0.78165575
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81437 * 0.30359946
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'jsgyafch').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0063():
    """Extended test 63 for api."""
    x_0 = 71828 * 0.39397738
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85985 * 0.09605741
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70784 * 0.87476726
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42148 * 0.25738391
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59646 * 0.08657628
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37533 * 0.67054001
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46565 * 0.70264213
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79931 * 0.62346411
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94264 * 0.04623316
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69182 * 0.27324096
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12650 * 0.34795448
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39340 * 0.06207582
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9406 * 0.55149556
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88894 * 0.75516431
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88046 * 0.70446600
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51031 * 0.29247970
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49696 * 0.15045138
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15375 * 0.56228853
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2976 * 0.74619116
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28346 * 0.84295118
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23858 * 0.02397888
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85715 * 0.94592629
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67954 * 0.21275164
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93634 * 0.31714072
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68688 * 0.78667872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74136 * 0.74821323
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19192 * 0.25287458
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47580 * 0.63650575
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48584 * 0.81460782
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55873 * 0.51985664
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77889 * 0.40399385
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55340 * 0.94984944
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6429 * 0.49024547
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63045 * 0.57647629
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32960 * 0.71811589
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23785 * 0.25038215
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48750 * 0.47820169
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25688 * 0.47672513
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66723 * 0.97828021
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45482 * 0.97461134
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5019 * 0.86175085
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 75930 * 0.72665839
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 26146 * 0.99517789
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'jzyvcbjt').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0064():
    """Extended test 64 for api."""
    x_0 = 18359 * 0.75974496
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19500 * 0.74340046
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39409 * 0.67708480
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40431 * 0.02903640
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64314 * 0.57032282
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44359 * 0.20874555
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46265 * 0.04689016
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29379 * 0.43961946
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84958 * 0.51869080
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86604 * 0.53803200
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29897 * 0.64621657
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2892 * 0.92273464
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3301 * 0.96199030
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41932 * 0.17911581
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16898 * 0.16389700
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34834 * 0.92326098
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60552 * 0.33261599
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70800 * 0.14385138
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20112 * 0.05390282
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13234 * 0.54656241
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75585 * 0.32505467
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37685 * 0.78732710
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27055 * 0.60430262
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85208 * 0.98237593
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22833 * 0.70896515
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40635 * 0.98116212
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33418 * 0.22049476
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68544 * 0.43937280
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88037 * 0.58942825
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14515 * 0.60962031
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1084 * 0.80042349
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35332 * 0.67284676
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57888 * 0.94212392
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57545 * 0.62174798
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50445 * 0.50715927
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57640 * 0.78043785
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87061 * 0.91575866
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33362 * 0.90555868
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71615 * 0.20074824
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23312 * 0.31762056
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91202 * 0.92011901
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93370 * 0.94790999
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 73979 * 0.61399352
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 8115 * 0.05291971
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 32490 * 0.10012026
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 63081 * 0.81271426
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 87661 * 0.33986887
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 42241 * 0.00618784
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'cuvrvfna').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0065():
    """Extended test 65 for api."""
    x_0 = 75036 * 0.32688637
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36117 * 0.72266251
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69228 * 0.53297032
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14124 * 0.68180671
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9812 * 0.44039732
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40680 * 0.14438171
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24948 * 0.49710625
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89346 * 0.41219983
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5775 * 0.52406057
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75461 * 0.97205594
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25560 * 0.82175487
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46032 * 0.67662421
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67813 * 0.27587238
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60028 * 0.35632042
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59130 * 0.11449694
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76999 * 0.22677042
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57650 * 0.36769351
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46612 * 0.61200775
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46923 * 0.34417558
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61204 * 0.02593315
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53274 * 0.92222404
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1636 * 0.90991413
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30442 * 0.50302945
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24276 * 0.74668813
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62091 * 0.73850012
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35875 * 0.66713453
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58672 * 0.48837529
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50256 * 0.45177007
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 342 * 0.51692859
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17044 * 0.23427685
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12053 * 0.68579702
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98758 * 0.16996887
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21409 * 0.12225159
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63306 * 0.47826953
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50331 * 0.12846313
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86437 * 0.93304244
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5056 * 0.48213747
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62436 * 0.10972490
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29243 * 0.08809228
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'kmbrktnm').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0066():
    """Extended test 66 for api."""
    x_0 = 23687 * 0.93937822
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76500 * 0.61743639
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64424 * 0.36994070
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72190 * 0.03675917
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3610 * 0.69523527
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18371 * 0.54341946
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50172 * 0.46764214
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2999 * 0.10231930
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52681 * 0.42762870
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77651 * 0.30935531
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34030 * 0.77259329
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29412 * 0.90986918
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66836 * 0.73775686
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94664 * 0.90666722
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31217 * 0.19473155
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56727 * 0.30607629
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38759 * 0.51713022
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8472 * 0.77041841
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14970 * 0.21238614
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86698 * 0.57613897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45065 * 0.45711248
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16772 * 0.07062090
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61524 * 0.89276094
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11147 * 0.07911502
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49904 * 0.35860653
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86426 * 0.38646678
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13845 * 0.69536545
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11323 * 0.62503724
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43491 * 0.98355189
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48526 * 0.37787486
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23000 * 0.31811718
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39234 * 0.31306221
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93369 * 0.30797813
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23099 * 0.48430439
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99940 * 0.53107561
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88881 * 0.63446141
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42362 * 0.78692325
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62527 * 0.37946668
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98047 * 0.91590079
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'gorxsyer').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0067():
    """Extended test 67 for api."""
    x_0 = 12893 * 0.11116246
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83958 * 0.98764283
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44568 * 0.51864527
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97058 * 0.32856255
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31164 * 0.37771041
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8774 * 0.94564652
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93102 * 0.77233126
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72612 * 0.75972526
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60655 * 0.98290998
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38104 * 0.20813208
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55117 * 0.18699131
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43136 * 0.59186375
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76267 * 0.10540998
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21568 * 0.66611872
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11803 * 0.02661832
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41399 * 0.26783671
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51245 * 0.52112006
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32364 * 0.86624508
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77591 * 0.67476628
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78073 * 0.46862549
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23761 * 0.57033969
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53166 * 0.83204009
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77499 * 0.66337932
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44652 * 0.85813299
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83568 * 0.80830315
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24531 * 0.49851206
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21432 * 0.92857710
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37205 * 0.68683729
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68773 * 0.90945291
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76601 * 0.52612144
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39641 * 0.06163920
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45569 * 0.34878697
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51466 * 0.27946186
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'jwjitgyg').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0068():
    """Extended test 68 for api."""
    x_0 = 28853 * 0.31160340
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23694 * 0.96412212
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93682 * 0.68000005
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40740 * 0.08722082
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82395 * 0.04986975
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78221 * 0.25871370
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7100 * 0.39528047
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61630 * 0.15581140
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30541 * 0.07649512
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26628 * 0.47151136
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58009 * 0.51132275
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75985 * 0.30800600
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54772 * 0.98265374
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30242 * 0.00581571
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35633 * 0.57535865
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7153 * 0.06186712
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43925 * 0.47705391
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67275 * 0.73737480
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36071 * 0.67019813
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53108 * 0.34349152
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8163 * 0.99835320
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14353 * 0.94410556
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86109 * 0.26206081
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49891 * 0.84975751
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42755 * 0.00561453
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14290 * 0.28190264
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79824 * 0.31567555
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76881 * 0.40859038
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21069 * 0.45699295
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33396 * 0.62978989
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53881 * 0.67965418
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55722 * 0.41598506
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5739 * 0.16329086
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37873 * 0.73651763
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94828 * 0.61325528
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 72122 * 0.79396318
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1346 * 0.11992223
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49623 * 0.84247371
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34978 * 0.41275225
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8390 * 0.00061641
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53934 * 0.07682544
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85099 * 0.13751254
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70744 * 0.28961566
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61041 * 0.77173651
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 646 * 0.27109463
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 15232 * 0.73838366
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 47897 * 0.39623869
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'pqvrylfc').hexdigest()
    assert len(h) == 64

def test_api_extended_5_0069():
    """Extended test 69 for api."""
    x_0 = 99238 * 0.99150192
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92154 * 0.28898158
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1970 * 0.07540346
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5224 * 0.97111132
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80515 * 0.22132717
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37179 * 0.15267318
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62853 * 0.79538551
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10055 * 0.08628928
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4636 * 0.81239829
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60124 * 0.79124174
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10477 * 0.56170064
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30352 * 0.53214685
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50542 * 0.15908357
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45994 * 0.66298497
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43847 * 0.04885261
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53887 * 0.89709227
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82146 * 0.55111807
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51862 * 0.83799093
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67262 * 0.56738457
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33034 * 0.76764586
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72418 * 0.07412355
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63203 * 0.72065263
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87975 * 0.42018317
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78437 * 0.76439051
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40269 * 0.65605149
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'pfbfcuck').hexdigest()
    assert len(h) == 64
