"""Extended tests for transcoding suite 5."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_transcoding_extended_5_0000():
    """Extended test 0 for transcoding."""
    x_0 = 38326 * 0.44215948
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3922 * 0.25024632
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59145 * 0.75316864
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96047 * 0.14444339
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53701 * 0.90786635
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58639 * 0.83015166
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19497 * 0.31679475
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15941 * 0.69087442
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42899 * 0.39456570
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9666 * 0.50031730
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31352 * 0.69457292
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65226 * 0.86832590
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36350 * 0.79612489
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52215 * 0.55494572
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31837 * 0.93513674
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64569 * 0.95768472
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86699 * 0.10859362
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55003 * 0.03471425
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9185 * 0.73714425
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2427 * 0.01677175
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33389 * 0.25489815
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4685 * 0.94336234
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32121 * 0.80092993
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34398 * 0.94653775
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24359 * 0.54746887
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45760 * 0.47107808
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57133 * 0.80961285
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86744 * 0.10075684
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12529 * 0.47094623
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45638 * 0.33637930
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59362 * 0.97969333
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59244 * 0.49729433
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30378 * 0.70484400
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45452 * 0.48224303
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69332 * 0.84501149
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53939 * 0.09887569
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75227 * 0.09979098
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67658 * 0.17923659
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38548 * 0.99366776
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68005 * 0.08177144
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 92807 * 0.20182272
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20871 * 0.52100441
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57201 * 0.42637578
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 91459 * 0.50519439
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 31315 * 0.74115680
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4317 * 0.72059544
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 68938 * 0.34526589
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 4037 * 0.33446629
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'lsghbzgd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0001():
    """Extended test 1 for transcoding."""
    x_0 = 84916 * 0.05458888
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39491 * 0.05737646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47601 * 0.01297916
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96064 * 0.35539791
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69718 * 0.14368818
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31458 * 0.01674133
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41819 * 0.78285887
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62073 * 0.00590683
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72832 * 0.96911833
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38034 * 0.54857365
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46037 * 0.67558476
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22768 * 0.90119649
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68422 * 0.97129261
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20889 * 0.48693601
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63805 * 0.33231572
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19073 * 0.42846630
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29186 * 0.80070409
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65831 * 0.36193296
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61395 * 0.87385776
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77864 * 0.39284891
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70737 * 0.19638970
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33881 * 0.99792096
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38670 * 0.49632292
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26176 * 0.62905782
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54873 * 0.32515203
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24299 * 0.92638111
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21238 * 0.42707259
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62876 * 0.84909424
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23230 * 0.43638534
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5820 * 0.10053483
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8816 * 0.76094767
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26214 * 0.56441411
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 9496 * 0.04691101
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10510 * 0.73190341
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36360 * 0.55444772
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'qfgigpny').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0002():
    """Extended test 2 for transcoding."""
    x_0 = 54287 * 0.30117700
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80724 * 0.00726124
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45995 * 0.97995658
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24858 * 0.22357079
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47981 * 0.62305853
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50510 * 0.85548885
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71201 * 0.98148815
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61650 * 0.02012921
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95854 * 0.29399384
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41231 * 0.20420828
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94045 * 0.63201893
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89701 * 0.48715351
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37213 * 0.73536922
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20005 * 0.36280177
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70969 * 0.39729222
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9845 * 0.87687797
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67715 * 0.26423041
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62904 * 0.89827077
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43821 * 0.53249277
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31525 * 0.01824113
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9952 * 0.44028101
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92778 * 0.16448461
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3607 * 0.26893870
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3494 * 0.16216203
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52279 * 0.70645749
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87554 * 0.34723514
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17521 * 0.86596759
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82559 * 0.64295688
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 462 * 0.05418823
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92229 * 0.98784780
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4157 * 0.51017934
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30923 * 0.68573511
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78351 * 0.46937552
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85820 * 0.69381746
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59613 * 0.98290503
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24846 * 0.12495588
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94865 * 0.19163522
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33185 * 0.04046017
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93911 * 0.56496517
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 36372 * 0.99250424
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 30101 * 0.29096119
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66485 * 0.08690097
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 3753 * 0.36505524
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 63381 * 0.24978612
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 48500 * 0.28349744
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 55067 * 0.66078550
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'bnmepyzy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0003():
    """Extended test 3 for transcoding."""
    x_0 = 45620 * 0.03736640
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86533 * 0.28654081
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18915 * 0.21730679
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38808 * 0.70718140
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85682 * 0.19360862
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95923 * 0.73540098
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7282 * 0.94261717
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49015 * 0.06474784
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9927 * 0.64733553
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3293 * 0.46892280
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33972 * 0.37032863
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16290 * 0.74231139
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7800 * 0.47045269
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75733 * 0.03401811
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57182 * 0.65687253
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31342 * 0.25769803
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60901 * 0.17279727
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49860 * 0.75172513
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54307 * 0.32504002
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96959 * 0.19327742
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70226 * 0.56683751
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50666 * 0.72454603
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33394 * 0.29206446
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77857 * 0.64654574
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22799 * 0.54451394
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47832 * 0.87988008
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16266 * 0.99554739
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63304 * 0.09868345
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23798 * 0.26334908
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44965 * 0.79670853
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46117 * 0.46705684
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1724 * 0.73396578
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59003 * 0.31137882
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 4148 * 0.44698788
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96542 * 0.88645695
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80372 * 0.96361733
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51273 * 0.33838599
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7395 * 0.41512623
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15017 * 0.23956727
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 800 * 0.27848119
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49556 * 0.85604912
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 91203 * 0.51806381
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 45272 * 0.67559416
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61771 * 0.93688542
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'vvacghmv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0004():
    """Extended test 4 for transcoding."""
    x_0 = 86345 * 0.37308040
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17883 * 0.65519569
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60472 * 0.11649557
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91498 * 0.72815895
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33590 * 0.91389358
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6574 * 0.70460250
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85461 * 0.43282084
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83512 * 0.47496298
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20435 * 0.87716074
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20527 * 0.96372436
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83757 * 0.43600823
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82709 * 0.19079221
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67443 * 0.63886381
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28539 * 0.99908869
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73943 * 0.01952580
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9853 * 0.53074099
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30984 * 0.04117253
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87751 * 0.29594640
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47687 * 0.51300496
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7233 * 0.55367827
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48637 * 0.70332536
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15650 * 0.76732679
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94748 * 0.83263124
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72553 * 0.58785881
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75949 * 0.08976829
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98641 * 0.00033099
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90806 * 0.07561486
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73438 * 0.44652003
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37021 * 0.52488829
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98214 * 0.03841792
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10050 * 0.31706158
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60190 * 0.82540301
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15622 * 0.46981231
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19198 * 0.63414453
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70097 * 0.66043978
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30026 * 0.75762891
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63632 * 0.41488927
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87528 * 0.82844514
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'knhwfaru').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0005():
    """Extended test 5 for transcoding."""
    x_0 = 54723 * 0.80159242
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46513 * 0.64897879
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4085 * 0.21646527
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78487 * 0.60260919
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21522 * 0.40368737
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45171 * 0.20577625
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74073 * 0.27995755
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49014 * 0.38767169
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14218 * 0.22878231
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25625 * 0.98076827
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76886 * 0.77301912
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39255 * 0.27401336
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53295 * 0.90841574
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21668 * 0.57468617
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56459 * 0.06739227
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4050 * 0.68376336
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47956 * 0.55163795
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83363 * 0.15074684
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 583 * 0.31822970
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20578 * 0.16559536
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70816 * 0.32003578
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17756 * 0.56302375
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32716 * 0.14362378
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76112 * 0.34787593
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19015 * 0.53378776
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58009 * 0.61664276
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20167 * 0.97041973
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18041 * 0.66792053
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47572 * 0.95540624
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33859 * 0.57694723
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26031 * 0.14856069
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87231 * 0.93515396
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75483 * 0.70834175
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5535 * 0.82757027
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5249 * 0.27011014
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34408 * 0.41470239
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69568 * 0.44628692
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97645 * 0.02906448
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51976 * 0.94481275
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45221 * 0.07428314
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95061 * 0.59690288
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 56089 * 0.53326232
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79824 * 0.57795950
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'dysxfwjc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0006():
    """Extended test 6 for transcoding."""
    x_0 = 24452 * 0.11394287
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4806 * 0.83557679
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86676 * 0.88851231
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8057 * 0.94817416
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14430 * 0.42511189
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88044 * 0.73688581
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69471 * 0.49906272
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73270 * 0.15837504
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9418 * 0.40336974
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81389 * 0.62774886
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30662 * 0.49883856
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87192 * 0.17289820
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18240 * 0.84411127
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93382 * 0.07121157
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47736 * 0.85717790
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93989 * 0.11260461
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43420 * 0.93201050
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16073 * 0.44827824
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88433 * 0.29920130
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8327 * 0.85741810
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66452 * 0.06023257
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88221 * 0.47961142
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88072 * 0.41220852
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96859 * 0.14306353
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72961 * 0.78977530
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14857 * 0.07276494
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9517 * 0.55121630
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39754 * 0.08049554
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64442 * 0.10316157
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33549 * 0.13883912
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4604 * 0.86577678
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'zphvvjwo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0007():
    """Extended test 7 for transcoding."""
    x_0 = 39914 * 0.34627837
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86772 * 0.27274164
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97882 * 0.67148870
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47024 * 0.24932419
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98762 * 0.83982263
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69654 * 0.59992652
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97792 * 0.71966475
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92672 * 0.70343988
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75219 * 0.51394257
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79032 * 0.07430116
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37915 * 0.17437168
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22514 * 0.45080638
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22595 * 0.52812790
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12640 * 0.69608707
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85414 * 0.99222351
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63071 * 0.40703032
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26322 * 0.28049901
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15056 * 0.61377966
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86909 * 0.41354102
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59567 * 0.25353125
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7334 * 0.94013480
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14409 * 0.53157109
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16940 * 0.99336318
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7067 * 0.10818844
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11920 * 0.17763166
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86346 * 0.30043207
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82719 * 0.18589209
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86909 * 0.39869584
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46474 * 0.37447649
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65031 * 0.77926200
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92112 * 0.40434646
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 641 * 0.98912116
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83391 * 0.75931725
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99980 * 0.87765500
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52914 * 0.63387910
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 91672 * 0.67961259
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51566 * 0.49889462
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31054 * 0.55613723
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17873 * 0.54073409
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59378 * 0.01522283
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27058 * 0.87887647
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13410 * 0.57887274
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 82916 * 0.54103300
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 56375 * 0.86110962
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'mbspqxjk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0008():
    """Extended test 8 for transcoding."""
    x_0 = 80061 * 0.40117113
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27659 * 0.14206151
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16067 * 0.80010572
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29331 * 0.93929204
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25741 * 0.10957946
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14771 * 0.58573764
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73132 * 0.43473728
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95784 * 0.03185608
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81522 * 0.22329375
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41259 * 0.51674779
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52717 * 0.23644462
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93570 * 0.31264637
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76381 * 0.17536003
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36642 * 0.75759463
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18519 * 0.45866716
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82224 * 0.55595768
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33815 * 0.59813095
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72661 * 0.15743925
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13022 * 0.73266410
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61669 * 0.37543620
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25381 * 0.42439227
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27744 * 0.19566646
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3880 * 0.30094420
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38480 * 0.05173027
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12474 * 0.45929474
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11599 * 0.41161660
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34944 * 0.72959460
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66770 * 0.38754619
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3042 * 0.66745283
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57365 * 0.50596440
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32790 * 0.60283838
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22696 * 0.39706040
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4100 * 0.27680707
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57911 * 0.89911578
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84543 * 0.96776205
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51398 * 0.48945977
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1968 * 0.75450051
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78199 * 0.60108766
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77950 * 0.63082928
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82022 * 0.85116278
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 67822 * 0.63200750
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 29598 * 0.05466251
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 69326 * 0.49078148
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 59426 * 0.54457864
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71849 * 0.34212188
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'bhbldqui').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0009():
    """Extended test 9 for transcoding."""
    x_0 = 4771 * 0.01249000
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94098 * 0.94452951
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15430 * 0.78715583
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59727 * 0.76898812
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66493 * 0.92996275
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 831 * 0.95807085
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80999 * 0.28067100
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63114 * 0.39684275
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64471 * 0.94638512
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36508 * 0.75685531
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82976 * 0.59577161
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34622 * 0.08850174
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86895 * 0.66623868
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14706 * 0.34795297
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20781 * 0.30923308
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84913 * 0.95327959
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82872 * 0.93324634
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29641 * 0.09023819
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98674 * 0.38925243
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75906 * 0.98075560
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32531 * 0.33145276
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78778 * 0.93182286
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52834 * 0.67248968
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54602 * 0.22870406
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71597 * 0.68033493
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32856 * 0.06404307
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32413 * 0.95728627
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15586 * 0.80916847
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'wcaooefv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0010():
    """Extended test 10 for transcoding."""
    x_0 = 89226 * 0.33070809
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74466 * 0.50436926
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73180 * 0.31589016
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65400 * 0.51690108
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72083 * 0.85309961
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62633 * 0.93876004
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32208 * 0.01056017
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37647 * 0.57166569
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18556 * 0.69652558
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65933 * 0.95119102
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12830 * 0.62344498
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31042 * 0.71822530
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42937 * 0.18067028
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29157 * 0.24148939
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69937 * 0.94579215
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67153 * 0.84088286
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3642 * 0.68185032
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6101 * 0.13040790
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34057 * 0.60847745
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4387 * 0.03738013
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85509 * 0.21467008
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93285 * 0.01129616
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41859 * 0.43785539
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38198 * 0.43572518
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16834 * 0.30072847
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10542 * 0.42067740
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94178 * 0.52224715
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37617 * 0.49963495
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64709 * 0.82713436
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75266 * 0.73504544
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'kvehsbej').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0011():
    """Extended test 11 for transcoding."""
    x_0 = 88213 * 0.71074579
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5470 * 0.30274411
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42633 * 0.39513548
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37656 * 0.08678966
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30608 * 0.32288599
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35046 * 0.92337715
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71228 * 0.98090494
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33787 * 0.15204887
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27705 * 0.38540990
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93163 * 0.20730653
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31547 * 0.33617669
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85704 * 0.47490485
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95620 * 0.50995800
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98038 * 0.35455592
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38198 * 0.62835612
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91133 * 0.52446720
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24812 * 0.71339003
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18342 * 0.42054535
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16482 * 0.85301553
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80910 * 0.47720553
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48451 * 0.41833734
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15342 * 0.91683284
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41842 * 0.86167512
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39075 * 0.10351696
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58311 * 0.87141567
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78324 * 0.50720160
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12811 * 0.49211356
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2846 * 0.85214065
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36407 * 0.15187502
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47433 * 0.57624950
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54195 * 0.42528462
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33268 * 0.20893588
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89663 * 0.77399183
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84241 * 0.03131223
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'crtimqop').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0012():
    """Extended test 12 for transcoding."""
    x_0 = 54958 * 0.05353296
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2850 * 0.59639202
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99438 * 0.25635980
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97375 * 0.85567936
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79329 * 0.45242018
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57857 * 0.77131657
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99049 * 0.47335078
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65978 * 0.28298656
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26184 * 0.12346310
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31944 * 0.84467532
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72541 * 0.72303371
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87839 * 0.50411328
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30251 * 0.62441211
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54949 * 0.52570207
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4029 * 0.41359617
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79833 * 0.71688948
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87921 * 0.69932239
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61041 * 0.77386927
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54929 * 0.02243882
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1790 * 0.10805088
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28926 * 0.69015757
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27746 * 0.02711063
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34715 * 0.77359532
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40922 * 0.92945675
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13427 * 0.04449356
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62412 * 0.33782554
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6678 * 0.82989759
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36007 * 0.93192692
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95371 * 0.95284622
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 84899 * 0.81117063
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56209 * 0.73709092
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50384 * 0.46478690
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26343 * 0.61668077
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24011 * 0.77632698
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7683 * 0.56338297
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97732 * 0.03400991
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90851 * 0.36891948
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2895 * 0.59980909
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26331 * 0.60276859
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22792 * 0.41878427
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95174 * 0.22437218
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22384 * 0.11309398
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16567 * 0.00981876
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 80204 * 0.84777784
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 30279 * 0.97101595
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 56052 * 0.20100821
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'uxmhesgd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0013():
    """Extended test 13 for transcoding."""
    x_0 = 97364 * 0.15556702
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70953 * 0.90883124
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53253 * 0.22310206
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30500 * 0.63842714
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24632 * 0.35633064
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35238 * 0.13504425
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85438 * 0.88474754
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28119 * 0.43595685
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5437 * 0.02724474
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15443 * 0.68561946
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31078 * 0.92914125
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61329 * 0.33279958
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39514 * 0.81251917
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90220 * 0.61746398
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44988 * 0.86096922
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79874 * 0.90851541
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26632 * 0.30209505
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51368 * 0.53915957
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4601 * 0.39908978
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21991 * 0.18174140
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36178 * 0.78403460
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41757 * 0.90608017
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80377 * 0.17923898
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23814 * 0.93883317
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83762 * 0.11481927
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78081 * 0.01574171
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40752 * 0.44894502
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'vzbrxiwd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0014():
    """Extended test 14 for transcoding."""
    x_0 = 26678 * 0.36403251
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31827 * 0.74081776
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37473 * 0.99553279
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6125 * 0.31613478
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62396 * 0.26699359
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29064 * 0.53285433
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83718 * 0.85431694
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31259 * 0.40623509
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64195 * 0.34670534
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93928 * 0.69232861
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78422 * 0.15850416
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83739 * 0.89910218
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25113 * 0.08141808
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94190 * 0.91768677
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69356 * 0.36934518
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83967 * 0.00074035
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11065 * 0.32278875
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47787 * 0.46351382
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94476 * 0.84744752
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69043 * 0.00363439
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62619 * 0.11957375
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97924 * 0.47722231
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78381 * 0.40667314
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'frpkekgw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0015():
    """Extended test 15 for transcoding."""
    x_0 = 32825 * 0.98330247
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25131 * 0.92066451
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75972 * 0.79803368
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66013 * 0.83547512
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83368 * 0.45107413
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36302 * 0.17874093
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41727 * 0.01227973
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67657 * 0.41324755
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30127 * 0.85884303
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84032 * 0.43251693
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51150 * 0.77411074
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53592 * 0.64135531
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70811 * 0.93895575
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82766 * 0.50848342
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84557 * 0.52471787
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81615 * 0.74442732
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75086 * 0.03067130
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64882 * 0.29931423
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55171 * 0.56242533
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64630 * 0.67768881
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27670 * 0.71507341
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21336 * 0.77827755
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43731 * 0.13882400
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38480 * 0.11173674
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98123 * 0.33957195
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23822 * 0.53635613
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80044 * 0.32903649
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72404 * 0.30405917
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21354 * 0.82719767
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'xbbqflls').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0016():
    """Extended test 16 for transcoding."""
    x_0 = 22081 * 0.53101611
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49987 * 0.66001357
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39099 * 0.03131486
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84627 * 0.00931559
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30771 * 0.71495874
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80699 * 0.72486223
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56633 * 0.32621047
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29559 * 0.93050395
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58553 * 0.74678153
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19837 * 0.66419830
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48151 * 0.12116982
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80682 * 0.24278017
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86087 * 0.23955800
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35344 * 0.80608282
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14758 * 0.77914144
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36239 * 0.95097289
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11178 * 0.61929030
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29851 * 0.88799098
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95474 * 0.99963740
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90990 * 0.60249794
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36364 * 0.51483295
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59572 * 0.53115251
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'zmzlauot').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0017():
    """Extended test 17 for transcoding."""
    x_0 = 53961 * 0.51884064
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67640 * 0.25294052
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97663 * 0.04519916
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75601 * 0.33766562
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85482 * 0.27491015
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25603 * 0.30941254
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94310 * 0.56015889
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58990 * 0.29406822
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52522 * 0.88407715
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89308 * 0.49037296
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80761 * 0.57508481
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29598 * 0.55425405
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25584 * 0.91484522
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22420 * 0.42565986
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39686 * 0.41956503
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46478 * 0.23127090
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57204 * 0.87586994
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74512 * 0.16319547
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92265 * 0.66489801
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27345 * 0.68655842
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66361 * 0.97945389
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67147 * 0.07939064
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'fcatcdaz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0018():
    """Extended test 18 for transcoding."""
    x_0 = 12901 * 0.61290598
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80392 * 0.38189580
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45811 * 0.57235578
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50715 * 0.51387456
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75375 * 0.85855283
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32200 * 0.81793594
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71990 * 0.12418406
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34157 * 0.17800808
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8292 * 0.83552487
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13209 * 0.44070469
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90588 * 0.09926529
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89621 * 0.11014748
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43478 * 0.98023378
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59240 * 0.08244889
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52961 * 0.85644419
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94506 * 0.83734927
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23623 * 0.04181162
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33151 * 0.60629169
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50237 * 0.40408466
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93973 * 0.20035254
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56962 * 0.58093645
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68573 * 0.77697189
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50768 * 0.71278597
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43592 * 0.27590803
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9912 * 0.28258202
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3598 * 0.47018302
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44890 * 0.46058335
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72181 * 0.63159266
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54367 * 0.93690628
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85617 * 0.71589826
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47670 * 0.93878839
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53679 * 0.03073645
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52791 * 0.13716875
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7991 * 0.77025109
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61059 * 0.78101616
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31885 * 0.03131118
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39378 * 0.64760549
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2871 * 0.62972534
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72736 * 0.68807184
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88717 * 0.16935388
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3482 * 0.33762738
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 64281 * 0.51476541
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'azafmapi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0019():
    """Extended test 19 for transcoding."""
    x_0 = 82249 * 0.59256839
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48026 * 0.45126624
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83108 * 0.48230264
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81957 * 0.49761485
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8929 * 0.49397587
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19272 * 0.40183023
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65971 * 0.07824858
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49961 * 0.93397369
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54955 * 0.16319271
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52193 * 0.45915900
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83272 * 0.30622223
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60649 * 0.10636065
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15344 * 0.48203458
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8400 * 0.48666938
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72897 * 0.28276749
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29231 * 0.95850699
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30378 * 0.08621556
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70411 * 0.58571681
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80235 * 0.01735992
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35366 * 0.49630981
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4841 * 0.28014061
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45346 * 0.52132800
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38449 * 0.03329536
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43232 * 0.15591656
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58843 * 0.44344919
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63779 * 0.91969523
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47401 * 0.52345224
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 189 * 0.96162257
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35565 * 0.56739671
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49804 * 0.32162550
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35637 * 0.58768135
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25156 * 0.95792593
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1303 * 0.17848557
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'aoiexiub').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0020():
    """Extended test 20 for transcoding."""
    x_0 = 52439 * 0.55309013
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79401 * 0.83542249
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97230 * 0.76793840
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79176 * 0.51934496
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11312 * 0.19765920
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19775 * 0.95905018
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37480 * 0.16590396
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74474 * 0.33907791
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99186 * 0.78669717
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7632 * 0.00018131
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6377 * 0.62150090
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41408 * 0.10111069
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84415 * 0.66450685
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95162 * 0.59356738
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80908 * 0.81638069
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9667 * 0.77351647
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18930 * 0.85510936
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42248 * 0.62414437
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88876 * 0.72949186
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26176 * 0.45580431
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19369 * 0.07915569
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65898 * 0.91656293
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74608 * 0.66803468
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86134 * 0.09672346
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'nhgzlyvm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0021():
    """Extended test 21 for transcoding."""
    x_0 = 68129 * 0.86347573
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56915 * 0.71632913
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86340 * 0.76579623
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84078 * 0.96877990
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22487 * 0.56066347
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23164 * 0.66000877
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75975 * 0.79898119
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86429 * 0.79295722
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76428 * 0.36055100
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61612 * 0.19320389
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72274 * 0.44526953
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13255 * 0.23408411
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59042 * 0.98065412
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48173 * 0.04818727
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69541 * 0.19825432
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16131 * 0.05858602
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91002 * 0.24972120
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27957 * 0.08552873
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54018 * 0.95621006
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98829 * 0.92637290
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75879 * 0.05558248
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82807 * 0.64684858
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92243 * 0.13540375
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68271 * 0.19981807
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3344 * 0.53934338
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56919 * 0.46478441
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65120 * 0.76663034
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49845 * 0.89160020
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30228 * 0.87972244
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57459 * 0.44941449
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89662 * 0.72707269
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60406 * 0.39139126
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36875 * 0.70304704
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35075 * 0.38745798
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95484 * 0.25254070
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53547 * 0.00743169
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91285 * 0.05249078
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32301 * 0.81390317
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61399 * 0.27184120
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 5298 * 0.81521106
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 55629 * 0.72259991
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 95373 * 0.10317165
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42867 * 0.17501523
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58113 * 0.14752971
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 58138 * 0.99636350
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 64601 * 0.48473601
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 21917 * 0.52127191
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 11560 * 0.92585930
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 27856 * 0.29185499
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'dqwincps').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0022():
    """Extended test 22 for transcoding."""
    x_0 = 11854 * 0.20547509
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73486 * 0.44200221
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45802 * 0.82985881
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38463 * 0.67099354
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1717 * 0.30380858
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7591 * 0.72532239
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43121 * 0.28450118
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43031 * 0.33615474
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46499 * 0.80889723
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83921 * 0.76933157
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37088 * 0.53039229
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37358 * 0.48267408
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12276 * 0.99213108
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8517 * 0.25918920
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34198 * 0.11883276
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58974 * 0.71014824
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5763 * 0.17949819
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1761 * 0.82842194
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72387 * 0.12065587
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56372 * 0.64396929
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30462 * 0.41806854
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90835 * 0.15251455
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58438 * 0.74057400
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13951 * 0.71456278
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2970 * 0.27983208
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87475 * 0.18254503
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33926 * 0.98848996
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84024 * 0.67125340
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72359 * 0.63079283
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64129 * 0.99424666
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91188 * 0.22048025
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23603 * 0.09612503
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46823 * 0.47779371
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62787 * 0.62416040
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80451 * 0.65834396
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89353 * 0.25665897
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91658 * 0.08603376
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32341 * 0.94718790
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 49409 * 0.60731123
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19861 * 0.39068720
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 30165 * 0.44207340
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 7879 * 0.65394093
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 63029 * 0.48698627
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 3147 * 0.52923339
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 51520 * 0.49032528
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 42519 * 0.16828873
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17344 * 0.24132031
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'hggypfew').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0023():
    """Extended test 23 for transcoding."""
    x_0 = 31178 * 0.73340633
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84430 * 0.62903731
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80699 * 0.77050275
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7509 * 0.75141419
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41249 * 0.97642038
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63705 * 0.74476668
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60069 * 0.30824817
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28205 * 0.23801212
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84242 * 0.63432711
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7663 * 0.80987084
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80120 * 0.86485019
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10097 * 0.82962644
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42785 * 0.63727839
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63157 * 0.02347486
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58720 * 0.69847182
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21693 * 0.17594969
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62779 * 0.50265151
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19973 * 0.62256672
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76125 * 0.97700704
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1309 * 0.33764625
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71250 * 0.60984798
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29512 * 0.82039547
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'gjlotjpu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0024():
    """Extended test 24 for transcoding."""
    x_0 = 39558 * 0.99996861
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65998 * 0.50071297
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95845 * 0.29382709
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17900 * 0.74802794
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76897 * 0.77713832
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78676 * 0.22164770
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90047 * 0.10124200
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24237 * 0.31357956
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98300 * 0.65321112
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72348 * 0.44106616
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28455 * 0.64040566
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45314 * 0.40590733
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73314 * 0.03365557
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49920 * 0.17104956
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83400 * 0.07540530
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92454 * 0.05386659
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64660 * 0.02298923
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25907 * 0.98376921
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86350 * 0.12484769
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65094 * 0.11633447
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37266 * 0.30365281
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10573 * 0.78907744
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'adyvghvr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0025():
    """Extended test 25 for transcoding."""
    x_0 = 54890 * 0.96890687
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19356 * 0.99529791
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40497 * 0.74601034
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83393 * 0.57338348
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57395 * 0.89468012
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70523 * 0.64072374
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49219 * 0.89254397
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99811 * 0.40962011
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39520 * 0.97481932
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58698 * 0.76265465
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9561 * 0.85654731
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96050 * 0.70784334
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71289 * 0.01106303
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12358 * 0.47718716
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74368 * 0.04408203
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88554 * 0.09863430
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4414 * 0.86949324
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80543 * 0.43235337
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20659 * 0.82252349
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 984 * 0.20890396
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50920 * 0.06525672
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73423 * 0.85985054
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58882 * 0.08344733
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26509 * 0.89186954
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57142 * 0.41407354
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22618 * 0.62551050
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43876 * 0.97405732
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94614 * 0.02317452
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85983 * 0.01267294
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30737 * 0.86117520
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61157 * 0.23805925
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46586 * 0.91400230
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67644 * 0.07206413
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31192 * 0.31365856
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97759 * 0.23498680
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34932 * 0.29153933
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8840 * 0.42352986
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 99705 * 0.22377633
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ymredtms').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0026():
    """Extended test 26 for transcoding."""
    x_0 = 48557 * 0.50628873
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 972 * 0.12024778
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47485 * 0.01297295
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65996 * 0.91935282
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90087 * 0.10806151
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18987 * 0.29520692
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77489 * 0.32632512
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77388 * 0.64197601
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93996 * 0.38450255
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38000 * 0.30803470
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36443 * 0.77165075
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22675 * 0.11200019
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82875 * 0.25280673
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71455 * 0.58008113
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28958 * 0.86297823
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35866 * 0.94047601
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66070 * 0.50097716
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51068 * 0.32650620
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76099 * 0.58067090
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16931 * 0.32659607
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35426 * 0.39269522
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13978 * 0.67596671
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25963 * 0.50772926
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57249 * 0.38945292
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14236 * 0.25575494
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12039 * 0.68312909
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88129 * 0.58908050
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12560 * 0.08591449
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99020 * 0.49849561
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60757 * 0.01635084
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40418 * 0.12460934
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24582 * 0.82501725
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29440 * 0.91976123
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20509 * 0.44921497
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 827 * 0.50482161
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85709 * 0.45085014
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 92817 * 0.49301905
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48089 * 0.41675191
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41207 * 0.01522166
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66055 * 0.20383835
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99827 * 0.38351864
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 51662 * 0.13701055
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 19476 * 0.82836581
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 44285 * 0.05679665
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'kyyojgzx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0027():
    """Extended test 27 for transcoding."""
    x_0 = 11965 * 0.97611240
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39504 * 0.86329904
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93362 * 0.98378439
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51488 * 0.30088909
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10449 * 0.18320574
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18136 * 0.96108752
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85537 * 0.15276214
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50425 * 0.44179357
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7230 * 0.02814462
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40105 * 0.38549628
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72426 * 0.28326020
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4760 * 0.39653886
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38258 * 0.24287730
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14550 * 0.98098902
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94456 * 0.25049306
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22053 * 0.96207871
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99373 * 0.26198984
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14188 * 0.77533182
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15466 * 0.91799779
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56373 * 0.70894141
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54304 * 0.58003093
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21474 * 0.93110770
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38387 * 0.44023706
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94953 * 0.22328441
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84042 * 0.16439830
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91993 * 0.12320907
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2251 * 0.08846558
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82089 * 0.22407885
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4264 * 0.00133992
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32769 * 0.31574896
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69125 * 0.20283602
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81426 * 0.24613617
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57767 * 0.98868868
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67279 * 0.05830553
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74520 * 0.33163252
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82916 * 0.56153673
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85153 * 0.81618062
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9527 * 0.65999057
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69315 * 0.50421165
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97044 * 0.46259612
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 16759 * 0.35041057
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 73251 * 0.05569815
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'bqkgxkxp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0028():
    """Extended test 28 for transcoding."""
    x_0 = 93331 * 0.10776892
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28681 * 0.67638600
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73211 * 0.94929222
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41619 * 0.31329846
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38205 * 0.05743174
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76357 * 0.93065516
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17765 * 0.74670584
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54581 * 0.00211712
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96620 * 0.61550303
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1052 * 0.54150274
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84530 * 0.65940181
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84189 * 0.30447126
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66632 * 0.56795781
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44608 * 0.59589030
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51793 * 0.07337485
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36030 * 0.04517770
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85657 * 0.84651067
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92963 * 0.59884933
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26146 * 0.40976168
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3231 * 0.51337866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55170 * 0.11060345
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54363 * 0.95219598
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18519 * 0.65129471
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29550 * 0.16308416
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39532 * 0.65712567
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'vhbwllmb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0029():
    """Extended test 29 for transcoding."""
    x_0 = 54893 * 0.93703152
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94505 * 0.05147189
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44606 * 0.47292668
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1841 * 0.17551789
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82900 * 0.44113879
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62034 * 0.71379971
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65494 * 0.97399724
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2252 * 0.78247884
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74569 * 0.00019473
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63968 * 0.72942468
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95187 * 0.87085029
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95059 * 0.79375444
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49226 * 0.33100114
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71182 * 0.99195947
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81743 * 0.46245168
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29095 * 0.84186343
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52126 * 0.75384342
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77817 * 0.89522902
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27443 * 0.40352584
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13415 * 0.33036834
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18625 * 0.80714205
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45643 * 0.67567011
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67669 * 0.96190639
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5648 * 0.18160833
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97876 * 0.64230022
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93091 * 0.20819222
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7212 * 0.84103694
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78694 * 0.68003517
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1863 * 0.94348271
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49288 * 0.74585461
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72593 * 0.13912741
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76878 * 0.40774956
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73674 * 0.07747254
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48296 * 0.04328284
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25592 * 0.83982132
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22592 * 0.51406761
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3451 * 0.00856029
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69721 * 0.87432759
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84231 * 0.65612020
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72365 * 0.97852068
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64962 * 0.04339758
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92768 * 0.59074837
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 64546 * 0.36857309
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 87244 * 0.04941255
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92295 * 0.75447839
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 76679 * 0.14358832
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 74450 * 0.36525244
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 62140 * 0.66765896
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'efhkqhqf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0030():
    """Extended test 30 for transcoding."""
    x_0 = 51750 * 0.02572105
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53078 * 0.73012679
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36153 * 0.32166206
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52534 * 0.46728782
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59663 * 0.24246934
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88087 * 0.62439970
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98567 * 0.29078314
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5688 * 0.07941243
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41908 * 0.94143661
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50670 * 0.32512787
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59026 * 0.69303848
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16816 * 0.67924657
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91884 * 0.30782314
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36981 * 0.32563873
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78028 * 0.39342684
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2013 * 0.08209666
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39836 * 0.94693436
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78915 * 0.12943258
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70985 * 0.77955178
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92890 * 0.55387666
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44971 * 0.90765468
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35292 * 0.71608017
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76847 * 0.07518442
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53143 * 0.10221992
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59454 * 0.85300540
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8044 * 0.82149987
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39983 * 0.30232555
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1891 * 0.90505922
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65234 * 0.36276720
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52572 * 0.21886742
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48655 * 0.89014215
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65848 * 0.81400559
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48057 * 0.53360988
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'bwkdfytm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0031():
    """Extended test 31 for transcoding."""
    x_0 = 62022 * 0.61898301
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72729 * 0.23693000
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36462 * 0.99349262
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38048 * 0.47656887
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97507 * 0.16936751
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47490 * 0.62737501
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42464 * 0.13243531
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37043 * 0.88120540
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15582 * 0.06292240
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58094 * 0.77629512
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80768 * 0.30443725
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42586 * 0.60121367
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73623 * 0.14062827
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93999 * 0.50865704
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74358 * 0.83060768
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1641 * 0.34852560
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24345 * 0.74297764
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40105 * 0.35186790
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42973 * 0.05410639
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84074 * 0.39227136
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11044 * 0.14370761
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9495 * 0.45758957
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87215 * 0.57001520
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12956 * 0.92003281
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57700 * 0.36689117
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34777 * 0.61608436
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83080 * 0.25175798
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95728 * 0.89757280
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'istmunvq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0032():
    """Extended test 32 for transcoding."""
    x_0 = 62683 * 0.89895359
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78338 * 0.36649588
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60458 * 0.35101204
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13453 * 0.64549449
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28632 * 0.93230636
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79886 * 0.30767530
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7036 * 0.83968419
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19339 * 0.31332742
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74906 * 0.48078504
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82129 * 0.84084779
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50207 * 0.39482069
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23170 * 0.07392170
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16411 * 0.78454895
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7356 * 0.03428456
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58079 * 0.52316877
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19326 * 0.01516543
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44458 * 0.87437707
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85171 * 0.43121339
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89324 * 0.98695456
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12713 * 0.69822948
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51293 * 0.62609567
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80161 * 0.80759579
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68908 * 0.16232606
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86344 * 0.43308997
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42068 * 0.63437298
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60990 * 0.49726351
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64440 * 0.31142472
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 197 * 0.95006310
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7679 * 0.53312154
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59817 * 0.40646566
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51901 * 0.22246802
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54767 * 0.93940136
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89845 * 0.14737085
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74467 * 0.45075415
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52706 * 0.58949721
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ggwvfzab').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0033():
    """Extended test 33 for transcoding."""
    x_0 = 8302 * 0.33392758
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58026 * 0.08059959
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88182 * 0.95815855
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26303 * 0.18423414
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66868 * 0.96151109
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19365 * 0.99478564
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70741 * 0.32519246
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25237 * 0.93114061
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26681 * 0.04151449
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12217 * 0.35626109
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39012 * 0.93349682
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12297 * 0.20837759
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92094 * 0.46689073
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63140 * 0.28030318
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3865 * 0.60085018
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70561 * 0.64905450
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29644 * 0.41968300
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93318 * 0.93418971
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24424 * 0.52574900
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2311 * 0.77425151
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32896 * 0.58079292
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79699 * 0.86524331
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25769 * 0.04748187
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82205 * 0.08487786
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65429 * 0.12264043
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97978 * 0.29952502
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79658 * 0.40090673
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85250 * 0.76699720
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15226 * 0.75501269
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98352 * 0.09667766
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9269 * 0.30111092
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8931 * 0.25078411
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'hulgjgmq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0034():
    """Extended test 34 for transcoding."""
    x_0 = 91040 * 0.27943210
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56073 * 0.13407445
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77753 * 0.14512525
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81255 * 0.70882535
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13970 * 0.53956502
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73051 * 0.75224850
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37207 * 0.97852104
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28746 * 0.45617661
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98642 * 0.44490512
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44974 * 0.26355867
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84428 * 0.97430123
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52845 * 0.58404741
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37579 * 0.07270450
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36361 * 0.44494976
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72245 * 0.94453001
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49893 * 0.29871898
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84381 * 0.06426447
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82866 * 0.15807147
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57460 * 0.90987506
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52639 * 0.72996693
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90410 * 0.19390469
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42344 * 0.63286564
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23778 * 0.88147701
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17684 * 0.69665106
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54767 * 0.78302497
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70971 * 0.51385890
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98886 * 0.18802202
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82249 * 0.30450826
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60994 * 0.67944261
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14044 * 0.82823762
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'fiotvwyb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0035():
    """Extended test 35 for transcoding."""
    x_0 = 33165 * 0.50265200
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15356 * 0.66777179
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48818 * 0.54681210
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80643 * 0.88444443
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64608 * 0.34547210
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31968 * 0.78297113
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90012 * 0.04184782
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70259 * 0.29190541
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16428 * 0.77784509
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93036 * 0.91362711
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44569 * 0.33895299
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32212 * 0.60081933
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60943 * 0.53344791
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85485 * 0.50748416
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86433 * 0.16922335
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14040 * 0.72149408
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44483 * 0.39628965
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82474 * 0.33420658
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43540 * 0.00894077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28561 * 0.19997055
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15935 * 0.11546174
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38749 * 0.57756376
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39007 * 0.40007739
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48616 * 0.10331394
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73623 * 0.36502364
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87304 * 0.57699546
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43066 * 0.66792436
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35139 * 0.21827569
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69264 * 0.43777579
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82748 * 0.63621004
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63616 * 0.80842826
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57060 * 0.87126317
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44218 * 0.85699126
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37070 * 0.06977944
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39073 * 0.53411528
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22936 * 0.50048592
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'aklrlxey').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0036():
    """Extended test 36 for transcoding."""
    x_0 = 46363 * 0.85215059
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2512 * 0.00333121
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72932 * 0.81680273
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42181 * 0.07854121
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98204 * 0.69849073
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94995 * 0.67118539
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99155 * 0.92126716
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92192 * 0.10521548
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34707 * 0.43977550
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95878 * 0.07671144
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75892 * 0.83242669
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97454 * 0.33565452
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49048 * 0.24912900
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63844 * 0.65649621
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29070 * 0.32064884
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29022 * 0.36762255
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11339 * 0.00379949
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60350 * 0.63243443
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65619 * 0.97837461
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54034 * 0.26410065
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92050 * 0.95089949
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3522 * 0.81703749
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52705 * 0.76109787
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32273 * 0.96945217
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96484 * 0.50971026
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91819 * 0.35418413
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68 * 0.27725538
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81365 * 0.54152125
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18196 * 0.96919181
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1604 * 0.10298991
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90506 * 0.88552391
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16917 * 0.66831696
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17421 * 0.45231567
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64997 * 0.22972672
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61556 * 0.83682319
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59488 * 0.18937730
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40551 * 0.68466437
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8705 * 0.24134358
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19444 * 0.02612190
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73846 * 0.30631457
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 67897 * 0.47550661
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69743 * 0.40245227
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 62200 * 0.98592023
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 45179 * 0.84191926
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 51833 * 0.53289627
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'vefmygmn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0037():
    """Extended test 37 for transcoding."""
    x_0 = 36721 * 0.36610167
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59058 * 0.86437762
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61563 * 0.07628734
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98917 * 0.34113150
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20330 * 0.32788527
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44518 * 0.22847060
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25107 * 0.79368887
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23839 * 0.95894356
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56625 * 0.97556736
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95142 * 0.05039674
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57343 * 0.98617827
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9427 * 0.35318241
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37117 * 0.59079914
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64218 * 0.27855447
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74786 * 0.31216460
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86208 * 0.29726902
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65911 * 0.33029762
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38505 * 0.23963021
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90881 * 0.53774440
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82092 * 0.78462859
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38651 * 0.81383658
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93429 * 0.55635381
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16181 * 0.82334195
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13234 * 0.86530656
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64552 * 0.40515264
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67920 * 0.34237503
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19814 * 0.92229318
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58584 * 0.18710055
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'fqkenwhq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0038():
    """Extended test 38 for transcoding."""
    x_0 = 59203 * 0.75724783
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24604 * 0.64148467
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65699 * 0.30497857
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32695 * 0.70967344
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60327 * 0.68718707
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71669 * 0.01294402
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89837 * 0.66515565
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59271 * 0.70371099
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17495 * 0.94917756
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33771 * 0.83497569
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34754 * 0.68768923
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58969 * 0.99344532
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16393 * 0.34589458
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94845 * 0.58456230
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49198 * 0.82113460
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63811 * 0.42733158
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16429 * 0.15981131
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81430 * 0.13832672
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94859 * 0.93457962
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70286 * 0.09170599
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73578 * 0.44216062
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27309 * 0.76260481
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45903 * 0.94993779
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68836 * 0.68496806
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3931 * 0.19215670
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60533 * 0.13801835
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80298 * 0.00707596
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88416 * 0.98199995
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46742 * 0.10874501
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'uegejbqp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0039():
    """Extended test 39 for transcoding."""
    x_0 = 98206 * 0.81572520
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61607 * 0.77709698
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86231 * 0.61873016
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45278 * 0.11526564
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39186 * 0.30263302
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46322 * 0.03726786
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28910 * 0.25838903
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85959 * 0.44905861
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10856 * 0.74192048
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52477 * 0.12391033
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92157 * 0.60567109
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66566 * 0.80466899
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53499 * 0.08285128
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13067 * 0.06583799
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87447 * 0.18598317
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38200 * 0.91849027
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67203 * 0.38942885
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40809 * 0.18004486
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78072 * 0.88665672
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52367 * 0.77956504
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60917 * 0.11061524
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60836 * 0.50130904
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46501 * 0.93254300
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14489 * 0.87048147
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81234 * 0.03388522
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35095 * 0.57372797
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8383 * 0.69963241
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84910 * 0.78987135
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49494 * 0.96264846
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13429 * 0.99957520
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64773 * 0.74908021
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75081 * 0.49009972
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42980 * 0.01322535
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 635 * 0.69144066
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43322 * 0.63298142
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2311 * 0.11673930
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11338 * 0.61264521
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 51056 * 0.64428085
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ykrzxreq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0040():
    """Extended test 40 for transcoding."""
    x_0 = 84350 * 0.10289177
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6295 * 0.75471858
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49811 * 0.28049700
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62350 * 0.81905323
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82015 * 0.85013088
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39756 * 0.90525697
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55350 * 0.62435143
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52306 * 0.40184883
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96962 * 0.06898036
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2880 * 0.21688932
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29435 * 0.18752502
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12500 * 0.40501433
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3265 * 0.95405061
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8453 * 0.31337420
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62192 * 0.71904318
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66402 * 0.19942311
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99586 * 0.88106992
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69979 * 0.32070187
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97128 * 0.45464716
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15394 * 0.70053003
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92014 * 0.66498431
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53804 * 0.61188707
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60643 * 0.14712398
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71465 * 0.55761166
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72960 * 0.98366069
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11472 * 0.61946967
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93137 * 0.82454622
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35137 * 0.93912751
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42933 * 0.51614403
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16340 * 0.21769913
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44254 * 0.46630668
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53183 * 0.82082099
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23669 * 0.89295991
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66452 * 0.54329156
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93609 * 0.36236761
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4485 * 0.01352808
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80154 * 0.42103985
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98956 * 0.88711661
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 54807 * 0.51526125
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22674 * 0.32222467
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48387 * 0.58593482
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59569 * 0.14847404
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 86262 * 0.15218830
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 65290 * 0.97573934
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'vqtrhvkt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0041():
    """Extended test 41 for transcoding."""
    x_0 = 90659 * 0.62832607
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43408 * 0.64362532
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51565 * 0.58427633
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77226 * 0.92257698
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72486 * 0.06859958
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76830 * 0.10098460
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61457 * 0.42538415
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43432 * 0.44362256
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74940 * 0.95880721
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2591 * 0.85387098
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55333 * 0.67307327
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90917 * 0.34617175
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24216 * 0.55130704
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46356 * 0.89367238
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57853 * 0.93097720
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80251 * 0.80171536
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94950 * 0.48670480
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50071 * 0.13562380
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14131 * 0.40326797
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98223 * 0.21692733
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98895 * 0.60305135
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95206 * 0.63534679
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30791 * 0.93344049
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77167 * 0.14029856
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28381 * 0.11031218
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74484 * 0.91253197
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85531 * 0.66989598
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98803 * 0.88461855
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20304 * 0.59970041
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22977 * 0.64152843
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28673 * 0.25143992
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11422 * 0.06821501
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45035 * 0.95607659
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97519 * 0.52141391
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93581 * 0.73465551
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1215 * 0.95100851
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73460 * 0.01653028
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44760 * 0.13693206
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'oumdtzso').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0042():
    """Extended test 42 for transcoding."""
    x_0 = 45299 * 0.39099137
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24244 * 0.80036001
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58960 * 0.15775857
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8489 * 0.20456824
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74261 * 0.25735144
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40860 * 0.74850043
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94435 * 0.67941595
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20912 * 0.32565777
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54632 * 0.83309961
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79563 * 0.52575582
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43458 * 0.77655905
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21407 * 0.63986399
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86153 * 0.59006143
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26936 * 0.86115041
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20566 * 0.52321311
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62213 * 0.61762782
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66609 * 0.80410233
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74121 * 0.30252747
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8918 * 0.80070724
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39681 * 0.42548624
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15872 * 0.58917580
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3429 * 0.82946539
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24424 * 0.89578540
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86734 * 0.46399705
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38464 * 0.94613951
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23893 * 0.28494217
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51397 * 0.42373508
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34647 * 0.48422300
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78503 * 0.29077879
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74995 * 0.48746041
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37962 * 0.12661243
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'zcrysjrb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0043():
    """Extended test 43 for transcoding."""
    x_0 = 4809 * 0.08301349
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39822 * 0.50386071
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77075 * 0.30545787
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80962 * 0.75285123
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71043 * 0.94570248
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48692 * 0.19683176
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75044 * 0.90448061
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5847 * 0.66411098
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7857 * 0.42590197
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84310 * 0.79238711
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15873 * 0.74735709
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94814 * 0.28327175
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9505 * 0.85868480
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61061 * 0.23567044
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77855 * 0.20803552
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63920 * 0.88510026
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22451 * 0.03510902
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73647 * 0.62635746
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12543 * 0.75174749
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63092 * 0.13989146
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21830 * 0.79852625
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33369 * 0.26189391
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86747 * 0.32169730
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2224 * 0.89896417
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71943 * 0.18446435
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70460 * 0.59322949
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81989 * 0.61944555
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22952 * 0.71766526
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72760 * 0.46404257
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11969 * 0.87416123
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39323 * 0.19741885
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67381 * 0.75431850
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'rnhwstec').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0044():
    """Extended test 44 for transcoding."""
    x_0 = 29986 * 0.53876853
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94560 * 0.62074442
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53630 * 0.06978220
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28744 * 0.55569981
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17979 * 0.32396857
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12501 * 0.90563426
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66251 * 0.83575886
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22642 * 0.88064819
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76367 * 0.47544402
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60694 * 0.83501748
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73338 * 0.68730189
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23380 * 0.57088411
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79334 * 0.44347463
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49187 * 0.78447119
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8691 * 0.11449911
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45021 * 0.99874475
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94855 * 0.33213072
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75071 * 0.77688027
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12892 * 0.21178951
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65758 * 0.96818425
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28588 * 0.38594158
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29839 * 0.36286633
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46238 * 0.82887126
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70365 * 0.42798031
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40880 * 0.23970009
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85644 * 0.40371530
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72430 * 0.31642893
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'wrntsbpu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0045():
    """Extended test 45 for transcoding."""
    x_0 = 5145 * 0.86969960
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96287 * 0.41866875
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89886 * 0.03563002
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92681 * 0.83700695
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60306 * 0.24351615
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50837 * 0.24616940
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15383 * 0.88928301
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72951 * 0.90341411
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95013 * 0.38939229
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71999 * 0.10141772
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9573 * 0.81720569
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56245 * 0.11534813
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50566 * 0.20746212
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74228 * 0.41537577
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65847 * 0.24684201
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79175 * 0.52815122
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49563 * 0.05638319
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46231 * 0.38222412
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33612 * 0.39592184
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19334 * 0.85625310
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88149 * 0.31959215
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83116 * 0.68839463
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99724 * 0.67059779
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60576 * 0.65411905
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36158 * 0.08678831
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75995 * 0.41078619
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59027 * 0.70236051
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23067 * 0.53533913
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 164 * 0.04618052
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29121 * 0.17495037
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12732 * 0.66085632
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13844 * 0.14703724
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68325 * 0.47285691
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69539 * 0.97701236
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21068 * 0.04727149
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42323 * 0.84220112
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21528 * 0.15016577
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49743 * 0.03966253
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47749 * 0.82293013
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31657 * 0.08374597
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'yzzrpxep').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0046():
    """Extended test 46 for transcoding."""
    x_0 = 48072 * 0.20272704
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36242 * 0.79496492
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73202 * 0.04701155
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1815 * 0.17399107
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86501 * 0.88979526
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91924 * 0.48316351
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76776 * 0.05261491
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92937 * 0.70396157
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46238 * 0.30896096
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94247 * 0.82314389
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38724 * 0.34859877
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42583 * 0.84481283
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67345 * 0.95369678
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97048 * 0.75228121
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92925 * 0.47130442
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31241 * 0.55863820
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 451 * 0.26062717
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17984 * 0.96200336
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90367 * 0.37399443
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97283 * 0.42120318
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92065 * 0.17031145
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57938 * 0.89579356
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6638 * 0.14897152
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40284 * 0.25954560
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64474 * 0.95093327
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39168 * 0.20746784
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12685 * 0.50189494
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90354 * 0.11463980
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65978 * 0.44608693
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88836 * 0.53560594
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69086 * 0.50844653
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'jvluxjvn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0047():
    """Extended test 47 for transcoding."""
    x_0 = 42114 * 0.33032620
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13704 * 0.25999772
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41139 * 0.03100943
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85147 * 0.92217271
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34921 * 0.12148599
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79280 * 0.66919651
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18003 * 0.88420390
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11511 * 0.09187031
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8324 * 0.89136180
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4479 * 0.28997290
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50495 * 0.45495808
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17401 * 0.88962710
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60486 * 0.22071789
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97991 * 0.48737470
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46352 * 0.88801178
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83627 * 0.77518729
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84496 * 0.61431831
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79275 * 0.86546422
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65263 * 0.55927831
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48094 * 0.76020586
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57897 * 0.21395788
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16791 * 0.18291514
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30672 * 0.35009779
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 751 * 0.31328978
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44599 * 0.21393157
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99462 * 0.19425479
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 781 * 0.77113716
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66980 * 0.56569697
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35087 * 0.03677984
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71282 * 0.86358194
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47414 * 0.70908585
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97934 * 0.02985608
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65982 * 0.63436335
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36560 * 0.75197071
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17390 * 0.30174561
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30652 * 0.64497560
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14384 * 0.17143289
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86045 * 0.79264908
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 89833 * 0.41832775
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47175 * 0.70575963
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21971 * 0.78748232
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74494 * 0.17334077
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'qtpbdkic').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0048():
    """Extended test 48 for transcoding."""
    x_0 = 14858 * 0.96402942
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58960 * 0.45628762
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32174 * 0.42681173
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69670 * 0.66884650
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7960 * 0.87510127
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32956 * 0.70427188
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74464 * 0.61027794
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91926 * 0.17864913
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58216 * 0.64991162
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54413 * 0.34190647
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49225 * 0.24450606
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83010 * 0.97651088
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32014 * 0.21360161
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77560 * 0.94042253
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12748 * 0.95638305
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30484 * 0.34934064
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17619 * 0.13379831
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49624 * 0.70360163
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91371 * 0.59627431
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38673 * 0.98266836
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58324 * 0.18506777
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67069 * 0.00234187
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30345 * 0.46650903
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90324 * 0.89898209
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25250 * 0.12063952
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41399 * 0.40563878
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63064 * 0.58163507
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45674 * 0.60883467
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70607 * 0.80863420
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6101 * 0.31811979
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46819 * 0.58264297
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38327 * 0.72956211
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7641 * 0.65008382
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95846 * 0.22989028
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'wckhlsbl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0049():
    """Extended test 49 for transcoding."""
    x_0 = 48671 * 0.22252202
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50010 * 0.62454821
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35460 * 0.34510656
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9334 * 0.54253264
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72399 * 0.14972388
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78768 * 0.69567292
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15129 * 0.99171363
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45445 * 0.05098041
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24741 * 0.18883516
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9533 * 0.62801434
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55944 * 0.23705282
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44096 * 0.80975540
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89909 * 0.16771246
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22817 * 0.61341276
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28482 * 0.56037553
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87524 * 0.41015164
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74034 * 0.65367421
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81663 * 0.63386133
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64305 * 0.27331907
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84390 * 0.01154800
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76326 * 0.26357508
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86164 * 0.49302307
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25986 * 0.81745295
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94788 * 0.07963652
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27581 * 0.66522394
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87233 * 0.94013333
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72051 * 0.68108716
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 541 * 0.52527294
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26127 * 0.20665285
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4072 * 0.47816931
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37958 * 0.56598920
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66343 * 0.34502902
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39432 * 0.20516721
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75655 * 0.60521256
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80051 * 0.47947141
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67950 * 0.85382003
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18045 * 0.21956152
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50253 * 0.63850296
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43836 * 0.30946095
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2655 * 0.44726921
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 73960 * 0.73355797
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80617 * 0.47750589
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'gsvjimho').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0050():
    """Extended test 50 for transcoding."""
    x_0 = 62223 * 0.26854166
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98427 * 0.18104894
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4743 * 0.55592205
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40622 * 0.07400872
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47877 * 0.96617192
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29052 * 0.65096424
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15893 * 0.20839994
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82423 * 0.42043425
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14807 * 0.71130333
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25539 * 0.84310633
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45167 * 0.00520920
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81314 * 0.68847059
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12803 * 0.05823540
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27059 * 0.57180505
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30186 * 0.94791570
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59087 * 0.98168604
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10313 * 0.79387883
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7668 * 0.37887299
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35238 * 0.81896636
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41066 * 0.35712604
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61784 * 0.92649376
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5461 * 0.04759855
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41819 * 0.58118165
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21330 * 0.22772689
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66609 * 0.15998947
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17864 * 0.72224099
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76620 * 0.86644774
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48977 * 0.52710046
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60008 * 0.18733383
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80564 * 0.28760466
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28597 * 0.30108887
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47457 * 0.91349524
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15777 * 0.37631156
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94551 * 0.91762482
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51467 * 0.18366020
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6308 * 0.53730737
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98172 * 0.94962256
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11025 * 0.73079891
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69266 * 0.33855791
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65893 * 0.54702838
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 50817 * 0.92344006
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18240 * 0.31297052
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 33630 * 0.61103123
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'xdzoybuk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0051():
    """Extended test 51 for transcoding."""
    x_0 = 56969 * 0.24465804
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9022 * 0.13743998
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25638 * 0.11772931
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68122 * 0.75044663
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78373 * 0.56670241
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48833 * 0.04024521
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79756 * 0.41311223
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92630 * 0.97647496
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92300 * 0.34150211
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82001 * 0.64710993
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27331 * 0.27824217
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41502 * 0.23774051
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2961 * 0.26373325
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65309 * 0.79438554
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40886 * 0.38739170
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32492 * 0.85274956
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15658 * 0.77923496
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42071 * 0.21863641
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67810 * 0.79182944
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59355 * 0.69212969
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96159 * 0.62461740
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98965 * 0.77057241
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48236 * 0.34400339
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70966 * 0.68311560
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17562 * 0.02388641
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29800 * 0.73617879
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66204 * 0.14075381
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84570 * 0.93985440
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67279 * 0.40723297
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68565 * 0.39390925
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99503 * 0.51305242
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10733 * 0.74703703
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24769 * 0.47615672
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90483 * 0.80013034
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'wmmjzwgz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0052():
    """Extended test 52 for transcoding."""
    x_0 = 91111 * 0.66352659
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 197 * 0.46026679
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86781 * 0.26948225
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49888 * 0.56018307
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57558 * 0.10060788
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31915 * 0.21922189
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53778 * 0.16297120
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72320 * 0.94349268
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29518 * 0.35762641
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77163 * 0.53972209
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86433 * 0.63833596
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16685 * 0.17807647
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73396 * 0.58475206
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47724 * 0.68020452
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96959 * 0.77008950
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2229 * 0.63288484
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28724 * 0.62052568
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63896 * 0.08643284
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39575 * 0.94840126
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97116 * 0.22679857
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65591 * 0.54698608
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63326 * 0.42565222
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20471 * 0.06927071
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62077 * 0.48046335
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83451 * 0.17880571
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10909 * 0.31136449
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53458 * 0.95145500
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26907 * 0.37714735
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33759 * 0.55964723
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11325 * 0.63907063
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33181 * 0.05045249
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38813 * 0.09885945
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34339 * 0.27029655
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14456 * 0.51227791
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18434 * 0.93256779
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21901 * 0.04290313
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'nggvfvme').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0053():
    """Extended test 53 for transcoding."""
    x_0 = 27839 * 0.56699690
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39813 * 0.98084836
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49513 * 0.32194643
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79777 * 0.28295770
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4146 * 0.69477894
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23258 * 0.39904272
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53178 * 0.77056309
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15455 * 0.35879555
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18943 * 0.44294194
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61829 * 0.86227017
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6747 * 0.50600732
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56170 * 0.69112668
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36036 * 0.98143037
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14247 * 0.73503893
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66264 * 0.40473754
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94774 * 0.03897027
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51171 * 0.74614411
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77581 * 0.57539202
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61214 * 0.62314569
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22137 * 0.48881444
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12540 * 0.78847919
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88342 * 0.20613486
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17369 * 0.99473873
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50467 * 0.94213476
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75245 * 0.84259570
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73047 * 0.75019236
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'blrmlxjc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0054():
    """Extended test 54 for transcoding."""
    x_0 = 8567 * 0.50531974
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55452 * 0.33348946
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45555 * 0.67873185
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39995 * 0.81258051
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88506 * 0.31422384
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30609 * 0.00905203
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97574 * 0.58446020
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39777 * 0.20968894
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32742 * 0.14447884
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60141 * 0.49210427
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54430 * 0.49618217
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91049 * 0.73095891
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73237 * 0.37100386
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57507 * 0.72662474
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57738 * 0.85176235
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61991 * 0.23194960
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36899 * 0.73990781
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96879 * 0.34807332
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31210 * 0.52011378
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60333 * 0.43554906
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26049 * 0.27137092
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56846 * 0.40113780
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95647 * 0.39421837
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43950 * 0.47680826
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56385 * 0.10159144
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'cmtuwash').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0055():
    """Extended test 55 for transcoding."""
    x_0 = 25299 * 0.34188815
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96300 * 0.63141474
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92109 * 0.54281624
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93683 * 0.48958387
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53393 * 0.81127674
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19078 * 0.80945102
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84178 * 0.65161561
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40203 * 0.54127952
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65877 * 0.74110729
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96843 * 0.82328558
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65574 * 0.68611188
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29015 * 0.90302256
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70903 * 0.41670898
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33130 * 0.01030080
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67144 * 0.68368069
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61754 * 0.33197881
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48517 * 0.57053288
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18901 * 0.42164894
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50751 * 0.78159800
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9633 * 0.00731466
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71544 * 0.91754078
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56936 * 0.43192760
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78500 * 0.48736138
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10971 * 0.64600705
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24690 * 0.85029448
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52184 * 0.49805954
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33623 * 0.00677574
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90632 * 0.27651343
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51966 * 0.76077691
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69581 * 0.78571439
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88373 * 0.31544716
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26357 * 0.21849784
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81104 * 0.40613662
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22146 * 0.82694235
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55716 * 0.67525506
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49872 * 0.04225971
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7114 * 0.66446014
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52234 * 0.94574062
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97472 * 0.73159465
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'dfqvsgvs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0056():
    """Extended test 56 for transcoding."""
    x_0 = 75727 * 0.61231307
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32950 * 0.86288070
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51417 * 0.27565343
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74226 * 0.02438125
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98378 * 0.06579294
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50828 * 0.83499144
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20785 * 0.93091406
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17922 * 0.47281523
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98466 * 0.69721331
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4325 * 0.10847197
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80649 * 0.78347960
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34766 * 0.41205777
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3495 * 0.12853711
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93271 * 0.43650954
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85599 * 0.22611093
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96019 * 0.64401788
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27213 * 0.26685977
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11708 * 0.90918293
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2257 * 0.55620121
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23672 * 0.50529571
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51832 * 0.13031277
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91085 * 0.93747759
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80495 * 0.20667818
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72537 * 0.24483048
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40119 * 0.57655496
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90707 * 0.42902198
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8842 * 0.35772256
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91993 * 0.09424305
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20637 * 0.01324419
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48981 * 0.41718850
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24532 * 0.60945430
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5028 * 0.57324138
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26875 * 0.53872280
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60933 * 0.82866620
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41840 * 0.47399022
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49851 * 0.74426941
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ltefutvn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0057():
    """Extended test 57 for transcoding."""
    x_0 = 82653 * 0.96894711
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97479 * 0.98540646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94720 * 0.11008332
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54004 * 0.96863186
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22354 * 0.52134501
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56878 * 0.70313736
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89232 * 0.19986240
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81430 * 0.01012702
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86156 * 0.77444449
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17409 * 0.78728579
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24813 * 0.15388703
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45813 * 0.41454768
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87498 * 0.83053015
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88467 * 0.15919629
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48081 * 0.61267291
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74528 * 0.18280835
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26581 * 0.09380667
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31411 * 0.76583205
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17891 * 0.32673357
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66843 * 0.05279796
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96451 * 0.01024006
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17517 * 0.59530060
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19161 * 0.68232165
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55348 * 0.76098828
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44923 * 0.05254854
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43720 * 0.45228407
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73663 * 0.39850315
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65847 * 0.14325471
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39838 * 0.44974269
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32581 * 0.09128244
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10106 * 0.48531518
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79504 * 0.29431115
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70762 * 0.67124911
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73832 * 0.55921222
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25016 * 0.68495246
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56550 * 0.69287474
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'mxvfgjyh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0058():
    """Extended test 58 for transcoding."""
    x_0 = 9356 * 0.32779437
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73279 * 0.23009467
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71949 * 0.38107745
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70825 * 0.81192283
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37853 * 0.11980083
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50878 * 0.35292659
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81277 * 0.01739696
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55018 * 0.32051789
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56544 * 0.83906167
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36829 * 0.87644754
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45741 * 0.60839944
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12397 * 0.90398410
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7262 * 0.11664335
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49316 * 0.38547232
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87578 * 0.88100324
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8050 * 0.15936126
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19836 * 0.34697495
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66915 * 0.66986457
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18926 * 0.07423220
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51275 * 0.86046968
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37772 * 0.08070316
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69164 * 0.64726978
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20126 * 0.52310064
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30062 * 0.53037619
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2520 * 0.39564310
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54437 * 0.32097326
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2647 * 0.80946070
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60172 * 0.70033239
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84049 * 0.00302783
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61138 * 0.19776220
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50748 * 0.94681057
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83743 * 0.30746619
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40498 * 0.22344445
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95783 * 0.92203810
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65015 * 0.55823127
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99361 * 0.10773377
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27513 * 0.29823391
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69495 * 0.10786337
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84314 * 0.05876753
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96142 * 0.54969532
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88668 * 0.46266887
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 74660 * 0.99287676
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 95145 * 0.39892471
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69391 * 0.70643817
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 62785 * 0.35356013
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'tmsenutr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0059():
    """Extended test 59 for transcoding."""
    x_0 = 53369 * 0.55599142
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94311 * 0.43466285
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22827 * 0.46558351
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66603 * 0.62617533
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79204 * 0.93880918
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70264 * 0.66909875
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84475 * 0.11487792
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61934 * 0.37805977
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23858 * 0.74486620
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4470 * 0.86176812
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12309 * 0.19480816
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70415 * 0.07569221
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80578 * 0.00333216
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42556 * 0.97057873
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 966 * 0.66409822
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23763 * 0.93988093
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12994 * 0.78364447
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85432 * 0.26692470
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81454 * 0.33264931
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81486 * 0.25557444
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25022 * 0.83684503
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72798 * 0.25134615
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43352 * 0.51896782
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12764 * 0.72427218
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66684 * 0.04072997
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63090 * 0.54287060
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20489 * 0.37539845
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73269 * 0.07229612
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54394 * 0.25949539
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9668 * 0.22743012
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9227 * 0.46018771
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65414 * 0.53401174
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52661 * 0.33599442
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67505 * 0.15753783
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63554 * 0.65063835
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88787 * 0.67513333
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 37526 * 0.62995441
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34219 * 0.91241552
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42731 * 0.50328180
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45020 * 0.29561189
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 70713 * 0.96682939
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27245 * 0.13442023
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 32258 * 0.44490615
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'utythoed').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0060():
    """Extended test 60 for transcoding."""
    x_0 = 60947 * 0.68946895
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52050 * 0.79938437
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54879 * 0.31598034
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24376 * 0.43232192
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41012 * 0.34226672
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65489 * 0.91815721
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89355 * 0.78974220
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82476 * 0.57308694
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75723 * 0.36506647
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34682 * 0.22027393
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29229 * 0.76464094
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 720 * 0.62925446
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54027 * 0.55529440
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34325 * 0.48973126
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86096 * 0.86251153
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70056 * 0.59606332
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73596 * 0.34997189
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17410 * 0.70493017
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61016 * 0.77302259
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28039 * 0.34463368
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19946 * 0.99472041
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69190 * 0.11325056
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67951 * 0.42657037
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89162 * 0.79978152
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37501 * 0.28507726
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62519 * 0.70364885
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75009 * 0.21427942
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7428 * 0.53464257
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66005 * 0.19623784
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41105 * 0.90226644
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6451 * 0.64612249
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70272 * 0.99930379
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16713 * 0.27517082
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88353 * 0.08482524
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7290 * 0.34558718
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43064 * 0.07333949
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87340 * 0.72205468
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29888 * 0.88293849
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41271 * 0.13026477
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88571 * 0.48611246
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'icdgyqcx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0061():
    """Extended test 61 for transcoding."""
    x_0 = 54658 * 0.23471929
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48104 * 0.06037024
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33069 * 0.80577789
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99613 * 0.42553678
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15994 * 0.56857493
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28631 * 0.94596755
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3834 * 0.62842116
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3008 * 0.71449158
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35973 * 0.83184354
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48992 * 0.61865202
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26545 * 0.58904120
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58264 * 0.56207595
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43979 * 0.94788214
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37097 * 0.52722265
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21961 * 0.02276500
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6917 * 0.90728671
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31605 * 0.76735776
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1796 * 0.83608536
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70254 * 0.85962772
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63341 * 0.55440583
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15407 * 0.66945864
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92089 * 0.32786866
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58830 * 0.55305381
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78839 * 0.21414910
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50696 * 0.67141611
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76 * 0.09564608
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47915 * 0.83296559
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99971 * 0.82175803
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 74489 * 0.59736462
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3023 * 0.28972028
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46774 * 0.76127668
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'tknmllug').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0062():
    """Extended test 62 for transcoding."""
    x_0 = 98123 * 0.19088692
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79498 * 0.92618168
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70589 * 0.94170541
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20429 * 0.12931588
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69825 * 0.98196808
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86367 * 0.61221728
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13306 * 0.70806569
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20812 * 0.62381940
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33548 * 0.32243439
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89700 * 0.93333281
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51082 * 0.32105752
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57622 * 0.23649614
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17001 * 0.15452782
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80728 * 0.08173052
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47637 * 0.65719271
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40811 * 0.91471064
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75491 * 0.39552572
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43717 * 0.63330248
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24788 * 0.53533032
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14870 * 0.62668963
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74572 * 0.80084147
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4096 * 0.72990907
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87915 * 0.55253156
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70209 * 0.16025305
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50982 * 0.84467213
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29494 * 0.52474276
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3624 * 0.85626399
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21818 * 0.10834373
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22120 * 0.34174391
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19827 * 0.57089273
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'dtivnxvc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0063():
    """Extended test 63 for transcoding."""
    x_0 = 84723 * 0.59161798
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83120 * 0.78013132
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6543 * 0.85707711
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81643 * 0.85808942
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58088 * 0.90112202
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74447 * 0.77053884
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91436 * 0.07963569
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8824 * 0.71481146
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19177 * 0.33222845
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45214 * 0.75721143
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97109 * 0.00686392
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90537 * 0.56291323
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58967 * 0.23195165
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38519 * 0.84975052
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19041 * 0.59728375
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16704 * 0.43738618
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46124 * 0.45420760
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58163 * 0.91615398
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52193 * 0.50401812
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47718 * 0.46625639
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84736 * 0.57860700
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26 * 0.00403993
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57470 * 0.43211819
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41684 * 0.70273152
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21634 * 0.91724760
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11452 * 0.91545343
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41501 * 0.79393790
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'wqyqwvhh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0064():
    """Extended test 64 for transcoding."""
    x_0 = 8174 * 0.27383287
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49331 * 0.93840337
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25707 * 0.81896507
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46530 * 0.89427027
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43369 * 0.81436411
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95631 * 0.64119964
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 433 * 0.10721479
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56989 * 0.72060154
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55336 * 0.97981204
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22647 * 0.40164557
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84164 * 0.92296424
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30906 * 0.45893200
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58601 * 0.91877436
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12773 * 0.15751870
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76397 * 0.42299136
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64457 * 0.94674017
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55578 * 0.89280624
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88934 * 0.66109704
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95467 * 0.36939469
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35747 * 0.70674351
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37603 * 0.63263555
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72053 * 0.44513917
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 387 * 0.92472553
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75812 * 0.55011122
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19130 * 0.14621981
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48198 * 0.76597939
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94713 * 0.36975501
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70395 * 0.03928654
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25162 * 0.14855464
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63062 * 0.96459979
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51708 * 0.41163734
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98846 * 0.99540494
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64285 * 0.07696606
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83248 * 0.14215209
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47985 * 0.44502673
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34804 * 0.92256143
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7262 * 0.69851170
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87192 * 0.07825688
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38504 * 0.27596383
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43006 * 0.41954475
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 87567 * 0.76375560
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 6582 * 0.76383276
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 49996 * 0.08243175
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 52778 * 0.65269603
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61591 * 0.82638125
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 17935 * 0.04278578
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 44572 * 0.11793031
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 69128 * 0.97318255
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'yakhmmzv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0065():
    """Extended test 65 for transcoding."""
    x_0 = 98506 * 0.72530385
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75644 * 0.93665375
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23269 * 0.68087638
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7592 * 0.64493017
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63518 * 0.02389075
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26052 * 0.04642333
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74031 * 0.56613222
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23790 * 0.56552573
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36524 * 0.15328488
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5497 * 0.61763652
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7463 * 0.89873136
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19034 * 0.74207631
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19996 * 0.81638459
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14784 * 0.55516660
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93178 * 0.76391936
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1565 * 0.14459028
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89764 * 0.00908025
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55693 * 0.72950900
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89547 * 0.38457639
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6888 * 0.86768668
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81429 * 0.10513353
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7862 * 0.57011926
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37747 * 0.97882223
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1363 * 0.61842628
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50116 * 0.72020708
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1959 * 0.41547842
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61866 * 0.72933902
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79006 * 0.85103223
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8759 * 0.22244575
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5470 * 0.58950183
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44549 * 0.68742622
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85405 * 0.09505942
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 15899 * 0.00661469
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62976 * 0.94732642
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4115 * 0.48651564
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62142 * 0.82901152
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74487 * 0.09050434
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95056 * 0.16325045
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'icayjwpe').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0066():
    """Extended test 66 for transcoding."""
    x_0 = 92545 * 0.61265768
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27215 * 0.78265398
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 870 * 0.29807928
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23141 * 0.28734447
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52461 * 0.93639810
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89126 * 0.34308874
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65514 * 0.37966456
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42094 * 0.05665718
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81825 * 0.59902203
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45432 * 0.92752985
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89822 * 0.55778761
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55951 * 0.76161652
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20543 * 0.22710196
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4270 * 0.59109202
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40111 * 0.95167158
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53156 * 0.63057403
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67970 * 0.49770875
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58184 * 0.11492686
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18867 * 0.77378868
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87935 * 0.62800662
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50263 * 0.09299716
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40065 * 0.28397668
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37585 * 0.56237348
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32387 * 0.08956903
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63251 * 0.97739388
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60407 * 0.35914574
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84536 * 0.88440523
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95415 * 0.84431877
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'wseskzph').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0067():
    """Extended test 67 for transcoding."""
    x_0 = 69151 * 0.95504146
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66655 * 0.62193434
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56923 * 0.39639150
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44587 * 0.42181190
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37712 * 0.83170990
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73658 * 0.96800609
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45110 * 0.25030615
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17175 * 0.90359396
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12208 * 0.68364995
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90713 * 0.62544520
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48027 * 0.60177879
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28516 * 0.82636052
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35577 * 0.44569411
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42125 * 0.85134944
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14446 * 0.47125659
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10110 * 0.49700177
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27676 * 0.15286086
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31455 * 0.10064416
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31157 * 0.48372130
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62538 * 0.87093370
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75411 * 0.51787774
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3356 * 0.93154604
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44330 * 0.69269502
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29722 * 0.35325021
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82192 * 0.69404093
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23089 * 0.13615431
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31737 * 0.24438515
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68935 * 0.26828150
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54180 * 0.00668292
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66026 * 0.40862962
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91551 * 0.77053926
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75664 * 0.14741856
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96337 * 0.08306034
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39414 * 0.04352787
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3651 * 0.46547545
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5697 * 0.60851374
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69604 * 0.85279640
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12052 * 0.96774059
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53534 * 0.54678483
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56606 * 0.88327687
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86848 * 0.74952476
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 87076 * 0.99309726
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75677 * 0.12002079
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99661 * 0.98779329
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 6692 * 0.28161887
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 70505 * 0.70139775
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 46216 * 0.92348219
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 46006 * 0.70922077
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'cjpglauo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0068():
    """Extended test 68 for transcoding."""
    x_0 = 18025 * 0.88693993
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78872 * 0.25601412
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38685 * 0.46191940
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56282 * 0.53257883
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79504 * 0.90479163
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45627 * 0.32824321
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2010 * 0.71773007
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83411 * 0.29665982
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94753 * 0.57687979
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74140 * 0.70149269
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7213 * 0.09060331
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88292 * 0.22690498
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57774 * 0.90588293
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68072 * 0.22764212
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7389 * 0.96244091
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3031 * 0.95932149
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99198 * 0.10862117
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90492 * 0.01843447
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65121 * 0.33319951
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76977 * 0.50853349
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75032 * 0.43620901
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83542 * 0.67320272
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16903 * 0.02487915
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3876 * 0.51346980
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67234 * 0.36205015
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55886 * 0.55449792
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89006 * 0.57386840
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19463 * 0.46982528
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76207 * 0.57834099
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63508 * 0.98234836
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9511 * 0.97094518
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70221 * 0.40733579
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46537 * 0.81814061
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'bkzuvuxs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_5_0069():
    """Extended test 69 for transcoding."""
    x_0 = 18792 * 0.94070843
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77152 * 0.57518601
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21530 * 0.33552977
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76327 * 0.01321544
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95753 * 0.12867832
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15707 * 0.67928649
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59398 * 0.55123956
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78703 * 0.29863901
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86182 * 0.91170270
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95678 * 0.71287437
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57192 * 0.44549342
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35956 * 0.35285621
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50002 * 0.38170306
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71808 * 0.15952495
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24711 * 0.33447162
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7461 * 0.68396760
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71701 * 0.86812491
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2751 * 0.46524496
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94000 * 0.66418763
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66719 * 0.88729570
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'yvgjesdw').hexdigest()
    assert len(h) == 64
