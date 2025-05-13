"""Extended tests for aggregation suite 4."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_aggregation_extended_4_0000():
    """Extended test 0 for aggregation."""
    x_0 = 66813 * 0.32701965
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23737 * 0.74448573
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52124 * 0.03449794
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99022 * 0.79931432
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4529 * 0.16782569
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95390 * 0.03550826
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93539 * 0.68635746
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89553 * 0.88877243
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19167 * 0.55991476
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67179 * 0.04870468
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39602 * 0.79696445
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24088 * 0.98934667
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 14013 * 0.71105456
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93136 * 0.82088069
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26893 * 0.25274528
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89758 * 0.76859311
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80555 * 0.44218082
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 18867 * 0.86448258
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68160 * 0.42711860
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33398 * 0.78297522
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65601 * 0.20082870
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75708 * 0.26443640
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 42366 * 0.79635322
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50947 * 0.76001676
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98066 * 0.40143352
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10916 * 0.38370733
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48925 * 0.91256859
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24588 * 0.64238847
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62033 * 0.55994757
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38381 * 0.79865380
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6165 * 0.53435755
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 92519 * 0.12461952
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 99844 * 0.91925547
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 20518 * 0.96011511
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 20166 * 0.31297728
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24275 * 0.44934815
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31499 * 0.36055133
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22506 * 0.22630753
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59046 * 0.66281196
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'yrzlpbsd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0001():
    """Extended test 1 for aggregation."""
    x_0 = 38123 * 0.86482951
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56246 * 0.08954226
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12597 * 0.67841644
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36726 * 0.36241752
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45896 * 0.81220271
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6776 * 0.54090429
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89551 * 0.95809458
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36448 * 0.56269460
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 308 * 0.01426003
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25721 * 0.35192673
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34734 * 0.21117658
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35699 * 0.92800754
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6998 * 0.16374782
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21458 * 0.96119167
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34938 * 0.21914870
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94074 * 0.74410691
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26871 * 0.09372350
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 57767 * 0.69311467
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 58957 * 0.31563277
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73220 * 0.89945784
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65092 * 0.68732231
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68904 * 0.21154047
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10359 * 0.77360992
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61587 * 0.20073589
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93258 * 0.75952465
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16568 * 0.95384617
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 25947 * 0.49382724
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22794 * 0.54232796
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43008 * 0.99303563
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 94693 * 0.29982428
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56524 * 0.05137618
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87444 * 0.76519912
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 42390 * 0.03995498
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 42275 * 0.29300205
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15065 * 0.75451838
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24907 * 0.13673315
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30299 * 0.67337514
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 61655 * 0.82733306
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66336 * 0.11939825
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 29997 * 0.33219483
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 77486 * 0.73687049
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'wshuesdh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0002():
    """Extended test 2 for aggregation."""
    x_0 = 41498 * 0.63573805
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89036 * 0.20505192
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11755 * 0.29089750
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26082 * 0.71828582
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89192 * 0.42213305
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60840 * 0.02262940
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87065 * 0.81289517
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72733 * 0.92630750
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64008 * 0.51647447
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 22690 * 0.60249248
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83943 * 0.84971889
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26779 * 0.24203360
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 85596 * 0.78795856
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87460 * 0.30481721
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66213 * 0.33779304
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94006 * 0.51730819
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18089 * 0.75038020
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87405 * 0.50617237
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25987 * 0.62165308
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63302 * 0.51670409
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88791 * 0.76968943
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61976 * 0.22955093
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90627 * 0.82007855
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67571 * 0.38604003
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83025 * 0.88029640
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 34424 * 0.21939590
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6345 * 0.80829131
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56702 * 0.16494805
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 56994 * 0.94417370
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82791 * 0.69304055
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48152 * 0.43982133
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 80702 * 0.67666049
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47909 * 0.44032127
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'mwsvyice').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0003():
    """Extended test 3 for aggregation."""
    x_0 = 65028 * 0.53418724
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58755 * 0.30970902
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81021 * 0.62649688
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 19308 * 0.38629041
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 65104 * 0.62409316
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47612 * 0.03729523
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19075 * 0.02518418
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29835 * 0.53524149
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95094 * 0.84961287
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 10717 * 0.24312835
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59943 * 0.74321592
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9920 * 0.69580473
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24271 * 0.22094741
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23841 * 0.16430314
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64195 * 0.47387682
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1830 * 0.40800794
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63700 * 0.69701795
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69336 * 0.06199828
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7638 * 0.44537413
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73983 * 0.15241331
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16535 * 0.99933808
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61487 * 0.04911548
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61979 * 0.72130512
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18414 * 0.15896559
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2586 * 0.01539960
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 41283 * 0.87365354
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 49010 * 0.79437579
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 39700 * 0.81620653
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58755 * 0.34710860
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71106 * 0.79215756
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16387 * 0.10861607
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52243 * 0.28534088
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82726 * 0.10769679
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 75778 * 0.02939903
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60498 * 0.35466111
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29818 * 0.55649767
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41740 * 0.35594997
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 30500 * 0.51015746
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59242 * 0.87904158
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 50532 * 0.78255503
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 4547 * 0.32661179
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 28213 * 0.97028807
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 80913 * 0.17814456
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 941 * 0.27970919
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 41866 * 0.98873686
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 70332 * 0.54111457
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 1244 * 0.93286163
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 98788 * 0.82092161
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 87926 * 0.25912534
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 15962 * 0.69358576
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'axakazgp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0004():
    """Extended test 4 for aggregation."""
    x_0 = 64679 * 0.27862993
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2894 * 0.89873113
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30468 * 0.66426098
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69365 * 0.28733202
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6720 * 0.96709833
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41068 * 0.65137178
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83500 * 0.36426283
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61282 * 0.41713466
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89474 * 0.88886239
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 94147 * 0.32730123
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76517 * 0.90575152
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23380 * 0.25566000
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24594 * 0.48214672
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62037 * 0.67355518
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24686 * 0.58624589
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38766 * 0.40481151
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75362 * 0.56359593
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 75210 * 0.11556955
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96143 * 0.06784980
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38279 * 0.53701701
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 59264 * 0.29354707
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61173 * 0.32334273
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86323 * 0.36241269
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21302 * 0.95015298
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 26129 * 0.31101594
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42102 * 0.79760531
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17119 * 0.66834893
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 63701 * 0.63900347
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69698 * 0.60631613
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93034 * 0.69237387
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 22481 * 0.47185160
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25930 * 0.73159918
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 70410 * 0.19642126
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95342 * 0.91495935
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 39490 * 0.95739750
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'bemcibcc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0005():
    """Extended test 5 for aggregation."""
    x_0 = 10238 * 0.33912017
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43288 * 0.85788505
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50365 * 0.57749895
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29259 * 0.62235389
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94776 * 0.26444067
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75383 * 0.33860456
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18705 * 0.66583751
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45165 * 0.67940692
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72442 * 0.71017511
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 8130 * 0.79752040
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88344 * 0.33855071
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 85724 * 0.48665046
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5124 * 0.82454693
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11789 * 0.99572496
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88122 * 0.16361552
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2204 * 0.05799933
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4091 * 0.66958485
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25453 * 0.18191454
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54965 * 0.41650688
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 88174 * 0.47732449
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87570 * 0.54129261
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35402 * 0.25289076
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63139 * 0.76213758
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57708 * 0.22068163
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'hharyqgg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0006():
    """Extended test 6 for aggregation."""
    x_0 = 39423 * 0.09359598
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57905 * 0.22036824
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33786 * 0.89133005
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30840 * 0.01658931
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18004 * 0.49925703
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75805 * 0.10151507
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3670 * 0.63900810
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4587 * 0.90621166
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33713 * 0.90246491
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44039 * 0.77407359
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92225 * 0.09402279
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46881 * 0.52712330
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73291 * 0.46098564
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47838 * 0.51863126
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 68845 * 0.03276136
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 7811 * 0.34651819
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99171 * 0.07645875
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62858 * 0.89114020
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39997 * 0.70167278
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58867 * 0.44300907
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32713 * 0.96101113
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37263 * 0.40942821
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83551 * 0.93337351
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87687 * 0.19176924
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 88328 * 0.17035456
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38377 * 0.61691215
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35782 * 0.68542350
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74218 * 0.31695345
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'bxhkblhu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0007():
    """Extended test 7 for aggregation."""
    x_0 = 17161 * 0.52437874
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 37619 * 0.30067939
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37966 * 0.50810376
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1211 * 0.71589225
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 98668 * 0.72872336
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48131 * 0.90246733
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1675 * 0.51721023
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22012 * 0.44234452
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22341 * 0.67904554
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93944 * 0.70550682
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79558 * 0.18977907
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19994 * 0.21581474
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3816 * 0.71585756
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25796 * 0.75134246
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 59358 * 0.78755018
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78835 * 0.48687929
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39948 * 0.23604975
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 8429 * 0.80463729
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95721 * 0.67669867
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 13078 * 0.50042160
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85103 * 0.69034484
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74085 * 0.96470686
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 36903 * 0.09552315
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 33583 * 0.81548063
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63165 * 0.23000491
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 67239 * 0.19713061
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87156 * 0.78913823
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 6086 * 0.82076217
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79311 * 0.83917033
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55238 * 0.43105905
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 94545 * 0.73678834
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78513 * 0.50866285
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24007 * 0.94533442
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48176 * 0.40449071
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56354 * 0.49287399
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25048 * 0.53180898
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 99983 * 0.32085577
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98290 * 0.80151080
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 68517 * 0.39960597
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ajtenaua').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0008():
    """Extended test 8 for aggregation."""
    x_0 = 5744 * 0.43317997
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16579 * 0.30007510
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32513 * 0.23613494
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45635 * 0.13319666
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66253 * 0.02498186
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50483 * 0.05537989
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89764 * 0.65065671
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10056 * 0.23533239
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21477 * 0.79982862
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32927 * 0.09630763
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53884 * 0.89254231
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11979 * 0.65922383
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42610 * 0.74636595
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98520 * 0.46161261
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7729 * 0.87076582
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87495 * 0.75668302
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 70002 * 0.67189999
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62706 * 0.52807167
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56392 * 0.98475689
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37851 * 0.03489074
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95299 * 0.68298118
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91006 * 0.51790910
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14718 * 0.38964301
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 11864 * 0.26737945
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77323 * 0.26646975
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 82703 * 0.16692027
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46772 * 0.74425207
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21711 * 0.19451437
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95769 * 0.38305124
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10687 * 0.59985619
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36061 * 0.18848552
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27901 * 0.22978581
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 634 * 0.88458464
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57524 * 0.44958684
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41824 * 0.64382333
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60892 * 0.31164476
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58774 * 0.99006573
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71816 * 0.62941750
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 71766 * 0.03858411
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 55737 * 0.90087579
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 87501 * 0.32708598
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 15213 * 0.99155624
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 31660 * 0.11697761
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 91230 * 0.00222037
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 11130 * 0.60006253
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 26831 * 0.11247385
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 21109 * 0.86448718
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 13731 * 0.61718195
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'nrhtnzrg').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0009():
    """Extended test 9 for aggregation."""
    x_0 = 92863 * 0.55520011
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47616 * 0.17717347
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64594 * 0.90125858
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61253 * 0.02863225
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18320 * 0.15075853
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 66014 * 0.67668309
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57737 * 0.96264690
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3151 * 0.93216980
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 64373 * 0.66452654
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4239 * 0.33280857
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33756 * 0.25551401
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22656 * 0.08011025
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46869 * 0.24369760
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15295 * 0.60150944
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94610 * 0.89914028
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8347 * 0.32552492
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 722 * 0.54001635
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73548 * 0.21644422
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98866 * 0.54064578
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80889 * 0.15141322
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53674 * 0.54054877
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12443 * 0.95821656
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69706 * 0.91814050
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68439 * 0.62497827
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'nuejrari').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0010():
    """Extended test 10 for aggregation."""
    x_0 = 80330 * 0.44199928
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 18331 * 0.50907660
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33197 * 0.54523036
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17468 * 0.04469379
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53359 * 0.46657319
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17666 * 0.91767671
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39878 * 0.67766210
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46789 * 0.22694655
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93306 * 0.78248694
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27161 * 0.81923495
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64836 * 0.48869398
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29585 * 0.19479904
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33791 * 0.41184477
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 20856 * 0.98650452
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81975 * 0.29903380
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21992 * 0.73382085
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44790 * 0.50422366
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98355 * 0.00195062
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9597 * 0.22016691
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77309 * 0.89026789
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21087 * 0.91386187
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66211 * 0.52163919
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 2539 * 0.69243356
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17283 * 0.72309505
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37155 * 0.19434024
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28045 * 0.91846315
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 89848 * 0.33754824
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14003 * 0.43708162
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75110 * 0.39507992
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36976 * 0.50776117
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88295 * 0.82143367
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82163 * 0.26478028
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64227 * 0.24093942
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 30094 * 0.78457782
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56227 * 0.03831560
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 8579 * 0.78006649
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 14957 * 0.97017484
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 5399 * 0.03719770
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 56873 * 0.19849900
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 66568 * 0.52914348
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32674 * 0.60842736
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 46048 * 0.59708948
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79146 * 0.87938888
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 70889 * 0.21858600
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 51948 * 0.73547739
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 12828 * 0.62739692
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 84259 * 0.00999890
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 65496 * 0.75712348
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 3860 * 0.25112977
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'sxgjvbwd').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0011():
    """Extended test 11 for aggregation."""
    x_0 = 31290 * 0.00558635
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45816 * 0.69119193
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29910 * 0.64005285
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 16591 * 0.84474505
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67808 * 0.92032999
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44663 * 0.95201304
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 57535 * 0.39829658
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38370 * 0.57679673
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 846 * 0.08014580
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90553 * 0.86635719
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74359 * 0.62549862
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17568 * 0.62374504
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 11018 * 0.26555686
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26450 * 0.75624188
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71745 * 0.42022774
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80248 * 0.92936283
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94586 * 0.08805962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 48846 * 0.44158252
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74764 * 0.04092443
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50380 * 0.99558251
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32666 * 0.21567861
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70781 * 0.17318287
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37373 * 0.89320144
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74681 * 0.01413804
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69950 * 0.40314662
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28691 * 0.33016581
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14671 * 0.67526279
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89684 * 0.04687040
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12111 * 0.71294005
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 42597 * 0.87151737
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54110 * 0.37721883
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63742 * 0.78883067
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 26553 * 0.02849879
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66857 * 0.95306960
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14941 * 0.04626822
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 58169 * 0.80288933
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22537 * 0.06232639
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64831 * 0.95177287
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74459 * 0.74959941
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2416 * 0.34563528
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 45154 * 0.83264079
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63461 * 0.07753482
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9100 * 0.74679661
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ywipngrt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0012():
    """Extended test 12 for aggregation."""
    x_0 = 58827 * 0.15501683
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41883 * 0.73982160
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86008 * 0.04301290
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 83182 * 0.08373708
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45103 * 0.44909652
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70202 * 0.03009107
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20951 * 0.86687140
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79161 * 0.55924445
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21484 * 0.56157598
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2661 * 0.76157179
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54819 * 0.45808621
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59339 * 0.67638489
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69192 * 0.54617582
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6728 * 0.12702375
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38613 * 0.45304629
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72318 * 0.15049874
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75317 * 0.49475600
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68747 * 0.53754951
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50156 * 0.71102717
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67445 * 0.59529352
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18145 * 0.75553298
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50982 * 0.16387396
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 61023 * 0.96409790
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27039 * 0.85581346
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90175 * 0.58045347
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70169 * 0.39694518
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6144 * 0.18320721
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35757 * 0.81086398
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76529 * 0.72384789
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17090 * 0.97648867
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28138 * 0.79557768
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1531 * 0.49377894
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58272 * 0.00300255
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9599 * 0.73815187
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63203 * 0.77392151
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70529 * 0.68992043
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12379 * 0.51407830
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10997 * 0.97540576
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16766 * 0.80175264
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14774 * 0.69019898
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 96913 * 0.18675506
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 60515 * 0.97447020
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 76106 * 0.44234860
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 2421 * 0.10579142
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 39790 * 0.48557799
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'dbkkblhr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0013():
    """Extended test 13 for aggregation."""
    x_0 = 12798 * 0.11623796
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 34708 * 0.13475240
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51164 * 0.10809828
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68321 * 0.18419044
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11577 * 0.11199517
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 5910 * 0.64648761
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 19486 * 0.01367174
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67932 * 0.27230359
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6842 * 0.73590754
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92623 * 0.02389502
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76364 * 0.03063771
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 97635 * 0.00884535
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 80371 * 0.84088739
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34798 * 0.98467436
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 1607 * 0.63898496
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9756 * 0.50395459
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25542 * 0.72475124
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 2492 * 0.47654434
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93030 * 0.80512358
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22631 * 0.20099970
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3559 * 0.65987920
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78925 * 0.34263954
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25368 * 0.17628672
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78096 * 0.24540932
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 53682 * 0.20239719
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'yfrzvzis').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0014():
    """Extended test 14 for aggregation."""
    x_0 = 58816 * 0.11669950
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98512 * 0.17359575
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21481 * 0.27623377
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7305 * 0.29703898
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 48355 * 0.87277390
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71404 * 0.59201450
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48188 * 0.25121164
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 12352 * 0.68709842
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 82022 * 0.88706829
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81878 * 0.15285566
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32793 * 0.08854662
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 74204 * 0.31515394
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8157 * 0.37882535
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1897 * 0.22996335
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44544 * 0.37481894
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76985 * 0.52663260
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42182 * 0.31817910
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89039 * 0.98671085
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87113 * 0.52475716
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35324 * 0.79268523
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66300 * 0.77807843
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49009 * 0.64214314
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9538 * 0.18716224
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7238 * 0.00732146
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 41348 * 0.52782331
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50726 * 0.06102011
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72945 * 0.55039352
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90626 * 0.19476575
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64056 * 0.21450825
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81838 * 0.45660888
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 78453 * 0.97157281
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10292 * 0.67572530
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28611 * 0.80829815
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 55134 * 0.67442013
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1731 * 0.14770909
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 45323 * 0.59226439
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90308 * 0.87221308
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 62504 * 0.46317436
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 11451 * 0.19678742
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'gzwuzsek').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0015():
    """Extended test 15 for aggregation."""
    x_0 = 63650 * 0.66805157
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26151 * 0.21491975
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 76943 * 0.95001274
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27345 * 0.43820790
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76946 * 0.94147801
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 57180 * 0.77733723
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88604 * 0.43175196
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 6539 * 0.15661822
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1838 * 0.08161854
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40787 * 0.30416383
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 42095 * 0.16705028
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 7968 * 0.69934968
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72203 * 0.16075812
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74291 * 0.30586493
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8432 * 0.52393213
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20390 * 0.02450152
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40486 * 0.06851646
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93707 * 0.01603217
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78354 * 0.16266603
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24848 * 0.53992634
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95935 * 0.73329792
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19062 * 0.99309935
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30494 * 0.73737040
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27672 * 0.85732955
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 51233 * 0.32664585
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4941 * 0.25920888
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65557 * 0.05950378
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 5278 * 0.05273735
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 68295 * 0.01053871
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25775 * 0.87576673
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72116 * 0.86256794
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89058 * 0.22965239
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 46583 * 0.83665489
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91656 * 0.66940835
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29384 * 0.68268015
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48774 * 0.59231595
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23536 * 0.21261945
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98615 * 0.72648702
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51333 * 0.90278183
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10855 * 0.57071184
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79377 * 0.44188395
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 500 * 0.87268603
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11424 * 0.80423137
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 12069 * 0.88160625
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17222 * 0.80033378
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 19709 * 0.63792198
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 57623 * 0.18459550
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 6824 * 0.65698745
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 497 * 0.81957552
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 93829 * 0.32319089
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'lyudnxpn').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0016():
    """Extended test 16 for aggregation."""
    x_0 = 58539 * 0.38265414
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8180 * 0.09673695
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85700 * 0.74093391
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82794 * 0.85287883
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11141 * 0.37847549
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42938 * 0.23784184
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6745 * 0.52798648
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14485 * 0.29894871
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13789 * 0.63829867
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20134 * 0.23467689
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21744 * 0.76174318
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23905 * 0.47791689
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98132 * 0.44237621
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76248 * 0.49289650
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 40371 * 0.06249276
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97644 * 0.06141331
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61796 * 0.51678699
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98965 * 0.37432816
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63463 * 0.80524218
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75668 * 0.80252456
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76345 * 0.82817116
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 42271 * 0.98211453
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48876 * 0.37007185
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66447 * 0.11475667
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57139 * 0.02208947
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33921 * 0.99924152
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98060 * 0.87312535
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29723 * 0.14813496
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49114 * 0.73887482
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59445 * 0.48454786
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 25326 * 0.36522315
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91001 * 0.01137324
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36177 * 0.51572065
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66854 * 0.28298397
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34341 * 0.30192017
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37040 * 0.71953699
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83788 * 0.98942648
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74641 * 0.95389241
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21090 * 0.36320364
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94795 * 0.35852346
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 66720 * 0.19888356
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50788 * 0.13365139
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 50933 * 0.87175176
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'owgeguyu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0017():
    """Extended test 17 for aggregation."""
    x_0 = 59942 * 0.79981556
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19357 * 0.10395521
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 48073 * 0.61110575
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60186 * 0.43682715
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66655 * 0.55457635
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70585 * 0.47286607
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70208 * 0.31979149
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92448 * 0.43210226
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9461 * 0.28816327
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39001 * 0.95257631
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63397 * 0.28091224
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17314 * 0.87355140
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 22608 * 0.06695093
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51858 * 0.02019363
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20423 * 0.46590785
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89193 * 0.68599840
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 66469 * 0.38617212
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64420 * 0.70937704
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30501 * 0.53845496
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10952 * 0.36249743
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 38969 * 0.07164324
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91248 * 0.93254695
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38959 * 0.97525247
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85245 * 0.01269560
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47079 * 0.07330505
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92259 * 0.84903194
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 87816 * 0.17032549
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99086 * 0.53275397
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43450 * 0.91053788
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61958 * 0.24729953
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50253 * 0.41878132
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16422 * 0.57101219
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24090 * 0.31248825
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53573 * 0.43468337
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 66349 * 0.32802912
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71366 * 0.08014877
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31088 * 0.89007330
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86797 * 0.70651160
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83266 * 0.35017152
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'bvdndxuo').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0018():
    """Extended test 18 for aggregation."""
    x_0 = 61080 * 0.67371648
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12076 * 0.88726868
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37722 * 0.96640997
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55495 * 0.52686680
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9666 * 0.96402595
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56893 * 0.29517377
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65943 * 0.05131330
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31167 * 0.02059539
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76416 * 0.72210519
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42451 * 0.07175607
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43093 * 0.68611476
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 45493 * 0.87214475
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71764 * 0.39326576
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90756 * 0.03868011
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93541 * 0.71798621
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23401 * 0.31535101
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13694 * 0.31127360
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37949 * 0.95274654
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27769 * 0.43732810
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 603 * 0.38064164
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50386 * 0.84999739
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5986 * 0.73391000
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58650 * 0.36546881
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64460 * 0.52504228
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47335 * 0.54752303
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45749 * 0.66520724
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30355 * 0.47017270
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 42606 * 0.41045548
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39175 * 0.27460668
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48719 * 0.28689076
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11810 * 0.86166339
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59911 * 0.95765516
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47853 * 0.87978339
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60602 * 0.90384385
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 6066 * 0.62145585
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85060 * 0.81030997
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 60744 * 0.86549349
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4983 * 0.56602849
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86855 * 0.16309782
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 2499 * 0.79692412
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 71113 * 0.03879325
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 46749 * 0.26233448
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'mthnstwc').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0019():
    """Extended test 19 for aggregation."""
    x_0 = 89526 * 0.29388273
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57004 * 0.17494720
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27223 * 0.64896169
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6107 * 0.71137490
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34619 * 0.68482631
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53925 * 0.01929843
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12431 * 0.09534430
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23729 * 0.77907940
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77259 * 0.61884435
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 81212 * 0.63964396
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8884 * 0.36135758
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17248 * 0.46713956
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54531 * 0.03044221
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75293 * 0.78222074
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71810 * 0.58141055
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 5986 * 0.15622493
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9457 * 0.17280949
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83555 * 0.40372793
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27803 * 0.13133326
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 93313 * 0.60915800
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71499 * 0.75053956
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 78420 * 0.80165965
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1265 * 0.50193972
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85693 * 0.83479950
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99683 * 0.90885619
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 28927 * 0.00944603
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69620 * 0.59209302
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26 * 0.07602444
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'vpvkqpns').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0020():
    """Extended test 20 for aggregation."""
    x_0 = 18075 * 0.60914494
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68831 * 0.80902497
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74847 * 0.38475911
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54575 * 0.15146889
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22937 * 0.16356237
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83711 * 0.58086219
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37354 * 0.48334005
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 62814 * 0.60396129
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45201 * 0.93128961
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2210 * 0.90732135
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41674 * 0.41442009
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52526 * 0.87735344
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44048 * 0.93021121
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21714 * 0.84404631
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23910 * 0.97421739
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61035 * 0.76938113
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82274 * 0.32882479
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12989 * 0.48742859
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84696 * 0.47424223
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52593 * 0.84391529
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94797 * 0.81872873
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24835 * 0.43971415
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13317 * 0.62391294
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 35887 * 0.62950878
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84497 * 0.32878579
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42818 * 0.21115933
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71866 * 0.16916703
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49386 * 0.63397648
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 304 * 0.26643128
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71672 * 0.89904005
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 85986 * 0.07431379
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68214 * 0.77515657
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'rqbrejha').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0021():
    """Extended test 21 for aggregation."""
    x_0 = 74221 * 0.74841846
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86657 * 0.10692211
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 49106 * 0.14428621
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20002 * 0.64725348
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89897 * 0.21958265
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69121 * 0.82850793
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 77537 * 0.90549681
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 9983 * 0.85838638
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46720 * 0.41668724
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35062 * 0.48535017
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2878 * 0.55805822
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72318 * 0.62250525
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82378 * 0.87332618
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6267 * 0.20331079
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27713 * 0.56297242
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37539 * 0.92679728
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 29688 * 0.13140962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56335 * 0.79627789
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67839 * 0.15338526
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86883 * 0.92191486
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40710 * 0.65780087
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94972 * 0.63705294
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70427 * 0.60812603
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48957 * 0.60136100
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83555 * 0.47799024
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 227 * 0.72830873
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 29084 * 0.21767832
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78527 * 0.50004065
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 32072 * 0.99339175
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82722 * 0.24866786
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44098 * 0.09553607
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18902 * 0.47735777
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 84355 * 0.69584438
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97750 * 0.73879324
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 97756 * 0.11304505
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34464 * 0.49616718
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 72509 * 0.70327578
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84702 * 0.08698251
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28018 * 0.73430465
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 77030 * 0.35594402
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89021 * 0.16511049
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 76683 * 0.72339622
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 97894 * 0.51033572
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 62400 * 0.70280737
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 90630 * 0.00098977
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 85838 * 0.74953316
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17053 * 0.02031076
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 88787 * 0.97004752
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'sxzkcacb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0022():
    """Extended test 22 for aggregation."""
    x_0 = 19198 * 0.61739499
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67400 * 0.46619119
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77758 * 0.76014737
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84044 * 0.90609130
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18512 * 0.45241391
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65677 * 0.68487361
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73450 * 0.41723007
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13279 * 0.42261477
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80707 * 0.34499069
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 95243 * 0.57008958
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 46597 * 0.15400215
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92312 * 0.40201432
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 24929 * 0.72777910
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 41723 * 0.76058190
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98693 * 0.21907546
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57456 * 0.31991284
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 23285 * 0.48934076
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56620 * 0.03459727
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11916 * 0.81022304
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52047 * 0.65517893
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18914 * 0.35508108
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91309 * 0.85450937
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1738 * 0.93177116
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67549 * 0.86224866
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77282 * 0.25457656
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 64499 * 0.69940307
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82846 * 0.97785596
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69445 * 0.69606774
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92414 * 0.85440090
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56181 * 0.41577132
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 91254 * 0.32229179
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 12931 * 0.23544542
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58443 * 0.64522638
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28557 * 0.30650539
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 28231 * 0.53514206
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 78921 * 0.70652768
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62919 * 0.94193763
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18528 * 0.67803314
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16271 * 0.12261526
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80111 * 0.59977121
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37338 * 0.53084644
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85885 * 0.70407566
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 56443 * 0.44643257
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 83906 * 0.98302923
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 77330 * 0.37226048
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'myhnsnad').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0023():
    """Extended test 23 for aggregation."""
    x_0 = 67890 * 0.63059714
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98009 * 0.60467940
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70680 * 0.88687573
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70321 * 0.77810861
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 55473 * 0.32793399
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96187 * 0.82430317
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28496 * 0.58147941
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37986 * 0.75191195
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39460 * 0.76860329
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98114 * 0.56773265
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 19140 * 0.40769218
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54532 * 0.85927795
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10538 * 0.00967676
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5767 * 0.04406102
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45715 * 0.05222800
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 86711 * 0.86820248
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92886 * 0.89593088
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7423 * 0.41664770
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 42583 * 0.77450693
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64344 * 0.18460973
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75907 * 0.46591982
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76576 * 0.16705854
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16963 * 0.28060684
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7038 * 0.49384342
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31061 * 0.05905287
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43843 * 0.21375070
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22919 * 0.19524767
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84730 * 0.52881169
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39018 * 0.24300924
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10570 * 0.86652616
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48073 * 0.15132227
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'fzbbshra').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0024():
    """Extended test 24 for aggregation."""
    x_0 = 40876 * 0.44525272
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 29430 * 0.96208045
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66839 * 0.07925992
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21382 * 0.29394731
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 85053 * 0.57227277
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1960 * 0.52525526
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20115 * 0.30574854
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95015 * 0.54389314
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97027 * 0.87600972
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17742 * 0.84267139
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67218 * 0.97144490
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 22196 * 0.64969795
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45593 * 0.79517704
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55184 * 0.23773590
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56116 * 0.02370463
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20616 * 0.18471470
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92720 * 0.01945757
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 71980 * 0.27663712
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37597 * 0.71103291
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7187 * 0.77083971
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71255 * 0.34543885
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69995 * 0.88714752
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58034 * 0.73617558
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23487 * 0.53556951
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71845 * 0.80236715
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 70241 * 0.18036434
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 97062 * 0.73913492
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 83925 * 0.45519921
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41216 * 0.42821719
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22953 * 0.55495925
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12373 * 0.75176374
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33365 * 0.45221556
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25188 * 0.64025312
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86439 * 0.40422349
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11890 * 0.10562493
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25979 * 0.94358507
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 13058 * 0.62225988
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 99982 * 0.68177348
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 79951 * 0.85476074
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 14651 * 0.62229398
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 41542 * 0.79738525
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 89831 * 0.84590878
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1478 * 0.98142827
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 37473 * 0.67419438
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 1822 * 0.53726441
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 95246 * 0.97538624
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'tvudwmtm').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0025():
    """Extended test 25 for aggregation."""
    x_0 = 19284 * 0.98658755
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24614 * 0.39623468
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20011 * 0.04366037
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70557 * 0.39551462
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90226 * 0.72219556
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70697 * 0.68715811
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50613 * 0.96007381
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83560 * 0.04843765
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81513 * 0.70628064
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12514 * 0.72411043
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50931 * 0.84896421
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50395 * 0.34221801
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10684 * 0.81178685
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97210 * 0.12986559
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91630 * 0.53131905
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68014 * 0.42695505
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26744 * 0.86832728
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42616 * 0.08297447
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91872 * 0.01940030
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 67773 * 0.80326663
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53316 * 0.18756513
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31574 * 0.48309613
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 99261 * 0.83588389
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76697 * 0.08271284
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78089 * 0.29997187
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 87103 * 0.24376999
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 66235 * 0.01439881
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2012 * 0.34500457
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1710 * 0.61969547
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 97788 * 0.54167005
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52646 * 0.64020471
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7551 * 0.46187296
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24640 * 0.27667391
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 19610 * 0.08375963
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41185 * 0.82747606
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'ucsbhdxa').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0026():
    """Extended test 26 for aggregation."""
    x_0 = 76019 * 0.97301199
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73616 * 0.75353094
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84027 * 0.51659611
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87658 * 0.59993530
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1523 * 0.46747435
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74282 * 0.72579504
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12444 * 0.88753409
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 61763 * 0.94207888
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44459 * 0.30852788
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32129 * 0.95986705
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 59551 * 0.55035427
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96879 * 0.84761514
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31999 * 0.75518890
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40340 * 0.97496545
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 26853 * 0.19083589
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4007 * 0.09376119
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61423 * 0.88844657
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31446 * 0.79877198
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91982 * 0.60448589
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99270 * 0.29279750
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95393 * 0.06426290
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39145 * 0.56606579
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23067 * 0.01836453
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41236 * 0.96257453
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39904 * 0.86979252
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 31557 * 0.95369526
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98799 * 0.33487351
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 976 * 0.06748904
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6343 * 0.54797359
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 37527 * 0.37358236
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49523 * 0.61589454
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75263 * 0.07449290
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39896 * 0.77715739
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98177 * 0.21154185
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 45700 * 0.92918497
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 21189 * 0.29665567
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 78219 * 0.82576818
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 56553 * 0.63284322
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37085 * 0.35935630
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31370 * 0.64586295
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54614 * 0.24853935
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 59696 * 0.57872360
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 63741 * 0.23724046
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 26255 * 0.79890527
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 4849 * 0.72752123
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 81944 * 0.20724200
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'vbyidrlv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0027():
    """Extended test 27 for aggregation."""
    x_0 = 40552 * 0.34998065
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 45121 * 0.19174889
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 40368 * 0.80134132
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54711 * 0.45970531
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 68505 * 0.21708294
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51902 * 0.51966543
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36190 * 0.97823024
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39051 * 0.84829404
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70119 * 0.78826167
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38568 * 0.71329156
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98374 * 0.53102032
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51656 * 0.87354539
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35718 * 0.22637704
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50215 * 0.09441336
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92848 * 0.05219407
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97405 * 0.91593339
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75224 * 0.01352813
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14236 * 0.38601657
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19906 * 0.00208336
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79544 * 0.17397257
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 48955 * 0.13744005
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67504 * 0.50247824
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3105 * 0.67392082
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47860 * 0.63903155
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7120 * 0.42010476
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44142 * 0.24598177
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 46167 * 0.01316787
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4351 * 0.77753617
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 22870 * 0.81629731
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 24826 * 0.59204964
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12913 * 0.88183537
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 57517 * 0.08794909
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63532 * 0.96910806
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 65786 * 0.72790424
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 36156 * 0.46230893
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60401 * 0.92140045
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 248 * 0.33206838
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 71439 * 0.90588450
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'tbvuyanj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0028():
    """Extended test 28 for aggregation."""
    x_0 = 76983 * 0.34577150
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52892 * 0.07075044
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 8445 * 0.61806394
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44158 * 0.70845995
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80514 * 0.00855662
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 69840 * 0.76209263
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63035 * 0.95219662
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18455 * 0.04789924
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 84733 * 0.40729210
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99835 * 0.26149500
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85790 * 0.10691191
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95759 * 0.63562847
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95985 * 0.84800853
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47106 * 0.91770773
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98772 * 0.44449486
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96873 * 0.57499548
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5123 * 0.60788966
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86947 * 0.69530943
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95018 * 0.78709753
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 73222 * 0.30430461
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75103 * 0.15161443
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69283 * 0.67666464
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 32215 * 0.56713232
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31201 * 0.13106054
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'bemzwmzt').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0029():
    """Extended test 29 for aggregation."""
    x_0 = 98719 * 0.00256585
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 72684 * 0.67372603
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71395 * 0.90663652
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41613 * 0.56000460
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 45262 * 0.51387477
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70143 * 0.46177906
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31571 * 0.66188364
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79293 * 0.67363341
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52648 * 0.59961497
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99221 * 0.89512061
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50347 * 0.50847103
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88176 * 0.61793522
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87302 * 0.12592366
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72216 * 0.06624571
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 47859 * 0.94812289
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31727 * 0.35092046
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34760 * 0.39630873
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87597 * 0.59416552
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3224 * 0.75586026
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71103 * 0.50459074
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 13250 * 0.55743841
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36477 * 0.73135475
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85460 * 0.67537390
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82314 * 0.13105342
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54234 * 0.28807567
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35154 * 0.99971161
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 44888 * 0.07109363
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31493 * 0.30643499
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41962 * 0.88129950
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86474 * 0.21336651
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5977 * 0.88049770
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37377 * 0.45105306
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58795 * 0.48662577
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15441 * 0.23833527
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 46464 * 0.93591802
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6990 * 0.48382393
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 56795 * 0.06556094
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26747 * 0.09864312
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87493 * 0.42023172
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41911 * 0.86163277
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 69294 * 0.72806703
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 77884 * 0.13540043
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'wcxwjibr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0030():
    """Extended test 30 for aggregation."""
    x_0 = 87454 * 0.04193165
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67044 * 0.78555500
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 19044 * 0.96647735
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28425 * 0.73508994
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29257 * 0.95955898
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50996 * 0.09671911
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11841 * 0.29039106
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79620 * 0.66779803
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70754 * 0.51346774
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 82397 * 0.08705388
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80534 * 0.85843144
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82216 * 0.97660402
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66040 * 0.07589769
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78049 * 0.60662575
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11222 * 0.40729217
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99027 * 0.89838747
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84508 * 0.60843486
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83918 * 0.88876863
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90471 * 0.82187044
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92336 * 0.94724508
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43087 * 0.32711347
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72099 * 0.75948257
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85199 * 0.90820906
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21994 * 0.19404545
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 545 * 0.26034716
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11013 * 0.30709368
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13767 * 0.11116682
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59038 * 0.61215420
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93689 * 0.62265803
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39866 * 0.37485999
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42420 * 0.01746397
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 3784 * 0.53676644
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 399 * 0.35970156
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13356 * 0.21560118
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19872 * 0.76674440
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 6871 * 0.78810966
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12219 * 0.38353839
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 91700 * 0.47512535
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 84821 * 0.21405594
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 87922 * 0.94480537
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'nvtczezu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0031():
    """Extended test 31 for aggregation."""
    x_0 = 22873 * 0.29247542
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95523 * 0.81774093
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1539 * 0.29649561
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99779 * 0.58295536
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 49557 * 0.81576626
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64017 * 0.39578372
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30697 * 0.97884373
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45237 * 0.12411545
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35809 * 0.84018282
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55220 * 0.84772909
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1167 * 0.96543504
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 43105 * 0.90750689
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87098 * 0.44814525
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78255 * 0.83694397
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32661 * 0.90326093
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6535 * 0.66214300
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 50708 * 0.74341734
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95847 * 0.23978259
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22265 * 0.71578046
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30748 * 0.26663976
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 23187 * 0.05681769
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14410 * 0.62872805
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60260 * 0.69249541
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'btulkdnw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0032():
    """Extended test 32 for aggregation."""
    x_0 = 22204 * 0.66124485
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36525 * 0.17552925
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6056 * 0.30129040
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44093 * 0.93040106
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52706 * 0.16735230
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 88923 * 0.60870709
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25572 * 0.50145561
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58885 * 0.28258466
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 51719 * 0.48017267
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60841 * 0.03752777
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15328 * 0.59837943
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93754 * 0.43943620
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34341 * 0.78238975
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72569 * 0.97257706
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75406 * 0.34305622
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43269 * 0.09381637
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52298 * 0.32931291
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31630 * 0.44541744
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54629 * 0.13752704
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52619 * 0.62450264
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83892 * 0.47586883
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72349 * 0.72145871
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 57600 * 0.24350842
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93652 * 0.65146336
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19037 * 0.61499350
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76423 * 0.58906330
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5202 * 0.29075298
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 339 * 0.16084654
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 40596 * 0.69618124
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2814 * 0.74636977
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 24067 * 0.25692539
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25101 * 0.32870722
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18543 * 0.31053601
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17324 * 0.12531012
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 81265 * 0.49161045
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46131 * 0.07726147
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 70435 * 0.20991949
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36991 * 0.03181439
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 48196 * 0.51310648
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 16208 * 0.05167874
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 87082 * 0.76189881
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 48079 * 0.73402042
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 32504 * 0.63515055
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 32013 * 0.27730675
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10574 * 0.00002807
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 33691 * 0.88712028
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 86858 * 0.71863460
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 28089 * 0.32487637
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 9511 * 0.62379810
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 66811 * 0.18232852
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'qxvqliia').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0033():
    """Extended test 33 for aggregation."""
    x_0 = 5051 * 0.93390390
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32960 * 0.29353645
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28976 * 0.60765606
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 61603 * 0.73354209
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31180 * 0.83266878
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 3108 * 0.21788383
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 44334 * 0.98291968
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93540 * 0.63580088
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90263 * 0.81079946
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17799 * 0.92390244
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63881 * 0.81104218
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9623 * 0.60060013
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61777 * 0.19450739
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67963 * 0.83498245
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12780 * 0.42416699
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6189 * 0.65844300
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37405 * 0.07558853
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7463 * 0.89829059
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9843 * 0.86436538
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11606 * 0.31794392
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67498 * 0.55506850
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 19615 * 0.02611060
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83137 * 0.55966990
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86792 * 0.06528729
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75420 * 0.31516067
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56955 * 0.61917090
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56989 * 0.91913520
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11614 * 0.00408234
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65028 * 0.78992372
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34147 * 0.43213326
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 51049 * 0.09772950
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89385 * 0.08799277
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 77016 * 0.84681618
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99861 * 0.93547806
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9883 * 0.64744156
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60327 * 0.83156409
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55088 * 0.88046860
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 53482 * 0.72026906
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62219 * 0.69761028
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 51450 * 0.95832371
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84317 * 0.68046569
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72744 * 0.67437353
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 87551 * 0.51281380
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 93062 * 0.97947051
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 95458 * 0.51725023
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 17975 * 0.04166446
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 12964 * 0.15730439
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 22714 * 0.73228054
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 13395 * 0.39708132
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 597 * 0.07261256
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'dpdcufsu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0034():
    """Extended test 34 for aggregation."""
    x_0 = 81429 * 0.17390264
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38322 * 0.44048227
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30849 * 0.42149203
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90660 * 0.19150224
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57635 * 0.38476889
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72804 * 0.21951865
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 13593 * 0.63702484
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 95897 * 0.33973714
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81330 * 0.63254584
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 29221 * 0.15468099
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26834 * 0.91513853
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39240 * 0.97605857
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34749 * 0.22140207
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 95012 * 0.61911861
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 83110 * 0.67153137
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69233 * 0.83579314
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79569 * 0.68418129
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82888 * 0.65016870
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64708 * 0.90142964
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4562 * 0.55328154
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'yxxzncck').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0035():
    """Extended test 35 for aggregation."""
    x_0 = 50872 * 0.70930270
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65118 * 0.21150900
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 47561 * 0.75633254
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44385 * 0.49647310
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 80720 * 0.09645433
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46645 * 0.65058829
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89422 * 0.37918145
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42286 * 0.71484652
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67171 * 0.74508724
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57263 * 0.50686950
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16558 * 0.42326060
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2125 * 0.50325010
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3335 * 0.46345668
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96479 * 0.11740491
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37701 * 0.87260264
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42133 * 0.36256772
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24354 * 0.34233571
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 39579 * 0.45531484
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11759 * 0.29166425
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65289 * 0.72254319
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41549 * 0.43068170
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13469 * 0.38072009
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33699 * 0.28646023
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 8149 * 0.28265065
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50352 * 0.26265431
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66722 * 0.62693067
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41984 * 0.58401905
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82945 * 0.99749451
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34260 * 0.59658989
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69071 * 0.37562720
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71263 * 0.78221283
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 28917 * 0.70415723
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 43091 * 0.39938319
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 57075 * 0.43565539
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'akwasree').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0036():
    """Extended test 36 for aggregation."""
    x_0 = 89834 * 0.02275956
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27012 * 0.78803405
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92032 * 0.51810616
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7817 * 0.51259697
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96159 * 0.07403237
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47123 * 0.08954435
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20235 * 0.78429298
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86754 * 0.09341224
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25824 * 0.90228998
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64513 * 0.96392711
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 15429 * 0.49945472
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8093 * 0.54355557
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77307 * 0.51398147
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24459 * 0.07221707
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70064 * 0.71605705
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19847 * 0.31267516
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 9932 * 0.62183010
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67985 * 0.23006876
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27262 * 0.66807802
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60538 * 0.26350260
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33318 * 0.55861593
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94812 * 0.92931531
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88864 * 0.30804503
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86556 * 0.64498706
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73903 * 0.90130495
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43904 * 0.33427213
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8583 * 0.01144918
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65525 * 0.84663761
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91913 * 0.47179296
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 55993 * 0.40725320
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56198 * 0.02702662
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48468 * 0.80060538
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 24052 * 0.72242781
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98334 * 0.07601392
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1051 * 0.44058547
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 7936 * 0.35832423
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 71729 * 0.90750543
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74678 * 0.24856318
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44114 * 0.12880812
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 25048 * 0.23246309
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 86276 * 0.22757238
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 38362 * 0.15167958
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 1098 * 0.87026570
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 85863 * 0.14973627
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'wykkhqks').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0037():
    """Extended test 37 for aggregation."""
    x_0 = 34247 * 0.98930128
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58836 * 0.89539287
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4211 * 0.39131347
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35941 * 0.08868726
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 3800 * 0.23109091
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56831 * 0.72013777
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82967 * 0.49485116
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68507 * 0.15579216
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89690 * 0.91810963
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6141 * 0.45664327
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26723 * 0.77952830
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70311 * 0.86986212
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98318 * 0.12765435
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12113 * 0.18710831
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69638 * 0.91888552
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88225 * 0.97988424
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94660 * 0.96503310
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1920 * 0.73673296
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1077 * 0.42676796
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57442 * 0.66980362
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 4900 * 0.62092367
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21994 * 0.21885696
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7664 * 0.96563849
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10045 * 0.88012932
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 18879 * 0.17368187
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 74082 * 0.26430544
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12523 * 0.81326907
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3491 * 0.03781715
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90529 * 0.65373225
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 27001 * 0.80339440
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56820 * 0.03110316
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 15326 * 0.14143717
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 52373 * 0.20060597
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44087 * 0.50443927
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 75261 * 0.47090976
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57207 * 0.79429418
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84113 * 0.22302749
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 8056 * 0.64847900
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 87796 * 0.86149887
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72832 * 0.94973663
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 35997 * 0.98874934
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'cxsmycsp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0038():
    """Extended test 38 for aggregation."""
    x_0 = 24717 * 0.31503412
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41559 * 0.53023081
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74924 * 0.89136875
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 55936 * 0.50153423
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 404 * 0.72746321
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94673 * 0.71029939
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41548 * 0.70830086
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46705 * 0.31974487
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33028 * 0.59859492
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92664 * 0.92519294
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66310 * 0.83637637
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12524 * 0.58943888
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37010 * 0.22231649
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 38111 * 0.93583555
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16714 * 0.46514545
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17320 * 0.69685353
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17482 * 0.97057500
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33553 * 0.44609571
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52038 * 0.75787344
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 81080 * 0.58958109
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 95808 * 0.97586118
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83506 * 0.57838798
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48237 * 0.03065358
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15573 * 0.05902519
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50717 * 0.65740257
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24372 * 0.39803076
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 17473 * 0.24669113
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 7549 * 0.84113354
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39449 * 0.36540411
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3825 * 0.74490216
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'gztrdzmv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0039():
    """Extended test 39 for aggregation."""
    x_0 = 62802 * 0.91631285
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7604 * 0.51546187
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27310 * 0.74750726
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81322 * 0.59750592
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73151 * 0.76904379
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55787 * 0.26477605
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32032 * 0.67668343
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24769 * 0.09815112
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12939 * 0.61948422
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93824 * 0.55005800
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41911 * 0.43625095
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92860 * 0.16131438
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46350 * 0.21036383
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 26666 * 0.28223384
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73655 * 0.72398791
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94057 * 0.67058127
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60903 * 0.68685314
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82603 * 0.33789947
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98847 * 0.18681850
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79854 * 0.32536876
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85848 * 0.36445149
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98762 * 0.25368455
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19315 * 0.40516478
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87541 * 0.84342412
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89961 * 0.50703054
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10386 * 0.16792834
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 9305 * 0.84994454
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29937 * 0.70276827
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'fgncouwu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0040():
    """Extended test 40 for aggregation."""
    x_0 = 94847 * 0.33549591
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13480 * 0.56389906
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93800 * 0.53071374
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71766 * 0.20625823
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34468 * 0.34847683
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86675 * 0.76957084
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30894 * 0.65558335
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 853 * 0.66909624
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49248 * 0.40338825
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65018 * 0.26355039
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4939 * 0.34773712
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 11866 * 0.54428319
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69692 * 0.79276599
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31140 * 0.51905507
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79657 * 0.02707366
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75449 * 0.15684416
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32787 * 0.34803387
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21217 * 0.63227417
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 34900 * 0.38201258
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85229 * 0.97491608
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 34730 * 0.05811796
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24618 * 0.33419544
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7446 * 0.03656833
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87975 * 0.72173271
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83321 * 0.99940812
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 88284 * 0.28472961
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 48856 * 0.09712018
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82770 * 0.52180065
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 51720 * 0.76011243
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 58695 * 0.55716565
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53063 * 0.82203272
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4387 * 0.18949235
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12447 * 0.64661166
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 83479 * 0.71993783
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94672 * 0.52762060
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2996 * 0.49124197
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 34572 * 0.13793186
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 9189 * 0.30426855
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97873 * 0.33117235
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 73388 * 0.00316510
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89885 * 0.75942702
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 18199 * 0.73706183
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 56445 * 0.79727122
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 55470 * 0.89949669
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71498 * 0.32828540
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 30966 * 0.70081675
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 16168 * 0.34159485
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 47646 * 0.67674199
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 61683 * 0.78307878
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'gsvwssey').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0041():
    """Extended test 41 for aggregation."""
    x_0 = 48901 * 0.50294426
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86022 * 0.62855986
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 53339 * 0.31607100
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44920 * 0.54390841
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 82665 * 0.35119694
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52712 * 0.77762740
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63296 * 0.23366639
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21652 * 0.33812300
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48580 * 0.92013391
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19808 * 0.35074013
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 20051 * 0.89718986
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75757 * 0.61434539
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31501 * 0.68525683
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67916 * 0.29767189
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71756 * 0.25245469
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 10598 * 0.28763974
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25661 * 0.24258998
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 90457 * 0.90055702
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35466 * 0.11314682
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43694 * 0.18493167
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 99419 * 0.63917164
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50005 * 0.57740090
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66801 * 0.06458445
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63432 * 0.63952204
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 97599 * 0.97335629
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44920 * 0.92215127
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20097 * 0.62867282
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96661 * 0.23729164
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 20075 * 0.79972409
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 73684 * 0.79392144
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16203 * 0.53677909
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83676 * 0.60062710
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'nrpbykgr').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0042():
    """Extended test 42 for aggregation."""
    x_0 = 63687 * 0.15944341
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11127 * 0.24587418
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91231 * 0.03846145
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62632 * 0.24062204
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 12300 * 0.24065055
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 839 * 0.79633521
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14340 * 0.53817432
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24199 * 0.27358465
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16475 * 0.52864006
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12241 * 0.70114848
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 11262 * 0.93798210
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77889 * 0.69038627
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56982 * 0.76003521
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64233 * 0.09311976
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72340 * 0.89949917
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 2774 * 0.63452374
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42053 * 0.08058414
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 61313 * 0.19356253
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67778 * 0.13053497
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16261 * 0.76944343
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9305 * 0.70059312
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 41217 * 0.17129228
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72332 * 0.25841509
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94700 * 0.53215906
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 1551 * 0.41478548
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48231 * 0.61624614
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'frzhugok').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0043():
    """Extended test 43 for aggregation."""
    x_0 = 1983 * 0.17583417
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12047 * 0.20643497
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94590 * 0.83981224
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71201 * 0.02148151
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 76370 * 0.75596761
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71334 * 0.51290614
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25213 * 0.80287412
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1350 * 0.80042592
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57414 * 0.19400043
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79157 * 0.13599204
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 50262 * 0.22419100
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75519 * 0.69230949
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43134 * 0.68199355
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10734 * 0.96270552
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 14037 * 0.09184995
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56034 * 0.40767313
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57572 * 0.66359716
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 31485 * 0.50916914
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3458 * 0.50025335
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19288 * 0.87731430
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40203 * 0.05443406
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 97344 * 0.99424026
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34713 * 0.09265740
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14443 * 0.69688233
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21906 * 0.63487700
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14200 * 0.00687707
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41018 * 0.88090362
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 66002 * 0.82902029
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42262 * 0.45040440
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59002 * 0.61353700
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92352 * 0.20135609
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67260 * 0.36559497
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64945 * 0.21596145
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63962 * 0.70312867
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85992 * 0.41106687
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65517 * 0.89832189
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 8871 * 0.58185431
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10830 * 0.91610683
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 99174 * 0.82290148
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67859 * 0.62677114
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 65382 * 0.78768787
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35872 * 0.78882691
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'sgegekaq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0044():
    """Extended test 44 for aggregation."""
    x_0 = 65039 * 0.82986657
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25775 * 0.05902868
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94632 * 0.73403021
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97243 * 0.29719207
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 1930 * 0.05212077
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29619 * 0.28800962
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93714 * 0.06032139
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50332 * 0.27816525
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 38833 * 0.33295673
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49290 * 0.28648396
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 32610 * 0.86965498
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37968 * 0.27921675
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64057 * 0.25591677
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32078 * 0.73244847
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 33838 * 0.59269598
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84024 * 0.09152067
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92937 * 0.62365749
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28391 * 0.23418989
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17055 * 0.45363496
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60818 * 0.71914283
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56060 * 0.40130133
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71368 * 0.10903230
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52190 * 0.75803340
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48065 * 0.88619543
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4596 * 0.90840602
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 13159 * 0.42077655
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53988 * 0.05102891
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'ymplcfds').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0045():
    """Extended test 45 for aggregation."""
    x_0 = 26163 * 0.79451545
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99080 * 0.75958475
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67823 * 0.18898637
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64349 * 0.35947947
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83137 * 0.31393243
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1823 * 0.78730053
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70562 * 0.93676090
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 70808 * 0.38722322
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25580 * 0.48491343
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 51381 * 0.26378564
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67502 * 0.33053620
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 14815 * 0.07679944
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 13766 * 0.57058492
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43170 * 0.18138338
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7272 * 0.33968202
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54567 * 0.83905791
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52967 * 0.49166042
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 170 * 0.06477362
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23066 * 0.58707500
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 2281 * 0.61591542
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 26340 * 0.03352566
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4868 * 0.87726285
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14270 * 0.93558651
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 848 * 0.39097318
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8820 * 0.06079930
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47754 * 0.51746039
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79482 * 0.73379924
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74646 * 0.60179059
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70876 * 0.16540408
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 96985 * 0.92956443
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12543 * 0.69260876
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 25339 * 0.21456671
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45444 * 0.00884619
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9321 * 0.85841042
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 61111 * 0.06858683
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18786 * 0.24995675
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 44621 * 0.98529286
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 72933 * 0.27711570
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'dqrtumkb').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0046():
    """Extended test 46 for aggregation."""
    x_0 = 67025 * 0.03240087
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73547 * 0.46251074
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20218 * 0.83933335
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 646 * 0.10671673
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 24123 * 0.90528626
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 7611 * 0.13814635
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70696 * 0.33958600
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13442 * 0.05031074
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 6320 * 0.46223862
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 80480 * 0.60053893
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 70070 * 0.51323797
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 48614 * 0.54450676
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 10477 * 0.82082175
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15671 * 0.00836095
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43739 * 0.28264723
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 29782 * 0.10123819
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86867 * 0.60336541
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12951 * 0.09388016
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 57480 * 0.34628652
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28556 * 0.66900268
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44255 * 0.57846375
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34196 * 0.73085574
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 95824 * 0.50679713
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 17489 * 0.58173670
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60853 * 0.83512500
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7423 * 0.13293601
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62343 * 0.93981379
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 16598 * 0.03022574
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12438 * 0.97729256
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 91288 * 0.46076650
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92209 * 0.61622415
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72898 * 0.99466769
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 47774 * 0.03055213
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40213 * 0.93678629
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89189 * 0.43362656
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'xptpaymu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0047():
    """Extended test 47 for aggregation."""
    x_0 = 23373 * 0.78311515
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64906 * 0.37675640
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 35905 * 0.24625816
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68359 * 0.32091622
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21590 * 0.01243874
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47797 * 0.61199104
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62070 * 0.06736146
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76970 * 0.97794184
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95965 * 0.19106567
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72164 * 0.37823546
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 88189 * 0.41595060
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 53591 * 0.71593950
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69876 * 0.05346810
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 59964 * 0.84032493
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39581 * 0.77984795
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82054 * 0.67365031
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54043 * 0.08097462
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6436 * 0.91642989
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6837 * 0.05518014
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55908 * 0.21866409
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62545 * 0.67062893
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 61893 * 0.65480165
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 73754 * 0.79878829
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26471 * 0.79897301
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17109 * 0.77847211
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'hncmjsnl').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0048():
    """Extended test 48 for aggregation."""
    x_0 = 55422 * 0.57077469
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93508 * 0.51153231
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20965 * 0.48509932
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30406 * 0.30195715
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78990 * 0.43224302
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65046 * 0.89941241
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79859 * 0.71936927
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48403 * 0.29443469
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63543 * 0.85106119
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1171 * 0.34302135
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74340 * 0.36579847
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82292 * 0.50206910
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 20735 * 0.90108652
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45996 * 0.14801376
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 60888 * 0.60572076
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6951 * 0.82293560
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46250 * 0.41959519
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 38674 * 0.89081332
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97248 * 0.74617387
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 51546 * 0.57298553
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32948 * 0.03050850
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56783 * 0.64045310
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4520 * 0.86941350
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10986 * 0.31657857
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33492 * 0.70437651
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20834 * 0.50218331
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11303 * 0.90248926
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 61753 * 0.59207575
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84023 * 0.27991793
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44984 * 0.60768877
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 10570 * 0.48490501
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18923 * 0.88021315
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13390 * 0.01005220
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97939 * 0.06618220
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'woaotvmh').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0049():
    """Extended test 49 for aggregation."""
    x_0 = 8660 * 0.92550956
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71109 * 0.85096442
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41229 * 0.93172146
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65190 * 0.46190073
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89256 * 0.48689411
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54031 * 0.71405267
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 874 * 0.28952539
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 7464 * 0.49582757
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70163 * 0.76014578
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12867 * 0.03942551
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72870 * 0.07424760
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13610 * 0.25499064
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9844 * 0.77832120
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93228 * 0.91164187
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43252 * 0.27751800
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59027 * 0.13615030
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13240 * 0.04909016
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93096 * 0.55370340
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62019 * 0.30531546
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6483 * 0.94196652
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75118 * 0.29910201
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95591 * 0.43786860
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97926 * 0.35986018
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'hmvbxflw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0050():
    """Extended test 50 for aggregation."""
    x_0 = 31584 * 0.66396601
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 41730 * 0.68046009
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73596 * 0.77689215
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37028 * 0.81043961
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71070 * 0.15319514
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4969 * 0.79701791
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30803 * 0.98531512
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49880 * 0.60708409
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80280 * 0.68144892
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 48137 * 0.84179665
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74253 * 0.22573100
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94794 * 0.08096013
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46488 * 0.61173264
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30499 * 0.18032846
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12043 * 0.83339328
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49953 * 0.55723956
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74944 * 0.01904845
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97161 * 0.12891374
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65278 * 0.82147707
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1065 * 0.82404656
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91675 * 0.59951654
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50911 * 0.58457153
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41079 * 0.92285449
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 1010 * 0.01173943
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'yuqoqdga').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0051():
    """Extended test 51 for aggregation."""
    x_0 = 90790 * 0.40121213
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17320 * 0.73810753
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86297 * 0.66984403
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 12815 * 0.53683307
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33629 * 0.60071502
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 53985 * 0.34528715
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 27191 * 0.58638508
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83985 * 0.50923874
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44066 * 0.94573872
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 42669 * 0.61090368
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62776 * 0.93266372
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23833 * 0.06454640
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43183 * 0.48209864
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71475 * 0.26388368
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20383 * 0.96033786
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6759 * 0.21965370
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53451 * 0.44705920
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45088 * 0.56519667
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19723 * 0.18405308
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16812 * 0.44886341
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45360 * 0.49049795
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90957 * 0.18253321
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21864 * 0.31831397
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 77876 * 0.28104477
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65535 * 0.90545260
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'gaozntwa').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0052():
    """Extended test 52 for aggregation."""
    x_0 = 52184 * 0.90547855
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27638 * 0.64131267
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87864 * 0.54174301
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 38805 * 0.25413730
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28974 * 0.49220423
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70743 * 0.37108098
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 87257 * 0.07812626
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45776 * 0.61405436
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46795 * 0.84098701
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68790 * 0.54290805
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26315 * 0.69717874
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67475 * 0.27316604
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3506 * 0.03855134
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3631 * 0.08331297
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94009 * 0.07540534
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 61904 * 0.53160845
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 84568 * 0.80345318
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80330 * 0.35150751
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99381 * 0.74105837
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60530 * 0.16958044
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 24523 * 0.83570733
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31526 * 0.32369958
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97680 * 0.03154319
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82033 * 0.49033797
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38308 * 0.06191656
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95913 * 0.61384920
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'rlnoulap').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0053():
    """Extended test 53 for aggregation."""
    x_0 = 12810 * 0.69846525
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 93505 * 0.57668703
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 68331 * 0.07436438
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 77327 * 0.26422965
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57602 * 0.44602917
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35241 * 0.94651698
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71842 * 0.79578972
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63332 * 0.71401958
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36173 * 0.59289280
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97850 * 0.91782049
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10136 * 0.00383878
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86569 * 0.47063140
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47703 * 0.27800698
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30619 * 0.48998432
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52241 * 0.25947491
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67718 * 0.04673600
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95684 * 0.75678259
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65874 * 0.92905595
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97015 * 0.30458393
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22639 * 0.78253519
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 91952 * 0.62740816
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59965 * 0.99388263
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 69694 * 0.60484901
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7566 * 0.91412846
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44533 * 0.16013943
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49008 * 0.05756714
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11491 * 0.26863630
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9235 * 0.60101638
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 11988 * 0.39553382
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82180 * 0.57430211
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 101 * 0.96390623
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 48776 * 0.69765014
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54943 * 0.51563553
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'gdjydenk').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0054():
    """Extended test 54 for aggregation."""
    x_0 = 87974 * 0.98849110
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83675 * 0.70718102
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30253 * 0.85284437
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82550 * 0.27918679
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71990 * 0.17125031
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87664 * 0.86514243
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6334 * 0.26808155
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17967 * 0.88107060
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 68077 * 0.48585099
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55808 * 0.30525717
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84110 * 0.29945594
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16248 * 0.12100760
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4622 * 0.22978600
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 92630 * 0.19941681
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31298 * 0.55154945
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 75076 * 0.70001921
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7616 * 0.58377978
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1591 * 0.36888763
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11081 * 0.14157026
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79526 * 0.83209706
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88918 * 0.26180943
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34378 * 0.72657026
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59380 * 0.82407587
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 82913 * 0.55926903
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47193 * 0.38739960
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52844 * 0.02282537
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54406 * 0.61353340
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90860 * 0.25466758
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 76760 * 0.56917298
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 45225 * 0.31868388
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'gzwxbjob').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0055():
    """Extended test 55 for aggregation."""
    x_0 = 50775 * 0.11198063
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99888 * 0.62808698
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54516 * 0.59748118
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 13339 * 0.43367258
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50072 * 0.94815197
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 32802 * 0.33387808
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 14298 * 0.29091981
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67488 * 0.75001499
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4886 * 0.02889952
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34811 * 0.16398525
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10346 * 0.29999471
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56185 * 0.93135618
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50481 * 0.10954867
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 62586 * 0.02581356
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78284 * 0.46496118
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6362 * 0.38351714
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60773 * 0.56242607
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26318 * 0.72637371
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17932 * 0.74937638
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27205 * 0.72471003
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61881 * 0.21774236
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66732 * 0.97552578
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24403 * 0.91008544
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73628 * 0.67392994
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 72048 * 0.66588865
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15129 * 0.61071501
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81559 * 0.92591128
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25502 * 0.84029722
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 8583 * 0.65842274
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 25530 * 0.83071606
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 73071 * 0.51611539
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'cygdfxww').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0056():
    """Extended test 56 for aggregation."""
    x_0 = 23512 * 0.60541339
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88319 * 0.52402699
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32332 * 0.69351458
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32576 * 0.86755373
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67799 * 0.28147211
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 96451 * 0.49855911
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 29471 * 0.31412870
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31538 * 0.96363406
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50535 * 0.68851465
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77028 * 0.57071551
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43287 * 0.31301635
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6936 * 0.18750747
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 82631 * 0.21592187
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68864 * 0.52844144
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 3321 * 0.49076588
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21891 * 0.53289109
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28717 * 0.52376886
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 12821 * 0.63152761
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39916 * 0.38486268
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24092 * 0.47637287
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3553 * 0.77170799
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83730 * 0.55854092
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43527 * 0.00006230
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 57716 * 0.10279053
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 8716 * 0.07439697
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11616 * 0.87074225
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5036 * 0.65897846
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 44615 * 0.15372887
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6386 * 0.84065583
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 82821 * 0.98040173
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62834 * 0.92279964
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30990 * 0.83147998
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 83095 * 0.44971122
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 77694 * 0.07761526
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37490 * 0.08434484
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26875 * 0.57881618
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80388 * 0.13049480
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 19466 * 0.51032521
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 91314 * 0.19946074
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 26743 * 0.33660495
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 6734 * 0.89552548
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3645 * 0.43464435
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44860 * 0.09623838
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 53301 * 0.76096292
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 10497 * 0.61738639
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 4979 * 0.31098247
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 72607 * 0.90974975
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 91098 * 0.63786967
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 24015 * 0.99665478
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 59717 * 0.71960719
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ldywqttp').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0057():
    """Extended test 57 for aggregation."""
    x_0 = 77566 * 0.84512330
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78970 * 0.82287226
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16784 * 0.30243132
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67813 * 0.16886887
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36873 * 0.87259952
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97603 * 0.82864809
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90994 * 0.78505607
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10182 * 0.78290182
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63531 * 0.27271248
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18259 * 0.35990588
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 24382 * 0.50297560
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70143 * 0.68084649
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46198 * 0.65933136
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75312 * 0.25894969
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95217 * 0.18534601
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 15921 * 0.80822795
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86501 * 0.20364511
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 25231 * 0.80530482
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95464 * 0.10945008
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 46921 * 0.53232648
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89621 * 0.04874803
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99908 * 0.41232213
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 88645 * 0.67300785
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 94298 * 0.63066468
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 37221 * 0.36101597
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 11234 * 0.83388532
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70847 * 0.95992915
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99338 * 0.95942014
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 41722 * 0.41832900
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50238 * 0.94344794
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 57209 * 0.73446074
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 27990 * 0.22138873
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89182 * 0.50934572
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 66023 * 0.93255508
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59209 * 0.17784106
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47310 * 0.36298935
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62582 * 0.47058494
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 80910 * 0.29305383
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23084 * 0.06820869
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ijhvzavy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0058():
    """Extended test 58 for aggregation."""
    x_0 = 34713 * 0.96577042
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27484 * 0.88130393
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84008 * 0.53354972
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54317 * 0.54020442
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42284 * 0.11734493
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64257 * 0.91973037
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31549 * 0.53426271
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 1420 * 0.05757002
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60201 * 0.92403760
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26113 * 0.22122818
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13487 * 0.15067750
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73648 * 0.42472335
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63267 * 0.50766641
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 30836 * 0.92406803
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27946 * 0.26658634
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 601 * 0.00601962
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 45302 * 0.01845796
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89692 * 0.32534728
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40956 * 0.78430183
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 8586 * 0.39353853
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83963 * 0.89080187
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9062 * 0.64561981
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 7835 * 0.96250191
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39193 * 0.02872929
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 89267 * 0.49967233
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85161 * 0.84645942
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61900 * 0.44210292
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99282 * 0.58797735
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 46350 * 0.21806707
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18691 * 0.61932468
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6757 * 0.11832388
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 81632 * 0.18787998
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18197 * 0.55449124
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24303 * 0.44522153
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5451 * 0.87424432
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 67404 * 0.70978796
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 93057 * 0.09879584
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 70190 * 0.08270422
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'wmuuqozv').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0059():
    """Extended test 59 for aggregation."""
    x_0 = 57770 * 0.32231624
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56780 * 0.10365553
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1763 * 0.61663992
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17588 * 0.20871251
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67707 * 0.53365036
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92322 * 0.86295356
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82561 * 0.66446525
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8772 * 0.21156753
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45692 * 0.42958256
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61483 * 0.69986434
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2725 * 0.95676275
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67348 * 0.31164973
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17231 * 0.11797633
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40681 * 0.83550889
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 20816 * 0.94701247
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52153 * 0.35177383
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 92697 * 0.27417598
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 41366 * 0.90418599
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15823 * 0.31577782
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33617 * 0.90721631
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33142 * 0.39354746
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74557 * 0.69846214
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4312 * 0.28637727
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 816 * 0.76127172
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99729 * 0.03011485
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10927 * 0.46606961
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94166 * 0.92609868
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36089 * 0.30971570
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 70633 * 0.27476403
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78841 * 0.03909212
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 11870 * 0.37175228
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 53423 * 0.40900909
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23532 * 0.59185951
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 53322 * 0.50847856
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 26499 * 0.00695066
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59644 * 0.97039089
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50039 * 0.17488852
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 18012 * 0.33819110
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47894 * 0.53471994
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'ezadcyyu').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0060():
    """Extended test 60 for aggregation."""
    x_0 = 4702 * 0.21379782
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2053 * 0.94722075
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92487 * 0.72396831
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42818 * 0.01056541
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 56226 * 0.86293144
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70906 * 0.60508658
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53911 * 0.87000940
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20379 * 0.80786301
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5103 * 0.86058193
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74889 * 0.62020692
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35199 * 0.49041114
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84241 * 0.79212728
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 36628 * 0.56232599
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46714 * 0.36481455
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32125 * 0.44134207
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17802 * 0.60253280
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24964 * 0.60412083
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42436 * 0.81998591
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63087 * 0.94319671
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54744 * 0.89635153
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80661 * 0.25335745
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91969 * 0.12098765
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 97969 * 0.52030851
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32900 * 0.76250928
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'yadmzhns').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0061():
    """Extended test 61 for aggregation."""
    x_0 = 32969 * 0.88445448
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32529 * 0.15846692
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18118 * 0.89658887
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1862 * 0.62810679
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 46290 * 0.73090282
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95012 * 0.17171825
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94051 * 0.40695973
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20265 * 0.40041253
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54774 * 0.90842701
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7770 * 0.09284211
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25613 * 0.11105513
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30020 * 0.95482481
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6083 * 0.42687396
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54566 * 0.84838386
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56307 * 0.64271561
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11775 * 0.02513367
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 55404 * 0.03017454
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99025 * 0.80227880
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13004 * 0.53198671
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42913 * 0.21945592
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10308 * 0.21846562
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 76100 * 0.72338428
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'pskksbyq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0062():
    """Extended test 62 for aggregation."""
    x_0 = 96394 * 0.39214003
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 97621 * 0.82910405
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52949 * 0.17137921
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82495 * 0.90034140
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19534 * 0.94406159
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76794 * 0.00978299
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60979 * 0.71739679
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50098 * 0.66518744
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63702 * 0.14852527
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90849 * 0.21385388
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8192 * 0.98601806
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86972 * 0.18724333
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15958 * 0.99286001
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82504 * 0.54150915
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24225 * 0.29738902
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39317 * 0.30496052
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32701 * 0.41564584
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 37025 * 0.41859548
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 12257 * 0.59875861
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50608 * 0.59823263
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 29275 * 0.39267272
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50407 * 0.06743446
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'jidcetfq').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0063():
    """Extended test 63 for aggregation."""
    x_0 = 31085 * 0.93494945
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70357 * 0.85575511
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3809 * 0.03395492
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 36263 * 0.74337842
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63351 * 0.33660133
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73848 * 0.92683997
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 12079 * 0.31984983
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25575 * 0.21355836
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49305 * 0.62272736
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49160 * 0.14929673
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80359 * 0.56436700
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 90213 * 0.34898708
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35694 * 0.98168711
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56397 * 0.21352869
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85828 * 0.71327846
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39022 * 0.21104724
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52847 * 0.26364599
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42288 * 0.96794993
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23822 * 0.62751419
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 82722 * 0.85266234
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 45436 * 0.93579041
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35618 * 0.54344639
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1005 * 0.78752762
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 91181 * 0.09399173
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 57289 * 0.99218206
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 7540 * 0.10972761
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34397 * 0.19673896
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29719 * 0.04308642
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67702 * 0.79745213
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81341 * 0.20558996
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92270 * 0.05475223
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19627 * 0.77080105
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38054 * 0.80894593
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98438 * 0.36401875
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37937 * 0.77159924
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 18636 * 0.06493232
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43100 * 0.93202842
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42609 * 0.00897171
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 64575 * 0.71125035
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18930 * 0.86523760
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54599 * 0.44550374
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'besanmem').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0064():
    """Extended test 64 for aggregation."""
    x_0 = 60629 * 0.33157245
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39934 * 0.99248664
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74218 * 0.37278363
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41784 * 0.98813858
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18042 * 0.77814613
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2700 * 0.56607571
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7356 * 0.13605542
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64818 * 0.22705620
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48711 * 0.54300775
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23674 * 0.60463947
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26295 * 0.24858374
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21794 * 0.56511595
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 30150 * 0.05656249
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4460 * 0.45922790
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 79850 * 0.97968478
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4217 * 0.25659280
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 99085 * 0.00765706
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36234 * 0.05388999
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30596 * 0.68449995
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 79584 * 0.25694542
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58536 * 0.94874989
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37139 * 0.38707621
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94760 * 0.74591004
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73427 * 0.62592299
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'eeksucwy').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0065():
    """Extended test 65 for aggregation."""
    x_0 = 21126 * 0.30913078
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27699 * 0.63450351
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21036 * 0.13626140
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33792 * 0.55702432
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31980 * 0.68285266
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64751 * 0.02679714
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97015 * 0.97104614
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65895 * 0.79379072
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62979 * 0.82513290
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61437 * 0.66682441
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85208 * 0.98756628
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95726 * 0.94518300
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 27501 * 0.38959838
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71671 * 0.61543363
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 23274 * 0.88126312
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 17537 * 0.65667423
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90634 * 0.82634753
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 11917 * 0.54240084
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 16292 * 0.57761633
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25741 * 0.96262459
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49256 * 0.77339255
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87632 * 0.27400965
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16539 * 0.00062242
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ztxdglez').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0066():
    """Extended test 66 for aggregation."""
    x_0 = 95226 * 0.05284713
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86491 * 0.59831416
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 30975 * 0.88035168
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67893 * 0.80481145
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 57828 * 0.60353893
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22141 * 0.51577270
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10101 * 0.33637281
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 79865 * 0.85201891
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54241 * 0.87945456
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21961 * 0.62261058
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33115 * 0.59679768
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86408 * 0.42664224
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39832 * 0.26560501
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63996 * 0.43515075
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94027 * 0.71358525
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 77010 * 0.66421441
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53379 * 0.60831389
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14295 * 0.40162831
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79322 * 0.61127710
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3972 * 0.26553542
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 92623 * 0.81610431
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88048 * 0.71764950
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37269 * 0.53214885
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6206 * 0.92027148
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71515 * 0.02458474
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29560 * 0.05684855
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20493 * 0.50122115
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89465 * 0.00294266
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 1142 * 0.76561139
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 17743 * 0.40243750
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23891 * 0.82630502
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 16926 * 0.12656036
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60488 * 0.86588438
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24291 * 0.62838867
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 37485 * 0.48728617
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 27613 * 0.17025656
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 45577 * 0.97132189
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'oshgubks').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0067():
    """Extended test 67 for aggregation."""
    x_0 = 22989 * 0.65647024
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86218 * 0.63568276
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64581 * 0.61691858
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 76311 * 0.26705358
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58267 * 0.93051450
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71653 * 0.91734878
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21833 * 0.69939510
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 54728 * 0.19885350
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 87742 * 0.50286876
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56734 * 0.54342483
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38706 * 0.56196645
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17009 * 0.24216071
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37059 * 0.86554120
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36407 * 0.65243994
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 8710 * 0.51297440
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26550 * 0.96981602
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47544 * 0.10660457
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51986 * 0.86749238
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 30045 * 0.40651700
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39134 * 0.88595280
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 756 * 0.46306964
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32967 * 0.44839389
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59797 * 0.41502623
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87305 * 0.67990962
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11032 * 0.80706721
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21573 * 0.60122115
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 42682 * 0.36559878
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64993 * 0.74129583
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95353 * 0.15456388
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5695 * 0.90710992
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'aeshftmw').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0068():
    """Extended test 68 for aggregation."""
    x_0 = 71259 * 0.09361742
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 12111 * 0.50747805
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24820 * 0.12212361
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7495 * 0.18915372
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87598 * 0.83201238
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84103 * 0.38137258
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15119 * 0.90634013
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47165 * 0.78440593
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18139 * 0.46276043
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 32698 * 0.84606097
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80337 * 0.26653924
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 98430 * 0.46346327
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7253 * 0.00107260
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5403 * 0.05554601
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36308 * 0.40257432
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65310 * 0.20071818
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 16849 * 0.39967123
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47397 * 0.54463180
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27606 * 0.68445656
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91195 * 0.88008109
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64637 * 0.94569946
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2895 * 0.61927397
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84179 * 0.87531460
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12187 * 0.78081357
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 33857 * 0.59777269
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 36002 * 0.93233096
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41351 * 0.80285477
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 35603 * 0.26620035
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90573 * 0.79902764
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'zkcdvapj').hexdigest()
    assert len(h) == 64

def test_aggregation_extended_4_0069():
    """Extended test 69 for aggregation."""
    x_0 = 37752 * 0.91961345
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 21182 * 0.75697042
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 72131 * 0.41271475
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24311 * 0.09027923
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43093 * 0.62490491
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33196 * 0.51361073
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64190 * 0.11414345
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76564 * 0.23980364
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17717 * 0.63116901
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1580 * 0.19381216
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4343 * 0.30598785
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26084 * 0.15096591
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46994 * 0.14340308
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 31493 * 0.80684690
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 7486 * 0.99120363
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58513 * 0.62395107
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17858 * 0.01592912
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58593 * 0.80008411
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81833 * 0.03786928
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 24185 * 0.86519354
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41437 * 0.96351310
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51889 * 0.48502077
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3440 * 0.81534737
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10437 * 0.89500955
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 93092 * 0.76511948
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 25745 * 0.37490349
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 6940 * 0.46102435
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'yrxqmqyw').hexdigest()
    assert len(h) == 64
