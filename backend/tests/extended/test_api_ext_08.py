"""Extended tests for api suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_api_extended_8_0000():
    """Extended test 0 for api."""
    x_0 = 49297 * 0.87017535
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49382 * 0.70515680
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79045 * 0.87827202
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56327 * 0.93922741
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11466 * 0.24004743
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90409 * 0.59068328
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16085 * 0.14035444
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11902 * 0.89753493
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72294 * 0.53787697
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6750 * 0.66301032
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48646 * 0.98155189
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74288 * 0.67573382
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5132 * 0.74293158
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42372 * 0.49526390
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50771 * 0.57290463
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69946 * 0.78390708
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92784 * 0.85964691
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 9801 * 0.25512532
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89254 * 0.45996738
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85793 * 0.72154576
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92853 * 0.20421476
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81299 * 0.94612880
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26715 * 0.26533449
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56599 * 0.49511990
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68953 * 0.04663129
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40661 * 0.22901445
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53098 * 0.24288887
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'bfnehnkh').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0001():
    """Extended test 1 for api."""
    x_0 = 13097 * 0.22045916
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41690 * 0.10346927
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90189 * 0.17424627
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4438 * 0.12257988
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6688 * 0.66155451
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27303 * 0.32943758
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19005 * 0.81850091
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33672 * 0.17686153
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76764 * 0.36084661
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13488 * 0.06357044
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46554 * 0.22511827
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13321 * 0.55517684
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57320 * 0.26114546
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9576 * 0.94107984
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48593 * 0.68168825
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33414 * 0.10401533
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64557 * 0.94703953
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18481 * 0.06560278
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54571 * 0.60639542
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44684 * 0.83598403
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15044 * 0.40107613
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18985 * 0.24767404
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69282 * 0.85238402
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21025 * 0.76999471
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82774 * 0.65695302
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45082 * 0.62342096
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8135 * 0.14685704
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3081 * 0.06646718
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26790 * 0.46033275
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65271 * 0.16553371
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99351 * 0.48718347
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7072 * 0.88780860
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81854 * 0.76949558
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72619 * 0.95009092
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80497 * 0.83721184
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94645 * 0.20403111
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12365 * 0.50457512
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46118 * 0.87106601
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78975 * 0.36205790
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43804 * 0.32334707
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'jzmmiilq').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0002():
    """Extended test 2 for api."""
    x_0 = 16712 * 0.16614193
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46208 * 0.66847061
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73134 * 0.36132159
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13852 * 0.35615807
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57686 * 0.75313775
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30587 * 0.30306015
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18661 * 0.12074581
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53674 * 0.01577786
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85724 * 0.71314038
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69798 * 0.59210278
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20015 * 0.59472071
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73651 * 0.59093129
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98692 * 0.44917641
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 725 * 0.92516144
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52976 * 0.10278353
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42507 * 0.81342122
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68312 * 0.26555766
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86077 * 0.82779072
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77908 * 0.36749996
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77670 * 0.05340653
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80315 * 0.31380769
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98811 * 0.20219283
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70802 * 0.38737999
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26195 * 0.15874745
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89510 * 0.72957934
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'tbeolnqa').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0003():
    """Extended test 3 for api."""
    x_0 = 24977 * 0.09426988
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4678 * 0.60016281
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39530 * 0.79781875
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51368 * 0.89544181
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13528 * 0.73812990
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54465 * 0.07332537
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11143 * 0.63467955
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63264 * 0.68419273
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29069 * 0.39101403
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54527 * 0.29394365
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42406 * 0.14079664
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26426 * 0.07608695
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42296 * 0.05431985
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49088 * 0.79340463
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52043 * 0.68734306
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69689 * 0.12433159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98248 * 0.11830714
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87723 * 0.38187747
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84135 * 0.83931648
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23866 * 0.94954309
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93620 * 0.44298942
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87034 * 0.23247128
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47036 * 0.12563201
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52422 * 0.99454773
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90594 * 0.50365974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26939 * 0.48340231
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29820 * 0.82330132
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74878 * 0.96549693
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37399 * 0.36374526
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61866 * 0.42161504
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97081 * 0.61724892
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56207 * 0.06370855
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 27889 * 0.92113010
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52910 * 0.76327040
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4864 * 0.45283772
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58731 * 0.41648959
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69772 * 0.21515843
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43058 * 0.40695629
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 65249 * 0.79487325
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73008 * 0.62175258
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82322 * 0.00378335
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'urywhuyd').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0004():
    """Extended test 4 for api."""
    x_0 = 90349 * 0.84841078
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98233 * 0.79332760
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56825 * 0.17841447
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62942 * 0.21692519
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58854 * 0.91680261
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25880 * 0.16413853
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92461 * 0.89043156
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98127 * 0.39027319
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4244 * 0.51372879
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52299 * 0.35637112
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94848 * 0.09623889
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72204 * 0.40170188
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86299 * 0.26824148
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27447 * 0.74943317
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5936 * 0.00376842
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91265 * 0.65650679
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92742 * 0.94642963
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21313 * 0.19060619
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68239 * 0.87772058
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93639 * 0.43574678
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66041 * 0.12127590
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84865 * 0.68061590
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14049 * 0.42555992
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4506 * 0.82397909
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32339 * 0.92977989
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32758 * 0.11499340
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61870 * 0.59317724
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 28118 * 0.16924619
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26649 * 0.12283642
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62732 * 0.83224807
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58390 * 0.52079631
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14308 * 0.15320463
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90360 * 0.04133320
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3135 * 0.29882632
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20474 * 0.19871775
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20660 * 0.07308995
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47976 * 0.62184936
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60880 * 0.02697584
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98844 * 0.01990366
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'oqhcsfqy').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0005():
    """Extended test 5 for api."""
    x_0 = 52104 * 0.83778095
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38955 * 0.33306714
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64155 * 0.41300028
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83299 * 0.23053375
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61871 * 0.49219011
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19194 * 0.83683534
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32082 * 0.75845131
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81611 * 0.27787746
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78883 * 0.88030217
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83110 * 0.94216084
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3306 * 0.88849786
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81626 * 0.73125047
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37101 * 0.94208891
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5952 * 0.14016132
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41622 * 0.31472889
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69156 * 0.47920275
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44812 * 0.40204447
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54452 * 0.35261566
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69919 * 0.87485279
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83407 * 0.27863640
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19402 * 0.76185933
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74359 * 0.19958380
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41041 * 0.48825388
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23115 * 0.70617160
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34722 * 0.92758290
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81288 * 0.86174083
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81695 * 0.25724311
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7108 * 0.54683782
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83787 * 0.58419915
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28038 * 0.23636408
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84969 * 0.73137196
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94485 * 0.52010211
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26783 * 0.83271746
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56775 * 0.17111540
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47009 * 0.13321419
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49747 * 0.03765846
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4500 * 0.96617155
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 59156 * 0.12795307
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 85145 * 0.90316224
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39709 * 0.50451050
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5154 * 0.15468376
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 52861 * 0.02557300
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70011 * 0.83732382
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69871 * 0.68125199
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 96812 * 0.29011680
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 51750 * 0.56309361
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 33833 * 0.03762962
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'jzhpouxt').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0006():
    """Extended test 6 for api."""
    x_0 = 93576 * 0.82037953
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1135 * 0.73129781
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17714 * 0.76936762
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85589 * 0.62972958
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3278 * 0.16129750
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84476 * 0.21342896
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41799 * 0.09932274
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56701 * 0.17058918
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74493 * 0.17861711
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22875 * 0.81661606
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20563 * 0.73331571
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72415 * 0.22857134
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 980 * 0.36382835
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8949 * 0.13909522
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1777 * 0.98206007
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96959 * 0.44501481
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97621 * 0.32651858
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88962 * 0.58467302
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26224 * 0.87434069
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31207 * 0.66561886
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4861 * 0.88783160
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12462 * 0.57469978
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39592 * 0.66023997
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4960 * 0.67272189
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64778 * 0.36376528
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44187 * 0.24102266
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87647 * 0.13910200
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9363 * 0.30510665
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77093 * 0.26892033
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65385 * 0.99564503
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13814 * 0.96154740
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86579 * 0.80294575
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52696 * 0.05281299
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77501 * 0.91147826
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89082 * 0.41929195
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98680 * 0.24402348
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51402 * 0.22731581
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16511 * 0.16037030
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82940 * 0.76724192
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33268 * 0.25566747
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65507 * 0.40145255
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81990 * 0.58562156
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 53385 * 0.99823950
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 99398 * 0.80132999
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17571 * 0.04247165
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 52086 * 0.00269373
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 31481 * 0.27596168
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 64478 * 0.44177570
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 31806 * 0.67702607
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'bvshrapp').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0007():
    """Extended test 7 for api."""
    x_0 = 76806 * 0.40044937
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56905 * 0.53262794
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25125 * 0.22056238
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21103 * 0.65744274
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71674 * 0.92652692
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66646 * 0.90193024
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30388 * 0.24607808
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40195 * 0.91813444
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5148 * 0.63399577
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18721 * 0.15333252
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14213 * 0.95206084
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17952 * 0.63721231
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5090 * 0.76321936
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77813 * 0.55875690
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93625 * 0.85808507
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21899 * 0.15317030
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37714 * 0.85176925
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21675 * 0.24413161
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71854 * 0.85972332
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97301 * 0.29668686
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78378 * 0.05978603
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98885 * 0.37689887
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78381 * 0.71518258
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21587 * 0.21387110
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11306 * 0.25588715
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'dnsmemgj').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0008():
    """Extended test 8 for api."""
    x_0 = 24422 * 0.72968881
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43778 * 0.83526323
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7390 * 0.60565143
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72977 * 0.72085491
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25594 * 0.81966771
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79141 * 0.90481532
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85100 * 0.18083254
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4932 * 0.06260112
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64806 * 0.20813009
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 107 * 0.82636987
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59585 * 0.72895956
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9595 * 0.50610577
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57909 * 0.69544811
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85028 * 0.14449049
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16991 * 0.67733822
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2386 * 0.43748663
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40573 * 0.80412941
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26296 * 0.48328004
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88918 * 0.39733878
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25484 * 0.19724122
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96397 * 0.87115432
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88747 * 0.92757364
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'hbpbnsyj').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0009():
    """Extended test 9 for api."""
    x_0 = 50654 * 0.98388920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95659 * 0.31577753
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37031 * 0.06133438
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11444 * 0.41294427
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91919 * 0.71733521
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68883 * 0.73056074
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39086 * 0.93399290
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58761 * 0.85388731
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73725 * 0.07348080
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84869 * 0.05655089
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70879 * 0.81954194
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40050 * 0.74397344
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70010 * 0.88858921
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65685 * 0.98030376
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66565 * 0.90428549
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36524 * 0.23024727
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80769 * 0.18762187
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98954 * 0.55612640
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8431 * 0.11709033
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66493 * 0.24760610
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28058 * 0.50385241
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4531 * 0.64864461
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82432 * 0.40961182
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93106 * 0.45439590
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22881 * 0.92853198
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15082 * 0.51289572
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42685 * 0.21060505
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51445 * 0.44598527
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28352 * 0.53781193
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62923 * 0.96633472
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96728 * 0.43617345
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20345 * 0.03689519
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23700 * 0.33522276
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77324 * 0.38579276
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85866 * 0.70405932
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99775 * 0.97548270
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71197 * 0.56337269
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'rtiibnya').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0010():
    """Extended test 10 for api."""
    x_0 = 71583 * 0.39750573
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85842 * 0.27618737
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54307 * 0.11317358
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 341 * 0.31392218
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93886 * 0.52475446
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96511 * 0.65587134
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35049 * 0.10017543
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30977 * 0.94830460
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80541 * 0.85619828
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27059 * 0.02867089
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1282 * 0.76467321
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85001 * 0.48299556
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8856 * 0.21362996
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93962 * 0.70360974
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14804 * 0.52120972
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41702 * 0.32833814
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5648 * 0.44632989
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44691 * 0.15687331
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43559 * 0.45534649
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87848 * 0.01135527
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64921 * 0.53572014
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17239 * 0.55465764
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22659 * 0.18947375
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50924 * 0.02896941
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29105 * 0.40204049
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15678 * 0.77639785
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9592 * 0.97353673
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82278 * 0.50971355
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13163 * 0.16018621
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67384 * 0.52700698
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59787 * 0.32018621
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24166 * 0.11124242
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49583 * 0.53994898
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'wtvmjmft').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0011():
    """Extended test 11 for api."""
    x_0 = 41493 * 0.30132077
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28867 * 0.87546141
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49733 * 0.80690341
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76369 * 0.57593673
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34387 * 0.00979000
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43468 * 0.07677487
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54389 * 0.40227985
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95342 * 0.20481574
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97919 * 0.58220849
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74912 * 0.29139008
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99286 * 0.15427410
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71840 * 0.23060149
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95275 * 0.53372396
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93917 * 0.38837388
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61414 * 0.03251081
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67050 * 0.86118458
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93868 * 0.47718018
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73493 * 0.41720602
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6252 * 0.97542237
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39450 * 0.29351957
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27535 * 0.41633624
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'sjdxlgwo').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0012():
    """Extended test 12 for api."""
    x_0 = 82083 * 0.86373203
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15056 * 0.11372596
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22309 * 0.74125847
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39573 * 0.73103074
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41078 * 0.63078179
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86071 * 0.82488487
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42957 * 0.81850207
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45645 * 0.28228449
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38039 * 0.15067465
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36369 * 0.98717306
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2969 * 0.03508987
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93808 * 0.48657094
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47168 * 0.31983584
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52302 * 0.76013675
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7560 * 0.50627880
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99502 * 0.33082322
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15445 * 0.25143188
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32252 * 0.92348027
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4266 * 0.47734439
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64102 * 0.66495527
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18898 * 0.17237061
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29919 * 0.43893396
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90788 * 0.71113381
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53969 * 0.74655176
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1539 * 0.15072540
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84356 * 0.16961169
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60055 * 0.05031298
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93807 * 0.83474675
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50555 * 0.01754766
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89847 * 0.50737585
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50162 * 0.82035378
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 96057 * 0.68113706
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'ymzvasma').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0013():
    """Extended test 13 for api."""
    x_0 = 70314 * 0.72635635
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92727 * 0.83705328
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84430 * 0.92057925
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 63302 * 0.68812755
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33978 * 0.78026616
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6078 * 0.81881057
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21041 * 0.91269480
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69634 * 0.19167425
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31830 * 0.02610697
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27518 * 0.48920585
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21813 * 0.16135654
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48704 * 0.45892453
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96512 * 0.86116326
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65435 * 0.66609322
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52675 * 0.78063823
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92487 * 0.57758681
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7458 * 0.58287228
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46250 * 0.43055331
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52674 * 0.79929086
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35466 * 0.42897376
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53420 * 0.72192322
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14645 * 0.67768600
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94994 * 0.40201955
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9864 * 0.53095340
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6017 * 0.78768846
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53569 * 0.09513940
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95725 * 0.11727894
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66537 * 0.82490428
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 55320 * 0.42381121
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27706 * 0.91622971
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19009 * 0.35845751
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45225 * 0.15315743
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67506 * 0.11169841
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'ndhpymie').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0014():
    """Extended test 14 for api."""
    x_0 = 64161 * 0.60957892
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68012 * 0.22537266
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46910 * 0.11419043
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7650 * 0.21201471
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8918 * 0.35233928
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85233 * 0.99146527
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1167 * 0.06601696
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86482 * 0.09867229
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64815 * 0.03524599
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42843 * 0.69257229
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68935 * 0.07935663
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88417 * 0.06112395
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64772 * 0.85320042
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58844 * 0.90297838
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88270 * 0.84189746
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40130 * 0.67627250
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43300 * 0.29952319
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43914 * 0.35898870
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45523 * 0.09589529
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79415 * 0.63957907
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41312 * 0.76716745
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13143 * 0.53963350
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30344 * 0.34884580
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'wnjufcno').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0015():
    """Extended test 15 for api."""
    x_0 = 39754 * 0.96828046
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30681 * 0.38984555
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 778 * 0.01555402
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24512 * 0.11775847
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43869 * 0.94957694
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42187 * 0.39639900
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85129 * 0.29569252
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67421 * 0.68383660
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 29858 * 0.74327465
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92182 * 0.67281516
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6675 * 0.18088122
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77358 * 0.67346340
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86314 * 0.40021431
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57655 * 0.75647889
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62196 * 0.41554518
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58360 * 0.72359590
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71496 * 0.76784996
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77200 * 0.01486940
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21270 * 0.24944374
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90925 * 0.95704803
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39965 * 0.30610938
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77232 * 0.20092416
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15055 * 0.07756651
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31546 * 0.25778758
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84700 * 0.77704418
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88362 * 0.77720083
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47634 * 0.16920902
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1842 * 0.30898976
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53945 * 0.71495566
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68427 * 0.92899015
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 98762 * 0.93475741
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24276 * 0.07276470
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25741 * 0.23220371
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74059 * 0.65500907
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2997 * 0.71169678
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 28525 * 0.37000390
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5723 * 0.39028957
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28491 * 0.61760803
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67886 * 0.48945298
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59293 * 0.85781422
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'mlzssrnb').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0016():
    """Extended test 16 for api."""
    x_0 = 32878 * 0.62398212
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29088 * 0.92450824
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77626 * 0.18518823
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88159 * 0.80453608
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97369 * 0.10870311
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97131 * 0.22266688
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74041 * 0.04256978
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43732 * 0.72681631
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44525 * 0.09922607
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17527 * 0.22105672
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1232 * 0.50431069
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2628 * 0.37213931
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49863 * 0.45962318
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82081 * 0.07203655
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55182 * 0.74060880
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29877 * 0.26919022
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68277 * 0.34345682
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1673 * 0.67409676
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61853 * 0.84558590
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9676 * 0.62076026
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95998 * 0.41255126
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53701 * 0.35006240
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14521 * 0.88067739
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19872 * 0.94130994
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95265 * 0.67898872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55653 * 0.19558171
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85168 * 0.19830179
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19141 * 0.94692418
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 72408 * 0.25735574
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11499 * 0.29250247
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70655 * 0.05237223
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 31106 * 0.05750512
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 67156 * 0.39918933
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99913 * 0.39891387
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'yptyjjcc').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0017():
    """Extended test 17 for api."""
    x_0 = 64892 * 0.62572127
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22418 * 0.67716416
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51282 * 0.62935768
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9985 * 0.43713559
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47364 * 0.77896085
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98211 * 0.28287226
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56770 * 0.11594989
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88584 * 0.46667039
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82293 * 0.44659142
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80271 * 0.77924455
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66304 * 0.54858684
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82686 * 0.03793223
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15464 * 0.06120389
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43009 * 0.37964148
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61388 * 0.20470307
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27266 * 0.25081241
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75425 * 0.53900760
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13810 * 0.78126385
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43732 * 0.79780852
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92077 * 0.81697786
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29400 * 0.65511699
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91053 * 0.90844983
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14912 * 0.11636887
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'cpfixulc').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0018():
    """Extended test 18 for api."""
    x_0 = 91903 * 0.57509635
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79168 * 0.15433796
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17816 * 0.23168125
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43602 * 0.68189505
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64464 * 0.29443342
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1887 * 0.28036152
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97932 * 0.29433879
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8200 * 0.35499535
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47284 * 0.56759091
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33046 * 0.33459295
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23631 * 0.96229155
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89590 * 0.62870873
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19844 * 0.40611294
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33366 * 0.19885435
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50665 * 0.95544428
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82881 * 0.19264474
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2099 * 0.52924833
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22348 * 0.42687201
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88304 * 0.03876881
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99468 * 0.46714782
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52762 * 0.28977181
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18924 * 0.43796176
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 558 * 0.26481180
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22608 * 0.16578028
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46957 * 0.96020652
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82153 * 0.06311045
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75773 * 0.51474192
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50300 * 0.26996528
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7654 * 0.40365313
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97836 * 0.15878903
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14581 * 0.42582856
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1262 * 0.36889041
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74446 * 0.26973840
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93222 * 0.54335159
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77202 * 0.48807324
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83357 * 0.58469508
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 48378 * 0.04067346
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88116 * 0.84219935
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 22345 * 0.18124632
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6420 * 0.48416942
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 9605 * 0.61745045
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81897 * 0.12797368
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 30245 * 0.07195185
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'rwtjhmqp').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0019():
    """Extended test 19 for api."""
    x_0 = 24997 * 0.30383577
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62963 * 0.85838953
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 518 * 0.48343062
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79705 * 0.64834068
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10686 * 0.92112023
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5933 * 0.76167400
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23541 * 0.68008760
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78136 * 0.71163500
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39798 * 0.03528381
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95855 * 0.93294311
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59443 * 0.73272358
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81716 * 0.76446952
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86424 * 0.46235078
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84164 * 0.49161905
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61055 * 0.16008769
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2726 * 0.44762246
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74802 * 0.11965354
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10655 * 0.36779132
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 59219 * 0.72551441
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93283 * 0.06711927
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31699 * 0.82273970
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38387 * 0.42263154
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80457 * 0.99402357
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39283 * 0.03736882
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31719 * 0.96738295
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65645 * 0.56844093
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24885 * 0.97095109
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 77637 * 0.66169030
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67180 * 0.18653497
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'xduuuujs').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0020():
    """Extended test 20 for api."""
    x_0 = 46522 * 0.39519165
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14063 * 0.84662492
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20434 * 0.59665703
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18316 * 0.15998058
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62334 * 0.39378351
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1573 * 0.78105758
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57176 * 0.02423632
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60579 * 0.22637787
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92549 * 0.06461619
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87834 * 0.67766998
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43342 * 0.38462527
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96426 * 0.80543412
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 79369 * 0.57587486
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48431 * 0.89373590
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46844 * 0.00399651
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64619 * 0.83230404
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55967 * 0.48021226
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90501 * 0.09604631
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55978 * 0.00998924
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34234 * 0.88391574
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55266 * 0.72684024
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32976 * 0.27984822
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63645 * 0.49637588
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 83739 * 0.44109164
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84601 * 0.29450231
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 26625 * 0.46242302
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12045 * 0.81049153
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29995 * 0.22844295
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95 * 0.01260490
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 13705 * 0.38031275
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21474 * 0.62944598
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81963 * 0.75711277
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59582 * 0.75208546
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73973 * 0.85844936
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16050 * 0.14527436
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50198 * 0.44743789
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71321 * 0.50400623
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35446 * 0.49598338
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17788 * 0.00574088
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17609 * 0.71684183
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 13921 * 0.37113216
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5085 * 0.90879771
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'zrzgpgbm').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0021():
    """Extended test 21 for api."""
    x_0 = 42275 * 0.43857306
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31676 * 0.02416211
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60326 * 0.11793376
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62857 * 0.87706083
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58070 * 0.69674697
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60876 * 0.84714761
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62138 * 0.37294150
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6308 * 0.41756900
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70149 * 0.06366812
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39232 * 0.95060309
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13555 * 0.43735683
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71290 * 0.97847717
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25539 * 0.11359387
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 33644 * 0.97956113
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4903 * 0.33613546
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95983 * 0.07803990
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1359 * 0.08995190
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25669 * 0.01908975
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64127 * 0.54210275
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52473 * 0.49681217
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16330 * 0.73396252
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31954 * 0.15593187
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60517 * 0.16019963
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23812 * 0.68571885
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13011 * 0.35969208
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57221 * 0.32339352
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42081 * 0.58726893
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24059 * 0.77911310
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81779 * 0.20074362
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9857 * 0.05072307
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6632 * 0.36757524
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69775 * 0.13898072
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62279 * 0.49661959
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3038 * 0.58152123
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 22731 * 0.22538142
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85372 * 0.55020522
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69406 * 0.07732536
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10267 * 0.83153122
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60874 * 0.83109478
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52483 * 0.25582991
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46660 * 0.31360749
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39425 * 0.66083850
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 65340 * 0.90125620
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 33938 * 0.89206886
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 45330 * 0.35856259
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 23557 * 0.72340243
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 67106 * 0.45357570
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'qiducyux').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0022():
    """Extended test 22 for api."""
    x_0 = 88956 * 0.85747339
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5476 * 0.91711371
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68053 * 0.24685851
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17464 * 0.45304429
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86732 * 0.50495219
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79597 * 0.39687034
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63997 * 0.57049943
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49557 * 0.06999062
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67153 * 0.72685556
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11293 * 0.35777480
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42916 * 0.38049320
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27733 * 0.87073806
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15024 * 0.43264050
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58041 * 0.09661330
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98220 * 0.84820342
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54688 * 0.07870672
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83223 * 0.54578084
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82027 * 0.96779762
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4874 * 0.88976161
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81055 * 0.97215158
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90557 * 0.37513326
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52602 * 0.55914578
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84683 * 0.56519317
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20180 * 0.61614579
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57634 * 0.08512938
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69487 * 0.98633486
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50555 * 0.65065538
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76237 * 0.51428922
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34742 * 0.71358098
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19393 * 0.59311911
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54616 * 0.00410736
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76119 * 0.83822387
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77221 * 0.67754216
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 80231 * 0.60096835
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57783 * 0.84943765
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1629 * 0.43177236
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16681 * 0.41584047
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96338 * 0.94617717
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'rppsaeqg').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0023():
    """Extended test 23 for api."""
    x_0 = 52741 * 0.64727425
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73399 * 0.80615502
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35395 * 0.29148512
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93239 * 0.16329094
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24173 * 0.45457193
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30757 * 0.62512793
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 917 * 0.99233361
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16902 * 0.18577912
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42170 * 0.24846559
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59709 * 0.72966181
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22663 * 0.40761699
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30683 * 0.03867658
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3671 * 0.45193776
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94461 * 0.94748480
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5647 * 0.20277531
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86540 * 0.57079810
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6822 * 0.87291878
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51987 * 0.16413870
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2250 * 0.60268025
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6698 * 0.67873441
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87474 * 0.25460938
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87167 * 0.31298402
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71188 * 0.41688757
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78802 * 0.77351051
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44755 * 0.23075771
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15191 * 0.87077394
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1613 * 0.05919682
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56323 * 0.38644183
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58355 * 0.36018717
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23661 * 0.40569869
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57009 * 0.62118342
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 42545 * 0.63315824
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46430 * 0.33213556
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 51252 * 0.67886244
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 44435 * 0.42980559
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99097 * 0.47836345
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 3921 * 0.54665849
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35671 * 0.51861434
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42681 * 0.09426427
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2591 * 0.87063908
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'zasztuhj').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0024():
    """Extended test 24 for api."""
    x_0 = 79654 * 0.21049531
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42988 * 0.95018896
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23528 * 0.42652044
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50234 * 0.12444218
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62675 * 0.92574779
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50521 * 0.57401132
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50708 * 0.13115046
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40164 * 0.88928372
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26358 * 0.00389874
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 817 * 0.26680375
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71138 * 0.44598677
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78776 * 0.65978882
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47743 * 0.26381575
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88880 * 0.59425752
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19213 * 0.76329241
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49670 * 0.03315567
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43920 * 0.85011351
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70976 * 0.56415008
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52832 * 0.47902284
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28438 * 0.04777765
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41909 * 0.43261850
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44356 * 0.27336500
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11790 * 0.58981294
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87293 * 0.70625329
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51806 * 0.90334267
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3950 * 0.94344569
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88507 * 0.77130513
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97669 * 0.70555564
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86166 * 0.37311713
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64547 * 0.76087054
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36596 * 0.84487689
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 408 * 0.86664071
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80935 * 0.57407340
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38397 * 0.20384628
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33509 * 0.84397704
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41360 * 0.56221565
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'irlxqjai').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0025():
    """Extended test 25 for api."""
    x_0 = 53377 * 0.37044903
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24653 * 0.13354353
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64055 * 0.44815071
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70049 * 0.07785889
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41817 * 0.19591534
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94882 * 0.43091391
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19087 * 0.74860944
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90478 * 0.66495468
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85015 * 0.38682780
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98825 * 0.37196593
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89636 * 0.12044349
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24630 * 0.83748843
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97041 * 0.25318862
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41874 * 0.34734767
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57932 * 0.41713728
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32296 * 0.48066502
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95372 * 0.65468616
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63180 * 0.88920774
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25839 * 0.60297528
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17976 * 0.64439410
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34825 * 0.90070593
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85575 * 0.26364221
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6054 * 0.55610496
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10122 * 0.77228592
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74812 * 0.00898137
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55530 * 0.85381782
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19019 * 0.62972105
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12657 * 0.89029893
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17327 * 0.83900736
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16600 * 0.00189199
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95600 * 0.49932501
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13151 * 0.50154277
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25606 * 0.66746815
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42025 * 0.42922450
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 25762 * 0.04794113
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 12898 * 0.66527897
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74655 * 0.50433245
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'crwtguxy').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0026():
    """Extended test 26 for api."""
    x_0 = 58635 * 0.10837145
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17920 * 0.03105183
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86243 * 0.70691752
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47788 * 0.72742080
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94878 * 0.96197686
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50795 * 0.76042518
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50953 * 0.25686826
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28264 * 0.09986242
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31758 * 0.64811078
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77862 * 0.62292332
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40393 * 0.97050939
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31739 * 0.28481380
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75551 * 0.49518743
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59303 * 0.78444486
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97619 * 0.10326752
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10810 * 0.22502185
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55949 * 0.46408312
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80693 * 0.94408957
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86219 * 0.99140352
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46785 * 0.71633103
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99517 * 0.92604529
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28927 * 0.39223375
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80539 * 0.96529320
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55330 * 0.82562074
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64725 * 0.24378902
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35591 * 0.70592482
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50435 * 0.86020016
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19111 * 0.27858848
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92523 * 0.15631673
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67550 * 0.23454821
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30942 * 0.15527448
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'agddpizd').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0027():
    """Extended test 27 for api."""
    x_0 = 9452 * 0.16780216
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45350 * 0.06939346
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69403 * 0.03844217
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35709 * 0.17942724
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59770 * 0.23018853
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34334 * 0.16371495
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40601 * 0.34636727
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96291 * 0.18082902
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11790 * 0.93610901
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32901 * 0.82559344
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32566 * 0.73684170
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72100 * 0.38173608
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24850 * 0.72879007
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3351 * 0.97256778
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 817 * 0.15669202
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96495 * 0.26340151
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88492 * 0.84703620
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96434 * 0.93436464
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92104 * 0.99335422
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29814 * 0.04755835
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81472 * 0.64428856
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74525 * 0.74550549
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37397 * 0.44782322
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26190 * 0.43493443
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9625 * 0.70800872
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'oqoddnvh').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0028():
    """Extended test 28 for api."""
    x_0 = 61296 * 0.22308832
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27244 * 0.41044013
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18329 * 0.03251304
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80860 * 0.76602571
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1292 * 0.14549650
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20031 * 0.20994170
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73856 * 0.59490688
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99999 * 0.13953064
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86940 * 0.44979759
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54608 * 0.43440005
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6090 * 0.14638170
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16289 * 0.59577626
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3992 * 0.44738494
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49128 * 0.70482129
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12107 * 0.90291298
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40809 * 0.32706816
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97560 * 0.94258962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66318 * 0.43028904
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25895 * 0.18938092
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38312 * 0.87275602
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22382 * 0.23393193
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9517 * 0.60522130
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72719 * 0.55299785
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3051 * 0.36289296
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57457 * 0.34650576
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43985 * 0.78993960
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77788 * 0.12739462
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66325 * 0.47685619
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88841 * 0.18869241
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23670 * 0.91890387
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88718 * 0.08526454
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60190 * 0.20830719
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91959 * 0.36644991
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86445 * 0.92555628
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65709 * 0.29132042
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27171 * 0.53766625
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10565 * 0.29926946
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53741 * 0.23264477
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18695 * 0.15123860
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 58954 * 0.37570337
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86327 * 0.39128170
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'tdoyoeee').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0029():
    """Extended test 29 for api."""
    x_0 = 70661 * 0.32151718
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21082 * 0.66509157
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79157 * 0.84317129
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86600 * 0.97821485
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63659 * 0.71171872
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31406 * 0.75488037
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13533 * 0.17267270
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22157 * 0.91047533
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47961 * 0.81782023
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 14903 * 0.06627625
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92702 * 0.62575691
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15702 * 0.69913485
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61189 * 0.18826490
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54616 * 0.45360940
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99662 * 0.47287594
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42262 * 0.44221663
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1741 * 0.42321712
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53352 * 0.22419017
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86575 * 0.19443851
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27389 * 0.17342853
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89768 * 0.96703622
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47341 * 0.44467644
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50546 * 0.97482134
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77125 * 0.62372663
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34128 * 0.32136307
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14778 * 0.62204032
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35119 * 0.47699193
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44236 * 0.41477551
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32546 * 0.02640549
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98660 * 0.63800697
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83850 * 0.54973487
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83633 * 0.89566017
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76223 * 0.53142368
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35492 * 0.43016170
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62230 * 0.71554515
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76668 * 0.69017657
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96906 * 0.60759547
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71632 * 0.44029297
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86813 * 0.58370091
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 44577 * 0.66038729
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 16099 * 0.84377800
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89580 * 0.61858869
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 26611 * 0.25712407
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11344 * 0.89031969
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 83989 * 0.35413002
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 56377 * 0.28860712
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 68866 * 0.52322056
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 39721 * 0.24220148
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'yazzfiqo').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0030():
    """Extended test 30 for api."""
    x_0 = 20570 * 0.51240010
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50536 * 0.22733814
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 160 * 0.26331075
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96104 * 0.57514491
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68404 * 0.10359589
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59954 * 0.88371275
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51549 * 0.89625424
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44717 * 0.15184866
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21627 * 0.46930491
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86673 * 0.77762012
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90930 * 0.29963312
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86256 * 0.83121427
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83901 * 0.26444341
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2245 * 0.00536303
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31914 * 0.92469514
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19009 * 0.27357672
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18617 * 0.66299501
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20305 * 0.35457128
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92546 * 0.15312773
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29275 * 0.79756488
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50663 * 0.30890373
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'dunvrxuz').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0031():
    """Extended test 31 for api."""
    x_0 = 69219 * 0.51238216
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62837 * 0.42257835
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42852 * 0.51637001
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68684 * 0.19572762
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58486 * 0.33649487
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16292 * 0.94333597
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93321 * 0.15051552
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19648 * 0.39589351
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58689 * 0.85895669
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82646 * 0.93011495
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43420 * 0.18385281
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68804 * 0.31645388
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24214 * 0.02550518
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90592 * 0.59144099
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90360 * 0.08843342
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13379 * 0.09622744
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92385 * 0.41340136
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16403 * 0.49980360
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8853 * 0.03506117
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 53787 * 0.41957973
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57805 * 0.32674645
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14292 * 0.17113196
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66469 * 0.51272930
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15926 * 0.39212665
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2524 * 0.10887691
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73713 * 0.57064549
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88749 * 0.32626721
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44766 * 0.48025486
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40690 * 0.29785708
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82300 * 0.98529854
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8469 * 0.11189069
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85873 * 0.21019449
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18332 * 0.79991257
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44204 * 0.31504674
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85927 * 0.32208550
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21277 * 0.22424730
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49581 * 0.19384979
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35567 * 0.83647899
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14052 * 0.34118837
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'geqxqqyt').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0032():
    """Extended test 32 for api."""
    x_0 = 20257 * 0.31027566
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60668 * 0.01344740
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94321 * 0.20145698
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40046 * 0.02035428
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75797 * 0.80026829
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35675 * 0.09602269
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58061 * 0.36794545
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73959 * 0.41898232
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98382 * 0.31860192
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22841 * 0.45732206
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36736 * 0.41293723
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58294 * 0.10235417
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1203 * 0.34695694
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90815 * 0.77466630
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64616 * 0.83476210
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68014 * 0.35576679
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46178 * 0.33005312
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79770 * 0.51062331
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83589 * 0.15277531
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28162 * 0.31962043
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68123 * 0.05118215
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66627 * 0.44950892
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47800 * 0.51654219
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87977 * 0.95024534
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54032 * 0.58101864
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25954 * 0.58617273
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86052 * 0.84453710
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33387 * 0.88696406
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39063 * 0.58796446
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92616 * 0.94077854
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27598 * 0.86185716
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50394 * 0.44093501
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26169 * 0.95851092
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76357 * 0.71986737
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17763 * 0.66112351
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51502 * 0.26843461
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34999 * 0.79143912
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74777 * 0.84725378
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11859 * 0.83932162
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99498 * 0.33893944
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 1784 * 0.25180242
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 68190 * 0.79386751
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24696 * 0.14434597
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'qmdpopjw').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0033():
    """Extended test 33 for api."""
    x_0 = 95898 * 0.93840182
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58550 * 0.75784071
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82711 * 0.25299124
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55728 * 0.04335914
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34978 * 0.01137841
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70774 * 0.35814870
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34660 * 0.37196262
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63476 * 0.37632807
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97760 * 0.53215652
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68504 * 0.22195674
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13884 * 0.04387336
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81020 * 0.56746514
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96259 * 0.83483294
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12314 * 0.32253911
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59740 * 0.00786610
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31924 * 0.20899780
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62479 * 0.85940399
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21709 * 0.52077384
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13846 * 0.72130444
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6161 * 0.02683940
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 527 * 0.79051292
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57353 * 0.64998236
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13265 * 0.33056288
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20671 * 0.67001897
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36918 * 0.94431246
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39765 * 0.70468430
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88858 * 0.67926733
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48326 * 0.28363536
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62950 * 0.00357703
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1125 * 0.78282150
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22621 * 0.44457603
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76384 * 0.64520838
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 10191 * 0.01658777
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76440 * 0.98878917
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9765 * 0.82979632
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 22233 * 0.92695805
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26972 * 0.25928831
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20424 * 0.49902139
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 90198 * 0.65019350
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84459 * 0.32246725
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84105 * 0.56099996
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18358 * 0.88618250
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 89847 * 0.98847246
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 61778 * 0.84361229
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 24605 * 0.23234361
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 27225 * 0.44343671
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 61624 * 0.93561674
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 69211 * 0.12406930
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'iutkvogg').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0034():
    """Extended test 34 for api."""
    x_0 = 35072 * 0.99195073
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70582 * 0.49194770
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98954 * 0.33137722
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24428 * 0.66427373
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60600 * 0.09920053
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61724 * 0.23606745
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94465 * 0.90591660
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22794 * 0.06727033
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74185 * 0.59829863
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81156 * 0.40850405
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54667 * 0.12213968
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23527 * 0.95402349
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31114 * 0.85334491
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88728 * 0.95286210
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52375 * 0.34923406
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56656 * 0.49875943
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58885 * 0.05764968
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22372 * 0.00672690
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39402 * 0.36872913
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98589 * 0.06605516
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49176 * 0.13835448
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48504 * 0.13924052
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26180 * 0.69179202
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33257 * 0.64872832
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67884 * 0.58291482
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'cddajvhp').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0035():
    """Extended test 35 for api."""
    x_0 = 5713 * 0.81570368
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26708 * 0.75565926
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87998 * 0.94010236
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4339 * 0.95989681
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56448 * 0.77916618
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73956 * 0.57385152
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47400 * 0.62543619
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18209 * 0.06237477
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9411 * 0.62998647
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38474 * 0.18278135
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37594 * 0.93362104
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49482 * 0.97338481
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7918 * 0.46069370
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63859 * 0.66745809
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89656 * 0.09349225
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14111 * 0.99221931
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6130 * 0.53013702
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74379 * 0.69688322
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63832 * 0.10949192
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22663 * 0.08976126
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77689 * 0.69372257
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88546 * 0.73263745
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78609 * 0.61024621
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48414 * 0.35409821
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88022 * 0.13197975
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94189 * 0.06152561
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85803 * 0.21820230
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12400 * 0.11101233
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47784 * 0.85862546
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82815 * 0.08916276
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48576 * 0.29850421
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68082 * 0.67026042
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60111 * 0.94015131
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24793 * 0.07488688
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 679 * 0.54306050
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93610 * 0.05673080
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80810 * 0.74828289
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80179 * 0.53844228
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74750 * 0.12861984
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81134 * 0.25778990
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 33024 * 0.23608267
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93171 * 0.17144722
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18030 * 0.49962801
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11555 * 0.30347498
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 68348 * 0.82034760
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 19410 * 0.95966324
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 25532 * 0.68756059
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 21816 * 0.70152841
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'jucoomzd').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0036():
    """Extended test 36 for api."""
    x_0 = 96226 * 0.01392656
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79890 * 0.35487929
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56685 * 0.17339814
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83300 * 0.31236549
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61034 * 0.83227484
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63579 * 0.50892793
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99084 * 0.87932764
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53107 * 0.26149190
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4463 * 0.34604307
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67315 * 0.39360620
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53081 * 0.35712898
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56001 * 0.04133946
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42089 * 0.45138224
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10880 * 0.19360533
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38306 * 0.69333219
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22378 * 0.21343018
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15170 * 0.47862568
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24520 * 0.56860730
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30264 * 0.61121210
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39149 * 0.47906341
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55634 * 0.24915118
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85605 * 0.98367704
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47195 * 0.20027047
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71932 * 0.46275143
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38495 * 0.87711024
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76445 * 0.11355755
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65187 * 0.45168970
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24455 * 0.73868178
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25784 * 0.02460458
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4208 * 0.98598235
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65796 * 0.54034717
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63854 * 0.42308502
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64781 * 0.96591195
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 7504 * 0.52516012
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62956 * 0.36503672
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'kxdnfjkf').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0037():
    """Extended test 37 for api."""
    x_0 = 67695 * 0.49581146
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87204 * 0.61540103
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2094 * 0.86894817
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46005 * 0.03307716
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46892 * 0.43179065
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48343 * 0.28741055
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72663 * 0.60945922
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10630 * 0.36112411
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23264 * 0.65482193
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73091 * 0.09486145
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46793 * 0.81206339
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18577 * 0.70803394
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31506 * 0.98384457
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48819 * 0.47095852
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31857 * 0.89496534
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83147 * 0.45577456
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73078 * 0.43019717
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64993 * 0.24169355
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77273 * 0.35736151
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15134 * 0.70715149
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44957 * 0.23325575
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47915 * 0.56509568
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13383 * 0.03734325
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18309 * 0.83895495
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ymsiyoqj').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0038():
    """Extended test 38 for api."""
    x_0 = 30296 * 0.92211132
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57022 * 0.70688903
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16834 * 0.72723328
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93669 * 0.59601576
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48641 * 0.47194823
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21821 * 0.69570400
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73611 * 0.39169298
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83019 * 0.79453787
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19294 * 0.75024060
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30407 * 0.08485069
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46174 * 0.67448690
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78140 * 0.40351231
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66475 * 0.55890181
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41528 * 0.05271493
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91382 * 0.78764394
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99523 * 0.76482404
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 551 * 0.90104140
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93721 * 0.72019852
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81140 * 0.16875317
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85168 * 0.46299401
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ethnupmj').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0039():
    """Extended test 39 for api."""
    x_0 = 95442 * 0.93118709
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75108 * 0.60060896
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47369 * 0.42137775
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88663 * 0.54540645
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28978 * 0.55273599
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18599 * 0.17746637
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7130 * 0.81999408
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34208 * 0.33040511
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32115 * 0.21246264
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33519 * 0.74895234
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27990 * 0.34966716
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96619 * 0.59357041
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40231 * 0.60390495
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5826 * 0.42401963
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49822 * 0.63533827
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49246 * 0.27282734
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26162 * 0.74355630
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87978 * 0.57321597
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86679 * 0.91047259
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5119 * 0.64813120
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91223 * 0.94369245
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58007 * 0.89524623
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61180 * 0.99543628
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69385 * 0.43706674
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47418 * 0.96488202
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87849 * 0.74362946
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72811 * 0.61119574
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79583 * 0.78573897
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 98921 * 0.88801520
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53827 * 0.99239259
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10852 * 0.72618291
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 267 * 0.67312270
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24205 * 0.17469847
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2916 * 0.90565244
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86721 * 0.20656662
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52335 * 0.36303653
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24339 * 0.15720842
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'cngpguiu').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0040():
    """Extended test 40 for api."""
    x_0 = 50213 * 0.61427200
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13048 * 0.41769186
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51135 * 0.81027344
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87438 * 0.58869717
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42398 * 0.74896476
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12379 * 0.82802967
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38603 * 0.60849296
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94000 * 0.23350132
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27294 * 0.48507606
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96425 * 0.17953148
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54125 * 0.31479200
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20075 * 0.22492323
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22146 * 0.24502771
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43711 * 0.53519816
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91378 * 0.98801658
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31775 * 0.47725385
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97671 * 0.35593259
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83708 * 0.47112545
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22903 * 0.08568534
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40745 * 0.99785670
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66311 * 0.39400137
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 63876 * 0.18263827
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66674 * 0.49095489
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56266 * 0.76175639
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90055 * 0.54085926
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80307 * 0.17778601
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63786 * 0.47163936
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46657 * 0.19660015
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'pvjexrnz').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0041():
    """Extended test 41 for api."""
    x_0 = 55658 * 0.36268099
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33908 * 0.20030784
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 409 * 0.22838694
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47204 * 0.18364316
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93594 * 0.26884605
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27720 * 0.84264421
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32302 * 0.34104901
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68607 * 0.84538840
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18996 * 0.61422250
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29729 * 0.47435908
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68090 * 0.99390335
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26390 * 0.04789147
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31474 * 0.19335682
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74225 * 0.82136555
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5000 * 0.95896394
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7884 * 0.83361756
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78417 * 0.45263518
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98241 * 0.85814407
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41272 * 0.33702880
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83306 * 0.88069505
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4115 * 0.32102456
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38304 * 0.33850091
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17938 * 0.87086189
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21370 * 0.43287041
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95485 * 0.52620132
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27242 * 0.04320025
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16982 * 0.24055698
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70791 * 0.89754870
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87489 * 0.05377965
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54681 * 0.32300326
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42717 * 0.28434619
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6400 * 0.93539903
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12586 * 0.36886382
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17358 * 0.05503901
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42502 * 0.19010762
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44480 * 0.53475790
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5401 * 0.82114894
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67449 * 0.28365147
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28949 * 0.51090150
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59183 * 0.08691403
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 55464 * 0.95471359
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67765 * 0.34394123
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 42234 * 0.34600597
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 88417 * 0.72607625
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59503 * 0.02722628
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 63451 * 0.33862665
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 90166 * 0.71254820
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 40411 * 0.87657510
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 92691 * 0.32273791
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 23722 * 0.19927389
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'qdqavsps').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0042():
    """Extended test 42 for api."""
    x_0 = 7250 * 0.76917692
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2917 * 0.47878847
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51565 * 0.23191046
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95676 * 0.98929864
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99112 * 0.06565078
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62089 * 0.35546558
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14957 * 0.19552441
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37731 * 0.78208887
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73384 * 0.37068408
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6815 * 0.29975395
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34741 * 0.85292014
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54624 * 0.34170009
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73054 * 0.22090953
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11443 * 0.18819419
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65295 * 0.59438639
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21746 * 0.25572448
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40542 * 0.50742958
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42405 * 0.11452036
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62515 * 0.76598498
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88799 * 0.68830512
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1297 * 0.08579282
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1585 * 0.29804112
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66647 * 0.31200816
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42994 * 0.07039094
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39230 * 0.14973038
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33012 * 0.19375099
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80241 * 0.42971664
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13746 * 0.34336221
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27030 * 0.04953170
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29964 * 0.11879161
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19857 * 0.21305558
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 60255 * 0.21699575
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31588 * 0.92923438
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17488 * 0.94932145
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'plvebncu').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0043():
    """Extended test 43 for api."""
    x_0 = 84151 * 0.01420276
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3521 * 0.33718534
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54299 * 0.32564137
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70803 * 0.15273708
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23472 * 0.75664762
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85055 * 0.88916459
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40687 * 0.51903418
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42857 * 0.76044092
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18222 * 0.06616709
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99220 * 0.46849221
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73396 * 0.87583590
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90370 * 0.90755785
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46107 * 0.32170335
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48069 * 0.91207118
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19128 * 0.78665976
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93846 * 0.88180679
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34351 * 0.04484477
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 401 * 0.33661585
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6900 * 0.92560467
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45642 * 0.16654450
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 15289 * 0.52568409
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13542 * 0.73786170
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46888 * 0.64977689
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ikckxjzf').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0044():
    """Extended test 44 for api."""
    x_0 = 46629 * 0.57482892
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86853 * 0.06071259
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48663 * 0.00381348
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41311 * 0.44959622
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15605 * 0.21688723
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35561 * 0.50634353
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26510 * 0.14965678
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31261 * 0.22754684
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24730 * 0.02802785
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53407 * 0.43566178
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88090 * 0.45869076
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30369 * 0.28671319
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40452 * 0.12666486
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52149 * 0.68945864
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46683 * 0.25025260
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59486 * 0.66024561
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28506 * 0.72484417
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31037 * 0.30226574
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34985 * 0.69708149
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 766 * 0.83628595
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53769 * 0.63527291
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'bzvgktlj').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0045():
    """Extended test 45 for api."""
    x_0 = 16487 * 0.25215866
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35225 * 0.40478401
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98765 * 0.26029861
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87126 * 0.20089613
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60752 * 0.45787756
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48507 * 0.75653951
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78486 * 0.39719713
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83341 * 0.28793161
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90826 * 0.10043003
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57718 * 0.50891892
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49943 * 0.14220303
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77019 * 0.89977473
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54087 * 0.81478749
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93245 * 0.39023231
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85602 * 0.04627484
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 672 * 0.90610152
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50888 * 0.92499777
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69011 * 0.54970554
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19918 * 0.53592647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40735 * 0.02604295
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94623 * 0.13203199
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87170 * 0.62126837
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74563 * 0.06139585
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24836 * 0.89529147
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75815 * 0.10540545
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61347 * 0.78780493
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72458 * 0.98577132
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56763 * 0.69788177
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20881 * 0.79725611
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40760 * 0.76127679
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87463 * 0.79751930
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56946 * 0.42915513
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29343 * 0.38187236
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70921 * 0.00711142
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82290 * 0.63766539
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66940 * 0.44689728
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85247 * 0.49333692
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55300 * 0.08587923
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 29186 * 0.65614448
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55220 * 0.20329336
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'nsjcuhoa').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0046():
    """Extended test 46 for api."""
    x_0 = 48847 * 0.38493379
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82683 * 0.42353614
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58599 * 0.82644719
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19703 * 0.03905216
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33498 * 0.88443666
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48782 * 0.20897122
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58069 * 0.93598267
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47814 * 0.38428267
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84136 * 0.23475991
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88731 * 0.16166155
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36591 * 0.58150920
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99759 * 0.53124661
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76372 * 0.82957281
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30936 * 0.03461524
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83187 * 0.15647340
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6659 * 0.79646642
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22278 * 0.55207224
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30180 * 0.49918749
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26571 * 0.56824352
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60987 * 0.33359180
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63527 * 0.08166415
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42529 * 0.90615109
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56228 * 0.99919862
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76792 * 0.22044223
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30498 * 0.78338720
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77460 * 0.28596500
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3029 * 0.59383434
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82590 * 0.78288216
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95966 * 0.34220781
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72652 * 0.22837064
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9661 * 0.12831704
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36183 * 0.28839389
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'tlsnmcua').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0047():
    """Extended test 47 for api."""
    x_0 = 73773 * 0.96437461
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67931 * 0.91485610
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36761 * 0.28266015
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38675 * 0.07985088
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58880 * 0.59134781
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95645 * 0.11855864
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24016 * 0.36504149
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13562 * 0.06313645
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67285 * 0.88253831
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52086 * 0.11692906
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29556 * 0.79629004
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56532 * 0.82792746
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37048 * 0.98335738
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3673 * 0.06650015
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45021 * 0.33752115
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22627 * 0.33363520
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 73111 * 0.85383104
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52137 * 0.52520104
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90357 * 0.08420657
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46624 * 0.97816362
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22453 * 0.94899679
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56881 * 0.12059497
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81650 * 0.07288908
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35949 * 0.07463218
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53409 * 0.57224280
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1930 * 0.77846699
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92662 * 0.09683634
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27838 * 0.55644064
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39594 * 0.73219987
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15492 * 0.90209087
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36850 * 0.87761885
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89861 * 0.75576292
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81804 * 0.45587148
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17516 * 0.34155557
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90714 * 0.88984094
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58918 * 0.59839657
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79815 * 0.20236064
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96096 * 0.86713701
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66706 * 0.06239027
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55435 * 0.74067576
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43236 * 0.62851799
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 8189 * 0.52690871
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96287 * 0.44012207
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 60405 * 0.76307096
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59900 * 0.75821863
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 41560 * 0.58936230
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 74024 * 0.62645948
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 62349 * 0.82285811
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 65599 * 0.66741577
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 65 * 0.03659885
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'tmsvpfze').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0048():
    """Extended test 48 for api."""
    x_0 = 23927 * 0.23131069
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7567 * 0.11618231
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5270 * 0.42797010
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40100 * 0.33975982
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89591 * 0.12575292
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10022 * 0.62452945
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42312 * 0.46583321
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3849 * 0.99868012
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34030 * 0.72466425
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87320 * 0.52306527
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27370 * 0.12063476
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41431 * 0.91770766
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60473 * 0.98712585
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60790 * 0.71941400
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91702 * 0.10645898
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82019 * 0.69103648
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88006 * 0.76973638
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93775 * 0.26841633
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13316 * 0.44149947
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80555 * 0.29854753
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70423 * 0.92400313
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10678 * 0.75533515
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15021 * 0.52782269
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74509 * 0.45286196
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23746 * 0.05228738
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56824 * 0.74457367
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25516 * 0.97165461
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 10558 * 0.88659773
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29725 * 0.81270247
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94623 * 0.93857390
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12029 * 0.12798189
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95002 * 0.36218799
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'tvhqmhfp').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0049():
    """Extended test 49 for api."""
    x_0 = 68224 * 0.25133749
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26400 * 0.80821698
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99479 * 0.44172883
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61253 * 0.55533272
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84613 * 0.31430404
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45568 * 0.08890030
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40001 * 0.26774932
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34365 * 0.77462582
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16184 * 0.04111824
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50335 * 0.30816278
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54336 * 0.77118598
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79258 * 0.85610649
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29717 * 0.62257795
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89728 * 0.02671600
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83407 * 0.54954197
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63737 * 0.68418897
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12027 * 0.71681023
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22474 * 0.12316712
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28547 * 0.50741440
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17123 * 0.51067181
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97235 * 0.96681620
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17575 * 0.82197473
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50445 * 0.43055899
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90952 * 0.27511669
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60746 * 0.93013399
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1977 * 0.32681518
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94725 * 0.51099317
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3969 * 0.63746999
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'nuttuzlv').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0050():
    """Extended test 50 for api."""
    x_0 = 43723 * 0.65570515
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16222 * 0.22409554
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73815 * 0.31158769
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93501 * 0.93020689
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10592 * 0.56411166
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36483 * 0.94080926
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99119 * 0.69340846
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67217 * 0.38736842
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53865 * 0.51815041
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73340 * 0.54256721
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68878 * 0.93590909
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16208 * 0.02455724
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43496 * 0.10523713
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65208 * 0.40274984
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14882 * 0.51261707
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99227 * 0.55868017
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35764 * 0.19056049
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25831 * 0.91650507
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21402 * 0.86618803
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75402 * 0.55747474
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24089 * 0.84171459
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2084 * 0.63574917
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66747 * 0.07553233
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27338 * 0.03762534
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82011 * 0.52908799
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64224 * 0.09471781
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1712 * 0.72429134
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17281 * 0.44469672
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50735 * 0.06909990
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'yahbgkny').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0051():
    """Extended test 51 for api."""
    x_0 = 65806 * 0.61425446
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75596 * 0.95951340
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15949 * 0.29341444
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55654 * 0.50478128
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80205 * 0.06326227
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98203 * 0.21807240
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91253 * 0.12730291
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50540 * 0.66314154
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18803 * 0.72936505
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19189 * 0.69415075
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87028 * 0.43247547
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23765 * 0.27066521
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 88159 * 0.11276315
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93928 * 0.21499661
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41655 * 0.57330345
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64256 * 0.69370871
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72174 * 0.22425613
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86508 * 0.57317982
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15105 * 0.37453964
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64056 * 0.97572614
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39223 * 0.27756822
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65812 * 0.44684854
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55962 * 0.09375658
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19385 * 0.86981505
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7301 * 0.34063800
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83691 * 0.29407733
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97400 * 0.43541587
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53084 * 0.22828859
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94070 * 0.58321273
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11848 * 0.82127301
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41834 * 0.30859052
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49414 * 0.73251089
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58309 * 0.30034382
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35079 * 0.86874733
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65925 * 0.47143246
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55107 * 0.77904506
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97577 * 0.96598911
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49745 * 0.40491413
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24949 * 0.67631201
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21001 * 0.54387653
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77763 * 0.39743228
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13624 * 0.10920632
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 22349 * 0.18910509
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 95545 * 0.88834398
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'uowjluci').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0052():
    """Extended test 52 for api."""
    x_0 = 67447 * 0.97880006
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61092 * 0.80967662
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99823 * 0.50777270
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87345 * 0.07068954
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98091 * 0.48758787
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6270 * 0.13327328
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43440 * 0.14139824
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76782 * 0.43801965
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39965 * 0.32512180
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44343 * 0.18302161
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18648 * 0.39828246
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67447 * 0.91998091
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21401 * 0.44174628
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14554 * 0.10979267
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57302 * 0.31394211
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34405 * 0.71809293
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14085 * 0.84288552
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91308 * 0.51587461
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86714 * 0.36647333
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66459 * 0.14875442
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17805 * 0.54651367
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43218 * 0.07985323
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75953 * 0.87072472
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42865 * 0.69472206
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6249 * 0.94231292
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79708 * 0.53138523
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80845 * 0.34128153
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60781 * 0.61270044
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51581 * 0.61466828
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56957 * 0.60155947
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86663 * 0.47472999
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87840 * 0.22105429
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 50396 * 0.33382617
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23056 * 0.49039934
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53502 * 0.93643465
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61065 * 0.20343752
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80462 * 0.08383251
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81455 * 0.78680012
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53112 * 0.59719969
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34506 * 0.72542307
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21241 * 0.95780458
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 78229 * 0.68138301
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 72775 * 0.59664624
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34850 * 0.22691862
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'yrharwuh').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0053():
    """Extended test 53 for api."""
    x_0 = 35555 * 0.62769348
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6308 * 0.48667410
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15704 * 0.78477386
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64557 * 0.00480603
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92102 * 0.51665616
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80743 * 0.93875421
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45625 * 0.30856848
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38558 * 0.59706801
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57585 * 0.35478199
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96847 * 0.61270925
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95837 * 0.74500133
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75564 * 0.24578859
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60402 * 0.80192324
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74561 * 0.51496063
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81042 * 0.90075133
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2244 * 0.08192763
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71653 * 0.27020299
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15181 * 0.65565349
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70355 * 0.34194378
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44417 * 0.95910550
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63068 * 0.67155040
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86869 * 0.26617286
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33906 * 0.99604767
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 62447 * 0.06663791
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44043 * 0.11565726
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1010 * 0.61188559
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19224 * 0.47725350
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56038 * 0.17574118
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 45282 * 0.54469428
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17895 * 0.04636978
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9626 * 0.46819808
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92547 * 0.71532439
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44340 * 0.62370487
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27535 * 0.81419369
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 53008 * 0.77418372
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27979 * 0.09395209
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 88274 * 0.01037465
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4179 * 0.44820491
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57811 * 0.77400778
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30602 * 0.38079314
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8034 * 0.65312782
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 17672 * 0.59921508
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 14785 * 0.98176615
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 60101 * 0.75103090
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 79274 * 0.28485996
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 37501 * 0.95956603
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 61239 * 0.13582272
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 5857 * 0.91684276
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'bszctvyo').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0054():
    """Extended test 54 for api."""
    x_0 = 37338 * 0.83078352
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56169 * 0.35049359
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51511 * 0.04178921
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28323 * 0.36785429
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81599 * 0.01905485
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27897 * 0.14265984
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56124 * 0.34242194
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43735 * 0.80306665
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3257 * 0.14018869
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78372 * 0.81727190
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66253 * 0.32182481
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77973 * 0.92744734
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8152 * 0.62927659
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88467 * 0.78428785
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25569 * 0.97105750
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10664 * 0.00305904
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39898 * 0.33185107
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20603 * 0.31203273
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17878 * 0.81113951
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33976 * 0.35503251
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95353 * 0.57040623
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55865 * 0.82420965
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89725 * 0.40331257
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35430 * 0.08714129
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39934 * 0.00501654
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28787 * 0.02705977
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25336 * 0.89881736
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44581 * 0.38206835
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96978 * 0.95285555
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'awzwcqlx').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0055():
    """Extended test 55 for api."""
    x_0 = 26224 * 0.50947999
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52906 * 0.22549562
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49156 * 0.19571824
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50638 * 0.45412335
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80446 * 0.55338405
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24876 * 0.11762411
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12766 * 0.08170619
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90820 * 0.64432137
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40036 * 0.55704299
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79353 * 0.26203668
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37557 * 0.24851349
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9426 * 0.77389591
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80186 * 0.72627694
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67916 * 0.25776590
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57566 * 0.96556444
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18169 * 0.34906470
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90253 * 0.26910352
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29063 * 0.95644787
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39850 * 0.58737155
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93553 * 0.53244370
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78121 * 0.04909579
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43976 * 0.54560957
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28106 * 0.12964279
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77052 * 0.80153857
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88753 * 0.22995519
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58256 * 0.92885850
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84924 * 0.91946774
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97366 * 0.35281106
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59029 * 0.05035433
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9146 * 0.38429514
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59383 * 0.64746526
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90373 * 0.23829573
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5442 * 0.18658630
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79023 * 0.70386412
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97041 * 0.08716856
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44799 * 0.88372037
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24734 * 0.76219036
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72506 * 0.21810242
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'nuasvjzm').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0056():
    """Extended test 56 for api."""
    x_0 = 96646 * 0.77787088
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34455 * 0.92039071
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59229 * 0.27109574
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31560 * 0.04004702
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1419 * 0.55191991
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91473 * 0.51613920
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49025 * 0.77465066
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67992 * 0.97367454
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26439 * 0.84151834
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50940 * 0.45759569
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99546 * 0.87163136
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53855 * 0.56664674
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8813 * 0.89097728
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96518 * 0.28796608
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92352 * 0.05701180
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45440 * 0.38850766
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45990 * 0.16739913
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18895 * 0.12794118
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86025 * 0.88304268
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75792 * 0.24016110
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3072 * 0.72974277
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85936 * 0.82513950
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85653 * 0.43560130
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 3653 * 0.63987998
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 34720 * 0.01744346
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83882 * 0.48209898
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 23755 * 0.88331567
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32277 * 0.67820628
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48940 * 0.03745939
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82998 * 0.96445197
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38065 * 0.66545347
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95293 * 0.65818635
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42333 * 0.66578895
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8195 * 0.67506618
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71839 * 0.96820150
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59711 * 0.93392974
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70700 * 0.09195009
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24610 * 0.37674871
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2271 * 0.04613363
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 71547 * 0.67736351
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 52783 * 0.09080119
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 14154 * 0.90691743
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 20907 * 0.05626334
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84610 * 0.36879273
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 66451 * 0.41851067
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 29994 * 0.70111517
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 16847 * 0.27199502
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 19847 * 0.93720121
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 88429 * 0.37314911
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 98734 * 0.80175000
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'bbqevcgd').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0057():
    """Extended test 57 for api."""
    x_0 = 52361 * 0.11959433
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29796 * 0.67862910
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54850 * 0.33554381
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35128 * 0.13901469
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7131 * 0.77598794
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4322 * 0.48357058
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68210 * 0.02933842
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23468 * 0.63806819
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8753 * 0.17889262
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73533 * 0.81256842
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40209 * 0.21223025
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13759 * 0.84234100
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24343 * 0.57888039
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7842 * 0.74140336
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63896 * 0.89449637
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83927 * 0.14110480
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16776 * 0.76478840
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29340 * 0.66877591
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27078 * 0.53803867
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88010 * 0.30465552
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11072 * 0.26262544
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33791 * 0.20091126
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66754 * 0.16151134
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7286 * 0.40333560
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19008 * 0.98697203
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15001 * 0.85351680
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86487 * 0.61840758
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ofimbvjk').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0058():
    """Extended test 58 for api."""
    x_0 = 22642 * 0.43094345
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84035 * 0.32113899
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57366 * 0.12872482
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32040 * 0.16910532
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84742 * 0.15340560
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42635 * 0.16345788
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30259 * 0.74130403
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29256 * 0.58254930
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90490 * 0.54842559
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6220 * 0.39418225
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98 * 0.58833962
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3252 * 0.84340213
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69834 * 0.79311625
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60733 * 0.97278220
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25040 * 0.84443648
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62812 * 0.86189343
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42247 * 0.71530593
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77503 * 0.47227505
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75056 * 0.54656975
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40585 * 0.06047535
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22667 * 0.55047100
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 53399 * 0.42956542
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40019 * 0.30090473
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 90447 * 0.39020886
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67723 * 0.50135662
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11485 * 0.72669618
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80509 * 0.64182099
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65206 * 0.65471816
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81134 * 0.35604835
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42681 * 0.57397357
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96918 * 0.19859022
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25965 * 0.34715559
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2340 * 0.67335054
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60710 * 0.08694491
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47269 * 0.78273433
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68223 * 0.38076630
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40783 * 0.18661698
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96806 * 0.43655220
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84165 * 0.01939908
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63247 * 0.07662306
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5527 * 0.10542773
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 62487 * 0.76443969
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 7982 * 0.68096965
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 5536 * 0.32232223
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 21691 * 0.26947468
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 9863 * 0.12130616
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'ygufjzfo').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0059():
    """Extended test 59 for api."""
    x_0 = 33478 * 0.74881486
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20950 * 0.20700287
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82046 * 0.58190731
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99301 * 0.86500641
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2235 * 0.63545810
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82677 * 0.52553364
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37215 * 0.72918064
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 5821 * 0.65920439
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95420 * 0.52563066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87356 * 0.14498514
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35998 * 0.70907615
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49586 * 0.62574572
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61771 * 0.29843795
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99170 * 0.20263370
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75041 * 0.91910390
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67106 * 0.51432051
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89521 * 0.71067164
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57596 * 0.72836150
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10177 * 0.67984124
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61647 * 0.52456222
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55185 * 0.11203282
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60140 * 0.82204835
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92041 * 0.04165578
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98925 * 0.72129327
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2889 * 0.40180758
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97351 * 0.69651074
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52138 * 0.29578664
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30122 * 0.83067769
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53540 * 0.62708285
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28304 * 0.14414854
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47778 * 0.82862685
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58389 * 0.68560465
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'yosqsoid').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0060():
    """Extended test 60 for api."""
    x_0 = 16138 * 0.77065628
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69863 * 0.09415379
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64648 * 0.36714450
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51448 * 0.21520807
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5379 * 0.15517462
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57261 * 0.00809054
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49706 * 0.67830780
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42761 * 0.56735215
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91125 * 0.46629321
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35756 * 0.27951501
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25312 * 0.42001839
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83508 * 0.00032364
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4426 * 0.33405681
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5580 * 0.85043520
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3824 * 0.06475056
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84979 * 0.55388451
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76142 * 0.40347468
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77280 * 0.44490988
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88032 * 0.48123927
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52308 * 0.34146643
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3632 * 0.36341885
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 3503 * 0.47105928
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71040 * 0.19314992
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63656 * 0.39468287
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'mdxlqets').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0061():
    """Extended test 61 for api."""
    x_0 = 51361 * 0.64202276
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6557 * 0.92700345
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75465 * 0.49305413
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19967 * 0.42801016
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38645 * 0.93791628
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16322 * 0.69634376
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90432 * 0.58027921
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 78371 * 0.40323686
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20325 * 0.13227185
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26373 * 0.06874999
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15762 * 0.41611060
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90952 * 0.09526220
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58502 * 0.68688324
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96488 * 0.89187321
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61722 * 0.54347020
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54603 * 0.39667758
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10781 * 0.04284564
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71801 * 0.00674365
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37793 * 0.39659150
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50768 * 0.75309835
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11652 * 0.20481951
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58102 * 0.20936391
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50175 * 0.57179513
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22330 * 0.12565511
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16824 * 0.65249675
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46869 * 0.36555769
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 43038 * 0.10443722
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18781 * 0.79248195
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8137 * 0.37456711
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76578 * 0.23020688
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31219 * 0.35624529
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65363 * 0.75923703
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47785 * 0.77334648
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43147 * 0.77354615
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42791 * 0.57950141
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5746 * 0.68663194
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22159 * 0.59485400
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88585 * 0.70583771
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23213 * 0.54822969
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45985 * 0.23942974
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46703 * 0.64584853
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3307 * 0.62106060
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1147 * 0.84779135
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 52538 * 0.21451926
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89517 * 0.95674964
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 67667 * 0.53761337
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'udminybc').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0062():
    """Extended test 62 for api."""
    x_0 = 15316 * 0.72604505
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31868 * 0.44809139
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3744 * 0.23438750
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86128 * 0.29904825
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38480 * 0.99743023
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45766 * 0.50579474
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16537 * 0.32885171
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51674 * 0.37968344
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71872 * 0.39481634
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13365 * 0.69766431
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1865 * 0.69427835
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46909 * 0.70863606
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28833 * 0.39427346
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65969 * 0.02593727
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81847 * 0.99055748
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47885 * 0.46561553
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19194 * 0.04850696
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11042 * 0.88882811
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46696 * 0.74162872
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40559 * 0.82894294
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50901 * 0.71294243
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54248 * 0.35423940
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72323 * 0.25303412
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58694 * 0.13243869
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66422 * 0.28100540
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81100 * 0.34974220
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2263 * 0.92257780
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 62266 * 0.47916242
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65951 * 0.68809634
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10550 * 0.09103365
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60614 * 0.13370125
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51198 * 0.97431438
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73797 * 0.95075440
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75277 * 0.26953476
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61466 * 0.18400905
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60994 * 0.67378807
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2477 * 0.49994336
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87866 * 0.56868391
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87164 * 0.33444788
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80854 * 0.79608195
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32685 * 0.02247922
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50554 * 0.47098807
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 92359 * 0.45479165
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 38031 * 0.37913637
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50173 * 0.66844929
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'nowajlxb').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0063():
    """Extended test 63 for api."""
    x_0 = 2363 * 0.33253928
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35667 * 0.29816306
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87176 * 0.80729689
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69602 * 0.64880954
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87900 * 0.23447895
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76915 * 0.07151060
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56669 * 0.95050227
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8462 * 0.56463004
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72024 * 0.09337803
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5680 * 0.97564193
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6705 * 0.33161547
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84979 * 0.81313310
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14094 * 0.73577519
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69282 * 0.34780068
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75021 * 0.87092645
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48582 * 0.09014161
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84709 * 0.19661089
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87747 * 0.36910934
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91742 * 0.29307067
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70541 * 0.79428516
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56108 * 0.69089778
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60020 * 0.15520425
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14260 * 0.47708744
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68802 * 0.96191350
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19660 * 0.56797507
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88749 * 0.26442521
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30971 * 0.24029909
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84518 * 0.57063295
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9466 * 0.02406151
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39207 * 0.31017420
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23414 * 0.99126302
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43214 * 0.54918509
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7799 * 0.68788557
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20325 * 0.79695974
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24175 * 0.93170232
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3421 * 0.99863175
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8646 * 0.45592854
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'nmlyupht').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0064():
    """Extended test 64 for api."""
    x_0 = 43705 * 0.48910969
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60562 * 0.92970687
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63548 * 0.10280222
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90236 * 0.98934507
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32730 * 0.22997715
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62226 * 0.05696221
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90167 * 0.00163985
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55791 * 0.21070101
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52684 * 0.57395745
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83388 * 0.73077285
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97363 * 0.93121745
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15124 * 0.23559067
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33367 * 0.23791203
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47426 * 0.82266091
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89151 * 0.10185637
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73930 * 0.52838465
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50836 * 0.00317890
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45251 * 0.05243571
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37145 * 0.79941982
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2259 * 0.95353337
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25758 * 0.53239206
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55690 * 0.09638658
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'jtxtnjuu').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0065():
    """Extended test 65 for api."""
    x_0 = 55829 * 0.95452031
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84818 * 0.97557358
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34636 * 0.94909848
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7218 * 0.60277247
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61608 * 0.47803884
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 68734 * 0.16098933
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10466 * 0.86759930
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22265 * 0.20029094
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59145 * 0.87242882
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13861 * 0.62676539
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24211 * 0.88368535
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57529 * 0.93951692
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43030 * 0.66033611
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9181 * 0.41908332
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30841 * 0.67296869
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24118 * 0.59600331
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79783 * 0.70949372
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70940 * 0.99965558
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26514 * 0.04677790
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10090 * 0.79747084
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85289 * 0.15467628
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52019 * 0.60813200
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24118 * 0.13929391
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52897 * 0.34731974
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70780 * 0.81838439
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89594 * 0.14817395
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80277 * 0.82200930
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54004 * 0.25911869
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21490 * 0.28661741
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10222 * 0.62912791
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 77620 * 0.07672982
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4155 * 0.87969775
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 20451 * 0.35505051
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36426 * 0.46221374
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70820 * 0.34750720
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24300 * 0.64796382
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59131 * 0.07104447
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68321 * 0.57587136
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 7260 * 0.10315714
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'vwjzpfed').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0066():
    """Extended test 66 for api."""
    x_0 = 42761 * 0.05077249
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37256 * 0.54795236
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5154 * 0.99565461
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49521 * 0.65817735
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61012 * 0.69021251
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7167 * 0.35073324
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78589 * 0.92528570
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51988 * 0.55603989
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44261 * 0.34864394
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40717 * 0.26575888
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50751 * 0.12801463
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31159 * 0.87327464
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34476 * 0.94908970
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69518 * 0.17019346
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71806 * 0.64742357
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21342 * 0.73004151
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61936 * 0.41259453
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52313 * 0.71036892
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95097 * 0.76851437
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35710 * 0.03043474
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97062 * 0.18338971
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40973 * 0.57362344
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94936 * 0.67305962
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77775 * 0.26243329
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'rszadlzo').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0067():
    """Extended test 67 for api."""
    x_0 = 48108 * 0.86119732
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 53320 * 0.96880518
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92865 * 0.07200473
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16194 * 0.22666278
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31071 * 0.38246333
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47008 * 0.82124257
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7046 * 0.55139243
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80922 * 0.83036537
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64368 * 0.53441608
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34185 * 0.08917084
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88448 * 0.30979255
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48797 * 0.94249262
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48730 * 0.88860882
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30652 * 0.29750944
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14311 * 0.57240643
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47436 * 0.77446542
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67249 * 0.00057287
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22711 * 0.72421022
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14777 * 0.44396908
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42568 * 0.17027724
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71745 * 0.03780186
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82810 * 0.88352895
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'mhxmcvgd').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0068():
    """Extended test 68 for api."""
    x_0 = 4339 * 0.97453935
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60982 * 0.01623000
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54766 * 0.82781764
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1258 * 0.25162209
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74871 * 0.91760843
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71490 * 0.09847879
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92337 * 0.73960484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4640 * 0.35918976
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92030 * 0.07753376
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3525 * 0.79066937
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69734 * 0.12032968
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48489 * 0.18472772
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16060 * 0.75272627
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43307 * 0.75793448
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82258 * 0.89140486
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35724 * 0.91211282
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86835 * 0.94294035
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27924 * 0.03661435
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68560 * 0.40232327
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52032 * 0.05848226
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ofctcjjn').hexdigest()
    assert len(h) == 64

def test_api_extended_8_0069():
    """Extended test 69 for api."""
    x_0 = 90133 * 0.16443718
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22345 * 0.38583967
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83201 * 0.71779914
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32607 * 0.31071071
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18003 * 0.06306104
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3833 * 0.22509918
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60934 * 0.92853555
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4829 * 0.92267920
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36487 * 0.08221359
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5716 * 0.75224612
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66611 * 0.86680297
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73127 * 0.70917745
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 1915 * 0.79861750
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7075 * 0.16212188
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23944 * 0.17582161
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32597 * 0.60834085
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27464 * 0.22744842
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84741 * 0.26875256
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9253 * 0.09347352
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52944 * 0.54087437
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43889 * 0.33965710
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52357 * 0.42554551
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52794 * 0.99026868
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16695 * 0.16862302
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13382 * 0.83331060
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60212 * 0.78806268
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18587 * 0.85162766
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22701 * 0.88718702
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 27774 * 0.06477911
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'fyacuyfv').hexdigest()
    assert len(h) == 64
