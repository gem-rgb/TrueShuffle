"""Extended tests for billing suite 7."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_billing_extended_7_0000():
    """Extended test 0 for billing."""
    x_0 = 88755 * 0.43455319
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47617 * 0.54894701
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51941 * 0.00948537
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5895 * 0.12581516
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9835 * 0.64447548
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47657 * 0.65376925
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26405 * 0.95096024
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19766 * 0.78505556
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86624 * 0.58255860
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17723 * 0.52385778
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3027 * 0.76543947
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45201 * 0.59168177
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99297 * 0.71137074
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22781 * 0.70042657
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86479 * 0.20432425
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34148 * 0.58074308
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7214 * 0.16027965
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29389 * 0.42144415
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90250 * 0.75963482
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59141 * 0.84322453
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72642 * 0.95016369
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77166 * 0.76543034
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48350 * 0.47294509
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3394 * 0.65760908
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69747 * 0.52097298
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41371 * 0.57427975
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19329 * 0.43603102
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'pikhjcxp').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0001():
    """Extended test 1 for billing."""
    x_0 = 89110 * 0.53132930
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45265 * 0.51818475
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53829 * 0.03690813
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82274 * 0.75276862
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56555 * 0.85607711
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30435 * 0.69443557
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89583 * 0.08826647
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18611 * 0.65173999
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86719 * 0.03462369
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99604 * 0.35471209
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56994 * 0.71445384
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17060 * 0.14305345
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81029 * 0.41203951
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28223 * 0.96439875
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65418 * 0.28832636
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50110 * 0.23238791
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91355 * 0.64633531
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22783 * 0.70069683
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66488 * 0.52617215
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38598 * 0.77747010
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55848 * 0.22614553
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36163 * 0.08576820
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92065 * 0.81496355
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49421 * 0.67417583
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40253 * 0.16163212
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46117 * 0.66499122
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4600 * 0.89897066
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15 * 0.57287735
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58980 * 0.01650106
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13634 * 0.69070218
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23002 * 0.74479389
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9279 * 0.43194796
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93862 * 0.43202531
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99789 * 0.23484231
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48481 * 0.93796969
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62600 * 0.50642027
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17778 * 0.22985767
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11909 * 0.40742639
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83776 * 0.63293409
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59249 * 0.29387139
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4958 * 0.78276967
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60320 * 0.20496048
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1193 * 0.21086047
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 60920 * 0.51395185
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 3939 * 0.05933973
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 50764 * 0.32304968
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 64794 * 0.64022253
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 54474 * 0.28919038
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 78841 * 0.07490427
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'zbknnuwq').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0002():
    """Extended test 2 for billing."""
    x_0 = 68424 * 0.80534821
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15024 * 0.96810295
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47700 * 0.26796904
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99401 * 0.13009338
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83254 * 0.24784221
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14753 * 0.82689542
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24581 * 0.50679170
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85883 * 0.71618363
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52600 * 0.31872709
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35467 * 0.48306638
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82414 * 0.26302751
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62333 * 0.01885445
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61890 * 0.42357982
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48808 * 0.58434730
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61679 * 0.83706316
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39430 * 0.89977632
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72521 * 0.16910563
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97490 * 0.07721947
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53863 * 0.72337163
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52401 * 0.64928803
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28597 * 0.47254670
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30011 * 0.24519676
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72663 * 0.15976405
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41498 * 0.33712368
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12808 * 0.98335122
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57999 * 0.50627473
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66261 * 0.48518110
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22728 * 0.96496276
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12066 * 0.66554589
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66264 * 0.16835633
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47834 * 0.14080473
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56252 * 0.25462347
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88267 * 0.01811222
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55886 * 0.21308342
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82523 * 0.74858012
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96612 * 0.31992340
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27432 * 0.40318432
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98581 * 0.62752238
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96875 * 0.60088922
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 95232 * 0.42618164
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'jyrjcipn').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0003():
    """Extended test 3 for billing."""
    x_0 = 70222 * 0.77207576
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58438 * 0.52716590
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97651 * 0.88086359
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43590 * 0.34403178
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 521 * 0.62996973
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84033 * 0.77122805
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95800 * 0.74276229
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60118 * 0.28794412
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47036 * 0.54121730
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50632 * 0.08045284
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84731 * 0.11803765
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16617 * 0.85426994
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52242 * 0.55498047
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37073 * 0.08055829
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24529 * 0.73397979
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20651 * 0.05859676
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12971 * 0.97962147
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77575 * 0.06369809
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6225 * 0.18829555
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57249 * 0.85261816
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79785 * 0.71735656
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'btanvzau').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0004():
    """Extended test 4 for billing."""
    x_0 = 92591 * 0.44454105
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75527 * 0.66221637
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28043 * 0.09270208
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73605 * 0.72395653
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11801 * 0.32264868
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58457 * 0.56077360
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61519 * 0.25751302
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66286 * 0.50020127
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7579 * 0.44741626
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60982 * 0.84663149
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55406 * 0.17182374
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68767 * 0.11675505
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17325 * 0.00460211
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24976 * 0.42991896
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98931 * 0.09067349
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59497 * 0.11171604
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61385 * 0.91018214
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44667 * 0.33499530
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95682 * 0.24237557
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67572 * 0.09128190
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78294 * 0.15302289
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76364 * 0.45300587
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31379 * 0.89893950
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'pdykvtom').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0005():
    """Extended test 5 for billing."""
    x_0 = 83130 * 0.43223477
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38135 * 0.24883611
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40665 * 0.79135702
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18187 * 0.57681733
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43598 * 0.62924101
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5931 * 0.18018706
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88537 * 0.77653698
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23122 * 0.54775763
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76505 * 0.82752295
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67882 * 0.57894964
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73106 * 0.72233065
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97808 * 0.04904399
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70299 * 0.22129330
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42993 * 0.08221060
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92308 * 0.58712466
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17808 * 0.13733235
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83058 * 0.49680891
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35948 * 0.43662000
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58381 * 0.11791806
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47264 * 0.07654082
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18175 * 0.77499243
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38252 * 0.74946950
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87807 * 0.50581457
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64546 * 0.99392652
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57648 * 0.54533262
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39749 * 0.55265903
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5786 * 0.69921345
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51095 * 0.58485402
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57096 * 0.06237747
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46269 * 0.04313019
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88596 * 0.54216339
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48963 * 0.47694241
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81994 * 0.08622160
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62350 * 0.88996705
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43175 * 0.74213085
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ptqytrqp').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0006():
    """Extended test 6 for billing."""
    x_0 = 85317 * 0.83508978
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28152 * 0.51147825
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46322 * 0.33376947
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76645 * 0.57400628
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99901 * 0.07500296
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78423 * 0.92254348
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76671 * 0.19871216
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59019 * 0.99424882
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33230 * 0.44106461
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40688 * 0.35154187
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93057 * 0.15729596
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53651 * 0.32956642
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32657 * 0.79788079
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18852 * 0.54682646
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20004 * 0.06313206
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3546 * 0.17073977
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79779 * 0.96835412
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64413 * 0.78538345
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81559 * 0.82678966
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71441 * 0.80848333
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20250 * 0.34933883
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'axqvnlci').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0007():
    """Extended test 7 for billing."""
    x_0 = 7846 * 0.43106191
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28191 * 0.88782474
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94143 * 0.66907893
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36649 * 0.85111078
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25056 * 0.52675342
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83414 * 0.68842134
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42736 * 0.78735418
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22540 * 0.44732684
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36868 * 0.18458362
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81115 * 0.28486973
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36645 * 0.30842014
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28583 * 0.23823097
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38889 * 0.52367853
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40939 * 0.81726640
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58168 * 0.38374456
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11814 * 0.63989826
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86959 * 0.76890392
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54699 * 0.97187541
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91392 * 0.67988921
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29233 * 0.51707954
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79466 * 0.10645523
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89104 * 0.71301443
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77286 * 0.32925162
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35868 * 0.25771502
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56950 * 0.02218690
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6930 * 0.00459094
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54253 * 0.82373523
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95634 * 0.91587796
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28287 * 0.25655973
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79531 * 0.32780596
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 40758 * 0.00102606
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89775 * 0.58251000
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'nidouxqr').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0008():
    """Extended test 8 for billing."""
    x_0 = 17264 * 0.03656539
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32567 * 0.92402122
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39002 * 0.01813424
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39480 * 0.14694334
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28956 * 0.67498768
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37727 * 0.58285822
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88195 * 0.71188785
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30940 * 0.83563469
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53911 * 0.91293064
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99323 * 0.41883815
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81207 * 0.91453423
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63659 * 0.74925322
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12631 * 0.54342975
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60327 * 0.25623647
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94858 * 0.91955281
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81591 * 0.88996100
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91166 * 0.19345293
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 4283 * 0.41902556
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4231 * 0.21458144
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19002 * 0.84209398
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4919 * 0.07862465
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61167 * 0.69951332
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23332 * 0.03425522
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7059 * 0.18710185
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42674 * 0.22379764
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'oejzzpfm').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0009():
    """Extended test 9 for billing."""
    x_0 = 65395 * 0.01407815
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 943 * 0.11780341
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4118 * 0.52468239
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21478 * 0.69281301
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10853 * 0.19524063
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 584 * 0.61725222
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53194 * 0.35885626
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68960 * 0.44181277
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50418 * 0.68898301
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76841 * 0.38344593
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71431 * 0.79666143
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53000 * 0.10732628
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51466 * 0.19115925
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1763 * 0.48018633
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35839 * 0.66368905
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70837 * 0.02921996
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37029 * 0.35838928
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93049 * 0.61989041
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28549 * 0.27714285
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49525 * 0.92513506
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85526 * 0.16895024
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77097 * 0.92592020
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95896 * 0.47941331
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95595 * 0.36618478
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83799 * 0.16946285
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35080 * 0.36397562
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84698 * 0.64868159
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14328 * 0.74884791
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43716 * 0.97459477
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87171 * 0.98323416
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77084 * 0.78737911
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6637 * 0.39728639
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35933 * 0.79778027
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64878 * 0.05111950
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50347 * 0.90515885
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87233 * 0.58013958
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43488 * 0.75929498
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21102 * 0.09804489
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 26273 * 0.29311279
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 8105 * 0.38000613
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48177 * 0.56787930
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5919 * 0.38091154
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 31251 * 0.88145156
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 73463 * 0.39530497
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92555 * 0.85334414
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 42368 * 0.42855919
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'hbwpsnuc').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0010():
    """Extended test 10 for billing."""
    x_0 = 52256 * 0.74339505
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29593 * 0.61449965
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49914 * 0.79694887
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 454 * 0.61691839
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93941 * 0.61613590
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61118 * 0.24197667
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63654 * 0.56504259
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9052 * 0.76643127
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91428 * 0.20201074
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34643 * 0.08134313
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17815 * 0.94232970
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93989 * 0.25520141
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85229 * 0.15733812
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24831 * 0.14680288
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69266 * 0.48775437
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6756 * 0.39166458
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48397 * 0.56053035
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3927 * 0.96264908
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88722 * 0.88587338
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63737 * 0.69736306
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43370 * 0.31858148
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90983 * 0.08946629
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64722 * 0.41136594
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22322 * 0.22044008
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97806 * 0.70989148
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 63248 * 0.48466276
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18753 * 0.54575729
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'maqjljhx').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0011():
    """Extended test 11 for billing."""
    x_0 = 22148 * 0.18484222
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42050 * 0.42574286
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79315 * 0.73406246
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1717 * 0.29766707
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83401 * 0.35759371
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83722 * 0.08735962
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93137 * 0.55121965
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38625 * 0.67952566
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91187 * 0.96296008
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15813 * 0.60007004
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45516 * 0.57626960
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29146 * 0.13544440
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51953 * 0.68044791
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53069 * 0.37797764
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83730 * 0.51105764
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48489 * 0.98441075
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1857 * 0.88019437
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17446 * 0.90067573
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80549 * 0.29681848
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24082 * 0.39238228
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71481 * 0.90048387
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44032 * 0.18687280
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89995 * 0.44334477
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11038 * 0.47696527
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10168 * 0.32058572
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11075 * 0.70649360
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75826 * 0.82454369
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89305 * 0.86309929
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94430 * 0.20971217
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45563 * 0.10479097
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55807 * 0.94214071
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'ecnjrxuz').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0012():
    """Extended test 12 for billing."""
    x_0 = 86782 * 0.24653197
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85430 * 0.84526861
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66973 * 0.40205181
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50762 * 0.97569502
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63182 * 0.22954802
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36848 * 0.19459366
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65249 * 0.61160943
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12675 * 0.44819668
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62101 * 0.30080794
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91114 * 0.02330510
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15330 * 0.38588814
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44884 * 0.27274601
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17787 * 0.03051496
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39835 * 0.87525432
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91361 * 0.15225801
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10549 * 0.52087300
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22095 * 0.54609727
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91632 * 0.61978795
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97943 * 0.13542383
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42318 * 0.12951324
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41852 * 0.90105407
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31518 * 0.31137313
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5683 * 0.88318596
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48459 * 0.10507548
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6925 * 0.72604829
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4841 * 0.39451563
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13243 * 0.66721281
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12433 * 0.54979859
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6535 * 0.86276729
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80132 * 0.28612928
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9833 * 0.16616340
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29813 * 0.42854032
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32895 * 0.89748983
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 108 * 0.77005900
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18427 * 0.75818315
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 42646 * 0.86996880
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98113 * 0.53531310
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25637 * 0.05303671
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79663 * 0.42027501
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67201 * 0.40676396
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 24747 * 0.71431034
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4239 * 0.69965699
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 98730 * 0.07884497
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 76799 * 0.22117270
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61802 * 0.74179738
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 16989 * 0.14817939
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 66269 * 0.83284214
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 26376 * 0.30718497
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 59043 * 0.07178653
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 50615 * 0.90156705
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'tdxeyptt').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0013():
    """Extended test 13 for billing."""
    x_0 = 48066 * 0.22059967
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95373 * 0.36485426
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86437 * 0.39343919
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90121 * 0.05309686
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4974 * 0.80777365
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52429 * 0.05953681
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43560 * 0.13016439
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1640 * 0.08843814
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98529 * 0.65256042
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94252 * 0.44086208
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50754 * 0.96953376
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80646 * 0.96342094
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10390 * 0.84873027
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67253 * 0.45073985
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35152 * 0.30957071
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94207 * 0.46164824
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16779 * 0.15812733
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25515 * 0.99851783
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49069 * 0.08051588
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14509 * 0.77964863
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56895 * 0.31703811
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17399 * 0.18811901
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12648 * 0.73948344
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4831 * 0.74101798
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73513 * 0.26636961
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40069 * 0.07959033
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12694 * 0.60526238
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14837 * 0.41491085
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76849 * 0.57384282
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 26587 * 0.91793092
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51953 * 0.82246152
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44748 * 0.73322564
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88382 * 0.46244813
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69756 * 0.67245575
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17907 * 0.93117815
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62955 * 0.99132075
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99086 * 0.31831517
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34037 * 0.62912640
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 7408 * 0.59933792
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 639 * 0.83745556
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13085 * 0.86555916
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 83636 * 0.33448486
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13294 * 0.17072490
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 45221 * 0.64616325
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 83199 * 0.77582143
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 63143 * 0.69748475
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 55090 * 0.67239085
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'vgvqplyq').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0014():
    """Extended test 14 for billing."""
    x_0 = 26645 * 0.06262886
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11495 * 0.76157086
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14630 * 0.89385386
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71118 * 0.09474419
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22119 * 0.95608074
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35445 * 0.87101346
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89904 * 0.31785870
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83611 * 0.15179329
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46060 * 0.92715578
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8162 * 0.60794085
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53956 * 0.17782510
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45972 * 0.87650524
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23942 * 0.76982153
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53374 * 0.50156528
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10541 * 0.26701192
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73919 * 0.80670822
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3183 * 0.91179956
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25895 * 0.82045859
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91994 * 0.93422430
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44719 * 0.08666395
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77993 * 0.67544750
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31175 * 0.35049214
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34479 * 0.99038668
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30905 * 0.62637374
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8990 * 0.90483483
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62142 * 0.05028687
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21377 * 0.97110483
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22209 * 0.76565937
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95389 * 0.30292601
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99074 * 0.18060288
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11435 * 0.87937248
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'aqdxnpxe').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0015():
    """Extended test 15 for billing."""
    x_0 = 85576 * 0.95118890
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19880 * 0.30044939
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11256 * 0.71982943
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54321 * 0.42497396
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55440 * 0.20819955
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20866 * 0.82376539
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92675 * 0.19781259
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81866 * 0.95880299
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2222 * 0.37204204
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91048 * 0.37424524
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67277 * 0.46985698
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87366 * 0.14182534
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10600 * 0.11300751
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82410 * 0.53589913
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45787 * 0.47243132
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4483 * 0.10472684
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40373 * 0.34073722
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61962 * 0.84061500
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20249 * 0.29542523
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20243 * 0.90424622
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83751 * 0.20345768
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13620 * 0.93287842
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13271 * 0.84506944
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14663 * 0.82922459
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77949 * 0.78463582
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79790 * 0.50328177
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37327 * 0.99649992
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29672 * 0.20532703
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53778 * 0.30974949
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85087 * 0.98916490
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41271 * 0.93372762
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56654 * 0.50448292
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5960 * 0.15867727
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36812 * 0.99095896
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4226 * 0.86408702
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36956 * 0.98732133
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78077 * 0.83397982
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44080 * 0.99951884
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71875 * 0.84433826
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2581 * 0.12237724
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 67680 * 0.70568904
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54 * 0.83790334
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 43456 * 0.99768399
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34610 * 0.22959464
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 51868 * 0.54765555
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 2711 * 0.66508933
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 44194 * 0.65960088
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 57739 * 0.46410154
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'myzvgheo').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0016():
    """Extended test 16 for billing."""
    x_0 = 67032 * 0.69986249
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29749 * 0.81910159
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10489 * 0.96217890
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50596 * 0.27959176
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65378 * 0.18995476
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14554 * 0.73378756
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91247 * 0.53599849
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68491 * 0.77396298
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43497 * 0.27083364
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98838 * 0.52032459
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90952 * 0.64208689
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68540 * 0.77287639
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92466 * 0.74327905
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40963 * 0.09974977
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94898 * 0.79710337
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2704 * 0.46588156
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90426 * 0.94920352
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14470 * 0.06692415
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35572 * 0.15181088
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26294 * 0.74566057
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92970 * 0.62312797
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90071 * 0.11704526
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20651 * 0.40876094
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41215 * 0.13154384
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95843 * 0.24413882
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38547 * 0.70745569
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41843 * 0.92849038
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52207 * 0.75557848
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63050 * 0.73581630
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11855 * 0.36358297
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6534 * 0.81311826
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26846 * 0.52503013
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 32936 * 0.68399298
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13351 * 0.10546293
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89088 * 0.55722615
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81605 * 0.16848586
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70796 * 0.78823382
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94728 * 0.53212035
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1194 * 0.41234901
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23111 * 0.23463788
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 93331 * 0.17668005
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84481 * 0.30674435
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 40207 * 0.42824677
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 55719 * 0.00360720
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 18274 * 0.08513372
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 22970 * 0.02466714
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 59828 * 0.42466293
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 94420 * 0.19929856
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 65139 * 0.17129195
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 36556 * 0.56501693
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'xpxigtgj').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0017():
    """Extended test 17 for billing."""
    x_0 = 34254 * 0.34862054
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56953 * 0.45956327
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22764 * 0.75423899
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62327 * 0.08531880
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37256 * 0.66473515
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57737 * 0.23573686
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11643 * 0.12181292
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46738 * 0.42835330
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57590 * 0.02216564
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79253 * 0.89457160
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69194 * 0.45340862
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1768 * 0.03589416
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31011 * 0.47122088
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58625 * 0.18109730
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32273 * 0.06251394
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62192 * 0.50155657
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46117 * 0.23325592
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45415 * 0.33026219
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84917 * 0.53901047
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44888 * 0.52282060
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74841 * 0.77888983
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87835 * 0.43892827
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6853 * 0.94207568
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9171 * 0.32678357
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10799 * 0.69729649
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85783 * 0.16894347
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84653 * 0.10574235
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99713 * 0.04338077
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9323 * 0.71701198
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80451 * 0.94997336
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24333 * 0.07863808
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51534 * 0.41130595
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22813 * 0.17853091
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77096 * 0.18132038
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54686 * 0.56402807
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'wtqjybdo').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0018():
    """Extended test 18 for billing."""
    x_0 = 85194 * 0.39405454
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12781 * 0.17344309
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7282 * 0.68998641
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61152 * 0.43906631
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46952 * 0.91995230
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10535 * 0.23828392
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30226 * 0.01857131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86599 * 0.79268407
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28471 * 0.60989493
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21053 * 0.39602155
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40092 * 0.87083159
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21624 * 0.18040399
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26827 * 0.14817652
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70215 * 0.87193660
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31922 * 0.93839209
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38307 * 0.89407050
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61073 * 0.23562460
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44821 * 0.97024257
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15347 * 0.19560319
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40161 * 0.85645698
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90100 * 0.71213397
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73032 * 0.89023329
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60099 * 0.30649019
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80110 * 0.39862815
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21965 * 0.74613107
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42262 * 0.85358805
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28522 * 0.52508563
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'yakydynt').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0019():
    """Extended test 19 for billing."""
    x_0 = 94192 * 0.20057406
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95991 * 0.60249255
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1378 * 0.55187264
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72914 * 0.51961996
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3303 * 0.63053196
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37680 * 0.43166956
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43539 * 0.57873019
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29781 * 0.96520172
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8956 * 0.01719957
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29281 * 0.31357233
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58477 * 0.31894951
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98105 * 0.01384268
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94295 * 0.19382028
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3569 * 0.85000208
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1058 * 0.50027427
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72485 * 0.74303658
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33046 * 0.13658502
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39728 * 0.10641565
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5356 * 0.43348416
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6848 * 0.47886886
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67008 * 0.70693328
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73211 * 0.36586642
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53488 * 0.93744270
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62371 * 0.42556011
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77524 * 0.47097256
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68128 * 0.50675686
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69346 * 0.61686809
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12834 * 0.38073233
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10817 * 0.91088372
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47987 * 0.46134013
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17814 * 0.86077536
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43403 * 0.09366601
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11819 * 0.51855062
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6500 * 0.60031491
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20467 * 0.58555162
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61984 * 0.81120392
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88147 * 0.08713437
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16059 * 0.89164991
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25703 * 0.70032822
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66981 * 0.41287047
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 44391 * 0.82599650
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 24298 * 0.44852589
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 98961 * 0.21395111
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 25519 * 0.31206744
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'oliuxgpk').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0020():
    """Extended test 20 for billing."""
    x_0 = 56048 * 0.26771987
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49125 * 0.55030992
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55974 * 0.42823605
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29414 * 0.29714672
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84606 * 0.66666995
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11584 * 0.12217700
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82821 * 0.29094168
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46875 * 0.86219228
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48251 * 0.08270398
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70178 * 0.37942369
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 376 * 0.78925323
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92371 * 0.80789820
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22471 * 0.25480303
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95667 * 0.80577594
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89542 * 0.19885207
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53657 * 0.85476261
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67813 * 0.13015749
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75363 * 0.26869323
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6196 * 0.48413709
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45948 * 0.75178383
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93284 * 0.10059468
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63406 * 0.99076049
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24509 * 0.09290410
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30877 * 0.16869391
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30509 * 0.99676333
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40854 * 0.30432635
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52545 * 0.34514673
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57171 * 0.06416415
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15378 * 0.69585768
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16644 * 0.99685539
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51724 * 0.89077485
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6737 * 0.19930472
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79111 * 0.26084030
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45068 * 0.40290324
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80769 * 0.22448234
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61224 * 0.93866572
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71755 * 0.87126510
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33419 * 0.93333026
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43091 * 0.32933511
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45973 * 0.54076987
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6006 * 0.98162993
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 78510 * 0.59191287
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 94273 * 0.65991603
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 224 * 0.86750884
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79835 * 0.83326677
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 13190 * 0.18141240
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'fhhwzuic').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0021():
    """Extended test 21 for billing."""
    x_0 = 70299 * 0.10990104
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 881 * 0.89244311
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52989 * 0.78951864
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17536 * 0.17543967
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97036 * 0.96345841
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6676 * 0.96164142
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98519 * 0.54647472
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49772 * 0.52749273
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12368 * 0.99712148
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33609 * 0.91632643
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82225 * 0.74572987
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30877 * 0.42624828
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18660 * 0.43951550
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52319 * 0.59111962
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36544 * 0.27259140
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79266 * 0.68819142
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84694 * 0.10624492
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8268 * 0.23365642
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10935 * 0.31855918
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69311 * 0.64375901
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57575 * 0.86323659
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31587 * 0.44642664
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71474 * 0.14387389
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88507 * 0.78208721
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69025 * 0.52221256
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30440 * 0.86705268
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16175 * 0.93280674
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61554 * 0.30217054
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24079 * 0.24299213
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75656 * 0.03925100
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19464 * 0.98569402
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 55786 * 0.52895521
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57604 * 0.34083194
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47614 * 0.82882835
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69422 * 0.62135585
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95392 * 0.80126083
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71415 * 0.78202246
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89328 * 0.76041502
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24032 * 0.79655098
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93349 * 0.37883021
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77595 * 0.69296859
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77452 * 0.19440507
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41517 * 0.68092409
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'wloleqro').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0022():
    """Extended test 22 for billing."""
    x_0 = 21865 * 0.96170065
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31023 * 0.47600387
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8433 * 0.49784363
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5315 * 0.61492361
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62269 * 0.10404862
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56390 * 0.02007061
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4212 * 0.50871116
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54303 * 0.05573968
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23411 * 0.44886827
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42786 * 0.79944630
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97064 * 0.73253450
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71911 * 0.78643871
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68766 * 0.04112538
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75257 * 0.86949189
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95111 * 0.11862359
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23258 * 0.42785326
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 262 * 0.71146788
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79211 * 0.04860958
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60792 * 0.09022602
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8832 * 0.68741157
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18195 * 0.45458709
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80898 * 0.53136672
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64578 * 0.58294318
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92533 * 0.06119285
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26159 * 0.08371614
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8067 * 0.65702324
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30810 * 0.93309002
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23499 * 0.88962905
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35743 * 0.15893667
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66977 * 0.32205923
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78710 * 0.54662049
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51156 * 0.14952291
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49035 * 0.46102843
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95436 * 0.44209329
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71175 * 0.56827807
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83825 * 0.74352434
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96957 * 0.32631523
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 262 * 0.37305661
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92670 * 0.79352269
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34598 * 0.20463732
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89340 * 0.12030005
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 23779 * 0.59167923
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 90538 * 0.83779434
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 26113 * 0.45942606
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 85197 * 0.20893189
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 97664 * 0.35460758
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 27988 * 0.72434285
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 381 * 0.83535907
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 99107 * 0.36888148
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 46961 * 0.08623346
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'pztyasci').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0023():
    """Extended test 23 for billing."""
    x_0 = 37165 * 0.63615672
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85106 * 0.42005921
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79276 * 0.76973458
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96398 * 0.55149138
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66745 * 0.69763372
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63079 * 0.57357762
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39762 * 0.41356193
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70313 * 0.51911407
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86337 * 0.60231406
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41810 * 0.99254043
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75126 * 0.70924500
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13415 * 0.31073922
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81841 * 0.19534745
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28613 * 0.28986868
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55143 * 0.39941722
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4242 * 0.19426958
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74713 * 0.72751637
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49917 * 0.66531061
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81358 * 0.73258152
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30898 * 0.74309733
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40582 * 0.83615673
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69518 * 0.02663578
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24033 * 0.26258314
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66504 * 0.76777445
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50472 * 0.81854616
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43163 * 0.51300779
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37969 * 0.81369221
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57335 * 0.59604156
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21106 * 0.92022797
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96870 * 0.88493819
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64672 * 0.35635135
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28683 * 0.60998913
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24677 * 0.46588769
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6616 * 0.40986010
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33448 * 0.90183165
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96086 * 0.46301564
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69742 * 0.96718162
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32300 * 0.99638732
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43921 * 0.38998449
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98250 * 0.59616355
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69364 * 0.28696051
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 37521 * 0.21513164
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 52753 * 0.76442325
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 81515 * 0.24986777
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35192 * 0.12108190
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 67887 * 0.08425272
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 13336 * 0.99072951
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 56771 * 0.77687823
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 12805 * 0.84968709
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 36192 * 0.72756435
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'canbgmuo').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0024():
    """Extended test 24 for billing."""
    x_0 = 87620 * 0.54336126
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1725 * 0.81115294
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64958 * 0.99308129
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31376 * 0.11169768
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68792 * 0.86723419
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24224 * 0.46601432
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54355 * 0.23927894
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71402 * 0.93949598
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68145 * 0.01495154
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4031 * 0.92635717
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97230 * 0.20740991
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36473 * 0.09823509
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47318 * 0.71097026
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23431 * 0.22083149
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5003 * 0.43236860
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52503 * 0.39979495
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57137 * 0.28659357
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36648 * 0.92392852
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6984 * 0.02308910
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60766 * 0.23894808
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29156 * 0.25431615
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22794 * 0.18796309
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13030 * 0.89444960
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27282 * 0.68844656
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42308 * 0.94592638
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78987 * 0.14777470
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50361 * 0.89031159
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35836 * 0.22468188
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62489 * 0.18334673
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71482 * 0.86277057
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19735 * 0.48554820
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64668 * 0.00658043
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38396 * 0.15537990
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52222 * 0.53263443
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1584 * 0.62171346
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65104 * 0.05280157
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 89561 * 0.60615560
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'lbrglbdl').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0025():
    """Extended test 25 for billing."""
    x_0 = 84154 * 0.88925834
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36735 * 0.20448813
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19723 * 0.55601143
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28047 * 0.47096879
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64850 * 0.20781858
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83630 * 0.45833095
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36660 * 0.60968186
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1026 * 0.78133877
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31630 * 0.66214759
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63234 * 0.35385315
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23698 * 0.12828192
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68546 * 0.50320549
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91766 * 0.38150734
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63083 * 0.64648449
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40792 * 0.92232586
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93398 * 0.07471227
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87625 * 0.24705593
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80580 * 0.81068486
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86797 * 0.44908557
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54434 * 0.13113412
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59297 * 0.68253356
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67769 * 0.42315986
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79749 * 0.24959008
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64549 * 0.39523248
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16720 * 0.79845165
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19693 * 0.48185040
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7979 * 0.89809983
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25019 * 0.65046997
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99664 * 0.24554264
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79484 * 0.42056712
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33216 * 0.89655105
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 485 * 0.13749867
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55286 * 0.00314848
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53004 * 0.76254775
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12717 * 0.37521511
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15068 * 0.46646594
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88054 * 0.92291529
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29525 * 0.10538106
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58737 * 0.01752949
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'mfryixqv').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0026():
    """Extended test 26 for billing."""
    x_0 = 68134 * 0.15958207
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61039 * 0.47333935
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45771 * 0.36225115
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81600 * 0.15447677
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44348 * 0.06104424
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53755 * 0.00994650
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3795 * 0.82517708
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84874 * 0.00311304
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70797 * 0.41683546
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9875 * 0.17784371
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20594 * 0.38430567
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15210 * 0.06279931
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69448 * 0.32243735
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11216 * 0.32656588
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29808 * 0.64403062
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91603 * 0.18094340
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 151 * 0.69838271
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90951 * 0.93841605
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89307 * 0.54953226
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15878 * 0.95132678
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36989 * 0.40099232
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75008 * 0.77432184
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74979 * 0.17988633
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 37755 * 0.37578425
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45830 * 0.33046667
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'zvywfiot').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0027():
    """Extended test 27 for billing."""
    x_0 = 11778 * 0.27033435
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76357 * 0.26062476
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75155 * 0.50960996
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73469 * 0.13818526
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32193 * 0.60070483
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13133 * 0.20128778
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32727 * 0.86579204
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14337 * 0.52086145
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51124 * 0.12057142
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71241 * 0.87906790
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43622 * 0.53702902
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60928 * 0.39640492
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23073 * 0.94020223
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 13390 * 0.28628269
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95895 * 0.43329697
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2263 * 0.73212150
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11215 * 0.71823102
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93054 * 0.04122891
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99597 * 0.34315129
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50461 * 0.92475745
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12290 * 0.76349331
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97784 * 0.98060606
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84241 * 0.69156566
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79553 * 0.70503177
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81236 * 0.50795081
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 710 * 0.39877208
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31685 * 0.45837762
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42676 * 0.52265076
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98947 * 0.70199258
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21314 * 0.43811246
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28827 * 0.11451455
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75489 * 0.18542399
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4777 * 0.45592282
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43680 * 0.14953035
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87726 * 0.62811453
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44616 * 0.06031552
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39854 * 0.21724925
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10558 * 0.04933338
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'vmxexwak').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0028():
    """Extended test 28 for billing."""
    x_0 = 15288 * 0.83591629
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63205 * 0.52035330
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69438 * 0.92835254
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30769 * 0.39260976
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53326 * 0.78162077
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68561 * 0.39601178
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47930 * 0.35300083
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50709 * 0.38847051
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43740 * 0.34349978
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28520 * 0.55322894
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2863 * 0.91134260
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42157 * 0.24432797
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48116 * 0.76558947
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41369 * 0.18051364
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91325 * 0.74937998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19257 * 0.70389942
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44175 * 0.03202113
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84685 * 0.82655650
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21191 * 0.35769395
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30203 * 0.43902729
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14777 * 0.75337726
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51911 * 0.13493733
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2660 * 0.10937243
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33576 * 0.02210141
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84897 * 0.65675163
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12729 * 0.97122520
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76475 * 0.72559414
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77985 * 0.59061899
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27936 * 0.03857826
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22340 * 0.50995131
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'zycgjobw').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0029():
    """Extended test 29 for billing."""
    x_0 = 34985 * 0.39414636
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37901 * 0.63998993
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46842 * 0.19502134
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 151 * 0.73091326
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75838 * 0.57075224
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59846 * 0.86921878
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8461 * 0.07293219
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28781 * 0.28964613
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38676 * 0.06487909
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59118 * 0.73251306
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31128 * 0.80096050
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55452 * 0.45494093
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3734 * 0.23774431
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61818 * 0.72129131
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82302 * 0.37314390
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24542 * 0.10010240
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16152 * 0.86180851
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89809 * 0.16408763
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34484 * 0.76464204
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26135 * 0.17572619
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2989 * 0.31844423
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73726 * 0.50242251
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37401 * 0.99742449
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55378 * 0.29827490
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55113 * 0.68757644
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37167 * 0.01421155
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46065 * 0.26506526
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53443 * 0.38104739
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11846 * 0.43661425
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51218 * 0.97528026
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21926 * 0.26096904
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7784 * 0.59376979
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26351 * 0.75412160
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46731 * 0.23917475
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33568 * 0.73225931
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76201 * 0.95377148
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'pyejnvuu').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0030():
    """Extended test 30 for billing."""
    x_0 = 60136 * 0.25638669
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47704 * 0.75612100
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5477 * 0.00424443
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71961 * 0.33695317
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23698 * 0.69367496
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80552 * 0.83060883
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56024 * 0.03285637
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73222 * 0.76975969
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36289 * 0.48751473
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78492 * 0.92265698
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24866 * 0.52009160
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17016 * 0.54158871
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95597 * 0.25662575
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65643 * 0.36219504
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38453 * 0.72105495
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1010 * 0.00993367
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69696 * 0.00783936
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92573 * 0.61694894
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45201 * 0.19578536
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65069 * 0.16347199
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39249 * 0.34895231
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45795 * 0.59406678
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60075 * 0.14215502
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'vhzbvwxs').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0031():
    """Extended test 31 for billing."""
    x_0 = 12005 * 0.92165358
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16922 * 0.37260815
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45781 * 0.25348115
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39211 * 0.04838221
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54627 * 0.18874457
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69727 * 0.40176550
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1143 * 0.70476939
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86057 * 0.73879701
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6548 * 0.50182776
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88129 * 0.80542634
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98569 * 0.96465143
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92776 * 0.84284147
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32437 * 0.78802873
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8813 * 0.43884466
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9474 * 0.54798152
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67974 * 0.37998052
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89371 * 0.17662631
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40214 * 0.84905246
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67316 * 0.34328761
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12054 * 0.20582431
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43519 * 0.48998447
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78500 * 0.54691852
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2353 * 0.61287495
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23159 * 0.52538289
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36794 * 0.04698034
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97500 * 0.24016618
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26006 * 0.42977788
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94176 * 0.25685727
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79079 * 0.65369705
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41475 * 0.23096578
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 68213 * 0.37773793
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54444 * 0.94710816
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16473 * 0.13127947
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90035 * 0.15200161
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56006 * 0.02784205
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54298 * 0.79291444
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16722 * 0.29659503
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41848 * 0.13800664
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64163 * 0.80092337
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21442 * 0.30111819
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19636 * 0.49552018
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71475 * 0.18732665
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14129 * 0.76236497
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 71771 * 0.45973874
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 73806 * 0.57441768
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 49233 * 0.51959986
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 45242 * 0.96556574
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 22415 * 0.06205178
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ctvzichv').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0032():
    """Extended test 32 for billing."""
    x_0 = 11617 * 0.58230163
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31396 * 0.52584584
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74451 * 0.30814591
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51416 * 0.39564506
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6948 * 0.66940385
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82347 * 0.93453363
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17957 * 0.21778982
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71339 * 0.42805264
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75572 * 0.61294524
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80544 * 0.01653677
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99950 * 0.92916866
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46683 * 0.56019204
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37679 * 0.29638366
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31035 * 0.17721198
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14036 * 0.90348825
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96924 * 0.46192053
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42653 * 0.06980915
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71961 * 0.11212918
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70515 * 0.86886474
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20263 * 0.78203938
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93761 * 0.98078405
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66871 * 0.05544450
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99761 * 0.13840344
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35216 * 0.41544594
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3989 * 0.29417608
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6488 * 0.07314033
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13013 * 0.25925762
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55776 * 0.91622083
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9611 * 0.25870614
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54374 * 0.16651031
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67773 * 0.90795581
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41499 * 0.31043519
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62200 * 0.69456555
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34503 * 0.50425334
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19907 * 0.61667154
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47705 * 0.47715226
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91510 * 0.05023367
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 41219 * 0.63742566
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17329 * 0.86875476
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97326 * 0.56126672
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52709 * 0.39912029
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3104 * 0.28629792
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65614 * 0.46406805
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94163 * 0.36174607
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17187 * 0.76873214
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 89874 * 0.76294419
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 5944 * 0.12847501
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 38784 * 0.87675946
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 16641 * 0.88628522
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'cvjqmiap').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0033():
    """Extended test 33 for billing."""
    x_0 = 36403 * 0.72780202
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49286 * 0.69397326
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29007 * 0.53935787
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77669 * 0.83990435
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45392 * 0.12725013
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52322 * 0.89607689
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92115 * 0.17246024
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44450 * 0.74126505
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88532 * 0.32651450
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96513 * 0.00771091
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33375 * 0.14707204
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92150 * 0.12171398
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97863 * 0.36756752
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97185 * 0.30138608
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91459 * 0.50657377
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73742 * 0.19091273
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88436 * 0.06470708
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60057 * 0.99779026
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86803 * 0.76283490
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97835 * 0.58363386
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90158 * 0.81438294
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89278 * 0.34060027
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41407 * 0.74373015
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70430 * 0.28293629
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90650 * 0.26615806
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82247 * 0.30398569
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25402 * 0.33705642
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69836 * 0.13798593
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10562 * 0.89882085
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92752 * 0.28572475
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39410 * 0.44486398
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75651 * 0.89590675
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72111 * 0.91966254
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71514 * 0.43476453
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23536 * 0.95575377
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20755 * 0.28517746
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 15342 * 0.36094940
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'awmmgcoo').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0034():
    """Extended test 34 for billing."""
    x_0 = 13997 * 0.87602566
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76949 * 0.77670940
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44638 * 0.63445728
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88504 * 0.93533125
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99089 * 0.93555838
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60934 * 0.65805941
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19278 * 0.01343626
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60022 * 0.34117779
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13241 * 0.22926969
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21062 * 0.89631295
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81338 * 0.56355112
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28086 * 0.86444066
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80136 * 0.81146731
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18823 * 0.33066359
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86825 * 0.04752038
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30929 * 0.41826898
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49052 * 0.84779455
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54902 * 0.85510118
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48873 * 0.57243849
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64203 * 0.25301085
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23540 * 0.54908549
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40520 * 0.08790659
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73624 * 0.04121889
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26379 * 0.12129742
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32333 * 0.30448666
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99521 * 0.00439965
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17847 * 0.86522198
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35709 * 0.73112072
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98683 * 0.62285065
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17721 * 0.15899439
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65453 * 0.57563151
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69005 * 0.74717466
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55522 * 0.94059991
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 748 * 0.38195883
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8639 * 0.88835308
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99696 * 0.45291644
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25393 * 0.77400186
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24345 * 0.89174621
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15189 * 0.96502154
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67961 * 0.97877668
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18151 * 0.48993355
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'luwbzblv').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0035():
    """Extended test 35 for billing."""
    x_0 = 7079 * 0.04033637
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85949 * 0.46671886
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27604 * 0.47287415
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85429 * 0.92326357
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27702 * 0.77939646
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53624 * 0.45726641
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84029 * 0.33987890
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65114 * 0.62663167
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6627 * 0.18825212
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52089 * 0.51193137
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78286 * 0.13224773
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94944 * 0.80047553
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95006 * 0.97772241
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9095 * 0.12321862
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79114 * 0.41183535
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4199 * 0.63276981
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25915 * 0.06102388
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58222 * 0.01099082
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28236 * 0.98192599
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64564 * 0.51821841
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77857 * 0.50095777
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54672 * 0.55561852
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51000 * 0.48036705
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10174 * 0.02865078
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71197 * 0.56069440
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44296 * 0.45473864
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51819 * 0.50651636
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31513 * 0.23454900
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68302 * 0.14595813
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ookeevnq').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0036():
    """Extended test 36 for billing."""
    x_0 = 58109 * 0.23173937
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46283 * 0.42557629
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57489 * 0.16577808
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72460 * 0.40185787
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48139 * 0.99162695
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40379 * 0.98593823
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9563 * 0.29368968
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92119 * 0.05919426
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84035 * 0.11924980
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65521 * 0.70808017
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94628 * 0.75110392
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92972 * 0.52756944
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12888 * 0.52236307
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3977 * 0.52034331
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4091 * 0.41721836
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67054 * 0.48794910
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37508 * 0.98454625
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67447 * 0.86221988
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19843 * 0.91689751
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75643 * 0.67476040
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24716 * 0.26515415
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63607 * 0.93563415
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55675 * 0.65805805
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24313 * 0.20283535
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2640 * 0.28605957
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39694 * 0.03444208
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'isfrlgxj').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0037():
    """Extended test 37 for billing."""
    x_0 = 29084 * 0.14356995
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24561 * 0.32473804
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38278 * 0.71778972
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17056 * 0.51351039
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83677 * 0.05751138
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59116 * 0.38219558
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92645 * 0.76191727
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90393 * 0.50101210
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54775 * 0.10675778
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95588 * 0.76125701
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7808 * 0.44288275
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86258 * 0.99699496
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44948 * 0.00603512
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75679 * 0.18626726
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32431 * 0.91223998
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69824 * 0.43520086
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1843 * 0.29373681
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18088 * 0.02664523
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7335 * 0.92505072
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69802 * 0.12439913
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47267 * 0.91583702
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58804 * 0.93731136
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71188 * 0.55013690
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45271 * 0.56027254
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24962 * 0.35096400
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37107 * 0.97080524
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82812 * 0.68335406
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43378 * 0.74963746
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83027 * 0.73925818
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52396 * 0.83876623
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42765 * 0.53873436
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3865 * 0.39605237
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 11583 * 0.84102465
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68313 * 0.00646530
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78498 * 0.65556488
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'yjviovfd').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0038():
    """Extended test 38 for billing."""
    x_0 = 50518 * 0.67675437
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41467 * 0.73714270
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91156 * 0.86865193
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89949 * 0.08104367
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61429 * 0.65037522
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22533 * 0.08111124
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88571 * 0.73016175
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80392 * 0.39564260
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41111 * 0.80930193
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41722 * 0.39903619
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88153 * 0.47336574
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19026 * 0.53001061
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11904 * 0.74758996
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92292 * 0.33100085
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49093 * 0.96617795
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54364 * 0.59284871
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86722 * 0.29052329
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81912 * 0.95663214
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98894 * 0.31021089
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84377 * 0.69194718
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26264 * 0.49104952
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44615 * 0.95859267
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6227 * 0.06701872
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78337 * 0.28538070
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43210 * 0.06414084
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33475 * 0.48814119
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 271 * 0.08718278
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40352 * 0.62212055
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 16151 * 0.18786389
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21203 * 0.98917376
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96483 * 0.14053818
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63069 * 0.36399607
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88459 * 0.75785286
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72765 * 0.34654931
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95534 * 0.46088422
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15347 * 0.96449882
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43460 * 0.38913978
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59245 * 0.53427119
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98921 * 0.74271018
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21758 * 0.62625941
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4617 * 0.68973801
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 27109 * 0.41667025
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83667 * 0.79911194
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 20608 * 0.58972555
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'tbqregpy').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0039():
    """Extended test 39 for billing."""
    x_0 = 13864 * 0.29628277
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21697 * 0.37937491
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89105 * 0.17787166
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31159 * 0.29130770
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34113 * 0.96914008
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36951 * 0.08906708
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74023 * 0.32804943
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59706 * 0.46568366
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15609 * 0.77615811
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26741 * 0.81436445
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86896 * 0.59788320
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91350 * 0.13997370
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75962 * 0.19130657
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94015 * 0.41307657
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65881 * 0.78040756
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10545 * 0.80545597
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82673 * 0.75358117
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20903 * 0.37517515
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17931 * 0.59173095
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60640 * 0.64114578
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34764 * 0.05803524
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86509 * 0.58868131
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50382 * 0.29611108
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28774 * 0.36313299
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39054 * 0.02199992
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27955 * 0.84156836
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'ddxzjznr').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0040():
    """Extended test 40 for billing."""
    x_0 = 77769 * 0.78462176
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33474 * 0.10163010
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81517 * 0.67409957
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94585 * 0.05357819
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67361 * 0.61000932
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43337 * 0.60719037
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25329 * 0.63305091
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5413 * 0.13104544
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64399 * 0.70018721
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97347 * 0.81372806
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51086 * 0.67971666
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23622 * 0.64640493
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60237 * 0.76228994
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62475 * 0.32454002
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12660 * 0.51243293
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1583 * 0.10332256
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64809 * 0.31537399
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66508 * 0.31422613
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77254 * 0.47545276
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66453 * 0.26198758
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31996 * 0.30616512
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28207 * 0.12121972
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50540 * 0.18972491
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17819 * 0.90509218
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78912 * 0.28196062
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56213 * 0.52007825
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33971 * 0.85820179
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61721 * 0.64165328
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24431 * 0.98960002
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36037 * 0.95725753
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41738 * 0.24201627
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46974 * 0.33219126
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59646 * 0.66468653
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87039 * 0.41966369
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79653 * 0.50731612
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8720 * 0.90722405
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46001 * 0.89191306
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66967 * 0.33148638
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12478 * 0.55572785
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74916 * 0.37023125
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 73488 * 0.15425302
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 53244 * 0.55566846
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74759 * 0.74059829
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'uodspymk').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0041():
    """Extended test 41 for billing."""
    x_0 = 43644 * 0.52068138
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21350 * 0.62582367
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5302 * 0.56736869
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99270 * 0.22672000
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85101 * 0.25324446
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27805 * 0.93751259
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 520 * 0.40334124
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44082 * 0.42429802
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22126 * 0.57132344
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4107 * 0.46233689
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33405 * 0.13534323
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59718 * 0.74041109
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21464 * 0.62334586
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83007 * 0.14449897
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84328 * 0.83494725
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75110 * 0.12547596
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14323 * 0.64159253
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72849 * 0.13848841
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18535 * 0.91020808
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98967 * 0.87131315
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26647 * 0.42129194
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75365 * 0.56044443
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46455 * 0.54617953
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61583 * 0.74104735
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 27544 * 0.19986927
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19706 * 0.16032958
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32663 * 0.05819383
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46573 * 0.50176737
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75571 * 0.35760570
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35849 * 0.19363981
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16205 * 0.36450916
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89602 * 0.47000328
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43051 * 0.10531709
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22178 * 0.54514766
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91794 * 0.94574083
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'kwgodesa').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0042():
    """Extended test 42 for billing."""
    x_0 = 21060 * 0.18797585
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18031 * 0.96931436
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59046 * 0.31365834
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77977 * 0.56738302
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65017 * 0.56631047
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80898 * 0.00643037
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1209 * 0.86391542
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45605 * 0.27054856
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63840 * 0.11270435
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8017 * 0.66634642
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72882 * 0.19639783
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28795 * 0.09378375
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36287 * 0.21722389
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92283 * 0.55624817
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45966 * 0.27461462
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21457 * 0.69816561
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82854 * 0.19135078
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42953 * 0.68673876
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48527 * 0.83920609
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37518 * 0.04524835
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40694 * 0.55125833
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87428 * 0.90244696
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19819 * 0.35589461
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'smavtwdu').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0043():
    """Extended test 43 for billing."""
    x_0 = 34403 * 0.32800978
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21869 * 0.45227772
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8909 * 0.61193572
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14945 * 0.37443546
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14101 * 0.62529088
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53895 * 0.18056978
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96162 * 0.74489677
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89534 * 0.72022027
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84369 * 0.81242990
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25339 * 0.27710430
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76922 * 0.83465590
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4111 * 0.19570280
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94111 * 0.04637258
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72993 * 0.15683307
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77723 * 0.34441841
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69860 * 0.07404074
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51920 * 0.42986399
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12964 * 0.22593899
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63368 * 0.74424550
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 94324 * 0.00691700
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86409 * 0.59034346
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37131 * 0.62135903
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51185 * 0.95204761
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 28569 * 0.57459085
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45896 * 0.08093451
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34688 * 0.71805212
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53089 * 0.44142239
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70421 * 0.83454947
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97145 * 0.04769513
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54716 * 0.31508785
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35978 * 0.19553292
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84896 * 0.53322720
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34330 * 0.38718212
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55942 * 0.56995105
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50668 * 0.86009522
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43143 * 0.14518784
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12654 * 0.51906167
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72858 * 0.72586052
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56432 * 0.83774427
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'yfdeswpw').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0044():
    """Extended test 44 for billing."""
    x_0 = 78336 * 0.54148730
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48525 * 0.81297530
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51537 * 0.03853377
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2531 * 0.49824697
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6477 * 0.08650338
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70732 * 0.98615273
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7805 * 0.22594686
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68623 * 0.19977095
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10767 * 0.94604286
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78693 * 0.27047564
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21931 * 0.28014026
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98939 * 0.73478472
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10200 * 0.48151060
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78996 * 0.70525194
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77095 * 0.06478163
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48820 * 0.41597041
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51330 * 0.87422522
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26267 * 0.17377568
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28587 * 0.39898320
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54690 * 0.62709142
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46340 * 0.60060087
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88904 * 0.88004729
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2056 * 0.56390376
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52159 * 0.53728973
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94078 * 0.80815661
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93281 * 0.57134049
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38150 * 0.85883097
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67209 * 0.29275782
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90590 * 0.28877422
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51834 * 0.52448337
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53028 * 0.73133620
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81835 * 0.93981041
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45262 * 0.45505223
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99917 * 0.11662486
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18939 * 0.09959909
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6635 * 0.42263912
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35376 * 0.16824540
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 2482 * 0.57114611
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 50643 * 0.64242324
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ewwtnnsn').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0045():
    """Extended test 45 for billing."""
    x_0 = 56780 * 0.64181743
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26392 * 0.39371837
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16247 * 0.34504821
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25888 * 0.24588127
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52983 * 0.31552669
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46317 * 0.99832915
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35275 * 0.14520000
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67421 * 0.97929893
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92124 * 0.38194296
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64578 * 0.28696436
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11871 * 0.41917077
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27830 * 0.48011411
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91957 * 0.98949471
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33949 * 0.14899714
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98635 * 0.26548460
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90304 * 0.75689809
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10532 * 0.79512624
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51868 * 0.09393210
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79094 * 0.44667676
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46837 * 0.70762407
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95114 * 0.03062102
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72020 * 0.48391984
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79234 * 0.97197088
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1054 * 0.93285580
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48978 * 0.57705061
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96010 * 0.73260997
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87336 * 0.40613596
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44605 * 0.94385127
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52195 * 0.61238051
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67008 * 0.80954901
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79217 * 0.33665953
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25508 * 0.19094595
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84287 * 0.65886465
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82512 * 0.48821756
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36436 * 0.61545642
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69431 * 0.87541701
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54677 * 0.48813538
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33261 * 0.63527885
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'wwwzblha').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0046():
    """Extended test 46 for billing."""
    x_0 = 68159 * 0.29896674
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98560 * 0.10770791
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3789 * 0.16307489
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65359 * 0.75420990
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69226 * 0.54965388
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25670 * 0.03574739
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1732 * 0.81578026
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13643 * 0.67242238
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26781 * 0.29556241
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53305 * 0.20961558
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10921 * 0.45580936
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42211 * 0.07208547
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41345 * 0.33516326
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64078 * 0.14164210
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74504 * 0.71822519
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40176 * 0.48309765
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43673 * 0.76189212
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64162 * 0.37394814
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95112 * 0.44740665
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81142 * 0.71831181
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15771 * 0.63837285
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56274 * 0.41120899
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85904 * 0.08847705
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87638 * 0.52682820
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42011 * 0.54843875
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58315 * 0.50829236
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'ktabxvsm').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0047():
    """Extended test 47 for billing."""
    x_0 = 32610 * 0.32034631
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79090 * 0.76749082
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13333 * 0.76448838
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78463 * 0.19685415
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40883 * 0.37942432
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78791 * 0.13541094
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27878 * 0.80359410
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79118 * 0.04947465
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54273 * 0.71348631
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83626 * 0.70195285
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29702 * 0.68855573
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10077 * 0.91481674
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15492 * 0.33006492
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28875 * 0.53125522
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92659 * 0.70634058
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33438 * 0.80735623
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82940 * 0.97501418
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40758 * 0.82623826
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2036 * 0.54293488
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55162 * 0.35574858
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85491 * 0.11277636
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97398 * 0.65820001
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19770 * 0.28302144
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59557 * 0.87307930
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72736 * 0.69820087
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2247 * 0.03395936
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41621 * 0.04962383
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18172 * 0.56657446
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81500 * 0.35223240
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23966 * 0.45592729
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66208 * 0.49872788
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29450 * 0.56300673
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27126 * 0.76417692
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68602 * 0.20591850
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88542 * 0.88310500
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75817 * 0.75329226
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 33145 * 0.69997883
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36154 * 0.76857484
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16249 * 0.08522181
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97762 * 0.08214217
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34901 * 0.74361586
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 86095 * 0.72953122
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 3430 * 0.49355197
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 90857 * 0.91271377
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'psaqobur').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0048():
    """Extended test 48 for billing."""
    x_0 = 83797 * 0.35667650
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32655 * 0.84809872
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49697 * 0.24733009
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 250 * 0.61867707
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43298 * 0.95436025
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32938 * 0.22264866
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91518 * 0.15137865
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94250 * 0.79512647
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56444 * 0.93051325
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73217 * 0.22215799
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27819 * 0.52797371
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83762 * 0.88170472
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41862 * 0.69716034
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24507 * 0.62985056
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35253 * 0.33062403
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57585 * 0.20141794
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75427 * 0.94227468
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58742 * 0.59940136
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51831 * 0.71749296
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53889 * 0.81249552
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41100 * 0.17069189
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76189 * 0.07657819
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62046 * 0.00004533
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92500 * 0.39165574
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84215 * 0.37509981
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38407 * 0.79825924
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79179 * 0.20359001
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18276 * 0.02640061
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65182 * 0.79057527
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11484 * 0.69771493
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32687 * 0.33350540
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46164 * 0.38654993
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80123 * 0.93342829
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58197 * 0.52670861
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10006 * 0.44819172
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24310 * 0.69073853
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91094 * 0.57999068
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'oocmiume').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0049():
    """Extended test 49 for billing."""
    x_0 = 13895 * 0.26115570
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50144 * 0.42477960
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16060 * 0.24630403
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 836 * 0.63723041
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93692 * 0.62141722
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6395 * 0.14573553
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14897 * 0.12255431
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57546 * 0.74249711
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37185 * 0.21796042
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23321 * 0.58954633
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94044 * 0.17217576
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70757 * 0.45871402
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31395 * 0.75317749
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65247 * 0.91286109
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10592 * 0.58891076
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52506 * 0.71589086
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81709 * 0.40727579
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65898 * 0.06679276
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55548 * 0.52550137
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72796 * 0.93487815
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25235 * 0.01492065
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74390 * 0.22617728
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78874 * 0.05740433
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2885 * 0.09448817
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3445 * 0.70915109
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87217 * 0.72839576
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'zraajony').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0050():
    """Extended test 50 for billing."""
    x_0 = 48005 * 0.09280286
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96346 * 0.83333068
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35477 * 0.16406118
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27702 * 0.76151109
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48213 * 0.92236767
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89570 * 0.51914365
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95057 * 0.08822949
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10947 * 0.68022433
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78329 * 0.98158587
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23592 * 0.02579217
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48493 * 0.15495292
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80631 * 0.83638702
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76132 * 0.99205421
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18649 * 0.45662184
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70737 * 0.09701983
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73780 * 0.57007798
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39934 * 0.56163322
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92312 * 0.10542590
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44724 * 0.72090041
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9520 * 0.24745019
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8593 * 0.39729828
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91946 * 0.99822992
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63742 * 0.55535015
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50082 * 0.69855310
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92647 * 0.06824881
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61770 * 0.68765490
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67148 * 0.16388116
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47280 * 0.15424737
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75388 * 0.59456148
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6581 * 0.54317902
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80396 * 0.07450797
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9478 * 0.08081872
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62226 * 0.48162215
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64825 * 0.61307027
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 32165 * 0.51125542
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78997 * 0.60165490
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11288 * 0.20200395
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91493 * 0.78646385
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19830 * 0.22959851
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 35493 * 0.05245350
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 56119 * 0.33229986
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'oqbgeloj').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0051():
    """Extended test 51 for billing."""
    x_0 = 20965 * 0.47201984
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74349 * 0.67293357
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32141 * 0.75902576
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5877 * 0.86834048
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63429 * 0.76201608
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5354 * 0.34530219
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24983 * 0.70977522
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23842 * 0.24905024
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63068 * 0.04748447
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92576 * 0.66183302
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15655 * 0.96545403
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19224 * 0.34274450
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94176 * 0.25837722
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29720 * 0.19555610
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98775 * 0.13438622
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44282 * 0.51086961
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2884 * 0.14067715
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76741 * 0.81857824
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30017 * 0.12447609
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40107 * 0.78234279
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 316 * 0.57859814
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92678 * 0.08588388
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63059 * 0.43110053
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38026 * 0.02189910
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13944 * 0.65937506
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6530 * 0.86102747
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18711 * 0.04255170
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3132 * 0.47091164
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38272 * 0.62979458
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64130 * 0.12931061
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82061 * 0.39847090
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54970 * 0.83457000
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99138 * 0.62175923
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2680 * 0.65974878
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43451 * 0.72118930
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65010 * 0.88041370
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 25139 * 0.15226304
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11442 * 0.84334500
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98462 * 0.35184293
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88635 * 0.46549585
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47367 * 0.61443164
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 25939 * 0.21123621
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70352 * 0.47329705
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47331 * 0.57180112
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50157 * 0.16667260
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'zqwgvhcv').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0052():
    """Extended test 52 for billing."""
    x_0 = 10508 * 0.19918512
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86045 * 0.53972947
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37109 * 0.36393814
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29744 * 0.15883844
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90637 * 0.15684159
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44771 * 0.34431276
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33918 * 0.80923786
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23734 * 0.95503448
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50349 * 0.84763161
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62685 * 0.42524021
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23524 * 0.29360926
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13284 * 0.72253336
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98036 * 0.31857614
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87271 * 0.05623381
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81998 * 0.06315530
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1431 * 0.57250250
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62683 * 0.15299761
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9087 * 0.78202515
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61081 * 0.47747577
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51749 * 0.67939584
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16114 * 0.18302603
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97744 * 0.44567504
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26835 * 0.49513008
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29512 * 0.76633536
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'defezvao').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0053():
    """Extended test 53 for billing."""
    x_0 = 72329 * 0.27577526
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15259 * 0.89758115
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45300 * 0.47527560
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17674 * 0.56303913
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95483 * 0.78963188
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29952 * 0.25195545
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80423 * 0.58536404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57686 * 0.40320524
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8433 * 0.62178962
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 920 * 0.96574831
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29859 * 0.84977308
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40317 * 0.89192316
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3244 * 0.01149834
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33078 * 0.98733516
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14942 * 0.48278510
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12056 * 0.61226893
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56333 * 0.92532951
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18029 * 0.11708105
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91799 * 0.92853009
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31405 * 0.16537042
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86042 * 0.89242885
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54924 * 0.48659734
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24884 * 0.84072405
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85884 * 0.90390990
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'yfmdwjcj').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0054():
    """Extended test 54 for billing."""
    x_0 = 69115 * 0.11879548
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62123 * 0.77747201
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75864 * 0.24160499
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62633 * 0.52563291
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68030 * 0.21049748
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47785 * 0.61968562
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6142 * 0.29675876
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82270 * 0.11499264
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30634 * 0.16755001
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40630 * 0.00193682
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80324 * 0.14262250
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35770 * 0.42853714
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15194 * 0.93790265
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56523 * 0.75632443
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24896 * 0.10292741
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47850 * 0.15314569
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 21263 * 0.55912756
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45201 * 0.74218267
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81437 * 0.75375689
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42161 * 0.47101931
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78445 * 0.91410670
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82191 * 0.38425099
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44164 * 0.47599835
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82035 * 0.31802471
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25965 * 0.36333891
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53686 * 0.54377323
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22717 * 0.71102798
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18684 * 0.31186455
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20677 * 0.11219557
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11488 * 0.63224199
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30462 * 0.50146725
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22920 * 0.50674401
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85620 * 0.96331187
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'qfglclqp').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0055():
    """Extended test 55 for billing."""
    x_0 = 39278 * 0.30000880
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40136 * 0.40348735
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61025 * 0.39496792
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10516 * 0.16323570
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27393 * 0.57446454
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95356 * 0.75899161
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75535 * 0.16493872
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5669 * 0.79733987
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88928 * 0.33761981
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13561 * 0.89495876
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72196 * 0.43022897
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41015 * 0.71856973
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94807 * 0.07055941
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34671 * 0.27150410
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12518 * 0.71004922
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 98745 * 0.30362873
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66521 * 0.47885609
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30735 * 0.60670116
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32333 * 0.58264539
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27894 * 0.65299871
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23287 * 0.41597980
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92701 * 0.74556941
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53895 * 0.62407115
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30735 * 0.09853187
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52950 * 0.77389526
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49754 * 0.29514152
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38307 * 0.01510236
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75908 * 0.94657539
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99428 * 0.63076490
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27719 * 0.75351104
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20324 * 0.80355793
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24006 * 0.47833218
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22172 * 0.40066242
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54839 * 0.80065922
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36044 * 0.97087993
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 39228 * 0.22357266
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79980 * 0.59302206
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30476 * 0.04233955
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45204 * 0.40312187
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51014 * 0.53391968
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85728 * 0.41814473
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 87818 * 0.58293437
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 45175 * 0.49047876
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 52392 * 0.56196307
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10131 * 0.38551823
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 87593 * 0.78627071
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'utjaqnfx').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0056():
    """Extended test 56 for billing."""
    x_0 = 68502 * 0.59507163
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16538 * 0.06145433
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56468 * 0.25164112
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80664 * 0.00409627
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90859 * 0.86205182
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65922 * 0.85727246
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13506 * 0.80271445
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15384 * 0.75621680
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10601 * 0.07408571
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58642 * 0.46075614
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81971 * 0.51883451
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93046 * 0.80349909
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73978 * 0.59110034
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26387 * 0.27348406
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94031 * 0.42518269
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87216 * 0.71205190
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48093 * 0.23118045
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8075 * 0.13085953
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14484 * 0.57349219
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23247 * 0.58250832
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95045 * 0.97572159
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94711 * 0.07578875
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29049 * 0.37939901
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94792 * 0.35126886
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35543 * 0.27284842
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13939 * 0.87463030
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57622 * 0.16383660
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9317 * 0.32330029
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47442 * 0.97123753
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93668 * 0.12321126
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12964 * 0.61267316
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50336 * 0.52997844
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27451 * 0.18663884
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97564 * 0.29313289
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 96177 * 0.44303181
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98810 * 0.27931566
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54018 * 0.88109421
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33861 * 0.78689683
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 22668 * 0.57588584
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77530 * 0.33125078
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1017 * 0.02601525
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59149 * 0.99133670
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 32115 * 0.53891584
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 10854 * 0.36258446
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 48554 * 0.19645346
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 67764 * 0.49668234
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 9301 * 0.12710168
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 19205 * 0.37321270
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'nhztrvmi').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0057():
    """Extended test 57 for billing."""
    x_0 = 67218 * 0.24758668
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21678 * 0.51199235
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90266 * 0.84906695
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39093 * 0.16211061
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61408 * 0.26737316
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35115 * 0.81263201
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6143 * 0.12776484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46499 * 0.17677728
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5559 * 0.32289889
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59247 * 0.01958665
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84912 * 0.63674855
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85497 * 0.96693266
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2455 * 0.51107579
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5980 * 0.13212069
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26513 * 0.95527206
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59729 * 0.00544539
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14843 * 0.44074136
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71304 * 0.25927551
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98860 * 0.69431347
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74381 * 0.74186600
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56922 * 0.06727812
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97394 * 0.84283855
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92898 * 0.51640915
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61091 * 0.56782468
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41037 * 0.27340280
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6270 * 0.08430582
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 99706 * 0.78564818
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58624 * 0.30403998
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23491 * 0.32010442
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63219 * 0.80532603
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34668 * 0.78792026
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66433 * 0.37768666
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30490 * 0.71733681
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'btpteqsb').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0058():
    """Extended test 58 for billing."""
    x_0 = 922 * 0.74130453
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68503 * 0.44431456
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26378 * 0.96145476
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56302 * 0.34949449
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57695 * 0.12171028
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97040 * 0.34217445
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61388 * 0.35840457
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18793 * 0.30482892
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71356 * 0.14536837
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22694 * 0.11180846
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12391 * 0.25689215
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90801 * 0.07152656
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33333 * 0.94770374
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78794 * 0.93089526
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71999 * 0.25197337
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40596 * 0.93341673
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48077 * 0.73440049
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46729 * 0.61506047
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83748 * 0.37922684
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18432 * 0.17165703
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35915 * 0.35785954
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71365 * 0.86505228
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'dsxnqnjp').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0059():
    """Extended test 59 for billing."""
    x_0 = 54891 * 0.18937004
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30192 * 0.94819147
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81749 * 0.73311998
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70871 * 0.55916229
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97000 * 0.57405539
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47950 * 0.27458344
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49583 * 0.66810547
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48102 * 0.81575715
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88427 * 0.19669353
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11348 * 0.76490893
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72196 * 0.90051947
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16252 * 0.22630963
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91318 * 0.63136585
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92192 * 0.73988148
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46290 * 0.39767175
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94524 * 0.17619004
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26953 * 0.42058591
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17002 * 0.90317453
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32354 * 0.74394571
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15322 * 0.65494028
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41248 * 0.57936042
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21211 * 0.75090222
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82959 * 0.68111555
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51517 * 0.19954262
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39742 * 0.59181891
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87933 * 0.31830085
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6373 * 0.73465112
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9500 * 0.86310096
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98349 * 0.95077076
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99708 * 0.84144710
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76289 * 0.91534424
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78944 * 0.95289819
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64118 * 0.34126864
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23562 * 0.57841314
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72975 * 0.62157322
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74666 * 0.79102510
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44402 * 0.59808937
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35081 * 0.20319457
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37084 * 0.12455313
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 58167 * 0.55262962
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62516 * 0.63224022
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 57491 * 0.91891884
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'ldeuyuao').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0060():
    """Extended test 60 for billing."""
    x_0 = 63816 * 0.89183565
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17887 * 0.98730381
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57774 * 0.34339033
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54708 * 0.48506684
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8130 * 0.72752834
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45225 * 0.07177279
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80554 * 0.09692933
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95129 * 0.03783003
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42985 * 0.78178866
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53319 * 0.11844213
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93853 * 0.26804108
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28453 * 0.96121665
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13991 * 0.89006571
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36784 * 0.79873091
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51433 * 0.60262526
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25140 * 0.80211335
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29943 * 0.70749572
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16005 * 0.28625277
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85805 * 0.01453430
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43728 * 0.74549913
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61214 * 0.75150684
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35444 * 0.40194463
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34231 * 0.75483192
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39504 * 0.22271044
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74220 * 0.22496985
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32633 * 0.21350702
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89540 * 0.84912709
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61734 * 0.20860574
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77287 * 0.94012533
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23704 * 0.44543274
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24467 * 0.09065277
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90588 * 0.90280847
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26853 * 0.31267902
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79751 * 0.96480589
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51250 * 0.85950289
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1970 * 0.89310522
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5 * 0.98530188
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 52770 * 0.33271767
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6169 * 0.47035127
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'raemovgk').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0061():
    """Extended test 61 for billing."""
    x_0 = 33071 * 0.58239962
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50616 * 0.83593309
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74587 * 0.51429571
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53974 * 0.89907328
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63701 * 0.83572791
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46384 * 0.41211554
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50519 * 0.87476999
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21409 * 0.96306309
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3887 * 0.05359107
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83501 * 0.32087867
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79587 * 0.05610003
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36013 * 0.52651413
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20207 * 0.67311546
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96238 * 0.69120128
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23057 * 0.95016788
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99435 * 0.27925180
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41894 * 0.15832653
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92367 * 0.12359481
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54221 * 0.56505104
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4196 * 0.69072045
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60090 * 0.07079879
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98747 * 0.25898082
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22483 * 0.24976253
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85913 * 0.76508211
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46497 * 0.57931232
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23613 * 0.33850911
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7118 * 0.82990853
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14415 * 0.43238977
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63315 * 0.32615082
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69310 * 0.16911736
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15379 * 0.28706135
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4877 * 0.52736446
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31277 * 0.46255805
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78405 * 0.85662159
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97030 * 0.62870543
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62288 * 0.48207157
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68169 * 0.71951850
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25561 * 0.58740668
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60339 * 0.06714621
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77948 * 0.06679642
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79979 * 0.68448303
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 46539 * 0.79423109
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10006 * 0.72544653
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'vrqixghr').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0062():
    """Extended test 62 for billing."""
    x_0 = 59385 * 0.26250441
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84027 * 0.38219714
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32989 * 0.39976464
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20073 * 0.88958293
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89214 * 0.20884393
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47364 * 0.50726861
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78840 * 0.69844566
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7700 * 0.49903591
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8670 * 0.33746010
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1948 * 0.89367108
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44521 * 0.89409853
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8740 * 0.92636035
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42300 * 0.56966108
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40434 * 0.35638946
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69014 * 0.70700330
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20046 * 0.76098157
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78829 * 0.67903436
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56417 * 0.66164090
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27186 * 0.54462806
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57687 * 0.60707433
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78150 * 0.96629808
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13768 * 0.29577515
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85301 * 0.40566112
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95630 * 0.31701861
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54516 * 0.16411602
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95271 * 0.42908518
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90665 * 0.37568310
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4697 * 0.64564471
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35169 * 0.91156258
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9130 * 0.24708465
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59974 * 0.15754995
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35566 * 0.90330250
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39916 * 0.41530675
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57894 * 0.55452808
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76022 * 0.72194712
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74169 * 0.00196108
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83003 * 0.35746010
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 21407 * 0.33965376
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77827 * 0.44950710
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66429 * 0.31324339
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52317 * 0.60109188
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 69233 * 0.38804780
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 94245 * 0.35471424
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'dqsvtmov').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0063():
    """Extended test 63 for billing."""
    x_0 = 43407 * 0.90983757
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99075 * 0.69291918
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23859 * 0.08900023
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36445 * 0.13949667
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35176 * 0.34016968
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60348 * 0.41869675
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80399 * 0.28585203
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87627 * 0.99079851
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20216 * 0.78749651
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26255 * 0.57624330
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33146 * 0.18251526
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60212 * 0.17146341
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18447 * 0.95914810
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86423 * 0.62775186
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54091 * 0.31959005
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46791 * 0.39575990
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9097 * 0.35850670
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91469 * 0.77460088
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72859 * 0.64697123
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93879 * 0.44224434
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84517 * 0.90344496
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4532 * 0.81472999
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49244 * 0.03917612
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58079 * 0.88570153
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96354 * 0.41818460
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46815 * 0.96358624
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34329 * 0.01282350
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 15023 * 0.15930452
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97028 * 0.06069978
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99984 * 0.16290349
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45322 * 0.48832141
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64901 * 0.09485824
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29408 * 0.20250399
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65866 * 0.99818180
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30143 * 0.65922012
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94103 * 0.73742962
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73750 * 0.65046197
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25773 * 0.84038716
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 39787 * 0.98471558
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91732 * 0.86839100
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29425 * 0.06962717
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92286 * 0.40530415
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55424 * 0.11543468
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 28081 * 0.52739551
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 96868 * 0.28842827
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'oiawfgmp').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0064():
    """Extended test 64 for billing."""
    x_0 = 36788 * 0.42884118
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85929 * 0.08805738
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24605 * 0.18613348
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64493 * 0.34865130
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50853 * 0.18673146
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28618 * 0.54870397
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72091 * 0.18511794
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9335 * 0.76958928
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11727 * 0.34118407
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70436 * 0.51835276
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17881 * 0.81418696
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30240 * 0.81672350
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96750 * 0.37843386
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89784 * 0.95893874
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64875 * 0.98704653
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26840 * 0.40687951
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95208 * 0.48837045
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67621 * 0.42955651
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60985 * 0.41877877
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13602 * 0.33237746
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47315 * 0.02845677
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24418 * 0.64453991
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43792 * 0.74587342
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81607 * 0.55766967
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46426 * 0.45170927
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87318 * 0.56146503
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82398 * 0.26855873
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9226 * 0.12362226
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12041 * 0.98214042
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52513 * 0.77675026
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96972 * 0.70626580
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6477 * 0.22597734
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24661 * 0.61356819
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62335 * 0.33180793
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24745 * 0.57441238
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55177 * 0.91612038
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87930 * 0.26668507
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19208 * 0.59655231
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34234 * 0.53864929
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11783 * 0.24615002
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21270 * 0.24742645
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71746 * 0.94149502
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 64897 * 0.86530718
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 86633 * 0.33101520
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 16190 * 0.05413138
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 72556 * 0.03278276
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 57979 * 0.20372697
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 77639 * 0.77492195
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'uslfcaie').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0065():
    """Extended test 65 for billing."""
    x_0 = 42038 * 0.17131946
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13832 * 0.05582987
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54588 * 0.77719363
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22670 * 0.64647670
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16346 * 0.28863967
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22770 * 0.98950024
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72880 * 0.45287466
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21607 * 0.08727723
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24741 * 0.04119280
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5114 * 0.23726232
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37323 * 0.47329411
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8415 * 0.14556232
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42551 * 0.62134493
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74278 * 0.69544435
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93651 * 0.71330160
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8720 * 0.15877958
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60665 * 0.60492474
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41481 * 0.49887094
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45881 * 0.04440595
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81010 * 0.62177077
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 8136 * 0.53904588
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5913 * 0.35227417
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'crhbmato').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0066():
    """Extended test 66 for billing."""
    x_0 = 43225 * 0.97422105
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13790 * 0.43672322
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11553 * 0.87377101
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40115 * 0.29998357
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25264 * 0.81292759
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1940 * 0.23342129
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78079 * 0.37262529
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96578 * 0.02792465
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75180 * 0.97672552
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9854 * 0.05711404
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90189 * 0.65698785
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12607 * 0.70178753
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6052 * 0.60742606
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18802 * 0.05786994
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89905 * 0.03446879
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47110 * 0.43648397
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15519 * 0.65222800
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39430 * 0.17282887
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49538 * 0.14137290
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34395 * 0.94548396
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80119 * 0.61168831
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35389 * 0.70599790
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21116 * 0.74771359
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93327 * 0.97436356
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12490 * 0.38942693
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18900 * 0.21005967
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81047 * 0.03701190
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26292 * 0.18429134
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14054 * 0.21633318
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61424 * 0.04177549
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90707 * 0.28248821
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2839 * 0.64419044
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94421 * 0.98123793
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76914 * 0.60815413
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50236 * 0.63141201
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82738 * 0.65169930
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66512 * 0.53473210
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69842 * 0.50551211
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'cdqkdwsz').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0067():
    """Extended test 67 for billing."""
    x_0 = 93897 * 0.59899811
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60304 * 0.10771813
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19101 * 0.18835623
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93242 * 0.50875845
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19300 * 0.88576819
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58006 * 0.43076418
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28253 * 0.89781769
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88626 * 0.62672913
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68043 * 0.12103718
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89531 * 0.72839037
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31584 * 0.83026186
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89943 * 0.37769989
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46338 * 0.50266813
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91742 * 0.03717974
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25691 * 0.80660826
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21479 * 0.88599622
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11518 * 0.77424572
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30225 * 0.87062446
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92276 * 0.27721931
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58244 * 0.23861888
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18258 * 0.10857997
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38239 * 0.72238957
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98574 * 0.48974828
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60393 * 0.64567759
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10091 * 0.80358187
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33846 * 0.76505304
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59032 * 0.90370054
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64761 * 0.12636190
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87888 * 0.42916069
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40251 * 0.33563967
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37581 * 0.12181809
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50155 * 0.25769375
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69301 * 0.87905426
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41749 * 0.37551890
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82172 * 0.04500580
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15992 * 0.80796366
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55435 * 0.67226230
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92628 * 0.01882069
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 89866 * 0.40144503
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 50328 * 0.33389327
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 91801 * 0.32562848
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'sqptfncw').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0068():
    """Extended test 68 for billing."""
    x_0 = 50491 * 0.57489310
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72378 * 0.23747459
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26275 * 0.33951875
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71048 * 0.06362106
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23111 * 0.83778367
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91798 * 0.45797214
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15924 * 0.81633938
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13537 * 0.68326792
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21430 * 0.03952530
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32410 * 0.50099205
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82569 * 0.32610443
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93267 * 0.15738719
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89527 * 0.78280812
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65126 * 0.34749655
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87204 * 0.62185177
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74125 * 0.89075197
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 753 * 0.56178296
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21189 * 0.69433026
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37559 * 0.97927340
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59732 * 0.86462505
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30225 * 0.42727571
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22075 * 0.38109562
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54056 * 0.47903877
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60050 * 0.18520471
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67557 * 0.54982981
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96142 * 0.42888167
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97468 * 0.32761768
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60786 * 0.66072593
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58236 * 0.31638499
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'sphghobt').hexdigest()
    assert len(h) == 64

def test_billing_extended_7_0069():
    """Extended test 69 for billing."""
    x_0 = 86119 * 0.26765411
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55165 * 0.58198771
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59057 * 0.70731368
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73944 * 0.05127148
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43884 * 0.51697178
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76308 * 0.33526455
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20972 * 0.05154744
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60144 * 0.17559109
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23622 * 0.25612658
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28594 * 0.57992477
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31016 * 0.05994487
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18826 * 0.76903024
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78387 * 0.32646779
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38396 * 0.47347391
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 84220 * 0.02650100
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35687 * 0.27652186
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74500 * 0.67013846
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96875 * 0.18884329
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87088 * 0.59709909
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56242 * 0.95797350
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75470 * 0.98452615
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15260 * 0.55604951
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12979 * 0.51183967
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27153 * 0.77386966
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96742 * 0.95852912
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19156 * 0.27338427
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10403 * 0.23034447
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56324 * 0.81242846
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 54051 * 0.93170058
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44293 * 0.34655995
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15881 * 0.03892004
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33516 * 0.69783264
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70512 * 0.36408620
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40430 * 0.27373248
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87052 * 0.49134373
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49516 * 0.46159155
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95162 * 0.94163587
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48173 * 0.61967850
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99880 * 0.53176242
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82020 * 0.98541159
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'tyfskzpn').hexdigest()
    assert len(h) == 64
