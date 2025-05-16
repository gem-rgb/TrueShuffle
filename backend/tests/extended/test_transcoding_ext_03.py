"""Extended tests for transcoding suite 3."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_transcoding_extended_3_0000():
    """Extended test 0 for transcoding."""
    x_0 = 41356 * 0.21066549
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46975 * 0.50046747
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36273 * 0.45070160
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75063 * 0.07588041
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79826 * 0.33944450
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68846 * 0.40036778
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55969 * 0.33699798
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65702 * 0.09332141
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25835 * 0.79090877
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61385 * 0.83872423
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21648 * 0.84441481
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67644 * 0.12136181
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99975 * 0.60247809
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73022 * 0.41507939
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19283 * 0.68745659
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 243 * 0.92262134
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47328 * 0.86469024
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50019 * 0.83247873
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3353 * 0.44290092
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25169 * 0.01643007
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70959 * 0.21460892
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43020 * 0.79937489
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49910 * 0.62264128
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37865 * 0.27527863
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58071 * 0.00703344
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29524 * 0.40519531
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10794 * 0.83870092
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63423 * 0.70176216
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45611 * 0.98662285
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35087 * 0.46750113
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78510 * 0.19034588
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36158 * 0.26241392
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51910 * 0.92320350
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16971 * 0.11580710
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69423 * 0.09294394
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15576 * 0.50673876
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18606 * 0.39296632
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24595 * 0.71998471
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96417 * 0.16209505
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'efjggsyk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0001():
    """Extended test 1 for transcoding."""
    x_0 = 40849 * 0.51229805
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20189 * 0.53470978
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13574 * 0.56211764
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59099 * 0.41203397
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64046 * 0.70744564
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79181 * 0.11290513
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7305 * 0.15593629
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62176 * 0.38918792
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13457 * 0.40926030
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7954 * 0.51943335
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66737 * 0.85278567
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40550 * 0.34058076
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14873 * 0.35564529
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17679 * 0.85417647
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30748 * 0.79307024
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84262 * 0.22359234
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4280 * 0.22471209
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22931 * 0.79847380
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53762 * 0.62071930
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13797 * 0.37346040
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23800 * 0.05001945
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67277 * 0.26892883
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79208 * 0.48824136
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40878 * 0.36289075
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53147 * 0.29805597
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31167 * 0.25261258
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'ymkfrtsf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0002():
    """Extended test 2 for transcoding."""
    x_0 = 79996 * 0.65383257
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80180 * 0.61401695
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77660 * 0.90368535
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50291 * 0.71364717
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94740 * 0.23661823
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55459 * 0.35849119
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45820 * 0.56372588
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93995 * 0.80455962
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65142 * 0.62692236
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18663 * 0.63976374
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19031 * 0.63677335
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2744 * 0.09033666
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9726 * 0.14595478
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23085 * 0.42268065
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65558 * 0.06357364
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2708 * 0.14453755
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28950 * 0.81084713
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79705 * 0.91923626
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12985 * 0.98498996
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83885 * 0.93572374
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48840 * 0.29963128
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18027 * 0.15149096
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81376 * 0.18070509
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43857 * 0.68737402
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24470 * 0.94006524
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73704 * 0.24441845
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74739 * 0.26092072
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22465 * 0.82974908
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55445 * 0.51370954
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96187 * 0.52088025
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35984 * 0.76605945
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49423 * 0.50442536
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93101 * 0.76890657
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83820 * 0.27522926
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41447 * 0.18727312
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47184 * 0.66213026
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15020 * 0.86191291
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34939 * 0.67987840
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17830 * 0.05493817
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34930 * 0.73338760
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 31052 * 0.85053992
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50188 * 0.85895534
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'jozhpzxp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0003():
    """Extended test 3 for transcoding."""
    x_0 = 87153 * 0.67705013
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94033 * 0.26978338
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59970 * 0.38696731
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6384 * 0.02662165
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90085 * 0.74900723
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99044 * 0.88578073
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34496 * 0.43621131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36920 * 0.53167955
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68896 * 0.97779831
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61491 * 0.06755889
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42117 * 0.14052613
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30022 * 0.69238010
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67297 * 0.82868231
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94217 * 0.41292774
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16825 * 0.85486429
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16589 * 0.09116643
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75925 * 0.09635422
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59139 * 0.07139560
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2110 * 0.37759329
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90832 * 0.22165686
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'rvdjjujt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0004():
    """Extended test 4 for transcoding."""
    x_0 = 65709 * 0.20324689
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31368 * 0.03640103
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40897 * 0.51795633
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44040 * 0.30033164
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42315 * 0.43782095
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2233 * 0.35111650
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18470 * 0.59206016
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73714 * 0.99413984
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90578 * 0.35881083
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14284 * 0.19518189
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37003 * 0.21076469
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87038 * 0.02777204
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35317 * 0.12383245
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76311 * 0.77063384
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57226 * 0.91148585
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64941 * 0.61224414
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19181 * 0.00420143
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19245 * 0.65856437
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84486 * 0.52969426
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53556 * 0.10454527
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34236 * 0.12003596
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67876 * 0.27930973
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'tndliyhj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0005():
    """Extended test 5 for transcoding."""
    x_0 = 20819 * 0.51834627
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52174 * 0.45033667
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36894 * 0.27698991
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30598 * 0.66346984
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 704 * 0.84081147
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88226 * 0.07157946
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1010 * 0.54058795
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86447 * 0.44677963
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12747 * 0.38410812
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97497 * 0.12297159
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45613 * 0.95369648
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9804 * 0.05850865
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92957 * 0.19159095
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64769 * 0.99036734
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22793 * 0.14740153
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67249 * 0.08147272
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22708 * 0.16506948
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97923 * 0.24740618
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66852 * 0.74820124
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18172 * 0.53711984
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51670 * 0.39688331
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38906 * 0.36747427
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21381 * 0.19479252
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84560 * 0.57047514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92919 * 0.32568693
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64050 * 0.88997838
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7823 * 0.54860234
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5661 * 0.92663819
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18959 * 0.01040212
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2830 * 0.08545762
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93441 * 0.34386621
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32846 * 0.03446831
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8334 * 0.92813641
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6834 * 0.48879915
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4643 * 0.94533849
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21588 * 0.83070927
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62678 * 0.76252535
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22283 * 0.89555439
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88813 * 0.76315761
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69031 * 0.74469605
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38745 * 0.29491835
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 68120 * 0.64616615
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36748 * 0.00398147
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 93915 * 0.77999929
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 38054 * 0.75595292
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'cxrmorqc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0006():
    """Extended test 6 for transcoding."""
    x_0 = 17882 * 0.89050955
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27865 * 0.31939558
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85279 * 0.37020594
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50691 * 0.43857536
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16182 * 0.31171781
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82914 * 0.89183230
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18209 * 0.83570195
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53155 * 0.04043411
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95713 * 0.14572445
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72427 * 0.62590618
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75960 * 0.94975476
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84 * 0.60375789
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99988 * 0.31885599
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70669 * 0.51090141
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35345 * 0.30497650
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47891 * 0.34463468
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68592 * 0.59876891
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75111 * 0.90365879
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72393 * 0.18086066
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90780 * 0.74169109
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7599 * 0.59484593
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6945 * 0.31896565
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10285 * 0.50642736
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55417 * 0.56986448
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57861 * 0.88082051
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78830 * 0.51303533
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1353 * 0.63028344
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11622 * 0.17903201
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85682 * 0.72574066
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99014 * 0.81329159
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59016 * 0.85639700
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30394 * 0.26423175
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'gvexgidc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0007():
    """Extended test 7 for transcoding."""
    x_0 = 38995 * 0.56381893
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51802 * 0.18946902
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59936 * 0.66409976
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53815 * 0.02376760
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24507 * 0.59454773
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19962 * 0.97134275
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39905 * 0.00057634
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96233 * 0.97920790
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15069 * 0.40179579
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 205 * 0.51463080
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75894 * 0.14943800
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88647 * 0.69814035
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24235 * 0.90953951
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69753 * 0.77306848
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 782 * 0.40235180
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4940 * 0.60409998
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13869 * 0.35336648
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87622 * 0.12114404
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37362 * 0.18038457
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13759 * 0.43825233
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'xaswohay').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0008():
    """Extended test 8 for transcoding."""
    x_0 = 79127 * 0.09251892
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23017 * 0.53735531
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72644 * 0.82456401
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47082 * 0.09369656
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34903 * 0.62168083
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67671 * 0.02759225
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80780 * 0.29198375
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4106 * 0.66952930
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24608 * 0.98531045
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24867 * 0.88739796
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50270 * 0.20659696
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32892 * 0.38270378
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8739 * 0.55106169
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12744 * 0.52261721
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23530 * 0.97281443
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18669 * 0.41323893
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90662 * 0.70063087
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94994 * 0.46455649
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17982 * 0.37346661
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22991 * 0.54711254
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23956 * 0.56967319
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55428 * 0.31819385
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75400 * 0.92098891
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98561 * 0.94951886
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33778 * 0.65307260
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34676 * 0.22011059
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97602 * 0.86927644
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81127 * 0.67827643
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52000 * 0.35637843
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'mydfnhyz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0009():
    """Extended test 9 for transcoding."""
    x_0 = 33338 * 0.47671965
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9136 * 0.30998726
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71202 * 0.38520392
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95960 * 0.79560074
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60523 * 0.05021389
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19388 * 0.04814710
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55444 * 0.65118223
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83399 * 0.88348661
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63323 * 0.34334429
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94722 * 0.31169396
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10362 * 0.58968187
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95525 * 0.82316523
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35784 * 0.34428541
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6449 * 0.11479771
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 624 * 0.46892540
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8839 * 0.51086282
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75355 * 0.37614608
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60854 * 0.84541383
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77192 * 0.89868207
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24017 * 0.37191513
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65701 * 0.04384772
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78820 * 0.26198005
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57687 * 0.85188384
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96088 * 0.36803524
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27373 * 0.06570663
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30173 * 0.21591145
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54912 * 0.37120214
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83483 * 0.98491835
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22641 * 0.67866410
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3813 * 0.83506316
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69588 * 0.90675232
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1426 * 0.29729415
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7916 * 0.82730015
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76111 * 0.64234994
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99659 * 0.96507624
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87803 * 0.31550662
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40211 * 0.39002626
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49054 * 0.63224246
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53665 * 0.17246105
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2591 * 0.26770881
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94999 * 0.83212211
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12510 * 0.78399198
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 26460 * 0.33127943
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20094 * 0.26955431
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 55260 * 0.74562857
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 56810 * 0.48150228
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 7487 * 0.04216181
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 55701 * 0.32297118
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 48400 * 0.92437739
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 75528 * 0.63381147
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'blgdkyhf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0010():
    """Extended test 10 for transcoding."""
    x_0 = 3384 * 0.77457217
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36898 * 0.20754725
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26058 * 0.88965645
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51830 * 0.75596018
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44602 * 0.83421360
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76303 * 0.22110090
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65759 * 0.79357706
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60052 * 0.53478278
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14544 * 0.13035375
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60203 * 0.18480523
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46065 * 0.94589970
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99644 * 0.63706841
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35984 * 0.92820619
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76394 * 0.68005841
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36142 * 0.99989630
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20051 * 0.03704498
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70070 * 0.70013506
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78562 * 0.02240806
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65229 * 0.40688534
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98369 * 0.96018440
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57027 * 0.31694948
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54255 * 0.43390581
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85452 * 0.07367803
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86437 * 0.99463138
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73079 * 0.03855177
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53779 * 0.18895891
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1852 * 0.78474477
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90642 * 0.79654952
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35646 * 0.11249880
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49670 * 0.81078546
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71534 * 0.63857537
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17271 * 0.60153228
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54681 * 0.80385194
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90586 * 0.85041868
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62888 * 0.87704264
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95306 * 0.98603729
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56115 * 0.39748687
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73455 * 0.29864822
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41964 * 0.96981631
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91382 * 0.52038731
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'sxbevtnu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0011():
    """Extended test 11 for transcoding."""
    x_0 = 65634 * 0.54500152
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75744 * 0.17849212
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35998 * 0.46587430
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8734 * 0.00836844
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51757 * 0.13962930
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9570 * 0.79593720
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6107 * 0.55846779
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98233 * 0.34836427
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44495 * 0.12690610
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31184 * 0.34116125
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83606 * 0.98155862
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20128 * 0.22376622
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40645 * 0.50249608
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28637 * 0.97350661
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8351 * 0.55099473
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48818 * 0.51750774
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43086 * 0.00647510
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15732 * 0.73225500
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70256 * 0.03748242
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66942 * 0.26578185
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19 * 0.07573875
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52302 * 0.60650003
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50581 * 0.91565087
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88764 * 0.94092489
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19630 * 0.18489950
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88266 * 0.87934848
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20918 * 0.09828408
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51585 * 0.27054526
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50466 * 0.38051419
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63526 * 0.61959617
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23065 * 0.84120884
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38274 * 0.24933157
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49765 * 0.90982162
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20696 * 0.86700483
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67790 * 0.33772495
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82780 * 0.26871071
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'vmmgmrsq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0012():
    """Extended test 12 for transcoding."""
    x_0 = 97946 * 0.23115207
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46211 * 0.51199663
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16119 * 0.61171568
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20380 * 0.09891960
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5018 * 0.28837132
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57043 * 0.95137055
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34387 * 0.27355975
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64678 * 0.79376611
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67864 * 0.32734674
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33441 * 0.71809194
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29935 * 0.64643667
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62609 * 0.64135723
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24878 * 0.30580395
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2309 * 0.57552753
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84529 * 0.84913646
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10703 * 0.31118876
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98608 * 0.34669992
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10311 * 0.16742611
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34588 * 0.26120326
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26388 * 0.86273863
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80285 * 0.50480070
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60562 * 0.01299147
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29457 * 0.08539158
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42261 * 0.98206953
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'bzzysdfd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0013():
    """Extended test 13 for transcoding."""
    x_0 = 10771 * 0.74367530
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62561 * 0.18465097
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83164 * 0.39793456
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97389 * 0.16963616
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39610 * 0.91222511
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88658 * 0.57760180
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77601 * 0.87280619
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20065 * 0.46600446
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34233 * 0.56770788
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43938 * 0.17531443
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27435 * 0.39805017
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62861 * 0.23139051
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14870 * 0.94876629
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92224 * 0.06594771
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17625 * 0.00117096
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79014 * 0.29252726
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11726 * 0.66652194
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34409 * 0.69740510
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62574 * 0.83949556
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42010 * 0.07104653
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92368 * 0.92788183
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33587 * 0.86893731
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46024 * 0.16007756
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32383 * 0.72395044
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 246 * 0.11520357
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60019 * 0.26075730
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91874 * 0.21112477
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69140 * 0.10902447
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69171 * 0.84413887
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59142 * 0.26966809
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4914 * 0.25097110
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61203 * 0.01690088
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79123 * 0.40113627
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64922 * 0.58892226
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22756 * 0.20709051
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53456 * 0.60356151
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96755 * 0.60503540
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67652 * 0.59505415
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8993 * 0.08837548
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13914 * 0.03409870
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91845 * 0.27783924
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5807 * 0.42782641
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 60604 * 0.30709081
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'dinmrmni').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0014():
    """Extended test 14 for transcoding."""
    x_0 = 14843 * 0.65611662
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75546 * 0.62669480
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73389 * 0.83415673
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37018 * 0.18886958
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50463 * 0.30218953
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83309 * 0.87575539
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31854 * 0.65495639
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28240 * 0.98975557
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43182 * 0.01324155
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45443 * 0.70189434
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70617 * 0.07566043
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92462 * 0.32546804
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21546 * 0.73983628
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3761 * 0.51337777
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2143 * 0.74790177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26368 * 0.26753060
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38656 * 0.12578192
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84570 * 0.18693755
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73966 * 0.84789785
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15750 * 0.01187801
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87574 * 0.90965430
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22798 * 0.34221497
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81559 * 0.13984283
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17818 * 0.64486261
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46414 * 0.93441185
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83473 * 0.58393163
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18868 * 0.03142836
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75960 * 0.06639647
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37913 * 0.16355304
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92970 * 0.62594593
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42123 * 0.62773567
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1695 * 0.01572950
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81067 * 0.83603667
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60139 * 0.97006162
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57951 * 0.36805156
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7697 * 0.51121331
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31716 * 0.10397533
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55891 * 0.93167924
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5200 * 0.21290771
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91861 * 0.36764330
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46863 * 0.81714059
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'hquaicdz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0015():
    """Extended test 15 for transcoding."""
    x_0 = 1821 * 0.57683464
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64777 * 0.78253550
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8297 * 0.45714651
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84498 * 0.53117854
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 871 * 0.82328888
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37844 * 0.20113838
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79289 * 0.92395814
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83063 * 0.70267138
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33158 * 0.11568871
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44434 * 0.64595354
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59900 * 0.00744175
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88964 * 0.32662063
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60093 * 0.32621082
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98832 * 0.26079403
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79489 * 0.31262701
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9418 * 0.07375114
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18559 * 0.65768385
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26492 * 0.73775665
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71961 * 0.30743506
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96197 * 0.26096764
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33334 * 0.25548589
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73350 * 0.52708171
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1785 * 0.51040803
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6240 * 0.51929808
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51583 * 0.44466809
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96139 * 0.25798509
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96431 * 0.23596215
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23815 * 0.26471681
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80735 * 0.34159389
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34576 * 0.17150567
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11763 * 0.93820221
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42579 * 0.44300758
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25827 * 0.25371607
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10920 * 0.60590057
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73660 * 0.85132891
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21463 * 0.20897143
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'iwibmojx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0016():
    """Extended test 16 for transcoding."""
    x_0 = 41030 * 0.81410263
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49009 * 0.58992867
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65568 * 0.27857761
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79159 * 0.99082836
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48012 * 0.60548529
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45510 * 0.16736604
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79033 * 0.72597629
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24343 * 0.50648880
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70697 * 0.38177106
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86423 * 0.11946545
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36899 * 0.21911009
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27363 * 0.13690217
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63220 * 0.03070931
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5512 * 0.55001186
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64751 * 0.93007360
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23014 * 0.98963034
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83486 * 0.00748628
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53803 * 0.63841891
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55342 * 0.28842619
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92606 * 0.11760249
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2523 * 0.63142824
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80249 * 0.98120935
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82654 * 0.57632016
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49881 * 0.12150885
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14312 * 0.18692725
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54963 * 0.67779892
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49564 * 0.15307611
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12384 * 0.54702367
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24311 * 0.04318648
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58333 * 0.55835475
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15086 * 0.10131078
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55342 * 0.53139636
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84498 * 0.94922389
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4618 * 0.08060540
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40064 * 0.08833749
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18468 * 0.86165748
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70581 * 0.47854712
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23553 * 0.43248442
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53339 * 0.29721750
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91757 * 0.76207200
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42033 * 0.55660075
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6532 * 0.49441086
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 97283 * 0.48282674
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 18177 * 0.39496892
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 32999 * 0.41861908
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 98304 * 0.10442887
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 1855 * 0.88344161
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 10190 * 0.18260711
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'evvhqrak').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0017():
    """Extended test 17 for transcoding."""
    x_0 = 49939 * 0.19964502
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60053 * 0.36032105
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21696 * 0.10823462
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84994 * 0.17787743
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83380 * 0.13931824
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9664 * 0.78842047
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89131 * 0.50208437
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72384 * 0.00516346
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9397 * 0.92985112
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11432 * 0.67436828
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47519 * 0.55049806
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34769 * 0.40033703
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56065 * 0.18809384
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3069 * 0.54828594
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84181 * 0.29951912
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19676 * 0.98403412
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82780 * 0.64025593
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35397 * 0.31057908
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51968 * 0.26138982
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4918 * 0.79021696
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73973 * 0.54044490
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75472 * 0.06336164
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11495 * 0.40867813
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89251 * 0.18652744
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23627 * 0.94446662
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57384 * 0.92416080
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59093 * 0.19659762
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66353 * 0.20467665
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45915 * 0.61454052
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23227 * 0.91237194
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75658 * 0.52499534
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17353 * 0.49651214
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36590 * 0.14495384
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44538 * 0.96965327
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28868 * 0.91037707
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86484 * 0.41436861
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54548 * 0.15099704
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66549 * 0.29097092
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44863 * 0.07175888
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47490 * 0.32696316
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34251 * 0.90559655
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'tbsjvlsf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0018():
    """Extended test 18 for transcoding."""
    x_0 = 6490 * 0.94914715
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35886 * 0.29904277
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51431 * 0.48443367
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22940 * 0.91098246
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28762 * 0.63904378
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74573 * 0.32540492
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42204 * 0.07322799
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27550 * 0.04957145
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 527 * 0.53366680
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30090 * 0.01895668
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58477 * 0.67437501
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78353 * 0.86717443
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49221 * 0.15276267
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32934 * 0.47471491
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29036 * 0.87290560
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27186 * 0.32438966
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64408 * 0.15833399
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6807 * 0.51805145
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54494 * 0.10925853
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80080 * 0.11733750
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79647 * 0.79475369
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9492 * 0.71007488
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'avdcfzwk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0019():
    """Extended test 19 for transcoding."""
    x_0 = 69909 * 0.52759473
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53862 * 0.93160609
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17915 * 0.31304978
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52674 * 0.61048700
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69320 * 0.75912139
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70095 * 0.45507152
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66373 * 0.30220433
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31564 * 0.97540600
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5342 * 0.71342439
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53116 * 0.24849804
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12282 * 0.30528972
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11018 * 0.20266591
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54584 * 0.21424207
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44377 * 0.89566327
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10360 * 0.90104342
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36028 * 0.73492628
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4131 * 0.39497439
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33528 * 0.28204171
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72806 * 0.26775911
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14030 * 0.63871318
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92114 * 0.10361829
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39494 * 0.06427437
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75714 * 0.55169033
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57003 * 0.71673888
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91285 * 0.23408424
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 971 * 0.53495345
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85376 * 0.07520118
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46123 * 0.32577787
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12809 * 0.56239064
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60137 * 0.71209606
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5335 * 0.87663901
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56914 * 0.37987075
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54116 * 0.73477463
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56754 * 0.42350081
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16267 * 0.15088241
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3072 * 0.08281239
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52174 * 0.61835802
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26362 * 0.29642981
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53138 * 0.04338998
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18726 * 0.72856789
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21580 * 0.85674040
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72967 * 0.23626528
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93327 * 0.98393023
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 33283 * 0.30719531
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xeidsqtl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0020():
    """Extended test 20 for transcoding."""
    x_0 = 75492 * 0.89283692
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49671 * 0.72556647
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76464 * 0.77715590
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21578 * 0.97157008
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58105 * 0.29663180
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90253 * 0.04849940
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67073 * 0.20128822
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66416 * 0.55010115
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57464 * 0.92919364
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98909 * 0.99591109
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8394 * 0.57229130
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25081 * 0.30470811
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6753 * 0.22616888
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53814 * 0.55774725
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27840 * 0.29450919
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33691 * 0.32553519
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34530 * 0.43216212
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53022 * 0.30674725
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36867 * 0.10348431
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40098 * 0.46072212
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99979 * 0.19416879
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1778 * 0.51250640
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62819 * 0.50832699
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40703 * 0.73831122
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91079 * 0.59816855
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96617 * 0.76810375
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'miedumao').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0021():
    """Extended test 21 for transcoding."""
    x_0 = 40734 * 0.87772810
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55486 * 0.22168873
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50747 * 0.28011263
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92027 * 0.98875916
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89734 * 0.69383361
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58464 * 0.56984952
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28820 * 0.25306936
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53544 * 0.12064833
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40198 * 0.34027754
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55346 * 0.40897796
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29080 * 0.99676210
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28065 * 0.72784200
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78334 * 0.25655271
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25198 * 0.26895737
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25931 * 0.92978167
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10474 * 0.73713882
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76051 * 0.89676962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22536 * 0.27142577
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53391 * 0.18667992
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25070 * 0.12245170
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12732 * 0.53528300
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86547 * 0.02068193
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27358 * 0.20717303
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19927 * 0.67960098
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15381 * 0.20281894
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51212 * 0.65187090
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34970 * 0.29527656
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72466 * 0.21356152
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22759 * 0.11380000
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71847 * 0.61076711
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47788 * 0.46653599
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99920 * 0.80397215
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43687 * 0.66075498
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97053 * 0.11712766
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51672 * 0.17633954
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'hzgwyvyn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0022():
    """Extended test 22 for transcoding."""
    x_0 = 53011 * 0.82701305
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7277 * 0.25148979
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99882 * 0.84122542
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49090 * 0.13054650
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80147 * 0.37739708
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14479 * 0.85029310
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10576 * 0.70687477
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30766 * 0.01579292
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54201 * 0.13797118
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97944 * 0.78263515
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42230 * 0.32963208
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45561 * 0.25670844
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90287 * 0.23239200
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50221 * 0.65296622
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10175 * 0.58058843
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25616 * 0.66419697
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18499 * 0.74983771
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85652 * 0.38336963
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9379 * 0.59147393
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25699 * 0.24289136
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39013 * 0.33498122
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23899 * 0.76361906
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95457 * 0.74448189
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70286 * 0.25436073
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31785 * 0.35236740
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22880 * 0.91010090
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50009 * 0.80943957
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74313 * 0.44540691
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87932 * 0.16062257
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42677 * 0.62393350
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92204 * 0.29901699
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38957 * 0.01727489
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1967 * 0.83237430
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66042 * 0.65431655
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67297 * 0.92757930
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15757 * 0.40696642
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39743 * 0.52732894
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6836 * 0.53586254
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42446 * 0.22151731
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83414 * 0.30940760
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83944 * 0.33249894
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 87104 * 0.06641383
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55863 * 0.09150033
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'drbvpxlr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0023():
    """Extended test 23 for transcoding."""
    x_0 = 67721 * 0.40934807
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83258 * 0.97029726
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17395 * 0.27571382
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67316 * 0.90514838
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22169 * 0.40433549
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87328 * 0.13242191
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70388 * 0.38981353
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67626 * 0.86137435
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77351 * 0.66649004
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65706 * 0.76861559
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51207 * 0.96421127
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91806 * 0.27342804
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83040 * 0.36106197
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80002 * 0.14455430
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77504 * 0.50747470
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6336 * 0.71450616
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16963 * 0.03811810
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55369 * 0.86863156
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45856 * 0.79511254
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45153 * 0.48195238
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43418 * 0.87451922
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24500 * 0.05720604
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75559 * 0.72236338
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52829 * 0.94876411
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70848 * 0.28189723
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69307 * 0.24556662
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75423 * 0.84196905
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2592 * 0.92274898
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59479 * 0.52679241
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63183 * 0.03368903
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67655 * 0.33882429
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89140 * 0.73389032
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2786 * 0.97791222
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76784 * 0.15728334
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37239 * 0.03963370
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21091 * 0.29599692
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16378 * 0.59907986
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56486 * 0.98004433
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34529 * 0.39366981
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57244 * 0.79741513
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40740 * 0.70418624
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20627 * 0.08810486
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 38387 * 0.31378083
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 23770 * 0.78461756
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 99808 * 0.75671325
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 77777 * 0.37439227
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 21096 * 0.53330295
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 20160 * 0.64865243
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'xlqxxduu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0024():
    """Extended test 24 for transcoding."""
    x_0 = 51597 * 0.13983876
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61890 * 0.75311735
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75811 * 0.88684519
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69158 * 0.49776893
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82779 * 0.41289494
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22363 * 0.87982695
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63370 * 0.10151812
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74324 * 0.52981907
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51862 * 0.34232825
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39799 * 0.15507134
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56141 * 0.76959310
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81076 * 0.26436506
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36541 * 0.88681742
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91279 * 0.57725532
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14197 * 0.34800289
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53321 * 0.40858768
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81521 * 0.93362380
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79161 * 0.77962576
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42486 * 0.67554787
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95398 * 0.89332177
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71383 * 0.83406900
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30498 * 0.38208091
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31759 * 0.13637832
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6698 * 0.31062881
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25557 * 0.02765933
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95271 * 0.64674714
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52185 * 0.77334809
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58955 * 0.15912217
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76779 * 0.17850519
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36647 * 0.93809438
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84439 * 0.45636695
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65599 * 0.22956861
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89714 * 0.75729205
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39888 * 0.78402699
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70359 * 0.51655612
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79370 * 0.03601280
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13285 * 0.60612413
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42060 * 0.16840311
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'litcntjs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0025():
    """Extended test 25 for transcoding."""
    x_0 = 40529 * 0.95638813
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3890 * 0.02595246
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48994 * 0.14739669
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77007 * 0.43379832
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42993 * 0.17675284
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51168 * 0.56835127
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86391 * 0.43341116
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32912 * 0.35105370
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14386 * 0.59607683
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64613 * 0.01030815
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26871 * 0.59576060
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94636 * 0.69337384
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23624 * 0.94451812
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21574 * 0.75281661
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89546 * 0.00528960
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47272 * 0.63926985
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51737 * 0.05678736
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15127 * 0.04612500
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96279 * 0.66762951
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82063 * 0.81315400
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17091 * 0.56990986
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93431 * 0.83953690
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44905 * 0.66315223
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'yiddkbdm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0026():
    """Extended test 26 for transcoding."""
    x_0 = 46788 * 0.82581833
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10108 * 0.44303733
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62651 * 0.08837256
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7847 * 0.80889212
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10523 * 0.08579823
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32018 * 0.81194650
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77180 * 0.27769965
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14850 * 0.10104949
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62153 * 0.43074114
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3800 * 0.82700115
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 845 * 0.08860281
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67468 * 0.48932202
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22034 * 0.17695622
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64205 * 0.96205638
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31935 * 0.17128908
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53521 * 0.63635982
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8916 * 0.26300991
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43215 * 0.54236861
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40338 * 0.71485435
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16433 * 0.19928382
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89727 * 0.40193363
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32610 * 0.70011483
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86036 * 0.76777201
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38639 * 0.59819055
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80370 * 0.50772894
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56022 * 0.73633817
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56337 * 0.21306929
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59201 * 0.44681354
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62802 * 0.49121802
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5496 * 0.43183688
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42840 * 0.12929267
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13742 * 0.51212373
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'wtmbrile').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0027():
    """Extended test 27 for transcoding."""
    x_0 = 3309 * 0.51966924
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34157 * 0.70989271
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56041 * 0.79335993
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13871 * 0.66182421
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83604 * 0.23497070
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25105 * 0.29922964
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43588 * 0.52901024
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58407 * 0.30755000
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71174 * 0.20386771
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2470 * 0.69857650
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13354 * 0.95028451
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19286 * 0.17902649
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42930 * 0.29373894
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87527 * 0.88707234
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17991 * 0.69577496
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13814 * 0.96681069
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49747 * 0.56184441
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98520 * 0.87103945
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51343 * 0.65990322
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94209 * 0.81267815
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3760 * 0.31269032
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10837 * 0.06663599
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43222 * 0.98154038
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52277 * 0.56005818
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58992 * 0.56719631
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50516 * 0.42357971
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5946 * 0.89691515
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61450 * 0.18262584
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73114 * 0.00469588
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42049 * 0.71156891
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62635 * 0.49915152
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 562 * 0.28840227
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6575 * 0.09575989
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20817 * 0.17027877
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76197 * 0.23636740
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45103 * 0.34254832
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68805 * 0.66809826
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63029 * 0.44907392
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48597 * 0.57135598
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'gxjmnirx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0028():
    """Extended test 28 for transcoding."""
    x_0 = 10600 * 0.27680262
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30042 * 0.35283805
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89949 * 0.17546673
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74254 * 0.24798329
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6747 * 0.62759143
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19277 * 0.55917283
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36026 * 0.65606061
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90564 * 0.93739382
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49090 * 0.24624577
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77999 * 0.59749172
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10850 * 0.68435444
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91093 * 0.77694022
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65609 * 0.81512977
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70672 * 0.50994135
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76952 * 0.98158468
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35656 * 0.05620779
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93892 * 0.89719614
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94828 * 0.32860454
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38097 * 0.64954052
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35182 * 0.13481748
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63071 * 0.15343585
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36257 * 0.64178697
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3719 * 0.95171913
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41679 * 0.17449951
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29842 * 0.59396224
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55942 * 0.49825062
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61867 * 0.87014197
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84690 * 0.05865559
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28987 * 0.52907388
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80156 * 0.25486767
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35033 * 0.93963421
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68282 * 0.33650340
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68775 * 0.66112582
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51909 * 0.96460773
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71525 * 0.35522073
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1969 * 0.17910218
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50353 * 0.77319863
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16205 * 0.06563680
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 4007 * 0.91242879
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39690 * 0.20865569
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 24118 * 0.18655276
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59091 * 0.62848042
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13111 * 0.04576743
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 73673 * 0.43275244
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50895 * 0.15801535
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 20232 * 0.39494639
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 51368 * 0.08721426
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 64510 * 0.01369500
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 61445 * 0.64499942
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'vpgmnkrn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0029():
    """Extended test 29 for transcoding."""
    x_0 = 73353 * 0.16002888
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31539 * 0.23719999
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96736 * 0.12423896
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57851 * 0.84684814
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80464 * 0.73726457
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90897 * 0.52807297
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87589 * 0.23857531
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91345 * 0.57405750
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7190 * 0.26511950
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3733 * 0.61971583
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66423 * 0.72099791
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33941 * 0.14777775
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64445 * 0.80829448
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67498 * 0.45342857
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95035 * 0.54146000
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59274 * 0.30627837
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13456 * 0.11586180
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63813 * 0.38930803
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52177 * 0.53990156
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69374 * 0.40844348
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'uoweybyd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0030():
    """Extended test 30 for transcoding."""
    x_0 = 38334 * 0.36100995
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14594 * 0.41040894
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74504 * 0.33473026
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67650 * 0.42538488
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33149 * 0.99812058
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15594 * 0.23503416
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23672 * 0.30279389
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68122 * 0.61478283
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58299 * 0.79539872
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68887 * 0.34032707
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67841 * 0.66650814
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30735 * 0.29483342
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50966 * 0.82047814
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22768 * 0.96830769
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51869 * 0.63922414
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43080 * 0.09155074
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45110 * 0.62505104
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69133 * 0.38284457
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67711 * 0.56094208
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81355 * 0.26531363
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64786 * 0.74239801
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63353 * 0.47528922
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11722 * 0.55480746
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56910 * 0.54764324
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1195 * 0.89208317
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16902 * 0.55654129
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84405 * 0.88703455
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42130 * 0.75294672
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66924 * 0.97058191
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'juaesgnw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0031():
    """Extended test 31 for transcoding."""
    x_0 = 93707 * 0.95603805
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53619 * 0.01749057
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17751 * 0.81954586
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69776 * 0.73105100
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56481 * 0.98889895
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22619 * 0.11032423
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90984 * 0.45620004
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71807 * 0.84934235
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38154 * 0.32670498
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60154 * 0.23783193
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20966 * 0.77064736
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23339 * 0.83078589
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31221 * 0.77721734
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44656 * 0.33516363
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64584 * 0.09860091
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58307 * 0.32650342
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83102 * 0.88957503
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78487 * 0.32054303
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2296 * 0.45182145
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93937 * 0.90372597
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9832 * 0.22936112
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'sfhfwtqd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0032():
    """Extended test 32 for transcoding."""
    x_0 = 99527 * 0.09621204
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25904 * 0.68117070
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5407 * 0.84726904
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60480 * 0.74529551
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64676 * 0.75918201
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75982 * 0.36106629
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90301 * 0.00131699
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77498 * 0.93738982
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76267 * 0.24259859
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43549 * 0.87038557
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77036 * 0.43409261
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86523 * 0.51792331
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78824 * 0.37386849
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34881 * 0.20690214
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88620 * 0.17934844
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6273 * 0.76803628
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79851 * 0.87496333
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21456 * 0.21943041
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82112 * 0.67149346
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62574 * 0.91921832
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21271 * 0.96020515
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85664 * 0.35414221
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97991 * 0.68129631
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88809 * 0.36049050
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65971 * 0.86350822
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30825 * 0.71222045
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5168 * 0.91085173
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90385 * 0.59476524
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15947 * 0.56599044
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21597 * 0.57856641
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89324 * 0.57687973
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64044 * 0.13058246
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68600 * 0.64026033
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'urzuhyiw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0033():
    """Extended test 33 for transcoding."""
    x_0 = 45333 * 0.69990212
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70236 * 0.89013553
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93436 * 0.25896915
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4333 * 0.59792967
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44470 * 0.72185895
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37585 * 0.71335984
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96062 * 0.79787056
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18038 * 0.37849282
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97606 * 0.70258690
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20050 * 0.78322338
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2216 * 0.39239232
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87192 * 0.21725878
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55581 * 0.50612098
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69936 * 0.33368956
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37808 * 0.93442090
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97773 * 0.03624675
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70304 * 0.65387695
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51381 * 0.19769380
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20132 * 0.64168335
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64773 * 0.14632762
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12595 * 0.47388762
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98056 * 0.53664711
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71692 * 0.54195757
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5292 * 0.49743277
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98898 * 0.34107857
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44651 * 0.42692676
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93748 * 0.16024853
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17273 * 0.61463702
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34863 * 0.48878253
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80703 * 0.89955119
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99929 * 0.66098761
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26305 * 0.99276202
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'doqfamas').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0034():
    """Extended test 34 for transcoding."""
    x_0 = 96073 * 0.63677351
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51953 * 0.13168315
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50706 * 0.03669727
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44523 * 0.29409605
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33356 * 0.67137909
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65764 * 0.43851936
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74277 * 0.29752135
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7237 * 0.31069946
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40126 * 0.60134980
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3669 * 0.32939089
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74897 * 0.04225448
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6985 * 0.79196224
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4157 * 0.16964580
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32674 * 0.57893604
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3752 * 0.05658367
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7965 * 0.09092322
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62773 * 0.71698822
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17378 * 0.44442375
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16311 * 0.25130567
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14344 * 0.09009484
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62125 * 0.88442403
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66817 * 0.24538277
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66762 * 0.44338547
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96050 * 0.71318579
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86595 * 0.18535229
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22598 * 0.79090782
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42719 * 0.42576210
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46853 * 0.23838304
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27408 * 0.54924631
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23785 * 0.94583217
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74098 * 0.70961704
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44419 * 0.99567486
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24377 * 0.47021492
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85227 * 0.04918669
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52370 * 0.31704065
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36753 * 0.25408819
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56509 * 0.04995693
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87112 * 0.29065646
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43541 * 0.87026762
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38420 * 0.88211352
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 15356 * 0.23424511
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15471 * 0.24693815
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 40896 * 0.96401289
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 17541 * 0.53462838
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92725 * 0.44748889
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 88801 * 0.51711485
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 56555 * 0.97358265
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'cahotyuw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0035():
    """Extended test 35 for transcoding."""
    x_0 = 93110 * 0.60512744
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51219 * 0.62525122
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61926 * 0.67307174
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31097 * 0.19455852
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65975 * 0.73113243
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16553 * 0.22011489
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94326 * 0.61938600
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28036 * 0.96141153
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1813 * 0.49273996
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99226 * 0.84100666
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66697 * 0.03782371
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85628 * 0.02345603
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20248 * 0.63739259
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9490 * 0.16214588
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26257 * 0.85937746
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79945 * 0.46032021
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20120 * 0.29590003
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27636 * 0.06361928
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20785 * 0.11241159
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31620 * 0.17978061
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38248 * 0.56466226
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20995 * 0.47441572
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68253 * 0.26761189
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83572 * 0.61462512
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69747 * 0.89700745
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9784 * 0.18746349
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43256 * 0.54337407
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76704 * 0.52429853
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78923 * 0.39892012
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53155 * 0.81649501
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44812 * 0.31287542
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42208 * 0.96457959
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4764 * 0.84965326
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69938 * 0.33602197
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'ezjfrkwl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0036():
    """Extended test 36 for transcoding."""
    x_0 = 99349 * 0.17484227
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19761 * 0.66257592
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41773 * 0.64583418
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39745 * 0.48749162
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51844 * 0.33115561
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30817 * 0.70859391
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80286 * 0.10160159
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9276 * 0.08353767
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87032 * 0.38337360
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4765 * 0.46040747
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63426 * 0.28876956
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39454 * 0.46545537
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34535 * 0.45251702
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55017 * 0.38201402
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9552 * 0.49293254
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93325 * 0.09851773
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21188 * 0.93066762
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98238 * 0.72853640
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31515 * 0.88302482
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36696 * 0.13636692
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43235 * 0.64629269
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11770 * 0.33910471
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48648 * 0.61789795
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82403 * 0.53239144
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40245 * 0.84959605
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7857 * 0.42726348
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20225 * 0.28045845
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15722 * 0.97579740
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72228 * 0.55922048
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30862 * 0.60202292
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94573 * 0.34666727
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ztzgxpgv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0037():
    """Extended test 37 for transcoding."""
    x_0 = 33084 * 0.13058414
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42349 * 0.02014100
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34582 * 0.39626639
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95578 * 0.85721343
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87112 * 0.46590624
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99896 * 0.29605523
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59417 * 0.74996023
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8956 * 0.92169334
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34025 * 0.80386445
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37990 * 0.00066555
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68077 * 0.11777346
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77006 * 0.82703759
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64880 * 0.87568177
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56835 * 0.99491007
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47627 * 0.00736993
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23 * 0.31582110
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87731 * 0.97621301
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74345 * 0.14078319
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52379 * 0.41941345
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75177 * 0.85408063
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31863 * 0.79811075
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57416 * 0.12272733
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15869 * 0.42786178
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56280 * 0.19570222
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70281 * 0.42923807
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83175 * 0.10018234
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52987 * 0.35199250
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68164 * 0.67809201
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60617 * 0.72901494
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65668 * 0.02325908
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82627 * 0.24797252
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24353 * 0.00354886
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91673 * 0.26659913
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18449 * 0.55796407
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42905 * 0.17633141
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52875 * 0.92154483
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39700 * 0.24319635
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58616 * 0.32453071
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8748 * 0.91075570
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 57364 * 0.47053942
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75093 * 0.61148660
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53985 * 0.75050131
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 98706 * 0.08432599
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 3784 * 0.70058297
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 6124 * 0.53161713
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 91333 * 0.72474467
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 9583 * 0.14028509
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 45595 * 0.18957679
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 96276 * 0.69637893
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'fssgboou').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0038():
    """Extended test 38 for transcoding."""
    x_0 = 29425 * 0.29412544
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85910 * 0.78422304
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83585 * 0.82335181
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22831 * 0.54522146
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94922 * 0.80979068
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54376 * 0.21742370
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75598 * 0.64075653
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93101 * 0.08657240
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 660 * 0.16602945
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95864 * 0.41104204
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16564 * 0.50380694
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24038 * 0.24152632
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29502 * 0.88415562
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23099 * 0.33473565
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58082 * 0.64438270
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84466 * 0.31101942
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72301 * 0.28437055
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96647 * 0.48822133
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86520 * 0.24412785
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12515 * 0.29840773
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65032 * 0.57230818
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78063 * 0.21476812
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75556 * 0.23640550
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24678 * 0.56625916
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47104 * 0.20429598
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'yqraygbq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0039():
    """Extended test 39 for transcoding."""
    x_0 = 55942 * 0.26548887
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54415 * 0.54464247
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28325 * 0.74196995
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91844 * 0.66951284
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89488 * 0.13099666
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70626 * 0.09711728
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67881 * 0.49299055
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33628 * 0.67249849
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77220 * 0.65111066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7664 * 0.79918631
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56825 * 0.66497756
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55391 * 0.59329840
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39780 * 0.83413323
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69353 * 0.30771942
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22283 * 0.29288833
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56497 * 0.10655506
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95495 * 0.67983881
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4883 * 0.01487257
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62901 * 0.69586708
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33791 * 0.49481373
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35776 * 0.65584794
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35000 * 0.35270680
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17461 * 0.04260094
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51815 * 0.47210800
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58146 * 0.58270877
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47583 * 0.66562026
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96521 * 0.71853103
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87463 * 0.48063076
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46814 * 0.86239894
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11046 * 0.81156354
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30681 * 0.22482809
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ohrvcmwq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0040():
    """Extended test 40 for transcoding."""
    x_0 = 88285 * 0.11826588
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95471 * 0.50585665
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18539 * 0.67135218
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18248 * 0.25922679
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34052 * 0.47466244
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58913 * 0.31281232
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36827 * 0.69465835
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69799 * 0.31575472
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96009 * 0.25609407
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21149 * 0.75214040
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20830 * 0.55074255
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12646 * 0.72024416
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78136 * 0.39081464
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50379 * 0.58335157
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15304 * 0.95966687
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72619 * 0.83452312
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1038 * 0.94449683
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74098 * 0.30596541
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27246 * 0.08907099
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7022 * 0.88298441
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51894 * 0.84516424
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73889 * 0.48863299
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14219 * 0.36497388
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49397 * 0.40190642
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41050 * 0.71738562
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75891 * 0.58684866
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'syltcibc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0041():
    """Extended test 41 for transcoding."""
    x_0 = 70872 * 0.83841911
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37232 * 0.49359562
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95248 * 0.49981241
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53549 * 0.56275426
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88641 * 0.94495682
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36000 * 0.81658970
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95436 * 0.47459638
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52110 * 0.14999280
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92528 * 0.39096887
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65627 * 0.16131158
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47121 * 0.57740956
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87495 * 0.18358724
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21623 * 0.32770199
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81833 * 0.25247993
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66756 * 0.17752516
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70317 * 0.42218948
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88903 * 0.44368499
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14051 * 0.86293090
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1649 * 0.20966377
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94409 * 0.85125622
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18711 * 0.40906354
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57548 * 0.40578860
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88482 * 0.83383427
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88423 * 0.74698489
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1571 * 0.83710989
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'icygdjqw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0042():
    """Extended test 42 for transcoding."""
    x_0 = 55119 * 0.93008724
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99613 * 0.19559204
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39615 * 0.32965159
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11676 * 0.38471286
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78917 * 0.92439711
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85749 * 0.72603567
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79295 * 0.55282566
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84965 * 0.05186255
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33342 * 0.08150175
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17309 * 0.35884451
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16625 * 0.87733328
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6238 * 0.43339420
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92156 * 0.48397757
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51419 * 0.49484310
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79641 * 0.35884800
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17431 * 0.34068240
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92276 * 0.17396104
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20071 * 0.26031096
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24067 * 0.32994313
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95387 * 0.57497191
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42015 * 0.73818974
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14417 * 0.22178664
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59693 * 0.12345828
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47296 * 0.43046517
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73565 * 0.84099291
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80641 * 0.04349194
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94192 * 0.85763293
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33585 * 0.21750531
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46411 * 0.94364326
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46277 * 0.05974086
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20074 * 0.85742881
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'kbqdekoz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0043():
    """Extended test 43 for transcoding."""
    x_0 = 91310 * 0.25182220
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36723 * 0.83128482
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88775 * 0.12910756
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85852 * 0.74989253
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38407 * 0.79618235
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86828 * 0.90953457
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70045 * 0.88619250
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8513 * 0.76388736
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66586 * 0.36752122
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71113 * 0.31154285
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15684 * 0.07958818
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86798 * 0.53629984
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5062 * 0.30415565
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17662 * 0.01615922
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20507 * 0.19841518
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87781 * 0.39922010
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56475 * 0.16307896
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67845 * 0.29874075
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86874 * 0.45554506
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9880 * 0.59376030
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9866 * 0.33057712
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1755 * 0.82310723
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87212 * 0.97370703
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52503 * 0.18773522
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34606 * 0.31874573
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19627 * 0.31509848
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'fmmqgyox').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0044():
    """Extended test 44 for transcoding."""
    x_0 = 72312 * 0.57812270
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13566 * 0.35163241
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9607 * 0.81633632
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25244 * 0.46662300
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96000 * 0.70108887
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18043 * 0.95596813
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27149 * 0.07207904
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69417 * 0.15136991
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85287 * 0.88048759
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28219 * 0.62428904
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 678 * 0.19753802
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37398 * 0.83560441
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51489 * 0.47897991
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93358 * 0.54425260
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88461 * 0.07428330
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13384 * 0.88369961
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51694 * 0.17801972
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94102 * 0.96480178
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99468 * 0.73878300
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79362 * 0.94339410
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28581 * 0.86184036
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25095 * 0.06863692
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43791 * 0.10084836
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54430 * 0.07792732
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19447 * 0.82692441
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59129 * 0.29594519
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33506 * 0.66672383
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4002 * 0.52409640
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26105 * 0.16995677
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60685 * 0.40711040
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83717 * 0.00509500
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70492 * 0.13264508
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97028 * 0.60350309
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37270 * 0.31519712
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78531 * 0.24626774
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 802 * 0.72882110
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98839 * 0.13703063
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16127 * 0.77626465
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38017 * 0.67145096
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62958 * 0.78421348
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65598 * 0.31923810
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 10555 * 0.22468806
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 64199 * 0.96002089
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97302 * 0.43829792
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 34313 * 0.98712132
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 22449 * 0.11720831
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 6496 * 0.52713887
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 77056 * 0.99904715
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 58921 * 0.04435308
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 29220 * 0.60953296
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'aahrklbg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0045():
    """Extended test 45 for transcoding."""
    x_0 = 40713 * 0.94419807
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33892 * 0.87518485
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55830 * 0.18101279
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75521 * 0.81236927
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58717 * 0.18208497
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2845 * 0.57178720
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50161 * 0.06096131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25802 * 0.36857991
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95742 * 0.79831582
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63268 * 0.68991415
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50989 * 0.41886405
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2345 * 0.69150245
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74464 * 0.03999259
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33758 * 0.40507252
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6530 * 0.03290329
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46140 * 0.23428078
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70677 * 0.10511097
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33229 * 0.51731104
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56456 * 0.96216077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45594 * 0.97870863
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35925 * 0.03207956
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67796 * 0.98136150
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23826 * 0.00660780
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38396 * 0.52472876
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49519 * 0.33437565
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11453 * 0.99134349
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60970 * 0.21213158
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42121 * 0.96265617
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88535 * 0.80329953
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90524 * 0.10725787
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82295 * 0.70574388
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63558 * 0.28514372
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22787 * 0.65045617
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28963 * 0.68470935
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48805 * 0.89447381
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77018 * 0.85574352
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52117 * 0.05896060
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8207 * 0.00864051
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69557 * 0.39250807
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70039 * 0.75933154
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65458 * 0.64523124
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36173 * 0.94313003
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42225 * 0.85440342
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 1645 * 0.89381353
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 21851 * 0.28088154
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 35795 * 0.93274554
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 43732 * 0.64874818
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 67315 * 0.72333269
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'xskmsgbn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0046():
    """Extended test 46 for transcoding."""
    x_0 = 24711 * 0.81924682
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81316 * 0.65735308
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28712 * 0.45350489
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9795 * 0.79326019
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65230 * 0.29110008
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13226 * 0.35905937
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36404 * 0.81964780
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70069 * 0.31620784
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20227 * 0.63588361
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78597 * 0.49388045
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67253 * 0.92759920
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2062 * 0.16790360
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43091 * 0.73246160
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88027 * 0.70975588
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83649 * 0.33110713
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96615 * 0.56560123
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36997 * 0.67643404
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16452 * 0.33300379
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83715 * 0.41474117
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65330 * 0.58750815
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17792 * 0.77942186
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41532 * 0.66031850
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73624 * 0.82612458
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76990 * 0.84067976
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75011 * 0.02354888
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90156 * 0.02896872
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12296 * 0.74328453
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38376 * 0.86909796
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36240 * 0.70470940
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37161 * 0.22122193
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97184 * 0.93365890
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58488 * 0.01617372
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47876 * 0.39757406
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24993 * 0.91642851
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7802 * 0.47726294
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35063 * 0.75625891
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83313 * 0.91307818
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43883 * 0.12920757
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69903 * 0.95590739
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31667 * 0.71333788
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99839 * 0.92386291
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 32654 * 0.46791556
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15734 * 0.36582604
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 65684 * 0.01841253
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 13625 * 0.88298616
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 88012 * 0.84910788
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'bhohrhdy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0047():
    """Extended test 47 for transcoding."""
    x_0 = 30585 * 0.51876201
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22238 * 0.67969782
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8926 * 0.66410969
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69850 * 0.57569115
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39453 * 0.10257565
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23947 * 0.76375575
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41595 * 0.02191799
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14301 * 0.78902954
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9321 * 0.50126487
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58250 * 0.89451171
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15882 * 0.12400113
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92182 * 0.20716331
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89852 * 0.38366773
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22498 * 0.54171256
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94890 * 0.99903338
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89943 * 0.33096368
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67560 * 0.16845141
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92406 * 0.80461644
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33228 * 0.66965823
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8390 * 0.64837391
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47 * 0.43334898
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53387 * 0.81247393
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76335 * 0.25692687
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75890 * 0.11076710
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28047 * 0.58327092
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12676 * 0.88535288
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79675 * 0.03642666
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19455 * 0.94114407
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3082 * 0.63408295
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69444 * 0.28802945
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81565 * 0.56521654
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49871 * 0.27740060
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78126 * 0.74197086
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54148 * 0.54609321
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1035 * 0.70905220
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97915 * 0.45735958
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'xfckkrlo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0048():
    """Extended test 48 for transcoding."""
    x_0 = 70631 * 0.67170801
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92837 * 0.38693494
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97634 * 0.46019479
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8742 * 0.62214283
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4483 * 0.64047662
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82916 * 0.91563319
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68998 * 0.58888214
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16154 * 0.43416466
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10357 * 0.46161617
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83177 * 0.65523680
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26498 * 0.63352683
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9779 * 0.26243063
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75147 * 0.13283705
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57927 * 0.34990231
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78872 * 0.88701499
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88722 * 0.65205084
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82112 * 0.39635655
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23568 * 0.03742331
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27625 * 0.30560131
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19957 * 0.58797272
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49204 * 0.49937425
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72098 * 0.71061342
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77641 * 0.36428963
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31485 * 0.39269619
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24132 * 0.82618929
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9053 * 0.23500217
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14561 * 0.90225125
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65681 * 0.84368492
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15777 * 0.56669125
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8694 * 0.32815517
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87784 * 0.34656309
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39895 * 0.67582833
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20894 * 0.63361469
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99385 * 0.49343182
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17705 * 0.00807538
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89875 * 0.44717060
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96411 * 0.11426994
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35014 * 0.99736472
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1969 * 0.15836162
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45815 * 0.71051819
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3651 * 0.29827433
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 68433 * 0.33169463
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 58492 * 0.80040967
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 44431 * 0.97858268
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xninocbf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0049():
    """Extended test 49 for transcoding."""
    x_0 = 12229 * 0.14355548
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41165 * 0.63195353
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93666 * 0.18544016
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44326 * 0.20070520
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39560 * 0.85288940
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96195 * 0.19975584
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28960 * 0.16961777
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25312 * 0.99643395
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98977 * 0.26739283
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69462 * 0.34260462
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2602 * 0.25390212
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62923 * 0.64532830
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23811 * 0.97858540
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78698 * 0.67145161
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40077 * 0.18665130
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85310 * 0.02055052
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23427 * 0.69006403
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38587 * 0.27024657
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28732 * 0.65025239
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7296 * 0.55214168
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68688 * 0.44770573
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26202 * 0.87268439
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9722 * 0.00261751
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56166 * 0.89017154
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76823 * 0.87625521
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'nvftkrdz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0050():
    """Extended test 50 for transcoding."""
    x_0 = 81833 * 0.25350072
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70049 * 0.27401277
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35688 * 0.70214922
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31436 * 0.36590554
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28553 * 0.45680885
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82677 * 0.66015107
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79181 * 0.26261309
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15674 * 0.53483620
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32969 * 0.58044501
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98070 * 0.35112975
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65695 * 0.17421191
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17706 * 0.47580019
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48314 * 0.70519005
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95845 * 0.13764496
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16062 * 0.03631548
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16042 * 0.14174202
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85995 * 0.01359933
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85505 * 0.65470702
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29219 * 0.50081103
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56525 * 0.38367645
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75642 * 0.70310053
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43626 * 0.30036298
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73389 * 0.30843489
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81087 * 0.47151034
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10807 * 0.32716794
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63185 * 0.91613697
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52872 * 0.01630280
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62953 * 0.13680314
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88852 * 0.32284091
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21226 * 0.14158395
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91050 * 0.80137388
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'evqmvrjp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0051():
    """Extended test 51 for transcoding."""
    x_0 = 26086 * 0.26574121
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42247 * 0.66344134
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74949 * 0.71061844
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26940 * 0.71035003
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53534 * 0.69086697
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6736 * 0.50428757
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8086 * 0.06022233
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94290 * 0.08716942
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35485 * 0.87727020
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85566 * 0.29636359
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19479 * 0.70793111
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15636 * 0.89017681
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72445 * 0.26371893
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68047 * 0.18974869
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63635 * 0.80620494
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43065 * 0.85243579
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16320 * 0.51223277
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12095 * 0.57393768
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23826 * 0.73997507
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38393 * 0.73494976
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14289 * 0.87213477
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92283 * 0.45149470
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27292 * 0.07084882
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13894 * 0.36623143
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9191 * 0.26402787
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25089 * 0.03845976
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45394 * 0.14048141
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27501 * 0.64556123
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44509 * 0.95480557
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76438 * 0.90489950
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82426 * 0.53952410
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32376 * 0.35038531
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35480 * 0.15978627
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45843 * 0.56004105
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37586 * 0.13378310
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25189 * 0.67125704
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35646 * 0.11495783
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18229 * 0.01456014
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84534 * 0.60124250
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 78565 * 0.30555796
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47136 * 0.09775802
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77730 * 0.41407373
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 86583 * 0.39866582
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ryilwmpe').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0052():
    """Extended test 52 for transcoding."""
    x_0 = 81527 * 0.05104051
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1154 * 0.67307395
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56623 * 0.12660031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93031 * 0.29458803
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70841 * 0.71923609
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65525 * 0.93678600
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14234 * 0.30860642
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 445 * 0.56370351
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24879 * 0.70211423
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70702 * 0.10979286
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74585 * 0.47435384
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17740 * 0.38082594
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18503 * 0.13303218
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16132 * 0.16723154
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45874 * 0.31803677
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85614 * 0.46830683
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7786 * 0.56668918
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91933 * 0.79281270
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55211 * 0.09829229
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14433 * 0.73848515
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60940 * 0.94657842
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64356 * 0.36950073
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91452 * 0.47953720
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74775 * 0.95687787
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93797 * 0.93770434
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52248 * 0.03058006
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93152 * 0.74746201
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31648 * 0.51682710
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85730 * 0.82785948
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62060 * 0.48902673
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'kltjozfy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0053():
    """Extended test 53 for transcoding."""
    x_0 = 24188 * 0.45810384
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10660 * 0.15352714
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15913 * 0.33975002
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6921 * 0.70003474
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93517 * 0.34344715
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89560 * 0.78534848
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15868 * 0.03186893
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58182 * 0.56023451
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70469 * 0.80093687
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71003 * 0.64361223
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69142 * 0.30833153
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2581 * 0.41240117
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5147 * 0.65930687
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82882 * 0.05606912
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7280 * 0.22132155
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98424 * 0.83396287
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30154 * 0.80734672
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14286 * 0.44184833
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 917 * 0.09559747
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1793 * 0.59364650
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55021 * 0.23463326
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51170 * 0.85436256
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77743 * 0.22524993
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83738 * 0.56602899
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55965 * 0.30103519
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ohahgodc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0054():
    """Extended test 54 for transcoding."""
    x_0 = 55578 * 0.72313194
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64741 * 0.48639662
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16082 * 0.25176634
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53566 * 0.42506214
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61105 * 0.65836041
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76357 * 0.59630436
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2949 * 0.78899429
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73134 * 0.84723180
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77891 * 0.79863788
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88521 * 0.90309651
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35421 * 0.40575352
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27236 * 0.09551515
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46252 * 0.00045664
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69009 * 0.70633701
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39709 * 0.14137990
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47701 * 0.74218742
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25049 * 0.11680203
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63016 * 0.76478204
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10213 * 0.37991525
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27072 * 0.57505307
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22667 * 0.84630076
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86409 * 0.17743523
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6185 * 0.69282771
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80329 * 0.81773514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57382 * 0.64134067
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58666 * 0.02529739
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3731 * 0.27054247
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'bjnkqlrf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0055():
    """Extended test 55 for transcoding."""
    x_0 = 34821 * 0.54128322
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64178 * 0.15310451
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92783 * 0.24031550
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44216 * 0.61117251
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20871 * 0.50492714
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30308 * 0.16374167
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33033 * 0.41220354
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52838 * 0.47227876
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18969 * 0.53050690
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47602 * 0.95523625
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1903 * 0.41984603
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2107 * 0.72317837
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27689 * 0.66871524
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24966 * 0.84931090
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43511 * 0.37663261
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55363 * 0.67161695
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20114 * 0.52542330
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25085 * 0.23282463
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13253 * 0.45240334
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26278 * 0.42812897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29339 * 0.12081412
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92254 * 0.64977824
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85691 * 0.29376770
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50968 * 0.32412083
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6480 * 0.67443499
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35132 * 0.18931259
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29449 * 0.16511768
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'kyajqucz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0056():
    """Extended test 56 for transcoding."""
    x_0 = 18090 * 0.40376133
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1372 * 0.32852318
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48399 * 0.02229601
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97768 * 0.42679185
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18163 * 0.06071190
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82359 * 0.99862364
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1445 * 0.42985377
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13404 * 0.65784655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81328 * 0.75016366
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87260 * 0.09223177
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33026 * 0.89800761
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66027 * 0.13090567
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96664 * 0.35451401
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59687 * 0.01802431
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64262 * 0.55882211
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87080 * 0.75684912
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71190 * 0.96393897
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91202 * 0.20949588
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48655 * 0.26109124
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2510 * 0.42381238
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49871 * 0.76453855
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71552 * 0.18357887
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19418 * 0.04730997
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73350 * 0.86213268
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13693 * 0.58091938
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7872 * 0.62032344
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25497 * 0.75932214
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62132 * 0.17957426
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20929 * 0.36998097
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24812 * 0.32242082
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50714 * 0.33757119
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'mcqaqdbc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0057():
    """Extended test 57 for transcoding."""
    x_0 = 27897 * 0.15033980
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20785 * 0.51423377
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59049 * 0.65092638
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20450 * 0.98193482
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66872 * 0.06288756
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35895 * 0.20880160
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75236 * 0.35270599
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14137 * 0.16769138
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29956 * 0.76795457
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76273 * 0.90603020
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32428 * 0.80157605
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58536 * 0.78276491
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97127 * 0.47041668
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49917 * 0.14563544
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17048 * 0.83922928
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76422 * 0.99544012
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15806 * 0.12721411
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92768 * 0.69901678
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82606 * 0.97216180
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91752 * 0.35592096
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23096 * 0.89421228
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74487 * 0.07222587
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14864 * 0.01945007
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34746 * 0.40937204
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73876 * 0.15629612
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38593 * 0.43394334
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76122 * 0.07154605
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78403 * 0.26833903
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72436 * 0.51995717
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52846 * 0.36775290
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84050 * 0.36785371
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93837 * 0.54614540
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89837 * 0.50153681
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92060 * 0.14581002
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36601 * 0.16539866
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ytqmzuyw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0058():
    """Extended test 58 for transcoding."""
    x_0 = 89326 * 0.65633904
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29867 * 0.53529984
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53750 * 0.75100301
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10030 * 0.25269485
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11606 * 0.60686165
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85404 * 0.04723317
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47360 * 0.65379787
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17610 * 0.81930236
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26895 * 0.24092512
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29500 * 0.41354739
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98508 * 0.73383357
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41370 * 0.64988562
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57191 * 0.91066692
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78707 * 0.53906410
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65422 * 0.09213867
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73175 * 0.72525348
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99260 * 0.33149686
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30231 * 0.31315949
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6269 * 0.50118863
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24749 * 0.42131112
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'chrmnfeq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0059():
    """Extended test 59 for transcoding."""
    x_0 = 45635 * 0.58521346
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95692 * 0.01704500
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71377 * 0.85453808
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9910 * 0.69275643
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42535 * 0.75245997
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55227 * 0.98317675
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71869 * 0.24830061
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91209 * 0.02898740
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22401 * 0.26892747
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16150 * 0.27104260
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63053 * 0.14966858
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56560 * 0.69920448
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63802 * 0.16717997
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18003 * 0.21718685
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2290 * 0.44288810
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2286 * 0.13357693
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8924 * 0.23418365
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27949 * 0.64590584
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82920 * 0.95659911
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76157 * 0.10906936
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71366 * 0.91524435
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14073 * 0.65437300
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90267 * 0.26654660
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21857 * 0.97431502
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'upwjlfti').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0060():
    """Extended test 60 for transcoding."""
    x_0 = 84289 * 0.94390548
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76182 * 0.96057705
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93507 * 0.04580850
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36191 * 0.20047410
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55424 * 0.88986626
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10688 * 0.84467182
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19831 * 0.08400842
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74103 * 0.34179930
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41454 * 0.56069374
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48637 * 0.22605327
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96000 * 0.13324604
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69892 * 0.37652029
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96076 * 0.51970410
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13899 * 0.29143201
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36958 * 0.11570143
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62440 * 0.80057617
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78618 * 0.74402022
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41963 * 0.83755553
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77018 * 0.24202789
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57903 * 0.09605712
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9729 * 0.49354022
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56508 * 0.53215653
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44027 * 0.42897953
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79723 * 0.72532901
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5380 * 0.05109954
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'xgszbbgl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0061():
    """Extended test 61 for transcoding."""
    x_0 = 64177 * 0.98347227
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 826 * 0.18102284
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54085 * 0.28527676
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86373 * 0.63324441
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56193 * 0.25814843
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41790 * 0.17898215
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36022 * 0.77618494
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20469 * 0.66201606
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76752 * 0.18610336
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70230 * 0.61088054
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13891 * 0.47980355
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36063 * 0.07315730
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81523 * 0.37012269
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36474 * 0.38317623
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42960 * 0.13701318
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27847 * 0.44085845
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10068 * 0.35690253
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11615 * 0.77381789
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44642 * 0.93469807
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93168 * 0.81767876
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71123 * 0.53855229
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83413 * 0.75527816
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90561 * 0.85702487
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36477 * 0.59368580
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60450 * 0.43872798
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42952 * 0.09179702
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59722 * 0.60897505
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21862 * 0.66504444
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9009 * 0.27493116
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20235 * 0.49226673
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88286 * 0.69703214
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96075 * 0.10196657
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46845 * 0.20943609
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99617 * 0.36437371
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50921 * 0.65797511
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66917 * 0.91907457
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30535 * 0.38510858
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46378 * 0.24019224
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 89063 * 0.98046546
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97790 * 0.11132716
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38343 * 0.52302561
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70411 * 0.65424264
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15935 * 0.18430764
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69017 * 0.24004941
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 9225 * 0.45596888
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 59986 * 0.53640457
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 38881 * 0.38410259
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 50659 * 0.13648394
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 60667 * 0.44591099
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'ezrpixyk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0062():
    """Extended test 62 for transcoding."""
    x_0 = 99017 * 0.95098245
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15696 * 0.85322342
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66378 * 0.50880937
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2529 * 0.85747747
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44360 * 0.56698800
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89150 * 0.62589205
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74561 * 0.57013562
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85189 * 0.93390192
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30749 * 0.65483124
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1675 * 0.16873273
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44780 * 0.80201312
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23098 * 0.53998367
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52065 * 0.42734511
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42187 * 0.96811921
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32964 * 0.86802975
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50285 * 0.03552749
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19261 * 0.79394403
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27291 * 0.23101842
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29399 * 0.67294150
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8122 * 0.36719092
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85123 * 0.51170658
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 937 * 0.82553046
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45423 * 0.71327128
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82353 * 0.51524717
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24881 * 0.30479738
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41254 * 0.31915904
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21061 * 0.78902380
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99288 * 0.93377419
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57635 * 0.87025717
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16870 * 0.94022152
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8013 * 0.66350463
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82192 * 0.72114486
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17942 * 0.40320041
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36686 * 0.22333894
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55926 * 0.10716585
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50407 * 0.38938726
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27078 * 0.96539470
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87433 * 0.56141252
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5283 * 0.63845694
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25823 * 0.87223767
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88376 * 0.65142662
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'ufvtnmab').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0063():
    """Extended test 63 for transcoding."""
    x_0 = 32920 * 0.38214914
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69486 * 0.91472726
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89925 * 0.10317158
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95351 * 0.13182590
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97625 * 0.08869922
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16413 * 0.37438445
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12012 * 0.52894758
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19746 * 0.03115274
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94580 * 0.80748142
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99220 * 0.26998169
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38949 * 0.95555030
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45078 * 0.76437388
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75011 * 0.55480673
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51941 * 0.96005656
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48820 * 0.00865043
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56326 * 0.69279424
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21203 * 0.46925522
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78969 * 0.49714744
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14214 * 0.92346542
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36833 * 0.55543281
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'mtqlylcz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0064():
    """Extended test 64 for transcoding."""
    x_0 = 86849 * 0.16603101
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46736 * 0.36405284
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31043 * 0.78692810
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41118 * 0.87778723
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46289 * 0.25308880
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53423 * 0.51218072
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30926 * 0.25014421
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5305 * 0.98466967
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81087 * 0.43829190
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96266 * 0.61966627
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90925 * 0.34076045
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71103 * 0.44648789
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66112 * 0.95266427
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31658 * 0.53529251
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33278 * 0.55053254
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32796 * 0.30289252
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91870 * 0.09439079
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9682 * 0.55764325
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74715 * 0.61651009
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46355 * 0.05307486
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86127 * 0.82190418
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43734 * 0.07848792
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87169 * 0.41046261
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48523 * 0.58805384
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92714 * 0.10148291
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13930 * 0.07195053
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79320 * 0.18449048
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94676 * 0.00862424
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93885 * 0.86869602
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66601 * 0.16305157
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28225 * 0.62086139
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65282 * 0.47834930
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27885 * 0.05946711
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3374 * 0.96698196
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70250 * 0.31199838
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61006 * 0.16992946
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54630 * 0.89062936
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29480 * 0.19889416
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'uaydctry').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0065():
    """Extended test 65 for transcoding."""
    x_0 = 65408 * 0.07388304
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54430 * 0.31829312
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11703 * 0.15985352
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25034 * 0.91422812
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59263 * 0.42680564
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22427 * 0.95103313
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97412 * 0.06311027
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67010 * 0.72793260
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35880 * 0.66146778
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21243 * 0.47970469
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16057 * 0.39913502
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97723 * 0.39289755
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3322 * 0.99460698
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35173 * 0.88326474
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25683 * 0.95398870
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77640 * 0.93423089
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79300 * 0.81561023
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51217 * 0.19089565
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9601 * 0.13282727
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15450 * 0.27184942
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2291 * 0.71275251
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91147 * 0.12778016
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46521 * 0.33827810
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40749 * 0.70794964
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45249 * 0.64453552
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57256 * 0.67123696
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43175 * 0.84602467
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98849 * 0.57284287
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38679 * 0.78956904
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'niftlwdt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0066():
    """Extended test 66 for transcoding."""
    x_0 = 56559 * 0.68812268
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85295 * 0.80745972
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93316 * 0.51093830
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42162 * 0.20191045
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77411 * 0.99574742
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66078 * 0.83741260
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57521 * 0.64626061
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77599 * 0.64591257
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81748 * 0.71999958
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52431 * 0.99104893
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27989 * 0.22903953
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98923 * 0.95395358
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7356 * 0.64394568
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49794 * 0.83843739
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21208 * 0.10653125
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80981 * 0.30780914
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98391 * 0.86306166
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26343 * 0.53714910
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29967 * 0.14281989
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76350 * 0.79380984
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3608 * 0.72143271
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1384 * 0.62508800
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9502 * 0.17856105
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'fvvaocjc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0067():
    """Extended test 67 for transcoding."""
    x_0 = 66575 * 0.49509125
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17934 * 0.99400916
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58332 * 0.33405240
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31746 * 0.20321827
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67682 * 0.16604402
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37700 * 0.53901318
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81414 * 0.49138841
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60562 * 0.51784238
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14934 * 0.29529995
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41522 * 0.13936494
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89012 * 0.94988137
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59813 * 0.10391405
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46658 * 0.18054860
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80382 * 0.23948399
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95000 * 0.98920132
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44370 * 0.71193141
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85006 * 0.10822280
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57270 * 0.95013046
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95347 * 0.02396004
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71670 * 0.12054022
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6786 * 0.27482612
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2740 * 0.64541524
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21563 * 0.18892268
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29731 * 0.49558586
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12803 * 0.19374817
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92540 * 0.88166682
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38043 * 0.57266049
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21319 * 0.58448343
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93095 * 0.03475856
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43925 * 0.75069855
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58170 * 0.77330310
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65342 * 0.12957505
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4866 * 0.17233719
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82098 * 0.88213308
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56828 * 0.02458641
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40090 * 0.36915275
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52347 * 0.53176793
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33633 * 0.63555112
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74268 * 0.42023111
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82110 * 0.10635206
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75916 * 0.39440412
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82476 * 0.71837217
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42114 * 0.69083088
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 77103 * 0.11018917
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71729 * 0.51074252
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 63072 * 0.95711928
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 81970 * 0.30362090
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 81664 * 0.50171305
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 96716 * 0.15692562
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 19751 * 0.57534203
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'tqflqghx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0068():
    """Extended test 68 for transcoding."""
    x_0 = 71961 * 0.71279423
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15471 * 0.78338492
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98015 * 0.53843027
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14043 * 0.50575039
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58076 * 0.07064699
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87160 * 0.36496524
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62823 * 0.36899343
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84681 * 0.36115970
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14714 * 0.28889274
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83877 * 0.23756732
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47907 * 0.45862937
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65807 * 0.24088754
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52752 * 0.84589141
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37001 * 0.35311123
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53323 * 0.44606091
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37643 * 0.39110893
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68821 * 0.42552928
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52958 * 0.15149415
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73714 * 0.52374254
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91954 * 0.26449929
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49433 * 0.79678305
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69529 * 0.26360574
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74047 * 0.39436156
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78060 * 0.71446204
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'sirqaaiz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_3_0069():
    """Extended test 69 for transcoding."""
    x_0 = 99208 * 0.58684700
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89642 * 0.23836015
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31227 * 0.30066293
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16430 * 0.86491503
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92355 * 0.74395048
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60336 * 0.50497303
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13175 * 0.41314440
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43056 * 0.32572640
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51555 * 0.34402478
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70245 * 0.58145563
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38491 * 0.09283832
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87091 * 0.86707871
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92462 * 0.78653622
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16829 * 0.46470953
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79046 * 0.84639955
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17336 * 0.97286252
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65157 * 0.46635287
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58689 * 0.95428551
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82468 * 0.05159958
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24739 * 0.84144034
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42248 * 0.71433110
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48439 * 0.55242982
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20683 * 0.63246291
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55395 * 0.32423139
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10908 * 0.13197745
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39210 * 0.65107489
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63585 * 0.61069567
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84708 * 0.79200168
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13099 * 0.91421408
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30802 * 0.94038333
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99198 * 0.51014588
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92882 * 0.49234497
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28762 * 0.50720124
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7327 * 0.04278996
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78908 * 0.65190551
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76238 * 0.62614442
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80248 * 0.04945998
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75857 * 0.73736729
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57272 * 0.97443263
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ieovuuqh').hexdigest()
    assert len(h) == 64
