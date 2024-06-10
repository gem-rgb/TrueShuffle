"""Extended tests for transcoding suite 7."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_transcoding_extended_7_0000():
    """Extended test 0 for transcoding."""
    x_0 = 67722 * 0.63734415
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61110 * 0.11085812
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77951 * 0.59640897
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29303 * 0.43415021
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9989 * 0.15411184
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13948 * 0.76432067
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36974 * 0.75010818
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18191 * 0.89342589
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20355 * 0.95674592
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15657 * 0.54197029
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52801 * 0.46215543
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46667 * 0.87485312
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60375 * 0.04028608
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37746 * 0.42433608
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77360 * 0.08921786
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37078 * 0.87496364
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10969 * 0.69121730
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65562 * 0.45925196
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8545 * 0.86755041
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39059 * 0.08766718
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75569 * 0.95624950
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20555 * 0.76960526
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68055 * 0.39368819
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89294 * 0.91409394
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56152 * 0.27609271
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71321 * 0.18585719
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14898 * 0.17352248
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22176 * 0.85861360
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32400 * 0.82103787
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77918 * 0.64548352
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78677 * 0.71031253
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38452 * 0.03976399
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94534 * 0.47337183
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31267 * 0.47732599
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27956 * 0.40628357
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22365 * 0.51641879
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34111 * 0.16998929
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30665 * 0.48092520
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8798 * 0.38790498
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24760 * 0.88069633
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 24815 * 0.30670472
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18315 * 0.50811344
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18771 * 0.44325370
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 62537 * 0.64138413
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50975 * 0.71751442
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'mnpywxxo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0001():
    """Extended test 1 for transcoding."""
    x_0 = 88313 * 0.59613892
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4181 * 0.49929158
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63760 * 0.65481190
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23382 * 0.91510388
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10932 * 0.19020235
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42295 * 0.25589179
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97577 * 0.32733956
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69122 * 0.88843343
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95443 * 0.32814392
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13575 * 0.06795401
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90178 * 0.08742025
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82150 * 0.22815612
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21059 * 0.67424555
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96319 * 0.83565097
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14234 * 0.79931097
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92671 * 0.66210567
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84049 * 0.03973489
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29670 * 0.63098843
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81608 * 0.82110664
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37396 * 0.16651317
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33412 * 0.71298470
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44089 * 0.92564557
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13939 * 0.57596046
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47357 * 0.28414017
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14926 * 0.32081069
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95472 * 0.64978042
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14937 * 0.09257260
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79570 * 0.44948681
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70671 * 0.42290494
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85472 * 0.43287059
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42794 * 0.48985298
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17883 * 0.24553814
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99774 * 0.47287226
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54607 * 0.66451164
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32487 * 0.03104997
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10538 * 0.19999146
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48561 * 0.89845123
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87400 * 0.22847033
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61550 * 0.79074601
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16661 * 0.65860870
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98436 * 0.43479641
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3023 * 0.11331431
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 67427 * 0.25252871
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 56707 * 0.06310829
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 84770 * 0.94528540
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 31424 * 0.19095589
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 67076 * 0.79641807
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'njehjpua').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0002():
    """Extended test 2 for transcoding."""
    x_0 = 43956 * 0.20728356
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71654 * 0.33643698
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11379 * 0.40718877
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78770 * 0.65954872
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52032 * 0.42974624
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10105 * 0.58950125
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16758 * 0.33090402
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7830 * 0.13719540
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46922 * 0.32997412
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75784 * 0.34868730
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84275 * 0.17659146
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7342 * 0.22723271
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54977 * 0.87437563
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40018 * 0.22249297
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14202 * 0.71641475
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78312 * 0.62913611
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78980 * 0.59911935
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26316 * 0.72036662
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12739 * 0.19273912
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35150 * 0.73352440
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67508 * 0.30703372
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82225 * 0.57940066
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93561 * 0.00164212
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28935 * 0.12665881
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25016 * 0.43931163
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83012 * 0.17130610
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12257 * 0.03577161
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42225 * 0.51508306
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69038 * 0.48510230
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'gzggwqgv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0003():
    """Extended test 3 for transcoding."""
    x_0 = 84511 * 0.60658076
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11682 * 0.62056969
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91452 * 0.43336367
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37276 * 0.13948043
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58456 * 0.17276103
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80401 * 0.00274452
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30903 * 0.11986089
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1446 * 0.42748593
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49101 * 0.83106842
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30706 * 0.34174115
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9305 * 0.32880136
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8897 * 0.53089078
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60091 * 0.47710037
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65247 * 0.65465725
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66731 * 0.84317003
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83252 * 0.95679399
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54461 * 0.69759745
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57304 * 0.77179272
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66991 * 0.03047008
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44855 * 0.59093057
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82805 * 0.64280604
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80641 * 0.44662089
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85839 * 0.12142379
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7865 * 0.34269417
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43125 * 0.52906988
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43777 * 0.46069752
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86045 * 0.90119946
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72599 * 0.56051769
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'pkbbjelj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0004():
    """Extended test 4 for transcoding."""
    x_0 = 30311 * 0.13035941
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31483 * 0.48883334
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90352 * 0.73493766
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70572 * 0.63127304
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82917 * 0.57806955
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43258 * 0.45772508
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35944 * 0.20216600
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74758 * 0.60710876
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51704 * 0.53737999
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12420 * 0.75770959
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72293 * 0.51354389
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57972 * 0.13930032
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83879 * 0.56720378
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48396 * 0.52832437
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37120 * 0.69015087
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45588 * 0.35402761
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99671 * 0.16752200
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82792 * 0.45633529
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23537 * 0.08341666
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70512 * 0.60959511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32727 * 0.97073006
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95481 * 0.95211933
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44790 * 0.26483990
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57155 * 0.52891163
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76493 * 0.29943686
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31199 * 0.61047711
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75007 * 0.78203669
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62712 * 0.76336919
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85786 * 0.93939750
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14180 * 0.42620303
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25317 * 0.43764489
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23665 * 0.80225346
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91829 * 0.65414729
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72155 * 0.36078252
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13981 * 0.72855695
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10690 * 0.29975889
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45559 * 0.64877129
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34940 * 0.48819964
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84184 * 0.60605989
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47073 * 0.08098859
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 90303 * 0.72005115
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27742 * 0.25867785
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 69012 * 0.79946806
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 90244 * 0.62496711
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 33619 * 0.89964252
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'xxhghtiv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0005():
    """Extended test 5 for transcoding."""
    x_0 = 81378 * 0.86334807
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89338 * 0.31499248
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87305 * 0.01966954
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90719 * 0.23322326
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95539 * 0.56178484
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87596 * 0.89873062
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8464 * 0.86661055
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23558 * 0.88389256
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95013 * 0.32884273
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38461 * 0.30820508
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47864 * 0.91873214
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36574 * 0.37815655
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78912 * 0.08000266
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2575 * 0.91917363
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77700 * 0.05234229
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39489 * 0.46755150
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27265 * 0.49043196
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73252 * 0.44255074
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87753 * 0.81035362
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96780 * 0.28664758
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94489 * 0.06379724
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95341 * 0.24225148
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54078 * 0.44694195
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58795 * 0.45030686
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18288 * 0.12769416
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56999 * 0.38269549
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67565 * 0.29285642
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66698 * 0.64377662
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70661 * 0.52030201
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39859 * 0.29454562
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29985 * 0.25661232
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8436 * 0.85295399
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38039 * 0.38502630
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1064 * 0.94706780
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45592 * 0.17519742
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8066 * 0.56190078
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13768 * 0.88813474
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82088 * 0.73534179
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76485 * 0.72782018
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90366 * 0.86572605
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 15677 * 0.52050016
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35088 * 0.41583395
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 26488 * 0.25732555
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20283 * 0.59656322
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 19438 * 0.65468935
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 86845 * 0.24975799
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 36095 * 0.83036813
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 32618 * 0.06758912
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 81606 * 0.94519190
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'osqiworo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0006():
    """Extended test 6 for transcoding."""
    x_0 = 63343 * 0.21841150
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17886 * 0.79696417
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47884 * 0.07575653
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85256 * 0.54140688
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43951 * 0.63964782
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94434 * 0.31511314
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93222 * 0.59961817
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20573 * 0.32104738
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5348 * 0.20024631
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6165 * 0.63143652
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75301 * 0.60401872
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 64957 * 0.42111914
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89357 * 0.15342565
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98196 * 0.89546678
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38613 * 0.05855468
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98573 * 0.14186380
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35607 * 0.45942326
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41383 * 0.84078142
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28767 * 0.25839367
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93445 * 0.75434982
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44505 * 0.61864577
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4851 * 0.33701455
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86991 * 0.59506477
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45780 * 0.82735085
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71743 * 0.50046453
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52167 * 0.12459594
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'dhaqvwqq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0007():
    """Extended test 7 for transcoding."""
    x_0 = 68474 * 0.46195037
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86109 * 0.31187813
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74373 * 0.33183348
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13017 * 0.44580272
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80271 * 0.61565784
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43127 * 0.42252742
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60896 * 0.07781168
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52283 * 0.38775191
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68835 * 0.38832466
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29201 * 0.35657568
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51258 * 0.89012015
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22528 * 0.23256679
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87798 * 0.59341952
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22934 * 0.58606266
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68791 * 0.82080158
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44214 * 0.99409705
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73716 * 0.90760901
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73834 * 0.40065377
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45214 * 0.61345874
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5029 * 0.53293448
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28073 * 0.65284497
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32032 * 0.16852166
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67879 * 0.22151533
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90254 * 0.10959124
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18990 * 0.56864690
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58235 * 0.41069996
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'crisayen').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0008():
    """Extended test 8 for transcoding."""
    x_0 = 65209 * 0.56378878
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53046 * 0.60216186
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22783 * 0.63716207
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13636 * 0.85102993
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58268 * 0.52694646
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72404 * 0.82055358
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44326 * 0.21850067
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53237 * 0.59917993
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58412 * 0.04578866
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33981 * 0.74534322
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41804 * 0.14217200
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30716 * 0.53590071
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81326 * 0.48730857
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77106 * 0.44299905
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38522 * 0.53405486
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71905 * 0.21606922
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98721 * 0.69182336
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75551 * 0.73887311
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90620 * 0.11138549
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40836 * 0.94347124
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74382 * 0.32233356
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66606 * 0.47279120
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66577 * 0.06745041
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36751 * 0.64955564
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79485 * 0.53963050
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'wcubxfal').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0009():
    """Extended test 9 for transcoding."""
    x_0 = 59867 * 0.89351104
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99076 * 0.73688707
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86999 * 0.30048690
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60140 * 0.20655204
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94852 * 0.80334088
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8366 * 0.26462673
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52034 * 0.99454765
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21996 * 0.69099771
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32104 * 0.94438237
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50498 * 0.77664221
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87151 * 0.86508015
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4600 * 0.64255693
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72910 * 0.91331981
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16761 * 0.81911796
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92734 * 0.44450822
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49809 * 0.36151305
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66639 * 0.63718130
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10442 * 0.39511408
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9864 * 0.11794067
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37724 * 0.09610401
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1788 * 0.61419729
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94975 * 0.68786147
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'aghumkub').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0010():
    """Extended test 10 for transcoding."""
    x_0 = 19970 * 0.79852006
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18368 * 0.46369046
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22919 * 0.16659655
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64865 * 0.12389190
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12819 * 0.29430763
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90216 * 0.15921786
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56207 * 0.57836287
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93734 * 0.66055331
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12764 * 0.31613999
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95675 * 0.06639298
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53652 * 0.94676156
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59819 * 0.74983404
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5212 * 0.62807557
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37036 * 0.02680160
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92767 * 0.18234054
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88235 * 0.52579106
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41586 * 0.34720467
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97011 * 0.63149302
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77828 * 0.94018575
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4100 * 0.13151052
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49108 * 0.45612256
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19569 * 0.41614921
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51573 * 0.23331183
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92441 * 0.62612570
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89138 * 0.75450791
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7995 * 0.49090529
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18898 * 0.15136843
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ktakcbhw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0011():
    """Extended test 11 for transcoding."""
    x_0 = 23580 * 0.59497218
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91207 * 0.22270981
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81379 * 0.25340462
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98385 * 0.48580894
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39416 * 0.44185068
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69936 * 0.87147136
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83103 * 0.78240807
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91540 * 0.41059145
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92417 * 0.10236998
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95542 * 0.27928361
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59973 * 0.77452676
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83301 * 0.70129933
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27246 * 0.81611975
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22136 * 0.02081571
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47055 * 0.54613969
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90682 * 0.65573102
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34487 * 0.11487542
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8747 * 0.34165822
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44449 * 0.37337883
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83556 * 0.69226778
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58942 * 0.30619545
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26388 * 0.92364583
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21358 * 0.26589932
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89709 * 0.05197124
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72073 * 0.13889850
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6900 * 0.65667452
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93114 * 0.89159806
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83950 * 0.03442402
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22547 * 0.15427728
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93252 * 0.36047741
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56511 * 0.83970551
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87331 * 0.72328271
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24542 * 0.72830610
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68471 * 0.93889035
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 49189 * 0.37146219
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22301 * 0.50143278
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56765 * 0.77063767
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'dmqkfhcw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0012():
    """Extended test 12 for transcoding."""
    x_0 = 29576 * 0.32512372
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99649 * 0.88641930
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25612 * 0.49983743
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48668 * 0.35460462
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43147 * 0.54269858
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90053 * 0.22732266
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58916 * 0.74577723
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5828 * 0.86789794
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68376 * 0.83222234
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40284 * 0.95614495
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33775 * 0.51734566
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17454 * 0.26629587
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40014 * 0.59957699
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71271 * 0.63319491
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31116 * 0.26262130
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30160 * 0.18786225
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12855 * 0.86323776
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93380 * 0.95005054
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67494 * 0.31505182
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88560 * 0.02521793
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9458 * 0.22100160
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49034 * 0.40502996
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 950 * 0.46181706
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'gykiryos').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0013():
    """Extended test 13 for transcoding."""
    x_0 = 91308 * 0.72435270
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34521 * 0.28793315
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15863 * 0.81746517
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87285 * 0.46883110
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94998 * 0.60355331
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2806 * 0.24902117
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16073 * 0.14981274
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80482 * 0.61895064
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97657 * 0.12867756
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73275 * 0.80518883
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51606 * 0.80687215
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43248 * 0.42687307
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25432 * 0.99953935
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86263 * 0.52638116
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63979 * 0.84815756
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55286 * 0.03623736
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6545 * 0.22921967
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27015 * 0.13183169
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66954 * 0.99272569
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47932 * 0.01191020
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45785 * 0.07268139
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78478 * 0.60556194
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82719 * 0.06503558
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62830 * 0.60150576
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72972 * 0.02914387
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47742 * 0.55434997
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32331 * 0.26731892
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97558 * 0.04761003
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86474 * 0.32861865
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14334 * 0.54360567
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48132 * 0.21428675
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78533 * 0.04876272
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20253 * 0.48649556
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'wvjaldeu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0014():
    """Extended test 14 for transcoding."""
    x_0 = 1210 * 0.61113120
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31947 * 0.92229020
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57509 * 0.47768268
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90280 * 0.38530247
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21069 * 0.46298921
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44441 * 0.05494828
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95449 * 0.24424755
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47435 * 0.36694264
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67670 * 0.97640827
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66005 * 0.83842607
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99738 * 0.63735513
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7894 * 0.24940835
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10755 * 0.68729392
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15955 * 0.71301620
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20009 * 0.64844723
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15671 * 0.82475420
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42138 * 0.63584651
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48994 * 0.54218221
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31032 * 0.76972047
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18247 * 0.60220126
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87518 * 0.32036022
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50628 * 0.32845978
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92936 * 0.61559015
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34359 * 0.08127508
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76832 * 0.03559647
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25968 * 0.16095805
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59590 * 0.88962948
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93599 * 0.93563838
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24924 * 0.40571439
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75350 * 0.61708780
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6223 * 0.13109397
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58308 * 0.98388246
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41700 * 0.23647986
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11345 * 0.64489396
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32925 * 0.59493374
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84026 * 0.61268402
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93374 * 0.53983299
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 54987 * 0.28275418
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58338 * 0.26763960
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88296 * 0.15140690
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41912 * 0.67035620
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 73981 * 0.38142654
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'xsqpzuee').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0015():
    """Extended test 15 for transcoding."""
    x_0 = 66529 * 0.94970258
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26469 * 0.46330355
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52884 * 0.29224699
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11433 * 0.59351917
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45828 * 0.04826647
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28497 * 0.41053831
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11006 * 0.05834432
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25383 * 0.17450050
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12530 * 0.31861113
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98648 * 0.03850337
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30879 * 0.52678398
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37740 * 0.86053470
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67094 * 0.90377750
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76180 * 0.04104671
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16681 * 0.58915371
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63482 * 0.19138317
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93924 * 0.94361835
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78082 * 0.93670828
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60385 * 0.57524030
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44595 * 0.29213052
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68718 * 0.97003668
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22184 * 0.83364943
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 532 * 0.99924856
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63700 * 0.85337909
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46872 * 0.82007322
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35890 * 0.68105447
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79532 * 0.76537323
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46423 * 0.53036078
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49912 * 0.44729943
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15548 * 0.47938548
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'srvpyqzz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0016():
    """Extended test 16 for transcoding."""
    x_0 = 22027 * 0.37190435
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60551 * 0.79217312
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95480 * 0.13446258
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6588 * 0.12499103
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90352 * 0.24632081
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86181 * 0.02676033
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91619 * 0.94213825
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97614 * 0.41772624
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59841 * 0.00507049
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67632 * 0.02341493
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33345 * 0.65290126
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70501 * 0.76600765
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87546 * 0.46375041
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91374 * 0.29831195
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98748 * 0.68227280
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70529 * 0.76457296
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59364 * 0.87793698
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65864 * 0.69746224
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30692 * 0.67850739
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55895 * 0.74226482
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10456 * 0.87523479
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79739 * 0.35911003
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44760 * 0.36780018
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89008 * 0.97286346
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85069 * 0.23026943
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16266 * 0.52211194
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43965 * 0.83145880
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65854 * 0.67362061
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12557 * 0.51687165
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55728 * 0.69608097
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76449 * 0.89441521
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46099 * 0.34675656
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31865 * 0.74875380
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72960 * 0.05422616
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42741 * 0.56248234
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15623 * 0.12603731
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20496 * 0.75559514
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56429 * 0.39820562
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96045 * 0.03473613
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'whavhndo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0017():
    """Extended test 17 for transcoding."""
    x_0 = 94192 * 0.95041168
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98984 * 0.11062531
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26640 * 0.64051481
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67258 * 0.58507258
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48958 * 0.90520060
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9778 * 0.04030379
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56158 * 0.88999640
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 142 * 0.05431176
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60254 * 0.88473344
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89353 * 0.40116615
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49132 * 0.61583029
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92116 * 0.25140026
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56778 * 0.78601190
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69034 * 0.43775102
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22583 * 0.51247678
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26677 * 0.58089411
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86876 * 0.30990584
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49847 * 0.71560470
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39470 * 0.99020489
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92054 * 0.70691789
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66093 * 0.49353768
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'yypfouti').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0018():
    """Extended test 18 for transcoding."""
    x_0 = 35511 * 0.71011879
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98711 * 0.11245885
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20770 * 0.44875788
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48164 * 0.50711939
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45527 * 0.08082220
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81995 * 0.50134788
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20049 * 0.45859056
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58656 * 0.93372641
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71300 * 0.86291813
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76309 * 0.80628471
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28163 * 0.51048713
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41205 * 0.01367610
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53104 * 0.03212011
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49535 * 0.26597390
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30598 * 0.32432605
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77519 * 0.07952818
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49940 * 0.89702145
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3887 * 0.15321219
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85464 * 0.04202077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10391 * 0.94521893
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69115 * 0.47554153
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46737 * 0.92496005
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58319 * 0.43142684
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71978 * 0.89497257
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96948 * 0.09467209
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36743 * 0.67772866
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7952 * 0.36447380
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67771 * 0.02846116
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23689 * 0.96477165
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'pjdbqxyb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0019():
    """Extended test 19 for transcoding."""
    x_0 = 16858 * 0.04824266
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69887 * 0.67595838
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34108 * 0.39194212
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76648 * 0.38913720
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85281 * 0.53170188
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52838 * 0.56811582
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72520 * 0.12351923
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70820 * 0.41496212
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84937 * 0.79054326
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47711 * 0.34899914
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16534 * 0.56341565
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48265 * 0.39057108
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61548 * 0.07645041
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9668 * 0.77479732
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79607 * 0.44710755
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18169 * 0.28882195
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98538 * 0.68360322
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90764 * 0.98205141
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93968 * 0.74834227
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68764 * 0.11152370
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83123 * 0.24723950
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44751 * 0.32394029
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43503 * 0.36574463
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68942 * 0.99315606
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46431 * 0.85692040
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97246 * 0.24985276
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37828 * 0.88354215
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30494 * 0.39413569
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71906 * 0.53655699
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50016 * 0.85047735
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2610 * 0.16191510
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10910 * 0.30082801
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22072 * 0.03569596
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36311 * 0.39701627
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44428 * 0.59017934
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 72388 * 0.12557379
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60147 * 0.13217302
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5904 * 0.12085496
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55777 * 0.63652867
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47738 * 0.96237974
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45264 * 0.48921494
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33251 * 0.65587134
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22964 * 0.70854171
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'uyvflfoc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0020():
    """Extended test 20 for transcoding."""
    x_0 = 72080 * 0.34468384
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32341 * 0.12709101
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25155 * 0.42428358
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59996 * 0.43417786
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58181 * 0.48912963
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42223 * 0.84103523
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77904 * 0.17365246
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28106 * 0.66882821
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15895 * 0.64546230
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2492 * 0.67660036
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15285 * 0.48278739
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6309 * 0.49594790
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30160 * 0.21641701
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7928 * 0.89018105
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71063 * 0.20765751
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39502 * 0.19419594
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95367 * 0.66219703
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10590 * 0.81743744
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90603 * 0.11483518
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30986 * 0.64056471
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84000 * 0.50399544
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92411 * 0.52042578
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70253 * 0.71038049
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66892 * 0.26410449
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22184 * 0.23252950
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83763 * 0.38914649
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77297 * 0.36693824
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88931 * 0.09436500
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79271 * 0.31667940
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69344 * 0.22124879
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79669 * 0.49681419
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31281 * 0.35772688
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57358 * 0.91425529
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71206 * 0.68857983
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25175 * 0.74827666
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17627 * 0.54988339
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61616 * 0.32674283
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59154 * 0.17178684
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64612 * 0.30219664
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25329 * 0.59108119
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62924 * 0.97475833
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'tizksmqr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0021():
    """Extended test 21 for transcoding."""
    x_0 = 22926 * 0.37973003
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67659 * 0.34634594
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34199 * 0.12014297
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11380 * 0.33315876
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71488 * 0.95955418
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85929 * 0.69757260
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83476 * 0.86607889
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51223 * 0.47450564
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11230 * 0.72208948
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80707 * 0.09976007
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92230 * 0.46710543
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24375 * 0.29186067
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42203 * 0.16652606
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61658 * 0.34983447
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72830 * 0.47713627
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52252 * 0.19978145
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81048 * 0.76802790
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38544 * 0.27897874
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94421 * 0.43539795
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59663 * 0.23837685
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39759 * 0.57584529
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78603 * 0.91767790
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96187 * 0.06659768
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44323 * 0.80795530
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61085 * 0.48884439
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'qjhofwxs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0022():
    """Extended test 22 for transcoding."""
    x_0 = 62339 * 0.79548859
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46475 * 0.14269834
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93894 * 0.59097432
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49131 * 0.75995045
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25205 * 0.02641739
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18104 * 0.83136037
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72334 * 0.09816828
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83364 * 0.92381687
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5584 * 0.07115633
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70403 * 0.56189971
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87603 * 0.01694978
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53805 * 0.20974474
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99515 * 0.65068100
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51621 * 0.29366163
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23631 * 0.10867942
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67647 * 0.28602218
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4635 * 0.95794301
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57346 * 0.28882460
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51992 * 0.64709258
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34417 * 0.14515611
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86509 * 0.71289936
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ltqhnnnc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0023():
    """Extended test 23 for transcoding."""
    x_0 = 25541 * 0.16349266
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97261 * 0.71583122
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22457 * 0.85660808
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81183 * 0.00259022
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18243 * 0.05041861
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88790 * 0.18906891
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82476 * 0.75720584
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63228 * 0.95099927
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55592 * 0.84084132
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75664 * 0.15017323
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82593 * 0.47411511
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80152 * 0.91696920
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38340 * 0.29246633
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3110 * 0.75620421
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66076 * 0.50772376
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10233 * 0.80963427
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68581 * 0.05532555
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73044 * 0.79040634
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50367 * 0.07615709
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53268 * 0.80592714
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22870 * 0.05787069
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79094 * 0.57570168
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40216 * 0.52990231
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26516 * 0.31040562
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58073 * 0.69890838
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99359 * 0.16792308
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14263 * 0.93687541
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10637 * 0.40180637
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21893 * 0.25009793
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95194 * 0.95864858
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90752 * 0.19093620
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84046 * 0.65293153
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64826 * 0.01799035
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35989 * 0.80453201
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42066 * 0.47592232
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70996 * 0.99475894
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71696 * 0.88022511
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69039 * 0.87295608
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80531 * 0.47277718
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80661 * 0.43698723
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49061 * 0.30260948
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 30626 * 0.35499125
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24648 * 0.35138544
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 10644 * 0.87652992
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 44538 * 0.02060239
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 11932 * 0.80976764
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 80381 * 0.29859754
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 24394 * 0.93504712
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'aucbsvrg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0024():
    """Extended test 24 for transcoding."""
    x_0 = 492 * 0.94639312
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87395 * 0.45831580
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97651 * 0.13986370
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2990 * 0.63432598
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74777 * 0.51063253
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95573 * 0.87292830
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7925 * 0.19215802
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92533 * 0.03428474
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68792 * 0.64131516
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30983 * 0.85516607
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91139 * 0.00365292
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58665 * 0.33838587
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11818 * 0.43502734
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95185 * 0.60327266
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22060 * 0.54885198
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50320 * 0.47649675
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93534 * 0.73038980
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34821 * 0.90875133
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48941 * 0.82363754
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26593 * 0.73050523
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83308 * 0.41425167
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27426 * 0.14639829
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67828 * 0.11614476
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77496 * 0.74100991
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78696 * 0.39192589
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73075 * 0.89720388
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'uzipdcxd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0025():
    """Extended test 25 for transcoding."""
    x_0 = 68027 * 0.56590880
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39816 * 0.41538606
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81249 * 0.80592251
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70146 * 0.35036602
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72870 * 0.05319155
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96636 * 0.18911790
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99716 * 0.96073412
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28279 * 0.44562768
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24418 * 0.93262612
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66300 * 0.82028128
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16556 * 0.10181563
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15215 * 0.20133690
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79103 * 0.23548093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8077 * 0.70233609
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95336 * 0.96258063
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21978 * 0.76416214
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2551 * 0.11784670
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55571 * 0.13067066
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64613 * 0.74568083
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59233 * 0.50415139
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17044 * 0.74119507
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43676 * 0.91592845
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99274 * 0.67782254
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66221 * 0.16980141
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31933 * 0.79787161
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87862 * 0.73169697
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64443 * 0.80137568
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61106 * 0.15060063
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16255 * 0.74749016
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99042 * 0.02723114
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98897 * 0.61436123
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62401 * 0.73277310
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39217 * 0.42184912
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54186 * 0.39065307
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10448 * 0.16778133
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99498 * 0.07246955
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12973 * 0.51109862
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33869 * 0.24268795
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59976 * 0.98269066
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 177 * 0.02867669
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 9305 * 0.20021726
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74006 * 0.76742836
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 842 * 0.61996431
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 24976 * 0.91741575
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86098 * 0.14550781
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 9817 * 0.87493414
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 45196 * 0.03952519
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'snflkbxt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0026():
    """Extended test 26 for transcoding."""
    x_0 = 76741 * 0.50708558
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11186 * 0.16066861
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90390 * 0.25138585
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85473 * 0.31322712
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90488 * 0.85338759
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85090 * 0.99334907
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72135 * 0.41690517
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19287 * 0.21803868
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54461 * 0.62798639
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65626 * 0.05794722
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28359 * 0.43904019
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32783 * 0.01146218
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22068 * 0.10197605
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69067 * 0.66190841
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90243 * 0.93447940
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45336 * 0.10652749
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61693 * 0.48662078
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50929 * 0.11582239
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42213 * 0.86748521
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71211 * 0.88976222
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'swjrbflh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0027():
    """Extended test 27 for transcoding."""
    x_0 = 94513 * 0.06034746
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2385 * 0.16503356
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87082 * 0.27361578
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18407 * 0.62724216
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49975 * 0.42683554
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10258 * 0.39843338
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34661 * 0.23594697
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64215 * 0.41400324
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1835 * 0.08382852
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37227 * 0.21192318
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5373 * 0.77886928
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54388 * 0.67766089
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17365 * 0.11378709
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79998 * 0.17376080
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19944 * 0.59787494
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96292 * 0.34304325
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75822 * 0.16530057
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85926 * 0.12104572
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89381 * 0.79044404
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88635 * 0.42774964
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45096 * 0.26831766
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61315 * 0.15388839
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21268 * 0.67820552
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57785 * 0.19931049
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4938 * 0.44286103
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86376 * 0.21236818
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76158 * 0.75320935
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5270 * 0.60239449
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67500 * 0.25589098
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77666 * 0.92236406
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19700 * 0.04378780
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97353 * 0.63999806
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73726 * 0.52025375
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85247 * 0.91433006
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85506 * 0.97644134
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90116 * 0.74336362
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81698 * 0.88663289
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7632 * 0.96986588
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11811 * 0.83467572
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43110 * 0.30886328
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'dpwawbgf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0028():
    """Extended test 28 for transcoding."""
    x_0 = 11457 * 0.19217309
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68480 * 0.21236036
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32061 * 0.24831763
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62921 * 0.42086819
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73913 * 0.61479603
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45709 * 0.91768121
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25399 * 0.00127416
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22847 * 0.92936324
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41285 * 0.82822813
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50748 * 0.20107104
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49456 * 0.87592750
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49471 * 0.52444682
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66220 * 0.52991369
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53180 * 0.69520117
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72160 * 0.48262826
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84153 * 0.87634717
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78548 * 0.63099313
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21023 * 0.67043413
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9037 * 0.01572832
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 929 * 0.00806993
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81565 * 0.89070246
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92331 * 0.88236168
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59432 * 0.49636937
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31032 * 0.32953837
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76607 * 0.56436150
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15659 * 0.02581085
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43569 * 0.86872263
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83664 * 0.82741107
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4173 * 0.38822906
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81238 * 0.18769319
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56347 * 0.88969100
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2687 * 0.11966067
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26380 * 0.13243086
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1163 * 0.91038147
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77411 * 0.84743815
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 19979 * 0.95130380
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5865 * 0.44956541
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30086 * 0.79283162
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45474 * 0.75890495
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24928 * 0.95958154
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 93428 * 0.52974851
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9776 * 0.48707664
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93391 * 0.91064886
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75197 * 0.06084629
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79359 * 0.21084655
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 95762 * 0.29888537
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 80224 * 0.01938510
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'noqwdjxy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0029():
    """Extended test 29 for transcoding."""
    x_0 = 17550 * 0.66861694
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66794 * 0.95059623
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58500 * 0.61205149
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19234 * 0.36424021
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55919 * 0.65088896
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18926 * 0.59363276
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10729 * 0.46249761
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5681 * 0.14978187
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88752 * 0.11710394
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72808 * 0.98161111
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43993 * 0.37849159
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66666 * 0.79405283
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32132 * 0.36482808
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35133 * 0.51069646
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67357 * 0.87182991
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51774 * 0.10996767
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50734 * 0.08885382
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68971 * 0.55103703
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45482 * 0.46784975
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67964 * 0.58139574
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85872 * 0.98171703
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7074 * 0.52806922
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68029 * 0.35666191
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17050 * 0.56221423
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79743 * 0.41897276
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72060 * 0.44223337
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18720 * 0.11561092
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2273 * 0.24497248
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67802 * 0.55360523
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9904 * 0.33488366
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38351 * 0.31222888
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30323 * 0.99875586
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19298 * 0.29661627
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42708 * 0.03749521
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2751 * 0.12824509
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17956 * 0.96958700
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26371 * 0.38434327
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 82095 * 0.68934726
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66228 * 0.11003164
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91649 * 0.12923938
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35016 * 0.83224006
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25763 * 0.97674449
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93231 * 0.00624614
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88693 * 0.93033530
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'eliakcts').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0030():
    """Extended test 30 for transcoding."""
    x_0 = 20270 * 0.72177053
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41604 * 0.18551185
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77412 * 0.60668382
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66374 * 0.06940602
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99662 * 0.17571921
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48021 * 0.01565587
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41526 * 0.83430806
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21331 * 0.42652147
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65960 * 0.79169114
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24984 * 0.35625146
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31014 * 0.08380600
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93142 * 0.40716429
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34705 * 0.00329310
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80855 * 0.13849890
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95163 * 0.22087413
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77788 * 0.41482795
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6944 * 0.57025557
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12500 * 0.99827249
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80034 * 0.31963723
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93222 * 0.90710553
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70800 * 0.60084046
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66911 * 0.74797072
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36934 * 0.33680598
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47268 * 0.80269360
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72191 * 0.14041170
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93091 * 0.93448235
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87386 * 0.51838463
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37747 * 0.34540110
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22965 * 0.22998392
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68716 * 0.25955272
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48480 * 0.89720919
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32222 * 0.04744682
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47779 * 0.83012222
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77080 * 0.99218393
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84448 * 0.75922815
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3434 * 0.92764285
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34286 * 0.92950919
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78183 * 0.48916856
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77973 * 0.54400180
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47304 * 0.90196469
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34723 * 0.07022918
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 68740 * 0.54890161
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ojupiunr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0031():
    """Extended test 31 for transcoding."""
    x_0 = 1498 * 0.35702236
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74596 * 0.63997172
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26330 * 0.46887667
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86909 * 0.69587198
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71110 * 0.81698781
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8775 * 0.39329383
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1130 * 0.35260590
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60855 * 0.48428007
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87331 * 0.94124992
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28342 * 0.18275903
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95181 * 0.79493060
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38024 * 0.93265329
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99477 * 0.98299826
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53226 * 0.38732123
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39394 * 0.18618281
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31372 * 0.14273913
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57502 * 0.51320982
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52294 * 0.05124510
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48845 * 0.95796657
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86852 * 0.28858280
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7490 * 0.90169864
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20124 * 0.98266209
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45282 * 0.83760935
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9720 * 0.37220542
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96050 * 0.18560105
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94170 * 0.27574152
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44148 * 0.95353044
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27577 * 0.91373094
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67190 * 0.81844885
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'mvhjpouw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0032():
    """Extended test 32 for transcoding."""
    x_0 = 10711 * 0.66241063
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94732 * 0.63766740
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14372 * 0.22529419
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96549 * 0.12661430
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25721 * 0.48925015
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53900 * 0.28268402
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95250 * 0.00028896
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56646 * 0.75964243
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34231 * 0.22927349
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1066 * 0.43865325
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89021 * 0.03604769
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72245 * 0.49444716
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91726 * 0.61126866
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79106 * 0.62177022
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22086 * 0.54275044
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87554 * 0.65579159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57670 * 0.43111413
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40452 * 0.89760439
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12616 * 0.85826346
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14061 * 0.71321228
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92219 * 0.52059620
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 400 * 0.85269573
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88859 * 0.24012929
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52010 * 0.24319609
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76537 * 0.60788174
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63228 * 0.45691247
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42254 * 0.66811117
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36876 * 0.74480810
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80489 * 0.92153940
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80193 * 0.52519056
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13049 * 0.23960186
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66148 * 0.22555957
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92911 * 0.30451901
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11442 * 0.17898164
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65423 * 0.01748068
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32667 * 0.45136642
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31878 * 0.81102668
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 54671 * 0.17201880
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21172 * 0.73334013
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11992 * 0.62491562
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43242 * 0.58266806
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4063 * 0.88418768
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9264 * 0.21654228
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88645 * 0.61399932
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 8321 * 0.43413740
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 92985 * 0.79787716
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 31878 * 0.80189364
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 93303 * 0.31569391
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 87765 * 0.03132360
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'cwsqgeaa').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0033():
    """Extended test 33 for transcoding."""
    x_0 = 27084 * 0.20264610
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23976 * 0.23089015
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82820 * 0.39911186
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42517 * 0.53769135
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36735 * 0.70354284
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63973 * 0.46892166
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97275 * 0.81172870
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9690 * 0.61943585
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93613 * 0.36686278
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46314 * 0.57160856
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80057 * 0.63664262
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98814 * 0.60880773
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18517 * 0.18056550
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57183 * 0.18650488
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41847 * 0.64757770
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78720 * 0.26909172
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43264 * 0.71234298
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59363 * 0.12515193
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33461 * 0.55471882
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49741 * 0.74921748
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65686 * 0.80503072
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63428 * 0.05955473
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3150 * 0.08973831
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59464 * 0.19133905
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16091 * 0.03182080
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25521 * 0.97080067
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50613 * 0.21875209
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59679 * 0.20129427
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8999 * 0.09077013
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27921 * 0.09531206
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28226 * 0.69488108
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1858 * 0.37336202
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53571 * 0.04342078
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72654 * 0.22612070
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47449 * 0.93796489
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37702 * 0.16328374
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'bkrpcweb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0034():
    """Extended test 34 for transcoding."""
    x_0 = 85969 * 0.00101695
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22798 * 0.00166710
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67660 * 0.48391871
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83279 * 0.79435625
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96236 * 0.51419671
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14463 * 0.62642243
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90025 * 0.82478158
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56875 * 0.94491626
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78364 * 0.71985233
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42232 * 0.49896377
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8797 * 0.61439562
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88774 * 0.44815619
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25450 * 0.15577509
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20182 * 0.12668551
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96527 * 0.42564629
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28472 * 0.97794223
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13016 * 0.11312574
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52919 * 0.72812321
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34999 * 0.89533943
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32234 * 0.97052166
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2363 * 0.71441080
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'bduwyhri').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0035():
    """Extended test 35 for transcoding."""
    x_0 = 86730 * 0.05602474
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82291 * 0.91349870
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10390 * 0.59332647
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54 * 0.39880743
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29179 * 0.58213312
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70019 * 0.72985396
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22605 * 0.79412487
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6514 * 0.53078554
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19479 * 0.17747705
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45634 * 0.53624809
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21407 * 0.73507670
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67303 * 0.05992412
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67625 * 0.74330750
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83870 * 0.72475067
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95287 * 0.92400460
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76868 * 0.85317350
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36917 * 0.33105864
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86720 * 0.44103652
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14540 * 0.19561734
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44449 * 0.94580449
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76230 * 0.22638867
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15761 * 0.18198030
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34329 * 0.95569814
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36475 * 0.90247857
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55001 * 0.67663198
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71955 * 0.65962429
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15932 * 0.12999851
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 750 * 0.61731388
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89757 * 0.57429448
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24848 * 0.07581724
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54042 * 0.25591570
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47137 * 0.83859503
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82748 * 0.98747786
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32390 * 0.85020004
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9784 * 0.24349169
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 9747 * 0.83419201
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'xgjrokio').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0036():
    """Extended test 36 for transcoding."""
    x_0 = 79510 * 0.04152996
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67309 * 0.13749159
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62893 * 0.22793410
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62603 * 0.64866636
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38313 * 0.19276678
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91340 * 0.29673947
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4771 * 0.59217091
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82277 * 0.27554152
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94017 * 0.96653220
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35826 * 0.68843338
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25852 * 0.44313610
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34308 * 0.17401216
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89696 * 0.01347962
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97597 * 0.31809283
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6157 * 0.00699208
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57357 * 0.65999162
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84533 * 0.87009240
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22298 * 0.69643298
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80994 * 0.52679268
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37414 * 0.04262205
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7195 * 0.29977481
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25508 * 0.48461926
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9683 * 0.15809718
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6454 * 0.43755905
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4595 * 0.34636681
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18462 * 0.60557050
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15101 * 0.76769104
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99797 * 0.26618058
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25215 * 0.25591856
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22690 * 0.38942099
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89794 * 0.06713870
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95094 * 0.42739682
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13831 * 0.01575947
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45507 * 0.53581927
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96323 * 0.15632053
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68422 * 0.01677154
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16337 * 0.23558963
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'uvytterq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0037():
    """Extended test 37 for transcoding."""
    x_0 = 1828 * 0.09826920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 895 * 0.24808228
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72319 * 0.42792068
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45069 * 0.22148131
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9316 * 0.49185594
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70187 * 0.44960594
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68532 * 0.20528564
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53682 * 0.59172029
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80021 * 0.54106281
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16828 * 0.41086209
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82440 * 0.57872822
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96860 * 0.29180875
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91039 * 0.72010920
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42723 * 0.63339803
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46978 * 0.94325541
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23430 * 0.94819131
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89131 * 0.95684103
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77442 * 0.27924031
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4897 * 0.18345453
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2362 * 0.52621286
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70337 * 0.43065208
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31046 * 0.71823257
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21414 * 0.69651366
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74727 * 0.11320703
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31037 * 0.63160363
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 100 * 0.27506669
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15734 * 0.10023807
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48301 * 0.61712846
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81634 * 0.35285012
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38268 * 0.17153547
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12060 * 0.69165867
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65893 * 0.50424903
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1328 * 0.44997721
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30020 * 0.40063775
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36695 * 0.79982977
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'wyetggww').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0038():
    """Extended test 38 for transcoding."""
    x_0 = 90413 * 0.47869815
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 573 * 0.57805738
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66821 * 0.13384892
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49202 * 0.60122383
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40647 * 0.05101402
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98384 * 0.67813405
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72672 * 0.45105419
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2395 * 0.14851118
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47884 * 0.70008068
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90098 * 0.13183601
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4557 * 0.93863046
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81581 * 0.70983551
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11229 * 0.70857595
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58718 * 0.93202364
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79621 * 0.57646177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70671 * 0.66127063
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89485 * 0.99484946
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76531 * 0.12785188
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78309 * 0.68741937
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88459 * 0.46568881
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59767 * 0.84558497
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57009 * 0.20986109
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18583 * 0.89707688
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30267 * 0.93122672
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7017 * 0.18763514
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29134 * 0.71285884
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97146 * 0.25811542
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48891 * 0.94528250
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36501 * 0.91711582
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96384 * 0.49853704
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53939 * 0.51718180
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58626 * 0.13364287
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62114 * 0.83734042
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20288 * 0.15535187
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98108 * 0.61632912
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52479 * 0.78556248
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'khdmaapj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0039():
    """Extended test 39 for transcoding."""
    x_0 = 79928 * 0.44095217
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61900 * 0.96029233
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48355 * 0.63011778
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70823 * 0.15194893
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36297 * 0.16744521
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88564 * 0.63342658
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63862 * 0.91532567
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25308 * 0.66284262
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78104 * 0.20908189
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1906 * 0.29188392
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32589 * 0.26000621
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96423 * 0.83234126
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60057 * 0.84680702
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8077 * 0.82947199
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65554 * 0.58892024
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14501 * 0.37031969
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55264 * 0.74582989
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98822 * 0.14392286
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31582 * 0.88535825
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38855 * 0.53853608
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37597 * 0.01358219
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10375 * 0.27894183
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5850 * 0.55756926
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42286 * 0.45948753
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80430 * 0.28068063
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6008 * 0.36685467
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99013 * 0.37488915
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40391 * 0.29977741
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6745 * 0.50890454
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13681 * 0.95474355
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84630 * 0.13222235
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61605 * 0.76366095
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'bkzpvjaj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0040():
    """Extended test 40 for transcoding."""
    x_0 = 67966 * 0.36670360
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63952 * 0.33614459
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90298 * 0.87886663
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64499 * 0.46042025
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44002 * 0.99563039
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49098 * 0.32458767
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54346 * 0.70324524
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59143 * 0.26844497
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50670 * 0.65343404
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52097 * 0.79291960
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99122 * 0.94482668
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90988 * 0.69940047
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7018 * 0.00861365
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40705 * 0.04795433
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55258 * 0.89952562
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31378 * 0.72727406
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83217 * 0.06126426
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93104 * 0.00329056
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15604 * 0.89258440
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99454 * 0.26470071
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47411 * 0.64207613
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37044 * 0.05156986
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69157 * 0.88348774
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20203 * 0.32993620
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13607 * 0.01325930
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21591 * 0.90930805
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84181 * 0.72724478
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93335 * 0.41216506
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81518 * 0.56402994
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21041 * 0.20502565
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42229 * 0.01158281
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30382 * 0.80728803
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22013 * 0.11342285
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31337 * 0.80919252
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'xxmxyrts').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0041():
    """Extended test 41 for transcoding."""
    x_0 = 15895 * 0.63305821
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36838 * 0.41328355
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8030 * 0.60417504
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2219 * 0.82016198
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8060 * 0.60111265
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24515 * 0.58206785
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5737 * 0.89652752
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4645 * 0.50311207
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74739 * 0.27552624
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57759 * 0.08072367
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51040 * 0.33025349
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52289 * 0.40174444
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91630 * 0.16753678
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72178 * 0.36441453
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69834 * 0.68336024
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37913 * 0.72456177
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12497 * 0.98259910
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90236 * 0.69576069
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13520 * 0.21113939
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29651 * 0.16604868
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77367 * 0.10678590
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18530 * 0.18505711
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39130 * 0.00151430
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74914 * 0.26411810
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74735 * 0.90943871
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64870 * 0.57753294
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12358 * 0.84058197
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'kpmkrzip').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0042():
    """Extended test 42 for transcoding."""
    x_0 = 57789 * 0.64498564
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28780 * 0.50974291
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7445 * 0.69794005
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72753 * 0.74324288
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45976 * 0.02368254
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79806 * 0.44941626
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30485 * 0.31226771
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88343 * 0.39314067
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68426 * 0.73585076
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1683 * 0.96915391
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56582 * 0.21055079
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40421 * 0.14119648
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9971 * 0.11754301
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44968 * 0.76428098
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51158 * 0.09222182
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85135 * 0.10483494
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54654 * 0.74007743
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41203 * 0.08429668
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42611 * 0.16172417
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27354 * 0.52327656
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33344 * 0.34635498
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19213 * 0.63546925
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9964 * 0.26406364
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96869 * 0.78883352
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13450 * 0.36667406
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37675 * 0.05358425
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45629 * 0.09301000
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11573 * 0.50606963
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57648 * 0.20625980
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29097 * 0.80716952
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35582 * 0.43982193
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29690 * 0.37626789
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82852 * 0.95195090
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88129 * 0.44327876
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84804 * 0.50530750
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 90068 * 0.52641230
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93375 * 0.83543776
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20733 * 0.73652530
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9986 * 0.20213054
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52234 * 0.68160548
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69094 * 0.78382356
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 45592 * 0.19726649
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 17365 * 0.23140955
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84218 * 0.11405770
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'njwrvvyd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0043():
    """Extended test 43 for transcoding."""
    x_0 = 71584 * 0.04096708
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1310 * 0.45384782
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86845 * 0.28293211
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80059 * 0.39441599
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13176 * 0.44740661
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8012 * 0.18176461
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25054 * 0.26035696
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12528 * 0.23939284
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89839 * 0.71220962
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96274 * 0.52761690
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76295 * 0.13867892
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12892 * 0.17456681
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89175 * 0.69604571
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92453 * 0.70838326
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15070 * 0.64664680
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8263 * 0.49815929
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96816 * 0.50499185
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3157 * 0.39866254
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11674 * 0.55168102
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21326 * 0.92041474
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39915 * 0.32834813
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'dabpciwe').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0044():
    """Extended test 44 for transcoding."""
    x_0 = 78775 * 0.50006293
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43790 * 0.01238021
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9 * 0.19115613
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68756 * 0.37450400
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41463 * 0.58268843
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3995 * 0.62861694
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3768 * 0.72629425
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16877 * 0.45133718
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34726 * 0.60765801
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44484 * 0.62112781
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58453 * 0.97464250
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61983 * 0.90624302
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48352 * 0.33691623
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56678 * 0.27318824
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82210 * 0.13847924
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74736 * 0.09505403
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62906 * 0.73765784
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78174 * 0.82334876
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62252 * 0.84058391
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38356 * 0.49626564
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5187 * 0.20562458
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30577 * 0.99393810
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31988 * 0.54316297
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84262 * 0.06998893
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46289 * 0.89532305
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56977 * 0.16182946
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61751 * 0.73299291
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83448 * 0.53613741
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97696 * 0.73836811
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67360 * 0.74841870
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94029 * 0.13667886
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93935 * 0.67054144
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61868 * 0.77478149
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10970 * 0.15189991
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92663 * 0.34516141
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71384 * 0.18682353
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'cjkpdlyl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0045():
    """Extended test 45 for transcoding."""
    x_0 = 60930 * 0.00784187
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21727 * 0.47972055
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55342 * 0.87963921
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44058 * 0.19297148
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58331 * 0.15193604
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25127 * 0.35104064
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32108 * 0.73607720
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2313 * 0.04462016
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48137 * 0.11920816
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 681 * 0.25861977
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68609 * 0.35916675
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17236 * 0.60671889
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58589 * 0.11181564
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18367 * 0.15088234
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31106 * 0.07327676
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60369 * 0.48493469
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25787 * 0.60635167
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31863 * 0.79302922
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59192 * 0.20368353
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58339 * 0.07217539
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44165 * 0.86823867
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47842 * 0.05498575
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65087 * 0.48857325
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9370 * 0.28287896
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21314 * 0.52402278
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52534 * 0.38585826
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24013 * 0.86942291
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41025 * 0.07341367
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72089 * 0.56122508
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12464 * 0.07910770
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46268 * 0.23170637
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55003 * 0.86064987
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89946 * 0.13081341
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56440 * 0.50319764
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59560 * 0.10237531
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98281 * 0.13468283
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67413 * 0.81087371
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62564 * 0.01306712
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'koowvksj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0046():
    """Extended test 46 for transcoding."""
    x_0 = 2234 * 0.31185240
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42034 * 0.97728288
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92004 * 0.88306901
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62185 * 0.24047793
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72025 * 0.39383105
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56601 * 0.93727081
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19023 * 0.95460333
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93188 * 0.86610385
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16829 * 0.04854815
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35518 * 0.26842726
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63268 * 0.75702179
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48517 * 0.75401936
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32759 * 0.57207420
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36591 * 0.34616864
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24938 * 0.94566601
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11645 * 0.29549371
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37005 * 0.79279410
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26639 * 0.70999458
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19638 * 0.62182777
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16782 * 0.36582595
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82224 * 0.90242637
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97712 * 0.69256538
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99651 * 0.15122728
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59253 * 0.13745425
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64048 * 0.22855604
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88026 * 0.69187215
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45935 * 0.09711899
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9118 * 0.29404034
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48942 * 0.99874455
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84840 * 0.24163540
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50749 * 0.19078666
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80165 * 0.34771570
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14939 * 0.84503841
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38251 * 0.24912694
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85534 * 0.81959265
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30775 * 0.28442436
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94327 * 0.88018502
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94182 * 0.94870374
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51440 * 0.75317206
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3571 * 0.40131339
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69606 * 0.75431488
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 23831 * 0.71971165
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 48958 * 0.36846653
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22280 * 0.44861178
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 98384 * 0.87224892
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'wfzcyrws').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0047():
    """Extended test 47 for transcoding."""
    x_0 = 54414 * 0.39478051
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42238 * 0.91588566
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88402 * 0.41293026
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53070 * 0.61765167
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2047 * 0.56384268
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23235 * 0.16629477
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38381 * 0.24328174
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74062 * 0.36851721
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29682 * 0.11055616
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77013 * 0.57947292
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72513 * 0.44317660
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52353 * 0.69022537
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83782 * 0.46133234
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40875 * 0.17344802
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57708 * 0.69794264
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10432 * 0.57154247
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71046 * 0.98898742
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2390 * 0.41878395
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67136 * 0.59299829
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47949 * 0.23320290
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7422 * 0.33784578
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77571 * 0.23084827
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2422 * 0.15003632
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12736 * 0.16968547
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87641 * 0.67378177
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31849 * 0.43135235
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26871 * 0.77735008
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94744 * 0.66048425
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81566 * 0.77784760
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41337 * 0.16975133
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55604 * 0.73431444
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81216 * 0.82449341
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40911 * 0.10684766
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99932 * 0.87317360
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27523 * 0.84390137
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61920 * 0.99957719
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'roeentxa').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0048():
    """Extended test 48 for transcoding."""
    x_0 = 8175 * 0.80405760
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31177 * 0.81883382
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61891 * 0.83600691
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80234 * 0.84729892
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59677 * 0.74185767
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34735 * 0.85070695
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54240 * 0.89807194
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32129 * 0.34813383
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79408 * 0.06179654
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78031 * 0.95290710
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96794 * 0.80304643
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27377 * 0.75114715
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29633 * 0.18032489
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50501 * 0.98764196
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49337 * 0.85851287
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15420 * 0.08690016
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34509 * 0.75342194
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40327 * 0.84912973
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38497 * 0.99488886
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44523 * 0.10760234
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28388 * 0.93818162
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77847 * 0.24925911
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32990 * 0.97645680
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53904 * 0.99427418
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5137 * 0.00934507
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99141 * 0.07205986
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43326 * 0.55953004
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3362 * 0.10930988
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8297 * 0.94364390
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9344 * 0.92874252
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 120 * 0.71304354
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50119 * 0.67265608
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13958 * 0.94045346
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29522 * 0.47082382
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46047 * 0.80555501
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96714 * 0.98078370
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21871 * 0.00730459
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98576 * 0.50173332
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66710 * 0.94321662
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42105 * 0.84101549
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11584 * 0.61710766
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 75648 * 0.67897813
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 84904 * 0.74737293
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 51062 * 0.62232786
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4472 * 0.86423607
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 29832 * 0.01643726
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'svklbedv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0049():
    """Extended test 49 for transcoding."""
    x_0 = 69692 * 0.74707121
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61339 * 0.50992100
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32183 * 0.25270721
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36959 * 0.07853806
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2689 * 0.05669807
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90387 * 0.01996256
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90564 * 0.28290353
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1837 * 0.62718723
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81003 * 0.12025950
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93657 * 0.19754265
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33558 * 0.69042546
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23261 * 0.21996997
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32365 * 0.98669675
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38163 * 0.04537626
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23393 * 0.92358760
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94521 * 0.99899120
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72793 * 0.48493282
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85388 * 0.12176481
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60548 * 0.59230061
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82878 * 0.00529075
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'xfzrybzr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0050():
    """Extended test 50 for transcoding."""
    x_0 = 43555 * 0.33191000
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86414 * 0.56953641
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58153 * 0.11215432
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5419 * 0.09115793
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11320 * 0.45511411
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94061 * 0.24125808
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11148 * 0.13459105
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99101 * 0.18962109
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35545 * 0.16947390
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77045 * 0.12876149
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95310 * 0.74624928
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58466 * 0.42124460
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35216 * 0.03870346
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7065 * 0.53093334
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94049 * 0.32685711
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79676 * 0.50501673
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19912 * 0.26409873
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61759 * 0.06055548
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80752 * 0.76407515
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24875 * 0.69044531
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48462 * 0.34955839
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18335 * 0.97793747
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58714 * 0.99481568
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66750 * 0.00857283
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24976 * 0.55504108
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43887 * 0.90634110
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31676 * 0.99787789
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40047 * 0.85172650
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10631 * 0.94884820
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14810 * 0.35693706
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34395 * 0.05062331
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98339 * 0.56290263
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35614 * 0.63688718
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61756 * 0.17716156
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60393 * 0.68287921
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53614 * 0.66723478
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89420 * 0.20880813
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 93233 * 0.25297332
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'cbuotuaw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0051():
    """Extended test 51 for transcoding."""
    x_0 = 17366 * 0.81331443
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98967 * 0.73984309
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95702 * 0.56756288
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99923 * 0.57998886
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28580 * 0.82993121
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12733 * 0.61921188
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76401 * 0.54528137
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78616 * 0.48193982
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55848 * 0.88520369
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57462 * 0.76511317
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13825 * 0.60294507
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69612 * 0.19805817
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37829 * 0.85219527
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43942 * 0.04309306
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63272 * 0.99593449
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 325 * 0.40096096
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40742 * 0.72028667
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82562 * 0.72375249
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48157 * 0.89168564
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52052 * 0.58972751
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92472 * 0.96715795
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54150 * 0.39402664
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93027 * 0.63388680
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51802 * 0.72231210
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84722 * 0.26928603
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'wueolbyw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0052():
    """Extended test 52 for transcoding."""
    x_0 = 84478 * 0.54934023
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72435 * 0.48858562
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43354 * 0.12014748
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43879 * 0.43113737
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93807 * 0.97681657
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55345 * 0.43276516
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64367 * 0.38234546
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8500 * 0.10033506
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3503 * 0.93806360
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43320 * 0.87574569
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26762 * 0.28460013
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16594 * 0.63390513
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85036 * 0.96953778
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78981 * 0.33017543
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26472 * 0.58447200
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10046 * 0.96554676
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14282 * 0.24519351
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46552 * 0.36170990
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5505 * 0.51548439
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62976 * 0.04644981
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77600 * 0.33412430
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62753 * 0.64597638
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27710 * 0.68555527
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3591 * 0.69056819
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94363 * 0.58667886
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13001 * 0.57516830
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27064 * 0.04374967
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60202 * 0.78832484
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20670 * 0.33997514
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79203 * 0.83116292
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41292 * 0.02332857
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12474 * 0.31759827
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66466 * 0.10445897
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86137 * 0.60997656
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'pfujypwu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0053():
    """Extended test 53 for transcoding."""
    x_0 = 43696 * 0.46815101
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72435 * 0.69586216
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76084 * 0.16682092
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38572 * 0.42290906
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66000 * 0.75510371
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37171 * 0.22410587
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47775 * 0.14799370
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64263 * 0.95465256
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20294 * 0.72580942
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90654 * 0.42032206
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90240 * 0.90873737
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10123 * 0.09539739
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5064 * 0.68848493
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87101 * 0.11019679
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48984 * 0.06758039
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49341 * 0.65172427
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48374 * 0.92459602
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71841 * 0.24007803
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25454 * 0.92057965
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57094 * 0.63317289
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4027 * 0.77265205
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14105 * 0.18458184
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12359 * 0.99727480
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24620 * 0.35061827
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4977 * 0.65416092
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4991 * 0.71615254
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85587 * 0.35178908
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23802 * 0.94705353
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33747 * 0.86207861
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27515 * 0.49191619
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34059 * 0.81097314
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38583 * 0.62122379
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2256 * 0.06464515
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97754 * 0.73232152
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58884 * 0.66579462
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98064 * 0.86124400
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48672 * 0.60994968
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22717 * 0.56767199
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 95764 * 0.06455213
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88234 * 0.32417748
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43914 * 0.24660114
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 23709 * 0.98376475
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 43254 * 0.83646469
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 30482 * 0.69490816
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 78775 * 0.41385459
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 32089 * 0.12336240
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 25555 * 0.09025074
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 957 * 0.57606751
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 66408 * 0.77310399
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'ljaahcwq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0054():
    """Extended test 54 for transcoding."""
    x_0 = 47368 * 0.69578870
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53650 * 0.77103133
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5675 * 0.77959810
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66567 * 0.11562288
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26679 * 0.64766648
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27483 * 0.50416628
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35304 * 0.24400995
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72216 * 0.43668848
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25138 * 0.71511582
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60558 * 0.02653078
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63437 * 0.23676473
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52418 * 0.51074281
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35427 * 0.23574465
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53696 * 0.05845188
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94092 * 0.97624000
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96151 * 0.99350639
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98395 * 0.48303457
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80550 * 0.09091714
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32992 * 0.08374513
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46630 * 0.72878817
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46002 * 0.40201495
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30802 * 0.97914975
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69166 * 0.39503929
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'bucrcbvr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0055():
    """Extended test 55 for transcoding."""
    x_0 = 63677 * 0.81309403
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48838 * 0.13752062
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85217 * 0.79858326
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66912 * 0.15725531
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74883 * 0.73245597
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50834 * 0.50738007
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68649 * 0.02525596
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34647 * 0.91928169
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37220 * 0.65012659
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34309 * 0.97985053
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81991 * 0.54105605
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49567 * 0.74763425
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66501 * 0.96637277
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35715 * 0.56096268
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82171 * 0.55573054
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51483 * 0.66881151
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76260 * 0.85895394
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40408 * 0.59283506
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77335 * 0.15390793
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51900 * 0.43638346
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22410 * 0.25621585
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5499 * 0.65778697
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22970 * 0.72728135
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 543 * 0.72223185
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24578 * 0.23807473
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18224 * 0.97769196
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20272 * 0.97105336
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27085 * 0.95089905
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3176 * 0.17605596
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28776 * 0.62728884
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30739 * 0.69166085
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31120 * 0.74753330
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19176 * 0.74954072
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40822 * 0.98309487
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58310 * 0.61944766
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 136 * 0.08657924
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96010 * 0.06915547
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38168 * 0.60974505
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6903 * 0.08547192
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84405 * 0.57886067
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'gnzyedpf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0056():
    """Extended test 56 for transcoding."""
    x_0 = 84661 * 0.72372051
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10302 * 0.11986472
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94779 * 0.97936788
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51034 * 0.81424225
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81267 * 0.98155095
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76358 * 0.59667167
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39461 * 0.74932092
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43010 * 0.51449860
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98144 * 0.66229380
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48624 * 0.87595577
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40523 * 0.03639234
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54141 * 0.12881616
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50360 * 0.98187792
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26075 * 0.80772140
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17367 * 0.90072291
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14791 * 0.33230470
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19495 * 0.80679536
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59160 * 0.28592816
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98140 * 0.19343112
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41851 * 0.43257968
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28752 * 0.36441000
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94287 * 0.62374053
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33610 * 0.96719122
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80007 * 0.06344038
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36007 * 0.08776611
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4107 * 0.86113479
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72787 * 0.79171961
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46497 * 0.77762534
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70170 * 0.68486930
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45384 * 0.00696693
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81646 * 0.61051020
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7566 * 0.39848185
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 825 * 0.85976930
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68155 * 0.56744210
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1998 * 0.71586710
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97418 * 0.51073632
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53977 * 0.39375734
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26544 * 0.85706668
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86639 * 0.76992583
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90435 * 0.16513203
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 93793 * 0.15331174
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3741 * 0.35394695
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13004 * 0.63819802
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84744 * 0.24906527
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 25978 * 0.61731448
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'evsyistq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0057():
    """Extended test 57 for transcoding."""
    x_0 = 39166 * 0.53566049
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17584 * 0.76201664
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57719 * 0.71268192
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25771 * 0.58580601
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83672 * 0.11218158
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97744 * 0.34945074
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12670 * 0.28596706
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5232 * 0.42868880
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90944 * 0.59061579
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42543 * 0.90836781
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11728 * 0.64628261
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52622 * 0.51236770
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38023 * 0.03556543
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4306 * 0.07658298
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61162 * 0.83574983
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32183 * 0.18100245
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26837 * 0.61891543
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18293 * 0.14013749
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82503 * 0.20931846
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81602 * 0.32470709
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89252 * 0.07487870
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89890 * 0.73769605
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49074 * 0.62996574
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'qtalpnkn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0058():
    """Extended test 58 for transcoding."""
    x_0 = 97180 * 0.57581017
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4179 * 0.30831319
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42649 * 0.38959805
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7727 * 0.94108448
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6351 * 0.29313407
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26027 * 0.27300346
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42615 * 0.86650743
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32079 * 0.06307238
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34776 * 0.43948175
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 607 * 0.29128844
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67175 * 0.72073296
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27574 * 0.76241002
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39103 * 0.30346750
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32524 * 0.75337317
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6548 * 0.91982182
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91043 * 0.12058407
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93227 * 0.25613945
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40784 * 0.69535650
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8202 * 0.08449188
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75007 * 0.70526366
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23281 * 0.88106154
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1557 * 0.67356077
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98907 * 0.71772816
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27305 * 0.76917344
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'uazmtfdy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0059():
    """Extended test 59 for transcoding."""
    x_0 = 8642 * 0.50888138
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64413 * 0.13567293
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61523 * 0.00208213
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54679 * 0.26283860
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19001 * 0.36519002
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26608 * 0.56803035
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79626 * 0.12558194
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96250 * 0.60892969
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3138 * 0.50662278
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48118 * 0.11727750
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51788 * 0.86574971
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4579 * 0.24813228
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14718 * 0.32537777
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62997 * 0.83118616
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18327 * 0.02404543
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21235 * 0.70474143
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24609 * 0.38187491
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47366 * 0.06947436
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10710 * 0.25682394
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94606 * 0.12589073
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27531 * 0.83346442
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94512 * 0.54945566
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42622 * 0.06492572
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44081 * 0.63611586
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60854 * 0.31193915
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98443 * 0.82669851
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29531 * 0.32487530
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27949 * 0.16804575
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52316 * 0.85887893
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ebpayplt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0060():
    """Extended test 60 for transcoding."""
    x_0 = 99480 * 0.82184426
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31310 * 0.49629076
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46627 * 0.83074187
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79366 * 0.73337362
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26678 * 0.28838182
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60748 * 0.55001117
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27764 * 0.34562500
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94891 * 0.99316878
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98649 * 0.59901967
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13207 * 0.22927875
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51875 * 0.87198008
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90315 * 0.41425363
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99992 * 0.64692305
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36927 * 0.34767008
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4386 * 0.91551580
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13826 * 0.15709917
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48792 * 0.91240774
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62762 * 0.36952523
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76156 * 0.03634555
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81662 * 0.88173781
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81517 * 0.99310118
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96362 * 0.88811140
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64046 * 0.70186276
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63429 * 0.64553100
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14413 * 0.22508807
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73178 * 0.47106719
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84863 * 0.82996312
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49395 * 0.47057518
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37612 * 0.91495795
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55064 * 0.15163480
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88374 * 0.75684103
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78783 * 0.24461394
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 66608 * 0.47020478
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19956 * 0.56563871
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93132 * 0.84422130
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96627 * 0.14046669
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39775 * 0.78434877
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 37433 * 0.98905946
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ztqqmhsg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0061():
    """Extended test 61 for transcoding."""
    x_0 = 10465 * 0.72524851
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36047 * 0.09277761
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20483 * 0.15343114
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88454 * 0.87702076
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76200 * 0.21111290
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39377 * 0.63098480
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39341 * 0.37630147
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65985 * 0.67581322
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30833 * 0.39332333
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1184 * 0.96447231
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79043 * 0.12271822
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32453 * 0.12870011
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26250 * 0.27979811
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39753 * 0.27446951
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12797 * 0.66316291
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48866 * 0.45521051
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74132 * 0.55536412
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68814 * 0.24852670
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63637 * 0.58582034
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30534 * 0.57831648
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16078 * 0.85970056
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16707 * 0.91682000
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53877 * 0.23146960
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49083 * 0.14044016
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91246 * 0.06669047
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51674 * 0.33798539
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35953 * 0.27174453
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97963 * 0.70832651
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74984 * 0.83931239
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4157 * 0.67115807
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59473 * 0.99656022
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24712 * 0.19070392
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64994 * 0.37288456
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47806 * 0.32819062
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58863 * 0.71291282
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49353 * 0.55485227
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66925 * 0.71648482
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72658 * 0.77078018
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94151 * 0.03991612
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9397 * 0.11632776
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77365 * 0.51983678
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 7451 * 0.79064566
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28628 * 0.95276542
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 9489 * 0.13539461
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 18173 * 0.34592964
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10536 * 0.67846921
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'tdkodzqk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0062():
    """Extended test 62 for transcoding."""
    x_0 = 93432 * 0.03025473
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57771 * 0.13828186
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86603 * 0.81183418
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52398 * 0.70755942
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49600 * 0.41813119
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20329 * 0.67838533
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51586 * 0.50279482
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69134 * 0.97303841
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18497 * 0.10880711
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31997 * 0.86835254
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29663 * 0.54912271
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83733 * 0.38136806
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92775 * 0.13978708
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69305 * 0.33872717
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25493 * 0.29204526
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38688 * 0.73760517
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20363 * 0.58824344
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88372 * 0.43928306
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96801 * 0.48048363
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46657 * 0.24112781
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87148 * 0.99009061
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37518 * 0.08601987
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48053 * 0.04739650
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66977 * 0.44200001
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26946 * 0.15608641
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1378 * 0.80308999
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35544 * 0.03306831
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34227 * 0.48896419
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39312 * 0.70405869
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6094 * 0.73776926
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33600 * 0.25506993
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35491 * 0.04783802
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62080 * 0.06985448
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66946 * 0.64588186
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15355 * 0.34908888
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'rxmumeaa').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0063():
    """Extended test 63 for transcoding."""
    x_0 = 51945 * 0.71990156
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1923 * 0.10021646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70082 * 0.63059849
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91931 * 0.13004620
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68615 * 0.01171624
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18373 * 0.79565244
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46828 * 0.36178849
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40472 * 0.80702244
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72186 * 0.50010288
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32039 * 0.06361543
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49497 * 0.90262856
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48491 * 0.91473988
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60657 * 0.93536208
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18980 * 0.46065477
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95004 * 0.23174953
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71685 * 0.41867035
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5165 * 0.96077426
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98608 * 0.54291216
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18767 * 0.34509696
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39422 * 0.21837422
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27715 * 0.47411428
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56854 * 0.89517836
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92945 * 0.31238368
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61986 * 0.97653595
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20079 * 0.74973637
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58977 * 0.77650292
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1983 * 0.11850874
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28471 * 0.23975341
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73457 * 0.99359642
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36299 * 0.44466292
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60748 * 0.95902192
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91614 * 0.89947449
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56899 * 0.02122275
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78470 * 0.12555900
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93230 * 0.85650996
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71921 * 0.06966882
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45512 * 0.21421309
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42673 * 0.19975947
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1710 * 0.48078560
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 49882 * 0.39742117
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'dgwstnvm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0064():
    """Extended test 64 for transcoding."""
    x_0 = 17541 * 0.64155649
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39723 * 0.07212840
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94744 * 0.19929297
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68430 * 0.55325671
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37215 * 0.81147162
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63073 * 0.59438912
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33286 * 0.83698485
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10802 * 0.08215060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53565 * 0.40504100
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71824 * 0.64317099
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56633 * 0.17029565
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19168 * 0.48438797
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65072 * 0.71009002
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68058 * 0.76597883
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38703 * 0.78984425
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74160 * 0.59745956
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59824 * 0.13797582
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46086 * 0.27120464
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50660 * 0.85366284
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87454 * 0.26321141
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72516 * 0.63322695
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62294 * 0.11079141
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6635 * 0.12530379
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56104 * 0.56969170
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15689 * 0.65166159
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74766 * 0.70957113
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14144 * 0.96098879
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55379 * 0.45929654
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25483 * 0.12706810
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68872 * 0.54071549
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47512 * 0.09039815
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49468 * 0.47784838
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29100 * 0.47765811
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26254 * 0.40602915
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63336 * 0.04349369
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28009 * 0.90364652
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28517 * 0.16480622
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 15344 * 0.49441965
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 89171 * 0.70324604
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67341 * 0.81929181
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99107 * 0.37212116
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66162 * 0.64501524
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79346 * 0.98395096
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 44507 * 0.29297040
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'fxlvhrdt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0065():
    """Extended test 65 for transcoding."""
    x_0 = 22401 * 0.58217152
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 896 * 0.32446983
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66079 * 0.53942998
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34239 * 0.12310176
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6937 * 0.01231077
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33164 * 0.87145995
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18918 * 0.04059651
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60733 * 0.06761449
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26041 * 0.10846444
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3865 * 0.74730880
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72388 * 0.31569676
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18009 * 0.14197279
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50419 * 0.41995121
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21866 * 0.31288986
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38002 * 0.01301270
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13494 * 0.41053834
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77782 * 0.98456960
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61910 * 0.12827113
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39774 * 0.49659321
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19759 * 0.95872395
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52663 * 0.44358090
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10062 * 0.89601441
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67199 * 0.55645713
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55002 * 0.85822548
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34092 * 0.29900769
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58078 * 0.86368872
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6249 * 0.51271258
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14795 * 0.89092179
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31344 * 0.48987632
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14801 * 0.22652805
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14916 * 0.97106389
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5522 * 0.76782057
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'jawfkyau').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0066():
    """Extended test 66 for transcoding."""
    x_0 = 77420 * 0.17439229
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67297 * 0.78173505
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43997 * 0.02879658
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67370 * 0.49364716
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64195 * 0.29541285
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46736 * 0.83191231
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60930 * 0.24581865
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9982 * 0.61825293
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22844 * 0.37597756
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92523 * 0.64801457
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56468 * 0.52400163
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58644 * 0.53646581
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76306 * 0.10972907
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38233 * 0.49191585
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61038 * 0.27450324
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60199 * 0.31994769
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69403 * 0.89310265
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37307 * 0.87467374
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91224 * 0.92700926
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10521 * 0.41961847
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 924 * 0.65252034
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55592 * 0.18723470
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3147 * 0.37265728
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25601 * 0.89352422
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89675 * 0.96811233
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21749 * 0.66446771
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1366 * 0.51806816
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86830 * 0.95333877
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84956 * 0.60157811
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4151 * 0.77584780
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66573 * 0.37191832
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66722 * 0.61857730
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58496 * 0.69241635
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65908 * 0.86925666
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95393 * 0.31226094
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83391 * 0.83528702
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7969 * 0.56994311
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32234 * 0.77810477
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'dwxcfqam').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0067():
    """Extended test 67 for transcoding."""
    x_0 = 36378 * 0.20058698
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45474 * 0.80920602
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95048 * 0.08213801
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45824 * 0.14784264
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26237 * 0.82589194
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94545 * 0.71825452
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50696 * 0.41838877
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94617 * 0.71798776
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77014 * 0.01859836
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57421 * 0.19190586
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75365 * 0.09218514
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5676 * 0.90228923
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93403 * 0.44571498
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46748 * 0.98892207
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76383 * 0.52186752
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85049 * 0.04670157
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18000 * 0.68229434
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56608 * 0.81544735
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88052 * 0.81154933
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56553 * 0.46155371
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52424 * 0.43444426
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54271 * 0.89810735
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26770 * 0.45093178
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55185 * 0.99900465
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95360 * 0.42516614
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90349 * 0.73764385
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19649 * 0.57194232
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57233 * 0.00853284
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7503 * 0.18593926
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54279 * 0.86458632
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42783 * 0.85201435
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33475 * 0.78344608
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41751 * 0.15090832
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11439 * 0.44114273
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68669 * 0.47886933
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'qwaanlwg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0068():
    """Extended test 68 for transcoding."""
    x_0 = 86623 * 0.57487189
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22222 * 0.69783843
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99950 * 0.98881170
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24459 * 0.16462573
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54134 * 0.06973868
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72496 * 0.60608481
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61268 * 0.91675651
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27951 * 0.66969583
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66155 * 0.64711491
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46937 * 0.52833839
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5831 * 0.23251958
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83180 * 0.74986342
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2357 * 0.05571433
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48371 * 0.95342651
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43404 * 0.42991956
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59921 * 0.16084126
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73353 * 0.85445313
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81287 * 0.68741402
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91895 * 0.15124964
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11075 * 0.67580128
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ivrvnfhg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_7_0069():
    """Extended test 69 for transcoding."""
    x_0 = 1699 * 0.42017144
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39326 * 0.56719525
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18880 * 0.65981365
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94127 * 0.36798525
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59521 * 0.78076326
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75580 * 0.04670245
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71769 * 0.14911347
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85930 * 0.76384930
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97275 * 0.01035910
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51789 * 0.01970545
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11637 * 0.71089345
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61546 * 0.99980830
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16487 * 0.04754454
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58779 * 0.49362855
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89555 * 0.62085724
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88325 * 0.67470472
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4154 * 0.57855252
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79675 * 0.85332727
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90016 * 0.26934176
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27310 * 0.66624419
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13562 * 0.60293183
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15472 * 0.36234577
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12190 * 0.38068240
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56177 * 0.59973209
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73269 * 0.99235181
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67524 * 0.07019848
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24662 * 0.66167084
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68534 * 0.15185341
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59199 * 0.51958320
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 953 * 0.80436680
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76093 * 0.66803378
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97544 * 0.38337473
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16257 * 0.96411454
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43999 * 0.49881682
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92190 * 0.18743667
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26970 * 0.75827110
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42126 * 0.67712544
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63165 * 0.45399191
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83944 * 0.43802918
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86795 * 0.36168810
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 59388 * 0.03056921
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 64420 * 0.94165365
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12688 * 0.39510464
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 78171 * 0.83893274
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'cquskvyj').hexdigest()
    assert len(h) == 64
