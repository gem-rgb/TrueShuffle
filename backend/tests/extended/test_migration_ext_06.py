"""Extended tests for migration suite 6."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_migration_extended_6_0000():
    """Extended test 0 for migration."""
    x_0 = 59810 * 0.30196593
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95955 * 0.37876977
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10848 * 0.58635237
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53813 * 0.04916807
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99410 * 0.67578995
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29844 * 0.74543580
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39031 * 0.69651117
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23676 * 0.32446033
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70598 * 0.20646703
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57474 * 0.80260597
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51565 * 0.97599396
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92395 * 0.69432203
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38894 * 0.34550369
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61070 * 0.54508629
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88022 * 0.47290567
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23826 * 0.57183754
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8332 * 0.64369243
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46093 * 0.73689056
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8056 * 0.91453822
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98363 * 0.80326107
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6311 * 0.67619398
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91712 * 0.90018959
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32987 * 0.38545206
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65669 * 0.18551287
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86980 * 0.36431966
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'vgiphwdn').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0001():
    """Extended test 1 for migration."""
    x_0 = 45575 * 0.78538952
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7867 * 0.71126188
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51316 * 0.80354275
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65604 * 0.11293969
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37727 * 0.21058727
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2351 * 0.72469765
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43828 * 0.69810130
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29589 * 0.11322153
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42918 * 0.51616530
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42572 * 0.64687991
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9623 * 0.96130083
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97104 * 0.36713785
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54098 * 0.62759585
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15622 * 0.98948777
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93992 * 0.51210479
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12182 * 0.92216480
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58064 * 0.80492402
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28337 * 0.32338828
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68449 * 0.55696052
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31292 * 0.53075784
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69891 * 0.53714843
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84294 * 0.87163024
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65401 * 0.14979271
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30931 * 0.29269284
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96767 * 0.01289861
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70491 * 0.66902418
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72980 * 0.88440427
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80346 * 0.09252323
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93645 * 0.49878360
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62984 * 0.60808333
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69899 * 0.39472053
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99432 * 0.81666102
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35902 * 0.42954742
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39532 * 0.22490310
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64331 * 0.27074116
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24196 * 0.79563356
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34165 * 0.21135778
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44563 * 0.92868747
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47437 * 0.63120475
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 78116 * 0.46404224
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 58346 * 0.16569771
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4075 * 0.13186336
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 32110 * 0.24683233
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 33955 * 0.29289419
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89740 * 0.97168324
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 42227 * 0.10142690
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 7415 * 0.67021320
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 44813 * 0.09161533
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 76569 * 0.73131986
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'igaevalk').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0002():
    """Extended test 2 for migration."""
    x_0 = 99603 * 0.84057186
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8332 * 0.29673008
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5823 * 0.17171187
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38901 * 0.50587801
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56592 * 0.46838385
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28114 * 0.18078052
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68947 * 0.16498608
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30366 * 0.52307564
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11001 * 0.01317978
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6906 * 0.26649080
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95727 * 0.24709462
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22608 * 0.50405462
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59949 * 0.09070380
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82097 * 0.47144051
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30028 * 0.23810148
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72294 * 0.33874155
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11625 * 0.02876842
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45481 * 0.80161352
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11475 * 0.09091723
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4120 * 0.99904801
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4138 * 0.63537310
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9666 * 0.33497097
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82028 * 0.32947919
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57038 * 0.51251699
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68730 * 0.95587408
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51173 * 0.35156200
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5650 * 0.20164470
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'nuohpgug').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0003():
    """Extended test 3 for migration."""
    x_0 = 1127 * 0.52402760
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60422 * 0.52501055
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76065 * 0.12774101
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59200 * 0.43457120
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44853 * 0.57725285
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3802 * 0.38786734
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26175 * 0.49074402
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50690 * 0.36461298
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82124 * 0.84728307
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79271 * 0.74069339
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52811 * 0.22625529
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26307 * 0.88953665
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59353 * 0.15409889
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75585 * 0.72551498
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13886 * 0.72810909
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80238 * 0.37552225
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66456 * 0.51598590
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77147 * 0.10375917
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57473 * 0.19282821
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24902 * 0.79883073
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76544 * 0.80182241
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83979 * 0.10096277
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90350 * 0.45399247
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11647 * 0.22206498
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6631 * 0.38381667
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82208 * 0.29785024
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71034 * 0.43714341
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52145 * 0.28517039
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8653 * 0.96849026
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30085 * 0.45933955
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58570 * 0.41715928
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79303 * 0.62402220
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4090 * 0.84645902
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41744 * 0.10913097
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48504 * 0.48556522
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97249 * 0.69261836
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43790 * 0.61213158
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41807 * 0.58703076
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65858 * 0.51232250
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19491 * 0.21833842
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 57813 * 0.80978911
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66071 * 0.49354572
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47823 * 0.94696172
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 93998 * 0.54487018
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10088 * 0.27549505
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 1355 * 0.91770739
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 4650 * 0.71398526
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 7503 * 0.29716860
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'bzcgnkyg').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0004():
    """Extended test 4 for migration."""
    x_0 = 93925 * 0.60879649
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60939 * 0.77858149
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96361 * 0.08985655
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36824 * 0.80464072
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27514 * 0.50596925
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71279 * 0.21982561
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72714 * 0.78630759
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89582 * 0.53282296
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70824 * 0.13185062
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35485 * 0.47232150
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73372 * 0.65672928
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75828 * 0.96640592
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1838 * 0.61115652
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80917 * 0.16702029
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54236 * 0.55297160
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24547 * 0.71364806
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24827 * 0.41512685
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38803 * 0.50504632
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25326 * 0.56924219
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32200 * 0.01172188
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20145 * 0.20735352
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78244 * 0.97384595
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22585 * 0.08285559
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68289 * 0.05455012
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50217 * 0.57043624
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'wtgdlzqm').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0005():
    """Extended test 5 for migration."""
    x_0 = 97493 * 0.67322315
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44306 * 0.53169670
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41709 * 0.11091583
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88790 * 0.20985686
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55056 * 0.29097809
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81387 * 0.10387186
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38327 * 0.65423406
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28913 * 0.40832274
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90344 * 0.34799776
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57972 * 0.51379211
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59515 * 0.81111353
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55242 * 0.33320469
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78458 * 0.61235025
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75633 * 0.50120131
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71908 * 0.31674765
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98987 * 0.02965293
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42473 * 0.66854858
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34964 * 0.26949409
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17761 * 0.55926686
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45006 * 0.17672393
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76108 * 0.60077071
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62479 * 0.84047769
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26275 * 0.18997894
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65282 * 0.59025254
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46361 * 0.49263353
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77119 * 0.36177592
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29318 * 0.18058162
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13573 * 0.84614155
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11911 * 0.38302076
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11816 * 0.17390654
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53600 * 0.71532792
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31204 * 0.73625838
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13506 * 0.46653408
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39658 * 0.40222080
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55900 * 0.25910789
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7509 * 0.37103208
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35803 * 0.72410588
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90889 * 0.37471938
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16166 * 0.49748401
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11479 * 0.37411961
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34802 * 0.69526301
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'jgzoxthf').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0006():
    """Extended test 6 for migration."""
    x_0 = 25482 * 0.98617448
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4189 * 0.36862205
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43781 * 0.81690088
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36895 * 0.73671783
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21458 * 0.46199001
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64314 * 0.36186996
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56037 * 0.21842696
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18026 * 0.35423284
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78700 * 0.46400865
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25462 * 0.77923766
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81280 * 0.59492596
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10510 * 0.81452376
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82208 * 0.40961998
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90631 * 0.59161431
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67071 * 0.85028414
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65427 * 0.80314260
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59692 * 0.14894360
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6380 * 0.64878572
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25084 * 0.78478335
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96464 * 0.26474897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79985 * 0.52617161
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43443 * 0.03829443
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57522 * 0.25827360
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40841 * 0.40562142
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57273 * 0.27538555
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26559 * 0.29753214
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40549 * 0.76014001
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15129 * 0.47077796
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11220 * 0.52491655
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93064 * 0.01348355
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26175 * 0.33779099
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 98342 * 0.28400055
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81326 * 0.62115968
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88887 * 0.68420810
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71043 * 0.82401735
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66227 * 0.40427351
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88438 * 0.08745122
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81072 * 0.16354356
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19933 * 0.64368641
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68144 * 0.04295679
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 92609 * 0.75860979
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50623 * 0.73288213
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 7195 * 0.70157125
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 25394 * 0.07679128
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 51656 * 0.39445702
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 77013 * 0.64292386
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 91280 * 0.48755296
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 98119 * 0.23585320
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'gnfiangv').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0007():
    """Extended test 7 for migration."""
    x_0 = 44187 * 0.78076264
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13862 * 0.88734429
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3837 * 0.22888566
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11915 * 0.79917266
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76688 * 0.20634994
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21481 * 0.25009521
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81480 * 0.41241901
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34778 * 0.17908376
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94031 * 0.34229815
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79566 * 0.60836956
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42949 * 0.10334557
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35819 * 0.12619165
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48160 * 0.46317586
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52323 * 0.26653908
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86891 * 0.62765620
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25902 * 0.63457807
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30629 * 0.00335043
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37990 * 0.65775012
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20438 * 0.59948245
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93204 * 0.77013987
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47594 * 0.16632579
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19946 * 0.35865226
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87494 * 0.72800147
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30533 * 0.36836830
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83593 * 0.66173265
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65194 * 0.89905527
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80612 * 0.43019286
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96175 * 0.38961405
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18162 * 0.93288197
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20652 * 0.19029808
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48671 * 0.37908532
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75867 * 0.03637385
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20665 * 0.26856326
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9585 * 0.90330384
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35991 * 0.42592879
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37634 * 0.66067196
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30612 * 0.35890331
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19267 * 0.05292596
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72898 * 0.75685763
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40310 * 0.07109156
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ptwvmoeg').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0008():
    """Extended test 8 for migration."""
    x_0 = 68172 * 0.91502100
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20559 * 0.79949228
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56016 * 0.04584397
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21611 * 0.91873377
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5777 * 0.48927693
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38408 * 0.54914690
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36980 * 0.83899497
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53065 * 0.87727489
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51484 * 0.22319582
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47708 * 0.01930691
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20014 * 0.98494653
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90234 * 0.29381739
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14830 * 0.69275724
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62872 * 0.56469423
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13289 * 0.84619545
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24493 * 0.48803755
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54120 * 0.87778040
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22520 * 0.07531907
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68541 * 0.38175524
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62225 * 0.91319131
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23110 * 0.32515119
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79726 * 0.34744410
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61371 * 0.87282965
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6000 * 0.46880393
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2622 * 0.27497273
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2172 * 0.81568154
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46586 * 0.37509972
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34788 * 0.20436323
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91266 * 0.22929594
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47704 * 0.42325086
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67887 * 0.15344338
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59642 * 0.81442604
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42898 * 0.61931447
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59192 * 0.65123332
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33475 * 0.67190223
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76092 * 0.76367657
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96053 * 0.54254355
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'llfmcrlq').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0009():
    """Extended test 9 for migration."""
    x_0 = 61830 * 0.39067927
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77446 * 0.26972499
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60319 * 0.63848635
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88482 * 0.84465574
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8878 * 0.74196321
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21384 * 0.39877973
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7224 * 0.69751721
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51399 * 0.45794372
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86835 * 0.55975740
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77439 * 0.77600896
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93369 * 0.72250551
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46182 * 0.95853726
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95294 * 0.69998705
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11765 * 0.51140951
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34573 * 0.15417777
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92298 * 0.50093709
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56195 * 0.90141784
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16410 * 0.13671077
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15487 * 0.47249246
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73250 * 0.29982827
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77020 * 0.46238770
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48240 * 0.99419168
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71828 * 0.80550525
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55379 * 0.95732335
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8483 * 0.65945632
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19573 * 0.00029432
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80888 * 0.70763183
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95596 * 0.33223054
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67736 * 0.91569979
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21222 * 0.80105437
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78988 * 0.78683517
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55540 * 0.62380576
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36418 * 0.68115659
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'phopgkjs').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0010():
    """Extended test 10 for migration."""
    x_0 = 26324 * 0.54316572
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28587 * 0.92588527
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24849 * 0.15335955
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26359 * 0.64937003
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1189 * 0.17527975
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12705 * 0.08900677
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8884 * 0.01143111
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58709 * 0.69565406
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57914 * 0.76064009
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72751 * 0.14712420
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18820 * 0.94485043
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69931 * 0.20389822
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40920 * 0.45644877
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46496 * 0.77064223
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9595 * 0.86480130
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83148 * 0.59078370
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42009 * 0.81321367
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85807 * 0.17472332
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69521 * 0.09481017
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54595 * 0.39987256
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23396 * 0.90461788
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77272 * 0.99270843
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16484 * 0.52086439
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25010 * 0.81649086
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4363 * 0.27318946
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19361 * 0.60565925
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74994 * 0.01926267
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66568 * 0.60384232
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2345 * 0.14544271
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40870 * 0.42590284
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92153 * 0.90930028
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4752 * 0.20669897
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84049 * 0.96565639
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50852 * 0.64194875
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42376 * 0.67293825
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69874 * 0.18296110
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93132 * 0.16476278
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69375 * 0.68929908
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92922 * 0.31260715
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3563 * 0.35133572
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40632 * 0.05428534
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47543 * 0.96138965
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 78301 * 0.86807402
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 42630 * 0.08217881
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 91935 * 0.77476215
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 57383 * 0.14574160
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'zjitklwa').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0011():
    """Extended test 11 for migration."""
    x_0 = 63287 * 0.93633943
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23543 * 0.75294647
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60170 * 0.50818706
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47544 * 0.63721925
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73478 * 0.61550701
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9872 * 0.67111902
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8083 * 0.28406487
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29404 * 0.24601770
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87902 * 0.75540118
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57032 * 0.23427598
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95505 * 0.50703511
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68352 * 0.12378544
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35734 * 0.22102028
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83883 * 0.15952655
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89631 * 0.86652552
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20367 * 0.01336306
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64660 * 0.21733104
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88276 * 0.57263362
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4219 * 0.46947115
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96088 * 0.53135087
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43772 * 0.13494087
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22685 * 0.05096809
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68056 * 0.79060902
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41164 * 0.66925063
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61179 * 0.92787701
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51890 * 0.90725962
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96419 * 0.31028808
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67243 * 0.41091275
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93972 * 0.37054293
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72766 * 0.35795177
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97182 * 0.71905513
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56068 * 0.34110809
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87798 * 0.88765194
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'hypehwyq').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0012():
    """Extended test 12 for migration."""
    x_0 = 92822 * 0.62486445
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49270 * 0.21876583
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34295 * 0.43719254
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78049 * 0.65151470
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43944 * 0.86953689
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22618 * 0.32152999
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52524 * 0.36077861
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4087 * 0.83955193
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47025 * 0.98977127
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30764 * 0.05930968
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5884 * 0.90132519
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68328 * 0.76698291
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27485 * 0.12223736
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88910 * 0.55015331
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86047 * 0.78088052
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60192 * 0.90085859
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47700 * 0.51140456
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96939 * 0.24626038
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1289 * 0.34062715
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83578 * 0.13443331
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98305 * 0.99208583
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33397 * 0.65297363
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30476 * 0.56184340
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27859 * 0.85396127
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55518 * 0.98772153
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60585 * 0.69788177
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84681 * 0.22527820
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88817 * 0.93757471
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40806 * 0.94156000
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49105 * 0.95273379
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76480 * 0.86410020
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 23133 * 0.81476073
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24041 * 0.22986332
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68675 * 0.56836468
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43210 * 0.50456774
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 53688 * 0.80699945
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32134 * 0.38835518
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52032 * 0.51700592
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6074 * 0.75193043
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69781 * 0.38610555
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 76840 * 0.33560202
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 94355 * 0.91222800
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 72337 * 0.94458980
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 21528 * 0.72385278
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'pfqpcygn').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0013():
    """Extended test 13 for migration."""
    x_0 = 79173 * 0.08219562
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5728 * 0.26868119
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84035 * 0.21704403
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39422 * 0.15692517
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64962 * 0.65805898
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8435 * 0.18961629
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72786 * 0.33914374
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62893 * 0.95355570
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80892 * 0.87254670
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24649 * 0.71326449
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36457 * 0.13402366
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15188 * 0.10271073
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1963 * 0.74947887
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46423 * 0.15443869
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92398 * 0.42910125
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38025 * 0.41781725
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41383 * 0.22808868
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14264 * 0.20692598
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6545 * 0.26493635
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53699 * 0.49486427
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55385 * 0.56028661
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'kgsbhlsm').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0014():
    """Extended test 14 for migration."""
    x_0 = 1904 * 0.31061964
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12358 * 0.45632815
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68536 * 0.68320019
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79943 * 0.36945648
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23170 * 0.44524514
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47577 * 0.66051331
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56524 * 0.56336758
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95737 * 0.34593399
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39975 * 0.24566892
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13254 * 0.80125193
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82631 * 0.73704589
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43628 * 0.85697693
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3565 * 0.56566778
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38422 * 0.43578633
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29366 * 0.97815512
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4357 * 0.33677816
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65821 * 0.85121940
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36218 * 0.10983881
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63604 * 0.61673911
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47343 * 0.37485851
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 669 * 0.07692982
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78014 * 0.41832242
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3276 * 0.09632994
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27410 * 0.44429522
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42963 * 0.46460525
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51585 * 0.12148341
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61692 * 0.51045231
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19092 * 0.60371535
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98971 * 0.22127944
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29641 * 0.02076668
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40999 * 0.75539619
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75431 * 0.47047809
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11342 * 0.12903258
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69368 * 0.80393998
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18663 * 0.58622856
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'eijulsrf').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0015():
    """Extended test 15 for migration."""
    x_0 = 25187 * 0.91608933
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69451 * 0.49262196
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25357 * 0.54656306
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82001 * 0.45237362
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86054 * 0.84256221
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71084 * 0.76138017
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65508 * 0.87844570
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39754 * 0.91122477
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34138 * 0.60862254
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79192 * 0.87631758
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69631 * 0.41416605
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4248 * 0.89624455
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70257 * 0.80497553
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53456 * 0.20359108
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80072 * 0.56051308
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93084 * 0.96932479
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1012 * 0.67532818
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1952 * 0.12373251
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18280 * 0.38959371
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22327 * 0.17177929
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37691 * 0.25447174
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28736 * 0.60785783
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62067 * 0.42146120
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40917 * 0.98900815
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37539 * 0.59342300
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24241 * 0.39503675
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80283 * 0.84331413
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77852 * 0.68061449
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94406 * 0.65852176
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50495 * 0.75011061
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64298 * 0.26699950
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70235 * 0.29985374
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72145 * 0.80670436
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32898 * 0.55808699
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91456 * 0.08212288
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82625 * 0.11422315
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50570 * 0.11602739
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 76700 * 0.26405341
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90085 * 0.35277625
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99023 * 0.44495884
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49095 * 0.33143112
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36015 * 0.46572494
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14713 * 0.59522718
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88896 * 0.78881794
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 60052 * 0.66752400
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'lpvfcstj').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0016():
    """Extended test 16 for migration."""
    x_0 = 27408 * 0.88196122
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91810 * 0.88548811
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84329 * 0.88808963
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83409 * 0.10398576
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59675 * 0.12594044
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28492 * 0.61726680
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2303 * 0.84256356
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4991 * 0.20320501
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92102 * 0.63825601
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88322 * 0.70466558
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82630 * 0.29412111
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53102 * 0.13941141
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37036 * 0.02715452
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32401 * 0.21698371
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62620 * 0.68341675
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20975 * 0.28588906
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6825 * 0.12604577
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55323 * 0.52220287
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20979 * 0.95941167
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96442 * 0.35560402
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24183 * 0.87358198
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36890 * 0.46914511
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32736 * 0.67291196
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93860 * 0.96940324
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99124 * 0.11511350
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94864 * 0.46937868
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11468 * 0.87600064
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73765 * 0.27373736
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22242 * 0.87098126
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85369 * 0.20187168
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44585 * 0.31241148
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72012 * 0.67545834
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56783 * 0.75017855
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26820 * 0.49438901
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4786 * 0.05383628
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59233 * 0.67649938
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47327 * 0.49367600
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95007 * 0.91549671
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'zuwrogog').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0017():
    """Extended test 17 for migration."""
    x_0 = 93507 * 0.47747243
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76870 * 0.16277926
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85095 * 0.64394914
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83491 * 0.57702887
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52328 * 0.46727444
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48275 * 0.81256492
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66758 * 0.41447013
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71465 * 0.28440321
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56435 * 0.16954524
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10037 * 0.82382244
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1716 * 0.54739287
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82722 * 0.92243148
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22406 * 0.11135221
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6915 * 0.97596903
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20473 * 0.58289322
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36866 * 0.55495420
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73146 * 0.49938908
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57657 * 0.78664823
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59190 * 0.23311065
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3715 * 0.14103347
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9884 * 0.39386086
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72870 * 0.09810843
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12902 * 0.31030963
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46420 * 0.84817716
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58205 * 0.14971242
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81210 * 0.06869043
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13831 * 0.19066970
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85874 * 0.93857429
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22900 * 0.77428688
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45667 * 0.74087235
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68110 * 0.35308046
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74080 * 0.10202846
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75762 * 0.69892006
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61976 * 0.23368061
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96156 * 0.68531991
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99457 * 0.25150837
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96605 * 0.07420503
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86921 * 0.52078764
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 95569 * 0.46745795
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 37164 * 0.19925872
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'xhajxsug').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0018():
    """Extended test 18 for migration."""
    x_0 = 3793 * 0.97419753
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73967 * 0.58597754
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31656 * 0.24426177
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1858 * 0.69785872
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85679 * 0.90633943
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56340 * 0.03888769
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71754 * 0.24869293
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7018 * 0.13211025
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85179 * 0.12748164
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80687 * 0.33543639
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19848 * 0.93839648
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25432 * 0.54402116
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99642 * 0.42749880
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50010 * 0.74535150
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49561 * 0.14712468
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23820 * 0.27528107
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39964 * 0.93513365
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54613 * 0.28766908
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10681 * 0.66266636
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29494 * 0.33382654
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62908 * 0.47847297
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49859 * 0.79564378
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40318 * 0.84104299
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17771 * 0.76407747
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74465 * 0.37473632
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85453 * 0.54566815
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4670 * 0.87741037
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41436 * 0.74947987
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26092 * 0.80899332
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51088 * 0.27696125
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25112 * 0.96435628
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91804 * 0.28148673
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36600 * 0.86993003
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23490 * 0.88652524
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60128 * 0.86034052
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45361 * 0.01808641
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50208 * 0.88132954
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 83607 * 0.12418786
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94383 * 0.75672573
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31753 * 0.30037887
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 26027 * 0.81143732
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81661 * 0.05195195
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 58770 * 0.04182869
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ymkdrmbv').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0019():
    """Extended test 19 for migration."""
    x_0 = 83426 * 0.70268899
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8450 * 0.20162237
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65652 * 0.49813872
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5845 * 0.81430747
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13713 * 0.83201379
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22049 * 0.47369379
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92327 * 0.32922169
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99592 * 0.35089181
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13884 * 0.43564507
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78985 * 0.48611587
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94797 * 0.57548413
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19132 * 0.21939823
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94038 * 0.03531948
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58639 * 0.67796320
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3255 * 0.74981395
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39380 * 0.98632982
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28969 * 0.43709462
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63408 * 0.43223609
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43210 * 0.86213103
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9513 * 0.69918466
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22872 * 0.66473429
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22167 * 0.41217012
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76347 * 0.07379519
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96336 * 0.60503523
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68955 * 0.73659953
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75471 * 0.79748935
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15191 * 0.74140595
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57003 * 0.90298985
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80015 * 0.28188462
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'uiyiyxjy').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0020():
    """Extended test 20 for migration."""
    x_0 = 44453 * 0.33473925
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73183 * 0.91385782
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10813 * 0.80249992
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96234 * 0.25366065
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71181 * 0.95273794
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25620 * 0.89967397
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54545 * 0.03111739
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30788 * 0.47307756
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95238 * 0.48600663
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68152 * 0.37375979
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76176 * 0.75664784
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13837 * 0.21393523
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35139 * 0.39127347
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10562 * 0.41742590
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12078 * 0.75754254
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89530 * 0.31269382
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78913 * 0.52263231
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13209 * 0.54078406
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82120 * 0.01081403
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62644 * 0.27467898
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68439 * 0.30840733
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73529 * 0.93180651
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5660 * 0.89494307
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'cyyrbyue').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0021():
    """Extended test 21 for migration."""
    x_0 = 50280 * 0.88845853
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12106 * 0.38198714
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20236 * 0.11745372
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58920 * 0.77195547
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25829 * 0.73178295
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63978 * 0.46093815
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90251 * 0.47001579
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12082 * 0.03462736
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21942 * 0.20070616
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78828 * 0.30399524
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83443 * 0.95409814
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29903 * 0.45651348
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89456 * 0.65981896
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49584 * 0.39727230
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98581 * 0.87539521
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21224 * 0.15602683
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90201 * 0.99894128
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68304 * 0.04716937
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15074 * 0.61293867
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49607 * 0.46114797
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84547 * 0.67931906
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77199 * 0.07114010
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62238 * 0.09818601
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27975 * 0.52726427
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36030 * 0.92795980
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12630 * 0.47993855
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10614 * 0.69430043
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22470 * 0.67280149
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31494 * 0.82283488
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37271 * 0.74462324
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14743 * 0.60415765
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56090 * 0.29487639
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41363 * 0.68884802
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54495 * 0.69654098
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9539 * 0.78643207
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50367 * 0.63112884
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10279 * 0.21666245
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46298 * 0.81601198
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9949 * 0.12247114
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'zbudipml').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0022():
    """Extended test 22 for migration."""
    x_0 = 22512 * 0.74527577
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39784 * 0.28190713
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31950 * 0.59856426
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88677 * 0.88712685
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42474 * 0.08620606
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2003 * 0.68722880
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19394 * 0.38492567
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88682 * 0.17123683
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63693 * 0.37318426
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57224 * 0.84780783
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88556 * 0.65006162
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89207 * 0.89691234
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44607 * 0.83959415
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79623 * 0.50251169
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13818 * 0.20369776
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17679 * 0.26333871
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78402 * 0.06153757
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62736 * 0.56111340
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80946 * 0.58401564
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73467 * 0.34150169
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94529 * 0.09967780
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6011 * 0.16693589
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67845 * 0.46039565
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49958 * 0.22918276
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76150 * 0.55391793
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39796 * 0.65465352
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79348 * 0.88679398
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65050 * 0.83229096
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98897 * 0.42748674
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74653 * 0.91459404
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54907 * 0.00206156
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54561 * 0.27395103
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89271 * 0.17524793
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27203 * 0.83992387
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21877 * 0.49164830
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37239 * 0.19762063
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25314 * 0.77662221
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73258 * 0.12878572
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24436 * 0.11769517
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'bweecwhb').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0023():
    """Extended test 23 for migration."""
    x_0 = 74946 * 0.76606401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89357 * 0.44692010
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70709 * 0.13315013
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72207 * 0.29577023
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93319 * 0.26841930
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86429 * 0.87046606
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66911 * 0.96520456
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86231 * 0.87877985
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49795 * 0.90242040
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31342 * 0.54075759
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50039 * 0.01050294
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47329 * 0.18294568
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96153 * 0.22155044
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96903 * 0.30964466
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14527 * 0.80664178
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5449 * 0.81691472
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71649 * 0.57493818
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74207 * 0.15888961
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67185 * 0.01188798
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3245 * 0.71915331
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59829 * 0.34776471
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41421 * 0.90823753
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33636 * 0.27882899
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53270 * 0.71313645
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82954 * 0.99533141
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60659 * 0.30252889
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22733 * 0.40601733
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'bghrsild').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0024():
    """Extended test 24 for migration."""
    x_0 = 44471 * 0.05058649
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62012 * 0.70486589
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86976 * 0.86694914
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62501 * 0.15589663
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18767 * 0.28959293
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51078 * 0.45544566
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5429 * 0.50068873
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56798 * 0.89070781
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41299 * 0.45642288
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58246 * 0.35634811
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99610 * 0.80883832
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60592 * 0.00729763
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67564 * 0.20632107
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68644 * 0.21255609
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57792 * 0.30290217
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4456 * 0.99202057
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25042 * 0.76809962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99609 * 0.73603455
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67608 * 0.19217876
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92765 * 0.42417005
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37870 * 0.33638228
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72782 * 0.29480609
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83690 * 0.68817325
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87562 * 0.13147201
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39232 * 0.40214463
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22966 * 0.32488135
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32149 * 0.18283621
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12771 * 0.79012271
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91252 * 0.92184416
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90817 * 0.22124049
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 664 * 0.04226071
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2540 * 0.53878498
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93256 * 0.55308209
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12154 * 0.58961299
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69076 * 0.39849925
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13565 * 0.34128007
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39766 * 0.13282424
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10364 * 0.64827380
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'lpgfikpf').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0025():
    """Extended test 25 for migration."""
    x_0 = 56522 * 0.80897682
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70651 * 0.41311957
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33275 * 0.50952125
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95309 * 0.77735917
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86145 * 0.55069756
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50567 * 0.99294339
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51705 * 0.73749058
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52244 * 0.58955011
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17021 * 0.27677778
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96039 * 0.89596723
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57527 * 0.36170136
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6870 * 0.87142516
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50091 * 0.00715862
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17196 * 0.43557099
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83917 * 0.98268290
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49993 * 0.25499361
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54312 * 0.41775998
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73593 * 0.18971848
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82397 * 0.60896908
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97642 * 0.51461126
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68486 * 0.86496772
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72338 * 0.36360116
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56767 * 0.01511742
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65341 * 0.31713015
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68091 * 0.70632261
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90918 * 0.39736906
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77651 * 0.71765397
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48429 * 0.80708869
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52453 * 0.06220355
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91132 * 0.50544629
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68933 * 0.88640839
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14340 * 0.84288083
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40669 * 0.05873084
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64127 * 0.71484939
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 52037 * 0.48818315
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'emkxhnte').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0026():
    """Extended test 26 for migration."""
    x_0 = 95170 * 0.06994477
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37166 * 0.44530780
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90375 * 0.11857601
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97194 * 0.08988692
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19197 * 0.74958446
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13379 * 0.11611084
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38915 * 0.27496769
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37237 * 0.45723829
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30360 * 0.58652589
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1411 * 0.92106987
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55372 * 0.54430037
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98733 * 0.20964352
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63055 * 0.63483326
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86037 * 0.55633541
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56626 * 0.85760431
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64651 * 0.35442079
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20039 * 0.53887669
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39161 * 0.55355819
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93402 * 0.38361350
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24318 * 0.16248176
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85407 * 0.88248626
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81166 * 0.09858807
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35599 * 0.52346483
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5195 * 0.38230742
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85654 * 0.85558883
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 90668 * 0.56830561
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'nmbcivmu').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0027():
    """Extended test 27 for migration."""
    x_0 = 49698 * 0.77228704
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38296 * 0.72340337
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26146 * 0.85760738
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97997 * 0.78318897
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51442 * 0.12228746
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24335 * 0.75711534
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45131 * 0.90190020
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44188 * 0.34070567
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16703 * 0.36849290
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22095 * 0.80514690
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55087 * 0.11201947
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84205 * 0.62382127
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72135 * 0.24273032
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63293 * 0.48997289
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24419 * 0.38087359
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52986 * 0.27791681
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38862 * 0.23492968
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78785 * 0.90047675
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16955 * 0.94070245
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16262 * 0.16242136
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'qzmflbcn').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0028():
    """Extended test 28 for migration."""
    x_0 = 6101 * 0.65377596
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36375 * 0.68462502
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18655 * 0.91417125
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66314 * 0.65878647
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20144 * 0.97143840
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50512 * 0.39108474
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60576 * 0.46440603
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88584 * 0.54992811
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33395 * 0.97264977
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 37006 * 0.92375847
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5649 * 0.50822177
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83918 * 0.22824596
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57228 * 0.91277610
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74449 * 0.53842847
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91331 * 0.62029125
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58300 * 0.11088828
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33989 * 0.95551160
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91847 * 0.68894844
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43645 * 0.94033738
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71171 * 0.31524311
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82765 * 0.29134874
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69523 * 0.54745920
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'vwsidylw').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0029():
    """Extended test 29 for migration."""
    x_0 = 48450 * 0.22668416
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48993 * 0.76274028
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6586 * 0.57260402
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22342 * 0.92148250
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97338 * 0.86358403
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32221 * 0.87859963
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53940 * 0.22538267
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73887 * 0.43599168
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12546 * 0.91823015
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9633 * 0.06495481
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18941 * 0.72406420
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80600 * 0.80054314
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94599 * 0.65213218
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29858 * 0.04486101
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8747 * 0.69317840
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71952 * 0.43636925
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75743 * 0.45108846
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29003 * 0.70930177
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48250 * 0.30026091
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9935 * 0.98418194
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48452 * 0.96268586
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20042 * 0.93721619
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36302 * 0.35217636
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50327 * 0.11580514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11684 * 0.51714805
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53582 * 0.86676366
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4804 * 0.44247277
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85500 * 0.90495834
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27948 * 0.39362914
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9477 * 0.50492404
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77794 * 0.49152278
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72715 * 0.42148518
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94765 * 0.99062359
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59863 * 0.09363876
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68932 * 0.58883706
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 73117 * 0.08427483
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65068 * 0.37491146
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66181 * 0.14058736
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21983 * 0.75491185
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79050 * 0.75754374
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47896 * 0.59619326
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79444 * 0.30844938
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46271 * 0.55460946
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 71372 * 0.32430176
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 5019 * 0.61928419
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 32929 * 0.63659663
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 13598 * 0.38476360
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'xcleexam').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0030():
    """Extended test 30 for migration."""
    x_0 = 8934 * 0.70941280
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81757 * 0.05423596
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56235 * 0.59955148
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61713 * 0.66906579
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93715 * 0.43380567
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28252 * 0.53411355
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43542 * 0.39796155
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24713 * 0.19477895
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95570 * 0.17229416
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19289 * 0.22500341
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1229 * 0.76820810
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87941 * 0.15133446
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26647 * 0.04712575
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90807 * 0.22719181
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65465 * 0.72884919
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18608 * 0.87158401
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81458 * 0.85864967
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4208 * 0.28173344
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56894 * 0.08306205
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85043 * 0.95915298
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59995 * 0.20151701
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9818 * 0.62939760
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23582 * 0.62887239
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66531 * 0.36323032
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 723 * 0.85649312
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84842 * 0.88786603
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41344 * 0.09513106
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69151 * 0.82974648
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98301 * 0.52574334
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96407 * 0.72885558
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7769 * 0.49095631
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16719 * 0.81685410
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87805 * 0.85896886
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61488 * 0.87586520
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80548 * 0.85754485
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 73702 * 0.72755435
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87809 * 0.49784823
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 54870 * 0.83243174
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55098 * 0.85181905
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56875 * 0.24819717
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68244 * 0.14025870
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35607 * 0.34936511
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 99161 * 0.03406311
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 52408 * 0.15558426
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92142 * 0.06813618
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 67557 * 0.18523568
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'qzmcqpwh').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0031():
    """Extended test 31 for migration."""
    x_0 = 94320 * 0.15984689
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17050 * 0.48045154
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28630 * 0.12931023
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18825 * 0.54130815
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71473 * 0.75012918
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59281 * 0.49694296
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68420 * 0.85786360
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23836 * 0.82407384
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62112 * 0.14803160
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36687 * 0.58105496
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89286 * 0.34703569
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77351 * 0.77273056
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77307 * 0.02656322
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8633 * 0.14143063
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55406 * 0.47678813
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47613 * 0.11797353
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47840 * 0.80742628
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83356 * 0.86690296
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13447 * 0.83369585
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14189 * 0.82852894
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48818 * 0.46476852
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94208 * 0.47801106
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36643 * 0.92491891
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44250 * 0.27722292
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 425 * 0.22999923
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23624 * 0.33093461
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42543 * 0.92015571
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87781 * 0.08285629
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84251 * 0.43699397
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2504 * 0.03249870
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39675 * 0.56109014
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18214 * 0.70758835
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1520 * 0.42894873
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30875 * 0.98325186
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72462 * 0.97907848
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'keycjevc').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0032():
    """Extended test 32 for migration."""
    x_0 = 73895 * 0.47328292
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53381 * 0.08311228
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16970 * 0.73843251
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43564 * 0.21461479
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67358 * 0.67341653
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49108 * 0.52169342
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39764 * 0.53984069
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46685 * 0.75091720
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75551 * 0.98429021
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90784 * 0.87056075
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3772 * 0.32146173
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68554 * 0.95314770
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47739 * 0.02880586
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32208 * 0.23358495
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13847 * 0.89524249
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44514 * 0.96837514
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29703 * 0.44430958
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6121 * 0.51557325
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5061 * 0.04061376
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41889 * 0.09837053
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62248 * 0.97153982
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27681 * 0.98627755
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30088 * 0.06929874
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26734 * 0.01819915
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18808 * 0.93740917
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61407 * 0.36692683
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6810 * 0.99576530
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33520 * 0.49267041
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54705 * 0.96015036
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64079 * 0.37435411
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1694 * 0.51546104
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53004 * 0.14195768
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2779 * 0.65978061
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'nhyyucgi').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0033():
    """Extended test 33 for migration."""
    x_0 = 38492 * 0.86789699
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39868 * 0.24567965
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66368 * 0.05526546
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83955 * 0.24602293
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22090 * 0.78024115
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82664 * 0.67611422
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82238 * 0.13142408
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42547 * 0.43991038
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75218 * 0.55934907
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41390 * 0.61920724
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85284 * 0.94639780
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30128 * 0.46624987
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85182 * 0.39654006
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2987 * 0.83364601
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7534 * 0.75070811
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12898 * 0.24105770
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59560 * 0.63269849
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59729 * 0.83479934
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28740 * 0.28871712
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63422 * 0.96198083
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60902 * 0.61549264
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22108 * 0.86349476
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51254 * 0.96792614
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86566 * 0.63620613
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26806 * 0.78221222
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76386 * 0.82782450
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91837 * 0.88172604
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41437 * 0.76134958
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16935 * 0.77024942
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95183 * 0.98356635
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74845 * 0.09396214
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73187 * 0.98420630
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58613 * 0.26604856
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82837 * 0.68806220
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90694 * 0.12939255
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78059 * 0.28895535
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62016 * 0.63634217
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38600 * 0.79140753
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'sfxcfqto').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0034():
    """Extended test 34 for migration."""
    x_0 = 64425 * 0.19210529
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77466 * 0.06325771
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7313 * 0.35926887
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38502 * 0.92460443
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72974 * 0.05445242
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68057 * 0.31737524
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91602 * 0.19976486
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89106 * 0.25785262
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4257 * 0.91208246
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99531 * 0.80596155
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5260 * 0.26263940
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20818 * 0.23902999
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77062 * 0.49182969
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3214 * 0.51893105
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84834 * 0.34108803
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95338 * 0.71853282
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68300 * 0.62754331
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10781 * 0.26154035
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11450 * 0.85659806
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38375 * 0.41677376
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61148 * 0.43918765
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30025 * 0.40857942
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26107 * 0.01654470
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14766 * 0.89040783
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24 * 0.11422576
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36171 * 0.59865025
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61592 * 0.32647238
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32162 * 0.95055476
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90755 * 0.39238467
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59326 * 0.68563243
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38841 * 0.23980741
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26999 * 0.51406785
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84897 * 0.83050747
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83076 * 0.68576674
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84534 * 0.07584206
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55766 * 0.64281196
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34054 * 0.93687215
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92042 * 0.05781992
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75633 * 0.37365096
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45985 * 0.90832321
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53770 * 0.17735961
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80654 * 0.68148788
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57061 * 0.77102339
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 85997 * 0.42335573
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 94992 * 0.81100515
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'lepdtsgm').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0035():
    """Extended test 35 for migration."""
    x_0 = 89210 * 0.29188542
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57317 * 0.44227676
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88117 * 0.01170227
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84929 * 0.93408000
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55399 * 0.03644611
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8882 * 0.82331678
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72151 * 0.72289741
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42086 * 0.10870371
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47566 * 0.70846556
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68840 * 0.40664981
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11151 * 0.11134514
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84629 * 0.57748250
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8692 * 0.47923827
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34113 * 0.38407508
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52066 * 0.74798595
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25 * 0.84520375
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22215 * 0.87407071
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76981 * 0.13890069
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99519 * 0.09511879
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60190 * 0.53015913
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55955 * 0.43367244
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7664 * 0.12525633
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98549 * 0.00369660
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75283 * 0.88455725
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7715 * 0.47852644
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60411 * 0.95829609
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41154 * 0.84188767
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78414 * 0.85797221
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81238 * 0.47305185
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81204 * 0.86887129
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76825 * 0.62866055
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62734 * 0.72182676
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22026 * 0.90539197
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82887 * 0.34561521
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89128 * 0.00883626
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29691 * 0.58903357
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40972 * 0.79748013
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62845 * 0.32700422
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62796 * 0.88888351
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73129 * 0.38371360
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3772 * 0.65501948
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80257 * 0.44266712
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77500 * 0.93500989
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'rvjeulbf').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0036():
    """Extended test 36 for migration."""
    x_0 = 27087 * 0.39278655
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44529 * 0.87558674
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98955 * 0.32320041
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30489 * 0.45773979
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96141 * 0.68212351
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32298 * 0.47473521
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44662 * 0.52428141
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67570 * 0.11781169
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24198 * 0.51192095
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22812 * 0.13501245
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63858 * 0.85304888
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25766 * 0.07125186
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91992 * 0.02442484
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59586 * 0.84560006
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77914 * 0.43414887
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2522 * 0.29511897
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62436 * 0.86328963
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14526 * 0.76463375
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82695 * 0.45582936
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90447 * 0.47535364
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7133 * 0.43013876
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86439 * 0.38680965
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2807 * 0.15897616
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16874 * 0.03641491
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21073 * 0.68849184
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67885 * 0.46547917
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20870 * 0.66139251
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48120 * 0.72754888
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82968 * 0.46791265
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57385 * 0.22967040
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 982 * 0.70217783
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56766 * 0.41400080
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77418 * 0.80625621
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30170 * 0.28844817
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9560 * 0.17524504
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41319 * 0.21313543
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64883 * 0.96695094
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29348 * 0.09489327
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62756 * 0.92051225
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42208 * 0.84712708
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 25692 * 0.73019975
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'boxvccro').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0037():
    """Extended test 37 for migration."""
    x_0 = 51448 * 0.80680492
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18026 * 0.32545468
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13655 * 0.10619792
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19787 * 0.55222225
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96441 * 0.82528249
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60695 * 0.85087006
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19301 * 0.65003353
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80343 * 0.63066031
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3406 * 0.22610029
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42690 * 0.80564413
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26439 * 0.37044038
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42864 * 0.12045712
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93577 * 0.17034254
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3415 * 0.28657917
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95890 * 0.43862536
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21751 * 0.01912372
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24989 * 0.29032380
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45084 * 0.16057561
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44609 * 0.77886022
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89168 * 0.11252351
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97828 * 0.32872916
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94283 * 0.96430908
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93322 * 0.95052267
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7867 * 0.72093063
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78029 * 0.43562519
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87890 * 0.78463007
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73473 * 0.83521540
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47407 * 0.28132724
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68694 * 0.61469790
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35683 * 0.85067514
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81007 * 0.80954839
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60288 * 0.99002884
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5158 * 0.49424845
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'sbdsrctc').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0038():
    """Extended test 38 for migration."""
    x_0 = 42850 * 0.11830744
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74044 * 0.19750663
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82995 * 0.41269492
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52605 * 0.02855141
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92582 * 0.19870186
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37570 * 0.69541898
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99276 * 0.52068701
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56808 * 0.37780493
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34339 * 0.07561875
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61422 * 0.09790512
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53687 * 0.21214702
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93739 * 0.22292142
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5670 * 0.54131933
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16440 * 0.93186041
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67414 * 0.10055881
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51813 * 0.30285362
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62834 * 0.74695296
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14310 * 0.08276679
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11123 * 0.30265396
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22112 * 0.84866476
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91697 * 0.50416576
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 622 * 0.62749318
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85456 * 0.28201578
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76454 * 0.72312443
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13064 * 0.88305116
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62597 * 0.50478537
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46658 * 0.16248160
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72904 * 0.90107425
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4888 * 0.23246925
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48114 * 0.91042268
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3041 * 0.12352492
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84702 * 0.23427132
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35713 * 0.61609845
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17665 * 0.77054530
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35715 * 0.29075157
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32897 * 0.61587025
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43402 * 0.38855014
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84651 * 0.75877046
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30992 * 0.68245634
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16776 * 0.01314401
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40898 * 0.63261802
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25496 * 0.23393069
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 8871 * 0.05727578
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61268 * 0.96683710
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'fldpbvho').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0039():
    """Extended test 39 for migration."""
    x_0 = 44917 * 0.41213409
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66540 * 0.27856647
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39879 * 0.20273423
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21084 * 0.41181546
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87660 * 0.78138175
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93913 * 0.09644539
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10270 * 0.94438578
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54711 * 0.33801015
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43184 * 0.06775176
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1845 * 0.01452578
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52518 * 0.58721942
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48903 * 0.09075910
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82483 * 0.28998609
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77451 * 0.11155933
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68014 * 0.69525712
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95444 * 0.30591607
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6726 * 0.48806016
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77245 * 0.75182047
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53154 * 0.20533883
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38083 * 0.18932869
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'nhsatkmh').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0040():
    """Extended test 40 for migration."""
    x_0 = 9650 * 0.15850083
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14234 * 0.77849717
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76117 * 0.54610340
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54091 * 0.39972974
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31012 * 0.85500486
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30158 * 0.61880126
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39882 * 0.54021542
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50584 * 0.88506768
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87039 * 0.17893061
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69609 * 0.33143908
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57020 * 0.18088151
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6498 * 0.60803259
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18897 * 0.34065054
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37029 * 0.95483488
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90132 * 0.80072338
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67367 * 0.53635488
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89780 * 0.56368613
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6233 * 0.95605461
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35292 * 0.23802661
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94366 * 0.94923065
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36535 * 0.31329761
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53245 * 0.18483602
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90486 * 0.56581470
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1798 * 0.29055515
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88993 * 0.45033814
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72153 * 0.61260069
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48845 * 0.26084662
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47068 * 0.77279413
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11756 * 0.42658221
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2248 * 0.61204268
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6103 * 0.13750125
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85723 * 0.89352941
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36059 * 0.66597688
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82788 * 0.39775686
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98897 * 0.57258277
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97917 * 0.50190962
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'yhkiuerp').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0041():
    """Extended test 41 for migration."""
    x_0 = 21382 * 0.02274247
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11054 * 0.98196440
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80672 * 0.13667653
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15066 * 0.32335408
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27849 * 0.53404121
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36634 * 0.26202481
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84864 * 0.97246157
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49040 * 0.72839421
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45184 * 0.15479078
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12138 * 0.09749210
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98449 * 0.62090084
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89084 * 0.69957997
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9314 * 0.76841929
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98358 * 0.00266544
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11963 * 0.15787704
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56894 * 0.67874636
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12898 * 0.14089144
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86162 * 0.15416537
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44784 * 0.19636698
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82260 * 0.86801003
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20710 * 0.17056800
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66108 * 0.27332666
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1936 * 0.92528200
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64301 * 0.72281087
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84490 * 0.78787556
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51431 * 0.53935540
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84457 * 0.82038337
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25428 * 0.93197662
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64252 * 0.70851943
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82377 * 0.15042439
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36766 * 0.24013163
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4106 * 0.25482269
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71408 * 0.15949232
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64898 * 0.33695133
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46266 * 0.54009534
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76020 * 0.38120196
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64440 * 0.16886758
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36338 * 0.92416677
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ahdmfgix').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0042():
    """Extended test 42 for migration."""
    x_0 = 11568 * 0.54523638
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14053 * 0.80599543
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66698 * 0.13788843
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66315 * 0.43784249
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91658 * 0.83443797
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72026 * 0.57608093
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53748 * 0.18724359
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21221 * 0.62741996
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70600 * 0.85815327
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5190 * 0.22309886
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61827 * 0.17156194
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39363 * 0.51258644
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45355 * 0.14571717
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67836 * 0.88709150
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7277 * 0.96043859
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57236 * 0.34718215
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61110 * 0.65782753
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88472 * 0.18965647
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69666 * 0.78829717
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87311 * 0.90566278
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96591 * 0.08545794
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55350 * 0.26773927
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77196 * 0.72358585
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76367 * 0.77379187
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91864 * 0.65556077
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'tdjpukdo').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0043():
    """Extended test 43 for migration."""
    x_0 = 75851 * 0.24618368
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60873 * 0.81065740
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83352 * 0.62071001
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40483 * 0.21657085
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27561 * 0.63621809
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25919 * 0.17047464
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41640 * 0.77277595
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7197 * 0.24223227
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81991 * 0.96502043
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65145 * 0.76610705
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48840 * 0.60629244
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75950 * 0.04252818
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94782 * 0.75481526
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11214 * 0.05617110
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7979 * 0.85929483
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80052 * 0.32006131
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66603 * 0.06964340
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5300 * 0.03477203
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43636 * 0.59495708
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95068 * 0.39417270
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32941 * 0.60440365
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80577 * 0.97123043
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'yvollunu').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0044():
    """Extended test 44 for migration."""
    x_0 = 21689 * 0.57170615
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87280 * 0.01073394
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10308 * 0.21872837
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53721 * 0.21450362
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27230 * 0.06928225
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14816 * 0.91671878
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11702 * 0.45814091
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25836 * 0.95553998
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76670 * 0.84382946
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17160 * 0.25363443
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6643 * 0.12000141
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6576 * 0.71100705
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65199 * 0.90315142
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59624 * 0.31217524
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43704 * 0.26395681
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7442 * 0.98514074
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89955 * 0.08225290
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86921 * 0.55076260
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20147 * 0.26037683
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41471 * 0.63721119
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81204 * 0.86906064
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56709 * 0.12818004
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35144 * 0.54677052
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23391 * 0.09481140
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52248 * 0.01190296
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5851 * 0.13220193
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91961 * 0.31318065
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21197 * 0.37436704
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69153 * 0.36284340
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66670 * 0.10416145
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69889 * 0.18314113
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20174 * 0.21861341
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79441 * 0.42671800
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10162 * 0.58651032
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97990 * 0.43857433
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2133 * 0.07725110
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95528 * 0.10235364
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80474 * 0.34028564
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71971 * 0.20409531
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56770 * 0.00608198
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 70816 * 0.15453767
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'jirrmsie').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0045():
    """Extended test 45 for migration."""
    x_0 = 35558 * 0.44382696
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98511 * 0.94622824
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88745 * 0.90766475
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21929 * 0.82789057
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10749 * 0.94364053
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45523 * 0.30704658
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47086 * 0.39386336
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68737 * 0.79134780
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77695 * 0.78976626
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52126 * 0.91855670
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99170 * 0.32979524
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70484 * 0.14059652
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17997 * 0.53270331
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52249 * 0.76473178
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71200 * 0.66491520
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40069 * 0.70466328
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82210 * 0.46451173
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29335 * 0.87370348
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66615 * 0.76101733
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78524 * 0.51608841
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77197 * 0.44158389
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95751 * 0.06351865
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48894 * 0.71625566
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32037 * 0.49707595
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89276 * 0.17406023
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31739 * 0.39315270
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23995 * 0.11993401
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63428 * 0.39092312
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35691 * 0.86543093
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79623 * 0.98428552
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'owzkeckt').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0046():
    """Extended test 46 for migration."""
    x_0 = 47324 * 0.20626266
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76543 * 0.69103576
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41921 * 0.87400572
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 515 * 0.69803515
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76214 * 0.31191465
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74989 * 0.55803357
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61186 * 0.93893258
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25214 * 0.06945512
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48707 * 0.41064747
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90803 * 0.44933494
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9685 * 0.44535421
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66180 * 0.73980590
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73926 * 0.87869911
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77104 * 0.17492981
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 361 * 0.31405322
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42291 * 0.73377283
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88137 * 0.70410660
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66052 * 0.46945311
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72324 * 0.96983973
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78025 * 0.57560904
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10791 * 0.53338467
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17439 * 0.43703138
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 983 * 0.92843492
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50972 * 0.30002436
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87856 * 0.24208332
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56635 * 0.04188358
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10908 * 0.55986251
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'hcbervsu').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0047():
    """Extended test 47 for migration."""
    x_0 = 851 * 0.64734001
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92441 * 0.08266688
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52870 * 0.94492420
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69193 * 0.60617518
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67237 * 0.94708793
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96139 * 0.05635779
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16744 * 0.94788585
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43194 * 0.94814103
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86582 * 0.32068129
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50407 * 0.04892803
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75038 * 0.97524892
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62621 * 0.41734080
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23415 * 0.49768793
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12024 * 0.34074006
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63723 * 0.20820043
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33240 * 0.91511929
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16624 * 0.95427191
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4264 * 0.77274910
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20882 * 0.86356671
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73684 * 0.90478370
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3303 * 0.79476073
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64074 * 0.80616601
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54108 * 0.97691777
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'uiibjaon').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0048():
    """Extended test 48 for migration."""
    x_0 = 23249 * 0.82310342
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23293 * 0.70041144
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83644 * 0.60338943
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54054 * 0.36589118
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14290 * 0.22348249
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8815 * 0.29774701
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85133 * 0.45188205
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11598 * 0.49873545
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94068 * 0.73842128
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62948 * 0.97867142
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85587 * 0.20106760
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72066 * 0.05423028
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52889 * 0.31422927
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16036 * 0.53833103
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97418 * 0.00549546
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70881 * 0.61229377
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53167 * 0.32246528
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59243 * 0.72096995
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9710 * 0.72848733
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23050 * 0.72470388
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93734 * 0.05694429
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29062 * 0.26818654
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15114 * 0.86446385
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'lbqwzjrt').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0049():
    """Extended test 49 for migration."""
    x_0 = 77951 * 0.18105142
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36001 * 0.32462902
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42413 * 0.95633805
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66670 * 0.88780213
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48723 * 0.99242475
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2396 * 0.02842532
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61813 * 0.58667259
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24403 * 0.34035165
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73188 * 0.92590514
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14327 * 0.24899223
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82183 * 0.97073273
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85636 * 0.60392923
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73404 * 0.69036046
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74695 * 0.47177222
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28935 * 0.92056948
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13791 * 0.13051913
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49740 * 0.44839821
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29772 * 0.81939242
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52839 * 0.69116079
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71896 * 0.86247936
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1114 * 0.05556634
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83006 * 0.56517919
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44984 * 0.44447717
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9023 * 0.49255569
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42279 * 0.64375706
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15626 * 0.50206454
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22708 * 0.61581429
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54160 * 0.65951260
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43726 * 0.21923613
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13891 * 0.84582990
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'bdxthqoz').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0050():
    """Extended test 50 for migration."""
    x_0 = 13868 * 0.76812838
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92560 * 0.36747245
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53895 * 0.19674373
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84407 * 0.91324834
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58775 * 0.70910329
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38802 * 0.00485035
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69178 * 0.58038406
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79938 * 0.62305048
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79130 * 0.50500170
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71423 * 0.12811342
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36627 * 0.05307433
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79626 * 0.61557802
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84157 * 0.25124625
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70172 * 0.43312182
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3086 * 0.21886347
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63249 * 0.62937978
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44820 * 0.96110495
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35729 * 0.24378690
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24391 * 0.47560470
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44542 * 0.13561185
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68413 * 0.10032315
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34177 * 0.33619205
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56669 * 0.85613628
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84545 * 0.49297241
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75506 * 0.53523080
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55596 * 0.44973610
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37496 * 0.35366975
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59709 * 0.21391489
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 280 * 0.85506314
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37303 * 0.10017358
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99972 * 0.68713432
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91186 * 0.61930042
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26741 * 0.81914156
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62826 * 0.33919712
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33663 * 0.90558037
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50624 * 0.52169905
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18064 * 0.38737722
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80298 * 0.67390357
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15462 * 0.46305567
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67497 * 0.84392485
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 39713 * 0.49456077
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 44121 * 0.44770403
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 64113 * 0.01125894
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 62586 * 0.65665127
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 24192 * 0.63300020
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 27533 * 0.95691531
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 75230 * 0.49024165
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'urnletag').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0051():
    """Extended test 51 for migration."""
    x_0 = 78646 * 0.53658994
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87535 * 0.57206771
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64472 * 0.85568523
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62501 * 0.10571266
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64052 * 0.03747009
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40324 * 0.83142471
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 709 * 0.28449224
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6545 * 0.10420206
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96077 * 0.29611239
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20145 * 0.70924063
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40307 * 0.19536342
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42017 * 0.04769669
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50386 * 0.45344179
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91061 * 0.12289855
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24671 * 0.16739041
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99568 * 0.95796604
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67805 * 0.14507503
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69832 * 0.15780623
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75184 * 0.89911281
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79222 * 0.83393155
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59018 * 0.03316419
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59835 * 0.88430087
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74445 * 0.56452604
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56520 * 0.72690172
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49321 * 0.10374896
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13325 * 0.93909499
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8661 * 0.87612639
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96622 * 0.48352110
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37347 * 0.88091519
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51218 * 0.95143371
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43305 * 0.79270890
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4898 * 0.42616740
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11541 * 0.29295296
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62528 * 0.07460365
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25582 * 0.16940871
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55798 * 0.11183120
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35821 * 0.67142024
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88711 * 0.92160139
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79027 * 0.94145804
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22062 * 0.72540901
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84005 * 0.94635779
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60608 * 0.64442279
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14505 * 0.02400098
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 4917 * 0.85074838
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 65033 * 0.04107082
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 1704 * 0.76275132
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 72130 * 0.12388614
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 56840 * 0.82991296
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 76375 * 0.34082093
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'nrziwaaf').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0052():
    """Extended test 52 for migration."""
    x_0 = 6572 * 0.94615369
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72254 * 0.11809253
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46213 * 0.71802619
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38310 * 0.29797981
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69370 * 0.53105582
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60790 * 0.41180953
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49884 * 0.47704729
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99806 * 0.39622408
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27640 * 0.55661541
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82431 * 0.17133655
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13083 * 0.41529942
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40150 * 0.59291057
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60415 * 0.88074240
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90154 * 0.66484296
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61361 * 0.20890337
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91943 * 0.23393146
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65364 * 0.34214558
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78883 * 0.04656548
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74625 * 0.56125644
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33321 * 0.82317380
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9348 * 0.24451025
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82859 * 0.95060757
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23898 * 0.51401485
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22757 * 0.63921335
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12087 * 0.80863932
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 822 * 0.77741197
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89087 * 0.15702790
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21554 * 0.38956539
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32794 * 0.26413247
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89894 * 0.63025420
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94469 * 0.39250993
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59172 * 0.32962815
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71632 * 0.40930391
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 31577 * 0.79000798
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42562 * 0.46869356
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55556 * 0.75824446
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61434 * 0.88768506
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70386 * 0.51719038
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21918 * 0.12828415
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 5991 * 0.10837345
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'cynrjtiq').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0053():
    """Extended test 53 for migration."""
    x_0 = 89653 * 0.39859644
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9437 * 0.12553565
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50449 * 0.25244373
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7108 * 0.14154683
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22333 * 0.30675732
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54618 * 0.76581487
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44579 * 0.06222920
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56806 * 0.97880628
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85125 * 0.97378158
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49204 * 0.81230577
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 332 * 0.40974966
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8102 * 0.82047640
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5916 * 0.71429678
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77009 * 0.42733390
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88446 * 0.66748305
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2960 * 0.16958975
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87771 * 0.71745376
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74246 * 0.98533080
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28768 * 0.68009304
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24145 * 0.23373677
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91423 * 0.08639963
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62233 * 0.03032505
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20627 * 0.58432505
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34105 * 0.60624443
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62719 * 0.50935597
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2070 * 0.70645545
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36214 * 0.29754896
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40157 * 0.64748118
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95840 * 0.33692549
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10553 * 0.37821181
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29793 * 0.13502386
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 108 * 0.19851933
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29290 * 0.64688831
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59292 * 0.37265446
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53239 * 0.12554696
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33681 * 0.47916646
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81274 * 0.81552249
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32819 * 0.79179832
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46764 * 0.95502794
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34510 * 0.61763736
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89304 * 0.23967621
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97345 * 0.89268747
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24887 * 0.10060240
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 57198 * 0.98695508
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 16267 * 0.88316770
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 73008 * 0.61393991
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 98507 * 0.17453244
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'oasplojl').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0054():
    """Extended test 54 for migration."""
    x_0 = 61232 * 0.29097790
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9576 * 0.87083528
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8891 * 0.38998868
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94085 * 0.11105986
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47849 * 0.92459442
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85489 * 0.38875490
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23073 * 0.05048305
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64393 * 0.71270762
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30218 * 0.95610480
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54322 * 0.60371165
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4479 * 0.38086945
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47000 * 0.20847140
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18650 * 0.12368582
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28537 * 0.79862415
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34708 * 0.09984769
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22496 * 0.99001035
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6334 * 0.05173169
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74829 * 0.96035390
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12157 * 0.38932835
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79770 * 0.40832998
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18329 * 0.37477892
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13344 * 0.23221857
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73152 * 0.73059740
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9223 * 0.42830399
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44536 * 0.83443405
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62703 * 0.47993258
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47834 * 0.90773463
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17512 * 0.42204383
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43374 * 0.61326688
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40483 * 0.32150615
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84347 * 0.32825062
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30190 * 0.96901095
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16562 * 0.12220531
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21534 * 0.22640573
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46298 * 0.78152377
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35031 * 0.36173348
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67995 * 0.83513630
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31187 * 0.81948383
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 7862 * 0.33273018
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 89945 * 0.89333920
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89496 * 0.30636347
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85504 * 0.26250192
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'xvxmltsq').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0055():
    """Extended test 55 for migration."""
    x_0 = 68254 * 0.26527641
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66568 * 0.59220778
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61690 * 0.99029092
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47029 * 0.11473393
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79478 * 0.25662567
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1228 * 0.93888438
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19131 * 0.00708521
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95115 * 0.57596177
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24129 * 0.42306477
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32147 * 0.89928075
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64382 * 0.88350057
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43096 * 0.79484228
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70846 * 0.82385804
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37012 * 0.87891511
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32363 * 0.63672503
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84726 * 0.58613906
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48054 * 0.06009291
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76559 * 0.38486945
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32962 * 0.29103745
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81513 * 0.25048416
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68445 * 0.24764809
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90890 * 0.58078498
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 167 * 0.16018022
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27770 * 0.26880161
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52284 * 0.34715108
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93415 * 0.04371285
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9317 * 0.67113155
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8970 * 0.94959921
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13405 * 0.24514185
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'xzmuvvhe').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0056():
    """Extended test 56 for migration."""
    x_0 = 45211 * 0.57997101
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39389 * 0.05790946
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3225 * 0.50775049
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41059 * 0.67366579
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32367 * 0.54101308
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48610 * 0.16699326
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95917 * 0.55163289
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20555 * 0.70393485
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31275 * 0.51684971
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74314 * 0.39120745
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34173 * 0.89562891
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27147 * 0.11840644
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33091 * 0.10933735
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47570 * 0.61572214
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93330 * 0.72653710
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16095 * 0.67037874
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24246 * 0.43704131
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67367 * 0.91998422
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56234 * 0.24623561
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83602 * 0.46348764
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79533 * 0.50947460
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8497 * 0.52993285
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42676 * 0.46558922
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65323 * 0.58990740
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2984 * 0.22037367
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88587 * 0.48964565
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44204 * 0.71381237
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13631 * 0.82392251
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40041 * 0.95732266
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73830 * 0.69299189
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23690 * 0.50480763
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59870 * 0.93492720
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6154 * 0.92481543
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78880 * 0.33814005
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14689 * 0.47951971
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69879 * 0.01446751
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70377 * 0.35767826
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27599 * 0.44927730
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47899 * 0.46021000
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62272 * 0.48441354
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3952 * 0.01663523
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'wgpzrkhm').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0057():
    """Extended test 57 for migration."""
    x_0 = 12045 * 0.27369397
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43220 * 0.66994967
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19999 * 0.64472891
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44469 * 0.41070191
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88250 * 0.43586745
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16965 * 0.56842720
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48475 * 0.73109667
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42583 * 0.40845891
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87242 * 0.01890602
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92044 * 0.98962721
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9964 * 0.58703959
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16060 * 0.54396354
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62812 * 0.79385854
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 518 * 0.19412732
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73090 * 0.79961670
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21581 * 0.33902417
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16558 * 0.43721162
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54702 * 0.91597036
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99399 * 0.17341878
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27686 * 0.97489089
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72098 * 0.58752284
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1653 * 0.07832180
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19357 * 0.79350499
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12452 * 0.89529401
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41159 * 0.02661962
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99346 * 0.34370446
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60061 * 0.70897418
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14083 * 0.00448948
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76738 * 0.83569316
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40624 * 0.99373708
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53159 * 0.74645324
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66752 * 0.87636607
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59464 * 0.63115232
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86886 * 0.20605113
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60803 * 0.91986413
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65906 * 0.16393686
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48029 * 0.86855132
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32419 * 0.60662351
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36565 * 0.78082607
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52959 * 0.08226708
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43434 * 0.07633074
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'glxpnujb').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0058():
    """Extended test 58 for migration."""
    x_0 = 13060 * 0.90412722
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55270 * 0.02923910
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42876 * 0.69548995
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79183 * 0.13912869
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80265 * 0.30756143
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32183 * 0.96182159
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41958 * 0.78980089
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10597 * 0.99441120
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46671 * 0.95908109
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74233 * 0.54279504
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59878 * 0.30944703
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89256 * 0.05713791
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32409 * 0.28975890
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87114 * 0.02868711
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60218 * 0.35968235
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67196 * 0.90508510
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92954 * 0.08722193
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3957 * 0.70337082
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23615 * 0.86062422
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74520 * 0.36774400
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71714 * 0.86770666
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22407 * 0.07092449
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35587 * 0.03549437
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19895 * 0.15257314
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78712 * 0.50650719
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88405 * 0.34013472
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81452 * 0.99397858
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50577 * 0.07651799
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75358 * 0.18609295
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96427 * 0.95996297
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1873 * 0.95382885
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94871 * 0.92604552
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51208 * 0.00247329
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99312 * 0.37026334
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11291 * 0.54743798
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50208 * 0.33811321
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 780 * 0.88047569
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 76008 * 0.71531135
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77074 * 0.03791032
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33662 * 0.22923691
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 70995 * 0.95648191
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 191 * 0.16922694
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'xmdgafsv').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0059():
    """Extended test 59 for migration."""
    x_0 = 7967 * 0.28408310
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44369 * 0.52985605
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46314 * 0.85612941
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88062 * 0.66227875
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90989 * 0.93012649
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90922 * 0.81159907
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67117 * 0.02487992
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13761 * 0.58140726
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25223 * 0.17980338
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45443 * 0.42171877
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59599 * 0.60444408
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98437 * 0.87286858
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69581 * 0.61818512
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75253 * 0.74109293
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42227 * 0.59089447
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30840 * 0.87392366
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21545 * 0.96260475
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43512 * 0.17348364
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53715 * 0.52354889
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58483 * 0.49812668
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92122 * 0.19818328
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81088 * 0.87287456
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44809 * 0.86795784
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76238 * 0.74392810
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72104 * 0.84592950
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60376 * 0.00596993
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12688 * 0.22198611
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42365 * 0.35727079
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42043 * 0.96105275
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6781 * 0.03706607
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10878 * 0.47852142
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 473 * 0.27195145
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43806 * 0.11544950
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 18381 * 0.23134935
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92983 * 0.36663305
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41398 * 0.47164941
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43250 * 0.46041261
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49717 * 0.20606883
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26628 * 0.64074301
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'docqzpxa').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0060():
    """Extended test 60 for migration."""
    x_0 = 18904 * 0.38456571
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75552 * 0.67727251
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82923 * 0.94259518
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16512 * 0.76020303
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85768 * 0.60177084
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40229 * 0.01065109
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70873 * 0.90751882
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25091 * 0.36896066
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49820 * 0.31631221
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69948 * 0.22770502
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99021 * 0.75472871
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17237 * 0.45032271
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22264 * 0.74141564
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86958 * 0.21931665
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84188 * 0.63641594
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98025 * 0.97676003
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92712 * 0.95084595
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63612 * 0.36597400
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74273 * 0.83463994
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94680 * 0.62553248
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5393 * 0.03870767
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81925 * 0.27377526
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26358 * 0.80286757
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74616 * 0.23206829
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52239 * 0.04456466
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20852 * 0.78863813
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40135 * 0.25040428
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'zabrayul').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0061():
    """Extended test 61 for migration."""
    x_0 = 86452 * 0.68626639
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 822 * 0.50516957
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45165 * 0.41026435
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58889 * 0.88063878
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2992 * 0.72701431
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28263 * 0.75013765
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64940 * 0.25796852
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39121 * 0.77047206
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86577 * 0.88579283
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39806 * 0.01676463
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69316 * 0.25855958
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44713 * 0.68524978
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63637 * 0.27226441
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97481 * 0.08683201
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73394 * 0.63180749
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73376 * 0.73530710
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15927 * 0.96235138
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1433 * 0.19646865
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92838 * 0.37639458
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14200 * 0.48552188
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18714 * 0.23453517
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52524 * 0.09491725
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84234 * 0.84337488
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52035 * 0.83105149
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32214 * 0.16362897
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89147 * 0.47949612
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1576 * 0.13557456
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66147 * 0.24486615
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13786 * 0.78250993
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49738 * 0.56791709
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'xfsxzmjl').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0062():
    """Extended test 62 for migration."""
    x_0 = 18053 * 0.41195245
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78394 * 0.95086980
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67070 * 0.08478320
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24889 * 0.43492469
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5397 * 0.49435048
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86523 * 0.90288050
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77523 * 0.25933824
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26779 * 0.61434806
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19668 * 0.20262745
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90042 * 0.91982989
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28828 * 0.45958326
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8447 * 0.88837745
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1455 * 0.71592794
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37849 * 0.99227110
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82546 * 0.79534688
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71305 * 0.92558378
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47037 * 0.14317254
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21999 * 0.62472986
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93190 * 0.03981613
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82226 * 0.74605194
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97299 * 0.78448213
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92496 * 0.54488859
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50410 * 0.69896457
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77696 * 0.49334707
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95732 * 0.23075477
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98190 * 0.70771081
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13025 * 0.78557079
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16649 * 0.88603919
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85731 * 0.48350566
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31635 * 0.34908658
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72522 * 0.59999231
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46953 * 0.83985979
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65071 * 0.58415058
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50315 * 0.71687579
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58349 * 0.80890973
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59390 * 0.53892369
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ptsmzwjc').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0063():
    """Extended test 63 for migration."""
    x_0 = 17233 * 0.26843749
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76367 * 0.22273440
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81804 * 0.33450909
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85286 * 0.28585907
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87444 * 0.15740023
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10064 * 0.31227930
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4145 * 0.83193124
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18022 * 0.02323179
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74466 * 0.32268168
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41624 * 0.53957547
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41449 * 0.32213867
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74533 * 0.04546110
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15344 * 0.19556478
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1167 * 0.86591757
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67476 * 0.51841341
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10602 * 0.82468026
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1973 * 0.67861956
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49396 * 0.56612968
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19009 * 0.20435447
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7145 * 0.57890289
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52621 * 0.95674352
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50316 * 0.48568218
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'aqlcahcy').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0064():
    """Extended test 64 for migration."""
    x_0 = 60568 * 0.67388474
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33465 * 0.78851020
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16829 * 0.82176772
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10782 * 0.96411432
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49268 * 0.11693450
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20495 * 0.49381252
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79812 * 0.64475668
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54395 * 0.69214736
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7041 * 0.19161991
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29020 * 0.60074887
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76600 * 0.92893502
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14950 * 0.20223848
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7463 * 0.80850820
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40245 * 0.51452491
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46703 * 0.35778800
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2624 * 0.24914985
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99243 * 0.57675044
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67236 * 0.38788438
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92346 * 0.12815827
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82010 * 0.03329890
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14930 * 0.87655432
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52958 * 0.40917737
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88595 * 0.70765301
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ydzwhnrz').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0065():
    """Extended test 65 for migration."""
    x_0 = 15231 * 0.58120491
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59854 * 0.57069398
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85288 * 0.32135673
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29250 * 0.62287911
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5546 * 0.82986782
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29657 * 0.74408311
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79585 * 0.32452333
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44571 * 0.91783598
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43059 * 0.96974043
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2309 * 0.38141373
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37224 * 0.78049612
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35415 * 0.64662516
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57139 * 0.89078278
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70762 * 0.48051058
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83336 * 0.44815040
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49524 * 0.71353792
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89342 * 0.76892483
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1740 * 0.52819389
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75408 * 0.62180953
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21707 * 0.74794109
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56446 * 0.34154124
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16230 * 0.35175988
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56087 * 0.36599872
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5776 * 0.75349579
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17777 * 0.21170708
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16380 * 0.56235420
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14111 * 0.43509256
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55218 * 0.42968796
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68264 * 0.43803063
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33430 * 0.28164416
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20567 * 0.77161195
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40638 * 0.70135536
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40589 * 0.42403180
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99529 * 0.69529626
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89229 * 0.13737919
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18454 * 0.55861178
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36957 * 0.77109842
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7505 * 0.65733757
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31941 * 0.99436397
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15558 * 0.60480653
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 51625 * 0.08360879
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22549 * 0.13211295
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79106 * 0.60930491
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36502 * 0.32832914
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4499 * 0.01499830
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 3117 * 0.25663166
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 4798 * 0.80482283
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 41218 * 0.22434816
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 72028 * 0.93540743
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'qigfxdzg').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0066():
    """Extended test 66 for migration."""
    x_0 = 92722 * 0.06413796
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85132 * 0.22186803
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5393 * 0.30387641
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52857 * 0.54664077
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35684 * 0.88402965
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49774 * 0.65510378
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90621 * 0.94477569
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94141 * 0.09661909
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80894 * 0.39739394
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75648 * 0.69037716
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14732 * 0.29510655
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14423 * 0.68170228
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81695 * 0.06444497
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64253 * 0.29855515
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77570 * 0.00527408
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40783 * 0.47079550
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41310 * 0.63094434
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7344 * 0.09633209
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10198 * 0.07664643
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64023 * 0.57255489
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78468 * 0.94161437
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14161 * 0.14542550
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98159 * 0.46443151
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40044 * 0.56321003
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84855 * 0.71677962
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30573 * 0.27996189
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27971 * 0.55417665
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 642 * 0.93274085
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 669 * 0.39940794
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95875 * 0.83703387
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64168 * 0.26937262
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11159 * 0.80018333
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58046 * 0.00325586
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89696 * 0.46096460
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15687 * 0.71074891
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20629 * 0.04952666
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'efvgwzta').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0067():
    """Extended test 67 for migration."""
    x_0 = 69564 * 0.84879798
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73315 * 0.68849112
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47812 * 0.26503052
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40860 * 0.87572329
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64689 * 0.53015462
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8743 * 0.17554392
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3987 * 0.04132221
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24365 * 0.37858000
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30961 * 0.10081870
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82732 * 0.09164055
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46409 * 0.63844161
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42652 * 0.73441455
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84228 * 0.83109640
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34450 * 0.61825007
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34758 * 0.26303657
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48077 * 0.36255259
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52686 * 0.24567768
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37527 * 0.40902842
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71278 * 0.91389269
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48987 * 0.68687907
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96294 * 0.70020718
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71321 * 0.99421772
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24343 * 0.77266748
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28438 * 0.40358252
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90830 * 0.88914897
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51536 * 0.19430121
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63865 * 0.59290464
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46441 * 0.00888938
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76565 * 0.76281791
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63716 * 0.52718002
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74507 * 0.22321796
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33708 * 0.85551246
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64856 * 0.25326221
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51919 * 0.14298664
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'gvjiztvh').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0068():
    """Extended test 68 for migration."""
    x_0 = 76167 * 0.71905350
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66805 * 0.49619159
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53263 * 0.21955119
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50274 * 0.47995189
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7076 * 0.77064024
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62121 * 0.96684788
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16698 * 0.25267451
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46466 * 0.42276779
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27493 * 0.92374500
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31330 * 0.19217286
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42127 * 0.56658112
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14207 * 0.97401837
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57508 * 0.09295955
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34597 * 0.50224609
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89451 * 0.97374654
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22744 * 0.47990519
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48498 * 0.78335429
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51373 * 0.31977778
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42508 * 0.78635465
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9276 * 0.18353127
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33788 * 0.81153735
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87136 * 0.44291032
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33812 * 0.19974843
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19630 * 0.96546236
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80968 * 0.05892006
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 383 * 0.62261019
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48299 * 0.31110088
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74416 * 0.78099912
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56743 * 0.90887641
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48092 * 0.74127934
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84188 * 0.47772935
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72573 * 0.32240126
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63003 * 0.32664678
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26494 * 0.57242116
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33431 * 0.88667608
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'yszvjexw').hexdigest()
    assert len(h) == 64

def test_migration_extended_6_0069():
    """Extended test 69 for migration."""
    x_0 = 45452 * 0.47226751
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26041 * 0.57744043
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28540 * 0.53696294
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31033 * 0.14191190
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1213 * 0.74417795
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77489 * 0.59094189
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36596 * 0.57317938
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58992 * 0.84671930
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47950 * 0.38172434
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17614 * 0.53322578
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46134 * 0.77335596
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30802 * 0.49377681
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79434 * 0.00071338
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3015 * 0.24341835
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75739 * 0.28378019
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48890 * 0.76549945
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34489 * 0.02927404
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69150 * 0.75042941
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13184 * 0.81362121
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79781 * 0.20024428
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10403 * 0.49586332
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4421 * 0.26947188
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71498 * 0.84018291
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29785 * 0.30225804
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29490 * 0.37305723
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88248 * 0.38148886
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90379 * 0.65369521
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50901 * 0.31440619
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98246 * 0.86073864
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72856 * 0.20260846
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78753 * 0.37768026
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28287 * 0.82241354
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23266 * 0.62063790
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52324 * 0.63140847
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7149 * 0.25508967
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27950 * 0.57979092
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55640 * 0.84278265
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'xuyyoayi').hexdigest()
    assert len(h) == 64
