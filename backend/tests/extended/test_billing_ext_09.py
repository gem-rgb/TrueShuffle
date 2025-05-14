"""Extended tests for billing suite 9."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_billing_extended_9_0000():
    """Extended test 0 for billing."""
    x_0 = 61870 * 0.98515106
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 44662 * 0.43409918
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28012 * 0.13826800
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92243 * 0.26493859
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45807 * 0.51209576
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66072 * 0.91422833
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20793 * 0.20701979
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22259 * 0.37549802
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6454 * 0.55757752
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19441 * 0.24792108
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90845 * 0.44421352
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71246 * 0.75404675
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67018 * 0.16566460
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34836 * 0.71605693
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71576 * 0.29316706
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7312 * 0.90704118
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63971 * 0.92545423
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72443 * 0.67302582
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58169 * 0.98928759
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65824 * 0.52638381
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97610 * 0.48996206
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37947 * 0.84003416
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11758 * 0.51171853
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76186 * 0.40948439
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26047 * 0.67451254
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88641 * 0.29509726
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28529 * 0.26716509
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92242 * 0.47978809
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9761 * 0.64841060
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6602 * 0.22925515
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72755 * 0.78805804
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21977 * 0.61174167
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'favgezxd').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0001():
    """Extended test 1 for billing."""
    x_0 = 13 * 0.86422567
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21705 * 0.09622832
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73628 * 0.68112487
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90852 * 0.06984635
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84825 * 0.49095537
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50241 * 0.17945189
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27976 * 0.57761235
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41063 * 0.89006986
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90494 * 0.40705136
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45623 * 0.84143303
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93594 * 0.30017665
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18774 * 0.15206172
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17156 * 0.50863703
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53656 * 0.66971871
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43249 * 0.13308150
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47690 * 0.97764583
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90656 * 0.73788380
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58561 * 0.09775513
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40624 * 0.84374980
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47058 * 0.70231903
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62133 * 0.19250996
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62916 * 0.26200162
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6785 * 0.41338879
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40169 * 0.84689101
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56531 * 0.17705780
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23886 * 0.20179880
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56763 * 0.49971391
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 58194 * 0.23413932
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 71024 * 0.46572886
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89875 * 0.83637749
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41755 * 0.95213017
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15753 * 0.47997894
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14921 * 0.67229326
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30789 * 0.01113476
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78405 * 0.38714637
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26386 * 0.84767199
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18611 * 0.33031269
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34120 * 0.37815768
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64654 * 0.72381351
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 81279 * 0.42539377
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'iptxyvdi').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0002():
    """Extended test 2 for billing."""
    x_0 = 54816 * 0.39186499
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78715 * 0.11768196
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31503 * 0.25692868
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7204 * 0.61094150
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95979 * 0.95267274
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63032 * 0.96943035
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26961 * 0.32298351
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57560 * 0.37667932
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70020 * 0.30275296
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68990 * 0.69507289
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71977 * 0.93448965
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41862 * 0.69913201
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93009 * 0.29018473
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2875 * 0.05424253
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32970 * 0.90693082
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86643 * 0.45882550
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76113 * 0.69879893
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90220 * 0.86976530
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26928 * 0.03110446
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34136 * 0.61865547
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83621 * 0.07325731
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56365 * 0.45049039
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53969 * 0.79899439
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49235 * 0.05585050
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32745 * 0.06560526
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92952 * 0.18811835
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59096 * 0.24313841
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'pncidhts').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0003():
    """Extended test 3 for billing."""
    x_0 = 44961 * 0.94010194
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10070 * 0.27857107
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51210 * 0.73886470
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11854 * 0.17344894
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78790 * 0.02659047
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36181 * 0.28187859
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58074 * 0.67573168
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57543 * 0.28837451
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71510 * 0.49078801
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46785 * 0.36306056
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40448 * 0.46503195
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 977 * 0.01497008
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56749 * 0.44407093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60495 * 0.01364837
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65404 * 0.29437588
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71065 * 0.42869280
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92220 * 0.32452791
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10152 * 0.23256273
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81305 * 0.02649595
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85200 * 0.51208359
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62607 * 0.44619914
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31019 * 0.93295993
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89843 * 0.55968516
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44823 * 0.12437040
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97956 * 0.97788186
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93124 * 0.44923269
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64097 * 0.07232009
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88612 * 0.76413512
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33064 * 0.20822939
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71590 * 0.51185814
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93701 * 0.63313054
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13601 * 0.06074039
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31985 * 0.75492294
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60302 * 0.06107600
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29662 * 0.00272633
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63747 * 0.37673319
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 79941 * 0.27732958
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 7542 * 0.00323538
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88049 * 0.93705340
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90190 * 0.46099365
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38536 * 0.16577292
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 99697 * 0.18847561
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83972 * 0.18011758
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69988 * 0.22067982
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 45049 * 0.16806684
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 88073 * 0.94332086
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 60916 * 0.09441989
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 31502 * 0.11341206
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'pgybxtru').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0004():
    """Extended test 4 for billing."""
    x_0 = 60760 * 0.77728590
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26134 * 0.92252004
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44788 * 0.48122258
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33631 * 0.02346586
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32870 * 0.82037521
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87335 * 0.30816175
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50609 * 0.62154336
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63391 * 0.04637975
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41084 * 0.43511321
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49425 * 0.55449126
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79898 * 0.23760855
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10904 * 0.50053992
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41310 * 0.75444302
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3042 * 0.60533495
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24099 * 0.17703260
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79505 * 0.31247957
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41430 * 0.31823761
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49342 * 0.02948324
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75792 * 0.32713312
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19810 * 0.53102724
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78501 * 0.03008348
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84157 * 0.28140561
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51027 * 0.29955049
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38860 * 0.00022204
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 92826 * 0.91093210
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68756 * 0.42871409
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36877 * 0.78918955
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34885 * 0.30284364
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46635 * 0.32001020
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63968 * 0.03108921
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90358 * 0.50942484
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35644 * 0.48578407
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99820 * 0.36247920
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42415 * 0.03485523
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 71798 * 0.36309255
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5142 * 0.58165301
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93097 * 0.84441892
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'hiuxedip').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0005():
    """Extended test 5 for billing."""
    x_0 = 1675 * 0.88153703
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35642 * 0.81676581
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71299 * 0.49367188
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25093 * 0.25762724
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62304 * 0.15693275
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31639 * 0.33540831
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9048 * 0.80965989
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52144 * 0.22884417
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20068 * 0.44606231
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8398 * 0.74252316
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35301 * 0.28023072
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60281 * 0.69964742
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11220 * 0.79974826
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26796 * 0.03660422
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33072 * 0.33519513
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20046 * 0.33216957
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74333 * 0.76483121
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62733 * 0.36963938
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78778 * 0.09549223
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52264 * 0.24867120
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63172 * 0.51402807
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6192 * 0.08154871
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24509 * 0.54433004
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27150 * 0.61914016
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97260 * 0.50865622
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94781 * 0.56174631
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92195 * 0.80198469
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47533 * 0.02669198
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75813 * 0.31148651
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17830 * 0.35791163
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60833 * 0.23047939
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58673 * 0.11004109
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29268 * 0.67787382
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 72658 * 0.37695701
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86517 * 0.43786426
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17884 * 0.57609432
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14990 * 0.46425465
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 28090 * 0.15545322
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1769 * 0.36512696
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3307 * 0.03303323
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3517 * 0.25183697
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88762 * 0.64868809
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'bfatwpho').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0006():
    """Extended test 6 for billing."""
    x_0 = 30937 * 0.61384219
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11132 * 0.67877389
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22417 * 0.17768567
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78070 * 0.57243525
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94503 * 0.28686703
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14579 * 0.87164612
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63495 * 0.72440520
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54563 * 0.43846791
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74940 * 0.96786276
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12947 * 0.08351648
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39202 * 0.30952958
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68485 * 0.46778629
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77194 * 0.82734973
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2136 * 0.01132701
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54422 * 0.93169980
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9094 * 0.92364819
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40094 * 0.15714179
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60272 * 0.09077728
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57595 * 0.62154461
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20774 * 0.63016314
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63936 * 0.69723671
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'ialqqdjh').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0007():
    """Extended test 7 for billing."""
    x_0 = 6546 * 0.14146130
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94994 * 0.72314525
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74046 * 0.39429913
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33778 * 0.00208890
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26557 * 0.40608870
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58353 * 0.20232345
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28369 * 0.53272980
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8034 * 0.58592107
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96698 * 0.53976534
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83583 * 0.41917446
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48467 * 0.48817615
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62935 * 0.04470993
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80676 * 0.44825796
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88103 * 0.64429084
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47732 * 0.51183507
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84458 * 0.33266681
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87792 * 0.33601990
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52519 * 0.55569169
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58532 * 0.82620573
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85384 * 0.20953413
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92871 * 0.41137922
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4551 * 0.90317648
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66800 * 0.37583346
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71360 * 0.81952490
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12136 * 0.09186341
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95287 * 0.42317816
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12980 * 0.96094085
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93283 * 0.17980907
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89619 * 0.45800246
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'pbhzyumy').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0008():
    """Extended test 8 for billing."""
    x_0 = 8425 * 0.35299028
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11624 * 0.18391243
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10331 * 0.57034757
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86550 * 0.70923568
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64852 * 0.60224716
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98306 * 0.24465662
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89094 * 0.02430092
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25440 * 0.63114414
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17058 * 0.61607905
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8044 * 0.82150010
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48457 * 0.53776553
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55006 * 0.87733971
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60346 * 0.01378645
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34079 * 0.65618021
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23818 * 0.49142505
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15159 * 0.11199664
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57777 * 0.44251316
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75815 * 0.74668642
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92725 * 0.00788228
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 62760 * 0.25879557
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47842 * 0.46657686
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93104 * 0.05036111
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81889 * 0.79083991
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5859 * 0.48111398
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77708 * 0.04242401
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60672 * 0.37137410
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74816 * 0.16442829
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26179 * 0.48258768
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2895 * 0.05291332
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 103 * 0.48260437
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10460 * 0.73712430
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48734 * 0.46376943
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54932 * 0.21195281
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17182 * 0.66774382
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13525 * 0.86018338
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50907 * 0.18288416
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'wipjpzpe').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0009():
    """Extended test 9 for billing."""
    x_0 = 74793 * 0.07061585
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7014 * 0.82915889
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89134 * 0.97401471
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14337 * 0.18414394
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65684 * 0.60758843
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53751 * 0.41145010
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48388 * 0.89710506
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24348 * 0.11910361
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71875 * 0.58069412
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1062 * 0.57244562
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62168 * 0.33073447
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9558 * 0.03836453
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11698 * 0.91628985
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31734 * 0.57692912
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42042 * 0.26946547
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39346 * 0.75827837
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95649 * 0.62430384
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14355 * 0.17788308
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20626 * 0.14407733
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84931 * 0.46567898
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24989 * 0.50636758
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13231 * 0.23988345
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70394 * 0.06256782
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88599 * 0.71274508
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38878 * 0.83618673
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92690 * 0.78142715
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87900 * 0.48579277
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'wkbspxre').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0010():
    """Extended test 10 for billing."""
    x_0 = 91142 * 0.64228257
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77565 * 0.87876386
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55494 * 0.23696174
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57486 * 0.73942043
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77511 * 0.75339261
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60272 * 0.13200604
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5555 * 0.56964715
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44247 * 0.04086817
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15229 * 0.51414222
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40446 * 0.95262874
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64228 * 0.05407225
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14855 * 0.76769657
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53147 * 0.18345138
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2800 * 0.86036835
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36975 * 0.51192331
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19962 * 0.87753267
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32553 * 0.32456284
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41568 * 0.79390552
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40867 * 0.52179002
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13779 * 0.14404777
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68280 * 0.66763743
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86122 * 0.01485769
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66733 * 0.67302177
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64510 * 0.10952853
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2780 * 0.66207168
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45971 * 0.01831137
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26544 * 0.87048120
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 80435 * 0.16059457
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4844 * 0.17538531
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16703 * 0.24805965
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50158 * 0.44719464
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92892 * 0.12334498
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40925 * 0.30856986
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79267 * 0.63169656
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51308 * 0.83304613
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45902 * 0.77985413
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86964 * 0.09419835
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 43249 * 0.66311338
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71424 * 0.22226117
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'dncalwja').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0011():
    """Extended test 11 for billing."""
    x_0 = 13026 * 0.60208814
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54255 * 0.38116439
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60945 * 0.21709206
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5208 * 0.73487275
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79644 * 0.17648080
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32291 * 0.88080266
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47802 * 0.26179709
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83854 * 0.92165077
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71187 * 0.82360907
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47084 * 0.98412507
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90454 * 0.66713207
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80709 * 0.89161890
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83186 * 0.56489240
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6021 * 0.11825280
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21831 * 0.45446734
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94234 * 0.35165859
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28629 * 0.07012098
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99646 * 0.72225396
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49227 * 0.82239573
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98140 * 0.12131851
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91703 * 0.73813143
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87824 * 0.48897088
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46778 * 0.84933201
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80624 * 0.19903776
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56148 * 0.99906470
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73710 * 0.56092323
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68641 * 0.60966687
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68962 * 0.19421199
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63732 * 0.71589895
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35639 * 0.72311498
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26793 * 0.76779965
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89705 * 0.85244201
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89966 * 0.53447048
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9808 * 0.32293745
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92420 * 0.25374525
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75798 * 0.79258277
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55101 * 0.40610746
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84178 * 0.78909293
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67082 * 0.73728177
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9034 * 0.45408510
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 76443 * 0.18429840
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 79880 * 0.06671967
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41526 * 0.68970736
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 30183 * 0.14693564
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 40015 * 0.72122931
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 89760 * 0.21999611
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 6636 * 0.97754238
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 95335 * 0.54273052
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 61759 * 0.78076316
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'afbciinp').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0012():
    """Extended test 12 for billing."""
    x_0 = 67926 * 0.34135096
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84615 * 0.32738546
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66068 * 0.47406222
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9323 * 0.97628698
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47731 * 0.77360874
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31011 * 0.18926331
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30414 * 0.87188765
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74246 * 0.71176699
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8330 * 0.50526413
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26863 * 0.48846348
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80396 * 0.87015315
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40704 * 0.84637885
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94125 * 0.02507515
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49453 * 0.47571295
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65813 * 0.82633791
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99175 * 0.79938110
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31420 * 0.93471591
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28005 * 0.01555693
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64572 * 0.24605856
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7789 * 0.47776137
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71364 * 0.31652923
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'qugrldgm').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0013():
    """Extended test 13 for billing."""
    x_0 = 50806 * 0.98966283
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90692 * 0.67084672
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94748 * 0.74236653
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13219 * 0.82053722
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46505 * 0.70479519
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35060 * 0.61332189
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51143 * 0.94822640
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29928 * 0.89554038
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42492 * 0.32556652
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73756 * 0.11938133
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35229 * 0.47951521
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86610 * 0.97535869
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73148 * 0.90828473
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99238 * 0.73810885
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27918 * 0.06331571
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31642 * 0.78051048
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87934 * 0.95422990
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60221 * 0.87636991
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9241 * 0.18453180
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31411 * 0.65008374
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10129 * 0.81143976
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35465 * 0.46664234
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83835 * 0.51088743
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52732 * 0.26397494
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87182 * 0.11418676
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35016 * 0.38095820
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59368 * 0.90789324
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87769 * 0.54093317
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56452 * 0.20669179
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37442 * 0.76352151
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26119 * 0.68970982
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75428 * 0.06433358
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24075 * 0.95043965
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36990 * 0.34408310
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82476 * 0.26306447
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8936 * 0.93885570
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95272 * 0.97658063
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'wotzyqyx').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0014():
    """Extended test 14 for billing."""
    x_0 = 15823 * 0.18164493
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81647 * 0.72845216
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55470 * 0.74915909
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19111 * 0.98027083
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28172 * 0.47229168
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67006 * 0.29374379
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61178 * 0.49469396
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48559 * 0.81368175
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34923 * 0.81309766
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41665 * 0.51599776
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 56820 * 0.35091247
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73115 * 0.88129399
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94133 * 0.96406750
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 450 * 0.91144950
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85048 * 0.13204472
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83560 * 0.84020477
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45575 * 0.56994983
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 30495 * 0.57796746
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51783 * 0.04119744
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40709 * 0.55956238
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48579 * 0.78796285
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71435 * 0.89905508
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43236 * 0.61057842
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89980 * 0.66073394
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31370 * 0.85628089
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24566 * 0.48201773
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74543 * 0.15579177
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64255 * 0.72498908
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48026 * 0.40723430
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62184 * 0.07468311
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45225 * 0.91198296
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27324 * 0.71207442
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74007 * 0.56316311
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69804 * 0.09889358
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66651 * 0.78281565
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47444 * 0.74244548
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28590 * 0.35318725
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8382 * 0.27969361
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59846 * 0.35043345
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 40600 * 0.06955246
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8408 * 0.23322186
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 8056 * 0.06772183
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 39260 * 0.32813118
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 47232 * 0.31471709
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'gdjlhgxf').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0015():
    """Extended test 15 for billing."""
    x_0 = 91942 * 0.16536697
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1159 * 0.16814997
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 438 * 0.54684134
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20813 * 0.47456623
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29655 * 0.91277119
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14842 * 0.67966713
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34405 * 0.15345283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39457 * 0.12719116
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21664 * 0.03147310
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96131 * 0.71168203
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24857 * 0.79661266
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15553 * 0.62980792
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18997 * 0.54030557
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54835 * 0.40975550
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98688 * 0.87646854
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47923 * 0.81124535
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35805 * 0.70723876
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65804 * 0.33059041
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47103 * 0.94457315
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30006 * 0.23149657
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79141 * 0.21749868
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96955 * 0.14031059
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57280 * 0.61578692
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36325 * 0.36949590
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69470 * 0.86594882
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37040 * 0.36031167
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10404 * 0.40765906
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99488 * 0.88068694
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18149 * 0.42000495
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91026 * 0.72804916
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96886 * 0.94057257
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59231 * 0.80499193
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7075 * 0.79843718
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38751 * 0.73428721
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11294 * 0.77855544
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47340 * 0.08959059
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 24486 * 0.42659476
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36600 * 0.45332384
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 31008 * 0.22491269
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93142 * 0.97571078
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 55906 * 0.49842029
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 7469 * 0.61241084
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 55194 * 0.50822301
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 74801 * 0.57589023
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 52343 * 0.39743549
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'qzfeykhm').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0016():
    """Extended test 16 for billing."""
    x_0 = 77232 * 0.94111009
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65380 * 0.66197025
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28993 * 0.15595967
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 73698 * 0.58024106
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52929 * 0.12798040
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93805 * 0.43448624
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71392 * 0.57999826
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66337 * 0.53449024
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28732 * 0.70666710
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96439 * 0.27951000
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79913 * 0.41252367
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81058 * 0.46004509
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9194 * 0.71721680
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68364 * 0.05604684
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38072 * 0.26664700
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24572 * 0.26208968
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53631 * 0.49034728
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46571 * 0.87513104
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18393 * 0.13058730
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34535 * 0.67950438
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7110 * 0.80893680
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17987 * 0.58603696
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17164 * 0.25502059
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98458 * 0.64810539
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18511 * 0.47001975
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13584 * 0.52829535
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90823 * 0.29233653
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91701 * 0.67751983
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8768 * 0.26411905
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 8274 * 0.05026206
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8872 * 0.35806172
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89734 * 0.94249803
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91397 * 0.68706442
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57655 * 0.80328096
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37591 * 0.32495444
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44312 * 0.11207704
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50814 * 0.45492558
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11121 * 0.60080329
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'yurecvtg').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0017():
    """Extended test 17 for billing."""
    x_0 = 29093 * 0.20631226
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7584 * 0.14226149
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50302 * 0.31929441
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67146 * 0.32515285
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15127 * 0.37155956
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20319 * 0.75284500
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 78589 * 0.51469294
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87796 * 0.37107415
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59788 * 0.61861940
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25847 * 0.53837276
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46597 * 0.14787621
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89743 * 0.83515928
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72456 * 0.92083002
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61501 * 0.66057395
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44287 * 0.33790303
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66356 * 0.99996669
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19030 * 0.61850862
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47631 * 0.58454946
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91797 * 0.08635238
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97015 * 0.29705107
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68332 * 0.68590792
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56547 * 0.55455706
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78433 * 0.07810294
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34853 * 0.73884141
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46051 * 0.13433057
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71657 * 0.78230222
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58117 * 0.00151573
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50668 * 0.27746476
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'yqqbupob').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0018():
    """Extended test 18 for billing."""
    x_0 = 83451 * 0.12377633
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84162 * 0.05045543
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54712 * 0.34581208
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7072 * 0.29879742
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36694 * 0.87902047
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13649 * 0.37184835
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3550 * 0.40295635
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47920 * 0.60334505
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67112 * 0.77848462
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67230 * 0.08129936
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3640 * 0.97665773
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35426 * 0.85155906
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77229 * 0.32164523
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86887 * 0.95939123
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79842 * 0.17199422
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55484 * 0.19187261
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24093 * 0.74077978
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55646 * 0.51557509
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73420 * 0.75766626
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29511 * 0.84291986
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78580 * 0.02379449
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85636 * 0.63675462
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15299 * 0.78139010
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74023 * 0.31181688
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28760 * 0.62289366
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11595 * 0.61894267
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79271 * 0.18158100
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83 * 0.84608176
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7212 * 0.83120570
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91068 * 0.99787199
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78596 * 0.30943620
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92208 * 0.92126291
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30703 * 0.79703144
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 79027 * 0.79949528
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84239 * 0.76054691
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 76029 * 0.79902179
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56521 * 0.14804148
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64959 * 0.04808125
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 45390 * 0.74213425
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 20574 * 0.99845538
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71188 * 0.30650656
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 56521 * 0.92727286
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9242 * 0.88262891
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 35711 * 0.12056507
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10155 * 0.23370337
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26949 * 0.44870593
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 90756 * 0.42085833
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'jlcphgsp').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0019():
    """Extended test 19 for billing."""
    x_0 = 92151 * 0.93694257
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92131 * 0.76494715
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15298 * 0.42214229
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83806 * 0.63494160
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52007 * 0.90806760
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96685 * 0.35245744
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58187 * 0.08530193
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98298 * 0.29546388
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27566 * 0.25945723
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71173 * 0.99506864
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78422 * 0.32984545
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99444 * 0.91954731
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60408 * 0.94306907
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28898 * 0.40020602
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21904 * 0.74443873
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48538 * 0.05062515
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16439 * 0.29602800
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 85023 * 0.23273917
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33018 * 0.00314811
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52196 * 0.71489921
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47156 * 0.06593539
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23795 * 0.47279811
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'nxzzyaen').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0020():
    """Extended test 20 for billing."""
    x_0 = 7231 * 0.30974491
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7184 * 0.36232710
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70270 * 0.01428988
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74597 * 0.07621239
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69357 * 0.51419374
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7291 * 0.16355250
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58568 * 0.63208494
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87954 * 0.78489901
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59539 * 0.68678207
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2508 * 0.39554123
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46954 * 0.17241546
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17036 * 0.31321630
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38986 * 0.98621850
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37185 * 0.39886114
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 928 * 0.64784364
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32043 * 0.74643507
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14440 * 0.05386709
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47246 * 0.38664848
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2453 * 0.22923036
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89525 * 0.43571572
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44332 * 0.58490106
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'crehlifd').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0021():
    """Extended test 21 for billing."""
    x_0 = 1643 * 0.46331786
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31718 * 0.60243511
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54479 * 0.35385778
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71814 * 0.17048796
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50586 * 0.39004850
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88459 * 0.05964761
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85763 * 0.78018793
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39008 * 0.95666300
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41030 * 0.58121866
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12964 * 0.36653351
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61938 * 0.31808176
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73721 * 0.08406474
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53187 * 0.45074943
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88553 * 0.47214089
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51281 * 0.48252150
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88049 * 0.24359162
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71503 * 0.03764063
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28895 * 0.95387681
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36689 * 0.22797255
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73886 * 0.59137635
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38560 * 0.44989054
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15931 * 0.99370534
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26003 * 0.41877725
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56557 * 0.12143397
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45484 * 0.98243852
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58888 * 0.84043096
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33805 * 0.15969032
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50385 * 0.00713738
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91200 * 0.76760452
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18813 * 0.87536744
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 41907 * 0.13529800
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97735 * 0.52217166
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 90857 * 0.97673180
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40873 * 0.34389198
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7705 * 0.26567541
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77361 * 0.51372978
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94808 * 0.28900240
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16037 * 0.26375087
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'kefzrtql').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0022():
    """Extended test 22 for billing."""
    x_0 = 97676 * 0.16381920
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25516 * 0.80428441
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77323 * 0.57411753
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78860 * 0.98183156
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30689 * 0.28559794
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1401 * 0.53536044
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99540 * 0.09539231
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22193 * 0.06036334
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36025 * 0.66242847
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36465 * 0.43876276
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12010 * 0.05805844
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66283 * 0.82243056
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18973 * 0.17889346
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5749 * 0.08433923
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3265 * 0.95006883
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11059 * 0.45478325
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40858 * 0.35138689
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55066 * 0.38277561
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78349 * 0.62392904
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15679 * 0.30150064
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77975 * 0.61948344
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36738 * 0.51206057
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99391 * 0.34224279
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88825 * 0.12515866
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87885 * 0.19848503
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54356 * 0.70589673
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60796 * 0.95181391
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86937 * 0.64377370
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80582 * 0.74233771
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92257 * 0.37918201
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23823 * 0.10503172
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52023 * 0.61350399
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31076 * 0.49743621
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53248 * 0.40998216
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79940 * 0.84306292
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67312 * 0.61925175
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8423 * 0.17687690
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34741 * 0.29933541
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72161 * 0.36155631
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73301 * 0.92082666
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'tprjiyzj').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0023():
    """Extended test 23 for billing."""
    x_0 = 56211 * 0.97582500
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41301 * 0.09612327
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45637 * 0.64629349
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59991 * 0.62121106
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36868 * 0.15064591
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98496 * 0.49244068
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9114 * 0.11575616
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70628 * 0.77450939
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64723 * 0.76082503
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 85973 * 0.82528183
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 30464 * 0.29877299
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28502 * 0.45177387
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78009 * 0.36121871
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18020 * 0.06694379
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9816 * 0.10813037
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35580 * 0.16315900
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6093 * 0.79132044
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99642 * 0.21813581
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81641 * 0.20709608
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23149 * 0.04588874
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72732 * 0.30243699
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69771 * 0.07102669
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13822 * 0.16893237
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69988 * 0.66273868
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41119 * 0.78611295
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31133 * 0.31889045
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27087 * 0.80163401
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68622 * 0.56958329
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34219 * 0.86990415
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22774 * 0.73723953
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83578 * 0.42482460
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2881 * 0.10783891
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75601 * 0.76309224
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 88189 * 0.60768826
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76034 * 0.56306973
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34257 * 0.46388575
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13853 * 0.40678565
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25811 * 0.37196216
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 69110 * 0.62037830
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 64302 * 0.63120607
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'gxalnzxc').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0024():
    """Extended test 24 for billing."""
    x_0 = 21418 * 0.08669947
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73427 * 0.68425500
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46219 * 0.43021588
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 218 * 0.72426097
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77829 * 0.96315032
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15274 * 0.34971614
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61780 * 0.86305122
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55786 * 0.39061308
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98594 * 0.58727564
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19480 * 0.58896538
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87539 * 0.95697124
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6335 * 0.02102892
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28917 * 0.80582859
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6125 * 0.29528920
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40325 * 0.88899966
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24455 * 0.88451386
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78849 * 0.08010518
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26412 * 0.62065729
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34394 * 0.54194497
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25983 * 0.52923400
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59666 * 0.17179991
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80089 * 0.99129446
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87463 * 0.26940530
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71886 * 0.95164489
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32080 * 0.80874402
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40 * 0.07940114
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'rgeqflsn').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0025():
    """Extended test 25 for billing."""
    x_0 = 61862 * 0.10114865
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51592 * 0.89287437
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40800 * 0.05027667
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42432 * 0.60705793
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74493 * 0.43667531
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63013 * 0.22663232
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19983 * 0.72766926
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93274 * 0.39368856
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31008 * 0.94882768
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43342 * 0.87838673
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89341 * 0.77594384
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9522 * 0.95222857
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67958 * 0.91194174
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64551 * 0.37597825
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91099 * 0.64471419
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73654 * 0.99363673
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20016 * 0.15875162
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78927 * 0.90117966
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37945 * 0.55592329
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56666 * 0.67038985
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 536 * 0.20178793
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54645 * 0.38210224
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16394 * 0.51288437
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79162 * 0.90004183
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40973 * 0.84195072
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91397 * 0.75814349
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 37560 * 0.69058430
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73166 * 0.50394700
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22356 * 0.04259277
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 99282 * 0.61926612
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29343 * 0.55647734
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 85195 * 0.26912068
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3047 * 0.77046551
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63010 * 0.22581634
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 7300 * 0.23714790
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10345 * 0.34374596
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85898 * 0.71455056
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9036 * 0.11097299
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56793 * 0.00749834
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 6981 * 0.55228193
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48507 * 0.88439276
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54512 * 0.38647246
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 94269 * 0.75287130
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27352 * 0.50968415
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 91784 * 0.67057946
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 86820 * 0.87624482
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'vxzsusji').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0026():
    """Extended test 26 for billing."""
    x_0 = 65348 * 0.33396796
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33011 * 0.51663786
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17403 * 0.35505324
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21916 * 0.77905430
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90469 * 0.37912000
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64509 * 0.69641016
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7648 * 0.99002969
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19044 * 0.67974709
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48991 * 0.73159443
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10477 * 0.53645720
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53749 * 0.93327425
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42438 * 0.00976319
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77554 * 0.18356140
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91830 * 0.35380663
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75717 * 0.49452972
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56004 * 0.63390872
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96656 * 0.11785416
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44577 * 0.31049231
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89226 * 0.87761060
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54344 * 0.77055779
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38415 * 0.59861894
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52055 * 0.37428852
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69772 * 0.21744864
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82518 * 0.24138785
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46768 * 0.75146582
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68052 * 0.31262559
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50871 * 0.74982385
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63967 * 0.22776715
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69835 * 0.44539706
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60257 * 0.75401374
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17538 * 0.01175515
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91669 * 0.10083448
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96171 * 0.02325479
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3711 * 0.95360335
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11851 * 0.65992543
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10577 * 0.23128343
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72736 * 0.78375989
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26725 * 0.77751764
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93045 * 0.85305675
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88996 * 0.75604991
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42125 * 0.27004463
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43298 * 0.35848163
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 89217 * 0.54106646
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 34071 * 0.65803920
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 24077 * 0.83250181
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'rlcbtrnd').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0027():
    """Extended test 27 for billing."""
    x_0 = 6691 * 0.66637273
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62473 * 0.01921106
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88159 * 0.88652582
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59569 * 0.27672698
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35399 * 0.86062768
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14587 * 0.21347561
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17640 * 0.64265639
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8411 * 0.62981361
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8748 * 0.08364021
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88177 * 0.16459951
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9099 * 0.07303134
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96134 * 0.70771898
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13656 * 0.98294985
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39078 * 0.55783964
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28968 * 0.57475556
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20869 * 0.54030856
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92762 * 0.65627022
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29195 * 0.75056801
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33011 * 0.47225843
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36512 * 0.08901601
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87373 * 0.16420249
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22495 * 0.71394662
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34269 * 0.53414681
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60889 * 0.45085926
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69634 * 0.12299857
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49636 * 0.48585522
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71831 * 0.71223595
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47305 * 0.90243733
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99693 * 0.21334337
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92895 * 0.90986819
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34910 * 0.10142120
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28854 * 0.05393368
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36788 * 0.81757982
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82554 * 0.33871397
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10956 * 0.98654992
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 84600 * 0.80217319
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2535 * 0.07026426
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 14743 * 0.75089743
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82172 * 0.84170706
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99390 * 0.34169582
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20483 * 0.82953274
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 925 * 0.92491139
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 53454 * 0.84622777
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 82452 * 0.01151938
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 43530 * 0.06688102
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 74094 * 0.34434156
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'uirkatdo').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0028():
    """Extended test 28 for billing."""
    x_0 = 82905 * 0.49813164
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71469 * 0.97555797
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68482 * 0.33609995
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89367 * 0.96655323
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21939 * 0.35271936
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8543 * 0.32737141
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61784 * 0.18471783
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12017 * 0.24629264
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73542 * 0.82747233
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58166 * 0.93876930
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9302 * 0.65902421
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40438 * 0.22387676
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86292 * 0.34242113
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31012 * 0.06213485
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87310 * 0.46128849
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26942 * 0.43121863
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20072 * 0.66263189
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43062 * 0.94944194
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75565 * 0.21960678
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32544 * 0.77818014
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75843 * 0.71289837
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39969 * 0.09057426
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28245 * 0.59622478
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39405 * 0.62138577
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35646 * 0.21355843
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'cfkkgwfz').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0029():
    """Extended test 29 for billing."""
    x_0 = 881 * 0.03433232
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72412 * 0.60698633
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67717 * 0.94255916
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41476 * 0.28608920
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35442 * 0.48914226
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96369 * 0.90206172
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24824 * 0.15670092
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16227 * 0.41770893
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28141 * 0.13609317
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31496 * 0.69319236
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9321 * 0.05254698
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37268 * 0.59799798
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68285 * 0.80193328
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23824 * 0.34125613
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44241 * 0.39423479
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65430 * 0.66591292
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 65863 * 0.26655086
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79823 * 0.52028616
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32149 * 0.59167363
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58973 * 0.45917064
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92248 * 0.60328429
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81179 * 0.15502112
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54512 * 0.32554104
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10623 * 0.54124957
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97623 * 0.54993006
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'nplaonwy').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0030():
    """Extended test 30 for billing."""
    x_0 = 49331 * 0.91698823
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88045 * 0.31623265
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9646 * 0.64313068
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19240 * 0.31484236
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66839 * 0.08387100
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88990 * 0.68108830
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29938 * 0.64879318
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49872 * 0.30844640
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99141 * 0.28500458
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73298 * 0.87985391
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71659 * 0.11540086
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16416 * 0.71796577
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59508 * 0.11216828
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 336 * 0.73255839
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42968 * 0.70038212
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24687 * 0.09930259
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23011 * 0.56625099
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83735 * 0.91816552
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85549 * 0.68281040
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63540 * 0.48892756
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5135 * 0.31553541
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2821 * 0.02677415
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67250 * 0.52949462
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70020 * 0.39601629
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35070 * 0.71477532
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48710 * 0.36345782
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82458 * 0.48638461
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'tkkfcgwp').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0031():
    """Extended test 31 for billing."""
    x_0 = 93625 * 0.23354379
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66600 * 0.15302896
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49141 * 0.54484575
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58779 * 0.00600239
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 79552 * 0.19453050
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45158 * 0.35031017
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82603 * 0.53389807
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46626 * 0.03393106
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85745 * 0.96592356
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6479 * 0.84537421
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11150 * 0.65571136
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86335 * 0.78192853
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51091 * 0.22654116
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50625 * 0.37477151
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43253 * 0.51718276
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34608 * 0.83003871
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92192 * 0.40180562
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27820 * 0.47554256
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50683 * 0.38498905
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87341 * 0.15475125
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40818 * 0.76842689
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'iipgwbku').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0032():
    """Extended test 32 for billing."""
    x_0 = 2187 * 0.80160380
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59272 * 0.03427942
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75110 * 0.94563819
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51296 * 0.54466855
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75126 * 0.56108040
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85426 * 0.52716184
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65660 * 0.03185624
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97910 * 0.19973189
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89329 * 0.33016969
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56128 * 0.22544535
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 935 * 0.68561829
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35266 * 0.44096550
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70118 * 0.64277737
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68479 * 0.74457844
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47268 * 0.45882844
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81069 * 0.99782956
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 132 * 0.12891460
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49795 * 0.52479962
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19788 * 0.46399104
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12187 * 0.09579041
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59075 * 0.40925590
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24098 * 0.54118705
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87803 * 0.00936044
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54183 * 0.98623988
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69709 * 0.10207785
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74263 * 0.40554364
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92602 * 0.58265637
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98984 * 0.97192471
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80321 * 0.67822531
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'rhlmufxl').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0033():
    """Extended test 33 for billing."""
    x_0 = 22209 * 0.47360215
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85443 * 0.17675501
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9070 * 0.84377619
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29959 * 0.78704122
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88621 * 0.61610829
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69891 * 0.97280827
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85522 * 0.66925739
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49062 * 0.93853557
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 257 * 0.36312644
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28468 * 0.32593891
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39558 * 0.91559874
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95041 * 0.86889085
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6424 * 0.48471157
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34455 * 0.17336008
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48167 * 0.50734042
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86182 * 0.37948079
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43861 * 0.14120213
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 799 * 0.69793566
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99902 * 0.18965903
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24577 * 0.13889381
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25066 * 0.49982137
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81988 * 0.21786055
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'baanfufm').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0034():
    """Extended test 34 for billing."""
    x_0 = 47145 * 0.29735993
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83904 * 0.21130019
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72001 * 0.18746915
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59366 * 0.45959113
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67394 * 0.09248908
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74411 * 0.99957497
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 96472 * 0.88843638
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16689 * 0.94370710
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18207 * 0.60357771
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52490 * 0.58549017
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44357 * 0.07827097
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42179 * 0.01138601
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91606 * 0.13490573
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49604 * 0.11981247
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93900 * 0.47441375
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31906 * 0.77654729
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4098 * 0.09148569
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25916 * 0.83040809
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90801 * 0.50563396
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41115 * 0.92945020
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13496 * 0.46860130
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45835 * 0.07972416
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'vixhrqtd').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0035():
    """Extended test 35 for billing."""
    x_0 = 9716 * 0.18978436
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95716 * 0.46618161
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19324 * 0.49996479
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64865 * 0.03551914
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32753 * 0.94686339
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12634 * 0.27642111
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36162 * 0.15056793
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39790 * 0.79475520
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87833 * 0.73959989
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48857 * 0.77178543
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51500 * 0.98641662
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51233 * 0.09008112
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54210 * 0.90387883
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92818 * 0.54792146
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76940 * 0.49677259
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3929 * 0.40048304
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 96101 * 0.46015785
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22731 * 0.35777813
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42469 * 0.07191123
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68298 * 0.39635969
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 284 * 0.70697573
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62892 * 0.56076199
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14314 * 0.75572462
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95375 * 0.72342924
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71578 * 0.25749564
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56349 * 0.11125800
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49422 * 0.12378161
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13646 * 0.72222393
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79389 * 0.44830922
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91508 * 0.28706988
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43035 * 0.10786586
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2295 * 0.70067194
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70660 * 0.23036287
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46240 * 0.49032042
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81808 * 0.94666807
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 89370 * 0.70600310
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52126 * 0.58243605
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92251 * 0.89209793
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'ltqnlwnk').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0036():
    """Extended test 36 for billing."""
    x_0 = 19859 * 0.16583322
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61049 * 0.75368889
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13066 * 0.87907566
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82010 * 0.73840912
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58405 * 0.64555223
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30135 * 0.21418164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27584 * 0.52921715
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 69143 * 0.66944017
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90161 * 0.08920849
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43893 * 0.19774842
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20611 * 0.37450270
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33199 * 0.72315993
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85055 * 0.64827117
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1400 * 0.17641956
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51161 * 0.62361251
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28631 * 0.20449085
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23580 * 0.37080895
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89777 * 0.28089323
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58982 * 0.77361354
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13767 * 0.59143000
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38483 * 0.52226702
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73932 * 0.12497118
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1952 * 0.00247411
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92991 * 0.47564221
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75069 * 0.13632423
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91707 * 0.30071386
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25903 * 0.16159099
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82241 * 0.46395224
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81137 * 0.87070930
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11048 * 0.51593963
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46585 * 0.48131905
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44823 * 0.84536611
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45619 * 0.60383686
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65602 * 0.26235281
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59515 * 0.14375031
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48937 * 0.79670469
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35993 * 0.27681603
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4168 * 0.05539351
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79502 * 0.59819097
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94311 * 0.92128883
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32095 * 0.56193594
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 44401 * 0.49882679
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'jijtowmf').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0037():
    """Extended test 37 for billing."""
    x_0 = 23325 * 0.74045789
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5368 * 0.06527775
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35917 * 0.90452755
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67943 * 0.49870868
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59824 * 0.60993850
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83529 * 0.97571523
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39873 * 0.33479892
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67155 * 0.55635507
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77602 * 0.77925045
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50293 * 0.87420631
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66249 * 0.26509866
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6068 * 0.53181810
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26626 * 0.63104615
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65245 * 0.42813669
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 895 * 0.95772395
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20818 * 0.92674658
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28364 * 0.37515446
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29104 * 0.77655889
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16061 * 0.10989969
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16204 * 0.95418525
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97579 * 0.62092294
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92940 * 0.96342467
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31341 * 0.24582211
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59682 * 0.96165131
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17032 * 0.87343121
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72454 * 0.41960374
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29598 * 0.35078135
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'uickaykx').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0038():
    """Extended test 38 for billing."""
    x_0 = 99685 * 0.34285456
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54407 * 0.32088679
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51138 * 0.13397512
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65429 * 0.88538276
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89044 * 0.60121349
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 877 * 0.13585549
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68270 * 0.98833283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86996 * 0.81866626
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85001 * 0.71848864
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52378 * 0.37843413
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12652 * 0.73052173
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52706 * 0.57659645
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46 * 0.35742927
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77799 * 0.77966005
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61243 * 0.99735840
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84686 * 0.82202457
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5179 * 0.31864292
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42054 * 0.92036004
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93925 * 0.48016885
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87195 * 0.18302704
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22459 * 0.55912869
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25758 * 0.23472667
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42693 * 0.37327265
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36445 * 0.60950836
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93907 * 0.98289486
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2896 * 0.40840745
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29874 * 0.54961406
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95444 * 0.18639389
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14833 * 0.39899353
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72959 * 0.83170249
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61752 * 0.13996833
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46828 * 0.83153150
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69143 * 0.78137764
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47382 * 0.67596294
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88497 * 0.90471006
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82283 * 0.15575336
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31699 * 0.48383786
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46110 * 0.47691118
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 68067 * 0.89764484
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99504 * 0.90347881
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 56002 * 0.44283759
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 68778 * 0.25785354
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41398 * 0.67848216
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 43721 * 0.76862474
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 86426 * 0.02181885
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 42535 * 0.28382889
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 81141 * 0.14495514
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 71745 * 0.41358151
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'wnkxsmqk').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0039():
    """Extended test 39 for billing."""
    x_0 = 54867 * 0.41588291
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46628 * 0.31567899
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71519 * 0.19189639
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93071 * 0.31253099
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5089 * 0.46431020
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17317 * 0.97840997
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4844 * 0.91254219
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31700 * 0.45789286
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35203 * 0.30412211
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15426 * 0.26841434
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83152 * 0.99097493
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16160 * 0.58101202
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54979 * 0.56970739
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10193 * 0.54685601
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95785 * 0.73060802
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91155 * 0.46372825
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15215 * 0.82651973
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73334 * 0.75159495
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79965 * 0.98681497
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82318 * 0.49974930
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87044 * 0.67138908
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26932 * 0.00170847
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93434 * 0.88577057
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57252 * 0.60439717
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7505 * 0.05944334
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14273 * 0.68563660
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79842 * 0.12358233
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13124 * 0.02699901
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79106 * 0.14674426
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74596 * 0.17305291
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4696 * 0.89686228
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72268 * 0.57153465
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26532 * 0.23614388
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45732 * 0.21310265
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39594 * 0.12205035
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56234 * 0.09338095
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84644 * 0.25326628
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 13156 * 0.16803873
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 98507 * 0.98547480
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84909 * 0.88819246
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62357 * 0.15566445
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58943 * 0.53660977
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 56944 * 0.37122452
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 64986 * 0.74222635
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 69522 * 0.65844977
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 7184 * 0.09311450
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 20025 * 0.23396034
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 96543 * 0.43259036
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 6674 * 0.81917676
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'xrfsohmw').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0040():
    """Extended test 40 for billing."""
    x_0 = 97338 * 0.16530117
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66767 * 0.60556973
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33385 * 0.36824329
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57291 * 0.15529569
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57453 * 0.30596171
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43488 * 0.77078676
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44675 * 0.42456626
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13115 * 0.34289068
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53148 * 0.36399055
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28134 * 0.60385720
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51114 * 0.46059544
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93269 * 0.23226491
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13040 * 0.42949281
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62572 * 0.35359740
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32409 * 0.95757482
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10697 * 0.78476024
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32140 * 0.90224119
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72710 * 0.75686344
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21122 * 0.91861793
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92050 * 0.63014444
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75006 * 0.97987218
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17495 * 0.76618613
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63540 * 0.04731550
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'eeatbxnk').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0041():
    """Extended test 41 for billing."""
    x_0 = 52548 * 0.52809919
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87901 * 0.88705416
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80852 * 0.50786933
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52672 * 0.86894538
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44551 * 0.52147806
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41563 * 0.64240476
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64918 * 0.18627560
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65084 * 0.41940981
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45573 * 0.11043500
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3981 * 0.33558233
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91593 * 0.12562556
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37722 * 0.91869346
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 26548 * 0.01920685
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1711 * 0.31362701
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45309 * 0.16361030
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60069 * 0.32717843
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88759 * 0.86416629
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5202 * 0.14260693
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18999 * 0.48091631
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98624 * 0.51186624
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31264 * 0.32557265
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33480 * 0.32458321
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36538 * 0.42018192
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12658 * 0.26563726
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10043 * 0.80474600
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85259 * 0.11442934
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17121 * 0.91947108
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98305 * 0.04138178
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70689 * 0.76580458
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79401 * 0.63900422
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34331 * 0.53519888
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59043 * 0.87291257
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16595 * 0.01477873
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28647 * 0.14415015
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19483 * 0.45744488
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37389 * 0.87114745
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42566 * 0.59461382
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26013 * 0.12571194
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57784 * 0.08479222
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 69556 * 0.95551376
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 48762 * 0.62564553
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 41913 * 0.85144426
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'jwcdvxci').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0042():
    """Extended test 42 for billing."""
    x_0 = 19515 * 0.61817081
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11868 * 0.30012262
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93947 * 0.62763594
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8399 * 0.73154913
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95356 * 0.30858067
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60006 * 0.07487042
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79495 * 0.09963602
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53403 * 0.26881505
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90077 * 0.72928119
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26285 * 0.52709004
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79614 * 0.02516297
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84332 * 0.47931008
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93990 * 0.62177783
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81345 * 0.66411905
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64668 * 0.94471712
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22040 * 0.77638474
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94282 * 0.72390129
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96455 * 0.60130664
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19753 * 0.34007479
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8529 * 0.58143051
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7519 * 0.11693614
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90138 * 0.18450402
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56342 * 0.15077285
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54564 * 0.98266500
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79663 * 0.28015389
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 69128 * 0.91410142
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89622 * 0.47030180
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37159 * 0.57542986
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63611 * 0.29481848
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58411 * 0.16927306
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20515 * 0.69000649
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91928 * 0.86507617
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33295 * 0.70105085
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48659 * 0.04014303
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30174 * 0.65236320
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 75266 * 0.63152095
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 38457 * 0.65807009
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74293 * 0.68904239
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96004 * 0.02543059
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43258 * 0.12743741
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 83161 * 0.45872900
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 93779 * 0.27276066
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81517 * 0.92242741
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39871 * 0.12187982
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 38432 * 0.67409695
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'tjgwpkde').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0043():
    """Extended test 43 for billing."""
    x_0 = 7304 * 0.35466000
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66503 * 0.99610424
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44108 * 0.02081515
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27428 * 0.56695510
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9152 * 0.88320775
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88494 * 0.22557492
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13343 * 0.51690865
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36588 * 0.50765999
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81759 * 0.32979779
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34824 * 0.66501375
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25502 * 0.68496072
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27202 * 0.03496399
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68615 * 0.79089267
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11184 * 0.56751556
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17336 * 0.42281087
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85310 * 0.13722253
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42604 * 0.17591462
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71732 * 0.08685390
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68470 * 0.60555783
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35934 * 0.51150330
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19038 * 0.74882729
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73407 * 0.77046680
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54628 * 0.50570199
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 95494 * 0.53054667
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29764 * 0.47251835
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19474 * 0.00751548
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96829 * 0.80719281
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87692 * 0.06786075
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88625 * 0.54088971
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96284 * 0.38909107
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 66205 * 0.15698423
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'yvejxsoj').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0044():
    """Extended test 44 for billing."""
    x_0 = 30521 * 0.45380979
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6740 * 0.96122692
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10869 * 0.52077076
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87644 * 0.27291903
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53291 * 0.90690243
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55322 * 0.69371007
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62604 * 0.00394705
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61536 * 0.65898031
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6082 * 0.26620431
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31138 * 0.12609897
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57463 * 0.34406468
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78341 * 0.63409456
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55795 * 0.99959362
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99536 * 0.27143807
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51774 * 0.01412263
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4901 * 0.17846700
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22580 * 0.45969223
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38517 * 0.88918783
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92880 * 0.96867344
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59547 * 0.05104287
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81570 * 0.73400447
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38206 * 0.95499900
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21065 * 0.01072182
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23946 * 0.88476459
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91474 * 0.28523756
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51881 * 0.53891708
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36570 * 0.12032032
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56817 * 0.01836221
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26722 * 0.55559084
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67241 * 0.11111948
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47084 * 0.63148594
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78062 * 0.33965094
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21952 * 0.86997531
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92653 * 0.67546929
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12391 * 0.85792229
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65848 * 0.93847011
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19804 * 0.21292403
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 35020 * 0.33940036
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 78088 * 0.24266720
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 65905 * 0.87491309
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 3496 * 0.10670393
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 32871 * 0.47001581
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71726 * 0.23009788
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'umnpiodc').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0045():
    """Extended test 45 for billing."""
    x_0 = 86330 * 0.82996774
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55446 * 0.58919013
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 798 * 0.24644636
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65683 * 0.05897682
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3735 * 0.75378318
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80153 * 0.63339560
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56209 * 0.58014055
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29526 * 0.28503909
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54236 * 0.15691368
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96073 * 0.42146993
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53012 * 0.44946209
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98800 * 0.33894504
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9421 * 0.91663564
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91815 * 0.75278942
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98731 * 0.81631386
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75488 * 0.40566754
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74917 * 0.97527688
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23226 * 0.25083544
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42909 * 0.37508011
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6275 * 0.22296750
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55716 * 0.93411746
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'htidixce').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0046():
    """Extended test 46 for billing."""
    x_0 = 38175 * 0.51222887
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56836 * 0.32019423
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 711 * 0.78684881
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41075 * 0.05024610
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95652 * 0.86505315
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96160 * 0.41375176
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91435 * 0.16962071
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49292 * 0.79440819
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23748 * 0.67205977
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70288 * 0.97329623
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35593 * 0.23265556
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49553 * 0.40982956
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80260 * 0.33545178
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23609 * 0.94693181
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70755 * 0.69564757
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88114 * 0.45192656
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62204 * 0.45536280
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 208 * 0.69311330
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38065 * 0.40697407
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52505 * 0.62080332
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5796 * 0.70095409
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92394 * 0.00962064
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98194 * 0.42130392
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70395 * 0.29415887
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25674 * 0.33352237
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62978 * 0.36695439
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85854 * 0.07316201
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66422 * 0.81017585
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40278 * 0.47798559
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 160 * 0.89480742
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57907 * 0.13243474
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92131 * 0.92521072
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98215 * 0.86900309
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48398 * 0.15486465
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54445 * 0.24486273
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4968 * 0.89501240
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12498 * 0.78652011
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 89292 * 0.78935271
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17794 * 0.29940609
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 85281 * 0.58068102
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 57884 * 0.38594853
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97483 * 0.01047344
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 7538 * 0.57180772
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 26472 * 0.90038069
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 1120 * 0.36801587
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4323 * 0.03066092
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 18692 * 0.40712251
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'vnahcnmp').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0047():
    """Extended test 47 for billing."""
    x_0 = 61174 * 0.03100092
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10205 * 0.33529269
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76053 * 0.78758144
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97651 * 0.82492134
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63347 * 0.88484501
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17112 * 0.00974723
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4310 * 0.52954032
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70580 * 0.58170100
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99457 * 0.92520084
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20487 * 0.06367687
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41760 * 0.22646706
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10524 * 0.63452104
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75823 * 0.95985030
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31094 * 0.87400882
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62527 * 0.23374300
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17959 * 0.02643264
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4998 * 0.16679029
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20437 * 0.43841415
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48499 * 0.81037885
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32874 * 0.22965352
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12028 * 0.28006689
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83334 * 0.87748444
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32653 * 0.44259785
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57839 * 0.72477536
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80602 * 0.21285998
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57586 * 0.78247823
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57711 * 0.78172103
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9674 * 0.81909811
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41740 * 0.48247033
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'rglopqbe').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0048():
    """Extended test 48 for billing."""
    x_0 = 8953 * 0.80000252
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56337 * 0.12539472
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96363 * 0.12535311
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31588 * 0.15898052
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30866 * 0.70285883
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42588 * 0.97982630
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52570 * 0.28117169
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52049 * 0.16236704
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42648 * 0.55953822
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8219 * 0.06431776
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86480 * 0.35533466
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10593 * 0.55751184
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62155 * 0.26330485
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15317 * 0.36038785
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66177 * 0.00070482
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96008 * 0.44833756
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72949 * 0.84437905
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 604 * 0.04604716
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81796 * 0.33448382
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27321 * 0.34387224
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30815 * 0.30798148
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46316 * 0.69537352
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70152 * 0.31351170
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59538 * 0.08329364
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43477 * 0.31014387
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77470 * 0.01294792
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49606 * 0.01464597
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 93601 * 0.71919762
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17437 * 0.37948375
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96819 * 0.32584665
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87140 * 0.10222597
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50971 * 0.28122567
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 87746 * 0.10842838
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93659 * 0.98731547
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15121 * 0.85007853
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88979 * 0.63396713
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7037 * 0.66405450
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69302 * 0.64135171
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13649 * 0.79593199
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 90553 * 0.90352995
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37951 * 0.62495500
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97402 * 0.77113174
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 61624 * 0.05790429
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 59220 * 0.08163272
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'xotpskba').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0049():
    """Extended test 49 for billing."""
    x_0 = 63156 * 0.57515732
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8639 * 0.38189044
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38081 * 0.30122034
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94671 * 0.50212186
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36127 * 0.55464685
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46666 * 0.98436280
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85521 * 0.83893649
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31082 * 0.61790001
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5088 * 0.56502410
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83216 * 0.42380447
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58272 * 0.36629145
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47914 * 0.75513274
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89421 * 0.81909655
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60994 * 0.90504859
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62961 * 0.59133574
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78093 * 0.09402563
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29674 * 0.58084287
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75640 * 0.08952937
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17194 * 0.04787591
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84738 * 0.30437671
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'vrntumpr').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0050():
    """Extended test 50 for billing."""
    x_0 = 84291 * 0.41391017
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42936 * 0.07172293
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20249 * 0.04404784
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86353 * 0.77708239
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75941 * 0.38058147
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51478 * 0.24528385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42190 * 0.93033213
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84996 * 0.59953142
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32526 * 0.67294741
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20610 * 0.78594466
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66690 * 0.66579275
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21999 * 0.26920636
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97909 * 0.80190017
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26566 * 0.74476924
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81887 * 0.73483148
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89377 * 0.47946804
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48014 * 0.95309391
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56543 * 0.18858112
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82591 * 0.68329284
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 34692 * 0.58650849
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57575 * 0.15393794
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51441 * 0.84417378
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90669 * 0.70892025
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68286 * 0.47347101
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35619 * 0.45514996
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36380 * 0.88562652
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14922 * 0.74257860
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 73785 * 0.10902399
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65718 * 0.09996507
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38206 * 0.48095538
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30486 * 0.97511605
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28101 * 0.97903476
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60972 * 0.32826234
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20783 * 0.59045500
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26948 * 0.33255728
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21746 * 0.91291540
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96616 * 0.15015431
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17924 * 0.04024657
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10274 * 0.09689728
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 45480 * 0.47558418
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8795 * 0.74010451
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26451 * 0.38724398
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96144 * 0.01088986
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27709 * 0.14044079
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23813 * 0.20006201
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 5556 * 0.59446234
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 25258 * 0.43329165
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 20024 * 0.47891794
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'jfnqeckd').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0051():
    """Extended test 51 for billing."""
    x_0 = 37832 * 0.62427524
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91686 * 0.40243422
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55249 * 0.13065451
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 57662 * 0.26822216
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86970 * 0.00769592
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93306 * 0.80619571
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36705 * 0.03983060
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6916 * 0.76901522
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43394 * 0.72976836
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28392 * 0.66623324
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90638 * 0.68574583
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96004 * 0.67036301
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38692 * 0.35930407
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86516 * 0.25522177
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30790 * 0.98852515
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 465 * 0.51446020
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87682 * 0.22116046
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81791 * 0.34880637
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73036 * 0.04709420
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 755 * 0.39126986
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99095 * 0.94766727
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72484 * 0.83470801
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67139 * 0.45904728
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39477 * 0.47825349
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79918 * 0.36835199
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21705 * 0.41341671
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'vcfjrdhi').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0052():
    """Extended test 52 for billing."""
    x_0 = 41283 * 0.64029998
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72661 * 0.28495319
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84874 * 0.64203489
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 91631 * 0.82574371
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49859 * 0.17646809
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51065 * 0.46795161
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36118 * 0.23247115
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44517 * 0.16819813
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68550 * 0.44493078
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23161 * 0.53108445
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51572 * 0.01605534
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59630 * 0.77439619
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68112 * 0.85414672
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79855 * 0.36967489
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11022 * 0.35545550
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30274 * 0.40997422
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48898 * 0.98447317
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62934 * 0.17655442
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94916 * 0.76887147
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48384 * 0.38069758
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3714 * 0.77654688
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52177 * 0.97487001
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47588 * 0.58247846
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92351 * 0.20743586
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73138 * 0.80748018
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68950 * 0.84246575
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21732 * 0.16070390
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12810 * 0.78157052
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6040 * 0.75069561
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'gflrfygd').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0053():
    """Extended test 53 for billing."""
    x_0 = 46915 * 0.19136575
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73084 * 0.73196547
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21110 * 0.17689375
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76050 * 0.58134365
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82233 * 0.87801383
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65420 * 0.51169974
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83632 * 0.62789509
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16965 * 0.14041627
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42921 * 0.97749171
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24217 * 0.66567326
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40666 * 0.30920136
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59198 * 0.74766334
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66435 * 0.00526192
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 423 * 0.52343319
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39800 * 0.02270286
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96744 * 0.50469259
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45126 * 0.47658451
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17768 * 0.64342200
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76399 * 0.36390860
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 95692 * 0.30019201
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61005 * 0.82756846
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93180 * 0.97940018
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52390 * 0.58888938
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29637 * 0.17195998
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29267 * 0.18498038
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82560 * 0.62965251
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69858 * 0.41100055
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8368 * 0.16862795
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29660 * 0.26382954
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36588 * 0.31295018
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7629 * 0.16450330
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19785 * 0.93082523
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 75754 * 0.03979374
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83564 * 0.26106155
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58517 * 0.87151720
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36745 * 0.66383421
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69405 * 0.56883182
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70485 * 0.68765241
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19461 * 0.73692630
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 48122 * 0.18786276
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23825 * 0.15419170
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4629 * 0.76601999
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 74953 * 0.37037741
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 68549 * 0.24215363
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4956 * 0.69628385
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 70449 * 0.29868042
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 51906 * 0.71499080
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 79906 * 0.93787177
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 4070 * 0.09344081
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'jobkguca').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0054():
    """Extended test 54 for billing."""
    x_0 = 60326 * 0.41326473
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18356 * 0.94803663
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12563 * 0.90185205
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32687 * 0.58692715
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56884 * 0.46699351
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11002 * 0.01360483
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68717 * 0.85370197
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 26786 * 0.89699709
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25607 * 0.95320216
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11497 * 0.91958467
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61648 * 0.29468231
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30164 * 0.81530633
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83348 * 0.58291325
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40588 * 0.40057089
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99412 * 0.54090056
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20135 * 0.50951624
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18960 * 0.87823711
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42666 * 0.55007559
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 977 * 0.99350690
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63816 * 0.67706794
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27201 * 0.81999808
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48994 * 0.52227725
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42307 * 0.92334545
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60584 * 0.40936500
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29733 * 0.51101767
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13317 * 0.67457495
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74459 * 0.11051623
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72825 * 0.00074608
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79320 * 0.36634035
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58772 * 0.32165414
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85040 * 0.89024107
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7868 * 0.95313579
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25273 * 0.63563939
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43179 * 0.24958436
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65030 * 0.20981210
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50315 * 0.03365107
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59893 * 0.76315454
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62069 * 0.33521929
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 75182 * 0.86177718
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46327 * 0.28252691
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35575 * 0.47687751
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42587 * 0.40407124
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'sgjuhsjq').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0055():
    """Extended test 55 for billing."""
    x_0 = 85591 * 0.78863725
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46365 * 0.73483788
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75409 * 0.07850035
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2157 * 0.69742976
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22772 * 0.88591930
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64694 * 0.70132994
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52242 * 0.51656458
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 57182 * 0.06752228
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96503 * 0.89100548
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53986 * 0.95149284
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65518 * 0.61557889
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40016 * 0.88183150
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12759 * 0.04427045
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42888 * 0.69867579
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75869 * 0.72925901
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45059 * 0.36452377
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83017 * 0.32516156
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93411 * 0.50439852
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90431 * 0.82208616
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23893 * 0.00674740
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99410 * 0.36457525
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'duchwwov').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0056():
    """Extended test 56 for billing."""
    x_0 = 41050 * 0.54283804
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69148 * 0.47279236
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87320 * 0.51505278
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68444 * 0.79558636
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91952 * 0.32656544
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93486 * 0.35864513
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26905 * 0.84586111
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19859 * 0.37998644
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33835 * 0.44146030
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71710 * 0.13637761
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60753 * 0.01436129
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43491 * 0.39487902
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89674 * 0.91827070
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88091 * 0.87189254
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45510 * 0.21801619
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33726 * 0.81049911
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30303 * 0.08019734
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 375 * 0.64175293
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2219 * 0.25815266
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47307 * 0.25591485
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2744 * 0.25969529
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49289 * 0.77543037
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94922 * 0.05193828
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77885 * 0.40476675
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 58815 * 0.21838253
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97951 * 0.91283672
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21787 * 0.59755906
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42284 * 0.11191137
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77403 * 0.96370414
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87610 * 0.85364113
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 90628 * 0.99954446
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12229 * 0.94340931
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55614 * 0.47455288
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64605 * 0.57553624
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'urbaajau').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0057():
    """Extended test 57 for billing."""
    x_0 = 40645 * 0.17578640
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10976 * 0.81531977
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54287 * 0.82056693
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52869 * 0.68062281
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59205 * 0.96788697
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91331 * 0.64453723
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83969 * 0.99060293
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75038 * 0.49924247
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32542 * 0.11747197
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29477 * 0.57524925
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47971 * 0.22849726
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96109 * 0.50873323
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25507 * 0.97343075
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58135 * 0.47035064
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10264 * 0.67958613
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59958 * 0.19552659
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26797 * 0.16494632
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31340 * 0.50591588
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91288 * 0.03843110
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5080 * 0.63208915
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68376 * 0.59119838
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35687 * 0.43852703
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76118 * 0.71630570
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67953 * 0.02500717
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73806 * 0.76958724
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75343 * 0.03188344
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52893 * 0.54719302
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57230 * 0.78527797
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34928 * 0.69859790
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94645 * 0.17733596
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16131 * 0.68128436
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'uivtdkik').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0058():
    """Extended test 58 for billing."""
    x_0 = 503 * 0.87363237
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87202 * 0.38081064
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76696 * 0.67495961
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84578 * 0.58776861
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84818 * 0.90650091
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66543 * 0.58853014
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34943 * 0.79316313
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99306 * 0.18950961
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12736 * 0.03495698
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25692 * 0.23636205
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98956 * 0.70524790
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61507 * 0.33212418
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77950 * 0.03532264
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49641 * 0.08284416
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85989 * 0.54858494
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41109 * 0.33645292
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61020 * 0.33801161
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68010 * 0.24958141
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96024 * 0.71073836
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46609 * 0.42778131
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6172 * 0.03647210
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40281 * 0.22103568
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23848 * 0.08362203
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67042 * 0.20342567
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4065 * 0.35455017
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10853 * 0.10036643
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89186 * 0.03849413
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7816 * 0.52433966
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44661 * 0.91233250
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83965 * 0.02099793
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43029 * 0.20759312
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19796 * 0.69698690
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69702 * 0.67062787
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 23341 * 0.45593881
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99350 * 0.15301586
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38187 * 0.77021645
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60792 * 0.50648371
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26561 * 0.99812186
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72340 * 0.70794195
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 58538 * 0.93004706
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20454 * 0.73902147
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 2705 * 0.47988867
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47557 * 0.07286036
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22672 * 0.14460480
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'dlutvaqr').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0059():
    """Extended test 59 for billing."""
    x_0 = 56053 * 0.00294801
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81675 * 0.85589687
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31630 * 0.46541238
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14597 * 0.38063995
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85769 * 0.67666750
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 93804 * 0.35946230
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76315 * 0.77633962
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30391 * 0.27820706
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37633 * 0.71616562
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77980 * 0.03628873
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6935 * 0.59108198
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7666 * 0.52148694
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32444 * 0.81549425
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54368 * 0.57250183
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75002 * 0.42459223
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54104 * 0.34459261
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10179 * 0.75734294
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75612 * 0.43242171
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11997 * 0.78184789
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 69940 * 0.60755191
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7067 * 0.15778424
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94756 * 0.94088309
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16421 * 0.53325962
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15831 * 0.18835564
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 25812 * 0.22489085
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59346 * 0.87306099
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31161 * 0.42528940
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41331 * 0.28616026
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13002 * 0.88489300
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20377 * 0.06077687
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63210 * 0.79252121
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 113 * 0.14936396
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 6048 * 0.42949930
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58436 * 0.95281698
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 64228 * 0.61819156
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11099 * 0.55553357
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'fnxgyatu').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0060():
    """Extended test 60 for billing."""
    x_0 = 49354 * 0.10472831
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48559 * 0.80853903
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54892 * 0.24438082
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22585 * 0.01562862
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99509 * 0.58486774
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61938 * 0.75933928
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87417 * 0.89690628
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2417 * 0.99806349
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70021 * 0.63852514
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47671 * 0.07661721
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96345 * 0.48866302
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82728 * 0.09921516
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16933 * 0.76148761
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32734 * 0.78341221
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61414 * 0.98436329
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99283 * 0.30162159
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63897 * 0.89769833
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29588 * 0.94463873
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38173 * 0.24628794
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75687 * 0.79246331
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55362 * 0.84831754
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 58032 * 0.98765151
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31796 * 0.79916150
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21092 * 0.51663902
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80703 * 0.84493974
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81594 * 0.97815611
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7062 * 0.96313097
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45847 * 0.79498009
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19878 * 0.55354608
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42076 * 0.20109690
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46892 * 0.17032355
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2195 * 0.34264437
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86531 * 0.37907452
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11850 * 0.73633974
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18218 * 0.78265449
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 44956 * 0.13178392
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 59125 * 0.66016717
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67348 * 0.05200720
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34070 * 0.17892204
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'vgliafba').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0061():
    """Extended test 61 for billing."""
    x_0 = 38298 * 0.26734818
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27449 * 0.96441221
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22934 * 0.43812400
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33493 * 0.17566987
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6824 * 0.63447830
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72021 * 0.90337443
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42954 * 0.97123637
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7689 * 0.31477662
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59139 * 0.05245908
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15214 * 0.45941516
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22031 * 0.83203922
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4555 * 0.29004579
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15832 * 0.36188294
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68297 * 0.50340341
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96419 * 0.99250482
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11578 * 0.08572861
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84286 * 0.33750682
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3518 * 0.61012672
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28407 * 0.68357138
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45642 * 0.22390204
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76026 * 0.47742398
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70787 * 0.04368282
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56150 * 0.64588526
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44428 * 0.45597122
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82560 * 0.98799819
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99695 * 0.51041221
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51909 * 0.08705474
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8204 * 0.61447782
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1724 * 0.75549817
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17757 * 0.22462562
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84270 * 0.15265688
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72385 * 0.63802026
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51748 * 0.47510204
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11275 * 0.19502315
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2858 * 0.79501969
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66634 * 0.71700953
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 18519 * 0.88651384
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 27769 * 0.13663662
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63869 * 0.57890919
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67533 * 0.73799985
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75244 * 0.96247001
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 39144 * 0.56347876
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 91967 * 0.32809991
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 81350 * 0.33985498
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 40546 * 0.73286559
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 64320 * 0.09725455
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 80532 * 0.00504969
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'gtnqdlhq').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0062():
    """Extended test 62 for billing."""
    x_0 = 26739 * 0.66866401
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87534 * 0.16306277
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27176 * 0.01266463
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26938 * 0.95192772
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48142 * 0.18110488
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72082 * 0.89832812
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53648 * 0.51578712
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70910 * 0.16971728
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28038 * 0.89568997
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15437 * 0.53528848
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10149 * 0.49026113
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78641 * 0.18015607
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39811 * 0.11826137
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1469 * 0.53106728
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28658 * 0.94958912
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22243 * 0.04801884
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9006 * 0.04387657
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41022 * 0.74201525
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88369 * 0.00561574
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22449 * 0.78547438
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41394 * 0.98713028
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87915 * 0.38001040
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55649 * 0.41613174
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44355 * 0.66208588
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15961 * 0.30126554
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46396 * 0.48053172
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49159 * 0.75267459
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39628 * 0.68447682
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63006 * 0.03233497
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87339 * 0.00691643
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26684 * 0.01774819
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74300 * 0.63280988
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56059 * 0.35813319
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70196 * 0.78334039
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93334 * 0.10813988
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24056 * 0.01025752
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 97104 * 0.52505625
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 58898 * 0.13883914
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 5780 * 0.38740429
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 60414 * 0.02516547
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 5538 * 0.38496201
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 71184 * 0.97280741
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81555 * 0.53861011
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'kiwejbtv').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0063():
    """Extended test 63 for billing."""
    x_0 = 82692 * 0.41710182
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6983 * 0.70433501
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68512 * 0.21121917
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7220 * 0.64367057
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34469 * 0.17912109
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5614 * 0.10046686
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5969 * 0.21880248
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12080 * 0.53752806
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59582 * 0.79072982
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70832 * 0.07331207
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5056 * 0.68276692
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22919 * 0.17101735
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85146 * 0.40307198
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18700 * 0.52431015
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48438 * 0.45325706
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45991 * 0.41852872
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99878 * 0.77307093
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2005 * 0.18701893
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77832 * 0.82590202
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97542 * 0.70176164
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91311 * 0.76715228
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16050 * 0.55289400
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91088 * 0.32646285
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26422 * 0.94607729
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 52489 * 0.65704427
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97056 * 0.38858029
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75820 * 0.34506611
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9962 * 0.78521618
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47897 * 0.84488925
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19393 * 0.44598810
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15613 * 0.05253590
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2220 * 0.07835946
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18345 * 0.05868236
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 34960 * 0.23561111
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68488 * 0.30148543
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50943 * 0.05866221
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30149 * 0.96130495
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22579 * 0.19101523
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14527 * 0.16424309
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 7166 * 0.67395577
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74178 * 0.27755327
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 1976 * 0.41781929
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'wlajtmsb').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0064():
    """Extended test 64 for billing."""
    x_0 = 22327 * 0.26652268
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25405 * 0.23553982
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12486 * 0.56219418
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51521 * 0.77283020
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48591 * 0.01401234
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83107 * 0.30055385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81717 * 0.38094617
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19825 * 0.47366916
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35926 * 0.81395108
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71448 * 0.91946379
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88356 * 0.69067084
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57852 * 0.31894121
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50850 * 0.01470159
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69299 * 0.54746132
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40655 * 0.96992900
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72777 * 0.14830685
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56331 * 0.38024641
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1373 * 0.12293917
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68538 * 0.17315515
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93133 * 0.22292884
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48877 * 0.57751925
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38672 * 0.63350283
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29050 * 0.31440722
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65919 * 0.82311978
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23039 * 0.77715110
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62930 * 0.34051268
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63564 * 0.08826452
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22023 * 0.87304357
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95919 * 0.72135707
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67167 * 0.76075158
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99741 * 0.96605451
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58920 * 0.87590307
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7795 * 0.20627887
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11594 * 0.83040087
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83463 * 0.76254313
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'dlchhynp').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0065():
    """Extended test 65 for billing."""
    x_0 = 41886 * 0.48927496
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52191 * 0.09590112
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28625 * 0.35884897
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29700 * 0.05667353
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35659 * 0.14203569
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62263 * 0.23510903
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29733 * 0.69301098
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6510 * 0.17728294
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41773 * 0.74230256
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53064 * 0.06133091
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98337 * 0.71518634
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14105 * 0.60278289
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6236 * 0.76372625
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7177 * 0.15039513
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11867 * 0.05199424
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32082 * 0.13279685
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 38798 * 0.86522476
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47806 * 0.91317061
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30770 * 0.67139141
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1598 * 0.29292933
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22137 * 0.86660548
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93035 * 0.91915928
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86068 * 0.01274046
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4941 * 0.46708711
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9383 * 0.31352990
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89770 * 0.21048258
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21623 * 0.87546887
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55357 * 0.19285269
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66964 * 0.62139511
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92248 * 0.87841703
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8121 * 0.33619426
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57823 * 0.93652073
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89585 * 0.46184393
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35581 * 0.55763343
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35112 * 0.99771422
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14012 * 0.04868036
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 95572 * 0.34152012
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 44921 * 0.66449901
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37339 * 0.54894589
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74557 * 0.30114572
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69232 * 0.25998993
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26400 * 0.12921571
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 3845 * 0.86604536
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 31928 * 0.32268303
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 39447 * 0.83166442
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'trsoraey').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0066():
    """Extended test 66 for billing."""
    x_0 = 6730 * 0.74598109
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69818 * 0.73851318
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81542 * 0.23508615
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19986 * 0.78944148
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 44795 * 0.48300327
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48303 * 0.93590077
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94342 * 0.64285482
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90055 * 0.95001697
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25220 * 0.41160671
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22767 * 0.18287943
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47855 * 0.87344486
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5271 * 0.59933106
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69592 * 0.61493877
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58493 * 0.57427196
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20388 * 0.33513650
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75498 * 0.58659990
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34657 * 0.99343041
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39177 * 0.23908857
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44680 * 0.78755036
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29504 * 0.88528811
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43633 * 0.66568855
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62517 * 0.44607357
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63579 * 0.45001233
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29152 * 0.18746654
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59156 * 0.39833478
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95133 * 0.05852436
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40027 * 0.01082595
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84887 * 0.15763282
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68415 * 0.40921950
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44457 * 0.46596678
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59354 * 0.41436087
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58861 * 0.26563203
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96503 * 0.67937698
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45905 * 0.99080508
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68560 * 0.22416078
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38541 * 0.30252604
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 91568 * 0.95485266
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 57174 * 0.21415322
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86857 * 0.09425129
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 47233 * 0.96979570
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 16133 * 0.75730418
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43074 * 0.92931012
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 99818 * 0.07683734
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 80892 * 0.28627816
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61653 * 0.20314655
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 75047 * 0.67381379
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 1285 * 0.82531236
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ptwrpouk').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0067():
    """Extended test 67 for billing."""
    x_0 = 24929 * 0.84193404
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74813 * 0.68015422
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29232 * 0.33257174
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 149 * 0.18935417
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5200 * 0.41124039
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65450 * 0.64678131
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69554 * 0.84706216
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89483 * 0.17497046
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35165 * 0.16286753
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65678 * 0.24184602
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 86374 * 0.35904861
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30819 * 0.56207584
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6543 * 0.26023746
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87356 * 0.91670730
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32889 * 0.65134346
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18903 * 0.51698869
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92008 * 0.61317691
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29718 * 0.85596103
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64353 * 0.02358017
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58492 * 0.42829868
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41329 * 0.66945859
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28859 * 0.82168793
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33523 * 0.65157444
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64702 * 0.17993320
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90779 * 0.90495246
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58177 * 0.56375447
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10169 * 0.07601516
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81738 * 0.28525558
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37876 * 0.64249926
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69584 * 0.02588245
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15054 * 0.89076289
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 8876 * 0.21478946
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 808 * 0.45321880
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38640 * 0.63496847
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31189 * 0.34957716
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63301 * 0.31415636
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 82031 * 0.74258728
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 14252 * 0.72486262
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'fddbanif').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0068():
    """Extended test 68 for billing."""
    x_0 = 84078 * 0.77701008
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28396 * 0.83087056
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93394 * 0.07837094
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5747 * 0.40739118
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18108 * 0.41405265
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52101 * 0.78122244
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44333 * 0.74219640
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8813 * 0.12909403
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69895 * 0.53331191
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32921 * 0.37583771
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17518 * 0.62687528
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81669 * 0.33759362
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85022 * 0.94737582
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95460 * 0.65221017
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72490 * 0.76062019
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53200 * 0.72575316
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46844 * 0.50788401
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50530 * 0.82194341
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55879 * 0.80352638
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64709 * 0.85018623
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17501 * 0.28696351
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42589 * 0.80356949
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91806 * 0.95582731
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76513 * 0.42456326
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59495 * 0.52855420
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92364 * 0.22523542
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54091 * 0.59707409
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90633 * 0.16134576
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31856 * 0.15435585
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 76232 * 0.14912087
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1736 * 0.10575153
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'wqgnvrle').hexdigest()
    assert len(h) == 64

def test_billing_extended_9_0069():
    """Extended test 69 for billing."""
    x_0 = 38508 * 0.93394294
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28306 * 0.45212751
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86191 * 0.18168729
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93739 * 0.12129997
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36337 * 0.93533089
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98057 * 0.36812689
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19129 * 0.48091773
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3058 * 0.90708034
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32931 * 0.43794040
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74150 * 0.74535128
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98500 * 0.88217582
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45777 * 0.87652270
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46648 * 0.01047476
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11113 * 0.83233430
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9879 * 0.05664933
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38809 * 0.18627446
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87522 * 0.99840462
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96797 * 0.41455640
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60124 * 0.51011587
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4684 * 0.91377247
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49657 * 0.47379459
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76481 * 0.34682220
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98939 * 0.39596470
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76278 * 0.16695374
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'zvqhuakw').hexdigest()
    assert len(h) == 64
