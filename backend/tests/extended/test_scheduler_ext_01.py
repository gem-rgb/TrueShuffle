"""Extended tests for scheduler suite 1."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_scheduler_extended_1_0000():
    """Extended test 0 for scheduler."""
    x_0 = 11381 * 0.77092562
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14523 * 0.66070214
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34683 * 0.07044603
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27541 * 0.27549601
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57368 * 0.85193247
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80465 * 0.50173426
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28390 * 0.18205624
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11547 * 0.90036624
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62741 * 0.79442011
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92236 * 0.02241942
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41833 * 0.56469228
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57219 * 0.28673583
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66156 * 0.49287992
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48375 * 0.37669365
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4488 * 0.07071716
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 12088 * 0.63034174
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25143 * 0.38588247
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50598 * 0.36364669
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5954 * 0.12854082
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4052 * 0.83143022
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70439 * 0.24691132
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80495 * 0.66642748
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37259 * 0.36503522
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96770 * 0.56242523
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1660 * 0.24963574
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27588 * 0.78045048
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98834 * 0.30158633
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59725 * 0.32742863
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43637 * 0.05723159
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45487 * 0.08322634
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80822 * 0.61528644
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57800 * 0.11067031
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58155 * 0.25564715
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67169 * 0.51238359
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40086 * 0.33211737
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36093 * 0.37382947
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66409 * 0.02468302
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73276 * 0.42069300
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 1789 * 0.85013997
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 49223 * 0.68627674
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81206 * 0.75790219
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'pwhimulr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0001():
    """Extended test 1 for scheduler."""
    x_0 = 5455 * 0.85390433
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76322 * 0.34767107
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18720 * 0.81741666
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47235 * 0.21194697
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94124 * 0.77415262
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82048 * 0.82590279
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65789 * 0.34532270
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24080 * 0.87151945
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36106 * 0.36486257
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42791 * 0.21237155
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62573 * 0.29591092
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21513 * 0.36004618
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13278 * 0.67350000
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57320 * 0.11224964
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88849 * 0.32781265
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46735 * 0.45668207
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64393 * 0.77208157
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39429 * 0.62052792
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44325 * 0.03357745
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38046 * 0.08764916
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71991 * 0.28308608
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18887 * 0.76420092
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8638 * 0.57991426
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57970 * 0.05238624
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12010 * 0.08708307
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91579 * 0.13747657
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92224 * 0.69348720
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16693 * 0.06355211
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'svvcodbk').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0002():
    """Extended test 2 for scheduler."""
    x_0 = 38052 * 0.76302955
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80900 * 0.68129095
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40783 * 0.60622709
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42217 * 0.44793350
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6731 * 0.11962478
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38192 * 0.98350306
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67889 * 0.29299470
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87417 * 0.17488352
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57942 * 0.11598272
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77764 * 0.59374421
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10127 * 0.44916116
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2561 * 0.41346056
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96183 * 0.62961263
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21990 * 0.00688353
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67926 * 0.64677001
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23178 * 0.43498247
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14952 * 0.49134513
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71051 * 0.25289373
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1371 * 0.61802068
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27201 * 0.25290767
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 22305 * 0.67423165
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60486 * 0.86277393
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11021 * 0.43184851
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66804 * 0.01892813
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 76664 * 0.75225306
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'tgyyclbq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0003():
    """Extended test 3 for scheduler."""
    x_0 = 92889 * 0.12897206
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74871 * 0.20108678
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93488 * 0.64786442
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96134 * 0.85629195
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95018 * 0.02618137
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47451 * 0.19870420
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8351 * 0.85721034
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76903 * 0.28973096
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24847 * 0.19221706
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98885 * 0.92885155
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81931 * 0.74075345
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50437 * 0.57115639
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82341 * 0.26646522
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17196 * 0.15804231
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57937 * 0.86646585
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83602 * 0.81073803
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75520 * 0.18277569
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83271 * 0.37427149
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50511 * 0.95321408
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7928 * 0.56780193
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96516 * 0.70512052
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59155 * 0.64198436
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19778 * 0.42840658
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39492 * 0.86451887
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89770 * 0.87840992
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'zsorikgh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0004():
    """Extended test 4 for scheduler."""
    x_0 = 79179 * 0.83765921
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27578 * 0.82547935
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87736 * 0.51250053
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70740 * 0.66518226
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76865 * 0.05034450
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84698 * 0.72778979
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66858 * 0.52823362
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25854 * 0.64865398
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52578 * 0.25742193
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68247 * 0.93922582
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57952 * 0.32796797
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15125 * 0.99049425
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50680 * 0.38785207
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44173 * 0.21393060
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61862 * 0.23520579
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99481 * 0.34988967
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26953 * 0.41295134
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39166 * 0.51425213
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62226 * 0.44538602
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1713 * 0.41451239
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'cwdrlbvs').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0005():
    """Extended test 5 for scheduler."""
    x_0 = 27917 * 0.20171419
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96826 * 0.65879649
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10854 * 0.77130911
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67767 * 0.41376203
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34093 * 0.08729229
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88618 * 0.14655230
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1628 * 0.33569634
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21567 * 0.32196429
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59619 * 0.30328492
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86587 * 0.41096903
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42274 * 0.89991619
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93079 * 0.84731294
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71816 * 0.92618035
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58943 * 0.23787093
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3368 * 0.06166895
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17047 * 0.65490155
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43022 * 0.02014737
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3834 * 0.08707519
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79972 * 0.62193315
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13022 * 0.62046056
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87327 * 0.14325259
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10022 * 0.39666044
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88072 * 0.93219466
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59396 * 0.91166454
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84592 * 0.79889471
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50845 * 0.28228066
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39924 * 0.21955291
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87656 * 0.01116302
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78467 * 0.53421385
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33188 * 0.58371642
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16327 * 0.40671775
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70743 * 0.35597167
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81093 * 0.71582937
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64496 * 0.41674406
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14485 * 0.22877986
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36521 * 0.02528602
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 57221 * 0.90268691
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'krioxfqd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0006():
    """Extended test 6 for scheduler."""
    x_0 = 12486 * 0.95138419
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41995 * 0.14827754
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22996 * 0.73309482
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50012 * 0.33203923
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 61732 * 0.35280508
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90982 * 0.52008330
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76008 * 0.29016233
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65398 * 0.98504378
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44344 * 0.59140889
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96331 * 0.35990470
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2765 * 0.50643494
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51519 * 0.83851308
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30329 * 0.41976623
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62229 * 0.80387036
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7051 * 0.10295235
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25515 * 0.11536962
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72386 * 0.83842135
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92087 * 0.98778331
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61282 * 0.44770084
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60327 * 0.57981799
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44316 * 0.02257265
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1256 * 0.21274116
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84773 * 0.88198290
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61640 * 0.96139468
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7938 * 0.69391034
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77956 * 0.08555181
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76649 * 0.18243719
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'mifleock').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0007():
    """Extended test 7 for scheduler."""
    x_0 = 68650 * 0.02412138
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67775 * 0.81114690
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25715 * 0.74171672
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21286 * 0.96824140
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59306 * 0.79010777
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47328 * 0.18276253
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45875 * 0.84163577
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71522 * 0.57004939
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84130 * 0.70181446
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59310 * 0.72323504
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21507 * 0.25633186
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56183 * 0.49176077
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8875 * 0.07583288
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55297 * 0.35853210
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83419 * 0.59907559
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54880 * 0.63405388
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28592 * 0.96424952
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43115 * 0.89327501
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82860 * 0.51493805
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74481 * 0.55640062
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41048 * 0.60295164
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50742 * 0.38567491
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65425 * 0.00829765
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6711 * 0.97122790
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36546 * 0.13277792
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52766 * 0.42910383
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68265 * 0.21483743
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23478 * 0.16021443
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85980 * 0.31230406
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12484 * 0.43387548
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92960 * 0.47071386
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26499 * 0.09794750
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86997 * 0.87858260
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17162 * 0.69082730
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90318 * 0.17270763
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79546 * 0.78127257
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83416 * 0.62884162
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26969 * 0.42861585
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12833 * 0.70308208
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43535 * 0.69687072
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21319 * 0.57164402
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96358 * 0.48789058
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'tydarain').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0008():
    """Extended test 8 for scheduler."""
    x_0 = 25401 * 0.27681887
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66806 * 0.27833560
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23654 * 0.41149569
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28576 * 0.10173138
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45991 * 0.86637574
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37815 * 0.57134719
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55986 * 0.83850030
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84382 * 0.81373795
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14963 * 0.36095253
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64623 * 0.98963949
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37225 * 0.18867886
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33287 * 0.15243425
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72132 * 0.86884894
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81622 * 0.66348394
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45005 * 0.20404538
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97185 * 0.63725776
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80072 * 0.29359106
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88734 * 0.90087904
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58271 * 0.63542244
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22445 * 0.84996106
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2832 * 0.99521580
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77485 * 0.20470840
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 46822 * 0.90879510
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12999 * 0.43426344
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17588 * 0.45920874
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97272 * 0.39628635
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53016 * 0.05985976
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49350 * 0.68947554
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93873 * 0.35365686
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70189 * 0.89013352
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63574 * 0.27467380
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83019 * 0.64801622
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78181 * 0.75476359
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'jxwysdky').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0009():
    """Extended test 9 for scheduler."""
    x_0 = 61113 * 0.06504272
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18398 * 0.28617102
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32824 * 0.94295963
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82230 * 0.74169699
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53999 * 0.45550631
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65368 * 0.36028622
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24928 * 0.37809606
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90336 * 0.91131175
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7474 * 0.08452441
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28550 * 0.91149812
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28282 * 0.12477983
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51137 * 0.13494185
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51953 * 0.44110996
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23794 * 0.68273675
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6159 * 0.89774178
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97585 * 0.83057479
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86794 * 0.61455923
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44239 * 0.58650451
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 51041 * 0.34852365
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25766 * 0.56136951
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2961 * 0.81193396
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68460 * 0.31279746
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4869 * 0.02529131
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59696 * 0.23342355
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14420 * 0.12453856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22655 * 0.64124811
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26172 * 0.75407538
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74384 * 0.98174707
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81311 * 0.30015814
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 41587 * 0.14850615
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19592 * 0.94197038
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16410 * 0.70077525
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28963 * 0.72751928
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85232 * 0.02933270
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46700 * 0.05484034
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2755 * 0.07029707
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44204 * 0.84389671
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8034 * 0.86453233
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 36226 * 0.74758214
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 88250 * 0.69066741
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 53257 * 0.73656077
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60292 * 0.69824566
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 35072 * 0.65320432
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 19446 * 0.03829872
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 54397 * 0.90385479
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 39569 * 0.24670508
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 24088 * 0.60345189
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 83949 * 0.43551560
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'axnsyhng').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0010():
    """Extended test 10 for scheduler."""
    x_0 = 6357 * 0.33919845
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71843 * 0.40593754
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3431 * 0.81377660
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29238 * 0.73343329
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35806 * 0.00646119
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94362 * 0.27403523
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48478 * 0.92825869
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18741 * 0.51816000
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96320 * 0.32483592
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6783 * 0.38879963
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41387 * 0.14595432
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44118 * 0.20606752
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31105 * 0.17600584
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10080 * 0.95067963
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29624 * 0.33066157
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88896 * 0.30703029
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72641 * 0.38056581
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11935 * 0.36619989
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96701 * 0.03928435
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6589 * 0.51881511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69576 * 0.97673821
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52732 * 0.58866476
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54000 * 0.52009918
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19584 * 0.36926171
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75395 * 0.11844426
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60616 * 0.31737498
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86960 * 0.78859588
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47843 * 0.79538592
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29578 * 0.52791321
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14609 * 0.55935017
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86952 * 0.64994121
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64977 * 0.79504901
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4235 * 0.78569438
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13908 * 0.29591228
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72161 * 0.73324264
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70864 * 0.12543590
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 17392 * 0.32634174
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 87841 * 0.99266014
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57855 * 0.73722204
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59790 * 0.84595713
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 33474 * 0.28869078
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 42539 * 0.79751439
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77827 * 0.68175357
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 22359 * 0.86349816
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 9844 * 0.49049773
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 51326 * 0.91658311
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 51016 * 0.62524311
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 3541 * 0.66346566
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 91961 * 0.27534907
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 42329 * 0.04863380
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'nrdmknfd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0011():
    """Extended test 11 for scheduler."""
    x_0 = 93275 * 0.48098264
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49337 * 0.50684683
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23788 * 0.63555612
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78969 * 0.82919749
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33684 * 0.82903272
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36826 * 0.25195229
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24170 * 0.32068360
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10340 * 0.11289502
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62804 * 0.30127111
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50652 * 0.85862033
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16940 * 0.68625224
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35520 * 0.12218150
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72148 * 0.88943267
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45147 * 0.41715451
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88789 * 0.62660871
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1811 * 0.51438401
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46499 * 0.65619672
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32893 * 0.05984485
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60678 * 0.28140332
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60300 * 0.21369583
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94659 * 0.46191604
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92627 * 0.33202658
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47937 * 0.23165850
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'sxnxdahn').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0012():
    """Extended test 12 for scheduler."""
    x_0 = 3763 * 0.29680671
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17213 * 0.42567802
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35652 * 0.83650083
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18326 * 0.52904419
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72001 * 0.28562412
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25661 * 0.22429933
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45829 * 0.65438033
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33162 * 0.93902298
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37970 * 0.89345015
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33545 * 0.44860675
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60567 * 0.17000476
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95022 * 0.76977320
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49896 * 0.35780953
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98840 * 0.38116030
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91339 * 0.34379058
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59214 * 0.81631842
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25328 * 0.41107789
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23949 * 0.47523246
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4626 * 0.64359286
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51501 * 0.71274268
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20580 * 0.41248681
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47353 * 0.68850723
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26631 * 0.47670799
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47614 * 0.42233232
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26445 * 0.56281186
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49389 * 0.06331957
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32077 * 0.67551781
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21972 * 0.60656106
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82042 * 0.13385469
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34420 * 0.41045769
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76518 * 0.13746541
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2858 * 0.68800582
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95234 * 0.21148354
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70622 * 0.06577778
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26671 * 0.66025699
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 63693 * 0.01980894
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98660 * 0.61440019
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72361 * 0.58388327
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 19293 * 0.07745634
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 89734 * 0.50173306
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65915 * 0.97580657
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 22778 * 0.41398799
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24598 * 0.69002410
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 5632 * 0.56392341
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92750 * 0.00803973
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 58371 * 0.27578414
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 85550 * 0.80027485
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 18676 * 0.23607938
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 50551 * 0.70330258
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 63426 * 0.75673483
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'foyeryvr').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0013():
    """Extended test 13 for scheduler."""
    x_0 = 97974 * 0.61715149
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23315 * 0.82515887
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4124 * 0.05324319
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11436 * 0.47017081
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70078 * 0.90433135
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 62305 * 0.13967802
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64962 * 0.11389054
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75619 * 0.92525978
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33923 * 0.07081614
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48256 * 0.97846090
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4098 * 0.49446364
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80915 * 0.90744647
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40431 * 0.89404502
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 35126 * 0.06559117
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27586 * 0.22102554
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34777 * 0.73188786
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48714 * 0.57277559
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42362 * 0.77518263
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85318 * 0.04441762
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21688 * 0.31728096
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64813 * 0.95455504
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41064 * 0.61611904
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10025 * 0.16624969
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82654 * 0.31457987
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 267 * 0.09397356
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78705 * 0.93221179
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 39982 * 0.65605900
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35159 * 0.73793719
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14118 * 0.61901107
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21889 * 0.40507162
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92573 * 0.91757464
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56146 * 0.53363727
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4525 * 0.29419281
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48396 * 0.85642418
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76315 * 0.68995759
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 73801 * 0.63203084
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 52163 * 0.64300602
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33816 * 0.28857102
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10967 * 0.96835837
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 97334 * 0.66871184
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 63044 * 0.24579006
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 73702 * 0.35611863
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 50964 * 0.60545533
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 29279 * 0.26200856
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59465 * 0.75409911
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 86596 * 0.30008117
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 92103 * 0.51581946
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 83768 * 0.76191843
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 55168 * 0.78677922
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 25197 * 0.41870622
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'pevfbaex').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0014():
    """Extended test 14 for scheduler."""
    x_0 = 34659 * 0.03450339
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70359 * 0.97738206
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99435 * 0.09469749
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34537 * 0.66802850
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91836 * 0.36493278
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21455 * 0.16264814
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47070 * 0.90967728
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32048 * 0.86753090
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70764 * 0.27227593
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93309 * 0.23465127
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46960 * 0.34549586
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44853 * 0.36886774
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10983 * 0.94885548
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12851 * 0.04582141
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11472 * 0.87997275
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42456 * 0.01626729
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25122 * 0.06383260
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3063 * 0.28061553
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29160 * 0.49145235
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18198 * 0.22960579
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43758 * 0.57778095
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54927 * 0.53244582
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31789 * 0.16989230
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15224 * 0.57137188
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71430 * 0.00979332
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74608 * 0.43272306
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2052 * 0.89820961
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78786 * 0.29587946
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50079 * 0.02928177
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21693 * 0.97486555
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96422 * 0.41583776
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32331 * 0.90433666
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'qjxvjont').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0015():
    """Extended test 15 for scheduler."""
    x_0 = 30136 * 0.16886037
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23173 * 0.87631432
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41687 * 0.43715884
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50574 * 0.42235661
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46055 * 0.21925404
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30317 * 0.92355241
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77561 * 0.18173522
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19923 * 0.83704188
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89839 * 0.39614940
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47862 * 0.92576361
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 792 * 0.59185744
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60609 * 0.56152974
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66132 * 0.05483455
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96490 * 0.86950162
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37955 * 0.33381230
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92363 * 0.47720140
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76282 * 0.17310784
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77020 * 0.84256257
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89795 * 0.78755471
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40132 * 0.77391809
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66200 * 0.42023134
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45365 * 0.17523602
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19850 * 0.35784050
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55081 * 0.35467725
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13143 * 0.52556487
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66924 * 0.46615430
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35319 * 0.63406799
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69336 * 0.00401859
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12214 * 0.10750718
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ipvdgxms').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0016():
    """Extended test 16 for scheduler."""
    x_0 = 12849 * 0.67344761
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21438 * 0.06448690
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96385 * 0.66977609
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88972 * 0.28380882
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73681 * 0.74845508
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86773 * 0.15351495
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39964 * 0.31131201
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54432 * 0.59840776
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12220 * 0.60348157
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99502 * 0.23053154
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80058 * 0.86539491
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52212 * 0.83590941
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52836 * 0.08805992
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62088 * 0.31968606
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30138 * 0.34819271
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75464 * 0.89862184
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4982 * 0.09556624
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33719 * 0.70421722
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54836 * 0.22614477
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11056 * 0.56772806
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13058 * 0.72939808
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61623 * 0.48868378
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33446 * 0.38093649
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42035 * 0.49593651
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72726 * 0.84722824
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84282 * 0.05744963
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12200 * 0.11749197
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91535 * 0.13683861
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35332 * 0.67348810
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33514 * 0.75424759
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45911 * 0.05445261
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89864 * 0.40347159
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68955 * 0.81309787
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2754 * 0.05754067
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85699 * 0.41347953
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 83868 * 0.19617194
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2235 * 0.55435723
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92793 * 0.32067678
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67876 * 0.70237779
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'lnqrtkry').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0017():
    """Extended test 17 for scheduler."""
    x_0 = 66430 * 0.05177997
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23666 * 0.14427066
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91253 * 0.66619313
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25582 * 0.89059531
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58620 * 0.67936767
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88042 * 0.90981770
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25635 * 0.55232268
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63508 * 0.55943622
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43275 * 0.77317228
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40717 * 0.47864677
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15794 * 0.64979950
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33175 * 0.00079655
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38676 * 0.37604843
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77505 * 0.29331894
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 97171 * 0.76181041
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43631 * 0.94748419
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30959 * 0.81586398
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2149 * 0.94133236
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20778 * 0.32713478
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30969 * 0.12308600
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25093 * 0.91243449
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26411 * 0.63253642
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9608 * 0.25874156
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72746 * 0.41182591
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81460 * 0.17628425
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22501 * 0.06196571
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74461 * 0.13890537
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'cxthhmnh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0018():
    """Extended test 18 for scheduler."""
    x_0 = 68538 * 0.70431112
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20916 * 0.62720676
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50098 * 0.38031963
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79532 * 0.68391827
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72417 * 0.00120811
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51773 * 0.84044061
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86739 * 0.76695371
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23354 * 0.89047451
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92389 * 0.59062493
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4744 * 0.87266351
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90144 * 0.38033371
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21148 * 0.81923502
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87988 * 0.01092100
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7667 * 0.10574611
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76542 * 0.74874460
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79617 * 0.05672177
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79897 * 0.88132830
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70949 * 0.90544638
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27587 * 0.20752313
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80918 * 0.19399821
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45029 * 0.62932520
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33020 * 0.87663882
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62427 * 0.89931531
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9552 * 0.28986554
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24677 * 0.76581732
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56883 * 0.09519031
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1614 * 0.31030138
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41473 * 0.25376737
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56592 * 0.53785852
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16697 * 0.03676544
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2721 * 0.17958893
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64999 * 0.28864194
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36262 * 0.97089991
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60548 * 0.58925161
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39386 * 0.26961133
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80671 * 0.33021445
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27180 * 0.48342144
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 97974 * 0.43573276
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 15343 * 0.97793163
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46293 * 0.54471456
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86140 * 0.81682946
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82868 * 0.86428835
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 43635 * 0.21470646
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 46091 * 0.37680905
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 97246 * 0.94703525
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 18175 * 0.25232338
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'xaxfgoxa').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0019():
    """Extended test 19 for scheduler."""
    x_0 = 3483 * 0.81911262
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15200 * 0.43241263
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99594 * 0.31408361
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21560 * 0.45375269
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75603 * 0.61984616
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4107 * 0.64208542
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68834 * 0.55460899
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29525 * 0.33287282
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57957 * 0.82957001
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39453 * 0.46574192
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39453 * 0.45000528
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27738 * 0.37129081
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96434 * 0.44259375
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85944 * 0.68117207
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98343 * 0.87000302
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 28515 * 0.93858637
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93830 * 0.77626254
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45546 * 0.89661037
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74868 * 0.17730317
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45790 * 0.38521897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57784 * 0.99488773
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20332 * 0.93985182
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57151 * 0.91302516
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51643 * 0.79642431
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35119 * 0.65251969
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13776 * 0.67662217
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32282 * 0.95733007
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32823 * 0.78698647
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9916 * 0.68812242
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 70958 * 0.79946808
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67252 * 0.00211220
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80491 * 0.27602072
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38490 * 0.47971590
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86745 * 0.15730565
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38487 * 0.02353396
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65201 * 0.00599037
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60494 * 0.65481673
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45148 * 0.79311108
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81213 * 0.69543267
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79823 * 0.61615683
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'jweakpmv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0020():
    """Extended test 20 for scheduler."""
    x_0 = 23129 * 0.88207919
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18942 * 0.28586162
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38551 * 0.80635473
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79638 * 0.51446487
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94491 * 0.63679117
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34550 * 0.52477909
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67454 * 0.52396674
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56210 * 0.36861458
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9126 * 0.15107481
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48116 * 0.64648560
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15917 * 0.94266385
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14145 * 0.54564230
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61009 * 0.43194438
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32156 * 0.66522926
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76279 * 0.33972297
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90589 * 0.62217172
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31651 * 0.50395292
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50111 * 0.12046817
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52392 * 0.17709230
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92210 * 0.97972712
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42686 * 0.72621169
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84441 * 0.66438955
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35299 * 0.79569657
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15683 * 0.33062228
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10650 * 0.25045532
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'ljszsupn').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0021():
    """Extended test 21 for scheduler."""
    x_0 = 4702 * 0.50043798
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81021 * 0.96262282
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85957 * 0.85112904
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64449 * 0.37965802
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24785 * 0.96027060
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12978 * 0.21016216
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2761 * 0.47291448
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44216 * 0.97760325
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31180 * 0.35185718
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20408 * 0.52726768
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26849 * 0.45275002
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28629 * 0.63249388
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49688 * 0.53136926
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42255 * 0.76591187
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24369 * 0.30403508
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24462 * 0.75458119
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30082 * 0.92847685
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67311 * 0.51789834
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14447 * 0.67007612
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27046 * 0.73593793
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 654 * 0.88105103
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82946 * 0.47778969
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15242 * 0.28959206
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94708 * 0.48860183
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53831 * 0.42801873
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10218 * 0.08517995
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92604 * 0.50424912
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64981 * 0.00042047
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'npxeimru').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0022():
    """Extended test 22 for scheduler."""
    x_0 = 99391 * 0.78094675
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16057 * 0.92009899
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88382 * 0.03020671
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1213 * 0.61265930
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96967 * 0.41888614
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8277 * 0.26588063
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41214 * 0.83186674
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15080 * 0.27404931
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 2620 * 0.11388073
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17408 * 0.30743865
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81359 * 0.29530216
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3809 * 0.24071772
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38250 * 0.42741570
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3112 * 0.16363433
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42947 * 0.08313170
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99783 * 0.70402808
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 359 * 0.97634407
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99131 * 0.40559402
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81890 * 0.58116076
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3098 * 0.62504705
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56793 * 0.80836102
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40262 * 0.60888939
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14959 * 0.61018020
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72111 * 0.87096247
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5549 * 0.84251766
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60721 * 0.93553295
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6220 * 0.68237203
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70059 * 0.76190360
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38118 * 0.86447840
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37564 * 0.12825345
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62499 * 0.07927751
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13019 * 0.34678271
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30585 * 0.70601657
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46799 * 0.03208165
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 51922 * 0.74712115
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20604 * 0.68348646
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12552 * 0.72279479
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11590 * 0.25616232
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 32654 * 0.06512616
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75178 * 0.25565672
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 28183 * 0.62901381
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97739 * 0.12796732
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 90703 * 0.28258475
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 42691 * 0.07523562
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 72419 * 0.25005734
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 90636 * 0.71709419
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 14014 * 0.96271180
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 53413 * 0.67707714
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 85867 * 0.60524315
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'wxzqfwfh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0023():
    """Extended test 23 for scheduler."""
    x_0 = 54412 * 0.38150533
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14712 * 0.37633930
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87390 * 0.96020897
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28904 * 0.56813262
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11716 * 0.32080567
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86437 * 0.65068587
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19105 * 0.46846700
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97051 * 0.92474959
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35774 * 0.57971261
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96702 * 0.45622283
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6753 * 0.40666206
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55159 * 0.72353886
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72679 * 0.53692112
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56082 * 0.18254152
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71391 * 0.82706650
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17310 * 0.27761827
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56349 * 0.01874944
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97781 * 0.26029288
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81521 * 0.30958906
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70322 * 0.91805073
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14225 * 0.44506188
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87022 * 0.95344174
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68160 * 0.63590164
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'lijkckts').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0024():
    """Extended test 24 for scheduler."""
    x_0 = 89903 * 0.44566697
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16482 * 0.50586301
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3395 * 0.68056200
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34436 * 0.24263812
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27068 * 0.03430613
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4936 * 0.90700904
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93715 * 0.49885354
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37453 * 0.26456146
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19046 * 0.32011296
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52850 * 0.36476363
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1715 * 0.72397790
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46623 * 0.75370142
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16278 * 0.30107559
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4543 * 0.18784487
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78029 * 0.31407174
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96665 * 0.46945273
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59891 * 0.49067609
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40022 * 0.82878174
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70750 * 0.34994170
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2642 * 0.38627594
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42723 * 0.55686066
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 29527 * 0.13231137
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87771 * 0.88054911
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 4163 * 0.63943682
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8666 * 0.05697086
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58332 * 0.90932276
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56876 * 0.88919120
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4308 * 0.93281540
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36219 * 0.70744697
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47642 * 0.74661060
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81303 * 0.07720406
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89997 * 0.55796593
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93493 * 0.36676675
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97185 * 0.60885621
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30802 * 0.80991809
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'uewolepd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0025():
    """Extended test 25 for scheduler."""
    x_0 = 70057 * 0.91292357
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50976 * 0.91245849
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62074 * 0.88392576
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96168 * 0.39013291
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66447 * 0.03120958
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88512 * 0.05309567
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31969 * 0.84024927
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 59535 * 0.63239472
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15782 * 0.16646380
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53109 * 0.05516411
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36983 * 0.12271336
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95564 * 0.33393001
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48424 * 0.74550817
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95458 * 0.24218091
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26837 * 0.16723924
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57393 * 0.21871591
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91967 * 0.38001709
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89192 * 0.68701768
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55217 * 0.07087108
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13039 * 0.96761304
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1864 * 0.68527525
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70517 * 0.59696666
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88495 * 0.88450322
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40713 * 0.56987595
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90980 * 0.95903228
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46032 * 0.72988468
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78270 * 0.32095285
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 92856 * 0.97933573
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19700 * 0.22219172
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78600 * 0.90100344
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33514 * 0.82996434
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12400 * 0.45399424
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86699 * 0.01226516
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64150 * 0.65381052
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90329 * 0.18179069
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95862 * 0.39064498
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65456 * 0.56499336
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94926 * 0.64775336
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62397 * 0.92321727
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 53189 * 0.05238674
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'xkmdkqxx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0026():
    """Extended test 26 for scheduler."""
    x_0 = 4498 * 0.27726224
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36105 * 0.71659425
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75720 * 0.16151892
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28541 * 0.06095492
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65173 * 0.15853689
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64947 * 0.80013026
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13973 * 0.29997245
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70628 * 0.03121049
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43559 * 0.27316263
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94106 * 0.75209260
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24473 * 0.22315647
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51106 * 0.39334984
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 86899 * 0.72424142
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10050 * 0.88415941
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26994 * 0.65695299
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46931 * 0.43037184
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62566 * 0.15624039
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17707 * 0.97893974
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65421 * 0.59485145
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77677 * 0.23461140
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42187 * 0.36573943
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86009 * 0.38318741
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69351 * 0.51368591
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25976 * 0.08746771
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81640 * 0.01646013
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32218 * 0.74314934
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18312 * 0.07562926
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14840 * 0.54822970
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59611 * 0.41364221
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44848 * 0.94319836
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64952 * 0.25078761
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44591 * 0.12088985
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69177 * 0.17348146
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22710 * 0.77821821
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42045 * 0.65553503
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87228 * 0.36736059
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78346 * 0.47690566
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32049 * 0.08538892
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61508 * 0.52309126
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96132 * 0.78598471
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20855 * 0.24084884
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85213 * 0.03605571
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 49457 * 0.60728781
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 87829 * 0.88934379
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 84060 * 0.63332327
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 62626 * 0.94546865
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'bjfytopa').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0027():
    """Extended test 27 for scheduler."""
    x_0 = 64752 * 0.37887243
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76158 * 0.27542981
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66589 * 0.38588922
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14416 * 0.98977800
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26471 * 0.99320186
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48445 * 0.18818121
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10171 * 0.91517143
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62447 * 0.41719303
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3539 * 0.19505597
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6971 * 0.21070715
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95332 * 0.79988641
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34045 * 0.24526267
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40170 * 0.18336674
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42747 * 0.56893164
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64722 * 0.02681433
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18895 * 0.36426744
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87397 * 0.00213087
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65042 * 0.46210696
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28506 * 0.35459374
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 20306 * 0.13216570
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41288 * 0.11210660
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55757 * 0.21501239
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50059 * 0.39438738
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20297 * 0.70799385
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12320 * 0.78385025
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48199 * 0.68618890
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31795 * 0.84417630
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20036 * 0.55073666
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48823 * 0.67726945
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97987 * 0.37121427
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78469 * 0.78483717
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15176 * 0.37447057
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92399 * 0.67355205
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76376 * 0.01162641
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13328 * 0.44948045
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 88867 * 0.89398292
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 16570 * 0.69386182
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84871 * 0.18137722
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'hcfjywuc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0028():
    """Extended test 28 for scheduler."""
    x_0 = 15668 * 0.55112210
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9262 * 0.59491268
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57524 * 0.53376861
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67277 * 0.70254206
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89692 * 0.96972570
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64587 * 0.65847129
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35650 * 0.01555229
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6440 * 0.78256053
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80781 * 0.84764593
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44170 * 0.03223067
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82781 * 0.30463007
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83611 * 0.76347517
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54333 * 0.17901354
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57251 * 0.68820830
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29690 * 0.71784874
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76743 * 0.38007864
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50833 * 0.75970932
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34178 * 0.49313737
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72787 * 0.14098344
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50221 * 0.82264228
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25172 * 0.77271522
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 85473 * 0.00717417
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12940 * 0.70945352
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31780 * 0.31503493
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75878 * 0.10107103
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78127 * 0.42125711
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48517 * 0.18577402
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50375 * 0.91114985
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80863 * 0.65380954
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 68871 * 0.16939249
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8317 * 0.58659151
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'qlybhvgk').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0029():
    """Extended test 29 for scheduler."""
    x_0 = 18220 * 0.94167131
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68358 * 0.71029336
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88962 * 0.56297592
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75906 * 0.31320077
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90759 * 0.89583897
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51074 * 0.47287077
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93366 * 0.04019109
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35191 * 0.44412833
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18683 * 0.47289094
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72243 * 0.38917753
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58726 * 0.34051849
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54032 * 0.36041461
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81434 * 0.23981266
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80947 * 0.26141931
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86966 * 0.36089038
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72476 * 0.04603097
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11901 * 0.60953141
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24153 * 0.01089898
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23207 * 0.32062976
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30523 * 0.26709397
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 77550 * 0.00052666
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4852 * 0.05703435
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97029 * 0.58970607
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93983 * 0.67848557
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98813 * 0.45205972
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79210 * 0.58074127
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27615 * 0.71575806
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 81890 * 0.03040433
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83654 * 0.06245114
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38546 * 0.57863898
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 39187 * 0.41453809
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 76034 * 0.96493302
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12791 * 0.96865097
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20722 * 0.18582240
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63682 * 0.87926188
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'qcbauugd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0030():
    """Extended test 30 for scheduler."""
    x_0 = 28408 * 0.22769229
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 91244 * 0.38752982
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3294 * 0.30350095
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85460 * 0.88813587
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 60926 * 0.42324893
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58532 * 0.11275022
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80685 * 0.53914235
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62895 * 0.53618713
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11352 * 0.87139487
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8898 * 0.89908167
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42376 * 0.69721989
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25730 * 0.57078006
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41029 * 0.18186424
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92643 * 0.12547301
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70872 * 0.63835370
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14537 * 0.90109661
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57489 * 0.56563160
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89640 * 0.16958981
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97894 * 0.36968124
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97220 * 0.74440641
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45345 * 0.79161679
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80276 * 0.95582920
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87132 * 0.21188910
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'beeobmwp').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0031():
    """Extended test 31 for scheduler."""
    x_0 = 19420 * 0.34066177
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35508 * 0.68647876
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29337 * 0.97434191
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38677 * 0.21452442
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5418 * 0.93924623
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73676 * 0.92184335
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81853 * 0.65334546
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23031 * 0.44098557
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22320 * 0.72998225
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8490 * 0.69825719
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42167 * 0.27134653
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40969 * 0.36347220
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12467 * 0.88560638
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61892 * 0.94178694
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94794 * 0.85596814
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5614 * 0.77226612
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 927 * 0.51888829
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99165 * 0.20046970
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98383 * 0.78012001
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99575 * 0.35176184
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7522 * 0.12764430
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48055 * 0.77566133
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64019 * 0.34883831
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85056 * 0.89685694
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80739 * 0.80376131
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53520 * 0.05204566
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21318 * 0.45390696
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50799 * 0.62693176
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49068 * 0.14440056
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17456 * 0.73542028
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'dtdoqwat').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0032():
    """Extended test 32 for scheduler."""
    x_0 = 23394 * 0.15094808
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47512 * 0.81978540
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3259 * 0.97223353
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33533 * 0.87892164
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83264 * 0.41874189
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3579 * 0.01489288
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89316 * 0.63335332
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22197 * 0.49744258
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61362 * 0.82526726
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95234 * 0.77108447
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66534 * 0.33115063
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2795 * 0.04568554
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60929 * 0.08913161
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76083 * 0.86956250
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 25032 * 0.02516283
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48699 * 0.06552929
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2502 * 0.15751191
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82710 * 0.85520198
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18525 * 0.00721859
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21809 * 0.92872765
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70582 * 0.84472072
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40241 * 0.63090450
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78833 * 0.20172632
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91960 * 0.15148759
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29337 * 0.44358337
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'xiltxyzi').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0033():
    """Extended test 33 for scheduler."""
    x_0 = 2340 * 0.71923595
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81999 * 0.49336374
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15346 * 0.40684849
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54625 * 0.17317994
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91295 * 0.52925065
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89654 * 0.96840630
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20785 * 0.50354210
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87661 * 0.73279209
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97953 * 0.18881933
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11109 * 0.64044357
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92521 * 0.07396904
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41495 * 0.22501105
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11026 * 0.46482799
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14143 * 0.01164034
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98952 * 0.15274017
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62189 * 0.64380204
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45580 * 0.79696243
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28586 * 0.64539657
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60297 * 0.99053279
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9726 * 0.81023201
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31729 * 0.35113633
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61350 * 0.52731197
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53526 * 0.92113016
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44879 * 0.66808625
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66220 * 0.35242573
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 91224 * 0.08567460
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82512 * 0.84353534
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91686 * 0.99933142
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35979 * 0.43370825
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20439 * 0.92367347
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55634 * 0.47465470
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78166 * 0.72579363
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'daggbebw').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0034():
    """Extended test 34 for scheduler."""
    x_0 = 44573 * 0.35660945
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59387 * 0.13338362
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24316 * 0.49960696
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19150 * 0.28325321
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14834 * 0.18582102
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90525 * 0.46680698
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81994 * 0.21908140
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1804 * 0.10451723
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99878 * 0.05961779
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39830 * 0.60069996
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87937 * 0.62440018
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 69571 * 0.23147380
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20305 * 0.11357463
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45164 * 0.84940832
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46002 * 0.50194111
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55042 * 0.16763251
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22192 * 0.17627744
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87712 * 0.81068363
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81182 * 0.33263927
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37726 * 0.51134881
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71936 * 0.39578934
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23030 * 0.92818234
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79887 * 0.17061344
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44010 * 0.49279205
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'qqrzzrtg').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0035():
    """Extended test 35 for scheduler."""
    x_0 = 31118 * 0.78445343
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10884 * 0.36021065
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18309 * 0.26120148
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95881 * 0.87058612
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24550 * 0.18812730
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13538 * 0.97081482
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68157 * 0.85002769
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31966 * 0.23369953
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50202 * 0.63335214
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50916 * 0.02919210
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33282 * 0.21872898
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41384 * 0.35037574
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 352 * 0.21129436
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80321 * 0.87214435
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73025 * 0.91653644
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87720 * 0.84079834
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82013 * 0.35138639
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78271 * 0.81182778
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47099 * 0.43612860
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10958 * 0.83248144
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78686 * 0.60304868
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67498 * 0.49801679
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80613 * 0.88930331
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46487 * 0.19444925
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45426 * 0.82314616
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36174 * 0.10978670
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28710 * 0.35186253
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52352 * 0.42188652
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17711 * 0.46505465
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 28458 * 0.73124783
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52980 * 0.66964931
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77059 * 0.30794452
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74568 * 0.36797000
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65434 * 0.65652428
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8814 * 0.84964436
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43355 * 0.17411415
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'ldjdxzrq').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0036():
    """Extended test 36 for scheduler."""
    x_0 = 2931 * 0.21787200
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48109 * 0.61141298
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 44343 * 0.32183945
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81711 * 0.00697527
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4876 * 0.74387216
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 24278 * 0.10614484
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25856 * 0.44865980
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50163 * 0.45805468
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15666 * 0.00221454
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86750 * 0.61670670
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91195 * 0.36569955
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63092 * 0.96907781
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67929 * 0.33653128
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23561 * 0.10577482
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76795 * 0.26236114
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32674 * 0.63569922
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45635 * 0.63294086
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62029 * 0.65845799
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36479 * 0.78501849
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55660 * 0.99440977
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2065 * 0.91177621
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17931 * 0.45556429
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14221 * 0.12380400
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23048 * 0.88553057
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8290 * 0.38310068
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82580 * 0.83130138
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58409 * 0.51088811
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65431 * 0.04063446
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90386 * 0.12777130
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94364 * 0.01786202
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30182 * 0.84855574
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95662 * 0.30093315
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 2916 * 0.66969808
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36587 * 0.43683306
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79464 * 0.95975409
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82336 * 0.24522741
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93235 * 0.16853194
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45510 * 0.22492956
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12165 * 0.84505796
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'qpjuxmfu').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0037():
    """Extended test 37 for scheduler."""
    x_0 = 95947 * 0.66149736
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88073 * 0.12802168
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60734 * 0.24390748
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4265 * 0.61206874
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16973 * 0.84028255
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2173 * 0.84174923
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76280 * 0.69116712
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99907 * 0.81646579
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50053 * 0.70913756
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48350 * 0.66135561
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73645 * 0.29921187
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19833 * 0.57392738
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42045 * 0.44094826
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58929 * 0.49524485
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71568 * 0.68374670
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1886 * 0.99933982
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64022 * 0.73859274
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58583 * 0.78792067
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2272 * 0.32449103
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97118 * 0.12500511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96735 * 0.97171778
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99183 * 0.24257162
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83192 * 0.24134465
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82703 * 0.99854600
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59602 * 0.84942491
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60758 * 0.62369924
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33652 * 0.23820966
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5294 * 0.12697110
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56171 * 0.02214726
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35458 * 0.33590801
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85886 * 0.00231739
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35924 * 0.10288600
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24072 * 0.51347943
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66812 * 0.99751940
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45487 * 0.31587238
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6340 * 0.16112463
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98140 * 0.40018630
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63060 * 0.87536456
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82942 * 0.44720431
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 12951 * 0.52369578
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19411 * 0.40030198
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'czrcqioh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0038():
    """Extended test 38 for scheduler."""
    x_0 = 63408 * 0.37149462
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19907 * 0.82153348
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 38306 * 0.07516954
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92989 * 0.08729175
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77598 * 0.30493811
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50982 * 0.84609533
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57185 * 0.90845039
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21910 * 0.81613076
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83117 * 0.04776872
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38953 * 0.74179946
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43794 * 0.06460401
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99894 * 0.71738021
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21522 * 0.42118061
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94609 * 0.76816265
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10778 * 0.11233748
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9964 * 0.48886071
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 97404 * 0.21100812
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7885 * 0.48555712
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43095 * 0.27747614
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88602 * 0.24470707
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50095 * 0.85851343
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47258 * 0.87054535
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 98004 * 0.39475287
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65593 * 0.92789802
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 94528 * 0.50372500
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62224 * 0.28001403
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 55538 * 0.14675966
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31818 * 0.05648086
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47718 * 0.51325698
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 14273 * 0.34200387
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19028 * 0.12896893
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 34755 * 0.80414093
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 3035 * 0.45396975
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70073 * 0.63994784
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16403 * 0.59541536
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45793 * 0.04383789
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67692 * 0.57348312
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 12923 * 0.93440514
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 24081 * 0.89631367
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 68492 * 0.74904127
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 26508 * 0.30599537
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 17631 * 0.21452880
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'aomxifdd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0039():
    """Extended test 39 for scheduler."""
    x_0 = 30116 * 0.66296958
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23621 * 0.85687261
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7821 * 0.86796637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28995 * 0.61117548
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49361 * 0.48354833
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3298 * 0.65098677
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21437 * 0.29659228
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95386 * 0.94554721
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66661 * 0.31167434
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79813 * 0.44527091
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96291 * 0.51825638
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56972 * 0.19040457
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59651 * 0.03052289
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88824 * 0.99056527
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37040 * 0.29820799
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78246 * 0.50294917
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52067 * 0.80496668
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45778 * 0.83159693
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2374 * 0.06015394
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57462 * 0.08160177
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58430 * 0.23447004
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23609 * 0.78818019
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57934 * 0.32614866
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19347 * 0.10696892
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55446 * 0.54335878
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'sgmakkcp').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0040():
    """Extended test 40 for scheduler."""
    x_0 = 66833 * 0.39622879
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5377 * 0.96654583
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96283 * 0.82066624
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12487 * 0.75300418
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 5593 * 0.34142324
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38276 * 0.86220319
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82100 * 0.69131572
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10174 * 0.01522938
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21859 * 0.35121411
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45076 * 0.49197931
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62180 * 0.08427096
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 4139 * 0.29067834
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25938 * 0.00334140
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92062 * 0.37913313
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36506 * 0.58420920
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99330 * 0.83135558
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27999 * 0.71598876
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43135 * 0.76254971
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42885 * 0.30062359
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47943 * 0.96846501
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6475 * 0.85899883
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88288 * 0.83243398
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87666 * 0.93575006
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71007 * 0.99160864
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24663 * 0.74151513
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52985 * 0.64138458
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36642 * 0.09435130
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7483 * 0.33057106
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69197 * 0.54435355
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25595 * 0.52938763
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'inudaadi').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0041():
    """Extended test 41 for scheduler."""
    x_0 = 17365 * 0.39054475
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93328 * 0.84779618
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64664 * 0.32782412
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26697 * 0.25865572
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87983 * 0.26439511
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47040 * 0.98119464
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17908 * 0.23674820
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61509 * 0.50978132
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 79495 * 0.18532434
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19811 * 0.56579712
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24016 * 0.18676593
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42123 * 0.95105026
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82851 * 0.02717676
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62646 * 0.25483635
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94656 * 0.73574361
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96386 * 0.33143938
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54784 * 0.05981763
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56538 * 0.83430121
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8093 * 0.05339116
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73647 * 0.29929151
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17526 * 0.48972893
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'aknzkycm').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0042():
    """Extended test 42 for scheduler."""
    x_0 = 42195 * 0.67664540
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89961 * 0.24876855
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79799 * 0.44473315
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79315 * 0.05084952
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2015 * 0.09373606
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16488 * 0.34239212
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31785 * 0.75705736
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37811 * 0.41501159
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26159 * 0.09653162
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5087 * 0.15745492
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8208 * 0.29356622
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34683 * 0.03749410
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18495 * 0.12541046
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37719 * 0.58046405
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1925 * 0.00755640
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52484 * 0.93653832
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33238 * 0.93994895
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79832 * 0.84883891
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80451 * 0.07567252
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24879 * 0.37774289
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2517 * 0.84905240
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61131 * 0.94546724
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54203 * 0.16721075
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46401 * 0.20882994
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35811 * 0.17005972
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32776 * 0.31688329
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86494 * 0.66328432
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 47890 * 0.33468455
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57802 * 0.84314490
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25202 * 0.62926154
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55612 * 0.45501973
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44941 * 0.19813458
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'pdmlwojh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0043():
    """Extended test 43 for scheduler."""
    x_0 = 31700 * 0.38060819
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62698 * 0.72147831
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41675 * 0.59230408
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25763 * 0.10560264
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41480 * 0.81511455
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23126 * 0.12954444
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10709 * 0.98014133
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30095 * 0.38451671
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14786 * 0.19417468
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76106 * 0.60560843
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6073 * 0.98103311
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57486 * 0.58551166
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 403 * 0.77486798
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98848 * 0.08552000
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41423 * 0.09712626
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90029 * 0.12516098
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48378 * 0.88594578
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41398 * 0.40868018
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46639 * 0.98146502
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14730 * 0.20620354
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21866 * 0.56844530
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'cujakimc').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0044():
    """Extended test 44 for scheduler."""
    x_0 = 77917 * 0.68863819
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 85527 * 0.38876477
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36886 * 0.57820526
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94884 * 0.71207072
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67014 * 0.25793105
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 15810 * 0.17112776
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53620 * 0.84693568
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8383 * 0.28814881
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22909 * 0.77600703
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66953 * 0.61426359
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45192 * 0.20884781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49921 * 0.72538264
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7467 * 0.99204773
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90509 * 0.13271999
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77099 * 0.57850930
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9590 * 0.83762755
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44110 * 0.93485843
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56039 * 0.25561872
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68961 * 0.10975295
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58376 * 0.90917765
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17867 * 0.43461455
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45752 * 0.11612988
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29880 * 0.18986632
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 40002 * 0.78899241
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45265 * 0.14815468
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86329 * 0.09106752
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62260 * 0.57599924
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2050 * 0.15242049
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75023 * 0.77087388
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89082 * 0.06058431
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76964 * 0.81618180
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59901 * 0.03411387
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 4036 * 0.45581486
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 37486 * 0.80964869
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 27813 * 0.28471111
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26543 * 0.25204603
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27257 * 0.84785400
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63519 * 0.90505629
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86799 * 0.40329530
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 3818 * 0.98000656
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46864 * 0.49687218
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54390 * 0.95210216
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'oqfwwoew').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0045():
    """Extended test 45 for scheduler."""
    x_0 = 55935 * 0.60412522
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95737 * 0.33692646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27637 * 0.58315582
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25711 * 0.42798078
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18462 * 0.76287996
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11549 * 0.08017838
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10237 * 0.65295581
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8621 * 0.10558442
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13333 * 0.00955066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25594 * 0.99373251
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8794 * 0.04887018
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63775 * 0.43018843
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15006 * 0.57658916
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11791 * 0.98037934
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71774 * 0.24043953
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94953 * 0.06295469
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31032 * 0.79779974
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43966 * 0.65151445
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21875 * 0.70447774
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76235 * 0.46932574
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19748 * 0.35621649
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83014 * 0.93565129
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16052 * 0.34218631
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29699 * 0.46838815
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87274 * 0.64540061
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33280 * 0.79315693
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45482 * 0.31624727
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 214 * 0.01078271
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5321 * 0.42081670
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1091 * 0.74021924
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69485 * 0.66569935
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77071 * 0.65014621
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98696 * 0.29759611
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53507 * 0.91577083
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94403 * 0.19771083
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66420 * 0.48371756
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39565 * 0.18041991
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'mzsxiqxp').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0046():
    """Extended test 46 for scheduler."""
    x_0 = 67566 * 0.56700327
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26267 * 0.54976118
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22871 * 0.54598443
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55220 * 0.01347095
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 7954 * 0.12945551
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8064 * 0.64756930
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89141 * 0.95795122
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14103 * 0.32012257
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27860 * 0.47653066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39028 * 0.01658355
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49 * 0.35482437
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 28275 * 0.32488642
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10529 * 0.68174342
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41456 * 0.93340371
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74548 * 0.17477691
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 46537 * 0.54266906
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53379 * 0.62287176
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91630 * 0.30710931
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 66584 * 0.77494321
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23811 * 0.39517361
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78584 * 0.70211314
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52480 * 0.03791083
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80704 * 0.23109335
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13754 * 0.38812295
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41071 * 0.24545411
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38635 * 0.50294743
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22143 * 0.24409879
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98370 * 0.13728499
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61002 * 0.97939833
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54242 * 0.19415927
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33249 * 0.16547042
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28068 * 0.89208977
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36918 * 0.20086193
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92807 * 0.51857457
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82663 * 0.99631196
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60366 * 0.50837483
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83060 * 0.21719940
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48901 * 0.41055443
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83003 * 0.04364064
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41922 * 0.59164991
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32030 * 0.70060843
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 5137 * 0.43301304
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6083 * 0.93625276
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 87835 * 0.47701452
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23061 * 0.42528377
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 96806 * 0.36678578
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 2286 * 0.00059753
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 37271 * 0.80800121
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'eulyhpqh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0047():
    """Extended test 47 for scheduler."""
    x_0 = 71928 * 0.75738303
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4165 * 0.13378342
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60494 * 0.15012849
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7213 * 0.18825594
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35964 * 0.74662706
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71554 * 0.24253870
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92472 * 0.41874375
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51717 * 0.50928430
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20099 * 0.31192343
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17830 * 0.43908009
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88796 * 0.75762545
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94941 * 0.75618022
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98836 * 0.78162867
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10076 * 0.82622114
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79498 * 0.67346362
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95783 * 0.12101912
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43544 * 0.90383721
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93672 * 0.16595093
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71300 * 0.55783826
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79378 * 0.60014284
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83974 * 0.89615691
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92338 * 0.59789713
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57395 * 0.55759376
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 46644 * 0.82475288
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20299 * 0.70799570
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77776 * 0.56438051
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79043 * 0.93211351
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84386 * 0.54802504
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65568 * 0.35948324
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60009 * 0.08649525
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 27554 * 0.42498628
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84686 * 0.66549794
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25323 * 0.46666596
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 5762 * 0.23872132
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12712 * 0.11099675
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 81940 * 0.09752517
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32624 * 0.82714746
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30004 * 0.54465012
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 12246 * 0.83670534
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17209 * 0.26082129
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 14747 * 0.69969147
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 95172 * 0.83069124
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66379 * 0.82929434
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 85122 * 0.13123570
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 63990 * 0.97938122
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 76278 * 0.22903912
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'pbpcjnfh').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0048():
    """Extended test 48 for scheduler."""
    x_0 = 66135 * 0.25626252
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76162 * 0.07464687
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35769 * 0.25002294
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85376 * 0.46749897
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99119 * 0.15382913
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80316 * 0.57619517
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84640 * 0.45763400
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61950 * 0.58237675
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57513 * 0.30382159
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90077 * 0.59476051
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98556 * 0.10935267
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42441 * 0.64367152
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 90691 * 0.87988324
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14010 * 0.37485915
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42023 * 0.10799698
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10655 * 0.15498886
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83836 * 0.33923108
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26217 * 0.56619038
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9873 * 0.78680740
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16277 * 0.77406085
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52643 * 0.37236395
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77122 * 0.58666668
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88097 * 0.28448257
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38718 * 0.72652577
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82659 * 0.74213767
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'hvbyvqea').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0049():
    """Extended test 49 for scheduler."""
    x_0 = 53431 * 0.29044826
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75497 * 0.53359047
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35738 * 0.61525618
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50316 * 0.78793896
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30102 * 0.41870781
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78102 * 0.06133775
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4165 * 0.52677939
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63856 * 0.51650696
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45336 * 0.55271784
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36500 * 0.09607530
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73576 * 0.69395681
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53498 * 0.64078129
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20290 * 0.64829301
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85361 * 0.04447349
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13053 * 0.91642217
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42744 * 0.99761592
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49253 * 0.87050183
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5193 * 0.74955456
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28084 * 0.54272141
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15358 * 0.68461511
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96207 * 0.29505300
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38287 * 0.94425116
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83525 * 0.07490956
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96972 * 0.47361369
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50373 * 0.33748174
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51186 * 0.01769156
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 58772 * 0.04294221
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95337 * 0.12388181
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52561 * 0.47404483
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55755 * 0.82637224
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42318 * 0.66133901
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77986 * 0.60332451
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73822 * 0.05218126
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'siokbdjx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0050():
    """Extended test 50 for scheduler."""
    x_0 = 16284 * 0.61909860
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50066 * 0.15023372
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16730 * 0.37432737
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92887 * 0.37105150
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31822 * 0.11042023
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79383 * 0.43725451
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79366 * 0.32421767
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2745 * 0.23565437
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70919 * 0.45684626
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65880 * 0.55170518
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44174 * 0.89982535
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35569 * 0.65190181
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62444 * 0.62996162
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 28168 * 0.37201952
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73775 * 0.63528995
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22387 * 0.61866602
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32735 * 0.39833808
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47205 * 0.33488803
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79433 * 0.86492157
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10894 * 0.77027812
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93679 * 0.84518040
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64634 * 0.33438229
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15200 * 0.85235293
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69121 * 0.22467719
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6771 * 0.64048204
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 27635 * 0.45642111
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45343 * 0.93778557
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41023 * 0.72351036
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62001 * 0.32259309
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18288 * 0.70295263
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18735 * 0.27853185
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3984 * 0.21153130
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34255 * 0.32154483
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81328 * 0.89495308
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85267 * 0.73688948
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5853 * 0.93520372
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'jjnzzihb').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0051():
    """Extended test 51 for scheduler."""
    x_0 = 12773 * 0.76149979
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12267 * 0.04520790
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30335 * 0.47985591
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41846 * 0.20628383
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81484 * 0.10718805
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53090 * 0.63954445
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38349 * 0.39064940
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 662 * 0.40102204
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59403 * 0.53185904
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86695 * 0.40923159
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43333 * 0.96746464
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94329 * 0.93623733
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52000 * 0.29022634
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49336 * 0.20973477
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21207 * 0.82529488
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9895 * 0.13947333
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 529 * 0.68462292
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64989 * 0.39883503
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78198 * 0.43004917
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97598 * 0.55167391
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94618 * 0.94412574
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37124 * 0.77564676
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86979 * 0.71140974
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23522 * 0.65605022
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40203 * 0.86366996
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92039 * 0.37324636
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69486 * 0.36793027
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60767 * 0.77090654
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34346 * 0.62154721
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85501 * 0.46123394
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 74175 * 0.26449361
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57271 * 0.15309591
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 21595 * 0.41524668
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91826 * 0.54679366
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41803 * 0.67675406
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93378 * 0.24712549
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2816 * 0.41683719
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62862 * 0.74027199
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92639 * 0.25165620
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 30386 * 0.83391532
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 40088 * 0.44468187
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 97241 * 0.99025962
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 49787 * 0.05231766
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 32522 * 0.06937326
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89861 * 0.20786314
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'qmysvump').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0052():
    """Extended test 52 for scheduler."""
    x_0 = 38858 * 0.21009616
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68323 * 0.07001606
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7389 * 0.09414629
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 18387 * 0.71729707
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 23212 * 0.55803746
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35207 * 0.89930346
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31036 * 0.95612518
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68821 * 0.86284653
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6746 * 0.44088847
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43921 * 0.93425606
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62669 * 0.36108605
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77854 * 0.10563079
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59210 * 0.21365344
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30386 * 0.26912004
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52174 * 0.32835330
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35323 * 0.07666767
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60504 * 0.98274098
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36595 * 0.77935513
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47416 * 0.14290767
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27536 * 0.87995683
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 90294 * 0.02332703
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40463 * 0.76121964
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 71283 * 0.29713539
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'mblosuvv').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0053():
    """Extended test 53 for scheduler."""
    x_0 = 76596 * 0.36466108
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13617 * 0.52038986
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41030 * 0.02905974
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25337 * 0.46969319
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41956 * 0.75650963
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3388 * 0.54726256
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4447 * 0.84140016
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80713 * 0.19629924
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9398 * 0.58766323
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18644 * 0.32457944
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9241 * 0.84046278
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1141 * 0.56002369
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65942 * 0.85776426
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86032 * 0.14540456
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30097 * 0.42529718
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58275 * 0.22600893
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91650 * 0.44224326
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15013 * 0.30960368
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4065 * 0.88258911
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64145 * 0.22912798
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84680 * 0.53282702
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54289 * 0.63066631
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66448 * 0.68515217
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'rwwfakna').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0054():
    """Extended test 54 for scheduler."""
    x_0 = 36078 * 0.02953997
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13764 * 0.51284512
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37281 * 0.46038577
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36368 * 0.75165403
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6645 * 0.90295635
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16679 * 0.56906709
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18293 * 0.00886372
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9649 * 0.20194778
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81303 * 0.49939238
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88288 * 0.84324942
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18168 * 0.93734065
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2837 * 0.26925749
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20665 * 0.65924484
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7489 * 0.10974272
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54923 * 0.27380277
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68034 * 0.30530196
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 11002 * 0.89398170
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40068 * 0.66980557
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38460 * 0.32475066
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83829 * 0.34141921
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71369 * 0.50519499
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68221 * 0.29042342
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40103 * 0.60326619
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59999 * 0.79083027
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22678 * 0.50548436
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36773 * 0.15877009
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49883 * 0.51952262
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37782 * 0.23352704
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93762 * 0.13534458
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49108 * 0.55467511
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'hzbzccbe').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0055():
    """Extended test 55 for scheduler."""
    x_0 = 12932 * 0.86824883
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72107 * 0.53450526
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37408 * 0.92607262
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8774 * 0.89466918
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98323 * 0.99520613
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 61315 * 0.15856455
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39692 * 0.48052383
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1812 * 0.35421782
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69859 * 0.94794073
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5175 * 0.36993980
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51540 * 0.53208920
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20136 * 0.61704086
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87306 * 0.50574512
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60281 * 0.69958822
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71367 * 0.46152409
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29683 * 0.34657812
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 81696 * 0.32564353
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44227 * 0.37224639
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42708 * 0.07831885
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46097 * 0.76901507
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87519 * 0.02706798
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52203 * 0.51252804
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3565 * 0.08989583
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20087 * 0.55973577
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89575 * 0.68458824
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38616 * 0.32404594
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33743 * 0.42242997
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7553 * 0.13878884
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9790 * 0.84988302
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50219 * 0.03563550
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32174 * 0.57511482
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97172 * 0.31764675
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62032 * 0.45077591
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 58660 * 0.40109254
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'zozpviob').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0056():
    """Extended test 56 for scheduler."""
    x_0 = 77352 * 0.59546563
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36013 * 0.73919454
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8634 * 0.29122764
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34876 * 0.44545533
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20789 * 0.13948503
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63143 * 0.97146007
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44250 * 0.03818895
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20034 * 0.76414908
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58145 * 0.97414857
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41153 * 0.34396353
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60499 * 0.53824421
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51194 * 0.61469961
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62436 * 0.46966245
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15019 * 0.62051686
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17529 * 0.71910616
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20883 * 0.56554646
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37543 * 0.35608927
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54775 * 0.11125515
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20171 * 0.89867354
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27405 * 0.20481790
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 73208 * 0.45077427
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26864 * 0.38966576
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80616 * 0.27561817
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11032 * 0.59703320
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23135 * 0.77983137
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79875 * 0.53681080
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 92971 * 0.28547991
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31113 * 0.05048628
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15489 * 0.78992134
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56730 * 0.22108867
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 38294 * 0.95452644
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65659 * 0.90361752
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48164 * 0.29984505
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32091 * 0.69210360
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73590 * 0.94249659
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26836 * 0.27382252
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43962 * 0.03243460
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5621 * 0.99182001
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48650 * 0.58612271
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 43366 * 0.75246259
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 96445 * 0.63469607
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 48452 * 0.22358308
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66249 * 0.20381812
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 58636 * 0.66107950
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 59108 * 0.69550792
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 54685 * 0.81555009
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 46311 * 0.99011201
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 9416 * 0.48353180
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 32331 * 0.07116817
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'mjpxzpvb').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0057():
    """Extended test 57 for scheduler."""
    x_0 = 65331 * 0.95517507
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65976 * 0.31782147
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25329 * 0.33508908
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68551 * 0.77871218
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81517 * 0.96030817
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50593 * 0.66296354
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21478 * 0.04756491
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88752 * 0.05313930
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12938 * 0.01347496
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93887 * 0.73429123
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77794 * 0.86039495
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5671 * 0.60618269
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5773 * 0.01581651
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29154 * 0.80543220
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46453 * 0.66112912
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25957 * 0.71772356
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 41847 * 0.13532867
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58239 * 0.57115644
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73951 * 0.11088851
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56020 * 0.11396886
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43944 * 0.49322318
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15015 * 0.08369555
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28594 * 0.78298663
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97911 * 0.75620654
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89142 * 0.02823981
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72142 * 0.64507462
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96755 * 0.19857316
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34356 * 0.81670467
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35933 * 0.46445671
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2270 * 0.21440276
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43449 * 0.57807835
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32493 * 0.95607455
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1888 * 0.62428045
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 45823 * 0.07790955
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 77129 * 0.78350677
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46863 * 0.06332831
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7009 * 0.46928743
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72827 * 0.31016834
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99947 * 0.61830157
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 84991 * 0.78502484
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6074 * 0.91959213
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82734 * 0.08922104
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 10353 * 0.72982356
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 19760 * 0.48031764
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 29715 * 0.26164948
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 58151 * 0.59213584
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 39624 * 0.21637693
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 62938 * 0.25153013
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'oqbfqmly').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0058():
    """Extended test 58 for scheduler."""
    x_0 = 68208 * 0.42487333
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20159 * 0.83104724
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46631 * 0.62529639
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70538 * 0.89039379
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48547 * 0.97497989
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 974 * 0.04532554
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16391 * 0.89949909
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44641 * 0.30539911
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24418 * 0.99277193
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43166 * 0.36140983
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18867 * 0.79118248
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 803 * 0.14762538
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52227 * 0.87816823
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 86508 * 0.18623268
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92396 * 0.14469754
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70955 * 0.83874285
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56417 * 0.11359797
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91597 * 0.13709673
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69867 * 0.37264851
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92325 * 0.47671043
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27025 * 0.66610394
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13950 * 0.65575135
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76255 * 0.00221732
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79099 * 0.24958753
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56173 * 0.11085451
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5348 * 0.02347203
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79187 * 0.30039789
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'vfvlahov').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0059():
    """Extended test 59 for scheduler."""
    x_0 = 91235 * 0.01343220
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80061 * 0.62931394
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82192 * 0.82626702
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5082 * 0.91022760
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13250 * 0.64115177
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27835 * 0.13143711
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86259 * 0.58156823
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39431 * 0.26570616
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74801 * 0.84982814
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34579 * 0.93619332
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41582 * 0.96722593
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73177 * 0.30724341
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54051 * 0.72027335
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84730 * 0.89326710
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75294 * 0.79782237
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 30316 * 0.41429090
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8546 * 0.76121963
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18517 * 0.67209707
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57956 * 0.97319268
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12659 * 0.75139378
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4707 * 0.79020171
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17368 * 0.18757749
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 29153 * 0.04511832
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18772 * 0.17423184
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56644 * 0.29582838
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72173 * 0.39718844
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31154 * 0.39004165
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61711 * 0.44809709
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94416 * 0.21054230
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59524 * 0.69415724
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'vmzqrvmx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0060():
    """Extended test 60 for scheduler."""
    x_0 = 62393 * 0.49981261
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54175 * 0.69404696
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97404 * 0.36379782
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44594 * 0.65562306
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36124 * 0.57731646
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81443 * 0.78878410
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38948 * 0.01637678
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16168 * 0.95960079
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12161 * 0.70463795
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70670 * 0.80763048
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34300 * 0.89480910
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93492 * 0.07166664
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53311 * 0.61096720
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41810 * 0.39320603
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85493 * 0.58448551
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72602 * 0.85490897
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57992 * 0.02791604
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99908 * 0.68897176
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13445 * 0.45493214
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31814 * 0.56601944
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'ykzjnhcd').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0061():
    """Extended test 61 for scheduler."""
    x_0 = 5787 * 0.99100889
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36458 * 0.25921069
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89112 * 0.95120227
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61310 * 0.92817447
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72190 * 0.99632257
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10775 * 0.19887005
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8593 * 0.34934907
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9043 * 0.58916594
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40229 * 0.06839085
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72813 * 0.64387409
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 31404 * 0.80651119
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59811 * 0.50997485
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7531 * 0.41945020
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37814 * 0.13927764
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41717 * 0.81642582
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22016 * 0.24624476
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62977 * 0.16053303
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60798 * 0.68697001
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37599 * 0.55695177
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 500 * 0.77607130
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'clkymglz').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0062():
    """Extended test 62 for scheduler."""
    x_0 = 52550 * 0.25160282
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15417 * 0.85620387
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 60887 * 0.46778594
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77598 * 0.05189283
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 15934 * 0.64839210
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79366 * 0.77784100
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52758 * 0.48319905
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93572 * 0.52873217
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71312 * 0.54478545
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74162 * 0.83931283
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45746 * 0.82589844
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52656 * 0.18217658
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 16745 * 0.45414491
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2919 * 0.15132435
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28331 * 0.03378675
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 34304 * 0.86358800
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29798 * 0.62446532
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94716 * 0.44822905
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58894 * 0.64553974
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 21347 * 0.48294900
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 232 * 0.99402575
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'zlbltcac').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0063():
    """Extended test 63 for scheduler."""
    x_0 = 77270 * 0.89152126
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9199 * 0.69801047
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57620 * 0.52929924
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46756 * 0.80077900
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17605 * 0.28106081
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32022 * 0.77262378
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73291 * 0.23973577
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84699 * 0.36844987
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 71255 * 0.36712616
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46533 * 0.66675272
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84311 * 0.64756489
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67398 * 0.11466974
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62214 * 0.01705067
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70969 * 0.40615260
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56973 * 0.52400513
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79112 * 0.67420333
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26559 * 0.46046223
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81521 * 0.50480656
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99849 * 0.69187085
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66048 * 0.17005039
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92073 * 0.65118673
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61 * 0.04424221
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43782 * 0.86981976
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79108 * 0.59589018
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65571 * 0.48612852
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45559 * 0.92998915
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90394 * 0.56210944
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85798 * 0.18313629
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44627 * 0.64131318
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 60028 * 0.24574224
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37328 * 0.29800303
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50044 * 0.54428975
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69917 * 0.95164177
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63369 * 0.40423973
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72184 * 0.21288186
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62606 * 0.96231503
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12655 * 0.23561252
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11477 * 0.67480954
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82090 * 0.97579063
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51994 * 0.36845992
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 15687 * 0.82205848
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 19025 * 0.18796990
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 28632 * 0.16848228
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 19407 * 0.68834634
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 48818 * 0.47470304
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 38172 * 0.99226688
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 26235 * 0.16556038
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 5557 * 0.58997334
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'nxyhlvcx').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0064():
    """Extended test 64 for scheduler."""
    x_0 = 10634 * 0.59735992
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43711 * 0.04885366
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47106 * 0.44374147
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30169 * 0.87092238
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74382 * 0.45988521
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34423 * 0.78250685
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51575 * 0.36670269
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56510 * 0.65437480
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68355 * 0.06236526
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88772 * 0.03282549
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62671 * 0.39187392
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 38494 * 0.73772399
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59189 * 0.56654456
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95849 * 0.47633430
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68068 * 0.34975829
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6642 * 0.12677841
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37071 * 0.38905379
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34319 * 0.67003485
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64605 * 0.65903241
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35962 * 0.56934472
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70052 * 0.56804425
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27509 * 0.39431906
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40870 * 0.21777450
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18140 * 0.11389011
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43544 * 0.48736222
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 2 * 0.85481692
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82196 * 0.20576159
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 67056 * 0.96448854
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67118 * 0.66323462
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 98920 * 0.13637371
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96481 * 0.99508244
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68212 * 0.45417543
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 14987 * 0.49364196
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44843 * 0.47491357
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1915 * 0.51988821
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15271 * 0.40806190
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35115 * 0.99305564
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 63423 * 0.09478078
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 55725 * 0.24428116
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73733 * 0.74692700
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43518 * 0.50249413
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 61687 * 0.94219753
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 51283 * 0.41414595
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 98896 * 0.71441426
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 44047 * 0.29142889
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 10336 * 0.31061803
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 33389 * 0.21648766
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 8053 * 0.45109959
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'lbkandly').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0065():
    """Extended test 65 for scheduler."""
    x_0 = 42869 * 0.23633094
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71713 * 0.30075196
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53111 * 0.02732736
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47970 * 0.72028630
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95636 * 0.22569791
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63831 * 0.32742339
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91544 * 0.91150054
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40129 * 0.15650166
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81528 * 0.29386740
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56789 * 0.92096372
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39129 * 0.22901384
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89857 * 0.11285179
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23900 * 0.94799032
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93374 * 0.91992850
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77325 * 0.99377195
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13691 * 0.65898668
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7999 * 0.76507924
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25351 * 0.68361009
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17090 * 0.35876483
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83853 * 0.29188197
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 46050 * 0.54169214
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22462 * 0.32662582
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41685 * 0.71627477
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42164 * 0.29918706
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21653 * 0.19884605
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55752 * 0.13797494
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86311 * 0.64992915
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 76798 * 0.20365765
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92726 * 0.08463041
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48766 * 0.36367999
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 2308 * 0.90329820
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41885 * 0.08830386
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84597 * 0.45387037
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89743 * 0.64022658
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88182 * 0.95289398
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85791 * 0.09991660
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 42103 * 0.09648627
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 20486 * 0.51883948
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 76240 * 0.81940974
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94277 * 0.96525022
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 99038 * 0.24522095
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81369 * 0.21162860
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 34245 * 0.82405724
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 64080 * 0.22529932
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 50744 * 0.93984436
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 38652 * 0.44627757
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 76266 * 0.63172762
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 11262 * 0.71860234
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'aueskznk').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0066():
    """Extended test 66 for scheduler."""
    x_0 = 835 * 0.68021001
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51056 * 0.90361344
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73486 * 0.75936648
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85273 * 0.44432577
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 95438 * 0.92695703
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28402 * 0.35028455
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84296 * 0.32935620
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91427 * 0.32133233
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17511 * 0.29827298
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80393 * 0.03603401
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69701 * 0.66742408
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43352 * 0.73803389
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58199 * 0.04989547
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7250 * 0.11577212
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 63812 * 0.95166273
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68304 * 0.34943668
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 93001 * 0.33020181
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98401 * 0.60098089
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9799 * 0.53768616
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96304 * 0.40870758
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5789 * 0.64441417
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23355 * 0.28093711
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5073 * 0.14858897
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30343 * 0.50253217
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1192 * 0.50376855
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 23545 * 0.13699595
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50730 * 0.92224738
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13437 * 0.44015402
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69759 * 0.57027309
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'hegvbrda').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0067():
    """Extended test 67 for scheduler."""
    x_0 = 74478 * 0.46154004
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26050 * 0.11754170
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87527 * 0.03598667
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35483 * 0.40512574
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33637 * 0.83789544
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37124 * 0.29633041
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59191 * 0.14282636
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93316 * 0.97901592
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93492 * 0.45266174
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73401 * 0.08057331
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45196 * 0.70144224
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72545 * 0.05250859
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77348 * 0.02424274
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38841 * 0.90585235
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19278 * 0.37209657
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71817 * 0.25873884
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22999 * 0.15212087
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82959 * 0.18889095
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19023 * 0.17535627
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10783 * 0.05588684
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3364 * 0.61151581
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55514 * 0.49929980
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12660 * 0.84407130
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12028 * 0.29469213
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8295 * 0.67161159
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28818 * 0.03686918
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42787 * 0.61514252
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'gtrzsmbj').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0068():
    """Extended test 68 for scheduler."""
    x_0 = 64039 * 0.89024657
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43521 * 0.26398949
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18107 * 0.17376630
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55194 * 0.51179977
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32756 * 0.79826524
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 79385 * 0.69102652
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53264 * 0.13308640
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6310 * 0.33912950
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99572 * 0.59040081
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46717 * 0.72175618
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77348 * 0.13993210
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95951 * 0.09713264
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14434 * 0.94990384
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81922 * 0.12602402
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19726 * 0.54762153
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51933 * 0.60282864
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47032 * 0.01040683
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97277 * 0.20308094
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88085 * 0.68867721
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10537 * 0.48732943
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10457 * 0.68526038
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45410 * 0.17563375
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12610 * 0.83902037
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16836 * 0.18967330
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14728 * 0.44679761
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86491 * 0.27841031
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60718 * 0.43471306
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83733 * 0.70916496
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50070 * 0.75759956
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75129 * 0.51347984
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8368 * 0.03907058
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18966 * 0.75089477
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73689 * 0.13168237
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94803 * 0.08965772
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83994 * 0.20053416
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14947 * 0.38680984
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35015 * 0.59172230
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50904 * 0.78114435
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77977 * 0.32473053
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13750 * 0.03899027
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 92186 * 0.86513599
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 65318 * 0.53205388
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'aymbctwi').hexdigest()
    assert len(h) == 64

def test_scheduler_extended_1_0069():
    """Extended test 69 for scheduler."""
    x_0 = 85801 * 0.93773863
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65154 * 0.74926123
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86562 * 0.14811092
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35646 * 0.09707476
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73060 * 0.68366230
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35157 * 0.69906407
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31003 * 0.75234259
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81168 * 0.39059374
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69311 * 0.95674023
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 24180 * 0.03929215
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38658 * 0.63371502
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7894 * 0.67006400
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23062 * 0.09826695
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81121 * 0.07052512
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98671 * 0.18805503
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52332 * 0.15471076
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79290 * 0.50982706
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43175 * 0.50066696
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76543 * 0.93603460
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45080 * 0.18149846
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64056 * 0.86335885
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11058 * 0.79544488
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70607 * 0.74144369
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 295 * 0.09894295
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64738 * 0.95074463
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43922 * 0.57407272
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17838 * 0.99901914
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41883 * 0.14419811
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17351 * 0.23724533
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6939 * 0.33138334
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 7973 * 0.56203111
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93207 * 0.72112044
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73644 * 0.54281792
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14266 * 0.25260963
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4206 * 0.77608015
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 62494 * 0.08655728
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 35380 * 0.39012116
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36473 * 0.44167146
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9676 * 0.04493893
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 417 * 0.49339389
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29370 * 0.94356191
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 62014 * 0.84757120
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 23569 * 0.25263858
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 68472 * 0.19990863
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 61716 * 0.51919905
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'crcvcgbr').hexdigest()
    assert len(h) == 64
