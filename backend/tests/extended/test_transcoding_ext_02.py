"""Extended tests for transcoding suite 2."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_transcoding_extended_2_0000():
    """Extended test 0 for transcoding."""
    x_0 = 8660 * 0.38702162
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86303 * 0.95678582
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68587 * 0.47806075
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72037 * 0.92806104
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21175 * 0.09285213
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53660 * 0.13384429
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19393 * 0.89296017
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72701 * 0.58933623
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53840 * 0.10551491
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7528 * 0.18089875
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80730 * 0.27482220
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26446 * 0.11681933
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54187 * 0.65922129
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26372 * 0.02089753
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30791 * 0.46584695
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97989 * 0.82214668
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54259 * 0.72438045
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56426 * 0.71371125
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31689 * 0.30944543
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10683 * 0.32763812
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82126 * 0.11546108
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90382 * 0.18609499
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37094 * 0.92662076
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96351 * 0.57791657
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21263 * 0.23159709
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81557 * 0.92277429
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71466 * 0.06160783
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99710 * 0.36625937
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 25997 * 0.87458156
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36151 * 0.42840601
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 89692 * 0.51364168
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6351 * 0.86889157
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'aghzwjhw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0001():
    """Extended test 1 for transcoding."""
    x_0 = 7856 * 0.18669747
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12956 * 0.41608528
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21610 * 0.35427546
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46804 * 0.68842047
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34813 * 0.74228064
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5410 * 0.85917986
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76234 * 0.95620210
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66004 * 0.49916809
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86026 * 0.51801361
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50709 * 0.94940601
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71202 * 0.03891815
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81438 * 0.60682078
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74509 * 0.91426520
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30607 * 0.27022544
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51363 * 0.81508465
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 25388 * 0.51900846
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 27828 * 0.15475705
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77217 * 0.73084777
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16686 * 0.59551784
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97479 * 0.45485790
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98398 * 0.13442291
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95862 * 0.76745459
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85554 * 0.09763526
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77280 * 0.04867396
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5416 * 0.19417056
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 59133 * 0.31078207
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16594 * 0.32116539
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86863 * 0.96912500
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42734 * 0.62949249
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65101 * 0.80461054
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52407 * 0.43688027
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89203 * 0.94504056
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92110 * 0.18297062
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68489 * 0.36910339
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 65197 * 0.54666648
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7392 * 0.04840242
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65531 * 0.97318111
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56353 * 0.30048415
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'otiyrcmw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0002():
    """Extended test 2 for transcoding."""
    x_0 = 97237 * 0.49227937
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 48085 * 0.46442851
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93792 * 0.91513402
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97740 * 0.73859382
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68790 * 0.46446603
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11452 * 0.17545309
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6463 * 0.29656561
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6555 * 0.84143421
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46980 * 0.49979828
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23051 * 0.36784168
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23246 * 0.63192364
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16283 * 0.61216856
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24907 * 0.27139366
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50675 * 0.17518988
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41893 * 0.79485268
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87661 * 0.92671874
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58517 * 0.56131251
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46030 * 0.50772758
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74276 * 0.16156479
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 17927 * 0.54147311
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49515 * 0.82256165
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77016 * 0.40520708
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89465 * 0.86267781
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72028 * 0.20837619
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89225 * 0.93763951
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93518 * 0.75506005
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 85924 * 0.88202158
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45083 * 0.09104656
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35669 * 0.97520602
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6247 * 0.62397703
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99320 * 0.94115795
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92030 * 0.38331585
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65650 * 0.23859175
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50559 * 0.53979158
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47829 * 0.00898895
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96579 * 0.75300530
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7526 * 0.52069920
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47369 * 0.28601786
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79141 * 0.79314428
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42692 * 0.76890793
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 62002 * 0.86627683
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26884 * 0.55619082
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 69209 * 0.10375627
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 31282 * 0.58159601
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 42764 * 0.72888884
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 68510 * 0.65656124
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 77711 * 0.99937360
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 79979 * 0.49221764
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'qlyvbtzn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0003():
    """Extended test 3 for transcoding."""
    x_0 = 71714 * 0.56566710
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55666 * 0.22105458
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59670 * 0.02966088
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78774 * 0.56898763
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70081 * 0.50467523
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30434 * 0.12515576
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22396 * 0.92749003
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63670 * 0.97164778
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62588 * 0.63887192
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1412 * 0.68740760
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36678 * 0.32455900
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22937 * 0.92934712
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17375 * 0.06583567
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9114 * 0.25873539
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 58048 * 0.87209092
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59659 * 0.95696439
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23222 * 0.24813544
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95619 * 0.41518830
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17708 * 0.51504014
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2519 * 0.22112820
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74273 * 0.59111799
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65898 * 0.90066355
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42293 * 0.57180461
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80587 * 0.59097294
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29383 * 0.40148046
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66158 * 0.62289331
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1334 * 0.45712543
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24603 * 0.27643116
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79044 * 0.25516776
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34625 * 0.49923727
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 9473 * 0.05493607
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19417 * 0.02205846
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7258 * 0.73800306
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66310 * 0.16322566
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19212 * 0.32326313
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4121 * 0.12806630
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 87781 * 0.65332775
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53884 * 0.85875838
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 72715 * 0.30954359
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76301 * 0.88320120
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 22575 * 0.52877097
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 49648 * 0.11823091
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79661 * 0.45200691
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 2177 * 0.20620036
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 89134 * 0.10188342
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 16497 * 0.40216369
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 1908 * 0.44865571
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 79804 * 0.87831924
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 89475 * 0.34718704
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'tyyqmddq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0004():
    """Extended test 4 for transcoding."""
    x_0 = 72513 * 0.74602687
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 81668 * 0.23058188
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21360 * 0.59191132
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28819 * 0.60873852
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41657 * 0.99106788
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42470 * 0.06727123
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22411 * 0.16019218
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67528 * 0.80283697
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99534 * 0.43645618
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53057 * 0.45151680
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13026 * 0.02636057
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45917 * 0.54033451
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50343 * 0.86183850
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53486 * 0.28328447
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11752 * 0.27992873
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82408 * 0.88318347
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31754 * 0.11414104
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12579 * 0.84678369
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7773 * 0.13809792
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46839 * 0.26002971
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 97265 * 0.61823368
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4060 * 0.78438882
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12815 * 0.09252423
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60618 * 0.16007750
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60910 * 0.83435923
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7215 * 0.63010881
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40352 * 0.80265449
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84855 * 0.03116272
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24670 * 0.76250691
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 4301 * 0.80490937
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81093 * 0.53709463
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 26339 * 0.77271984
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12998 * 0.23083781
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40915 * 0.56470467
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 67525 * 0.88761019
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 3510 * 0.50737396
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 29946 * 0.90767469
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36 * 0.23098055
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67136 * 0.96719881
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66366 * 0.26279271
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29603 * 0.72736875
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 21627 * 0.90178527
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 29292 * 0.10410464
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 43467 * 0.28499466
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 54245 * 0.02394080
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 39085 * 0.14748229
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 76992 * 0.46437654
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 63772 * 0.05020030
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 8505 * 0.72089696
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 3014 * 0.38381561
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'kvthdyli').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0005():
    """Extended test 5 for transcoding."""
    x_0 = 65592 * 0.84386344
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30386 * 0.03768752
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8636 * 0.00099779
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67082 * 0.69880810
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88083 * 0.33549448
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33142 * 0.74181128
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3494 * 0.22065349
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12650 * 0.54900219
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59175 * 0.17937218
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5434 * 0.86415097
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26445 * 0.45484947
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14713 * 0.37148198
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78535 * 0.98232352
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76029 * 0.62387047
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74168 * 0.91991157
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6565 * 0.78059984
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67660 * 0.52990074
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40057 * 0.96548065
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71602 * 0.23198462
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61528 * 0.31784255
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75669 * 0.86765285
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74558 * 0.73063418
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89860 * 0.83191580
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70084 * 0.84600189
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45352 * 0.31686202
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21241 * 0.22088698
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97232 * 0.22942291
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84692 * 0.64733842
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12017 * 0.29477594
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11145 * 0.54716243
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71861 * 0.99819014
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48173 * 0.39464978
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13188 * 0.22822909
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75012 * 0.97206351
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 4823 * 0.93816892
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21389 * 0.20530353
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'pzwfezpi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0006():
    """Extended test 6 for transcoding."""
    x_0 = 96044 * 0.25386167
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73061 * 0.60265661
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56252 * 0.05381860
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 47444 * 0.17618665
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32570 * 0.92600006
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22960 * 0.43946243
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67977 * 0.56804241
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72335 * 0.21255952
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92844 * 0.73412866
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41610 * 0.42992595
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40296 * 0.58457949
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45253 * 0.34971000
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99231 * 0.27284381
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44000 * 0.51872466
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95967 * 0.99711194
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81042 * 0.97091537
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37329 * 0.29398965
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31400 * 0.24387299
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95748 * 0.72985201
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26202 * 0.98476484
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81000 * 0.22570164
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 96591 * 0.25829876
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 40895 * 0.21014562
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82868 * 0.56974357
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2009 * 0.07692317
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76972 * 0.38881620
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41432 * 0.23695618
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 13004 * 0.65009053
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38563 * 0.17296085
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65646 * 0.20382824
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86540 * 0.02598238
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14142 * 0.87874161
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69963 * 0.36085092
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36823 * 0.14713119
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99121 * 0.54009022
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 51567 * 0.05476403
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39754 * 0.59523108
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74660 * 0.10439186
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83964 * 0.74594452
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25931 * 0.55664197
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 10142 * 0.00143896
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 84920 * 0.61694241
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 96693 * 0.36167032
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 66404 * 0.24037683
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'tqbxtsbc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0007():
    """Extended test 7 for transcoding."""
    x_0 = 26125 * 0.65999896
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69682 * 0.67489395
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62929 * 0.73658495
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75495 * 0.12993564
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39402 * 0.41363902
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31596 * 0.21499797
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84806 * 0.48916822
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61368 * 0.24971809
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 69153 * 0.72262320
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73962 * 0.87496306
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43187 * 0.95194983
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55171 * 0.24915125
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91583 * 0.84289668
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55324 * 0.28398297
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88804 * 0.68587867
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55645 * 0.16675416
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85203 * 0.49073473
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38567 * 0.38890276
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6987 * 0.78147868
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59643 * 0.39624193
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17396 * 0.37354163
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40793 * 0.32527042
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48750 * 0.96863367
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53487 * 0.77170768
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29815 * 0.78857214
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98254 * 0.69379909
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'xwmgbksw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0008():
    """Extended test 8 for transcoding."""
    x_0 = 36295 * 0.90713962
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23299 * 0.23293681
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26644 * 0.01255113
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 103 * 0.34402494
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51328 * 0.99000659
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52912 * 0.40886722
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76863 * 0.08642566
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32184 * 0.13597201
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57935 * 0.66464024
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95251 * 0.36079414
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6188 * 0.62258723
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80202 * 0.47729763
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 290 * 0.96339327
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80799 * 0.09421473
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 51310 * 0.95188875
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62390 * 0.72091361
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46670 * 0.90750954
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79365 * 0.77810813
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6660 * 0.18124644
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55507 * 0.56321602
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84764 * 0.25780669
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91506 * 0.63522196
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 55725 * 0.79795471
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41111 * 0.98138504
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14241 * 0.04942407
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53641 * 0.97622541
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89088 * 0.92753143
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'twzsjdsi').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0009():
    """Extended test 9 for transcoding."""
    x_0 = 3229 * 0.26661094
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63895 * 0.40697107
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25754 * 0.67575526
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97618 * 0.92756409
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96513 * 0.87731550
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32226 * 0.96635933
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74638 * 0.48734876
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56243 * 0.56806648
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70013 * 0.19565633
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 3703 * 0.71175454
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85454 * 0.14264360
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14749 * 0.84345327
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35230 * 0.31816524
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 7976 * 0.91775647
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62627 * 0.56595652
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3281 * 0.56801197
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46200 * 0.77017196
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90109 * 0.06281361
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56642 * 0.96062834
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84821 * 0.89519135
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28901 * 0.13531111
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46816 * 0.27154704
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31820 * 0.08599549
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63158 * 0.25770373
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82746 * 0.52259126
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10052 * 0.50558635
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4727 * 0.29903644
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12343 * 0.42491244
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86344 * 0.11884424
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83844 * 0.36475918
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6034 * 0.54431127
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37454 * 0.87551172
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81864 * 0.35048370
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 61013 * 0.52070838
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97470 * 0.31513933
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10104 * 0.09099431
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31729 * 0.48809026
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90215 * 0.11987982
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91585 * 0.82029424
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'eafdpavc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0010():
    """Extended test 10 for transcoding."""
    x_0 = 33616 * 0.25636083
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33703 * 0.93325099
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51707 * 0.64823888
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51302 * 0.64868614
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37 * 0.76382508
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47245 * 0.77678488
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67318 * 0.50436272
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14402 * 0.78132273
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20823 * 0.79301748
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86058 * 0.12324154
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27333 * 0.25296933
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15730 * 0.18717853
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27432 * 0.00508808
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93020 * 0.07074694
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48815 * 0.48613705
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87893 * 0.99109877
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84478 * 0.22124183
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1561 * 0.02292678
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83799 * 0.54711103
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37797 * 0.45612750
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'lxnuvses').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0011():
    """Extended test 11 for transcoding."""
    x_0 = 26470 * 0.38606721
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2260 * 0.08741721
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87577 * 0.39628594
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83396 * 0.22131985
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91121 * 0.88775416
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 28804 * 0.06028849
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34772 * 0.84546861
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4583 * 0.58594123
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96875 * 0.77904033
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48380 * 0.84354039
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49508 * 0.75436745
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5272 * 0.17376170
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41564 * 0.05643345
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38267 * 0.37845736
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5996 * 0.72907087
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75264 * 0.14502719
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26402 * 0.46360671
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90748 * 0.04934911
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32283 * 0.93642529
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85865 * 0.16237458
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1384 * 0.00537622
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77356 * 0.48071565
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90441 * 0.04876919
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84906 * 0.16829798
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62623 * 0.10450614
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28880 * 0.69762358
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97192 * 0.28581567
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97092 * 0.13603802
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'yunvrvhh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0012():
    """Extended test 12 for transcoding."""
    x_0 = 31917 * 0.56452795
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92601 * 0.29268501
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57768 * 0.91104761
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22978 * 0.07580755
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71530 * 0.21356393
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86116 * 0.20199634
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63474 * 0.39351228
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34784 * 0.81612549
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9863 * 0.23816144
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22391 * 0.13592088
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67341 * 0.84799691
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55134 * 0.95308812
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29934 * 0.37082719
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87330 * 0.44904423
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56662 * 0.68792321
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47639 * 0.47256091
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63425 * 0.69072945
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 3306 * 0.68399072
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 92389 * 0.35180390
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92737 * 0.16798187
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85122 * 0.43794985
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13856 * 0.38734953
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83367 * 0.47260346
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57652 * 0.44790282
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51553 * 0.88976093
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52806 * 0.64194331
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21414 * 0.69751449
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34903 * 0.77800948
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 89516 * 0.52981972
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73842 * 0.17151312
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21998 * 0.53536181
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27719 * 0.30374599
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61268 * 0.63652261
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9254 * 0.29869451
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34495 * 0.59759679
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54117 * 0.82861887
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74376 * 0.82690562
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1869 * 0.34530674
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46255 * 0.92423844
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 91891 * 0.17758228
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 25357 * 0.33484019
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 58085 * 0.81394458
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 24922 * 0.62892370
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 91795 * 0.21570547
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11124 * 0.40202771
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 66769 * 0.32846152
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 25560 * 0.39289606
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'masmzlya').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0013():
    """Extended test 13 for transcoding."""
    x_0 = 84735 * 0.59219030
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33098 * 0.78430193
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37386 * 0.07341556
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 96551 * 0.63233692
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63655 * 0.13989265
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69636 * 0.95606400
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31272 * 0.33541740
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48401 * 0.46184348
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58645 * 0.83574000
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41378 * 0.15080159
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1153 * 0.55641277
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 595 * 0.49333571
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19430 * 0.53004571
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75360 * 0.19339043
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92226 * 0.37342932
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10858 * 0.82569805
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15920 * 0.32009903
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60293 * 0.97943718
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 31685 * 0.63218058
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46039 * 0.32945046
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40871 * 0.58737806
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13734 * 0.44399482
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2634 * 0.65476447
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6734 * 0.04940850
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70850 * 0.13365074
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53598 * 0.17654117
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54218 * 0.29399014
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32427 * 0.25871529
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78722 * 0.87587265
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55253 * 0.91565797
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55812 * 0.75364941
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53586 * 0.23056841
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13183 * 0.44364811
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39185 * 0.21553485
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98352 * 0.28679890
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27524 * 0.67396856
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'okelhclm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0014():
    """Extended test 14 for transcoding."""
    x_0 = 51438 * 0.06152260
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5203 * 0.43244320
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57536 * 0.83302798
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75724 * 0.61219646
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1578 * 0.89850382
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 90991 * 0.46584910
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63974 * 0.92980677
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6060 * 0.97749796
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7541 * 0.31663961
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13475 * 0.05603604
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49733 * 0.60128215
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1515 * 0.40804082
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84507 * 0.88383789
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49598 * 0.03398901
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69496 * 0.66579103
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83998 * 0.64911281
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63345 * 0.98676784
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55870 * 0.79798095
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58205 * 0.83945663
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 673 * 0.12217645
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79838 * 0.78410856
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51600 * 0.55882707
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 56718 * 0.64661607
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 97950 * 0.38032820
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3933 * 0.14073215
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84583 * 0.28225574
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11566 * 0.05983958
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 53907 * 0.58850601
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36367 * 0.81416462
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43295 * 0.50027945
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75707 * 0.79115172
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68898 * 0.71634956
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62044 * 0.23582081
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 29490 * 0.71237709
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12205 * 0.52701312
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'kfdfuwxd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0015():
    """Extended test 15 for transcoding."""
    x_0 = 26714 * 0.03578683
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46911 * 0.51736702
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47847 * 0.68544143
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4879 * 0.80091976
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56455 * 0.10408811
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94044 * 0.09843156
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62937 * 0.01296544
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40713 * 0.39678171
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33920 * 0.39041443
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31508 * 0.46006171
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 51251 * 0.66189323
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73793 * 0.38181700
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25761 * 0.57030495
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5757 * 0.59063222
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24231 * 0.67354554
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27502 * 0.67578049
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8938 * 0.71143161
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56108 * 0.70476618
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90565 * 0.06825609
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61800 * 0.93369396
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65766 * 0.62672737
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90246 * 0.59132633
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27007 * 0.06767776
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 84750 * 0.15278584
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20851 * 0.24212169
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49869 * 0.96320778
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15171 * 0.95104133
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 95109 * 0.21833534
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41056 * 0.19057381
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96436 * 0.02368782
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30125 * 0.10230692
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 34851 * 0.29971876
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25458 * 0.53153340
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97875 * 0.73962146
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13399 * 0.76980009
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45823 * 0.16667697
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80710 * 0.96615253
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16111 * 0.90372663
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40600 * 0.99744692
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75977 * 0.50067721
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 21685 * 0.12486111
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'vrvqmjic').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0016():
    """Extended test 16 for transcoding."""
    x_0 = 40297 * 0.74511487
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93670 * 0.09175364
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25016 * 0.59979111
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86845 * 0.75215025
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53977 * 0.85280558
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25014 * 0.89333241
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99356 * 0.67166658
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79187 * 0.13643986
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73634 * 0.17463231
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 36355 * 0.38296031
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68391 * 0.61116237
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20556 * 0.50733209
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29617 * 0.78611420
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61007 * 0.57411803
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 21542 * 0.08959297
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6537 * 0.86487584
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49784 * 0.92593505
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22407 * 0.29798062
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82327 * 0.15604814
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25826 * 0.78544376
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50308 * 0.27020297
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71173 * 0.09682794
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68566 * 0.91909804
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60668 * 0.66820733
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90783 * 0.17491396
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36381 * 0.32766162
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74491 * 0.50091382
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68462 * 0.55087718
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15235 * 0.91862279
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83331 * 0.01426404
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67249 * 0.93991667
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1394 * 0.73341790
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34104 * 0.14511090
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86580 * 0.47790280
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11745 * 0.12313300
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68858 * 0.64756753
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 64717 * 0.56507168
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'wgupnmwb').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0017():
    """Extended test 17 for transcoding."""
    x_0 = 91782 * 0.75970288
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16434 * 0.32385329
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81129 * 0.83433208
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76586 * 0.83053463
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91450 * 0.38956551
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44711 * 0.02123160
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 47494 * 0.47489498
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93619 * 0.79704798
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96930 * 0.67757505
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84505 * 0.94858216
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26094 * 0.00084055
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 58210 * 0.99450204
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60173 * 0.26460442
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38302 * 0.31091262
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27155 * 0.33459459
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92039 * 0.29861687
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17636 * 0.68669878
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26398 * 0.00035247
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 467 * 0.93845897
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44675 * 0.00510781
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25496 * 0.66670151
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66986 * 0.96223158
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62751 * 0.61008822
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88439 * 0.52989891
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7174 * 0.19181046
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 94361 * 0.58086779
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 31759 * 0.09479195
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42929 * 0.86618438
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 78171 * 0.90421216
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 23705 * 0.04914420
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20898 * 0.44778604
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84494 * 0.10144820
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31644 * 0.72702335
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75405 * 0.13714813
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 98822 * 0.56081778
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38502 * 0.94780541
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90599 * 0.88279032
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91004 * 0.24407617
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 14351 * 0.65669364
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93051 * 0.86354045
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 11155 * 0.44102158
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33640 * 0.10052918
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57215 * 0.36195822
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 7235 * 0.38641150
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 95032 * 0.83848167
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 55665 * 0.98561312
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'imqlghel').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0018():
    """Extended test 18 for transcoding."""
    x_0 = 89914 * 0.78523147
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36824 * 0.46193542
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4673 * 0.67569578
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 43983 * 0.84212362
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22491 * 0.36210022
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56068 * 0.82891634
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55515 * 0.08325386
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49363 * 0.90589024
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60992 * 0.96592301
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69787 * 0.25763409
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10989 * 0.97208385
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73062 * 0.17127741
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55490 * 0.21501737
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57130 * 0.21165397
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33410 * 0.77593335
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8859 * 0.77434161
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33807 * 0.25941200
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21599 * 0.68392438
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15446 * 0.59186975
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15723 * 0.08338672
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41727 * 0.72353678
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 52760 * 0.73704731
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39625 * 0.65375304
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 70144 * 0.92048991
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12713 * 0.27116413
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57561 * 0.50896231
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42160 * 0.82181959
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64178 * 0.23076334
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66149 * 0.06093830
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17376 * 0.23985846
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64337 * 0.52358103
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9005 * 0.37824703
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95295 * 0.48679695
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76779 * 0.93779454
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6640 * 0.16558120
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60201 * 0.26096060
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12994 * 0.51154012
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45038 * 0.84093344
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 46296 * 0.07914866
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 39957 * 0.24410955
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38712 * 0.80710358
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67265 * 0.90581894
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 13166 * 0.72461123
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 63247 * 0.60363819
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 40160 * 0.72934088
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 34304 * 0.09130995
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 80495 * 0.80208454
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 32706 * 0.12795062
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 29548 * 0.63227874
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 49909 * 0.11367354
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'zywmxnfq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0019():
    """Extended test 19 for transcoding."""
    x_0 = 34233 * 0.75653974
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3595 * 0.98858193
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18947 * 0.41009199
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49144 * 0.11466114
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85489 * 0.95504677
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6634 * 0.69395426
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4488 * 0.67952776
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95392 * 0.38285891
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 37623 * 0.62503754
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58062 * 0.35888738
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17095 * 0.96006875
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91867 * 0.42302239
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32832 * 0.58859123
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95838 * 0.41652440
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55932 * 0.40222726
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55079 * 0.50655227
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61549 * 0.00675082
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27815 * 0.84836585
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 88752 * 0.39573381
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22141 * 0.99724486
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99237 * 0.45550386
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48512 * 0.11216207
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9925 * 0.34793058
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25490 * 0.03787265
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 32096 * 0.79385579
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98108 * 0.23788523
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6090 * 0.33424605
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 641 * 0.73473775
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26507 * 0.96643452
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93839 * 0.15474522
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58848 * 0.95693564
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74927 * 0.28177581
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34563 * 0.62406703
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 2579 * 0.04616084
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 17839 * 0.81337963
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79223 * 0.08107944
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68563 * 0.44059662
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'voqsisuv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0020():
    """Extended test 20 for transcoding."""
    x_0 = 60994 * 0.62116963
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35087 * 0.48439490
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 65752 * 0.99397600
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8280 * 0.43297412
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65447 * 0.26175266
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51171 * 0.67864699
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73296 * 0.61978999
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46028 * 0.97696731
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 31157 * 0.92563762
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33050 * 0.69383598
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89635 * 0.14080949
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 79221 * 0.49357129
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 83215 * 0.50092564
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97628 * 0.47176346
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66181 * 0.27075337
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40327 * 0.03726585
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51032 * 0.35413542
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70405 * 0.73516460
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61519 * 0.94900500
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6969 * 0.89009526
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51585 * 0.88917531
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'hzektanj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0021():
    """Extended test 21 for transcoding."""
    x_0 = 24047 * 0.26956333
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36485 * 0.44008538
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78603 * 0.49431623
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30428 * 0.66548086
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89996 * 0.69446523
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38376 * 0.33061437
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43510 * 0.29392397
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 84194 * 0.10584247
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68284 * 0.71354983
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15485 * 0.43992509
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17545 * 0.55978539
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68770 * 0.09356070
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13535 * 0.85147077
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80614 * 0.53509160
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81043 * 0.41693415
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73964 * 0.36732683
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95101 * 0.47390776
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13539 * 0.28983558
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70286 * 0.24820426
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80059 * 0.47321849
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53562 * 0.35978990
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97920 * 0.31197555
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49040 * 0.66060646
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74803 * 0.69848355
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67179 * 0.83079331
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81016 * 0.16848133
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11815 * 0.33214098
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29796 * 0.09003527
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20345 * 0.56991256
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49229 * 0.55511646
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88331 * 0.66868091
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10822 * 0.30918565
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73683 * 0.77039130
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68416 * 0.16363492
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47625 * 0.34237133
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93244 * 0.25390935
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20092 * 0.25798907
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 54345 * 0.47442087
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79590 * 0.20292302
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 70825 * 0.12016401
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 57314 * 0.69793135
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 2091 * 0.73930520
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 864 * 0.49115334
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 69979 * 0.69898713
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 42147 * 0.75782290
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 14551 * 0.63007463
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 12493 * 0.40002051
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 48608 * 0.67821960
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 16502 * 0.27704037
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 72492 * 0.00824214
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ldxvamzj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0022():
    """Extended test 22 for transcoding."""
    x_0 = 69154 * 0.90444465
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88955 * 0.09669144
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31839 * 0.29303278
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84303 * 0.50150306
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97777 * 0.97734320
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80083 * 0.60024136
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59749 * 0.18198579
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71568 * 0.99491914
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81670 * 0.24127593
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55227 * 0.85052634
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9066 * 0.11923355
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31458 * 0.16052209
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76416 * 0.55619177
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31073 * 0.50500559
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81035 * 0.47652211
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78912 * 0.73610596
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13683 * 0.96299527
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73327 * 0.85574696
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10851 * 0.89376308
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15037 * 0.04092998
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80657 * 0.40782595
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60556 * 0.66295880
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67531 * 0.12551481
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 71966 * 0.23881693
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99409 * 0.22956275
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73858 * 0.86955044
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61438 * 0.92965706
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52460 * 0.31265966
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63673 * 0.76541832
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29403 * 0.01267550
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33120 * 0.73543404
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62533 * 0.60048156
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68973 * 0.56596125
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60683 * 0.99967060
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42691 * 0.37741176
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14752 * 0.43976257
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 53614 * 0.18912209
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68316 * 0.77566298
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91324 * 0.45829744
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66994 * 0.66974655
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 22235 * 0.13007251
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 88401 * 0.20525922
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 45583 * 0.81256788
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 98416 * 0.21010605
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 3487 * 0.51796119
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 67384 * 0.08050069
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 7215 * 0.54973693
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 27897 * 0.54796024
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 17617 * 0.11919528
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'buaquljs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0023():
    """Extended test 23 for transcoding."""
    x_0 = 96774 * 0.89718544
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98514 * 0.55451384
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94860 * 0.95113514
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51305 * 0.52019077
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53823 * 0.01521770
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17285 * 0.85057351
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34923 * 0.13115987
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73079 * 0.52866043
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15671 * 0.63374674
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64696 * 0.39404916
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21326 * 0.27729965
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90682 * 0.67745237
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 68292 * 0.41836383
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97364 * 0.04296170
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73984 * 0.46822643
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94970 * 0.07855726
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43072 * 0.14945437
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61807 * 0.28015092
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56923 * 0.72567497
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71338 * 0.52588252
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82103 * 0.79059485
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99092 * 0.25958865
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28858 * 0.36766231
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11193 * 0.11722200
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3970 * 0.91610793
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39218 * 0.83553480
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86520 * 0.48990587
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86315 * 0.08055998
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 700 * 0.16731001
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63740 * 0.45082133
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99566 * 0.11444090
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64298 * 0.47436707
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54937 * 0.85940998
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81989 * 0.46714419
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33800 * 0.05629952
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 86141 * 0.77793489
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81617 * 0.47736142
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16071 * 0.11190715
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38935 * 0.38729301
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 99610 * 0.94944360
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20439 * 0.07969681
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 81960 * 0.26307742
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 93775 * 0.66756220
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92589 * 0.04211267
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10554 * 0.74631260
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 95363 * 0.82594415
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 79746 * 0.51111887
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 66119 * 0.76799114
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 38434 * 0.74517775
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 24892 * 0.21775945
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ztfumsvu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0024():
    """Extended test 24 for transcoding."""
    x_0 = 77988 * 0.90021676
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32302 * 0.01303695
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54529 * 0.96446686
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8953 * 0.15642292
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76109 * 0.45130020
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9593 * 0.71960125
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24865 * 0.86820947
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1814 * 0.64583776
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59899 * 0.51748470
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95429 * 0.37692770
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97493 * 0.69298870
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66709 * 0.50883524
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50029 * 0.22002654
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77561 * 0.37445884
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49883 * 0.69571688
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74690 * 0.71812024
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5537 * 0.40168615
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67831 * 0.06600626
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5811 * 0.90083934
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65285 * 0.99644698
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25785 * 0.64033602
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28920 * 0.25774975
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13125 * 0.70076399
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 52554 * 0.75299506
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17185 * 0.30596699
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 97094 * 0.71430536
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 68681 * 0.99742302
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98554 * 0.49839533
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86606 * 0.53762004
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18607 * 0.71847572
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99403 * 0.09132006
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19694 * 0.29033950
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81818 * 0.87295751
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11260 * 0.26589185
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 54918 * 0.50475488
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36500 * 0.15041942
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40107 * 0.17942243
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26849 * 0.12832692
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 7446 * 0.13287131
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'yrxeiwmc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0025():
    """Extended test 25 for transcoding."""
    x_0 = 4414 * 0.82691986
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68927 * 0.98817233
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16656 * 0.61254842
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1186 * 0.50143111
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14795 * 0.27134318
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11627 * 0.92350490
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64137 * 0.52349921
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67771 * 0.91532775
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33206 * 0.15337843
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48126 * 0.98464014
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96454 * 0.55225253
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96235 * 0.81757532
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15886 * 0.94333341
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82021 * 0.69595384
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42468 * 0.90636267
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74210 * 0.61531267
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90095 * 0.11306675
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63892 * 0.33167093
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 73816 * 0.90712883
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49319 * 0.60059470
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30655 * 0.89081066
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 82049 * 0.19949919
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33053 * 0.74112735
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74354 * 0.60873911
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79371 * 0.86738344
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98299 * 0.06090762
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61154 * 0.21622645
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'fcgcndxy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0026():
    """Extended test 26 for transcoding."""
    x_0 = 57614 * 0.68066546
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33753 * 0.55058747
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35628 * 0.57981346
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54298 * 0.81383376
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26783 * 0.91618213
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22499 * 0.33825346
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25851 * 0.57835096
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29085 * 0.96197939
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61768 * 0.97144494
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62077 * 0.84038620
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92265 * 0.04341797
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12270 * 0.90290172
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84543 * 0.05796526
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99859 * 0.73220648
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8227 * 0.66991406
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2931 * 0.15750967
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57248 * 0.28545149
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92130 * 0.44574694
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60070 * 0.42592547
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 97785 * 0.61105416
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16719 * 0.21215333
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 62065 * 0.65332093
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 815 * 0.29786845
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56681 * 0.50010668
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63630 * 0.06317321
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22880 * 0.63736860
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 26913 * 0.36042095
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66161 * 0.88817294
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95034 * 0.41445567
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3247 * 0.22943628
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 32734 * 0.63870206
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59693 * 0.16561694
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 49977 * 0.30536025
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 92438 * 0.83932277
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14784 * 0.86274491
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69642 * 0.28134902
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 37689 * 0.39256702
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 51734 * 0.92119771
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 96040 * 0.19946145
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59571 * 0.38647142
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 738 * 0.70777850
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 13281 * 0.81149693
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'xejmcamv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0027():
    """Extended test 27 for transcoding."""
    x_0 = 47616 * 0.08020870
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39393 * 0.32521391
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42069 * 0.73217302
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44855 * 0.73079747
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97752 * 0.02462286
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73867 * 0.37930255
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5705 * 0.09735688
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48444 * 0.05165185
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58372 * 0.99634725
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4450 * 0.22244946
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90172 * 0.62625265
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82926 * 0.18624067
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37091 * 0.71459642
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44494 * 0.95021550
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12825 * 0.32337198
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91213 * 0.42550463
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62648 * 0.64016408
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 44335 * 0.18282106
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52373 * 0.08772647
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29897 * 0.61334109
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 47464 * 0.02086411
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91808 * 0.24389788
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62570 * 0.48622042
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 56359 * 0.17133230
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1034 * 0.02418812
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 30514 * 0.44207551
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15743 * 0.07219604
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34838 * 0.62912604
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 87415 * 0.70926220
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46362 * 0.33184169
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 93429 * 0.49758694
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'elncegno').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0028():
    """Extended test 28 for transcoding."""
    x_0 = 51109 * 0.94445832
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94114 * 0.95911253
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69919 * 0.49972458
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45779 * 0.39901500
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9442 * 0.36722624
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48792 * 0.66213892
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1233 * 0.42174747
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97268 * 0.25316218
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63173 * 0.13606960
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81400 * 0.75596320
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83695 * 0.00004428
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13597 * 0.27634590
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57614 * 0.14427668
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61351 * 0.52431099
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60603 * 0.74716737
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53280 * 0.08307639
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43568 * 0.46682588
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60999 * 0.37513226
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85389 * 0.01751597
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50709 * 0.26240687
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81753 * 0.55750153
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50415 * 0.88995912
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75061 * 0.84708325
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47495 * 0.18455991
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 95887 * 0.75900716
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'vvoohmgy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0029():
    """Extended test 29 for transcoding."""
    x_0 = 4471 * 0.82842886
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36357 * 0.31400535
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10183 * 0.45129048
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90058 * 0.13206110
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4534 * 0.05615687
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99498 * 0.69092460
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55429 * 0.22893514
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31161 * 0.28148604
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35368 * 0.78137277
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64669 * 0.16441343
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81136 * 0.75937490
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45813 * 0.19583485
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39968 * 0.38223669
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43341 * 0.38214769
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4646 * 0.19246006
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51343 * 0.67703530
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14117 * 0.76502609
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51730 * 0.75362892
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37840 * 0.74904866
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45115 * 0.90192454
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27870 * 0.67959346
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21917 * 0.63576544
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 67638 * 0.25023810
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ktnhzqry').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0030():
    """Extended test 30 for transcoding."""
    x_0 = 62687 * 0.91886663
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89937 * 0.10775780
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 62974 * 0.24215227
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17096 * 0.06210243
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31534 * 0.70295642
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56169 * 0.33422128
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31335 * 0.35488388
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81775 * 0.14995115
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98992 * 0.44557329
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97215 * 0.44082809
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7223 * 0.63525329
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75283 * 0.83092233
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81829 * 0.49459737
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20460 * 0.67079241
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 82754 * 0.19444782
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84012 * 0.85165746
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83124 * 0.77561712
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57813 * 0.62530671
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78483 * 0.61437451
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25871 * 0.36471179
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87732 * 0.42572922
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18164 * 0.45533762
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28223 * 0.07867942
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91107 * 0.71381796
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68146 * 0.34696137
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 3865 * 0.87314997
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48131 * 0.01916315
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 88068 * 0.82801855
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35340 * 0.96918962
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37032 * 0.00991446
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46896 * 0.49259330
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13470 * 0.23762242
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29606 * 0.82648183
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 33302 * 0.40601307
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 12822 * 0.27318832
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 61204 * 0.66932967
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 19866 * 0.23905187
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64157 * 0.77585580
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80573 * 0.22766530
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 83375 * 0.53808983
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20166 * 0.09884038
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72241 * 0.97709312
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 40184 * 0.61122608
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 63625 * 0.57910628
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 53456 * 0.66495549
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 13804 * 0.54951728
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 8379 * 0.18427740
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 3073 * 0.15438302
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 62627 * 0.12421641
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'gyrbyzzf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0031():
    """Extended test 31 for transcoding."""
    x_0 = 17729 * 0.07087109
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28756 * 0.82902257
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40696 * 0.86687471
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44746 * 0.59859094
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73459 * 0.59787781
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60383 * 0.20531245
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40429 * 0.28035904
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62250 * 0.36892900
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62650 * 0.05662121
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 83739 * 0.07962826
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47327 * 0.73291440
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5620 * 0.06452687
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99555 * 0.28961781
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67962 * 0.21671181
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26924 * 0.80039268
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87241 * 0.55795672
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37987 * 0.23587909
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60279 * 0.67409077
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29080 * 0.64432003
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60699 * 0.58527453
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25782 * 0.98276154
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2233 * 0.51547599
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 93120 * 0.63143268
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45060 * 0.78472666
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3864 * 0.36187205
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 62626 * 0.81670371
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14797 * 0.99622958
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 98160 * 0.89429872
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93619 * 0.34415914
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69594 * 0.65584944
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 86250 * 0.55517810
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18621 * 0.84194114
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 72148 * 0.96035001
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53436 * 0.59140800
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 16810 * 0.30650152
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59634 * 0.79175524
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41269 * 0.43675911
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'zjwsibvj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0032():
    """Extended test 32 for transcoding."""
    x_0 = 6073 * 0.70732814
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30343 * 0.05730597
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22509 * 0.16758208
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 80384 * 0.55149676
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57415 * 0.07551650
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80401 * 0.24152202
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27499 * 0.62571599
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64440 * 0.14104494
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12710 * 0.73864121
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21285 * 0.50030070
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89226 * 0.48648974
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10183 * 0.68447495
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70620 * 0.43577344
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91361 * 0.81750247
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18851 * 0.50419231
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51801 * 0.98995413
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 31937 * 0.46978117
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32206 * 0.43117766
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 72858 * 0.38973812
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80016 * 0.94917445
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 990 * 0.61583470
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42737 * 0.27731196
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87737 * 0.69981559
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74447 * 0.80719513
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79801 * 0.40549583
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93138 * 0.97131465
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24969 * 0.82912951
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90849 * 0.85922125
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 4307 * 0.92827995
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77962 * 0.08774072
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17132 * 0.30825176
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72271 * 0.02833996
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73607 * 0.56918103
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53863 * 0.54735231
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56047 * 0.19284656
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 82151 * 0.33829714
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 49299 * 0.04785412
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71063 * 0.76020014
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93305 * 0.52953118
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33102 * 0.20932473
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80587 * 0.96805314
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 48237 * 0.64874008
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16246 * 0.92165618
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 26021 * 0.38893288
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 12553 * 0.52189355
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 71925 * 0.33284426
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 44200 * 0.19320260
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 34589 * 0.33327045
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'wihlmzep').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0033():
    """Extended test 33 for transcoding."""
    x_0 = 39738 * 0.46052640
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30988 * 0.12564558
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34141 * 0.12749369
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21180 * 0.77303665
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57929 * 0.15900827
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 303 * 0.50827032
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19717 * 0.86115669
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 91187 * 0.67292235
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30348 * 0.68820982
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94821 * 0.37457176
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89748 * 0.46363586
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54162 * 0.82065307
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76785 * 0.12673855
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 39624 * 0.53364388
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33143 * 0.82379819
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7407 * 0.16160333
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75394 * 0.45410226
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91506 * 0.15885735
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25183 * 0.49128331
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30670 * 0.28947003
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6167 * 0.96176014
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 15753 * 0.91122942
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89716 * 0.15218754
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66320 * 0.19667065
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84444 * 0.70766207
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83411 * 0.01811042
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63506 * 0.42810400
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61758 * 0.19021315
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 83715 * 0.64008819
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2814 * 0.39078319
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'anbvnwun').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0034():
    """Extended test 34 for transcoding."""
    x_0 = 3648 * 0.22494875
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66960 * 0.02568792
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71059 * 0.03523107
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40633 * 0.71731416
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 35307 * 0.61119641
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65825 * 0.40188250
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25563 * 0.10505679
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46299 * 0.42612216
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28607 * 0.25474026
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33397 * 0.91928522
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66846 * 0.29021951
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55293 * 0.54399900
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70577 * 0.62125306
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82428 * 0.99316166
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15447 * 0.76593079
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44736 * 0.62836577
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 88092 * 0.68569278
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34018 * 0.57053363
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9994 * 0.13907270
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39565 * 0.89926395
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75486 * 0.24723379
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47800 * 0.69815622
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12545 * 0.04233476
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47449 * 0.56052589
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85427 * 0.33405022
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48045 * 0.76977835
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59635 * 0.80050423
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16575 * 0.64633171
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62246 * 0.85499911
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58833 * 0.11598047
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88123 * 0.97172418
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46053 * 0.79146302
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70770 * 0.03998502
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32285 * 0.64140311
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 93998 * 0.22803675
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'umcedeww').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0035():
    """Extended test 35 for transcoding."""
    x_0 = 8001 * 0.75560086
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14280 * 0.71356764
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22674 * 0.42251335
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36632 * 0.40522915
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58944 * 0.39882021
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45168 * 0.15639746
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81536 * 0.76580443
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49887 * 0.11574825
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28276 * 0.03411037
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20235 * 0.31574821
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49490 * 0.07276205
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14998 * 0.86146853
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40430 * 0.35190630
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84518 * 0.17112331
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94390 * 0.27763796
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50104 * 0.49125260
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3355 * 0.23802177
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22441 * 0.03136143
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 75721 * 0.57193281
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44739 * 0.26486245
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43535 * 0.93204131
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46336 * 0.45900122
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53409 * 0.20401863
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69216 * 0.39949131
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98248 * 0.53625139
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13655 * 0.64392879
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 76470 * 0.98218837
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6027 * 0.99246011
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18955 * 0.43866208
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 6589 * 0.76630939
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44962 * 0.35665310
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77571 * 0.10861478
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 48004 * 0.99864764
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19940 * 0.65634004
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 42755 * 0.70817705
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49329 * 0.69786751
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 68203 * 0.82938735
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95417 * 0.36396611
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60451 * 0.04641223
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'txoiqbez').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0036():
    """Extended test 36 for transcoding."""
    x_0 = 72575 * 0.68843665
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28391 * 0.92324537
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16209 * 0.20320188
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15005 * 0.73209749
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88220 * 0.82745536
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4438 * 0.41541501
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38610 * 0.95873922
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65232 * 0.67026164
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70955 * 0.46706076
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8928 * 0.32728005
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46749 * 0.73484452
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89599 * 0.99810982
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11641 * 0.17153668
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51021 * 0.56392407
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64939 * 0.12723060
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 83310 * 0.07527358
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94283 * 0.03478750
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42150 * 0.18338178
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80161 * 0.43408409
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27890 * 0.97478906
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39268 * 0.29017686
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98033 * 0.87196913
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38793 * 0.80791550
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 34257 * 0.64326280
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 13346 * 0.91514798
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57987 * 0.07254796
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57489 * 0.67482939
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'qrfllkdw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0037():
    """Extended test 37 for transcoding."""
    x_0 = 61554 * 0.39764052
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73942 * 0.40550584
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92100 * 0.21611369
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3504 * 0.18170398
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71561 * 0.71919569
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44724 * 0.46150435
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28217 * 0.28162404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83192 * 0.51443256
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41074 * 0.09256432
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18307 * 0.10626260
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15924 * 0.37869490
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60971 * 0.69512314
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87819 * 0.47001666
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98137 * 0.16295863
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19 * 0.89533583
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48041 * 0.18107402
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49976 * 0.31131832
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43002 * 0.68059968
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81256 * 0.84622274
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 83108 * 0.27701683
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75207 * 0.42217648
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21147 * 0.83630742
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'kgtzftio').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0038():
    """Extended test 38 for transcoding."""
    x_0 = 59079 * 0.39718377
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20716 * 0.29171079
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 80810 * 0.82674752
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6451 * 0.75838085
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49101 * 0.92185902
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30774 * 0.84755031
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35233 * 0.10565026
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33792 * 0.08777205
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22286 * 0.94043813
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13106 * 0.29693916
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 99816 * 0.08635476
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41421 * 0.33670802
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43828 * 0.89865561
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74230 * 0.08283163
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5655 * 0.12413245
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84318 * 0.72719287
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80742 * 0.81659268
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6178 * 0.41035178
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 46702 * 0.31268889
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8819 * 0.39993455
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86273 * 0.39171335
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51840 * 0.10053557
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'qpphtsyf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0039():
    """Extended test 39 for transcoding."""
    x_0 = 32040 * 0.88764460
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69939 * 0.12510326
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63040 * 0.79258471
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16829 * 0.58885058
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74429 * 0.23273045
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41679 * 0.20938471
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21521 * 0.26199811
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23087 * 0.89954927
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 53488 * 0.28192208
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82662 * 0.80993179
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76258 * 0.12661244
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22991 * 0.70534477
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71474 * 0.70949251
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23992 * 0.80060450
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33966 * 0.14087896
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94368 * 0.75080052
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64407 * 0.65351070
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63339 * 0.58252634
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11174 * 0.09484052
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35774 * 0.02082585
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 74914 * 0.05602095
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16275 * 0.99474861
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61441 * 0.96445045
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 45331 * 0.36005395
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 48601 * 0.63570600
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51674 * 0.93859464
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4223 * 0.14108083
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64283 * 0.97475329
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29492 * 0.06904676
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21083 * 0.69651438
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18694 * 0.78089499
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 38714 * 0.34188973
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84446 * 0.24824781
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 49876 * 0.38899037
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13778 * 0.25039451
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17458 * 0.63228502
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 20564 * 0.80020398
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19419 * 0.63118554
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71053 * 0.55740557
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80532 * 0.57020632
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85329 * 0.11190483
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 20780 * 0.48892844
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 63656 * 0.57801713
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39915 * 0.56990346
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11586 * 0.95096624
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 83728 * 0.69917459
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 10469 * 0.89726837
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'czqlnwxe').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0040():
    """Extended test 40 for transcoding."""
    x_0 = 57882 * 0.63347610
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79567 * 0.26636596
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90852 * 0.25415746
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21687 * 0.07096297
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30663 * 0.81370697
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86650 * 0.24144007
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43744 * 0.48600705
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75743 * 0.51819591
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7115 * 0.97188951
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59546 * 0.30042474
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40754 * 0.78179163
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47049 * 0.06997162
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34177 * 0.20398632
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64571 * 0.32776151
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32120 * 0.06002400
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62617 * 0.96072356
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56214 * 0.19675465
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83399 * 0.52723721
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61194 * 0.15741420
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51409 * 0.40319609
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12976 * 0.50383111
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49712 * 0.90990674
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99185 * 0.38683111
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13496 * 0.38628314
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21010 * 0.06323148
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58159 * 0.92925872
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88849 * 0.14055739
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27511 * 0.08339685
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 77342 * 0.47722782
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59298 * 0.46257100
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94740 * 0.75448514
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16469 * 0.45013020
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 97081 * 0.61806278
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 94167 * 0.46347909
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 21731 * 0.23350053
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27300 * 0.86614247
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45866 * 0.01586740
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8604 * 0.33712268
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 92218 * 0.19167279
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 21546 * 0.56741014
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 96912 * 0.54845908
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 92702 * 0.24931197
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 59037 * 0.44984968
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'gfnjaznh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0041():
    """Extended test 41 for transcoding."""
    x_0 = 41427 * 0.79857655
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57195 * 0.35944578
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25009 * 0.23022195
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37302 * 0.68100380
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36680 * 0.76631796
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80867 * 0.55636009
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15740 * 0.25761385
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24195 * 0.98664046
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94994 * 0.24882325
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98079 * 0.92082292
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41706 * 0.31784898
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98006 * 0.47335474
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91849 * 0.88199463
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2520 * 0.47641208
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14402 * 0.94992933
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50751 * 0.23274703
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 3806 * 0.03451287
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5685 * 0.19187434
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 89811 * 0.44168855
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71453 * 0.75558289
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49887 * 0.83898653
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'uqsayzjw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0042():
    """Extended test 42 for transcoding."""
    x_0 = 5894 * 0.78001480
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 5823 * 0.24271001
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97545 * 0.14086367
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13000 * 0.22314938
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99256 * 0.40156553
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10847 * 0.24951572
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2151 * 0.51785857
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98927 * 0.41872936
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7262 * 0.79863131
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38731 * 0.08761648
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60300 * 0.70673699
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25862 * 0.62699043
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98960 * 0.40114506
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30529 * 0.30162749
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45744 * 0.58738754
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15503 * 0.56373916
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 43336 * 0.99450665
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38669 * 0.65831749
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 70399 * 0.52788503
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60866 * 0.47405827
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58596 * 0.59078072
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71020 * 0.06363618
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74421 * 0.52050636
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18171 * 0.39916581
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15679 * 0.82832702
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53708 * 0.13921312
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79889 * 0.95408357
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 17025 * 0.32652355
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93319 * 0.23997740
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67055 * 0.86738448
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56945 * 0.57592091
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 65029 * 0.40433681
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 40424 * 0.46395326
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 3372 * 0.42136638
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 48199 * 0.77231638
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 55496 * 0.97427831
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4685 * 0.53014203
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50250 * 0.66991885
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 22133 * 0.80708030
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 17215 * 0.00980964
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45335 * 0.13601702
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 83289 * 0.70827580
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 87876 * 0.95016021
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 30690 * 0.94504400
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 28284 * 0.49733128
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 89278 * 0.72145403
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 61520 * 0.81484130
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 47243 * 0.33140030
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 85944 * 0.61225954
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'aqriyima').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0043():
    """Extended test 43 for transcoding."""
    x_0 = 93474 * 0.43479972
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50382 * 0.08809553
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26860 * 0.60260555
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22668 * 0.94267075
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57810 * 0.24555316
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32650 * 0.79940801
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76344 * 0.44918094
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9329 * 0.06384888
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 40027 * 0.44053028
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38548 * 0.37820041
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75432 * 0.00633749
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96011 * 0.35578024
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40026 * 0.09913828
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41899 * 0.31408802
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8704 * 0.07659843
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1923 * 0.77018078
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12381 * 0.51393707
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65077 * 0.01192375
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48155 * 0.55580810
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3641 * 0.58289741
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62232 * 0.74859137
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41326 * 0.13651509
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25676 * 0.93593525
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27992 * 0.61565066
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86719 * 0.45837801
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 12272 * 0.40292266
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78657 * 0.15286898
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 33766 * 0.36136706
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23015 * 0.66740430
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7866 * 0.41631535
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23130 * 0.78123642
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'jtpdjyig').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0044():
    """Extended test 44 for transcoding."""
    x_0 = 6056 * 0.73782501
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42082 * 0.60455221
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32355 * 0.44064638
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36827 * 0.52897107
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 54355 * 0.88199051
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25105 * 0.00104514
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 45398 * 0.17708447
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30339 * 0.28546717
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 98119 * 0.78286369
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21909 * 0.25166868
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69998 * 0.44689065
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37299 * 0.03978232
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21121 * 0.79240115
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78704 * 0.94655066
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89863 * 0.25889441
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80327 * 0.54244210
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24041 * 0.20844536
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32830 * 0.53900054
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74560 * 0.08113363
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68731 * 0.84658034
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 5366 * 0.85642262
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44638 * 0.11752915
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30087 * 0.35826345
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63040 * 0.75597650
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90477 * 0.39958796
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49189 * 0.09866720
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 10246 * 0.49196647
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56280 * 0.38357866
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 17067 * 0.65051788
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97387 * 0.86922648
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 30352 * 0.48325736
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'cxkhnvoo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0045():
    """Extended test 45 for transcoding."""
    x_0 = 7159 * 0.22201507
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19638 * 0.03995613
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74809 * 0.80845861
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65319 * 0.81120792
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75035 * 0.02241727
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97327 * 0.55447387
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 2121 * 0.97626527
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74099 * 0.68706950
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 14808 * 0.54288922
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71109 * 0.41422998
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57851 * 0.64953234
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27490 * 0.65223031
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28381 * 0.46916936
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58477 * 0.65594414
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37214 * 0.19397232
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45093 * 0.15240069
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14097 * 0.30546241
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99040 * 0.38297691
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56954 * 0.87327465
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80250 * 0.00420837
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10886 * 0.60403042
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37769 * 0.83664496
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13545 * 0.52635717
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 69493 * 0.46442105
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 81708 * 0.83639092
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44244 * 0.69698630
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12836 * 0.81144192
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5471 * 0.35337039
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92415 * 0.18513865
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3176 * 0.62042717
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 59467 * 0.84132396
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 86288 * 0.39551714
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59427 * 0.77907101
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22383 * 0.55328619
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 31051 * 0.55583380
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'sbhsnqut').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0046():
    """Extended test 46 for transcoding."""
    x_0 = 83661 * 0.56559249
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14078 * 0.66157296
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71650 * 0.31657440
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76886 * 0.55978147
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 81224 * 0.30480567
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34007 * 0.17953068
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 16388 * 0.21472707
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 30361 * 0.83107553
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5073 * 0.70875216
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26101 * 0.94590505
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 75173 * 0.59242494
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2638 * 0.80272144
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15459 * 0.44197032
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 2271 * 0.90124487
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69506 * 0.56647070
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76784 * 0.92951087
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35022 * 0.88301416
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67866 * 0.59285201
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8433 * 0.99535488
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66610 * 0.68523166
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55247 * 0.16445532
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30835 * 0.39648624
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'sctrgwzl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0047():
    """Extended test 47 for transcoding."""
    x_0 = 92366 * 0.54434430
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8563 * 0.23913820
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87898 * 0.29234895
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33887 * 0.32557725
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47113 * 0.10048490
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3417 * 0.15804753
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61774 * 0.36160092
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10129 * 0.32149330
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36509 * 0.30907858
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19625 * 0.62875575
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1987 * 0.19247629
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66144 * 0.82332346
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75815 * 0.27972094
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98677 * 0.20027801
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17153 * 0.90593167
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68554 * 0.86061549
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42588 * 0.48602242
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 19917 * 0.32102736
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 33177 * 0.45715949
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5864 * 0.31760669
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94035 * 0.95871737
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86658 * 0.03486457
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47753 * 0.77811519
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50590 * 0.38768230
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72158 * 0.90579122
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 22621 * 0.85997481
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15099 * 0.91458387
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35863 * 0.37731884
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8443 * 0.44707607
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20194 * 0.07655114
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 15783 * 0.44136372
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78194 * 0.82332801
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74174 * 0.36478421
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50435 * 0.13172994
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97299 * 0.68458082
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49190 * 0.11550685
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 37386 * 0.24635495
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'osvxbnjt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0048():
    """Extended test 48 for transcoding."""
    x_0 = 58515 * 0.80578791
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2992 * 0.97084150
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34224 * 0.78399649
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61646 * 0.92906227
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11179 * 0.51647267
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27652 * 0.00528894
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 17363 * 0.05312475
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 44953 * 0.95109885
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27819 * 0.55533310
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86420 * 0.28746881
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78118 * 0.88510037
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 41836 * 0.13658597
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97912 * 0.87469772
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15240 * 0.78469201
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22683 * 0.30946246
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20667 * 0.09399880
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23003 * 0.55592855
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27503 * 0.24436823
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62667 * 0.64160681
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52764 * 0.07017859
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39034 * 0.36895318
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69219 * 0.23363141
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17893 * 0.94743726
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49684 * 0.43727266
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73687 * 0.67498956
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40478 * 0.33621991
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1215 * 0.20160602
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5259 * 0.79272579
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53164 * 0.26591420
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'gcaulrup').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0049():
    """Extended test 49 for transcoding."""
    x_0 = 23337 * 0.71205461
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 117 * 0.95032415
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64260 * 0.36775482
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39686 * 0.30997633
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70487 * 0.56816155
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23468 * 0.97855336
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23830 * 0.19978375
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80739 * 0.82324080
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17096 * 0.05695900
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 76378 * 0.85609407
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 14692 * 0.54433432
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51999 * 0.85263458
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84904 * 0.73731530
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18895 * 0.54702102
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5543 * 0.43405322
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18388 * 0.55231703
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80012 * 0.79356811
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36528 * 0.80905754
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 26147 * 0.65568907
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50420 * 0.75170476
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7000 * 0.93486564
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37665 * 0.06881199
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 74554 * 0.46717532
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82802 * 0.47468987
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23100 * 0.55687487
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82109 * 0.29907313
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53520 * 0.08329211
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55323 * 0.36852843
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18184 * 0.49564844
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43359 * 0.92261514
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 33956 * 0.58043605
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 56244 * 0.19739767
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39200 * 0.27423693
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78198 * 0.51771277
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 83826 * 0.68047259
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68176 * 0.42496330
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80620 * 0.67715746
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66301 * 0.70312126
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 545 * 0.82902922
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 27928 * 0.59224378
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29872 * 0.98909901
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12616 * 0.25457430
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81785 * 0.96543355
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 43056 * 0.04882158
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 24313 * 0.81551239
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'jzkcxdxw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0050():
    """Extended test 50 for transcoding."""
    x_0 = 16112 * 0.01086349
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90252 * 0.15949999
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47928 * 0.53836266
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27137 * 0.61892645
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42500 * 0.44402155
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96150 * 0.77153262
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44456 * 0.47844078
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54139 * 0.59755145
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3158 * 0.22741534
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49470 * 0.02361250
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19303 * 0.04619256
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84566 * 0.68388446
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4216 * 0.78895147
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74975 * 0.34011655
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55108 * 0.97603076
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99402 * 0.22458014
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 22295 * 0.38719730
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48030 * 0.62387219
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62468 * 0.55876093
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50628 * 0.83846341
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28540 * 0.68567144
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60476 * 0.21156868
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28919 * 0.30209117
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54828 * 0.50482244
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 74530 * 0.06594141
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32801 * 0.49427571
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60071 * 0.43243036
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91867 * 0.21495157
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66923 * 0.38641937
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54107 * 0.43571998
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82624 * 0.27531017
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44152 * 0.37666539
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18223 * 0.49608891
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 74526 * 0.23972237
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 3454 * 0.48628159
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45261 * 0.37059918
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93207 * 0.78162430
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 68215 * 0.24619315
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 53257 * 0.99446450
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74529 * 0.41511429
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 81628 * 0.90289778
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 98620 * 0.38215035
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 81400 * 0.13754333
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39593 * 0.94321290
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 95413 * 0.76408015
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 67586 * 0.77344452
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 15418 * 0.27006443
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 68649 * 0.90974876
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'dkedemgh').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0051():
    """Extended test 51 for transcoding."""
    x_0 = 10987 * 0.70095444
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 3587 * 0.33853099
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85430 * 0.80209324
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56780 * 0.69657523
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27434 * 0.03302334
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58360 * 0.78142475
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97738 * 0.44921297
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72591 * 0.65525757
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16638 * 0.00252693
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44535 * 0.85379432
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92716 * 0.90304949
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99414 * 0.72601246
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 25900 * 0.36546169
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24994 * 0.12952352
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96119 * 0.14204429
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93604 * 0.69829941
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42386 * 0.81189644
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35908 * 0.32609575
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82312 * 0.16061129
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27310 * 0.16030146
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26101 * 0.81469022
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35402 * 0.96809762
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13920 * 0.43564827
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93527 * 0.16266278
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36652 * 0.12680800
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16409 * 0.54475097
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 59820 * 0.06315517
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6815 * 0.57578300
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75218 * 0.64018549
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24995 * 0.46759861
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8930 * 0.29926947
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79495 * 0.36509303
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 35106 * 0.64650073
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 6512 * 0.79742352
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97358 * 0.59167353
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 92921 * 0.71585502
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78783 * 0.08626538
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94503 * 0.93074224
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 17776 * 0.40469116
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'nmugjatr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0052():
    """Extended test 52 for transcoding."""
    x_0 = 99767 * 0.37196891
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38820 * 0.78029767
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98644 * 0.78667654
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90004 * 0.74238583
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73304 * 0.89821475
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50138 * 0.94635892
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55503 * 0.85180146
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20374 * 0.63275302
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25620 * 0.61886879
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20587 * 0.52901712
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33064 * 0.46261885
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20688 * 0.10561028
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42243 * 0.03748380
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69245 * 0.42956094
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3058 * 0.38979337
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32689 * 0.53296749
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 8046 * 0.40479771
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6978 * 0.35741318
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96857 * 0.36982049
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14002 * 0.30781179
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71913 * 0.02209784
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92213 * 0.71183786
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44616 * 0.63998074
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22443 * 0.57244757
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39449 * 0.58638575
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19035 * 0.27241714
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57927 * 0.11576801
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85461 * 0.36924160
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65478 * 0.77948296
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15224 * 0.85961373
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 362 * 0.23773978
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44122 * 0.07733131
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7074 * 0.38890975
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17740 * 0.99847784
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 86929 * 0.80073243
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70227 * 0.94704962
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14792 * 0.43167812
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 25321 * 0.68454296
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 25969 * 0.95561001
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 93497 * 0.43579549
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89500 * 0.32946181
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'wdpnynwx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0053():
    """Extended test 53 for transcoding."""
    x_0 = 3125 * 0.12078639
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54722 * 0.43608223
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32295 * 0.48259009
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68396 * 0.01271862
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84806 * 0.82954422
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27346 * 0.79636604
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52789 * 0.89380616
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31843 * 0.43278231
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70359 * 0.42587840
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 70884 * 0.83459708
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80532 * 0.04776437
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53426 * 0.05895195
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32814 * 0.39333328
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70865 * 0.85247168
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81156 * 0.81623267
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9425 * 0.12365882
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83555 * 0.62611753
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 76938 * 0.34098544
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86196 * 0.00961989
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51429 * 0.10080858
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24982 * 0.66540966
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74858 * 0.36262823
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49410 * 0.22993095
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80258 * 0.65950903
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57228 * 0.00516902
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11501 * 0.67922202
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18882 * 0.50131399
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18531 * 0.05768473
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 31942 * 0.07685079
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54751 * 0.26112559
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44324 * 0.23484910
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61380 * 0.01108784
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51252 * 0.47051559
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44820 * 0.16803631
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36707 * 0.99316852
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41579 * 0.69807195
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55662 * 0.70581836
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 40884 * 0.22570233
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 80673 * 0.36458689
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63435 * 0.10883847
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71361 * 0.22111639
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 17712 * 0.29257394
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 57888 * 0.06202161
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 36365 * 0.93803335
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11131 * 0.26440457
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4821 * 0.48673349
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 75589 * 0.66296003
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'tmapfggv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0054():
    """Extended test 54 for transcoding."""
    x_0 = 56880 * 0.08013139
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 14675 * 0.97895664
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1596 * 0.15962919
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27686 * 0.72301908
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37990 * 0.36094793
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95797 * 0.57994541
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81498 * 0.86644186
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93810 * 0.99440392
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54517 * 0.47771349
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89861 * 0.05541043
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9512 * 0.84632210
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52719 * 0.01394020
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11640 * 0.44634562
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48351 * 0.85226840
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33156 * 0.32072886
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42529 * 0.46458750
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55577 * 0.39887660
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21512 * 0.38947420
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32074 * 0.69102309
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32257 * 0.57633057
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58980 * 0.15425283
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40274 * 0.12159667
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34162 * 0.62554029
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64512 * 0.16766368
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16559 * 0.23939810
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60720 * 0.93712060
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30820 * 0.36157221
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85518 * 0.28560127
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 61684 * 0.76639460
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 62934 * 0.21340206
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 21526 * 0.30689996
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92347 * 0.81233535
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 94146 * 0.93196473
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48970 * 0.92652661
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5920 * 0.00225278
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74767 * 0.76296770
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51402 * 0.76881034
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72081 * 0.52753561
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30143 * 0.62196455
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 62304 * 0.32516625
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 93922 * 0.30998080
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'gbbyomze').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0055():
    """Extended test 55 for transcoding."""
    x_0 = 54380 * 0.64010344
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 90415 * 0.02886288
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 58520 * 0.79981666
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34715 * 0.73380900
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65806 * 0.52653922
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88416 * 0.97635138
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77802 * 0.29618999
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15626 * 0.48169231
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34800 * 0.67605138
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79760 * 0.34250041
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6378 * 0.67632585
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1197 * 0.52699987
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28837 * 0.84950201
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25139 * 0.95125168
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 10977 * 0.17226540
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99235 * 0.64792111
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54841 * 0.21721528
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55248 * 0.59936846
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6273 * 0.18031492
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39025 * 0.81158838
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 19705 * 0.64379056
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73215 * 0.90432175
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24391 * 0.98154231
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31790 * 0.70118782
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29992 * 0.30476483
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 46666 * 0.22116185
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35070 * 0.67611354
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16508 * 0.21539956
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'nmckdhna').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0056():
    """Extended test 56 for transcoding."""
    x_0 = 72150 * 0.45895210
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71249 * 0.36665362
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50629 * 0.93180582
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 137 * 0.16178357
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52542 * 0.49276150
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60877 * 0.50996367
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89961 * 0.84375097
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13713 * 0.34377338
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83237 * 0.56538617
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40844 * 0.50060246
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79592 * 0.66550438
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 66008 * 0.76711185
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91292 * 0.15686435
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99259 * 0.77420775
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42143 * 0.17210306
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2005 * 0.23971545
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 67252 * 0.84432353
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77033 * 0.51471376
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10879 * 0.82209955
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63553 * 0.62915693
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12364 * 0.77735345
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24681 * 0.10904968
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59512 * 0.04068726
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11869 * 0.45232664
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62003 * 0.98409204
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37026 * 0.34111911
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9609 * 0.02834555
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38833 * 0.00591475
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 13046 * 0.54691123
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 20580 * 0.19893971
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 8607 * 0.30987751
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9139 * 0.07159880
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 74442 * 0.79100467
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 1253 * 0.86847200
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'xqtugvei').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0057():
    """Extended test 57 for transcoding."""
    x_0 = 15803 * 0.95707197
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68067 * 0.11846246
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 5272 * 0.15879774
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44874 * 0.14491296
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43292 * 0.76218842
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 39786 * 0.28851195
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98661 * 0.57359003
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21215 * 0.47153456
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47515 * 0.60869101
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55008 * 0.04095024
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39439 * 0.89531444
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81547 * 0.72545537
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 49514 * 0.61269313
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58374 * 0.31510074
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89389 * 0.36826578
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67286 * 0.40093283
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51766 * 0.47268748
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 88238 * 0.03741436
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1588 * 0.37156206
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74149 * 0.55395697
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6241 * 0.31100420
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89867 * 0.60899755
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 50051 * 0.92904209
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36771 * 0.51569577
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'nbbeegpo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0058():
    """Extended test 58 for transcoding."""
    x_0 = 1430 * 0.82231191
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21208 * 0.68287029
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53616 * 0.95996887
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99372 * 0.00145670
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83462 * 0.23417706
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3281 * 0.54492515
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52505 * 0.08193429
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46866 * 0.04050882
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3693 * 0.50672014
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10252 * 0.96228948
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93739 * 0.98457146
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16775 * 0.32571482
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 732 * 0.89378333
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34318 * 0.98804744
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17386 * 0.90613660
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79484 * 0.32705415
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14857 * 0.11847658
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 5649 * 0.38817758
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65223 * 0.69601654
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59156 * 0.34744497
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38246 * 0.51115872
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24711 * 0.24868441
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15889 * 0.57175594
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39279 * 0.32654997
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90235 * 0.40305273
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 83790 * 0.31966246
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86155 * 0.81504579
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74218 * 0.33946227
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79991 * 0.92461662
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67132 * 0.10965498
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51528 * 0.99937063
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1277 * 0.57421615
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 564 * 0.06350087
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35280 * 0.67834368
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 92964 * 0.50183300
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 94719 * 0.00980665
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 98442 * 0.57725050
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 39247 * 0.44022812
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83176 * 0.55270716
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 188 * 0.47593515
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 24091 * 0.57379615
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'kzlkuywg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0059():
    """Extended test 59 for transcoding."""
    x_0 = 18684 * 0.09418268
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15548 * 0.25279003
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1735 * 0.21280660
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52862 * 0.24650088
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85270 * 0.02947212
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7596 * 0.19906697
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80245 * 0.04460192
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80725 * 0.36559922
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49489 * 0.79592116
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22282 * 0.56957387
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22018 * 0.46625392
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21925 * 0.39009271
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87628 * 0.82182915
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59573 * 0.09011224
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50005 * 0.40030585
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4097 * 0.14685845
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60957 * 0.30704286
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87556 * 0.18887594
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55351 * 0.36416987
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10308 * 0.20209303
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51848 * 0.18819147
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89000 * 0.93912632
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96871 * 0.23256954
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 20715 * 0.13789652
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53595 * 0.21709116
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 176 * 0.82931738
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 90572 * 0.54371136
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57189 * 0.12231751
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95759 * 0.48576487
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30920 * 0.83821539
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87819 * 0.06851297
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 97936 * 0.53671671
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46152 * 0.14689757
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70185 * 0.43470598
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 79077 * 0.51426050
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38443 * 0.70274500
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 38461 * 0.24307619
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 85930 * 0.68675500
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 81622 * 0.75872708
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18345 * 0.79508147
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 82287 * 0.42380187
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54271 * 0.88717800
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 66516 * 0.53579638
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 11314 * 0.00932238
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 20418 * 0.66131046
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 58098 * 0.45480506
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 65127 * 0.92326794
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 87222 * 0.39585938
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'efnzdzij').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0060():
    """Extended test 60 for transcoding."""
    x_0 = 28902 * 0.48660453
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 50936 * 0.86560632
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99929 * 0.84009831
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99427 * 0.92125933
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56783 * 0.24616467
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58910 * 0.13270361
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88354 * 0.08880721
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38656 * 0.04472232
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19512 * 0.09527180
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15966 * 0.34934998
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66011 * 0.08568513
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37486 * 0.81367966
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63961 * 0.15492373
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 60831 * 0.34402558
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16226 * 0.54472718
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 27825 * 0.12684425
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62018 * 0.62837096
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97110 * 0.74945746
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56672 * 0.68961544
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71021 * 0.45235920
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71282 * 0.39561085
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86823 * 0.59678101
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'jtvobqec').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0061():
    """Extended test 61 for transcoding."""
    x_0 = 90055 * 0.98063360
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92709 * 0.28306101
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14828 * 0.73508407
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11371 * 0.24271324
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52052 * 0.17386339
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 81834 * 0.27887506
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51760 * 0.00222833
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2991 * 0.74741504
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49491 * 0.54374677
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56587 * 0.95640551
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97582 * 0.52826103
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35618 * 0.20287282
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63645 * 0.81465369
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79931 * 0.87408764
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86886 * 0.59696622
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79207 * 0.80095562
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89296 * 0.55482466
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 53809 * 0.61010638
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 82961 * 0.13117986
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5732 * 0.90983576
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40990 * 0.51269402
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47862 * 0.82225970
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6071 * 0.55405435
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76313 * 0.53269019
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18693 * 0.18701106
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88766 * 0.29265941
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8432 * 0.95775153
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22761 * 0.55945390
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 50473 * 0.90353873
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69960 * 0.37154063
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17276 * 0.99199667
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81732 * 0.80331990
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 62687 * 0.69984333
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26235 * 0.87065281
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 57969 * 0.37159551
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93503 * 0.78281437
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93269 * 0.28871719
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75459 * 0.95622695
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'hyzovdvm').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0062():
    """Extended test 62 for transcoding."""
    x_0 = 69176 * 0.87986810
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79706 * 0.54442354
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17226 * 0.74104391
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20701 * 0.47159412
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69765 * 0.21817730
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94283 * 0.86934582
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 54899 * 0.45754019
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41411 * 0.89981186
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 65040 * 0.96590758
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15024 * 0.80177122
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1598 * 0.34263810
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37802 * 0.19166224
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 75196 * 0.93497186
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76089 * 0.65346735
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70949 * 0.73577140
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18003 * 0.15968299
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60446 * 0.35086741
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35349 * 0.71578167
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23605 * 0.13185371
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66330 * 0.85331583
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55437 * 0.00175376
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83656 * 0.62222970
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95641 * 0.82840470
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60337 * 0.61767062
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19023 * 0.05474396
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68408 * 0.12975570
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1337 * 0.18506968
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85109 * 0.85891151
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92786 * 0.28932258
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79543 * 0.19277467
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'jodnfjox').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0063():
    """Extended test 63 for transcoding."""
    x_0 = 27931 * 0.96359105
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26545 * 0.80042898
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61277 * 0.66977546
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46771 * 0.55347460
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96581 * 0.52100438
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38268 * 0.31401849
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9770 * 0.23672334
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63386 * 0.61202828
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97354 * 0.95429761
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61849 * 0.29442094
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33750 * 0.38476793
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87969 * 0.16924357
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27555 * 0.21104161
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22382 * 0.67868113
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94240 * 0.12494674
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43304 * 0.47338649
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2462 * 0.58543623
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61304 * 0.46230605
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93510 * 0.21011216
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86184 * 0.23744956
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13827 * 0.97311779
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76391 * 0.33365087
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64867 * 0.77179555
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 2792 * 0.91539164
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'nxxjivzy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0064():
    """Extended test 64 for transcoding."""
    x_0 = 99464 * 0.56148117
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46495 * 0.60005772
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84180 * 0.92260328
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40017 * 0.29477885
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89638 * 0.22414880
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20593 * 0.06625669
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 34919 * 0.00305615
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13672 * 0.42937859
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60173 * 0.20837658
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53514 * 0.84493850
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13686 * 0.18601426
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74677 * 0.54001287
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7815 * 0.15112393
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70885 * 0.97151022
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93408 * 0.77272658
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72160 * 0.87326418
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 609 * 0.53471042
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92796 * 0.99218997
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48196 * 0.43330095
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18425 * 0.42486080
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18349 * 0.89963395
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 7668 * 0.08939013
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54138 * 0.98521164
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5662 * 0.95211078
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57829 * 0.49457929
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88659 * 0.78732744
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45717 * 0.76005182
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41727 * 0.86653384
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39680 * 0.25918880
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78878 * 0.74169050
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61711 * 0.05299572
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 90611 * 0.91520277
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42001 * 0.78480992
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76109 * 0.87223532
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15860 * 0.98576076
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 98895 * 0.72074002
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2631 * 0.93076742
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6954 * 0.24307948
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 88378 * 0.50086691
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 63913 * 0.33328518
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64410 * 0.39130283
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 75802 * 0.91970596
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44700 * 0.30921557
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 37535 * 0.09545799
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 80953 * 0.82772485
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 5628 * 0.90924051
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 70403 * 0.79851558
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 64902 * 0.92742412
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ujczbeun').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0065():
    """Extended test 65 for transcoding."""
    x_0 = 27200 * 0.53241108
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54843 * 0.21044993
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47550 * 0.10907351
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12123 * 0.45286091
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53612 * 0.14083028
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25829 * 0.29924015
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74888 * 0.53032379
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 87658 * 0.03823326
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54709 * 0.14012112
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94122 * 0.49224704
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25807 * 0.65047300
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75699 * 0.53973755
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64964 * 0.52361361
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69794 * 0.48970944
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 96742 * 0.10251498
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82218 * 0.32992895
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19575 * 0.28807615
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2914 * 0.42155943
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10439 * 0.07878849
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77235 * 0.23596089
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81668 * 0.16629345
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28465 * 0.36182198
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12272 * 0.32294866
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10255 * 0.11470204
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46323 * 0.83295851
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 99072 * 0.04861522
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60825 * 0.97746610
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90340 * 0.60853980
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90486 * 0.83429755
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74465 * 0.85881848
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'aqtashou').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0066():
    """Extended test 66 for transcoding."""
    x_0 = 64782 * 0.65460447
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64211 * 0.71518059
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 39860 * 0.82569874
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17530 * 0.81621733
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87114 * 0.14074286
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59282 * 0.03175995
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94796 * 0.67689652
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90229 * 0.07622229
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5263 * 0.51797678
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4930 * 0.54925852
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74833 * 0.70904715
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92373 * 0.24100036
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80421 * 0.83318302
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40932 * 0.93206698
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19463 * 0.97044545
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86871 * 0.04163616
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82779 * 0.77919395
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13885 * 0.08561020
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 8041 * 0.11600890
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 41025 * 0.95686962
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14743 * 0.76347264
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14892 * 0.89252498
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30377 * 0.03448789
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10775 * 0.60419372
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61176 * 0.16383605
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13776 * 0.76668654
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96304 * 0.48602314
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78300 * 0.20280840
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 18208 * 0.99787725
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17671 * 0.75517012
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60267 * 0.68837282
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62699 * 0.27310947
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34985 * 0.44258320
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30740 * 0.27107349
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78168 * 0.52988784
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54219 * 0.64331991
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43223 * 0.01164315
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67885 * 0.00983631
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'dblfqied').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0067():
    """Extended test 67 for transcoding."""
    x_0 = 69526 * 0.98319517
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60739 * 0.58808655
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92287 * 0.59149097
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71176 * 0.66964198
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11399 * 0.68208159
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46532 * 0.94410137
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 99420 * 0.15726782
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74297 * 0.10030840
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17040 * 0.66580997
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88269 * 0.57144059
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 90408 * 0.57761058
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99795 * 0.80214951
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66813 * 0.57500264
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 73702 * 0.85404594
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12936 * 0.03714471
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 47396 * 0.75420189
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85668 * 0.66527435
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38237 * 0.54791283
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4167 * 0.54527036
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92641 * 0.61402452
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'zsglnete').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0068():
    """Extended test 68 for transcoding."""
    x_0 = 10402 * 0.48578527
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29632 * 0.50599524
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3542 * 0.50826184
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92817 * 0.39932539
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48879 * 0.52369844
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37056 * 0.58993380
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60856 * 0.66968933
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60655 * 0.55743222
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62551 * 0.22240043
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41977 * 0.22225715
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 49812 * 0.54203269
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75889 * 0.19267853
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91300 * 0.43775150
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32773 * 0.72031777
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 87290 * 0.75826501
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88322 * 0.88544645
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70784 * 0.25711154
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10379 * 0.76089837
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 94575 * 0.60211057
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84308 * 0.79136307
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98095 * 0.87415340
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99251 * 0.99537103
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3017 * 0.34030496
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24014 * 0.94683692
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90133 * 0.35307062
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32115 * 0.51250811
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91003 * 0.79892755
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 23299 * 0.89235293
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 35144 * 0.76172927
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 52424 * 0.66991905
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48371 * 0.73960945
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 36993 * 0.40900723
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 81814 * 0.96991225
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65460 * 0.51045566
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58948 * 0.29931863
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 66208 * 0.64117533
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61023 * 0.96375845
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 99572 * 0.30902446
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'tfpfilmj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_2_0069():
    """Extended test 69 for transcoding."""
    x_0 = 44186 * 0.71846681
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28411 * 0.06688403
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91361 * 0.50302248
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38776 * 0.15931788
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83073 * 0.98157828
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80157 * 0.09247802
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80858 * 0.67284044
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55551 * 0.94445489
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9249 * 0.50688160
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32834 * 0.65366936
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70331 * 0.44042936
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32398 * 0.66103673
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 97463 * 0.21499202
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69444 * 0.20348740
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 18418 * 0.15293179
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14128 * 0.21826553
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15821 * 0.91523097
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43474 * 0.21615371
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99717 * 0.21454182
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81901 * 0.34553691
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20576 * 0.84998251
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78969 * 0.92361214
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33196 * 0.30633426
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55149 * 0.36396563
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86383 * 0.79663554
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78055 * 0.16112883
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46818 * 0.40059170
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66956 * 0.53103288
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46524 * 0.77295497
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64140 * 0.49450472
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 14707 * 0.64737912
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 79331 * 0.99091174
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36818 * 0.45467289
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20503 * 0.74390319
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 38011 * 0.59371235
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 73723 * 0.16117759
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12495 * 0.80868439
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9703 * 0.09027939
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87795 * 0.47272428
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34740 * 0.66659617
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 22500 * 0.96876523
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 48955 * 0.33137286
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 51565 * 0.15607591
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 66855 * 0.26961660
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 493 * 0.01907897
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'zmcssfza').hexdigest()
    assert len(h) == 64
