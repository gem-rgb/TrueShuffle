"""Extended tests for auth suite 4."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_auth_extended_4_0000():
    """Extended test 0 for auth."""
    x_0 = 72726 * 0.68135739
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84226 * 0.77643475
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57463 * 0.97158288
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92690 * 0.42193670
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65095 * 0.02472598
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86390 * 0.51797525
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82245 * 0.28919355
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86317 * 0.80109761
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9327 * 0.64044159
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92064 * 0.43849343
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42207 * 0.82889921
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77944 * 0.18263477
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37487 * 0.84779302
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80203 * 0.78713761
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35513 * 0.46355592
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46843 * 0.79218378
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69307 * 0.07054726
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82100 * 0.42689329
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37818 * 0.65489162
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44293 * 0.31201891
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56394 * 0.76551615
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21658 * 0.01113230
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27640 * 0.74943284
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19934 * 0.29211296
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41772 * 0.07907308
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62179 * 0.85443593
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18827 * 0.63802591
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'gwsnkrao').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0001():
    """Extended test 1 for auth."""
    x_0 = 11545 * 0.96461841
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11438 * 0.18045901
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74911 * 0.35259961
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36104 * 0.51908815
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84903 * 0.11084164
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50620 * 0.03061078
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57214 * 0.63351898
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98418 * 0.92619473
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8011 * 0.79832426
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63862 * 0.19306232
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69174 * 0.73336247
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86782 * 0.42505381
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67769 * 0.94338414
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15198 * 0.05068641
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14750 * 0.25605727
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17465 * 0.71934673
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54934 * 0.27150220
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63944 * 0.54700006
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56603 * 0.96681236
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95476 * 0.07469180
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30663 * 0.66593450
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57417 * 0.24845752
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82560 * 0.26901589
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91469 * 0.92920036
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14148 * 0.06476186
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32518 * 0.71872000
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47802 * 0.05221111
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82801 * 0.21155764
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69993 * 0.29928759
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10217 * 0.28257791
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55909 * 0.62143158
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69337 * 0.42420474
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59092 * 0.09053961
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86273 * 0.86578084
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2146 * 0.67193422
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ivekjqmf').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0002():
    """Extended test 2 for auth."""
    x_0 = 35307 * 0.02817349
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22993 * 0.72660358
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66869 * 0.17127296
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75800 * 0.78547879
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77258 * 0.99198272
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63262 * 0.18911947
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15816 * 0.25989527
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62586 * 0.40343210
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20992 * 0.73913784
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4772 * 0.74727845
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1330 * 0.28192470
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27093 * 0.99588488
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98696 * 0.86558720
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45211 * 0.63711131
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15402 * 0.83639689
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19874 * 0.12967172
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43554 * 0.67700207
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6610 * 0.97620070
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12922 * 0.11266456
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48322 * 0.04953324
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14793 * 0.42943486
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98719 * 0.44389434
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8967 * 0.61582906
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92755 * 0.97363458
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 49598 * 0.49515749
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15118 * 0.50668364
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76845 * 0.96299378
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32255 * 0.76775471
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91125 * 0.00143858
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 956 * 0.56100463
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75846 * 0.22635413
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31343 * 0.58150609
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54477 * 0.67830354
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78684 * 0.90250028
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51466 * 0.94698426
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74945 * 0.50154796
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70217 * 0.07792251
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22256 * 0.53026499
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2960 * 0.70980615
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85850 * 0.56791124
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11551 * 0.17437269
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 7915 * 0.29751007
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75585 * 0.38585642
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 31652 * 0.60793181
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 25578 * 0.30850368
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 86744 * 0.77502113
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 84167 * 0.92205805
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 25479 * 0.53399199
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 86583 * 0.22957520
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 56226 * 0.14513889
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'aeysuihp').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0003():
    """Extended test 3 for auth."""
    x_0 = 37381 * 0.20670113
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77794 * 0.12152016
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17873 * 0.88814721
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28 * 0.44462590
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84704 * 0.99136021
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 479 * 0.15517530
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6057 * 0.78953754
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9371 * 0.43461730
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83327 * 0.94943279
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6618 * 0.67820341
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35187 * 0.68846867
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18130 * 0.90518327
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95678 * 0.46268685
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37498 * 0.15246238
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49559 * 0.61256905
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35680 * 0.72508153
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5117 * 0.74589613
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13076 * 0.04171050
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22070 * 0.00765261
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50878 * 0.91772896
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17493 * 0.23679842
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12414 * 0.89323109
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25669 * 0.35203922
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91383 * 0.11318305
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7107 * 0.46746380
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91073 * 0.64823468
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22628 * 0.01559839
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45480 * 0.50451026
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62956 * 0.93312218
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74815 * 0.50423760
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57272 * 0.60172065
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53344 * 0.08006056
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3627 * 0.26972324
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6742 * 0.65341068
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17309 * 0.70125180
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84909 * 0.71131523
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93064 * 0.96051858
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32920 * 0.95267918
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56958 * 0.87118476
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43574 * 0.54582875
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'bhaekuwp').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0004():
    """Extended test 4 for auth."""
    x_0 = 39774 * 0.58384175
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36241 * 0.44276384
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15890 * 0.71696534
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69619 * 0.21333422
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19157 * 0.48925521
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18301 * 0.65887082
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28058 * 0.82698926
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72737 * 0.16519452
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50271 * 0.65215861
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56769 * 0.58103527
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28062 * 0.58067454
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24784 * 0.60877387
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25237 * 0.33943216
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57102 * 0.30305515
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27060 * 0.99379830
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95158 * 0.39891756
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23821 * 0.18745354
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39066 * 0.34078131
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67582 * 0.39272184
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77936 * 0.13545127
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12151 * 0.42882934
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38992 * 0.53398217
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79754 * 0.61533834
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28650 * 0.69241340
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89603 * 0.57368223
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26608 * 0.03051317
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58906 * 0.03006535
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30872 * 0.84257560
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54088 * 0.30117660
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32230 * 0.69466552
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80673 * 0.31573208
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10270 * 0.57196106
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87567 * 0.91614129
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21615 * 0.28669572
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98485 * 0.66452720
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'xymwvlts').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0005():
    """Extended test 5 for auth."""
    x_0 = 61600 * 0.69173077
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48464 * 0.83215337
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90014 * 0.10529130
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34769 * 0.18189847
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72087 * 0.49497845
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79576 * 0.64135034
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76349 * 0.49120724
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4976 * 0.00028265
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35415 * 0.38434995
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36952 * 0.35167222
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4667 * 0.79747583
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17666 * 0.57039659
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84517 * 0.81504985
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33946 * 0.62953899
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59052 * 0.32094153
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21961 * 0.81351342
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94881 * 0.11674458
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51982 * 0.46252097
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92686 * 0.17119921
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88629 * 0.74887476
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ynfajmqr').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0006():
    """Extended test 6 for auth."""
    x_0 = 6873 * 0.36883433
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36453 * 0.02537081
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72543 * 0.12499976
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29728 * 0.86534600
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72197 * 0.64283844
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69075 * 0.15181128
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27856 * 0.96526160
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78778 * 0.26792250
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61686 * 0.99663390
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79789 * 0.66529049
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33933 * 0.63041166
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84434 * 0.13209025
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95197 * 0.23279574
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91352 * 0.66949022
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15593 * 0.49252317
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50701 * 0.24448867
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36955 * 0.21869419
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14345 * 0.92164704
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2957 * 0.63619144
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98631 * 0.80475310
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74392 * 0.17294930
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71923 * 0.14501092
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61810 * 0.86987305
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37719 * 0.42138714
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97880 * 0.72555547
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23238 * 0.93305780
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11555 * 0.56429242
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72648 * 0.42729986
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43267 * 0.58878067
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75020 * 0.40209056
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6717 * 0.22230214
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72474 * 0.39000213
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'asavhzll').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0007():
    """Extended test 7 for auth."""
    x_0 = 95982 * 0.77594739
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14050 * 0.87371263
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52595 * 0.88284211
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55001 * 0.10998739
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89059 * 0.17342498
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96568 * 0.54023190
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18049 * 0.12500355
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51234 * 0.13538664
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7893 * 0.96937918
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96110 * 0.44261436
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13610 * 0.35980136
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5867 * 0.43049070
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71468 * 0.45153198
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19927 * 0.57311634
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51545 * 0.14143710
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42579 * 0.28956539
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70182 * 0.03817036
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96585 * 0.55661862
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24532 * 0.65242167
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41920 * 0.73151821
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61078 * 0.28980856
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32578 * 0.02207087
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8013 * 0.48489693
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97019 * 0.49257861
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72643 * 0.62381558
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60828 * 0.94041251
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49258 * 0.33639958
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37273 * 0.73289245
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15122 * 0.93704113
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75514 * 0.16332121
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76491 * 0.37080237
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7854 * 0.16762995
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30793 * 0.88512476
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78241 * 0.51558084
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66705 * 0.21226499
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34134 * 0.58426364
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3693 * 0.70503457
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38395 * 0.55068573
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'nebeuskl').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0008():
    """Extended test 8 for auth."""
    x_0 = 57136 * 0.34144168
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29991 * 0.99776842
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57581 * 0.40484884
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18616 * 0.31602378
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88962 * 0.70542112
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96045 * 0.32860962
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51764 * 0.27616019
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61132 * 0.24502764
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71002 * 0.66032594
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69266 * 0.39949877
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65581 * 0.27516220
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13497 * 0.55822017
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17900 * 0.05197605
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69277 * 0.61476813
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63545 * 0.76589521
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23586 * 0.18445209
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80634 * 0.59082826
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62828 * 0.64817669
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33373 * 0.41996666
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34332 * 0.79926439
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60861 * 0.60053825
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73042 * 0.93003093
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34317 * 0.70136575
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23798 * 0.40010763
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15760 * 0.88839191
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64545 * 0.73463213
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47305 * 0.33584676
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34539 * 0.42725526
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92923 * 0.49675963
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4134 * 0.44158960
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6875 * 0.57035731
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4712 * 0.49424093
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59873 * 0.83574328
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 870 * 0.77684210
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96223 * 0.70042659
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39656 * 0.56879348
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52802 * 0.32005820
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10211 * 0.96057608
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97059 * 0.53940648
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97733 * 0.33960072
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53358 * 0.29455635
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9560 * 0.51585727
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1689 * 0.84266896
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 5709 * 0.38707855
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 51509 * 0.17057741
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 78834 * 0.19905144
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'tanwcmxz').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0009():
    """Extended test 9 for auth."""
    x_0 = 2778 * 0.83456186
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71251 * 0.41798367
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93636 * 0.20005266
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12750 * 0.04654495
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53286 * 0.24053637
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71861 * 0.33275597
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25217 * 0.48751616
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91963 * 0.18463349
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88699 * 0.11207283
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5185 * 0.41801790
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5801 * 0.26020800
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79384 * 0.08904907
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77857 * 0.09782111
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38763 * 0.95132601
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62728 * 0.77367218
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15171 * 0.07538528
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65282 * 0.89069900
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12160 * 0.05651969
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92634 * 0.25314211
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99780 * 0.95456636
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49143 * 0.85597911
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73192 * 0.01623707
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26542 * 0.19071286
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34921 * 0.88357353
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48888 * 0.18746372
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3212 * 0.00714210
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98384 * 0.91238837
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'qthhhhvg').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0010():
    """Extended test 10 for auth."""
    x_0 = 66375 * 0.01987278
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19715 * 0.40744239
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13785 * 0.56698917
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4989 * 0.08867655
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4765 * 0.12282222
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60227 * 0.79291123
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74303 * 0.39846620
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72449 * 0.25459748
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32591 * 0.02670017
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34909 * 0.79345461
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44573 * 0.54138072
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69611 * 0.93127345
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14891 * 0.36991936
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 616 * 0.44934078
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2399 * 0.94554836
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17 * 0.00177338
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85796 * 0.48517401
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15593 * 0.12655562
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28384 * 0.29368669
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4260 * 0.90774038
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68023 * 0.45301716
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9128 * 0.64448467
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99943 * 0.87254863
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74876 * 0.84542252
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55833 * 0.90331428
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83341 * 0.48679499
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20723 * 0.19616989
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7166 * 0.40097977
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11069 * 0.79813691
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34856 * 0.13445077
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66601 * 0.18671545
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47314 * 0.30979043
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2343 * 0.81133230
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32883 * 0.12670276
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88202 * 0.45493352
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18434 * 0.95978324
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22945 * 0.20440089
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2609 * 0.32963830
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 8306 * 0.35492142
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91891 * 0.61776964
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11405 * 0.80353596
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85222 * 0.17849414
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 89255 * 0.85605432
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 21945 * 0.16120324
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 2530 * 0.50062245
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 52094 * 0.31523176
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 16653 * 0.74152995
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 57256 * 0.71147224
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'qkmsgvwg').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0011():
    """Extended test 11 for auth."""
    x_0 = 44268 * 0.90523363
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47663 * 0.95669631
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59511 * 0.87338850
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61113 * 0.37439895
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87864 * 0.29604549
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46807 * 0.77794227
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10677 * 0.81501153
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35881 * 0.69171572
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94316 * 0.57337826
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27544 * 0.63479861
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16480 * 0.63931078
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60675 * 0.95593401
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17662 * 0.17247739
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27870 * 0.37887984
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80347 * 0.48478875
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68144 * 0.01728915
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60066 * 0.66060107
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69165 * 0.96897593
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99821 * 0.70624349
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60763 * 0.18875621
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9837 * 0.31107788
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95722 * 0.45699007
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47148 * 0.71116290
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77502 * 0.87606002
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67511 * 0.16329590
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31245 * 0.50095838
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80517 * 0.62539373
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30962 * 0.43646733
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34218 * 0.67119608
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2891 * 0.49994093
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89358 * 0.79526961
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54705 * 0.86553064
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80625 * 0.09971241
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63839 * 0.30349154
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28179 * 0.98842566
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75524 * 0.25992658
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29784 * 0.01549473
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66306 * 0.21820113
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ltdhvmzo').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0012():
    """Extended test 12 for auth."""
    x_0 = 95217 * 0.79580300
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67656 * 0.82764521
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22556 * 0.33728523
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2764 * 0.92525574
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54340 * 0.51067683
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32739 * 0.38603659
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12030 * 0.39030328
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3407 * 0.46736368
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14275 * 0.67127672
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26982 * 0.83513042
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78752 * 0.75898046
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61520 * 0.73641672
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66506 * 0.46432268
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30326 * 0.95606444
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44860 * 0.77303954
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86640 * 0.22300600
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58556 * 0.34046772
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86556 * 0.44886414
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55156 * 0.29177064
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28925 * 0.41910410
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33495 * 0.88358306
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22513 * 0.32871050
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72517 * 0.55934700
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46400 * 0.91504060
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42487 * 0.20057592
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25494 * 0.10422266
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81247 * 0.25992937
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16799 * 0.93297321
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79880 * 0.84684219
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39702 * 0.93451421
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58312 * 0.23260038
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81866 * 0.67564108
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5909 * 0.47465082
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77273 * 0.00064240
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73194 * 0.65225016
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17481 * 0.97407474
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 77504 * 0.07538216
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55968 * 0.42798512
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35660 * 0.72160840
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20340 * 0.25838951
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68719 * 0.16978445
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 51250 * 0.53823690
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 37617 * 0.36642413
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'pkmptzgr').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0013():
    """Extended test 13 for auth."""
    x_0 = 90431 * 0.62998747
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45457 * 0.32080758
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46318 * 0.60198547
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50866 * 0.98466680
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62853 * 0.15999820
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37411 * 0.24421527
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87979 * 0.15514491
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76799 * 0.37048403
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72774 * 0.28624238
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8082 * 0.77706165
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64623 * 0.88906697
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83015 * 0.69283186
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99279 * 0.26388575
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14807 * 0.09043743
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90262 * 0.57132394
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71887 * 0.40082556
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61733 * 0.13486506
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33918 * 0.56083451
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43563 * 0.78412239
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3803 * 0.99970330
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95977 * 0.77717255
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48746 * 0.83311210
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93761 * 0.29931040
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86601 * 0.42772444
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3001 * 0.08164593
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33796 * 0.39248839
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30804 * 0.47610626
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43307 * 0.59426277
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38374 * 0.38132682
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54705 * 0.76093434
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36786 * 0.75614819
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13163 * 0.62110890
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21508 * 0.99699506
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98433 * 0.20491037
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92579 * 0.10884421
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66704 * 0.49745794
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60822 * 0.84426443
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13064 * 0.10375657
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18797 * 0.06795573
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69092 * 0.82548662
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'paictpji').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0014():
    """Extended test 14 for auth."""
    x_0 = 55099 * 0.10378958
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36561 * 0.31659829
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90096 * 0.57730428
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71907 * 0.61823279
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88271 * 0.16136455
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94241 * 0.27029029
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21828 * 0.92291170
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13465 * 0.56916092
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82482 * 0.21381364
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54018 * 0.74003794
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32325 * 0.40376850
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57972 * 0.02745926
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28071 * 0.24392851
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97648 * 0.50033071
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31862 * 0.92763858
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12557 * 0.42964846
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78009 * 0.26582086
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2223 * 0.29041796
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14816 * 0.74473226
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67491 * 0.36905234
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6948 * 0.26423660
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36095 * 0.17557699
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90251 * 0.04245999
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28907 * 0.90628582
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22765 * 0.16853968
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17686 * 0.67616616
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94227 * 0.63346245
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69887 * 0.47598985
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94072 * 0.89422131
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29289 * 0.63617889
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69784 * 0.72994448
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9583 * 0.67083554
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52906 * 0.05192336
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33411 * 0.04627481
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19099 * 0.98713979
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 23382 * 0.75251671
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65233 * 0.89935139
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35718 * 0.61853297
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14385 * 0.78617716
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22972 * 0.66560674
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48270 * 0.03889953
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89133 * 0.76295817
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 61673 * 0.96490833
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20928 * 0.93268880
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 216 * 0.17552401
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 43085 * 0.75802343
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 33102 * 0.80319791
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 68298 * 0.81284108
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 25853 * 0.82652469
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'xojfmnco').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0015():
    """Extended test 15 for auth."""
    x_0 = 20708 * 0.26443342
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91644 * 0.75941459
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93397 * 0.32517196
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47556 * 0.63132070
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71492 * 0.97672939
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73794 * 0.78933347
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83765 * 0.53745189
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29747 * 0.73060985
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95776 * 0.53606669
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11887 * 0.33523643
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88372 * 0.16258885
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13583 * 0.13533144
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81812 * 0.31610439
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51583 * 0.94937333
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65939 * 0.50803206
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89793 * 0.27660326
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26393 * 0.76488447
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1758 * 0.74829156
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91973 * 0.52193998
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69778 * 0.85073340
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24856 * 0.15708205
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'majtppbh').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0016():
    """Extended test 16 for auth."""
    x_0 = 27803 * 0.92451907
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44820 * 0.36024259
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72934 * 0.71223479
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13928 * 0.14713782
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44049 * 0.94343909
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20567 * 0.65829333
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8311 * 0.11129892
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55091 * 0.12471804
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35419 * 0.47886144
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6248 * 0.96700214
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11772 * 0.30596438
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91500 * 0.96499990
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77075 * 0.77571375
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25947 * 0.27921796
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57402 * 0.23544305
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11650 * 0.95405638
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77643 * 0.96705123
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18588 * 0.92964928
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54826 * 0.16693640
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11450 * 0.66819385
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62301 * 0.89181065
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73125 * 0.84377734
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26524 * 0.83141723
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3176 * 0.01143038
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2136 * 0.81878085
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29176 * 0.51117323
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73671 * 0.82919949
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19175 * 0.77832109
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56834 * 0.87227685
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33968 * 0.14482825
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57215 * 0.56137324
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85353 * 0.83894323
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17889 * 0.63247164
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77764 * 0.54298640
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69271 * 0.67606694
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82901 * 0.53975235
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88656 * 0.66656235
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66476 * 0.43811382
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20751 * 0.96465601
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'eejmmczg').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0017():
    """Extended test 17 for auth."""
    x_0 = 32797 * 0.67710824
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57068 * 0.95721929
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19367 * 0.32972548
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61319 * 0.14835968
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73941 * 0.60627899
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99543 * 0.55775984
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63444 * 0.44332828
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19422 * 0.05706885
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84589 * 0.12504211
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13552 * 0.45503303
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70321 * 0.87544247
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44170 * 0.80008073
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44274 * 0.87572360
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56750 * 0.77510779
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46640 * 0.60121723
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88487 * 0.98362948
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77612 * 0.09879645
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20369 * 0.36583515
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13287 * 0.10871106
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97540 * 0.13808403
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79250 * 0.78496089
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57686 * 0.51924765
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17629 * 0.49137023
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71288 * 0.90748022
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80769 * 0.52916520
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41778 * 0.72209923
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52469 * 0.40639707
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36890 * 0.85876246
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35674 * 0.37415810
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24176 * 0.08980745
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39527 * 0.61625747
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15958 * 0.69111934
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58855 * 0.58640200
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13182 * 0.18828049
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14608 * 0.15554219
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12623 * 0.88998552
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52935 * 0.42617176
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85844 * 0.35485506
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 20619 * 0.37268496
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 5119 * 0.05259733
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8558 * 0.88668792
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36381 * 0.45848361
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88011 * 0.00506387
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40579 * 0.18982136
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86134 * 0.90626160
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'qqlfzkni').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0018():
    """Extended test 18 for auth."""
    x_0 = 80156 * 0.38571646
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50857 * 0.37659200
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76625 * 0.02658497
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2063 * 0.16672027
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40982 * 0.04435447
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70568 * 0.77240160
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39467 * 0.05996722
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37380 * 0.56622047
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59293 * 0.49786350
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78267 * 0.87991255
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22236 * 0.75782836
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65798 * 0.10000768
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39635 * 0.24915619
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44818 * 0.66469952
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9953 * 0.65986276
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55519 * 0.77110435
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45049 * 0.23629155
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87785 * 0.61598155
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59175 * 0.66895071
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46962 * 0.80434239
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30422 * 0.77346259
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8845 * 0.54128652
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44011 * 0.58346425
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76462 * 0.51663734
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44257 * 0.89659962
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25699 * 0.74715016
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92972 * 0.96051133
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44909 * 0.86950646
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10928 * 0.12259894
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18973 * 0.86749365
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91657 * 0.43370381
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45643 * 0.77975067
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'gluuoeww').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0019():
    """Extended test 19 for auth."""
    x_0 = 38756 * 0.07127502
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77918 * 0.44777878
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21119 * 0.29302551
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46410 * 0.62200818
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48282 * 0.13686727
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5390 * 0.76462582
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70564 * 0.95536340
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91752 * 0.43889524
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28421 * 0.45015719
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 502 * 0.54964102
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6852 * 0.33339628
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37271 * 0.03304595
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37250 * 0.33955300
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79434 * 0.26281466
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45240 * 0.27138675
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42414 * 0.57508969
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91200 * 0.06531807
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66453 * 0.57807492
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89338 * 0.92934492
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34476 * 0.05872852
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11521 * 0.22216869
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83219 * 0.02335806
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75651 * 0.79905664
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5924 * 0.81623876
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48485 * 0.21133542
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94813 * 0.66348720
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4105 * 0.48931261
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1249 * 0.41782126
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62056 * 0.08326959
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15409 * 0.22628472
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60981 * 0.01289167
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65690 * 0.38300014
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92057 * 0.74167459
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19137 * 0.40647397
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'sxkwcjdv').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0020():
    """Extended test 20 for auth."""
    x_0 = 95346 * 0.78110120
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18639 * 0.30120575
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15262 * 0.20752831
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2392 * 0.22199823
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72126 * 0.63024500
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28520 * 0.53615140
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85617 * 0.46066687
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85965 * 0.53014422
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85311 * 0.89024597
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87190 * 0.87837991
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12406 * 0.64850377
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40448 * 0.77513695
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84073 * 0.85357033
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1430 * 0.93768830
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15365 * 0.58192418
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43585 * 0.11746583
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26041 * 0.85840245
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4687 * 0.16275278
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42261 * 0.84847276
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38759 * 0.19633347
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15973 * 0.04362774
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48591 * 0.66678670
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86570 * 0.27802549
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18335 * 0.97402276
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53776 * 0.99903523
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1728 * 0.50201719
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74 * 0.60147591
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11365 * 0.47351861
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75681 * 0.78875452
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'uatbgtbs').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0021():
    """Extended test 21 for auth."""
    x_0 = 91479 * 0.59597842
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43912 * 0.48050815
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83134 * 0.04033984
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75776 * 0.54170832
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42649 * 0.96041118
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70239 * 0.29523188
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97253 * 0.74294856
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31076 * 0.07171333
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1042 * 0.70212936
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88269 * 0.52183853
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13436 * 0.26033514
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60669 * 0.73794863
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 295 * 0.36076254
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56979 * 0.67913310
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18201 * 0.48177916
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8182 * 0.08045223
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71933 * 0.59221683
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91424 * 0.03703451
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30300 * 0.67168622
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58421 * 0.79963943
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84973 * 0.80042447
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10356 * 0.95109436
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26014 * 0.77831811
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46076 * 0.66217497
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21493 * 0.79286092
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46127 * 0.04234174
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94597 * 0.82576348
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71261 * 0.54676898
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91485 * 0.88076326
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22841 * 0.38302878
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72959 * 0.49460630
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97538 * 0.94481115
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'fevmapfg').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0022():
    """Extended test 22 for auth."""
    x_0 = 10262 * 0.93047313
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43880 * 0.36174780
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93769 * 0.94977119
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46402 * 0.90574884
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92766 * 0.25087888
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23485 * 0.53469899
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49997 * 0.70107797
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47591 * 0.32876114
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73248 * 0.50241667
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59744 * 0.41820985
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25977 * 0.98708911
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78583 * 0.33364306
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82258 * 0.23719760
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73182 * 0.99841260
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24051 * 0.21892934
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25467 * 0.44045852
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74863 * 0.46506039
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20065 * 0.80876274
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10553 * 0.53881226
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39748 * 0.01290754
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50874 * 0.00112953
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22217 * 0.69352655
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55315 * 0.08953323
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16428 * 0.72245616
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24335 * 0.24849166
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50660 * 0.84060100
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42977 * 0.85777832
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50775 * 0.66755400
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55563 * 0.65533939
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76031 * 0.71332685
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94109 * 0.87407925
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96192 * 0.43893482
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'ulcphxox').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0023():
    """Extended test 23 for auth."""
    x_0 = 75703 * 0.96483134
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23729 * 0.90469578
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2039 * 0.33943856
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66207 * 0.60167988
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8998 * 0.20117400
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66100 * 0.98770972
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61480 * 0.19289602
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54827 * 0.83198853
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63712 * 0.50733091
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15364 * 0.56036684
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5292 * 0.95748320
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83588 * 0.24947321
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33556 * 0.35227991
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54174 * 0.69973845
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95654 * 0.88840268
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33182 * 0.62078350
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42775 * 0.40850552
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41566 * 0.00956718
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92973 * 0.19110708
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61620 * 0.30159016
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22564 * 0.59933441
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21217 * 0.74282470
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'nfugtsyf').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0024():
    """Extended test 24 for auth."""
    x_0 = 92711 * 0.33325982
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87178 * 0.11502488
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78640 * 0.72651040
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82854 * 0.34497840
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68837 * 0.29977825
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97486 * 0.11956376
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92235 * 0.23356321
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67404 * 0.24844559
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33893 * 0.97540743
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78834 * 0.66747756
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83731 * 0.05309885
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50071 * 0.61621818
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16369 * 0.26168850
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25729 * 0.92812575
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82536 * 0.01069761
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15960 * 0.54296055
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15550 * 0.07379705
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63555 * 0.57645109
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42055 * 0.01662106
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23759 * 0.05203636
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30925 * 0.17463702
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71284 * 0.41710564
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49372 * 0.67946028
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65756 * 0.27335888
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1419 * 0.26423777
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93085 * 0.38646025
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57514 * 0.36036846
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7543 * 0.66513767
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40946 * 0.58367908
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77335 * 0.06204480
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35649 * 0.49999951
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56251 * 0.44905321
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72510 * 0.35278154
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55928 * 0.08421403
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53328 * 0.51794298
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26081 * 0.44913361
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65035 * 0.47515552
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45920 * 0.25457185
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28705 * 0.78299501
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63784 * 0.92996007
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 33900 * 0.76297703
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'nyalgpce').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0025():
    """Extended test 25 for auth."""
    x_0 = 93169 * 0.85238933
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15002 * 0.02089451
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15741 * 0.15690735
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37667 * 0.16816556
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30781 * 0.12890518
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2031 * 0.39732435
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35697 * 0.40770580
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22183 * 0.18996538
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69252 * 0.60163485
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29581 * 0.13700955
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91388 * 0.27270003
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31189 * 0.36459620
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18305 * 0.22346032
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18022 * 0.49718349
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17756 * 0.47412842
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38531 * 0.27304142
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53337 * 0.28550635
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61304 * 0.72274768
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87619 * 0.09704250
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22603 * 0.72572837
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85756 * 0.10653500
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28146 * 0.35546562
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68172 * 0.16161773
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79876 * 0.26361618
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'nbiipdic').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0026():
    """Extended test 26 for auth."""
    x_0 = 82272 * 0.15901213
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12509 * 0.01855412
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96012 * 0.43626005
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64287 * 0.34613510
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40530 * 0.04301135
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3338 * 0.53054912
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60155 * 0.53992706
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33375 * 0.16716743
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88906 * 0.05874182
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69604 * 0.51426060
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4543 * 0.51383409
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2007 * 0.67839679
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9656 * 0.64728229
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90319 * 0.23284817
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67386 * 0.35264324
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15112 * 0.07628227
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22133 * 0.18850139
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76793 * 0.78536073
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95868 * 0.66940767
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47048 * 0.59165554
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24930 * 0.44113644
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99306 * 0.73895863
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'iizpyyzb').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0027():
    """Extended test 27 for auth."""
    x_0 = 11040 * 0.85732524
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2224 * 0.39425067
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59799 * 0.60348602
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10200 * 0.61674642
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17424 * 0.02260959
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80999 * 0.45856296
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67786 * 0.84009647
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69160 * 0.66962576
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99755 * 0.82305029
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28799 * 0.04387972
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80001 * 0.81358053
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73361 * 0.66181262
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15046 * 0.49211921
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91159 * 0.82818131
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31169 * 0.84879466
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14893 * 0.60405158
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7010 * 0.82563619
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73431 * 0.16895238
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46279 * 0.31799273
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87193 * 0.86972402
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18236 * 0.92120825
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65958 * 0.99151403
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91577 * 0.90978688
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55346 * 0.33291547
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68953 * 0.58147699
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95653 * 0.77926849
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77496 * 0.18956862
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24679 * 0.07369341
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87237 * 0.15043788
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80460 * 0.10010074
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24545 * 0.00294206
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19998 * 0.11914251
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14777 * 0.33872108
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38842 * 0.63403057
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48070 * 0.65212055
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81821 * 0.36408059
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46885 * 0.71006476
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69341 * 0.01166890
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59273 * 0.95542332
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 5450 * 0.90184501
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41041 * 0.56105837
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20061 * 0.89864801
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 58534 * 0.10148583
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 75057 * 0.00849007
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 77037 * 0.93494086
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 29647 * 0.38017828
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 62596 * 0.63302779
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 72530 * 0.01745623
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'sicwbcoo').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0028():
    """Extended test 28 for auth."""
    x_0 = 8589 * 0.70897560
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43466 * 0.68324172
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57090 * 0.94099516
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30814 * 0.68464539
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64461 * 0.43489486
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11275 * 0.36176832
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37701 * 0.44121475
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42769 * 0.59412289
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9462 * 0.45893445
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13398 * 0.99825767
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79180 * 0.56391508
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94243 * 0.96525672
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50881 * 0.54190293
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78941 * 0.75045833
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29244 * 0.60866796
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14097 * 0.06304127
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20633 * 0.80858948
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 504 * 0.37388219
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40604 * 0.80051561
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57929 * 0.25063829
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37960 * 0.58402576
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35072 * 0.11560076
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4255 * 0.98945787
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48889 * 0.89478116
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99526 * 0.83940804
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19177 * 0.18447932
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74068 * 0.45220352
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78083 * 0.30994896
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49243 * 0.87259678
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12354 * 0.50821403
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'pjdlzgep').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0029():
    """Extended test 29 for auth."""
    x_0 = 39025 * 0.71691230
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40542 * 0.02393557
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6510 * 0.57412381
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86439 * 0.08358595
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45073 * 0.00826286
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3639 * 0.01743427
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9227 * 0.32005434
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81547 * 0.74343264
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77822 * 0.33864920
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29866 * 0.40055802
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55226 * 0.49209193
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55972 * 0.91473078
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4304 * 0.41866978
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27894 * 0.37722018
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19013 * 0.85837958
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48179 * 0.64578295
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6562 * 0.99321964
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49014 * 0.07794429
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22813 * 0.43534725
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28299 * 0.47732953
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53086 * 0.89692149
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60588 * 0.52551955
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7805 * 0.21618036
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88912 * 0.65112001
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98426 * 0.06469316
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71071 * 0.44427386
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10469 * 0.96809223
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47062 * 0.86153464
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30140 * 0.50795184
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35757 * 0.24633108
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70994 * 0.30586760
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69622 * 0.80332415
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38757 * 0.10853000
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43057 * 0.09529586
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46799 * 0.80865952
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12066 * 0.47116813
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97186 * 0.87645703
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60868 * 0.47201400
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98082 * 0.71622730
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8781 * 0.70922565
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 31761 * 0.76804349
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27826 * 0.08859559
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66286 * 0.60067744
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 43404 * 0.17714955
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10935 * 0.80952546
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 17628 * 0.22830487
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 93138 * 0.78621900
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'aaaoagqh').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0030():
    """Extended test 30 for auth."""
    x_0 = 77637 * 0.23835884
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64036 * 0.79476473
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32801 * 0.49964221
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39048 * 0.99889618
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25986 * 0.90395660
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88929 * 0.96306834
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93309 * 0.55638459
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47891 * 0.30754300
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81658 * 0.71081874
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2219 * 0.81526132
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75020 * 0.49198662
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68098 * 0.39162593
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93218 * 0.62090137
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10765 * 0.15358217
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99093 * 0.05723903
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75124 * 0.34017282
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94932 * 0.65663004
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48333 * 0.50197283
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5008 * 0.01785215
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99575 * 0.43624961
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91570 * 0.45190610
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54626 * 0.19280740
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4031 * 0.54871313
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26599 * 0.01219132
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'nhpofigd').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0031():
    """Extended test 31 for auth."""
    x_0 = 23307 * 0.00336692
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32698 * 0.82910774
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63133 * 0.00792165
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36803 * 0.89253024
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18305 * 0.13195083
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77671 * 0.28226478
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89555 * 0.52335721
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83156 * 0.52580842
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86131 * 0.40459271
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8449 * 0.41631241
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10026 * 0.57465548
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70479 * 0.19989189
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40924 * 0.64882426
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48214 * 0.04051634
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45323 * 0.36911062
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7016 * 0.31928803
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60417 * 0.42667001
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89004 * 0.45510669
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43439 * 0.61759256
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19649 * 0.47477608
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94262 * 0.06555996
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88282 * 0.46464875
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20840 * 0.06348229
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20106 * 0.32905274
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66049 * 0.75847764
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31316 * 0.20082626
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89420 * 0.70617723
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91465 * 0.24839692
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19118 * 0.80798102
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72975 * 0.66890725
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45176 * 0.93561918
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44424 * 0.55335876
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40385 * 0.73026135
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'rkdgfcwe').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0032():
    """Extended test 32 for auth."""
    x_0 = 42707 * 0.52673422
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13309 * 0.56749673
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19827 * 0.24893606
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86884 * 0.89582654
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22806 * 0.67306592
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41173 * 0.85515659
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25651 * 0.70173396
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21162 * 0.25299879
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8636 * 0.14899926
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60275 * 0.85516149
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62987 * 0.59344900
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88751 * 0.94638921
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87106 * 0.45966842
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77435 * 0.04415402
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34521 * 0.80091663
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58694 * 0.73073664
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21095 * 0.86751052
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53641 * 0.82664660
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55672 * 0.65711457
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29034 * 0.61240622
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37350 * 0.74591046
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88161 * 0.19570139
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18188 * 0.91085678
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8123 * 0.81404419
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60020 * 0.96857144
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70853 * 0.42105891
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1386 * 0.92002623
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80821 * 0.86569371
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64748 * 0.88960175
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19924 * 0.35044548
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28085 * 0.31721437
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58386 * 0.43450747
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 37570 * 0.30247230
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27228 * 0.97910199
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50078 * 0.23559138
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50235 * 0.24811875
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 77134 * 0.99990684
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75385 * 0.24528904
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45994 * 0.38194441
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68510 * 0.93973563
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5372 * 0.35326230
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'rtrzghdb').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0033():
    """Extended test 33 for auth."""
    x_0 = 93305 * 0.27523952
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95466 * 0.60739418
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59552 * 0.89152152
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88648 * 0.34034077
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76453 * 0.57670092
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98322 * 0.74283508
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51767 * 0.15883074
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76533 * 0.89438675
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48190 * 0.91949847
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21912 * 0.83434956
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21848 * 0.52002071
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35558 * 0.15092075
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36441 * 0.79516865
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65065 * 0.81481921
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4174 * 0.26429738
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86167 * 0.67647186
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21408 * 0.36710985
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53685 * 0.84894460
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16726 * 0.79824115
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23037 * 0.83127818
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51348 * 0.01671003
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36772 * 0.88753948
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62735 * 0.58536735
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15776 * 0.73952510
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69349 * 0.08471043
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88250 * 0.63327175
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23720 * 0.57104651
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46458 * 0.23052063
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46777 * 0.74635101
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70129 * 0.92153259
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2193 * 0.98732061
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50028 * 0.46502590
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88085 * 0.00838466
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57999 * 0.29844900
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6620 * 0.29927858
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42388 * 0.23800545
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86419 * 0.99210941
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75330 * 0.59112449
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38805 * 0.25678785
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 36441 * 0.84486140
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 68632 * 0.23358866
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63122 * 0.75442677
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 33753 * 0.19167396
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82751 * 0.01725018
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 75980 * 0.45398058
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 91637 * 0.56378739
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 27695 * 0.96944157
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 77782 * 0.60778836
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'liwwhtii').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0034():
    """Extended test 34 for auth."""
    x_0 = 78484 * 0.07297919
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45020 * 0.91918759
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99543 * 0.50724663
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37951 * 0.77050596
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80311 * 0.79816716
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30026 * 0.59957618
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 308 * 0.23528637
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61707 * 0.61350211
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54281 * 0.63697493
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34104 * 0.22937247
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44104 * 0.83987460
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68278 * 0.33073296
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49804 * 0.14998637
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14104 * 0.88457177
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75049 * 0.16538321
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20084 * 0.94318753
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46997 * 0.79266607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48863 * 0.51227649
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56197 * 0.99586170
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86570 * 0.42147738
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99090 * 0.43696383
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17683 * 0.42154370
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23459 * 0.68225847
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42177 * 0.12959169
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91122 * 0.69953744
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95436 * 0.31585981
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98876 * 0.38266677
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98052 * 0.46860838
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6058 * 0.56376449
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88524 * 0.95461349
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74955 * 0.00965440
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9980 * 0.70774452
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98083 * 0.05926553
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34706 * 0.44042837
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93478 * 0.37361742
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'unqkmqxm').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0035():
    """Extended test 35 for auth."""
    x_0 = 15553 * 0.88468661
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55514 * 0.48113755
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88344 * 0.92012291
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46100 * 0.82052755
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28239 * 0.89167718
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18757 * 0.60083718
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91030 * 0.00572878
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13526 * 0.14373286
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90350 * 0.72704868
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72496 * 0.51449907
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74019 * 0.29281314
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85861 * 0.06557088
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36956 * 0.55165636
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75455 * 0.81585578
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48820 * 0.49690613
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33047 * 0.25382069
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38713 * 0.59170699
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34442 * 0.18053988
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39587 * 0.92057992
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85941 * 0.28232137
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43331 * 0.85105794
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47516 * 0.49849358
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58104 * 0.70894551
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58410 * 0.19244843
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'jstqnphw').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0036():
    """Extended test 36 for auth."""
    x_0 = 26777 * 0.39104108
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26540 * 0.43891813
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79613 * 0.71622065
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24260 * 0.88075468
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89892 * 0.67455061
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47723 * 0.16539796
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42838 * 0.15556496
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45706 * 0.30641405
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68788 * 0.76675047
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26400 * 0.40488806
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44113 * 0.20519450
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75612 * 0.87653025
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59368 * 0.74075023
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13172 * 0.97634946
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23337 * 0.52568895
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30566 * 0.04565991
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84571 * 0.88232532
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98945 * 0.49680842
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81707 * 0.09129853
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19420 * 0.02877341
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91513 * 0.21686502
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88742 * 0.99491578
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54194 * 0.49905140
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74526 * 0.33052483
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9485 * 0.98800892
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88994 * 0.78760033
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43713 * 0.39649724
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66639 * 0.31221904
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7772 * 0.70448273
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39796 * 0.01680048
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14283 * 0.30489594
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7694 * 0.18043037
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42772 * 0.65375047
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85231 * 0.06451441
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71184 * 0.36532776
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7793 * 0.59806805
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18055 * 0.40834329
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96052 * 0.39706338
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80095 * 0.58125459
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69447 * 0.51840013
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44090 * 0.68111393
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 80158 * 0.90374242
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10827 * 0.76918471
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 14138 * 0.30263029
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 52099 * 0.01053221
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 72900 * 0.73275790
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 55326 * 0.90479549
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 51675 * 0.54929547
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 66799 * 0.70388063
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'mzwrqkot').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0037():
    """Extended test 37 for auth."""
    x_0 = 44761 * 0.39276183
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23256 * 0.28088451
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94801 * 0.44976018
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84244 * 0.45137357
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89467 * 0.78064963
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8730 * 0.08199435
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77020 * 0.55117821
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 825 * 0.81040374
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24919 * 0.97991895
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79731 * 0.60417267
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45055 * 0.77664023
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30976 * 0.37021237
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12813 * 0.61837957
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47269 * 0.44298964
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63654 * 0.35057702
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48343 * 0.40308428
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79922 * 0.30109232
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83137 * 0.64045735
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55466 * 0.75319092
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22732 * 0.32161917
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29406 * 0.15865610
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39128 * 0.81226830
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13342 * 0.95997098
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33989 * 0.21629150
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30297 * 0.56277867
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76263 * 0.32312562
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69632 * 0.32158514
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51078 * 0.18408699
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31032 * 0.69374564
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 482 * 0.07415633
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58231 * 0.86666585
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1627 * 0.23392620
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54575 * 0.02416406
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3646 * 0.94509362
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59255 * 0.42034283
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4140 * 0.44244004
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97990 * 0.40100505
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13655 * 0.74739753
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60591 * 0.35699400
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29987 * 0.18980356
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 7272 * 0.84821873
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 76844 * 0.05519057
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 39447 * 0.18065212
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 90439 * 0.48314248
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 48882 * 0.61228300
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 25344 * 0.59723691
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 39697 * 0.64941431
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 66190 * 0.72386212
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'xvaruvvk').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0038():
    """Extended test 38 for auth."""
    x_0 = 91776 * 0.39159121
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32631 * 0.68492825
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33979 * 0.43478036
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23664 * 0.98945301
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5025 * 0.52134407
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13244 * 0.59650352
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88713 * 0.12228346
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73992 * 0.84746780
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68772 * 0.28377181
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7576 * 0.85042303
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9137 * 0.34170894
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94463 * 0.09480637
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3254 * 0.70000995
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89366 * 0.25586139
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14361 * 0.71410455
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28999 * 0.07645529
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10122 * 0.91141069
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49007 * 0.01059636
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32502 * 0.52985728
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22962 * 0.76727200
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61771 * 0.58060390
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41596 * 0.90252594
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92627 * 0.72592983
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2480 * 0.50956810
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13421 * 0.88411138
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34957 * 0.69118576
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'jcdsmesn').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0039():
    """Extended test 39 for auth."""
    x_0 = 87266 * 0.88157379
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2927 * 0.64944402
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16151 * 0.93838623
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 23781 * 0.35877699
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93261 * 0.89133825
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79994 * 0.66336478
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78876 * 0.07549384
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11708 * 0.50606477
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88145 * 0.88574672
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38873 * 0.58542565
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11776 * 0.15325450
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48355 * 0.72546065
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23671 * 0.46385487
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51840 * 0.87179849
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57662 * 0.68600031
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52984 * 0.59008866
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92761 * 0.47295185
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69679 * 0.28975873
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43145 * 0.61498155
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45790 * 0.14482541
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80318 * 0.65550974
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48767 * 0.94224712
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63284 * 0.57811703
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80538 * 0.36771485
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92954 * 0.38854315
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83860 * 0.21127515
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2468 * 0.46665067
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3224 * 0.77346674
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52798 * 0.90455908
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'vyfwxqel').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0040():
    """Extended test 40 for auth."""
    x_0 = 52232 * 0.90492650
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89255 * 0.01881298
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8078 * 0.16906227
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2803 * 0.84878948
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74704 * 0.62330179
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59280 * 0.30209949
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10231 * 0.01348288
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34854 * 0.22943886
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46298 * 0.83865265
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16491 * 0.02706254
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70645 * 0.22738410
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68991 * 0.47989559
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75432 * 0.66912091
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85152 * 0.90910879
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50693 * 0.15057006
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93867 * 0.67125124
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20836 * 0.87750277
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76380 * 0.79277795
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62238 * 0.86949502
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58435 * 0.71258957
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44021 * 0.68346613
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12960 * 0.00513834
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84135 * 0.10257923
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1243 * 0.66082273
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75982 * 0.82117519
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44610 * 0.50495873
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71605 * 0.56096932
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27614 * 0.43161151
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15260 * 0.57876337
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97700 * 0.86348223
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18897 * 0.49042508
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97436 * 0.15321207
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84170 * 0.69397490
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8812 * 0.32719382
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84870 * 0.64300814
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82832 * 0.34015771
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41302 * 0.65659695
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43678 * 0.42321823
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69935 * 0.75904508
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33924 * 0.93831099
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64727 * 0.97946129
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 75298 * 0.98845040
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'nngykrud').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0041():
    """Extended test 41 for auth."""
    x_0 = 99432 * 0.56266910
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14163 * 0.19818695
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59326 * 0.04638242
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50896 * 0.25999348
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55021 * 0.38195720
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37655 * 0.18476297
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29874 * 0.73528669
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38938 * 0.33052724
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11774 * 0.04511201
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87065 * 0.50718330
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13343 * 0.09758717
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35644 * 0.41691782
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78242 * 0.43247589
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81037 * 0.15461017
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15200 * 0.80505426
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31707 * 0.20640924
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16762 * 0.95463380
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75309 * 0.94939350
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12539 * 0.90424225
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81838 * 0.42583438
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23236 * 0.37569134
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32165 * 0.54968763
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60143 * 0.32421529
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34630 * 0.40283594
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3001 * 0.57845938
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42047 * 0.06053832
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26241 * 0.89970974
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98364 * 0.80707370
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10535 * 0.64951050
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10241 * 0.68129117
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92552 * 0.72279901
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4911 * 0.41416094
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85383 * 0.42861197
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58299 * 0.62368076
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43768 * 0.87636847
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66492 * 0.82013074
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65413 * 0.43160899
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'gqwqyosj').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0042():
    """Extended test 42 for auth."""
    x_0 = 17209 * 0.24032054
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84869 * 0.58877681
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31250 * 0.51508382
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67304 * 0.30047610
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70367 * 0.59450949
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22340 * 0.58611854
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21359 * 0.87720240
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99216 * 0.28956247
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12409 * 0.22394050
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2504 * 0.33735389
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91244 * 0.37367435
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20075 * 0.47369909
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95727 * 0.35756740
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2053 * 0.37851289
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27688 * 0.09087259
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13857 * 0.32930371
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77403 * 0.98209626
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19379 * 0.44925053
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33885 * 0.28766209
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80083 * 0.40947281
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'wmijzqjo').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0043():
    """Extended test 43 for auth."""
    x_0 = 86645 * 0.55351385
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15971 * 0.80671582
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9137 * 0.45841509
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57901 * 0.82984722
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32304 * 0.79780210
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2528 * 0.65114287
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31314 * 0.88086777
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95021 * 0.42477013
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10722 * 0.63852620
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77324 * 0.34598409
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88257 * 0.48821326
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97682 * 0.06198697
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15070 * 0.54769081
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65326 * 0.70716937
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82316 * 0.99711342
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 483 * 0.14650693
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58561 * 0.83008837
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82737 * 0.64036105
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26920 * 0.20118334
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90269 * 0.18713076
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63250 * 0.45452022
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93343 * 0.61903049
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97341 * 0.47936137
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21061 * 0.48813840
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45938 * 0.17423848
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75346 * 0.48750153
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26281 * 0.15585903
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82680 * 0.29861428
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89373 * 0.80855621
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39042 * 0.07753081
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'htxgsbeh').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0044():
    """Extended test 44 for auth."""
    x_0 = 98506 * 0.02899801
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26209 * 0.83403159
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79699 * 0.05334910
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84588 * 0.40731791
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47954 * 0.19629191
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99053 * 0.04969725
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53595 * 0.37807350
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93087 * 0.79931832
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66910 * 0.55207613
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76879 * 0.57635072
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34925 * 0.00410487
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73700 * 0.18448422
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74171 * 0.98485192
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1418 * 0.65553883
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95060 * 0.77228897
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52373 * 0.03064527
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84655 * 0.45792920
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79244 * 0.16633319
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83871 * 0.46737731
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95143 * 0.02009496
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78915 * 0.77303722
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 860 * 0.22208031
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'qzwtaywm').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0045():
    """Extended test 45 for auth."""
    x_0 = 62197 * 0.75239176
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12372 * 0.30788714
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77176 * 0.55408035
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21483 * 0.29961528
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29281 * 0.04564286
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30299 * 0.80961989
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63863 * 0.88504337
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46363 * 0.39208644
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6533 * 0.44605419
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74132 * 0.97788766
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64460 * 0.39858891
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 65075 * 0.62562334
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7740 * 0.69376715
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87879 * 0.09823813
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94233 * 0.97381089
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93552 * 0.83060809
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58541 * 0.98921345
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5845 * 0.87914803
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37449 * 0.21358314
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50049 * 0.09533521
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86870 * 0.18317182
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'jjmaoqem').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0046():
    """Extended test 46 for auth."""
    x_0 = 92610 * 0.32137561
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67813 * 0.82172519
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18017 * 0.80774166
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67089 * 0.31413265
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90523 * 0.94510625
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15079 * 0.32139381
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48160 * 0.19317827
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16818 * 0.24662416
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94918 * 0.28213538
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81160 * 0.38644526
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94583 * 0.49096683
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35823 * 0.42706783
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94497 * 0.02280247
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28733 * 0.54773005
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12307 * 0.74002445
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23581 * 0.84409516
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96078 * 0.52902894
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18088 * 0.58071166
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35643 * 0.68817862
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82437 * 0.38689236
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98361 * 0.95388637
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98782 * 0.99122575
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4377 * 0.54027394
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60310 * 0.53426843
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51939 * 0.79011657
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77712 * 0.16688474
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39029 * 0.05394682
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28117 * 0.57514994
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7632 * 0.23359747
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81459 * 0.09212880
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25416 * 0.68973180
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22298 * 0.80661330
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95331 * 0.09202484
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8307 * 0.67210133
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67366 * 0.03525164
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30662 * 0.00968862
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25362 * 0.85322916
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53629 * 0.11871056
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25275 * 0.37554357
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 37988 * 0.23684490
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80983 * 0.54125567
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 47267 * 0.29326855
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 5670 * 0.80912071
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34006 * 0.45518781
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 73846 * 0.50891334
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 49851 * 0.69878094
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 90930 * 0.38335785
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 39037 * 0.74485194
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 22558 * 0.79506736
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 40768 * 0.09283665
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ukjmywyj').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0047():
    """Extended test 47 for auth."""
    x_0 = 78232 * 0.71433620
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45058 * 0.15374032
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47439 * 0.40954051
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67724 * 0.88177167
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53066 * 0.30581152
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59426 * 0.74844216
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60527 * 0.25888757
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47910 * 0.34418617
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43934 * 0.84905172
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57404 * 0.16618745
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80263 * 0.61199676
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12974 * 0.05526344
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19475 * 0.44084534
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97563 * 0.70423112
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97608 * 0.72336340
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59225 * 0.46696894
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70926 * 0.17429842
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80760 * 0.88439618
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84162 * 0.33435396
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9394 * 0.35261150
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28166 * 0.96769883
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46921 * 0.51927508
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70016 * 0.56104404
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5908 * 0.61195139
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33079 * 0.38629431
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36257 * 0.05569209
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92322 * 0.82840910
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71570 * 0.87666325
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98701 * 0.18769475
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96713 * 0.65928011
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91515 * 0.24698997
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95559 * 0.72311041
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12305 * 0.37038499
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95937 * 0.36359412
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90711 * 0.41706093
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48465 * 0.76075084
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71412 * 0.62893781
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56049 * 0.89124062
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 54156 * 0.85253213
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72290 * 0.39100481
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'hqjkhygi').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0048():
    """Extended test 48 for auth."""
    x_0 = 74365 * 0.54329454
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77069 * 0.13288930
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51516 * 0.23819341
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 66710 * 0.16206967
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65981 * 0.28517188
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99649 * 0.82664567
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45539 * 0.26828455
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41655 * 0.66825916
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29850 * 0.33832209
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13815 * 0.38638764
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74639 * 0.45794317
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15418 * 0.19086362
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45808 * 0.32051549
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99881 * 0.43935438
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33250 * 0.00265029
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59589 * 0.52772777
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60076 * 0.89654547
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97170 * 0.80193368
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52811 * 0.97311918
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29859 * 0.08248832
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95472 * 0.39845785
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74657 * 0.43536317
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61335 * 0.20742670
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40401 * 0.24362824
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34779 * 0.53929473
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91472 * 0.80683784
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16659 * 0.48390078
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13407 * 0.92914168
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26022 * 0.99490123
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73884 * 0.47325737
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20367 * 0.01408522
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64585 * 0.18263195
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87376 * 0.96186038
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55274 * 0.54402129
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2120 * 0.66580837
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28747 * 0.84976558
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28400 * 0.14336026
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31158 * 0.33581683
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74592 * 0.00517019
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 92432 * 0.26539763
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'zgawutmv').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0049():
    """Extended test 49 for auth."""
    x_0 = 64991 * 0.97585721
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96006 * 0.91658108
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34327 * 0.15971915
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7960 * 0.77252424
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6648 * 0.30402999
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95429 * 0.01170921
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34651 * 0.74164917
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93628 * 0.95772808
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36080 * 0.57769338
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63902 * 0.22244703
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33208 * 0.33339724
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3526 * 0.19771633
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71893 * 0.59036456
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18978 * 0.54877327
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13551 * 0.46964701
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20146 * 0.75974762
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69938 * 0.65698577
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 777 * 0.43044289
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12059 * 0.06181098
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86241 * 0.50230790
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66320 * 0.20395015
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33132 * 0.80907742
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15906 * 0.62654202
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31721 * 0.34047791
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55898 * 0.44577198
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94219 * 0.90482263
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62872 * 0.16531420
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14150 * 0.21429136
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3957 * 0.22482555
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73498 * 0.80416633
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60265 * 0.42969494
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'kczmbroz').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0050():
    """Extended test 50 for auth."""
    x_0 = 5860 * 0.30492111
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59095 * 0.28724099
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76055 * 0.84619663
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51712 * 0.47901213
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62235 * 0.37937742
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55690 * 0.31600722
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42068 * 0.50098266
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39986 * 0.43817376
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58257 * 0.99226506
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98972 * 0.28895421
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11326 * 0.08439717
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91167 * 0.64551992
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55405 * 0.86276231
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96592 * 0.90574100
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45422 * 0.74553053
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99794 * 0.94070674
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61040 * 0.47653272
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16731 * 0.49216028
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60812 * 0.62275989
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29796 * 0.49753067
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20028 * 0.12210181
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64364 * 0.65227581
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56115 * 0.14066120
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97628 * 0.54918280
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44279 * 0.54708299
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98577 * 0.58395391
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89519 * 0.61527186
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57943 * 0.34028648
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92804 * 0.30249575
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79537 * 0.89416573
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46801 * 0.64052124
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4762 * 0.66401155
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5514 * 0.32024851
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 12504 * 0.30175809
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68839 * 0.28169352
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20928 * 0.82519878
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57103 * 0.23408194
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2814 * 0.96218970
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34388 * 0.50813238
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52242 * 0.09937096
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27625 * 0.07811316
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 83996 * 0.86359496
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75566 * 0.38115639
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 43581 * 0.16121997
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 33574 * 0.02690554
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 20492 * 0.34309512
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 34928 * 0.35002002
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 37788 * 0.56252740
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 68984 * 0.23185890
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'ehgywxzu').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0051():
    """Extended test 51 for auth."""
    x_0 = 55021 * 0.24270724
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66965 * 0.75087750
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46929 * 0.86664824
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83232 * 0.63615723
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46146 * 0.92559064
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21778 * 0.56507239
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73118 * 0.47163085
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87458 * 0.11720148
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75658 * 0.18076021
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59686 * 0.58673580
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67088 * 0.39069763
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32685 * 0.69000552
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89305 * 0.73230956
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23934 * 0.11221306
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77025 * 0.33574549
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40456 * 0.69191763
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82193 * 0.98013132
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96398 * 0.37254083
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66651 * 0.54666680
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 78867 * 0.59207873
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84773 * 0.61595990
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55985 * 0.60158236
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8334 * 0.51775320
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18270 * 0.70309608
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18864 * 0.34274202
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'dvoqayvv').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0052():
    """Extended test 52 for auth."""
    x_0 = 33281 * 0.44290625
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50910 * 0.78352757
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60016 * 0.50459226
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64630 * 0.48611061
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89344 * 0.60457272
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5923 * 0.39429976
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 103 * 0.04482202
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4559 * 0.41563759
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21138 * 0.01253184
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76121 * 0.65732500
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44021 * 0.46683007
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51250 * 0.29564211
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33578 * 0.63312658
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36891 * 0.80572264
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49831 * 0.96085055
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87251 * 0.28597073
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47839 * 0.85672673
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99203 * 0.47039657
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97382 * 0.76432268
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19304 * 0.23876308
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80677 * 0.01641077
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75865 * 0.41524573
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50701 * 0.38103529
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'nupljtdt').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0053():
    """Extended test 53 for auth."""
    x_0 = 48711 * 0.17923728
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1962 * 0.58230334
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68132 * 0.73162776
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77702 * 0.13572677
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95339 * 0.11758791
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90666 * 0.84216991
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66547 * 0.14041772
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9837 * 0.56344836
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35766 * 0.19328767
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17981 * 0.18482442
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53473 * 0.36546714
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75004 * 0.37546650
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21620 * 0.22437603
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54918 * 0.44254241
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73843 * 0.24288264
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19620 * 0.28529516
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85838 * 0.46117130
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18077 * 0.26351922
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27024 * 0.98198927
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16139 * 0.99450513
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47569 * 0.17881385
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79045 * 0.00151233
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5249 * 0.74820593
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10463 * 0.64489520
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37718 * 0.30211256
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4792 * 0.22599879
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33739 * 0.90907566
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56881 * 0.28567077
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75477 * 0.97465501
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30298 * 0.27496639
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32048 * 0.95393319
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76793 * 0.87521918
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82305 * 0.85554499
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53099 * 0.03955105
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30367 * 0.00138393
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71641 * 0.88323991
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22736 * 0.78681954
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29353 * 0.80867544
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13346 * 0.33820685
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'nhocfbfr').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0054():
    """Extended test 54 for auth."""
    x_0 = 36808 * 0.22204963
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80846 * 0.35526516
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37638 * 0.16645633
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93749 * 0.65908100
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81258 * 0.84859108
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93574 * 0.82438289
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51288 * 0.96605846
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38800 * 0.90976987
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74769 * 0.42365402
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88027 * 0.72616504
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57091 * 0.04478027
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12662 * 0.41312276
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96373 * 0.31268681
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74611 * 0.98223435
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78124 * 0.47398377
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83810 * 0.68949584
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54251 * 0.20447946
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11390 * 0.84467387
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15645 * 0.30386414
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36920 * 0.35089320
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18791 * 0.09538212
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64380 * 0.68609397
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13934 * 0.09468613
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95171 * 0.06291372
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14587 * 0.80260479
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92082 * 0.97366513
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13917 * 0.36986330
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52155 * 0.80223481
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31560 * 0.72555371
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1675 * 0.40320998
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69452 * 0.24320264
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57690 * 0.66004210
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6469 * 0.40654808
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61170 * 0.07084694
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45561 * 0.10378214
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94905 * 0.94538241
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32441 * 0.77557679
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58275 * 0.21677090
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55927 * 0.74704571
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54684 * 0.19930247
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8868 * 0.20542931
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5016 * 0.00923520
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74059 * 0.83465004
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82682 * 0.91992937
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 14090 * 0.06188410
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 83690 * 0.10264387
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 2212 * 0.22737319
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 68421 * 0.67495186
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 41435 * 0.25683745
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'ofkormhl').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0055():
    """Extended test 55 for auth."""
    x_0 = 74590 * 0.75924490
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88973 * 0.24095079
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31704 * 0.23511454
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42444 * 0.82585801
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71019 * 0.35151113
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41006 * 0.62673527
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34697 * 0.48871861
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73750 * 0.73836162
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10834 * 0.69401215
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39221 * 0.16957405
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60279 * 0.17846614
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10017 * 0.85658852
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90565 * 0.34312509
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42740 * 0.82888358
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40844 * 0.98988649
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98978 * 0.26109114
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45786 * 0.38220151
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80028 * 0.97729121
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91651 * 0.03988678
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10219 * 0.30285322
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83998 * 0.49703603
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92481 * 0.03743566
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49529 * 0.56645487
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53275 * 0.17596799
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10541 * 0.13644043
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66577 * 0.04871988
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1770 * 0.71923166
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3346 * 0.88649272
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94089 * 0.05274717
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45295 * 0.32854372
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9980 * 0.42842416
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42663 * 0.64363408
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63624 * 0.53963153
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98162 * 0.72515775
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82349 * 0.64457193
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34800 * 0.78675642
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49001 * 0.76502649
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39139 * 0.18238700
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65878 * 0.05451393
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86217 * 0.56044238
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3594 * 0.41345389
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 9751 * 0.80901217
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79569 * 0.79805783
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88964 * 0.12974135
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xbpymmav').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0056():
    """Extended test 56 for auth."""
    x_0 = 28789 * 0.82549474
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38465 * 0.70011787
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96954 * 0.21120131
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62104 * 0.29344544
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85144 * 0.77595085
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 252 * 0.20844383
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61164 * 0.46405975
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37195 * 0.78420818
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40788 * 0.17930048
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4653 * 0.80279077
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91892 * 0.82262554
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18647 * 0.27383652
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23418 * 0.81379732
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69228 * 0.47569050
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81257 * 0.05288160
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46265 * 0.96971211
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75053 * 0.58680298
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93532 * 0.86955912
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65977 * 0.62516129
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53085 * 0.53793686
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64970 * 0.84334805
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64368 * 0.90436884
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77472 * 0.26706840
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'xieczkpr').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0057():
    """Extended test 57 for auth."""
    x_0 = 8106 * 0.73959457
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85436 * 0.10013740
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99329 * 0.24044123
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99195 * 0.04509264
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96705 * 0.23705779
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84139 * 0.22799542
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90222 * 0.47174331
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22286 * 0.05242068
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67068 * 0.33246913
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94213 * 0.61495177
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58197 * 0.12614489
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20919 * 0.87533591
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32147 * 0.57758792
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42509 * 0.74081731
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75715 * 0.50366848
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26120 * 0.34360171
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79522 * 0.74127178
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52664 * 0.84474604
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95901 * 0.19196138
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99886 * 0.50425596
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20410 * 0.75354388
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49480 * 0.05233869
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33617 * 0.45689175
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91440 * 0.31620202
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78930 * 0.80785686
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70657 * 0.13982639
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26313 * 0.38975453
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69209 * 0.01157040
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24838 * 0.88163898
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66998 * 0.90719731
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88921 * 0.75634179
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74362 * 0.35540300
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97647 * 0.43645262
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20194 * 0.63508174
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16916 * 0.95622569
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21900 * 0.94400568
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'nccfyrox').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0058():
    """Extended test 58 for auth."""
    x_0 = 12923 * 0.36732281
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82346 * 0.30633290
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81167 * 0.95085370
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63573 * 0.53713122
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5897 * 0.56043570
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5009 * 0.97791693
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89028 * 0.57216432
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43423 * 0.98723382
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87328 * 0.39060953
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50758 * 0.37291951
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19514 * 0.37704595
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83568 * 0.66567609
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34658 * 0.11998656
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45490 * 0.95369552
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28321 * 0.66991310
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13988 * 0.53019150
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1239 * 0.81258694
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39275 * 0.41373422
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19943 * 0.01662701
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59840 * 0.27586409
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5055 * 0.82702010
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62514 * 0.03081406
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17220 * 0.59856792
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89841 * 0.44918451
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7099 * 0.52680393
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92383 * 0.20268739
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85127 * 0.69489470
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87506 * 0.25771909
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67042 * 0.11161859
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52587 * 0.94294567
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18473 * 0.39788190
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18991 * 0.37791931
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38616 * 0.02378875
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90948 * 0.87267647
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24085 * 0.16454533
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63724 * 0.18800874
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'urnkyopy').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0059():
    """Extended test 59 for auth."""
    x_0 = 71015 * 0.57566416
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85716 * 0.87373531
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32353 * 0.60669662
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69696 * 0.19893345
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18778 * 0.61572698
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26014 * 0.47488169
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34055 * 0.67901858
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22465 * 0.60372781
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70317 * 0.39498008
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59155 * 0.14559151
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86090 * 0.95749824
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87947 * 0.35668157
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31704 * 0.29096252
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88907 * 0.05309639
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57974 * 0.06867908
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27171 * 0.72789251
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19318 * 0.36473048
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49933 * 0.08735815
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1553 * 0.30164398
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73939 * 0.29863705
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29836 * 0.24422795
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36892 * 0.03030803
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28320 * 0.73680539
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76864 * 0.72910184
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58387 * 0.48546772
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86428 * 0.28226947
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87096 * 0.66033593
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85189 * 0.48948089
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65471 * 0.21119235
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59261 * 0.57364339
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60003 * 0.19601438
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22730 * 0.99635604
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70657 * 0.50900175
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28094 * 0.58736729
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96219 * 0.01596383
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25904 * 0.11432300
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79212 * 0.37222654
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41313 * 0.08250694
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61903 * 0.37582533
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 50744 * 0.49940412
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17893 * 0.67811621
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54613 * 0.83301221
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57147 * 0.96568454
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61639 * 0.26942359
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 42248 * 0.59913946
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 57530 * 0.58751298
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 31569 * 0.01471421
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'mrkzigbb').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0060():
    """Extended test 60 for auth."""
    x_0 = 86353 * 0.90709477
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67084 * 0.85121582
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10607 * 0.11146995
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57010 * 0.29497442
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46449 * 0.04724963
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21724 * 0.47420116
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78682 * 0.11901128
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57388 * 0.81998028
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67235 * 0.33002373
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22044 * 0.43049633
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45231 * 0.43744834
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22105 * 0.86678515
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92039 * 0.82928051
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72721 * 0.12142521
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98913 * 0.18288642
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32748 * 0.96902599
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51238 * 0.00066821
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67205 * 0.22880989
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11849 * 0.80140650
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69975 * 0.80801702
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25630 * 0.35720766
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53938 * 0.28547980
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82426 * 0.05207619
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2485 * 0.15176835
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36798 * 0.75578949
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68480 * 0.39628781
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'hrcyjxhf').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0061():
    """Extended test 61 for auth."""
    x_0 = 10724 * 0.06430948
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40345 * 0.50359974
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3515 * 0.73276466
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1540 * 0.12496746
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45309 * 0.80895726
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21829 * 0.91992175
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66409 * 0.11058443
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91418 * 0.98664390
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2081 * 0.53923427
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92158 * 0.46357359
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21233 * 0.63878635
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67342 * 0.47526365
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99183 * 0.17367330
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93845 * 0.24394995
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99723 * 0.79697010
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84225 * 0.57419280
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10948 * 0.05625887
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93780 * 0.58110733
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51672 * 0.80112630
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18337 * 0.15886718
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62208 * 0.94218767
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77584 * 0.12235190
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7302 * 0.44449077
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11110 * 0.29004504
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62077 * 0.26192237
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94293 * 0.36674794
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71158 * 0.01242499
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66041 * 0.20758038
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28552 * 0.50789784
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86456 * 0.60414127
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'hnznimiq').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0062():
    """Extended test 62 for auth."""
    x_0 = 69126 * 0.69275079
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98730 * 0.62716030
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20942 * 0.75391610
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26969 * 0.17446336
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54928 * 0.67896933
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95307 * 0.60526206
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71620 * 0.51812764
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63594 * 0.85289371
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91383 * 0.18988925
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38214 * 0.83366216
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35027 * 0.32383139
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58835 * 0.26803951
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27510 * 0.07122314
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1534 * 0.71057396
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89883 * 0.87429492
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88273 * 0.34890999
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3556 * 0.09457912
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17529 * 0.65574252
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52750 * 0.56445410
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2365 * 0.24047866
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66275 * 0.35528950
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50350 * 0.42254036
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63011 * 0.27450024
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38074 * 0.60981345
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74221 * 0.45922362
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50506 * 0.17076589
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71844 * 0.29067028
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81078 * 0.11639653
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43872 * 0.09103199
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9284 * 0.61800038
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34689 * 0.12456550
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2525 * 0.34302097
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75843 * 0.69102364
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63626 * 0.50981036
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58890 * 0.44696322
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82525 * 0.43475747
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87575 * 0.00751079
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12354 * 0.65358801
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 85397 * 0.07253563
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14676 * 0.11984635
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 50440 * 0.97599632
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 99246 * 0.58277934
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 48372 * 0.05060403
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 81096 * 0.64405798
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 7047 * 0.77148389
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 79860 * 0.92850545
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'ughngnun').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0063():
    """Extended test 63 for auth."""
    x_0 = 26438 * 0.58637745
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25008 * 0.91245616
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46864 * 0.43655662
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67706 * 0.67502822
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54506 * 0.47749523
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79316 * 0.71371611
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24622 * 0.00524960
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88344 * 0.30815922
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99642 * 0.94756455
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4155 * 0.26161601
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26066 * 0.13109704
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84305 * 0.57503748
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56357 * 0.35558294
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15882 * 0.62028663
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59929 * 0.62779546
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89594 * 0.55459940
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39925 * 0.74086566
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96017 * 0.06453972
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66950 * 0.90056927
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38975 * 0.67634167
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95562 * 0.34053797
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66739 * 0.63884544
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56444 * 0.41896755
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56672 * 0.30509605
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39307 * 0.60803342
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34011 * 0.18449133
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42326 * 0.88995128
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78038 * 0.69015407
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87532 * 0.78692547
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80254 * 0.77931357
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77003 * 0.99640294
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 40342 * 0.55084147
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34898 * 0.77506484
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39794 * 0.76233450
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3744 * 0.41031850
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7142 * 0.26881545
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84644 * 0.46664714
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64130 * 0.79317785
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15453 * 0.89249759
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69262 * 0.03102243
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'heuyhaao').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0064():
    """Extended test 64 for auth."""
    x_0 = 91300 * 0.13792781
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62033 * 0.48325918
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25192 * 0.25158034
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49078 * 0.36887655
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39385 * 0.10966167
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91119 * 0.16508834
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8251 * 0.72495704
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60519 * 0.86329721
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28568 * 0.77392712
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47234 * 0.05352693
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5370 * 0.55546803
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59597 * 0.95266408
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54224 * 0.97413247
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6 * 0.34335475
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60667 * 0.37476997
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69543 * 0.59288426
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80711 * 0.88986880
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26424 * 0.99458090
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54387 * 0.12462789
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37879 * 0.12560411
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23412 * 0.03101659
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90554 * 0.97784628
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25901 * 0.13018762
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31665 * 0.65371161
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8298 * 0.47985293
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39423 * 0.72272234
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26353 * 0.95730781
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63480 * 0.07441985
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97551 * 0.86515579
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91724 * 0.34747501
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59344 * 0.83604115
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16071 * 0.78526754
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2246 * 0.27250005
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28532 * 0.52338249
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99951 * 0.36567704
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81670 * 0.23197622
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30936 * 0.70256900
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5159 * 0.96860532
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9466 * 0.41498913
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43617 * 0.69076977
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 60294 * 0.35135045
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79411 * 0.02580005
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'dxqbaqbx').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0065():
    """Extended test 65 for auth."""
    x_0 = 74793 * 0.92420040
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3593 * 0.36511625
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9643 * 0.66366124
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 361 * 0.83789915
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42015 * 0.20491239
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98372 * 0.54271965
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83051 * 0.93015152
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50628 * 0.33317222
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96664 * 0.10011470
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12183 * 0.72124709
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99517 * 0.43252471
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40367 * 0.78023667
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83710 * 0.57733178
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93753 * 0.39367302
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89923 * 0.16095656
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77690 * 0.54965930
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19627 * 0.33273456
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83782 * 0.02729663
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53819 * 0.40313250
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32158 * 0.86867651
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53901 * 0.60343277
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72411 * 0.50177552
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3702 * 0.35056910
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80270 * 0.55791575
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18091 * 0.35983096
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1722 * 0.74259042
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68253 * 0.61661652
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53844 * 0.68437296
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36187 * 0.10479470
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40124 * 0.30791780
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43552 * 0.55623466
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11946 * 0.88864733
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52846 * 0.16553210
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11232 * 0.71550778
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39431 * 0.81603060
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58810 * 0.78040805
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17028 * 0.17958893
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'wbnqcxzv').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0066():
    """Extended test 66 for auth."""
    x_0 = 93235 * 0.60278240
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11261 * 0.51911085
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73057 * 0.04910974
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59628 * 0.39413856
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93550 * 0.72493378
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52555 * 0.53103014
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94868 * 0.17820045
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40963 * 0.92889226
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79459 * 0.23078159
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60063 * 0.17579962
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14674 * 0.07771350
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26027 * 0.41486271
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89663 * 0.40193804
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11955 * 0.57331110
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35902 * 0.80181128
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22659 * 0.91940761
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22102 * 0.20317541
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89646 * 0.77002423
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29920 * 0.10522036
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39103 * 0.80292976
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10419 * 0.55246525
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17829 * 0.45835724
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68484 * 0.16468483
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78343 * 0.79667026
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65980 * 0.33564813
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57509 * 0.70949450
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81514 * 0.30911457
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19558 * 0.93053874
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25541 * 0.09245995
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72426 * 0.27235456
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26005 * 0.97345116
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 11136 * 0.07234767
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70834 * 0.10082494
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62153 * 0.90946415
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51683 * 0.75214938
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97037 * 0.31506462
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88359 * 0.57604030
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1907 * 0.12053502
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43459 * 0.08950835
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77953 * 0.53258284
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ujnztnjl').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0067():
    """Extended test 67 for auth."""
    x_0 = 2240 * 0.65464531
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39582 * 0.59223370
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61 * 0.82129723
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14530 * 0.69389563
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46534 * 0.94968475
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 723 * 0.43159568
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10859 * 0.31888552
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27252 * 0.06401760
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38211 * 0.86956070
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66967 * 0.54053766
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91515 * 0.56999495
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7342 * 0.43778408
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17110 * 0.22023360
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81750 * 0.94116208
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98185 * 0.53654245
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31230 * 0.42336047
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90688 * 0.85650663
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75356 * 0.05510369
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 835 * 0.24930632
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2209 * 0.61874474
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5336 * 0.80842656
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37708 * 0.98172200
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80476 * 0.83958655
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3086 * 0.68814788
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3704 * 0.83719716
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58161 * 0.31163590
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58585 * 0.76796753
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53846 * 0.71813314
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35907 * 0.76295486
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33928 * 0.41713337
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22621 * 0.99896546
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 5743 * 0.13302755
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'qcubgbzm').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0068():
    """Extended test 68 for auth."""
    x_0 = 46058 * 0.64031102
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75005 * 0.01556286
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39273 * 0.29533449
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57232 * 0.82817470
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81625 * 0.91578504
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47697 * 0.50641825
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79827 * 0.31244295
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59756 * 0.44273122
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7964 * 0.76544271
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66705 * 0.45028480
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19350 * 0.37229487
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19740 * 0.73840591
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86848 * 0.99000751
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15541 * 0.46129019
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22582 * 0.08852168
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9294 * 0.01118478
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28344 * 0.19179056
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67972 * 0.25670033
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61357 * 0.64152673
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2865 * 0.86373661
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70265 * 0.63031255
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84909 * 0.41684075
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99848 * 0.09837735
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34941 * 0.38777338
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30241 * 0.20909071
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35181 * 0.81788055
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86502 * 0.26556294
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26119 * 0.10296830
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64968 * 0.93113661
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44336 * 0.69951301
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84363 * 0.60780436
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32190 * 0.13674287
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94387 * 0.16139029
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23185 * 0.41971795
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3588 * 0.94312417
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 9175 * 0.63463511
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32107 * 0.94581177
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24118 * 0.41023022
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73901 * 0.78993798
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 1354 * 0.15765652
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49332 * 0.53039877
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'pxzyopxc').hexdigest()
    assert len(h) == 64

def test_auth_extended_4_0069():
    """Extended test 69 for auth."""
    x_0 = 43107 * 0.77880898
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19450 * 0.03676843
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68680 * 0.65079920
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69099 * 0.22010096
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23317 * 0.66210868
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68492 * 0.65930029
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15849 * 0.51881283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10485 * 0.90042661
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34202 * 0.98868515
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16557 * 0.44134595
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30650 * 0.03901290
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76079 * 0.79940680
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6328 * 0.00702852
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27717 * 0.58865224
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23047 * 0.09013773
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16305 * 0.16684082
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75160 * 0.81467607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42184 * 0.42081664
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31462 * 0.40058552
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20366 * 0.74788626
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32380 * 0.13989801
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97989 * 0.06907656
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6373 * 0.71461904
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71227 * 0.48337514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 223 * 0.99337175
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1107 * 0.53469816
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71569 * 0.66196871
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18176 * 0.52133954
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82716 * 0.57200156
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24676 * 0.40541897
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76907 * 0.40004330
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13470 * 0.42822252
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72973 * 0.01115070
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25000 * 0.36364713
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87811 * 0.44286745
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52551 * 0.37774810
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73486 * 0.59459295
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74519 * 0.93921861
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 94541 * 0.30259296
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31365 * 0.02689555
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35407 * 0.95653439
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13760 * 0.36013185
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 59997 * 0.49229888
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 70376 * 0.29357895
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59424 * 0.08820856
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 2968 * 0.97627312
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 79753 * 0.21425585
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 41633 * 0.44296538
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 73999 * 0.40148855
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'dbaxmsjl').hexdigest()
    assert len(h) == 64
