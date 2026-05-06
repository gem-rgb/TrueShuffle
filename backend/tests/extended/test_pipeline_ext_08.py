"""Extended tests for pipeline suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_pipeline_extended_8_0000():
    """Extended test 0 for pipeline."""
    x_0 = 79622 * 0.14489212
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31089 * 0.64177473
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4973 * 0.80116080
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83363 * 0.74387821
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26628 * 0.09176415
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28387 * 0.49773664
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45611 * 0.21505973
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99834 * 0.13716554
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19841 * 0.47078276
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63104 * 0.26425110
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75687 * 0.63136110
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84230 * 0.27485851
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1210 * 0.40739191
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75388 * 0.08162626
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50123 * 0.45572928
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17096 * 0.67946514
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76166 * 0.40417097
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52553 * 0.93085173
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43345 * 0.20537107
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58343 * 0.71418454
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35899 * 0.95251474
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28439 * 0.10101856
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67254 * 0.22107332
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78000 * 0.27015372
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56992 * 0.42810973
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35296 * 0.24966424
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22740 * 0.74186935
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6929 * 0.95068944
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15818 * 0.90336560
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79996 * 0.93162092
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92664 * 0.38879304
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83314 * 0.58111889
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36930 * 0.09571403
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35856 * 0.38902558
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 49657 * 0.02590735
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'rkonskrs').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0001():
    """Extended test 1 for pipeline."""
    x_0 = 75511 * 0.70361382
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9417 * 0.11495544
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35218 * 0.35799941
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50367 * 0.22873443
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46440 * 0.45368675
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55118 * 0.00072992
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11251 * 0.39329456
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41544 * 0.42723206
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34467 * 0.17697747
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42229 * 0.73429831
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54612 * 0.91898928
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94273 * 0.59393433
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77788 * 0.88553961
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10281 * 0.96340962
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61747 * 0.09774852
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83576 * 0.89767744
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38494 * 0.53576045
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32721 * 0.31875530
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51494 * 0.02340199
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6870 * 0.08124535
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32437 * 0.28413825
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38393 * 0.91391798
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68862 * 0.62912770
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30918 * 0.64904864
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72527 * 0.04660275
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50320 * 0.39657205
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36008 * 0.52383863
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12734 * 0.36323766
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70224 * 0.09167619
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69976 * 0.29437605
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75136 * 0.59442876
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90418 * 0.50344800
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42848 * 0.50219705
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62423 * 0.46570596
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12385 * 0.58512371
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1950 * 0.76098056
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84060 * 0.43330997
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97982 * 0.72008830
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14510 * 0.63315645
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 15163 * 0.79750262
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32116 * 0.95871295
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 34527 * 0.86265654
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 86952 * 0.84146322
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99799 * 0.74814907
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 6370 * 0.98245802
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'pxfmocez').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0002():
    """Extended test 2 for pipeline."""
    x_0 = 70981 * 0.03025291
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94029 * 0.74407684
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19066 * 0.51916585
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73754 * 0.43188539
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81288 * 0.11705319
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63766 * 0.30602337
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64170 * 0.59401011
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41385 * 0.91927153
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 55755 * 0.16061083
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28127 * 0.87646493
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31342 * 0.83266851
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68611 * 0.75489796
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1464 * 0.59594487
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98981 * 0.66366165
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51046 * 0.52780516
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23515 * 0.42349681
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54941 * 0.96757031
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34493 * 0.86342185
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85450 * 0.71303758
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97076 * 0.81608673
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10335 * 0.13901299
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94445 * 0.26770975
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'nlmuocgw').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0003():
    """Extended test 3 for pipeline."""
    x_0 = 9535 * 0.64230437
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1268 * 0.93885164
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63463 * 0.39376264
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71824 * 0.38261120
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48685 * 0.71243548
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96342 * 0.52442759
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10753 * 0.72306912
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93037 * 0.52360693
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17405 * 0.45875064
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77271 * 0.24997661
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10073 * 0.43590883
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17611 * 0.01830780
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68468 * 0.91172585
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10235 * 0.85444689
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61649 * 0.04922375
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92313 * 0.80347478
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99418 * 0.63898706
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58988 * 0.84945688
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59328 * 0.06938101
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12883 * 0.08781945
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63919 * 0.25366538
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20650 * 0.42315379
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69178 * 0.61717026
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9463 * 0.24613239
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26931 * 0.65851279
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92955 * 0.33122664
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96238 * 0.64939112
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51570 * 0.13617667
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83380 * 0.74090797
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67740 * 0.06167032
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92166 * 0.95556860
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93658 * 0.66791639
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'fyvqgcmy').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0004():
    """Extended test 4 for pipeline."""
    x_0 = 62383 * 0.15672268
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43328 * 0.24961244
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19529 * 0.71737956
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8340 * 0.95687499
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69757 * 0.20885478
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89144 * 0.76395841
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44393 * 0.37913660
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87840 * 0.20925422
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83694 * 0.61362574
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17718 * 0.62588832
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 980 * 0.37361619
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61418 * 0.35299157
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25034 * 0.08843962
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8927 * 0.71608909
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24745 * 0.79340374
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65479 * 0.48171693
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36092 * 0.97041446
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14971 * 0.16636322
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71604 * 0.80909616
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93412 * 0.86630226
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21266 * 0.16168133
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70519 * 0.11069956
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13078 * 0.87563356
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86375 * 0.74680448
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58547 * 0.47480189
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48145 * 0.94244021
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32738 * 0.10648445
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14821 * 0.52520880
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28846 * 0.31714370
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47998 * 0.60987009
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18701 * 0.58808526
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9342 * 0.91104950
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1404 * 0.77930108
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84862 * 0.08541741
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51142 * 0.30547183
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98076 * 0.84557416
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36559 * 0.78577652
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67154 * 0.01049525
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59740 * 0.39860686
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70034 * 0.21386660
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 96745 * 0.64309017
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42409 * 0.17742639
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23043 * 0.35571371
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36319 * 0.57979508
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 99691 * 0.33168028
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 83222 * 0.43529183
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 71646 * 0.77200835
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 8588 * 0.90933902
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ctdjaqln').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0005():
    """Extended test 5 for pipeline."""
    x_0 = 11091 * 0.91553900
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80977 * 0.90882322
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18416 * 0.16400698
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18721 * 0.48035328
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55898 * 0.09816025
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18015 * 0.25550156
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53016 * 0.97663997
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3199 * 0.94488930
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50968 * 0.07189252
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74562 * 0.67240785
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13235 * 0.28959412
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15150 * 0.74746556
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69636 * 0.03587592
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66721 * 0.96232557
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25300 * 0.93477287
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20416 * 0.08543940
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 36020 * 0.08688729
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19551 * 0.80281685
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79061 * 0.34850425
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94703 * 0.20518192
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61540 * 0.69043529
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'cljqquos').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0006():
    """Extended test 6 for pipeline."""
    x_0 = 65914 * 0.09781478
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82461 * 0.41609962
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95626 * 0.80808885
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10727 * 0.06014773
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56121 * 0.37071724
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69199 * 0.10280366
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11648 * 0.03106005
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32668 * 0.46565777
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50464 * 0.04106334
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 145 * 0.93001557
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80228 * 0.70293061
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55545 * 0.59754735
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94394 * 0.56140805
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58993 * 0.16668323
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23209 * 0.12554885
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44973 * 0.45621150
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81372 * 0.16327608
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78726 * 0.81971205
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69865 * 0.21462991
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72018 * 0.44560680
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71021 * 0.15184744
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23578 * 0.77841554
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74311 * 0.17271525
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91650 * 0.17011684
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38353 * 0.92439303
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38658 * 0.70250751
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48767 * 0.09316060
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31950 * 0.55286031
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45139 * 0.03148842
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41212 * 0.16210378
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'nadixdeu').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0007():
    """Extended test 7 for pipeline."""
    x_0 = 29326 * 0.69932288
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20817 * 0.92521574
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8622 * 0.63513008
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33874 * 0.76884344
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74624 * 0.55122248
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55125 * 0.86148535
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25228 * 0.54903510
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20297 * 0.74806007
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53096 * 0.23088780
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48250 * 0.77764075
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46467 * 0.37686981
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38382 * 0.54535950
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91850 * 0.46437050
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94053 * 0.26873963
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50613 * 0.57052309
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49022 * 0.67930266
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94632 * 0.73670218
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45602 * 0.08358283
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18867 * 0.69490975
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71848 * 0.73662183
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65451 * 0.79858205
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58548 * 0.21244223
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48795 * 0.04637737
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13752 * 0.20460866
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88312 * 0.58530880
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56700 * 0.54235402
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57503 * 0.08059390
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89231 * 0.44182224
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6872 * 0.43867472
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69437 * 0.84030204
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54409 * 0.56462846
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82265 * 0.54638749
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43458 * 0.37727150
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'jjaivnmn').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0008():
    """Extended test 8 for pipeline."""
    x_0 = 9880 * 0.75782581
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92953 * 0.94448169
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24680 * 0.11191092
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2892 * 0.44807652
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18829 * 0.54317715
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33443 * 0.24671149
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60333 * 0.61969802
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40149 * 0.74065423
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30508 * 0.73238614
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9745 * 0.53959879
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50492 * 0.25308647
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68948 * 0.46727721
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99501 * 0.39844843
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33799 * 0.08068295
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56703 * 0.91375976
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76861 * 0.83284884
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33074 * 0.54575318
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73083 * 0.83209288
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11776 * 0.96437014
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11706 * 0.28777002
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47069 * 0.41640176
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18983 * 0.87041746
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34530 * 0.64135343
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77288 * 0.96160155
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95228 * 0.77084769
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26854 * 0.38851212
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48371 * 0.96801965
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78713 * 0.04725945
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36367 * 0.09048402
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52247 * 0.03909328
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46419 * 0.04248690
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42561 * 0.87124613
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16143 * 0.07778641
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34966 * 0.27043195
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86617 * 0.39816007
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33147 * 0.33486518
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39136 * 0.39902490
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 546 * 0.56376783
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83744 * 0.44791603
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20507 * 0.91436907
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45480 * 0.59547111
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21408 * 0.89472990
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83457 * 0.73619957
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'wneagtbn').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0009():
    """Extended test 9 for pipeline."""
    x_0 = 31369 * 0.62811320
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43268 * 0.80685851
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37604 * 0.63062826
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87164 * 0.78596142
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52646 * 0.16619327
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87833 * 0.62996128
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30696 * 0.60546844
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60464 * 0.62722395
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7872 * 0.14834001
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43116 * 0.75927075
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62956 * 0.64973606
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33258 * 0.35729660
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24228 * 0.22765504
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65622 * 0.09215267
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17889 * 0.51746973
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95638 * 0.52801318
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95347 * 0.93004746
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56610 * 0.97740224
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20619 * 0.10517623
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9898 * 0.46018357
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4685 * 0.88949191
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3163 * 0.26890976
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40465 * 0.53732537
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28301 * 0.15345686
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9633 * 0.04738339
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67313 * 0.58604718
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75992 * 0.98804047
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57083 * 0.57622502
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77363 * 0.17605182
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67733 * 0.02930827
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58912 * 0.44370746
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 47745 * 0.54831059
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91336 * 0.62017817
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1107 * 0.01796806
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89504 * 0.31981665
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25906 * 0.16364498
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26324 * 0.80135416
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16000 * 0.78229675
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53486 * 0.39818228
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32126 * 0.23900464
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 66938 * 0.58449392
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13594 * 0.77120675
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1295 * 0.30080593
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 67133 * 0.66803427
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 2079 * 0.66363660
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 44440 * 0.33799228
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 10593 * 0.65156247
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 98962 * 0.05304387
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'bnmjmuxm').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0010():
    """Extended test 10 for pipeline."""
    x_0 = 96544 * 0.45729342
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68165 * 0.88323372
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10061 * 0.71687899
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54090 * 0.47853879
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72794 * 0.46824696
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56315 * 0.08529157
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83155 * 0.94745273
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81166 * 0.04290082
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28774 * 0.22980042
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3898 * 0.53008905
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55325 * 0.59220340
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22840 * 0.66933531
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51308 * 0.47588469
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27032 * 0.36071400
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8468 * 0.83543789
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60056 * 0.87257768
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72990 * 0.44252034
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1622 * 0.09014448
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12306 * 0.20237305
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74206 * 0.98362814
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13030 * 0.69551102
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39800 * 0.24880232
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68210 * 0.72833829
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86674 * 0.72692328
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29345 * 0.41352688
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65388 * 0.03290553
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2284 * 0.98555778
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12350 * 0.84441428
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77179 * 0.72178036
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26587 * 0.87941030
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30447 * 0.68351301
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91646 * 0.62504551
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84338 * 0.50867518
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24725 * 0.58275522
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50890 * 0.11179006
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74255 * 0.01532332
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24816 * 0.58292494
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72120 * 0.91118235
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9881 * 0.70672129
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32779 * 0.41162422
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43403 * 0.28602041
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36196 * 0.68997749
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65743 * 0.20670894
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61773 * 0.72674808
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 69273 * 0.11201903
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 39716 * 0.01513079
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'zqlfnrsk').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0011():
    """Extended test 11 for pipeline."""
    x_0 = 86217 * 0.01613520
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46494 * 0.62261123
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64460 * 0.60712211
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25176 * 0.10355793
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37363 * 0.97643488
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49915 * 0.94571661
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31559 * 0.43570999
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8149 * 0.23675746
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39954 * 0.35439573
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86129 * 0.29340237
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32385 * 0.06257340
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80072 * 0.48432349
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32059 * 0.28502599
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39924 * 0.85761153
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80222 * 0.86469925
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38549 * 0.92310500
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64484 * 0.72551543
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19456 * 0.72909106
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82768 * 0.79289223
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34396 * 0.50535994
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71511 * 0.83029899
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86206 * 0.13099144
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54236 * 0.01348852
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38385 * 0.72594933
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19336 * 0.39228358
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92444 * 0.47455917
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34129 * 0.88822450
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82910 * 0.13400145
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70026 * 0.62839164
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70496 * 0.49928470
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78581 * 0.75834933
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31702 * 0.71885045
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 19414 * 0.46014964
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88034 * 0.47656996
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31926 * 0.42117953
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17480 * 0.95936032
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ucdmsrzj').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0012():
    """Extended test 12 for pipeline."""
    x_0 = 88930 * 0.65459144
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5119 * 0.05867764
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98025 * 0.58091924
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64490 * 0.45651138
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25165 * 0.06891394
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83321 * 0.11641317
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39732 * 0.22366908
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37536 * 0.37077535
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50583 * 0.93162653
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83622 * 0.51476342
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95873 * 0.03716377
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 76660 * 0.93672010
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45221 * 0.15308579
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73779 * 0.35012740
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40187 * 0.01804714
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42426 * 0.99689135
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16207 * 0.07692304
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32774 * 0.05451558
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14274 * 0.53297797
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20969 * 0.94894654
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61514 * 0.86450623
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20442 * 0.40020453
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77097 * 0.28664404
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24278 * 0.33249144
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51282 * 0.24918806
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47687 * 0.96319480
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17599 * 0.51158337
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1354 * 0.58808224
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30059 * 0.93687349
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66212 * 0.75741462
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96619 * 0.53028889
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6482 * 0.86156374
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11438 * 0.82272103
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92595 * 0.81819217
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80027 * 0.89954940
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29432 * 0.59321984
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71074 * 0.58820386
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92493 * 0.13022687
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10340 * 0.18170258
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94270 * 0.22356693
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21871 * 0.22748358
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33643 * 0.03684042
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 94845 * 0.01804457
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 66494 * 0.82227910
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'kamskqzd').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0013():
    """Extended test 13 for pipeline."""
    x_0 = 36312 * 0.20852038
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85757 * 0.62196973
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46104 * 0.89952837
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86513 * 0.53642047
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11483 * 0.47695465
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16798 * 0.33763370
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51096 * 0.44061708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8196 * 0.30180217
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95808 * 0.43877845
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84437 * 0.53762793
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33784 * 0.54539885
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92668 * 0.53960118
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68518 * 0.32888799
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49062 * 0.84022561
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68416 * 0.22156653
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30870 * 0.90959398
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25233 * 0.50009195
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97113 * 0.91821982
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42414 * 0.66977937
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8224 * 0.40289754
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87506 * 0.84607941
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8741 * 0.91528363
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77355 * 0.81605260
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59737 * 0.88571223
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12868 * 0.04975154
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79017 * 0.05734532
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83650 * 0.50997196
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62672 * 0.72167092
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33562 * 0.90959613
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63483 * 0.12253378
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42158 * 0.87503000
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'napothpw').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0014():
    """Extended test 14 for pipeline."""
    x_0 = 52260 * 0.02750665
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17396 * 0.06383147
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36683 * 0.88632542
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51327 * 0.49851580
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38513 * 0.30415680
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88883 * 0.46253164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73377 * 0.90324887
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60995 * 0.68950156
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54897 * 0.33491716
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65230 * 0.07511841
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71818 * 0.91541150
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81033 * 0.30536951
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83704 * 0.50023405
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35114 * 0.58936455
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91900 * 0.51728210
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9306 * 0.82135542
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68254 * 0.82818349
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78850 * 0.38050647
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11187 * 0.50916636
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89840 * 0.77042788
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17574 * 0.64968653
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95356 * 0.01045590
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14771 * 0.24721002
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43477 * 0.05797231
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15141 * 0.60525057
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10124 * 0.96114013
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88112 * 0.73574239
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6636 * 0.20734161
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14161 * 0.04174921
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99832 * 0.96093792
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8818 * 0.57953568
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58910 * 0.08544705
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 71869 * 0.68648287
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21609 * 0.83892252
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21559 * 0.30741988
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67178 * 0.97951611
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71769 * 0.12779408
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13649 * 0.26482289
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'xsfxmzmx').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0015():
    """Extended test 15 for pipeline."""
    x_0 = 17288 * 0.61555723
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67299 * 0.76792082
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73262 * 0.28293705
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15577 * 0.03532668
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87227 * 0.02097236
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83812 * 0.02854853
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94634 * 0.78201505
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9613 * 0.22456694
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20251 * 0.81848584
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11830 * 0.59716897
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14971 * 0.54025712
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40218 * 0.81133804
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19586 * 0.63045941
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63836 * 0.01030906
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83271 * 0.33365194
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54124 * 0.55784200
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65940 * 0.18387341
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39524 * 0.16296270
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60574 * 0.05567914
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56163 * 0.06040164
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87029 * 0.73258389
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'nsxgxuns').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0016():
    """Extended test 16 for pipeline."""
    x_0 = 12330 * 0.36581363
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99097 * 0.70588124
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 994 * 0.88802960
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54085 * 0.15820544
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10387 * 0.43983674
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77198 * 0.30432074
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51608 * 0.79280583
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74227 * 0.70405016
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17122 * 0.23198634
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79219 * 0.29749220
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41528 * 0.83257859
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12066 * 0.54946904
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80102 * 0.20703615
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45356 * 0.84392898
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57988 * 0.12457841
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49562 * 0.92082150
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41980 * 0.55120726
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88055 * 0.13888987
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50916 * 0.65054393
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64915 * 0.48563494
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23182 * 0.32021046
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51326 * 0.67641996
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30016 * 0.63210464
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20149 * 0.12935319
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94528 * 0.75299961
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24556 * 0.17858602
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83544 * 0.08012378
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'qqbtsais').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0017():
    """Extended test 17 for pipeline."""
    x_0 = 34349 * 0.14701890
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60702 * 0.17028824
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68170 * 0.65460839
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29936 * 0.24907175
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44278 * 0.07227580
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50507 * 0.01155921
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16494 * 0.35576146
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81521 * 0.82756718
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4762 * 0.34741821
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27196 * 0.60186093
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49675 * 0.85375372
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50750 * 0.81387771
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67589 * 0.72221294
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46212 * 0.31955865
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4707 * 0.51771102
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98343 * 0.20839850
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20774 * 0.59258133
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88392 * 0.52158279
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27395 * 0.86361036
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25146 * 0.99383779
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32141 * 0.44841677
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11506 * 0.76524028
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21550 * 0.22522473
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86457 * 0.15049541
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87065 * 0.82435174
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91091 * 0.55279630
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5417 * 0.15146901
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97249 * 0.94961934
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14322 * 0.85497038
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37799 * 0.04322868
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3308 * 0.67021347
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39086 * 0.71261496
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54853 * 0.75771832
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16944 * 0.58505128
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90024 * 0.20119384
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37225 * 0.09705397
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67575 * 0.34823995
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91269 * 0.23128814
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73554 * 0.38540882
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82710 * 0.27822828
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42322 * 0.26792169
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42797 * 0.52199485
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29085 * 0.40371522
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22880 * 0.17091422
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 75645 * 0.67938068
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'uybfubeb').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0018():
    """Extended test 18 for pipeline."""
    x_0 = 13306 * 0.19629914
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53550 * 0.11269541
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8947 * 0.95757359
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98780 * 0.24483703
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49857 * 0.10973776
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65827 * 0.03003801
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85562 * 0.27491833
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11397 * 0.20535825
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24680 * 0.82296446
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11697 * 0.98065195
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39925 * 0.29574650
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54579 * 0.32966759
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58472 * 0.65530514
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58618 * 0.40525568
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31938 * 0.99490148
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60246 * 0.30056060
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4506 * 0.18740717
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18892 * 0.50392933
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36928 * 0.90736096
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13247 * 0.07037999
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69522 * 0.09668742
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3799 * 0.57132068
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91834 * 0.84066964
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9324 * 0.90112185
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70902 * 0.81637767
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18947 * 0.31946543
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37622 * 0.02860212
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35601 * 0.18412051
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33563 * 0.90301774
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50420 * 0.88880534
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'chnjdglc').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0019():
    """Extended test 19 for pipeline."""
    x_0 = 52587 * 0.21675114
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26610 * 0.47945770
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8775 * 0.06228604
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39116 * 0.85763728
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64704 * 0.15286816
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95753 * 0.33737804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69752 * 0.29234432
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3254 * 0.49198785
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90160 * 0.14808027
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22300 * 0.72587667
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42723 * 0.64069087
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81719 * 0.70754770
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36362 * 0.25104172
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69180 * 0.70885318
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52385 * 0.25389295
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39309 * 0.21276400
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19528 * 0.98291545
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36094 * 0.66603420
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13378 * 0.93118559
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73371 * 0.31139256
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99114 * 0.23454904
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40382 * 0.82244852
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60598 * 0.92389908
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60701 * 0.14556935
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88053 * 0.26276885
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35409 * 0.35130706
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71154 * 0.15285161
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92009 * 0.03824541
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46514 * 0.85225562
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32303 * 0.68356108
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20616 * 0.29641502
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'gttrmixw').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0020():
    """Extended test 20 for pipeline."""
    x_0 = 15484 * 0.48163614
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39746 * 0.51184851
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10742 * 0.85903757
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90046 * 0.84759669
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11960 * 0.44062309
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76343 * 0.94635450
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55107 * 0.52669746
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61993 * 0.28259110
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87294 * 0.12855030
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45450 * 0.76714836
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20488 * 0.97625423
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13647 * 0.37982310
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37991 * 0.57733217
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13971 * 0.72013577
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81785 * 0.88197162
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58276 * 0.57101959
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83865 * 0.78986988
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86908 * 0.45608699
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44389 * 0.25465408
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67374 * 0.61741130
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20557 * 0.16505115
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20317 * 0.40215951
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'djbtezyi').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0021():
    """Extended test 21 for pipeline."""
    x_0 = 20283 * 0.68270709
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96170 * 0.64041287
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58209 * 0.75822454
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51059 * 0.50766398
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91018 * 0.73732872
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93624 * 0.13624967
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38979 * 0.44169791
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58441 * 0.54915325
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14010 * 0.08047231
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39041 * 0.18421346
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34191 * 0.94196345
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58382 * 0.23368389
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8443 * 0.59642180
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24687 * 0.27051114
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54656 * 0.35553310
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69842 * 0.45861912
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65682 * 0.86943449
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40395 * 0.00573424
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77310 * 0.77638042
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54339 * 0.38433142
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62376 * 0.11116832
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84312 * 0.33768695
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43744 * 0.92278539
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98540 * 0.59702413
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92350 * 0.05357413
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66649 * 0.59939032
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'oplhomxn').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0022():
    """Extended test 22 for pipeline."""
    x_0 = 77090 * 0.75659920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64186 * 0.73771047
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98857 * 0.21436875
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65187 * 0.63685118
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47204 * 0.34444755
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50049 * 0.55604250
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13350 * 0.53599853
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13428 * 0.97471221
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37377 * 0.33076095
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82321 * 0.50082900
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38761 * 0.58105475
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55741 * 0.76829026
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63208 * 0.81067246
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68406 * 0.54033576
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 603 * 0.51393063
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20985 * 0.36302733
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15449 * 0.25283041
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42449 * 0.65544531
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91290 * 0.57513366
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46091 * 0.45803122
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17391 * 0.38142013
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66970 * 0.52302304
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74215 * 0.36112792
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78505 * 0.31335276
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30906 * 0.45521321
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6303 * 0.08340583
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66366 * 0.45286373
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74052 * 0.61252809
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12344 * 0.50982835
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20449 * 0.83830285
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45176 * 0.01162548
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93799 * 0.80336226
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39894 * 0.08141716
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48399 * 0.74741222
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47172 * 0.27179113
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76839 * 0.17719902
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43152 * 0.28608385
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92071 * 0.64352262
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14645 * 0.56870840
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46789 * 0.76867318
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44281 * 0.32876691
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77497 * 0.06293849
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70243 * 0.17502522
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'klqeleov').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0023():
    """Extended test 23 for pipeline."""
    x_0 = 3546 * 0.92686401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50177 * 0.12776279
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91882 * 0.64771278
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1364 * 0.80512053
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58103 * 0.91302119
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93589 * 0.68484761
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83388 * 0.88778734
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31356 * 0.29406398
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85842 * 0.17053182
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84007 * 0.69286859
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5832 * 0.33094308
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75036 * 0.60709726
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73613 * 0.99983602
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99497 * 0.12454111
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13509 * 0.48662266
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43871 * 0.37480336
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22786 * 0.23020569
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61509 * 0.00982403
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12605 * 0.86284358
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87253 * 0.96527247
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84216 * 0.34362831
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'axcjsabe').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0024():
    """Extended test 24 for pipeline."""
    x_0 = 91928 * 0.85982179
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34358 * 0.95076439
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23848 * 0.84216466
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20145 * 0.66578128
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93347 * 0.42702997
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24499 * 0.72448918
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49780 * 0.32831188
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89167 * 0.71054118
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18847 * 0.45577032
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70903 * 0.00529440
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21398 * 0.46002670
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28653 * 0.92406284
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88196 * 0.08164218
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40708 * 0.46153281
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86256 * 0.35897544
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62336 * 0.06425194
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15532 * 0.99687095
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56449 * 0.42501500
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10681 * 0.63565714
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22324 * 0.98472264
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46445 * 0.51380878
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15595 * 0.14987768
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48407 * 0.56956494
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47767 * 0.59003386
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26597 * 0.10265835
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41109 * 0.78995631
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74973 * 0.28929908
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95850 * 0.85607487
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41455 * 0.37594673
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31774 * 0.17993573
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20025 * 0.83381726
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69885 * 0.23160134
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52143 * 0.07222999
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33963 * 0.28054663
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86940 * 0.07425268
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66678 * 0.98771970
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4713 * 0.01260593
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87423 * 0.51416966
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91317 * 0.49597048
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 22512 * 0.51271799
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75142 * 0.64845511
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20332 * 0.60272632
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'koatpikd').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0025():
    """Extended test 25 for pipeline."""
    x_0 = 2871 * 0.81564920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8654 * 0.71853415
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94731 * 0.57399335
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67867 * 0.91757519
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1700 * 0.28389260
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16051 * 0.56883633
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39770 * 0.80938162
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97778 * 0.04169664
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37616 * 0.53489123
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60170 * 0.55951782
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58612 * 0.63226958
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39153 * 0.93008924
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17877 * 0.85473742
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37642 * 0.89422664
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57471 * 0.62068470
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34871 * 0.64673463
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75448 * 0.67128186
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17254 * 0.83184212
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49065 * 0.56110355
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85451 * 0.18624544
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12898 * 0.06052162
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23073 * 0.92572209
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63244 * 0.59096770
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91839 * 0.25815076
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1787 * 0.88259097
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 207 * 0.55925912
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'obqrqxay').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0026():
    """Extended test 26 for pipeline."""
    x_0 = 60878 * 0.89588563
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28499 * 0.29483201
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31947 * 0.90864111
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82424 * 0.53465937
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26224 * 0.26444808
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43002 * 0.99269110
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70416 * 0.58894343
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33850 * 0.66706057
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44530 * 0.68678418
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98185 * 0.13660545
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81244 * 0.73183403
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10626 * 0.47344142
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92128 * 0.27913842
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98847 * 0.57923758
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40926 * 0.30556914
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97768 * 0.24458539
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62478 * 0.22646931
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19056 * 0.19458471
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31992 * 0.30922281
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26322 * 0.85014626
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16252 * 0.99271906
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97649 * 0.34371955
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45519 * 0.58942050
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7550 * 0.48241862
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76158 * 0.14666139
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15554 * 0.22029726
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68104 * 0.29878243
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50915 * 0.81602109
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'vwouahfb').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0027():
    """Extended test 27 for pipeline."""
    x_0 = 76728 * 0.64585827
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54863 * 0.96314591
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96649 * 0.52101277
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10517 * 0.90558016
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52965 * 0.14616268
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25250 * 0.13832420
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15920 * 0.32829254
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26048 * 0.57577901
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21670 * 0.44429745
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27801 * 0.01898148
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76580 * 0.09763462
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53594 * 0.67324074
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68623 * 0.29024808
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24512 * 0.70201900
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83108 * 0.12017907
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8764 * 0.50040879
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90185 * 0.54102242
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4056 * 0.79072225
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16827 * 0.77046152
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37920 * 0.89482035
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13851 * 0.38667435
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58746 * 0.96474404
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31022 * 0.76331960
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92106 * 0.70095233
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57165 * 0.99070824
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93357 * 0.00228479
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94668 * 0.37542342
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59478 * 0.62619606
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19424 * 0.08595230
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92933 * 0.19031352
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3512 * 0.26531957
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38058 * 0.81665812
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78817 * 0.01481580
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45416 * 0.34660438
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94847 * 0.21666917
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56504 * 0.38642374
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72671 * 0.38470941
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78305 * 0.67200877
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36443 * 0.26102667
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93957 * 0.74322236
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37933 * 0.21784582
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72414 * 0.99855934
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46485 * 0.88086378
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 50014 * 0.67240418
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 44075 * 0.55079440
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 72941 * 0.67220841
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 86718 * 0.65657637
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 57252 * 0.72376034
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 74198 * 0.65481268
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 65641 * 0.71971650
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'feyamolj').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0028():
    """Extended test 28 for pipeline."""
    x_0 = 65312 * 0.40650768
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78949 * 0.58172269
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25924 * 0.74880082
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46996 * 0.18233799
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19152 * 0.06650766
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18997 * 0.52155893
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21393 * 0.22039809
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25949 * 0.12387682
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47325 * 0.71148261
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76953 * 0.47833857
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76601 * 0.83072679
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 941 * 0.58418747
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72266 * 0.14652736
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15267 * 0.16443808
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55884 * 0.61897842
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2871 * 0.89647333
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16339 * 0.57763056
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76554 * 0.49031598
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65687 * 0.55871553
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28381 * 0.61358545
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86434 * 0.69279355
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93738 * 0.15100110
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12312 * 0.38786683
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95510 * 0.19790689
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39606 * 0.34930441
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11655 * 0.64941676
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13960 * 0.04098218
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91920 * 0.81640864
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85671 * 0.44825216
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34177 * 0.80900511
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39394 * 0.22107875
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49279 * 0.26159458
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58791 * 0.75846159
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79348 * 0.32985930
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87019 * 0.69444780
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70779 * 0.32521552
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35499 * 0.56316473
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 57874 * 0.65893496
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93869 * 0.34619265
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85103 * 0.53308446
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 2829 * 0.86300764
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59780 * 0.97463060
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'dyjvtgtu').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0029():
    """Extended test 29 for pipeline."""
    x_0 = 17954 * 0.32437222
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48555 * 0.36515489
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54276 * 0.50954880
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41630 * 0.45645589
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24484 * 0.97550733
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93363 * 0.24713952
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56011 * 0.33707412
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20786 * 0.98358264
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45561 * 0.03851765
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24749 * 0.55290579
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80268 * 0.95088101
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69473 * 0.84273577
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79441 * 0.21999684
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53872 * 0.62143422
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88397 * 0.56752353
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5603 * 0.62528950
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87270 * 0.11169564
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24406 * 0.15368942
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27790 * 0.88471076
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86187 * 0.79764378
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'yxdvytlv').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0030():
    """Extended test 30 for pipeline."""
    x_0 = 51956 * 0.94152095
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37979 * 0.66268112
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99344 * 0.26540211
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64012 * 0.18056803
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51265 * 0.43011938
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70556 * 0.90837247
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63317 * 0.02989022
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51679 * 0.32765666
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69877 * 0.82535915
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43520 * 0.78266656
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6756 * 0.56218528
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60299 * 0.63457827
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95339 * 0.48614279
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89450 * 0.56131928
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68674 * 0.57951564
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62195 * 0.66789149
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94295 * 0.61374701
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94694 * 0.71373190
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50712 * 0.35124034
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59828 * 0.48576031
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88002 * 0.03100093
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99947 * 0.56582512
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92942 * 0.88652930
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56361 * 0.66215608
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'cxgwqlli').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0031():
    """Extended test 31 for pipeline."""
    x_0 = 79931 * 0.63483838
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44966 * 0.37553533
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70807 * 0.37478207
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42334 * 0.15040305
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 737 * 0.92305499
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50299 * 0.69900991
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3318 * 0.03877303
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57960 * 0.28718555
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96678 * 0.52384717
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48874 * 0.86324772
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60693 * 0.65061949
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97858 * 0.02677429
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26977 * 0.47999922
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41568 * 0.19511167
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64501 * 0.07485639
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7042 * 0.09861080
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60781 * 0.87623094
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84210 * 0.87434702
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37328 * 0.81044148
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92099 * 0.77154729
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20533 * 0.09768847
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84104 * 0.37738314
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35616 * 0.70528236
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47136 * 0.36162219
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55365 * 0.49973900
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5554 * 0.98730395
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47969 * 0.63397695
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96556 * 0.19724222
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73286 * 0.56885329
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17703 * 0.69862229
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15425 * 0.50496318
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72277 * 0.85191085
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22188 * 0.00939098
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62094 * 0.61581429
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16073 * 0.50334888
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59687 * 0.93820181
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36597 * 0.35754969
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74004 * 0.02835859
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11815 * 0.37141819
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23435 * 0.07847829
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43517 * 0.49906566
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66899 * 0.22154531
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57992 * 0.01625597
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38756 * 0.88774214
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 37808 * 0.78614828
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 73586 * 0.37303539
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 70617 * 0.82529566
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 49213 * 0.07064630
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 66611 * 0.49255120
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 73843 * 0.52698179
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'uagcmcne').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0032():
    """Extended test 32 for pipeline."""
    x_0 = 41327 * 0.34778969
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82636 * 0.07612398
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59699 * 0.16383023
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82060 * 0.22914997
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50090 * 0.93930906
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61309 * 0.19742713
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75858 * 0.99043225
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68449 * 0.85297071
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26404 * 0.25399212
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11365 * 0.46121925
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62256 * 0.06177614
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70576 * 0.87211966
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23979 * 0.41637198
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68892 * 0.21016265
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12507 * 0.35117112
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 689 * 0.22994493
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1296 * 0.50920607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56261 * 0.33144852
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4235 * 0.44593959
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60357 * 0.14907029
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60564 * 0.46243236
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57264 * 0.91506189
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98286 * 0.96413462
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22871 * 0.92384521
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7930 * 0.42259571
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30823 * 0.63055872
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'sgqvrozd').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0033():
    """Extended test 33 for pipeline."""
    x_0 = 77457 * 0.90097194
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84044 * 0.77725396
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50395 * 0.42257273
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14480 * 0.04702674
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60609 * 0.94292723
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97608 * 0.31221527
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63275 * 0.07836364
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19899 * 0.73195262
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13447 * 0.90051315
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75863 * 0.68377148
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87074 * 0.59642200
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46643 * 0.39087928
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49081 * 0.37706145
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55672 * 0.27620780
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82887 * 0.26326173
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91149 * 0.98519410
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26235 * 0.83171893
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62078 * 0.81818567
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80419 * 0.86973923
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38872 * 0.35508581
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49164 * 0.25696483
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9823 * 0.01572442
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12658 * 0.60901890
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75426 * 0.64293572
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65461 * 0.29705238
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49838 * 0.45070490
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85883 * 0.42818456
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34399 * 0.37128826
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94716 * 0.73881623
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56702 * 0.56989340
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2314 * 0.58666613
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89227 * 0.87721182
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55304 * 0.37796775
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64258 * 0.37189090
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55661 * 0.91878387
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38526 * 0.60036332
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67841 * 0.10164071
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52363 * 0.55957374
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24190 * 0.22994844
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 27473 * 0.31698189
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 88886 * 0.42435656
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 75506 * 0.10786685
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24730 * 0.49916242
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94766 * 0.06864631
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 25177 * 0.13591449
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 45132 * 0.54528191
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 31516 * 0.66986244
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 6146 * 0.42765939
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 11426 * 0.89748173
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 55874 * 0.87132993
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'etfqepef').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0034():
    """Extended test 34 for pipeline."""
    x_0 = 29096 * 0.86807241
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73941 * 0.92996737
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79477 * 0.94413323
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97272 * 0.03081346
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2248 * 0.18298054
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80252 * 0.95797932
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93930 * 0.90059669
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84623 * 0.37035501
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98939 * 0.08401611
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56946 * 0.19678774
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33060 * 0.14791916
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67678 * 0.76136906
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9107 * 0.51507582
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5715 * 0.04733974
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9923 * 0.60056545
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67947 * 0.80110917
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45759 * 0.28752007
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71835 * 0.63447819
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39745 * 0.03893047
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96836 * 0.39967799
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94840 * 0.79856492
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78730 * 0.48585987
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35160 * 0.94499870
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9945 * 0.23800420
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18498 * 0.43373010
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'rzfdmyld').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0035():
    """Extended test 35 for pipeline."""
    x_0 = 84897 * 0.68021344
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62878 * 0.74828456
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14407 * 0.50773209
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36898 * 0.90708955
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80997 * 0.00189450
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42091 * 0.40687403
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74070 * 0.53683343
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97505 * 0.50823080
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73616 * 0.62662260
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19812 * 0.16036807
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23544 * 0.55712400
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52711 * 0.39304891
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43680 * 0.32839584
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83560 * 0.40743309
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14650 * 0.83320151
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85092 * 0.68606802
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92287 * 0.87136497
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94180 * 0.21843472
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70930 * 0.16000050
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96770 * 0.84204560
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30208 * 0.31464379
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50351 * 0.10240160
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'nldupwbk').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0036():
    """Extended test 36 for pipeline."""
    x_0 = 556 * 0.36286305
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99498 * 0.58325958
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18664 * 0.88044716
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37496 * 0.04461929
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88553 * 0.44212766
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13678 * 0.13063925
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90028 * 0.59566051
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67397 * 0.56076413
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89376 * 0.72057006
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80268 * 0.44243580
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32431 * 0.34746012
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62202 * 0.72056510
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95654 * 0.53670053
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58523 * 0.44004825
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72406 * 0.24727899
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35007 * 0.68171694
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 769 * 0.93150527
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75643 * 0.01512357
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30749 * 0.58478298
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52746 * 0.45343452
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23241 * 0.74383013
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97667 * 0.09218062
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99324 * 0.05148851
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62221 * 0.46022880
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85187 * 0.16694304
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34593 * 0.18629662
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47661 * 0.00289759
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27729 * 0.00953600
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'xarnbmql').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0037():
    """Extended test 37 for pipeline."""
    x_0 = 3576 * 0.96918223
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68610 * 0.47516369
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87442 * 0.90167483
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88298 * 0.25599446
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82771 * 0.33638683
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12621 * 0.45735708
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3800 * 0.71549270
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49749 * 0.56101535
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83266 * 0.94141301
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56512 * 0.41902579
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83335 * 0.02240982
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27486 * 0.38552810
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68228 * 0.46312552
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20359 * 0.95163754
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83990 * 0.23800153
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40064 * 0.29273211
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17651 * 0.14388626
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85657 * 0.73584617
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11764 * 0.97131360
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11116 * 0.85057375
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5724 * 0.49365614
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7477 * 0.42155992
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94153 * 0.15375079
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41743 * 0.64237362
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37509 * 0.82350630
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3036 * 0.81014077
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44980 * 0.91378094
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77543 * 0.89959597
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24154 * 0.88989534
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55347 * 0.64667218
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27781 * 0.87244606
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35690 * 0.41680073
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43217 * 0.93774201
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60504 * 0.29411019
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64776 * 0.01515641
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99113 * 0.18649596
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73533 * 0.09867503
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65792 * 0.37928710
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27355 * 0.61678404
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68254 * 0.76667468
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80793 * 0.85493430
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70241 * 0.09624136
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 99991 * 0.60977374
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 32165 * 0.71100481
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 9095 * 0.56882028
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'fevyvveq').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0038():
    """Extended test 38 for pipeline."""
    x_0 = 98444 * 0.11768353
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7941 * 0.96383329
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90224 * 0.40423587
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47050 * 0.23039315
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38484 * 0.54642622
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19087 * 0.68871324
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 919 * 0.81551607
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34288 * 0.07425331
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45157 * 0.48533247
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81742 * 0.08726051
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59685 * 0.72432662
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63658 * 0.01442242
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69953 * 0.60299188
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 16492 * 0.05650434
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55713 * 0.38513847
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87226 * 0.58286751
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23251 * 0.51878092
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73946 * 0.37456555
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44000 * 0.27488177
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42665 * 0.79467234
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78650 * 0.14314396
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28117 * 0.17891999
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78909 * 0.11506949
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5227 * 0.35948096
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96136 * 0.35368708
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68154 * 0.59151380
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81229 * 0.99389487
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75410 * 0.71493011
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95412 * 0.64552590
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80107 * 0.21366741
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6475 * 0.84266417
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19069 * 0.18741201
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74280 * 0.14448809
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 84111 * 0.37319782
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51934 * 0.77539650
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94378 * 0.57940125
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23622 * 0.44995519
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95013 * 0.78622550
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'jmmicxmc').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0039():
    """Extended test 39 for pipeline."""
    x_0 = 13821 * 0.61943734
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29774 * 0.77972846
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8003 * 0.26239917
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10734 * 0.52305809
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76472 * 0.04940650
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42528 * 0.97318216
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91779 * 0.72925691
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29678 * 0.08465616
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25131 * 0.22182890
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51295 * 0.35467248
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79695 * 0.65326934
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93039 * 0.84725605
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67969 * 0.70239988
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17479 * 0.75593449
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16638 * 0.93805991
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5889 * 0.24263778
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69236 * 0.63526221
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9457 * 0.33909172
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61209 * 0.85753421
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81821 * 0.68751796
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56984 * 0.30880436
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61836 * 0.86447980
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22529 * 0.60738656
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39288 * 0.32447321
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75994 * 0.89918084
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73003 * 0.66728046
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77621 * 0.56183199
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'lupyuxqk').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0040():
    """Extended test 40 for pipeline."""
    x_0 = 4791 * 0.18071541
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41319 * 0.74973816
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78572 * 0.38627867
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90164 * 0.30007602
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29833 * 0.37217926
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50899 * 0.46696841
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76753 * 0.59550775
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94965 * 0.72902855
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22111 * 0.68840902
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3328 * 0.87326079
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36588 * 0.14892093
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44344 * 0.92368864
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29673 * 0.01143867
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65734 * 0.32576762
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61991 * 0.10821062
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88966 * 0.93903875
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85042 * 0.62284202
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45166 * 0.61768688
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38571 * 0.09761755
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29760 * 0.89151688
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16324 * 0.08794508
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84758 * 0.86733053
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8525 * 0.96156458
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60706 * 0.85070510
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30059 * 0.21715073
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45940 * 0.27758309
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96465 * 0.46774817
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6607 * 0.71872132
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1549 * 0.85597009
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62009 * 0.76347799
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34494 * 0.40812591
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37442 * 0.16708591
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'qnefjuky').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0041():
    """Extended test 41 for pipeline."""
    x_0 = 16960 * 0.48488746
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72486 * 0.73777828
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9749 * 0.03193796
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45784 * 0.40880072
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58326 * 0.20407107
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11610 * 0.92817992
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95151 * 0.91122252
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24585 * 0.76695428
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83179 * 0.18028203
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78727 * 0.37373735
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35358 * 0.04988409
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10828 * 0.21216777
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30212 * 0.56106358
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80465 * 0.41865731
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25721 * 0.81043030
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45542 * 0.64122875
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62862 * 0.10245707
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51264 * 0.51065842
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48300 * 0.77452628
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7878 * 0.05577326
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58214 * 0.52576541
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41158 * 0.62363863
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31954 * 0.33072931
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72133 * 0.53505122
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16452 * 0.70098349
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56607 * 0.81656845
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71190 * 0.43817755
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64425 * 0.78954642
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60802 * 0.89905640
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71666 * 0.81238517
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11759 * 0.92086786
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'wekturdn').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0042():
    """Extended test 42 for pipeline."""
    x_0 = 16775 * 0.01961206
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67599 * 0.23668302
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86210 * 0.53262544
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69070 * 0.20001040
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10930 * 0.66409093
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37946 * 0.20164470
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87339 * 0.74123639
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67028 * 0.37115332
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91520 * 0.37189656
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42896 * 0.34353743
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11295 * 0.40178828
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5467 * 0.60049292
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45907 * 0.08156376
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36599 * 0.73400682
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92660 * 0.59054325
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55769 * 0.66529387
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51790 * 0.94690677
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25590 * 0.27301862
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48394 * 0.55185490
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31281 * 0.56876277
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99742 * 0.49669238
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78702 * 0.82225837
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94087 * 0.83758829
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28587 * 0.46902837
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25665 * 0.27244980
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60078 * 0.41424637
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75637 * 0.58896743
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81933 * 0.51246266
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88192 * 0.47970089
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4064 * 0.93886032
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89669 * 0.73371280
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26995 * 0.66349225
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77150 * 0.98688372
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58256 * 0.13481642
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39425 * 0.63302972
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74774 * 0.31586079
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81492 * 0.13573961
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1013 * 0.96471710
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30348 * 0.16633951
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79056 * 0.02500702
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 90424 * 0.45472490
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43594 * 0.15080282
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 17212 * 0.06145071
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 79283 * 0.98152007
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 75630 * 0.02301035
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 9639 * 0.33748057
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 66911 * 0.48153960
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 57339 * 0.97628403
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ylholbug').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0043():
    """Extended test 43 for pipeline."""
    x_0 = 5424 * 0.97334530
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47722 * 0.97440078
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87484 * 0.14151538
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27943 * 0.77291986
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58685 * 0.20578510
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48402 * 0.92804675
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60860 * 0.70319505
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27470 * 0.75974360
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59619 * 0.20765434
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23967 * 0.40276721
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2035 * 0.54552935
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59399 * 0.77235027
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7400 * 0.57015267
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44856 * 0.94807136
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26361 * 0.88628093
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20350 * 0.98756141
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45866 * 0.17550571
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11784 * 0.17066877
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95438 * 0.04984618
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12480 * 0.99334212
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'kvcjcavp').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0044():
    """Extended test 44 for pipeline."""
    x_0 = 23879 * 0.69245905
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82108 * 0.34628056
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75120 * 0.89757172
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26389 * 0.12162225
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40796 * 0.50100187
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57717 * 0.29597879
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35324 * 0.68650472
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37695 * 0.55275116
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46856 * 0.84734628
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74487 * 0.86384944
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26772 * 0.91823189
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15443 * 0.20604525
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44193 * 0.69041828
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46086 * 0.22551716
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85404 * 0.66767247
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20132 * 0.26575565
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46320 * 0.76797241
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24427 * 0.34899617
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69159 * 0.86943793
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98057 * 0.65473217
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26866 * 0.39248149
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25930 * 0.51526777
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26907 * 0.29448760
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95670 * 0.32265647
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97774 * 0.83731189
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30773 * 0.44149845
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11892 * 0.14892062
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76961 * 0.61894804
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3546 * 0.27593935
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8601 * 0.56580158
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24264 * 0.20566290
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59247 * 0.29704949
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62298 * 0.03496131
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82710 * 0.04249277
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32138 * 0.39439155
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83300 * 0.11788214
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7145 * 0.21457571
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31039 * 0.11296075
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86064 * 0.13236685
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9539 * 0.71460808
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3259 * 0.64727512
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35856 * 0.59821609
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 52455 * 0.30766359
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34354 * 0.28821596
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 26595 * 0.88864775
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 970 * 0.74565002
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 94986 * 0.21262888
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 94289 * 0.65910121
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'fhfndksx').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0045():
    """Extended test 45 for pipeline."""
    x_0 = 40683 * 0.79314986
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24914 * 0.02197517
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67606 * 0.62325992
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70618 * 0.81839889
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46705 * 0.76604368
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4888 * 0.38608999
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58826 * 0.30222004
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52119 * 0.69457483
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48685 * 0.19660129
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75383 * 0.72827537
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25219 * 0.92947103
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30384 * 0.73872882
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10271 * 0.04922033
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37604 * 0.11434547
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40977 * 0.43944358
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78038 * 0.44040788
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27615 * 0.48484682
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97536 * 0.65774943
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74940 * 0.68454975
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76130 * 0.05214849
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76643 * 0.31916431
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92593 * 0.39593227
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4757 * 0.16764839
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11452 * 0.91571389
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14767 * 0.36509085
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5445 * 0.59409876
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89432 * 0.63492969
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72678 * 0.17138064
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48516 * 0.25029955
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83067 * 0.88553235
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50105 * 0.37030813
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27580 * 0.74686064
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48160 * 0.85535266
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83392 * 0.36881857
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36858 * 0.17075339
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64047 * 0.82653121
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29098 * 0.61665591
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43887 * 0.82725555
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 35034 * 0.48962654
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 12246 * 0.35051985
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 98349 * 0.41530488
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'fvokjcmi').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0046():
    """Extended test 46 for pipeline."""
    x_0 = 71730 * 0.20476139
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83218 * 0.77150261
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10416 * 0.79276547
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38633 * 0.74019336
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88413 * 0.51286419
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51635 * 0.91773675
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66921 * 0.31742429
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49836 * 0.73151988
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30353 * 0.05845077
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92094 * 0.94320206
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94320 * 0.31818248
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78208 * 0.01212000
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94819 * 0.58275221
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65397 * 0.40528481
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83519 * 0.20100430
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54552 * 0.82311018
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18670 * 0.72290395
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82800 * 0.43974635
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87999 * 0.38042917
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34619 * 0.37906390
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31838 * 0.30805344
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96633 * 0.74703878
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83670 * 0.40934411
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48364 * 0.93920474
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60131 * 0.10474503
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'kqejhpjk').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0047():
    """Extended test 47 for pipeline."""
    x_0 = 73764 * 0.83547643
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10456 * 0.16348056
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47582 * 0.76840028
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38246 * 0.59262277
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25216 * 0.35382288
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44976 * 0.89363893
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53027 * 0.10027130
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49475 * 0.37557164
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82214 * 0.02680066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72301 * 0.51781555
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66594 * 0.73588852
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32799 * 0.18601564
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7774 * 0.39619182
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89309 * 0.95330313
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46657 * 0.10857777
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70768 * 0.59319251
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88597 * 0.52836936
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69133 * 0.07135467
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23432 * 0.56520709
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2327 * 0.65147351
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68655 * 0.61126579
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72536 * 0.80482839
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19918 * 0.54413431
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63849 * 0.38262643
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44756 * 0.58259432
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41519 * 0.95658608
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 680 * 0.51842044
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6782 * 0.93069714
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21100 * 0.00306440
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5586 * 0.17529636
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15391 * 0.66511780
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72358 * 0.05513616
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54607 * 0.50453938
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56028 * 0.37150765
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27808 * 0.21706369
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65252 * 0.49930250
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46379 * 0.32061343
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 51041 * 0.45488349
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82849 * 0.82216044
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41192 * 0.84945888
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 72012 * 0.52411926
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4859 * 0.74905673
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 15121 * 0.58038417
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 15701 * 0.46234079
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 27677 * 0.22722119
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 65065 * 0.83612120
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 68346 * 0.82582474
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 15616 * 0.79718471
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'bjehrduq').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0048():
    """Extended test 48 for pipeline."""
    x_0 = 24587 * 0.29545092
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84662 * 0.26398622
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18428 * 0.53351106
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73975 * 0.17782380
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26895 * 0.69950659
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79282 * 0.13438993
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71264 * 0.01108139
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33138 * 0.00261613
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90584 * 0.44002414
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77433 * 0.07083919
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89169 * 0.55703740
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14456 * 0.21765709
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67995 * 0.28234261
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18395 * 0.06345806
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41535 * 0.64841079
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21120 * 0.80312268
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10637 * 0.56238327
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68758 * 0.26757528
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45534 * 0.64132930
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30484 * 0.13610317
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43662 * 0.21133043
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84840 * 0.73636543
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96696 * 0.73550749
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28742 * 0.08014457
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66383 * 0.82127464
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68402 * 0.71690376
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99613 * 0.57404444
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85499 * 0.21917381
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39244 * 0.45681701
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21701 * 0.14606214
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43836 * 0.66931917
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76680 * 0.77605862
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12697 * 0.34954499
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99267 * 0.85310776
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3840 * 0.71498529
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38877 * 0.05596873
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 21244 * 0.38426425
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 31908 * 0.89952144
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30248 * 0.28103182
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 53131 * 0.42791037
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38020 * 0.00411171
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36384 * 0.39169895
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47147 * 0.59637736
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 44130 * 0.55112546
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 41360 * 0.86819671
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 14179 * 0.15069274
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'eslhmdgn').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0049():
    """Extended test 49 for pipeline."""
    x_0 = 71497 * 0.77500795
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85004 * 0.73801371
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 490 * 0.22443499
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57851 * 0.32449116
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60479 * 0.62551042
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64502 * 0.00436727
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36059 * 0.16644437
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92778 * 0.31709408
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38447 * 0.48727740
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75744 * 0.10504375
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73970 * 0.37612019
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24323 * 0.16165574
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20099 * 0.20197911
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85998 * 0.03906114
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35754 * 0.78094460
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1278 * 0.59314475
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76439 * 0.27717671
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34014 * 0.39018224
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57878 * 0.69857546
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48002 * 0.07360304
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48426 * 0.29931522
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76229 * 0.79442592
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63450 * 0.71085601
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54755 * 0.50508865
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62764 * 0.34434423
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48109 * 0.87173594
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33695 * 0.93321812
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55585 * 0.36460119
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68466 * 0.54224567
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4198 * 0.51371037
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93586 * 0.59359318
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96443 * 0.12823321
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61401 * 0.05398940
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46298 * 0.37070916
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 404 * 0.43619119
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82945 * 0.72345323
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4664 * 0.04071870
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23932 * 0.29374698
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24092 * 0.44807040
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 58068 * 0.48835474
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75231 * 0.05542249
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14746 * 0.94580785
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 61122 * 0.47659728
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 32231 * 0.93162762
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92953 * 0.37995097
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 85540 * 0.32961308
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 9720 * 0.75718176
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'qnpxgpfw').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0050():
    """Extended test 50 for pipeline."""
    x_0 = 83360 * 0.07922160
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17562 * 0.81516233
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80939 * 0.67872271
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26126 * 0.99685806
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98645 * 0.85300367
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64800 * 0.67090263
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42062 * 0.36679681
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 27840 * 0.41943898
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78888 * 0.13282846
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55556 * 0.18031502
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73842 * 0.02372951
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86581 * 0.24906702
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68951 * 0.90731017
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70872 * 0.01655916
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81090 * 0.56087692
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14390 * 0.03527301
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11812 * 0.22647574
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37773 * 0.48349238
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3791 * 0.34508177
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8499 * 0.65499120
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22632 * 0.74312018
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70761 * 0.90094512
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37807 * 0.95761467
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81633 * 0.38015801
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21069 * 0.90690410
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81894 * 0.02829941
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'lpzoaaqb').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0051():
    """Extended test 51 for pipeline."""
    x_0 = 67997 * 0.21927249
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24767 * 0.19183255
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78397 * 0.56474838
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90245 * 0.91146040
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26461 * 0.65738966
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3698 * 0.33816029
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83479 * 0.17990006
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9000 * 0.93258876
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40458 * 0.77935368
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54544 * 0.77437805
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4001 * 0.70103662
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59969 * 0.63201353
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97887 * 0.40880764
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13639 * 0.78693217
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47059 * 0.72777970
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40647 * 0.32061410
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90770 * 0.26457886
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7743 * 0.56170989
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46880 * 0.68144534
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63358 * 0.60048785
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41172 * 0.00036362
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9792 * 0.95813416
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20780 * 0.84320229
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86211 * 0.19850858
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38161 * 0.14537435
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2163 * 0.53461772
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75739 * 0.37573447
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29983 * 0.71068854
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31750 * 0.66206048
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57877 * 0.52403470
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51343 * 0.32230955
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1551 * 0.10974417
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14949 * 0.71390881
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'frpxgnxo').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0052():
    """Extended test 52 for pipeline."""
    x_0 = 30253 * 0.79518877
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92168 * 0.40328714
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52178 * 0.91620561
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57411 * 0.70356055
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8612 * 0.28038698
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32024 * 0.12911188
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36337 * 0.40150675
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76459 * 0.56678846
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91459 * 0.59790459
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62187 * 0.17921116
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40782 * 0.79231396
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56181 * 0.61481958
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65503 * 0.60031510
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39976 * 0.00197635
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73502 * 0.23625069
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40023 * 0.58575803
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13200 * 0.39268882
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1693 * 0.33020850
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5472 * 0.30127960
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13378 * 0.31527555
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37833 * 0.83400683
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70097 * 0.25152175
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76927 * 0.90863624
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75202 * 0.89505439
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9213 * 0.06574919
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14197 * 0.34769241
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46582 * 0.91764289
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63155 * 0.45532282
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'ciblpidc').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0053():
    """Extended test 53 for pipeline."""
    x_0 = 10685 * 0.51738120
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61363 * 0.56906772
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77792 * 0.55218218
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5843 * 0.22807570
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21026 * 0.28447899
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48506 * 0.52225942
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51916 * 0.63308136
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94980 * 0.61133635
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86237 * 0.01059811
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82230 * 0.53720600
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88554 * 0.61196556
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81016 * 0.55674880
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57370 * 0.93834628
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84708 * 0.36137985
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87004 * 0.53483341
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97906 * 0.02773881
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31128 * 0.66468928
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42186 * 0.05171590
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16342 * 0.34417712
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19276 * 0.98222491
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75687 * 0.79604902
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73019 * 0.93286026
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79785 * 0.87289289
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90052 * 0.32494420
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88716 * 0.98089572
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84416 * 0.84935225
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82261 * 0.22517384
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42746 * 0.14473650
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 882 * 0.94395408
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40534 * 0.21405246
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28132 * 0.65435100
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35120 * 0.25450199
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3235 * 0.18984956
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74730 * 0.36479579
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44270 * 0.76279824
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45020 * 0.86435345
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42040 * 0.86196744
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89695 * 0.12918534
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86254 * 0.77235715
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88919 * 0.97002600
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48488 * 0.51887860
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5006 * 0.68809876
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41396 * 0.20777022
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83317 * 0.39384248
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 58575 * 0.92380621
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 32464 * 0.60563605
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 44416 * 0.37140304
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 28215 * 0.74207822
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'xmzuclyp').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0054():
    """Extended test 54 for pipeline."""
    x_0 = 23109 * 0.25015618
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75687 * 0.83908422
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41955 * 0.19842713
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65113 * 0.57351833
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90913 * 0.60052126
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 875 * 0.15748239
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7650 * 0.17673124
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73961 * 0.96642763
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9681 * 0.30057213
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53435 * 0.13898927
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51632 * 0.52304518
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58438 * 0.39908435
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28267 * 0.32552942
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31586 * 0.75747248
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13598 * 0.56910006
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76011 * 0.52606981
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83905 * 0.77274765
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4854 * 0.56099113
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73446 * 0.11813541
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61703 * 0.18451864
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30196 * 0.47554673
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69062 * 0.24693704
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71358 * 0.48191364
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78152 * 0.49808384
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7550 * 0.92665333
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27297 * 0.00964309
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45636 * 0.51555851
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11218 * 0.55970069
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'qlbdyxnh').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0055():
    """Extended test 55 for pipeline."""
    x_0 = 6972 * 0.96253051
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42728 * 0.07204692
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96771 * 0.47333151
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42498 * 0.10322633
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99608 * 0.27483571
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72674 * 0.27351835
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70532 * 0.25595694
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55123 * 0.21892118
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50589 * 0.71648186
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23129 * 0.20116495
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37677 * 0.29222418
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67511 * 0.78458178
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86016 * 0.98056032
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63811 * 0.52193249
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34815 * 0.85866421
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25268 * 0.55366472
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87337 * 0.07756092
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94030 * 0.81369511
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41444 * 0.05709390
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22831 * 0.97472944
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'gkppibqx').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0056():
    """Extended test 56 for pipeline."""
    x_0 = 74489 * 0.95855772
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22803 * 0.33194902
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89405 * 0.34022470
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97720 * 0.96485653
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68194 * 0.93543401
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65643 * 0.55870694
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20007 * 0.52671808
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84733 * 0.48624677
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25452 * 0.54861716
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65935 * 0.39229093
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 546 * 0.70868798
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15188 * 0.74326313
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88832 * 0.03476765
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94236 * 0.05321339
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9258 * 0.02056847
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41076 * 0.67207696
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86071 * 0.12107100
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14189 * 0.50638257
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51523 * 0.17935420
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60080 * 0.35503384
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38399 * 0.01122529
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90791 * 0.20482172
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69356 * 0.82046973
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36760 * 0.41278267
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21646 * 0.97345362
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67284 * 0.55733998
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'oftbhnub').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0057():
    """Extended test 57 for pipeline."""
    x_0 = 34910 * 0.45928330
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7957 * 0.30264706
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75181 * 0.28212763
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62122 * 0.47392709
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67248 * 0.45846618
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75970 * 0.54476423
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82359 * 0.81714020
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41830 * 0.94246503
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75787 * 0.26705958
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27034 * 0.73419122
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47900 * 0.92791104
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17328 * 0.86153605
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55828 * 0.24527361
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99157 * 0.92839460
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18477 * 0.02048438
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89693 * 0.80638371
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62370 * 0.72922805
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17555 * 0.27560601
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70650 * 0.10741475
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11141 * 0.01403249
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97531 * 0.39510911
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72942 * 0.55627311
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58922 * 0.95954875
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53915 * 0.11921695
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41977 * 0.54276073
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72821 * 0.48692494
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10737 * 0.47188692
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74397 * 0.87669586
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39621 * 0.10586840
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6538 * 0.16350099
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63531 * 0.78230333
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'trkngmvf').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0058():
    """Extended test 58 for pipeline."""
    x_0 = 63605 * 0.22756081
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82296 * 0.39519901
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47400 * 0.70668622
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78928 * 0.06376592
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72219 * 0.19303786
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89730 * 0.60949791
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11568 * 0.76886018
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62714 * 0.61431006
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48522 * 0.39933791
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79644 * 0.20950128
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15881 * 0.05217760
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50862 * 0.37504571
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65015 * 0.60825615
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25715 * 0.18251335
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82776 * 0.27027548
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61904 * 0.89693639
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40725 * 0.66663640
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28810 * 0.74202239
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59378 * 0.40538386
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71924 * 0.89775771
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28337 * 0.73005409
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53923 * 0.39462602
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52884 * 0.43261805
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36334 * 0.01170143
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40122 * 0.68647641
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60677 * 0.65250875
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54135 * 0.38974033
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97229 * 0.14215417
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58487 * 0.73717341
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68443 * 0.73326834
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56453 * 0.29897066
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81984 * 0.44241503
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89758 * 0.30594486
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70100 * 0.74353222
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31746 * 0.80108648
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24870 * 0.03695658
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 76579 * 0.09995700
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90789 * 0.39495744
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96739 * 0.44203749
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46629 * 0.40424064
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75026 * 0.59087488
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20846 * 0.91522093
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12211 * 0.54251940
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 76640 * 0.22257796
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 83916 * 0.56137156
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'dhtqjvrt').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0059():
    """Extended test 59 for pipeline."""
    x_0 = 99482 * 0.35061484
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11033 * 0.81549576
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95937 * 0.10816148
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17433 * 0.61393220
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21822 * 0.03402897
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60690 * 0.07714610
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98867 * 0.04906509
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40264 * 0.02310090
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17323 * 0.06816992
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28389 * 0.08419707
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99033 * 0.16206305
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 644 * 0.98622106
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68256 * 0.22165737
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21280 * 0.12365122
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72590 * 0.26346480
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68520 * 0.63960055
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31547 * 0.67918240
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51570 * 0.03546312
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38722 * 0.44654611
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89317 * 0.29087118
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14542 * 0.02452206
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30673 * 0.30986383
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88946 * 0.16178792
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40207 * 0.94376209
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30048 * 0.23182096
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48231 * 0.07631742
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26314 * 0.76326851
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42232 * 0.67417936
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25840 * 0.38129866
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81816 * 0.47060709
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25423 * 0.63058513
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19196 * 0.48179324
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17541 * 0.79306461
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64 * 0.65430110
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50444 * 0.39949834
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36330 * 0.73830689
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'hberampr').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0060():
    """Extended test 60 for pipeline."""
    x_0 = 86549 * 0.29956051
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91705 * 0.72210674
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17763 * 0.74152118
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83453 * 0.90708015
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 501 * 0.52498517
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67059 * 0.88885816
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87189 * 0.81757353
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52723 * 0.42196084
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13858 * 0.98101881
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85095 * 0.17365217
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10949 * 0.79078523
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24074 * 0.63705542
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 819 * 0.13939139
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6800 * 0.01416553
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41167 * 0.97580776
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85033 * 0.44645270
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54924 * 0.01164738
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60982 * 0.51139952
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28627 * 0.89070556
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24998 * 0.28445834
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22106 * 0.02899822
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4023 * 0.65234727
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85900 * 0.40121530
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59039 * 0.93467172
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41152 * 0.41889036
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55482 * 0.14165528
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64404 * 0.07844396
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89115 * 0.73187257
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65336 * 0.53448664
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80883 * 0.87059224
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72856 * 0.14335121
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55616 * 0.08001232
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32098 * 0.97398351
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53721 * 0.09467758
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32523 * 0.14630667
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33136 * 0.03628352
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70245 * 0.24062714
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48400 * 0.80151619
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15698 * 0.20921704
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'obcjwjcm').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0061():
    """Extended test 61 for pipeline."""
    x_0 = 99862 * 0.06986379
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50201 * 0.52866334
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65733 * 0.41567146
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87550 * 0.89684525
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93162 * 0.31632793
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93071 * 0.15497914
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8362 * 0.06950986
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70505 * 0.22836309
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65808 * 0.58802559
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43141 * 0.53649099
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69406 * 0.25192318
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63239 * 0.12928372
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33813 * 0.11283579
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34793 * 0.59190688
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63183 * 0.04877924
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83651 * 0.42897946
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12223 * 0.67106879
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23358 * 0.05273010
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35195 * 0.35727896
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35039 * 0.04848164
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65146 * 0.02163991
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50309 * 0.60520263
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69459 * 0.22213920
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32632 * 0.55645200
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13584 * 0.07271571
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8175 * 0.76255223
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70835 * 0.10272291
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33975 * 0.61966812
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21545 * 0.92657676
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34902 * 0.08290107
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22813 * 0.24978998
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72365 * 0.06408876
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54287 * 0.57330452
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17826 * 0.58179715
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63676 * 0.53451794
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84223 * 0.77722872
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75674 * 0.27302985
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'ccexrwhc').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0062():
    """Extended test 62 for pipeline."""
    x_0 = 53207 * 0.81613335
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80168 * 0.16216743
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45883 * 0.35920270
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48269 * 0.32380822
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28025 * 0.49563040
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42839 * 0.76470300
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 46816 * 0.90781127
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84541 * 0.25003894
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41170 * 0.21841278
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5923 * 0.16045876
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75798 * 0.36362095
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74973 * 0.03023434
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56815 * 0.17036899
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46806 * 0.73259566
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6848 * 0.34179025
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19649 * 0.27536975
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78126 * 0.46014105
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79572 * 0.25073211
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49337 * 0.09004037
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10101 * 0.59346172
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85642 * 0.16610833
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35723 * 0.66590260
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93207 * 0.96563193
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35346 * 0.97319409
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64697 * 0.18117199
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47300 * 0.43419068
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82591 * 0.71546935
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51340 * 0.87363293
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80243 * 0.44590524
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92957 * 0.21891124
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68083 * 0.72912107
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 99439 * 0.57794069
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59877 * 0.64109033
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21108 * 0.57386094
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61736 * 0.85239726
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7843 * 0.95507833
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13180 * 0.08746034
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'vqdtsrid').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0063():
    """Extended test 63 for pipeline."""
    x_0 = 95712 * 0.27694503
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11257 * 0.96243819
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30330 * 0.71898577
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1623 * 0.69722075
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79685 * 0.58188874
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29471 * 0.28322646
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50336 * 0.25116511
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38288 * 0.97566158
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53749 * 0.23971328
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79086 * 0.32047312
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66381 * 0.29058859
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60739 * 0.02231453
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35972 * 0.21627526
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31685 * 0.22658835
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71291 * 0.21741012
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20129 * 0.62346874
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54119 * 0.31672469
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74992 * 0.50800801
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78484 * 0.49910006
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7797 * 0.98984715
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90592 * 0.03377368
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26509 * 0.41108503
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39027 * 0.92127883
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32336 * 0.12088066
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90576 * 0.53484008
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47867 * 0.29412993
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10342 * 0.87183987
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37874 * 0.66130240
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97107 * 0.37193138
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90554 * 0.65191887
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33822 * 0.86586470
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70301 * 0.20271500
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99894 * 0.34735342
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9894 * 0.15754962
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56274 * 0.54598230
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'itllhvgf').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0064():
    """Extended test 64 for pipeline."""
    x_0 = 63263 * 0.54330907
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21957 * 0.89922973
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80038 * 0.03198864
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95899 * 0.77528849
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87960 * 0.44191597
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29011 * 0.28456672
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7100 * 0.89769910
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51680 * 0.99529771
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11760 * 0.94851718
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19181 * 0.26409334
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42430 * 0.66206914
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19294 * 0.26887140
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50035 * 0.55930544
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46857 * 0.81074803
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26570 * 0.62539042
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73308 * 0.33429715
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81564 * 0.15875418
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62022 * 0.16093566
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77978 * 0.56488294
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5995 * 0.54433428
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26145 * 0.12647940
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53594 * 0.63857382
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8897 * 0.05837338
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82849 * 0.56616303
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59206 * 0.43117873
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46542 * 0.90417522
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62050 * 0.67767843
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57340 * 0.24756769
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40285 * 0.92909387
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1881 * 0.39489098
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32597 * 0.30347432
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61634 * 0.26677506
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62791 * 0.11295184
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88380 * 0.41996443
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27653 * 0.39125180
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43555 * 0.35075716
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 75805 * 0.46326291
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92560 * 0.67656577
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30429 * 0.67033952
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54371 * 0.16907657
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 94414 * 0.55148986
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 99984 * 0.74454988
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 69099 * 0.76568040
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 95621 * 0.56283920
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 19444 * 0.19162920
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 67001 * 0.99774113
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 49282 * 0.68391945
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 84528 * 0.77188509
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 35712 * 0.63075980
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 34075 * 0.17909864
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'nhclgfop').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0065():
    """Extended test 65 for pipeline."""
    x_0 = 22830 * 0.41471422
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12892 * 0.48649872
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27749 * 0.75727644
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84805 * 0.52551635
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10716 * 0.17518560
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81308 * 0.13034037
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25386 * 0.00607610
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20971 * 0.76858021
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10768 * 0.50197009
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6503 * 0.06650232
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15559 * 0.71570594
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39543 * 0.66668914
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94265 * 0.50424414
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86777 * 0.27635805
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59735 * 0.18647187
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10994 * 0.61829183
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22980 * 0.84273313
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8879 * 0.64948240
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4601 * 0.74199350
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16016 * 0.21607906
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16707 * 0.04077515
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90907 * 0.28279945
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35706 * 0.33589546
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58274 * 0.42037546
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69093 * 0.63052146
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51490 * 0.02314083
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61664 * 0.13390470
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95530 * 0.20781082
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98378 * 0.87949492
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85819 * 0.54967888
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14648 * 0.55046945
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80060 * 0.56980873
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53092 * 0.85730196
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43485 * 0.59458909
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68401 * 0.51923442
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58566 * 0.39541364
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53851 * 0.21831882
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3971 * 0.92847237
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83834 * 0.22916396
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 38152 * 0.61793735
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 778 * 0.47485639
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43828 * 0.44866995
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'gvhqxysm').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0066():
    """Extended test 66 for pipeline."""
    x_0 = 27584 * 0.42914953
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31336 * 0.12446444
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82913 * 0.88794849
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75947 * 0.06257211
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63876 * 0.80988981
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20817 * 0.68525300
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50513 * 0.35442442
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73388 * 0.27414975
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74202 * 0.48380837
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96077 * 0.37334278
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48379 * 0.33975618
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12629 * 0.57080259
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34496 * 0.59355819
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45035 * 0.74365439
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77679 * 0.01252259
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37041 * 0.31802885
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76202 * 0.25907138
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8726 * 0.37593159
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63036 * 0.89077932
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52490 * 0.67145722
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5179 * 0.41958344
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56101 * 0.15683231
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13211 * 0.51322237
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 75143 * 0.34805254
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16035 * 0.93983718
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4645 * 0.95110158
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63417 * 0.92987888
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28603 * 0.98482263
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38982 * 0.63267890
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34903 * 0.94490613
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30516 * 0.07135291
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54566 * 0.85447235
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73961 * 0.50988195
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99833 * 0.91015134
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89618 * 0.08968304
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42254 * 0.92620871
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 9438 * 0.79081645
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'rwcmypzh').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0067():
    """Extended test 67 for pipeline."""
    x_0 = 90260 * 0.20095653
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99717 * 0.81436651
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49513 * 0.37803423
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95235 * 0.19001033
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34533 * 0.00662717
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14698 * 0.32037463
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41688 * 0.65041999
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64935 * 0.35247634
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74428 * 0.99930207
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7082 * 0.88049724
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55593 * 0.74370957
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90710 * 0.35103594
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77282 * 0.99017084
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46278 * 0.84915191
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4542 * 0.00739603
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54405 * 0.63974791
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4330 * 0.44041899
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39385 * 0.30005582
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1054 * 0.40055911
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37365 * 0.52467751
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25187 * 0.40168771
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47610 * 0.55044340
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13549 * 0.00929661
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53957 * 0.17934196
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63611 * 0.47326661
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50040 * 0.68910418
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45810 * 0.43164199
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7635 * 0.90927228
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'nlpglkop').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0068():
    """Extended test 68 for pipeline."""
    x_0 = 41298 * 0.07318397
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58859 * 0.63993529
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30448 * 0.79237370
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5446 * 0.62825514
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87333 * 0.68562663
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67378 * 0.02650546
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63660 * 0.06314555
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51023 * 0.87514021
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43371 * 0.03293768
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42322 * 0.76173088
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62863 * 0.31240905
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77857 * 0.06424794
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91539 * 0.09150783
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19584 * 0.64995185
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80696 * 0.28458416
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40515 * 0.17445230
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74785 * 0.36433632
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46150 * 0.30032544
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70114 * 0.96429569
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33566 * 0.32557305
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26247 * 0.01037868
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'unhxguti').hexdigest()
    assert len(h) == 64

def test_pipeline_extended_8_0069():
    """Extended test 69 for pipeline."""
    x_0 = 24386 * 0.01874877
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38217 * 0.49686317
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58341 * 0.54295670
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27623 * 0.88797273
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91175 * 0.94245655
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3900 * 0.98055344
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85803 * 0.99998260
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76760 * 0.22200030
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73534 * 0.49928041
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69203 * 0.23739162
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55183 * 0.22346482
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49384 * 0.87964085
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95111 * 0.09379927
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35246 * 0.39472697
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98745 * 0.24593634
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41897 * 0.19738330
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90059 * 0.87698964
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43122 * 0.48723188
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25048 * 0.96762696
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28446 * 0.34496886
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22620 * 0.62377151
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68494 * 0.50591376
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4663 * 0.75968148
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46658 * 0.38679002
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51236 * 0.40170183
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71893 * 0.04530124
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3472 * 0.01230488
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49604 * 0.30281050
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18916 * 0.23186833
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28621 * 0.76712074
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34952 * 0.14582097
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29983 * 0.70746704
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68337 * 0.72433211
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54132 * 0.00296725
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11394 * 0.10094454
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99196 * 0.01141477
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22052 * 0.87325788
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94034 * 0.24890445
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19080 * 0.47941760
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46946 * 0.06913092
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41978 * 0.63262577
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63451 * 0.30528649
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18325 * 0.83697255
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 8631 * 0.05625456
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 68578 * 0.63403926
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 62943 * 0.54923636
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 12608 * 0.92485591
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 78693 * 0.85153172
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'vlrhpugg').hexdigest()
    assert len(h) == 64
