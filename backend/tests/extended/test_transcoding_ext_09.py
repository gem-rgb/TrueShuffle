"""Extended tests for transcoding suite 9."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_transcoding_extended_9_0000():
    """Extended test 0 for transcoding."""
    x_0 = 36838 * 0.73996939
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66873 * 0.92100056
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 25548 * 0.59800202
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10003 * 0.72712188
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64773 * 0.49705739
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 21669 * 0.33330312
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 38686 * 0.58542391
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23947 * 0.37316175
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10313 * 0.42112637
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62295 * 0.99062857
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 74913 * 0.75921675
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49510 * 0.65374119
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 42973 * 0.05541433
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88175 * 0.91033695
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 37991 * 0.34569279
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 54355 * 0.66624462
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91906 * 0.63138094
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 73897 * 0.56943553
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 3775 * 0.36209678
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33570 * 0.12898349
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2302 * 0.25430052
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88769 * 0.96317777
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 10571 * 0.12158885
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66389 * 0.38921325
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 10026 * 0.51528607
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37281 * 0.93648344
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8974 * 0.50487241
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65099 * 0.27328127
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48506 * 0.85774419
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 43821 * 0.49199159
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19329 * 0.28740814
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1951 * 0.90196339
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44102 * 0.90222046
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69382 * 0.46415081
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35060 * 0.00703134
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 99330 * 0.74556751
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65767 * 0.88165836
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'nudmyzss').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0001():
    """Extended test 1 for transcoding."""
    x_0 = 79217 * 0.05975943
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30287 * 0.58620397
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18021 * 0.49797544
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79826 * 0.98432661
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96542 * 0.33183433
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56239 * 0.80321063
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 72208 * 0.25965147
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17575 * 0.33675015
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33589 * 0.47919847
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12627 * 0.91854902
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 8837 * 0.14706890
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93137 * 0.67454594
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38277 * 0.95773352
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89927 * 0.50040173
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35662 * 0.41981758
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21816 * 0.78966340
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69255 * 0.41434262
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 519 * 0.08027380
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 2427 * 0.53420331
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42714 * 0.02805319
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81778 * 0.15331964
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88860 * 0.78451793
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25452 * 0.89176485
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72887 * 0.24575293
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6173 * 0.42380939
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98991 * 0.57975779
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57782 * 0.27333753
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24671 * 0.92383332
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94005 * 0.67630322
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 12921 * 0.48864406
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 28191 * 0.61064197
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35676 * 0.41171113
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82864 * 0.21104145
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97050 * 0.38742782
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 30350 * 0.10638276
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 46755 * 0.23721165
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'nlbpxanj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0002():
    """Extended test 2 for transcoding."""
    x_0 = 44427 * 0.34009626
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 13592 * 0.39533825
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 57509 * 0.59747437
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6519 * 0.23225986
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97847 * 0.87761434
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6795 * 0.52057229
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88125 * 0.16550404
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3445 * 0.09025678
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93850 * 0.82521064
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59036 * 0.21515057
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3372 * 0.53426119
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63169 * 0.46284989
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 93255 * 0.25975188
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 87403 * 0.27845657
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4381 * 0.72690046
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69924 * 0.26572051
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76414 * 0.45652333
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28229 * 0.69046242
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41630 * 0.51102020
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16989 * 0.43722715
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42709 * 0.00274786
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 83772 * 0.02300899
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'tpzuetro').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0003():
    """Extended test 3 for transcoding."""
    x_0 = 82797 * 0.28622889
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88596 * 0.53116316
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89942 * 0.27045564
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70660 * 0.66001215
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 52459 * 0.51439446
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1871 * 0.31318979
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 10234 * 0.74870827
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71793 * 0.89725136
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17951 * 0.94542030
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73222 * 0.59845912
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 91774 * 0.09615376
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87260 * 0.74301798
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60330 * 0.08849979
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 25307 * 0.61460672
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24896 * 0.12934405
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 20471 * 0.81884588
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95286 * 0.72531327
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24825 * 0.93608039
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56468 * 0.93054082
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47290 * 0.00171331
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30301 * 0.55400113
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70230 * 0.44503437
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14563 * 0.46071766
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 38040 * 0.74204216
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 166 * 0.17581698
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32773 * 0.59026003
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4254 * 0.09601001
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 21756 * 0.60054548
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 79543 * 0.50360839
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54933 * 0.26053746
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49824 * 0.55689976
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67155 * 0.34323106
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'tmefqzme').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0004():
    """Extended test 4 for transcoding."""
    x_0 = 83858 * 0.70307236
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75971 * 0.34007247
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43502 * 0.40001237
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92958 * 0.61807474
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 62816 * 0.72006031
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82658 * 0.73454320
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88042 * 0.07578886
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 15746 * 0.11788256
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1783 * 0.46576837
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 71230 * 0.88351526
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34862 * 0.86391586
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2035 * 0.30453391
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 31722 * 0.09335482
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66442 * 0.48994669
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 61411 * 0.08603274
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 8762 * 0.25599301
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24804 * 0.14314050
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 20590 * 0.99190305
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68919 * 0.62740697
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 30519 * 0.94445320
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39835 * 0.72144127
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20038 * 0.68496543
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19686 * 0.94005006
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10920 * 0.76197862
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17613 * 0.99230668
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77285 * 0.66271319
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 65614 * 0.23128316
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56775 * 0.08060967
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'drvantdp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0005():
    """Extended test 5 for transcoding."""
    x_0 = 83555 * 0.98664751
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17987 * 0.09987022
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83058 * 0.19030095
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44263 * 0.40027194
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13945 * 0.11201647
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38481 * 0.63804733
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94976 * 0.48993996
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 35125 * 0.88082252
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90474 * 0.55257463
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77762 * 0.66593159
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10437 * 0.34609039
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 93772 * 0.51908814
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 33732 * 0.63326594
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82500 * 0.18281457
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 16742 * 0.80161500
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 52476 * 0.97835661
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19282 * 0.95597206
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84935 * 0.39961672
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81592 * 0.97643851
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 68509 * 0.41495235
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35870 * 0.82305725
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 37726 * 0.82830365
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53389 * 0.15077993
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 47779 * 0.70488347
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 46284 * 0.56800364
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4572 * 0.47883247
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62994 * 0.70866534
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 60206 * 0.65050125
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5061 * 0.93744398
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77766 * 0.69919788
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 36598 * 0.13641000
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46861 * 0.10637892
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93002 * 0.54560627
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 15948 * 0.11118711
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59086 * 0.76329754
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 72234 * 0.04712152
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 11794 * 0.10901187
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 32179 * 0.88266039
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93166 * 0.23899297
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 13583 * 0.76134587
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47711 * 0.22298446
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50701 * 0.52385422
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 79586 * 0.74269344
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 8530 * 0.51156001
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'khjkgmfs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0006():
    """Extended test 6 for transcoding."""
    x_0 = 32546 * 0.99184185
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15094 * 0.10131883
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 17205 * 0.65693031
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33627 * 0.61513344
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58171 * 0.19664544
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 45176 * 0.88440042
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81284 * 0.00967604
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 43127 * 0.30269647
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80870 * 0.01892761
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79906 * 0.57245721
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60885 * 0.22994954
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63069 * 0.13151194
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7859 * 0.01855793
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 67311 * 0.60775004
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95433 * 0.11546863
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36963 * 0.61945181
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18877 * 0.23364002
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 26212 * 0.37037072
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21517 * 0.86065980
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28549 * 0.80531705
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65185 * 0.17716048
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11310 * 0.82527289
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47801 * 0.51670868
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79282 * 0.19529401
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47810 * 0.66545856
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 51374 * 0.95100611
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'xchcjyyw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0007():
    """Extended test 7 for transcoding."""
    x_0 = 2088 * 0.14169645
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 59313 * 0.59826973
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 24357 * 0.83190117
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 64487 * 0.17414180
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84499 * 0.61321196
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40721 * 0.53959889
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 88070 * 0.67325505
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94988 * 0.58435822
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9796 * 0.38722413
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6051 * 0.47673270
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76002 * 0.37405754
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 25438 * 0.19352830
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 7677 * 0.83770028
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 11955 * 0.74292283
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71962 * 0.44653715
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26878 * 0.48016031
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49891 * 0.01681659
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15328 * 0.90859884
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65857 * 0.24348737
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31911 * 0.01885574
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36845 * 0.16775145
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44029 * 0.07343056
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16910 * 0.58688114
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 6372 * 0.82090724
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35486 * 0.00678145
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54166 * 0.17587410
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40268 * 0.71347673
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 24520 * 0.83435316
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 38802 * 0.94293339
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 21592 * 0.66830472
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 26973 * 0.38707345
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17712 * 0.68989450
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 28163 * 0.85663450
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'loimtkpy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0008():
    """Extended test 8 for transcoding."""
    x_0 = 69041 * 0.06266843
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7159 * 0.54938779
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2637 * 0.40024821
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3708 * 0.94593347
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99285 * 0.56251495
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29943 * 0.81796247
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49157 * 0.07132556
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17722 * 0.26963613
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73638 * 0.52376431
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97533 * 0.00568850
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58803 * 0.89265306
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80182 * 0.08713736
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15142 * 0.37811327
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43762 * 0.53912728
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 9171 * 0.10856210
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6729 * 0.59153541
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44501 * 0.64727552
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97013 * 0.44372181
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35451 * 0.94126784
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96065 * 0.41970072
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7585 * 0.36120891
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99841 * 0.86421509
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37144 * 0.24450362
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31488 * 0.94032254
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 19617 * 0.48559496
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77788 * 0.14535894
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21064 * 0.95229389
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50881 * 0.27620126
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 26719 * 0.18743993
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 86542 * 0.04423111
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62995 * 0.14728632
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 89494 * 0.44623596
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57995 * 0.76940237
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 40691 * 0.33589874
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8138 * 0.57838544
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 71774 * 0.85647839
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23391 * 0.88930078
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 69968 * 0.68328114
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 47522 * 0.50419920
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 49857 * 0.95861958
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'lfsudega').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0009():
    """Extended test 9 for transcoding."""
    x_0 = 99555 * 0.22427288
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 58061 * 0.88581386
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83360 * 0.31613704
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54216 * 0.43243483
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96108 * 0.15926590
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86261 * 0.71207959
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 53940 * 0.78617488
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71939 * 0.02252270
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17327 * 0.51119269
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11171 * 0.92986752
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9455 * 0.60268707
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56667 * 0.94657677
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17792 * 0.34041391
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81452 * 0.90157473
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81863 * 0.39808166
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 45314 * 0.02177002
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 90812 * 0.60063707
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36188 * 0.91720991
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85782 * 0.89159272
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47643 * 0.17423826
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93302 * 0.40264315
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 28347 * 0.41544464
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 20176 * 0.22619521
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16645 * 0.15024141
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 353 * 0.61555153
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 68582 * 0.35742380
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45738 * 0.96342330
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14978 * 0.65221230
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'phomtvga').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0010():
    """Extended test 10 for transcoding."""
    x_0 = 54088 * 0.35743459
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 35361 * 0.44247613
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 92322 * 0.41793602
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11013 * 0.85649314
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25539 * 0.78722611
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 59037 * 0.67625242
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 36095 * 0.82364376
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58240 * 0.47808765
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76426 * 0.81893165
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27930 * 0.65454118
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 35077 * 0.61284021
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27088 * 0.98770310
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 32107 * 0.97139881
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44134 * 0.34574004
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 95905 * 0.94324169
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49832 * 0.33067633
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87113 * 0.86436998
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52299 * 0.97798890
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 99091 * 0.29499259
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54385 * 0.17274220
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84536 * 0.99676315
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48957 * 0.06465128
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54619 * 0.49090385
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36769 * 0.16865045
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66323 * 0.63068656
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58008 * 0.67599897
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56675 * 0.93583089
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27956 * 0.56988678
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88534 * 0.53888793
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3988 * 0.94482665
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97471 * 0.28060197
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 13860 * 0.78399935
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5489 * 0.22881649
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25706 * 0.98265453
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63398 * 0.00142543
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5850 * 0.93752481
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65635 * 0.23183819
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 57179 * 0.43286559
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61635 * 0.38424826
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74598 * 0.88988625
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ysslqosv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0011():
    """Extended test 11 for transcoding."""
    x_0 = 24362 * 0.68542968
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78077 * 0.17151500
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52931 * 0.24372837
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51775 * 0.47760355
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43694 * 0.05398362
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47617 * 0.20587472
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22385 * 0.90684677
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 31731 * 0.44299143
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63098 * 0.66754480
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66826 * 0.36566961
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72470 * 0.74770029
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94631 * 0.52358916
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 78052 * 0.88319785
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34670 * 0.81126252
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98157 * 0.38929710
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6279 * 0.00438799
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64772 * 0.51794670
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83881 * 0.69652696
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 6679 * 0.49748333
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 27465 * 0.09718806
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25918 * 0.65062902
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 36984 * 0.67920464
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22046 * 0.59257984
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27450 * 0.12859072
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 99665 * 0.05331260
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92334 * 0.04530313
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16785 * 0.00440613
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84237 * 0.08661042
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86536 * 0.58054242
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61930 * 0.47040807
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1330 * 0.29073080
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69798 * 0.98758470
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98955 * 0.17222563
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64323 * 0.97938668
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 59946 * 0.78449715
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38368 * 0.17692641
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 84361 * 0.63778685
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92887 * 0.09428370
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'zomlmuwe').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0012():
    """Extended test 12 for transcoding."""
    x_0 = 19034 * 0.37999118
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77853 * 0.38959944
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94741 * 0.49820524
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 48559 * 0.12075376
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38673 * 0.17748190
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 36809 * 0.26955217
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89155 * 0.84343246
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81547 * 0.06645919
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13846 * 0.96564135
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18235 * 0.56987119
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7610 * 0.13282781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 37002 * 0.99977563
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57629 * 0.53362729
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6428 * 0.45540515
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50849 * 0.19512918
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57320 * 0.51167209
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 86804 * 0.26182337
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51875 * 0.83765360
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38503 * 0.68370560
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16029 * 0.97364912
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37705 * 0.20608056
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'slvemffg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0013():
    """Extended test 13 for transcoding."""
    x_0 = 74433 * 0.56707629
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65906 * 0.24152498
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 98698 * 0.73217050
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62901 * 0.74116908
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32300 * 0.21896933
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55187 * 0.93832638
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79037 * 0.23898219
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17710 * 0.73065177
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99004 * 0.90102644
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63445 * 0.14948792
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 7157 * 0.34276625
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1304 * 0.39892566
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5119 * 0.96930593
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 22623 * 0.67596512
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86518 * 0.60961634
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48655 * 0.25963942
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33540 * 0.21951532
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58900 * 0.06490347
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 68894 * 0.13016054
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 87908 * 0.20823089
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 85589 * 0.23405453
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 86264 * 0.30089320
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18885 * 0.25074475
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 21048 * 0.93798353
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9630 * 0.71944199
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89727 * 0.66326301
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95388 * 0.64711908
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56340 * 0.57030106
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86461 * 0.04367972
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 5109 * 0.00446412
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 87167 * 0.49224708
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 66462 * 0.73425117
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12249 * 0.93848653
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'tqxzympw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0014():
    """Extended test 14 for transcoding."""
    x_0 = 7703 * 0.73727235
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19014 * 0.70205141
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 29700 * 0.33278684
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51643 * 0.84444754
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33432 * 0.19394865
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 35642 * 0.47973124
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6784 * 0.37776199
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34088 * 0.53684028
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91231 * 0.60141178
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4998 * 0.79782906
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27590 * 0.00474060
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6501 * 0.45133766
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69781 * 0.38276706
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10993 * 0.20048446
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 43006 * 0.71569991
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78839 * 0.97479793
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6879 * 0.31234767
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 83450 * 0.41450783
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98482 * 0.45585944
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70789 * 0.55964757
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 69929 * 0.82560898
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40596 * 0.04452234
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 81866 * 0.67444896
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41355 * 0.19337036
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 77059 * 0.82674225
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 77449 * 0.09502485
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 80852 * 0.60565523
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 43510 * 0.06062893
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99733 * 0.27471707
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 78043 * 0.25268683
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 70632 * 0.72285385
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 7671 * 0.49659899
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91139 * 0.37835669
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'dzpfdhku').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0015():
    """Extended test 15 for transcoding."""
    x_0 = 28022 * 0.05598557
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 33921 * 0.18405461
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34536 * 0.03720705
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50268 * 0.95105130
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40317 * 0.08173593
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20665 * 0.77780248
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31824 * 0.56081996
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58559 * 0.85967441
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 4855 * 0.82670258
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 9268 * 0.07234802
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 55602 * 0.84610066
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18768 * 0.48009984
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 8160 * 0.34663760
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61820 * 0.41265988
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6109 * 0.01482325
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43254 * 0.20424186
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 87725 * 0.90634081
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10530 * 0.40424575
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64200 * 0.93983327
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75142 * 0.48361483
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56437 * 0.87310375
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45124 * 0.04184277
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72325 * 0.82849610
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49666 * 0.08574991
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64580 * 0.50394077
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6402 * 0.80349382
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53265 * 0.86469748
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 86407 * 0.70801039
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 37212 * 0.48396232
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 39894 * 0.10878289
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72911 * 0.42752990
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77327 * 0.55288831
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53402 * 0.81362403
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 98090 * 0.85206044
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 80934 * 0.78546728
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50886 * 0.10090829
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23013 * 0.11209921
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64059 * 0.97834688
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97487 * 0.90733146
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 12849 * 0.80131861
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 55148 * 0.52186540
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72869 * 0.54050705
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 70176 * 0.79370451
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ojpsqjwz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0016():
    """Extended test 16 for transcoding."""
    x_0 = 70164 * 0.71553399
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19227 * 0.63120002
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73990 * 0.54280017
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 41658 * 0.73283440
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32137 * 0.46418721
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50049 * 0.81629804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 75501 * 0.93946349
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 40636 * 0.54968320
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60484 * 0.06002980
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53462 * 0.29278508
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 94489 * 0.24007481
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 62904 * 0.35809025
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 61184 * 0.58985875
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93120 * 0.70656443
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 52426 * 0.50760171
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68645 * 0.56118063
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34766 * 0.49001062
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79480 * 0.34285135
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79036 * 0.56925256
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56746 * 0.34247311
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10718 * 0.30893600
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 49177 * 0.84825649
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 70281 * 0.17807248
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 39417 * 0.26709584
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 29579 * 0.28136570
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18203 * 0.69432236
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 67942 * 0.22113731
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 26104 * 0.30199642
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 69026 * 0.86844169
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 19276 * 0.47829583
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 56817 * 0.10932057
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37786 * 0.39726590
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17488 * 0.45996736
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36307 * 0.06676758
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 62224 * 0.39828818
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 93195 * 0.33346108
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 51693 * 0.58603763
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 47324 * 0.43388672
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97367 * 0.23229196
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76160 * 0.67535240
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 34179 * 0.55182528
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 85410 * 0.68050009
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 58085 * 0.42428898
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'vhwvasvo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0017():
    """Extended test 17 for transcoding."""
    x_0 = 48171 * 0.42310177
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80784 * 0.85157054
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51967 * 0.20374753
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44745 * 0.92474867
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2945 * 0.13966819
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26178 * 0.37102673
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 58022 * 0.58421692
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80809 * 0.81252590
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33843 * 0.04843962
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 92930 * 0.69813711
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22187 * 0.55063000
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 24518 * 0.33967063
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81369 * 0.67602511
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54199 * 0.11042488
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5460 * 0.43742452
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6914 * 0.50242588
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1442 * 0.14236636
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96498 * 0.09040900
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32371 * 0.89173989
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64314 * 0.39720141
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43265 * 0.03010687
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 60922 * 0.83353861
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90228 * 0.40347841
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10096 * 0.95943129
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39661 * 0.68035885
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38266 * 0.15044034
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88887 * 0.91545143
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31376 * 0.71621951
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75197 * 0.92656476
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2848 * 0.82941655
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42094 * 0.76097548
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 63169 * 0.63004224
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 64307 * 0.36745500
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39284 * 0.12818368
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89868 * 0.33631500
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 77916 * 0.23517471
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'gyhtqlmy').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0018():
    """Extended test 18 for transcoding."""
    x_0 = 69856 * 0.87529514
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89736 * 0.23452290
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 69877 * 0.92426871
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79368 * 0.24717822
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36054 * 0.22100180
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63864 * 0.48874420
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59377 * 0.16838144
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10660 * 0.71950020
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97942 * 0.79180031
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 34858 * 0.09529876
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66062 * 0.51625531
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59575 * 0.50742154
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 52072 * 0.57319137
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8880 * 0.21223193
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88447 * 0.75340382
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93760 * 0.32639036
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 71303 * 0.84405032
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95426 * 0.90294760
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21914 * 0.03851798
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 52194 * 0.09408629
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63840 * 0.51644334
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8853 * 0.88343873
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65386 * 0.57936218
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 43944 * 0.51638329
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84941 * 0.19371935
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93440 * 0.70505156
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64202 * 0.27909523
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 78975 * 0.78781486
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5176 * 0.12369856
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34473 * 0.62233560
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43094 * 0.12382610
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 75602 * 0.74344626
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 55736 * 0.75080080
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 69679 * 0.89340291
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14409 * 0.90218806
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 35092 * 0.12678782
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 32278 * 0.28641366
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64810 * 0.76070993
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 57653 * 0.53642715
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 34191 * 0.33531419
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'cwdbshmg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0019():
    """Extended test 19 for transcoding."""
    x_0 = 12258 * 0.52997215
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 11612 * 0.95159152
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83226 * 0.45830447
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42976 * 0.97429017
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74102 * 0.16133026
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 55799 * 0.36973779
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 71166 * 0.75138977
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98071 * 0.33576781
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58171 * 0.52651771
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90782 * 0.25864289
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 6349 * 0.85158849
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 92562 * 0.71373950
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 58220 * 0.21600569
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55797 * 0.20341994
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6596 * 0.16470763
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32843 * 0.31068326
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7596 * 0.13051701
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33034 * 0.13869277
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78611 * 0.87715274
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18774 * 0.61134506
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20175 * 0.48442401
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64028 * 0.68935831
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38038 * 0.97459266
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61616 * 0.18736125
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90059 * 0.08781992
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8759 * 0.49429315
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28811 * 0.27451030
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 50094 * 0.43191438
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93272 * 0.58743187
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3701 * 0.71572877
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69701 * 0.72283265
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84689 * 0.04765743
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82966 * 0.14496361
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 25754 * 0.90650493
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78254 * 0.60838191
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47344 * 0.42596833
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50990 * 0.34131762
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3926 * 0.91247153
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 93862 * 0.96680900
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 10508 * 0.46751273
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 42798 * 0.13781221
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54115 * 0.32863737
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 794 * 0.28740226
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 86391 * 0.04061220
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 88285 * 0.41608363
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 92181 * 0.96516990
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 61116 * 0.07616185
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 25088 * 0.11103228
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 30758 * 0.53083350
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'lsdditnf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0020():
    """Extended test 20 for transcoding."""
    x_0 = 34701 * 0.11108558
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63810 * 0.09382338
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 73491 * 0.05130719
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 20367 * 0.80463884
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22046 * 0.53103158
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67782 * 0.35621852
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63304 * 0.88941486
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 14097 * 0.48126558
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59013 * 0.87876412
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 66456 * 0.62333722
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23284 * 0.50649651
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95320 * 0.99492739
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6522 * 0.50356410
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96754 * 0.67105689
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 29936 * 0.64810841
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4794 * 0.36523204
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1700 * 0.98259242
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34321 * 0.12510558
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95548 * 0.56374500
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1853 * 0.04111214
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75751 * 0.84573804
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'tumjhmxk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0021():
    """Extended test 21 for transcoding."""
    x_0 = 45125 * 0.47278047
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94483 * 0.85758937
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37467 * 0.66402537
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11803 * 0.81068303
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 14387 * 0.33350649
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 84965 * 0.23768545
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 61158 * 0.05900672
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34091 * 0.50245381
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44350 * 0.89322659
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43184 * 0.31415408
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79032 * 0.86523018
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26139 * 0.93138448
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15773 * 0.59563978
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 129 * 0.72566660
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69374 * 0.73168026
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31206 * 0.99657783
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40648 * 0.51343549
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70751 * 0.95837152
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83313 * 0.86123819
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 43845 * 0.89242718
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 44834 * 0.70235432
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 71755 * 0.02866230
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 89873 * 0.87045640
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15355 * 0.81249536
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 60964 * 0.48006501
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 55938 * 0.86276077
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 51308 * 0.26367159
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34779 * 0.82070856
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7606 * 0.65303817
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 33374 * 0.24379031
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64886 * 0.48282525
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35857 * 0.78567231
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 96504 * 0.41276067
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 62945 * 0.02599247
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1855 * 0.06296621
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 96293 * 0.61372411
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69148 * 0.32491212
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 6873 * 0.40925473
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6942 * 0.63625995
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 33690 * 0.23996947
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 17552 * 0.43482724
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 96274 * 0.11380942
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 59824 * 0.66890698
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 68773 * 0.60461749
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'fnrmpvpn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0022():
    """Extended test 22 for transcoding."""
    x_0 = 45641 * 0.11937749
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66948 * 0.13121417
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12449 * 0.83518819
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 78268 * 0.39102952
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84405 * 0.13616595
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42706 * 0.21006626
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 6498 * 0.84727931
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53124 * 0.77997322
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75323 * 0.28570930
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52198 * 0.80523463
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 64404 * 0.74149336
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84366 * 0.09835725
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 38970 * 0.38973819
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48843 * 0.82350730
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62811 * 0.00606678
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 82679 * 0.74771112
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10384 * 0.54086035
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 72120 * 0.81011969
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93571 * 0.24508213
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 35451 * 0.97749647
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10295 * 0.94716113
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4859 * 0.86255497
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41845 * 0.70390213
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 89454 * 0.42378769
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47935 * 0.23505888
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 43580 * 0.99721771
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18576 * 0.50753608
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32606 * 0.57097332
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3223 * 0.01875773
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63813 * 0.67691891
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88109 * 0.43829151
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'vsacooao').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0023():
    """Extended test 23 for transcoding."""
    x_0 = 11492 * 0.27426366
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 4924 * 0.09119761
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 470 * 0.52994544
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52842 * 0.16416206
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 72611 * 0.66290612
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 41622 * 0.56151749
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 92269 * 0.70475527
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83483 * 0.38415661
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 9126 * 0.39671127
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57359 * 0.41589858
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95806 * 0.18365901
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87848 * 0.67320463
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96254 * 0.51785486
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14405 * 0.10183754
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49933 * 0.67297719
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33839 * 0.69334429
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19845 * 0.31088232
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49845 * 0.88879232
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20970 * 0.20768160
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55188 * 0.77363725
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53262 * 0.59863760
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 93655 * 0.79791616
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48604 * 0.55460667
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67552 * 0.63052986
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47139 * 0.29690773
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19226 * 0.49898483
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 70559 * 0.34671083
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52672 * 0.82125418
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 60687 * 0.45135693
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 571 * 0.28111008
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 75943 * 0.49628729
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 51531 * 0.04291933
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1217 * 0.63526599
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60350 * 0.69653490
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58125 * 0.43272315
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 1687 * 0.56837854
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 46824 * 0.52499896
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10628 * 0.02787722
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 60410 * 0.04622253
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 59261 * 0.57601173
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 46662 * 0.15320144
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 26775 * 0.71723475
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 76425 * 0.52664700
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27926 * 0.49451792
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 60238 * 0.87691169
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 60739 * 0.11485624
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 3502 * 0.46446912
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 8434 * 0.04465041
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 54133 * 0.06303803
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'qdjngxqx').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0024():
    """Extended test 24 for transcoding."""
    x_0 = 19045 * 0.76754123
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43955 * 0.17693316
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 186 * 0.82323953
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69792 * 0.83916171
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86208 * 0.11087333
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 80826 * 0.42580775
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 74280 * 0.41805543
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 94908 * 0.19960382
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70002 * 0.71060223
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 98826 * 0.55291349
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16004 * 0.56044413
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67182 * 0.59583492
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53764 * 0.46715071
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65476 * 0.40938174
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34689 * 0.22366180
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51489 * 0.45308135
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 82754 * 0.55830279
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56860 * 0.38512557
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67192 * 0.74823115
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 38229 * 0.70983826
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71707 * 0.55397730
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64814 * 0.12008323
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96086 * 0.25555246
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50524 * 0.00663708
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17458 * 0.20703827
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40806 * 0.24866363
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 27287 * 0.11637521
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85553 * 0.46182888
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'uijtnviu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0025():
    """Extended test 25 for transcoding."""
    x_0 = 77067 * 0.39938291
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92520 * 0.42596390
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36974 * 0.63864524
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26524 * 0.34930638
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69581 * 0.59234029
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49262 * 0.68367745
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80412 * 0.97973075
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10473 * 0.68379466
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 17385 * 0.44127691
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 62365 * 0.80006433
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22527 * 0.65394196
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 50944 * 0.13544223
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15066 * 0.79181569
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27642 * 0.64229506
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49071 * 0.82122997
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9928 * 0.00421700
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6161 * 0.78913401
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47218 * 0.50425285
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 15772 * 0.59400608
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4938 * 0.01991359
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96898 * 0.87933599
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20846 * 0.92927342
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51200 * 0.57767688
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86902 * 0.48157200
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73536 * 0.80046921
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 76289 * 0.96775288
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13972 * 0.87758887
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55581 * 0.28921891
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93159 * 0.11705243
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'cndddddc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0026():
    """Extended test 26 for transcoding."""
    x_0 = 50877 * 0.43301943
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 77701 * 0.54677886
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79405 * 0.25106033
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95936 * 0.62622469
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18387 * 0.78063099
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46292 * 0.05260086
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18153 * 0.48413500
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 36781 * 0.33847517
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 33472 * 0.63290466
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53638 * 0.03473660
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 38253 * 0.54679775
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71664 * 0.29540610
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 92138 * 0.52776541
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 44044 * 0.09775665
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11634 * 0.22516465
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 4160 * 0.10938386
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 17328 * 0.83647895
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 13145 * 0.39400960
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69239 * 0.36872799
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5956 * 0.68034068
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6039 * 0.54232356
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 50162 * 0.23771232
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41061 * 0.27045143
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63159 * 0.77280531
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'yblefrgo').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0027():
    """Extended test 27 for transcoding."""
    x_0 = 6738 * 0.47640684
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27946 * 0.85238267
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21167 * 0.67918488
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92814 * 0.81870818
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 37889 * 0.66938360
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75500 * 0.28843144
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52811 * 0.66037824
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60628 * 0.95080684
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76559 * 0.61639867
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63917 * 0.75803909
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48771 * 0.19082641
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 67799 * 0.41100455
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37388 * 0.82339911
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 3464 * 0.06527897
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4093 * 0.05778872
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81222 * 0.24976680
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 69298 * 0.23928251
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77441 * 0.15025155
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 36302 * 0.58395282
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90924 * 0.15874284
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63862 * 0.13333094
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56934 * 0.96322218
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28015 * 0.67888754
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93010 * 0.50999120
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5168 * 0.67858654
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49698 * 0.30688065
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 47554 * 0.51218901
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 25366 * 0.27429227
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85266 * 0.54691608
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53352 * 0.41811431
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 47918 * 0.01491752
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 30182 * 0.01008177
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82790 * 0.74593502
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 48163 * 0.14250177
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 85973 * 0.42266951
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 15907 * 0.23238938
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40430 * 0.69515313
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 60533 * 0.17529049
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'jckdrssk').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0028():
    """Extended test 28 for transcoding."""
    x_0 = 92674 * 0.86630554
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24075 * 0.77511599
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3183 * 0.91313712
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11412 * 0.22676869
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28208 * 0.98065550
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14632 * 0.38986348
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24841 * 0.93763858
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 83832 * 0.24626166
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15070 * 0.57861429
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41026 * 0.09903729
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62371 * 0.26848288
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33594 * 0.61182844
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34218 * 0.09958035
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8110 * 0.17544559
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 98062 * 0.38186390
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84886 * 0.36089180
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2753 * 0.13187212
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 7674 * 0.12917346
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81788 * 0.59264509
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 37040 * 0.50824622
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72116 * 0.07998336
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14541 * 0.80043541
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41031 * 0.99603689
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29124 * 0.06669907
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 12310 * 0.36787389
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37721 * 0.56536933
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2892 * 0.99921082
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 87015 * 0.18522759
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33928 * 0.69375830
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 3971 * 0.75840754
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 52184 * 0.29271368
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 87202 * 0.80115598
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33290 * 0.96286249
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 99834 * 0.97730846
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 33006 * 0.74407636
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 2547 * 0.35766111
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 23498 * 0.35670933
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10606 * 0.63278960
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 3504 * 0.25299281
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 74227 * 0.81871172
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 54657 * 0.50310569
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 83693 * 0.57847608
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11781 * 0.54778675
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 90236 * 0.11634712
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 34570 * 0.94885957
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'nlnjpszp').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0029():
    """Extended test 29 for transcoding."""
    x_0 = 59537 * 0.35793254
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95394 * 0.51137328
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97522 * 0.85082425
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88663 * 0.05718523
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78219 * 0.45998954
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78486 * 0.30548858
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59332 * 0.64785732
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 28809 * 0.05179436
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 19735 * 0.41981281
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25660 * 0.17372594
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 98410 * 0.31993753
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 80958 * 0.30881688
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96296 * 0.65306115
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 83700 * 0.15192231
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6981 * 0.07604649
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 58836 * 0.55781176
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 95770 * 0.59489109
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95715 * 0.37156722
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 1781 * 0.86322825
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63002 * 0.61809310
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62059 * 0.80906133
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2490 * 0.37416552
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18949 * 0.89135816
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78576 * 0.53451251
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61504 * 0.94819414
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14398 * 0.31228223
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 72362 * 0.38701802
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9095 * 0.80273558
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63681 * 0.37401965
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 47498 * 0.11258416
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 62485 * 0.93398425
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 24004 * 0.94933558
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 7929 * 0.49276378
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73746 * 0.62121814
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76772 * 0.45114728
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 64823 * 0.34587275
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69680 * 0.96703471
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 88074 * 0.24289484
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 34891 * 0.21998973
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31921 * 0.33289093
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19219 * 0.09964404
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'vvyxbefg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0030():
    """Extended test 30 for transcoding."""
    x_0 = 38644 * 0.54698923
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 55832 * 0.03532126
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 189 * 0.98722602
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5331 * 0.87297631
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 26310 * 0.54138530
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77928 * 0.12026085
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73799 * 0.36392816
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29260 * 0.23071141
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85712 * 0.73621349
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60907 * 0.16300007
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 67549 * 0.21968609
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29606 * 0.92560062
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99384 * 0.21007606
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 72188 * 0.04250190
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42399 * 0.98497650
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36399 * 0.92957321
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62163 * 0.32702491
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95744 * 0.84519457
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23706 * 0.92021097
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57292 * 0.74263833
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 62395 * 0.00217067
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 38294 * 0.44226514
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18314 * 0.91439976
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63769 * 0.41097528
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78898 * 0.31566137
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37161 * 0.62094689
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 73890 * 0.30850343
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27253 * 0.39927471
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 88762 * 0.16039455
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22372 * 0.75387871
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50275 * 0.46068183
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46533 * 0.23198710
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'gwojvnkc').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0031():
    """Extended test 31 for transcoding."""
    x_0 = 34479 * 0.12591486
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89510 * 0.80093655
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75453 * 0.31571909
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39055 * 0.80593392
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73643 * 0.68763609
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 11210 * 0.39528385
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67409 * 0.38045054
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10947 * 0.89993916
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 44054 * 0.90810446
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 56731 * 0.87337532
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 95759 * 0.45333378
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 89145 * 0.60496897
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71583 * 0.21977079
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52956 * 0.86907740
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46033 * 0.19512630
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92617 * 0.36866763
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 77377 * 0.13468731
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 32428 * 0.79257198
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17574 * 0.88556440
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 29750 * 0.92628325
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28766 * 0.33975253
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 43147 * 0.14603438
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14058 * 0.11423338
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41656 * 0.27686645
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21889 * 0.65254952
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57551 * 0.33571646
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 78289 * 0.44653571
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40149 * 0.42064968
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 23376 * 0.19682847
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38585 * 0.62381040
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96045 * 0.28178031
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 61847 * 0.10247479
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 80520 * 0.16664348
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 59153 * 0.44403200
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 95890 * 0.74166628
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 31082 * 0.43549133
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 43080 * 0.79614148
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 49017 * 0.00338375
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86332 * 0.38306881
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11313 * 0.79197200
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 31623 * 0.07485014
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 44250 * 0.77850960
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 47378 * 0.93343653
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 31946 * 0.00659310
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 76213 * 0.45679890
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 6156 * 0.55093021
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 54563 * 0.84930154
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 2238 * 0.05314547
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 9143 * 0.28373689
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'mifniphf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0032():
    """Extended test 32 for transcoding."""
    x_0 = 95807 * 0.01618163
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9765 * 0.58591557
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 93685 * 0.02169353
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 51600 * 0.91612053
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 75287 * 0.09561535
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 1789 * 0.68078664
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83820 * 0.31847858
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 46972 * 0.62976831
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95258 * 0.36912678
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 19992 * 0.45223939
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82524 * 0.71706876
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 33051 * 0.03964054
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62769 * 0.42613742
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21787 * 0.35215370
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 67329 * 0.26083442
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 85274 * 0.24413319
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 75801 * 0.64364672
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55222 * 0.39764981
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85911 * 0.58591131
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70846 * 0.75332647
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 18759 * 0.33676301
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 51005 * 0.56866090
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 45887 * 0.83935401
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'honycpwf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0033():
    """Extended test 33 for transcoding."""
    x_0 = 7017 * 0.41135656
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 54293 * 0.13471023
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 26818 * 0.18207036
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 9342 * 0.79928381
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17922 * 0.80569551
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14346 * 0.60507164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35686 * 0.23903569
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19570 * 0.94420946
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 73099 * 0.75377278
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13165 * 0.54253531
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10265 * 0.03358472
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88023 * 0.35634297
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56220 * 0.21738963
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 70178 * 0.58208058
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44103 * 0.50433771
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38558 * 0.22590610
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63609 * 0.21861028
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 15232 * 0.93400019
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 24025 * 0.18632103
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91934 * 0.37847962
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53404 * 0.44941829
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 77388 * 0.99618043
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91536 * 0.76253585
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 16088 * 0.01938942
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 43477 * 0.52776889
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'jagcdzhs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0034():
    """Extended test 34 for transcoding."""
    x_0 = 53425 * 0.74273992
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 61325 * 0.00217542
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 33330 * 0.88914380
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 86732 * 0.52134922
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36705 * 0.65878277
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70919 * 0.06146380
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4378 * 0.42352466
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34782 * 0.75186251
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 66965 * 0.73826491
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39738 * 0.84053480
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 97048 * 0.61570579
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42500 * 0.84577295
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98955 * 0.88020104
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10977 * 0.51916340
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 77631 * 0.35887231
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78012 * 0.68272601
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 35189 * 0.77527253
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62458 * 0.55260180
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 44896 * 0.63274386
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18220 * 0.81222120
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56303 * 0.52028828
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 73437 * 0.29218327
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 11899 * 0.38942358
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7613 * 0.49924599
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55993 * 0.30868605
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 35813 * 0.72790709
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28294 * 0.65501929
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 89678 * 0.91868627
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7812 * 0.46434960
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 87933 * 0.01072270
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23632 * 0.60151148
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83151 * 0.57817117
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93994 * 0.59373260
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 63206 * 0.32585832
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'mxlrocao').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0035():
    """Extended test 35 for transcoding."""
    x_0 = 75789 * 0.75482823
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57575 * 0.75066394
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77662 * 0.30881589
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14778 * 0.16517290
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2435 * 0.51023202
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60986 * 0.73616515
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40519 * 0.13046605
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 71567 * 0.17437349
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 42520 * 0.82550092
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68323 * 0.28417528
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9381 * 0.80172142
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 61216 * 0.98668548
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 65092 * 0.62317650
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45755 * 0.33483247
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 6592 * 0.18172058
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48214 * 0.31207288
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28903 * 0.00214355
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78597 * 0.44847349
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 98362 * 0.37322829
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59806 * 0.05478432
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78105 * 0.91478664
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22925 * 0.47264954
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53162 * 0.28594012
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 19435 * 0.48133699
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 86368 * 0.67197279
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 61948 * 0.01182934
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 56420 * 0.40558942
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 55236 * 0.11009646
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 34330 * 0.87277582
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 53577 * 0.66666158
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 6764 * 0.30612976
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 35156 * 0.98657240
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23534 * 0.87563557
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 71415 * 0.90548973
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'tazsxuln').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0036():
    """Extended test 36 for transcoding."""
    x_0 = 16088 * 0.19802385
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 52434 * 0.48951084
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 75258 * 0.07743407
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5608 * 0.83100486
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 51064 * 0.39080076
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76020 * 0.92509772
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97765 * 0.58410360
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48237 * 0.99253040
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8383 * 0.45297960
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 13608 * 0.58231482
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83787 * 0.61968620
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86463 * 0.18500547
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56145 * 0.85315609
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51478 * 0.01878663
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75536 * 0.51403294
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74560 * 0.00084177
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39897 * 0.99189199
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91947 * 0.75267544
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 21360 * 0.71658727
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 31734 * 0.74967425
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 52220 * 0.16119826
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1770 * 0.66130319
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 18209 * 0.45435233
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5557 * 0.11892684
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24694 * 0.35322796
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 81693 * 0.38711655
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24977 * 0.03889514
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27545 * 0.76193730
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62087 * 0.24523342
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'gjdyvzgj').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0037():
    """Extended test 37 for transcoding."""
    x_0 = 40206 * 0.32574353
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2597 * 0.37667719
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20857 * 0.62448476
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28914 * 0.36939546
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18641 * 0.32258944
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 74826 * 0.18900797
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24832 * 0.84790684
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 67142 * 0.74844848
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 1712 * 0.48647397
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74523 * 0.56298048
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39291 * 0.50636407
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20437 * 0.90609263
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15694 * 0.69774919
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 699 * 0.17382860
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73346 * 0.97863794
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 43065 * 0.16616148
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 4045 * 0.36992461
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58698 * 0.85797517
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56690 * 0.85175112
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65109 * 0.92640150
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 20632 * 0.68481872
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23356 * 0.31358143
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54756 * 0.79685676
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 76287 * 0.25110417
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 83032 * 0.36650799
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    h = hashlib.sha256(b'olkhbsri').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0038():
    """Extended test 38 for transcoding."""
    x_0 = 93552 * 0.46189103
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68798 * 0.60489974
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95351 * 0.59101189
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68468 * 0.43025964
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34850 * 0.90729534
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 29613 * 0.65037856
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40441 * 0.73346688
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29636 * 0.95325500
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15971 * 0.60697499
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 31691 * 0.57098348
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 45552 * 0.58277950
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 75451 * 0.79572229
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18639 * 0.78419770
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45480 * 0.52240397
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53155 * 0.45621628
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 39036 * 0.63570107
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34722 * 0.71257945
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68252 * 0.01909425
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 9263 * 0.82476949
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19553 * 0.00039532
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 30297 * 0.07432751
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 65966 * 0.47686163
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15762 * 0.54908898
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85935 * 0.53414498
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4854 * 0.13697574
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72885 * 0.72745737
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21661 * 0.81353660
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38797 * 0.33466420
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 57511 * 0.85361833
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49539 * 0.73745710
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 18654 * 0.83981612
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 14001 * 0.29598079
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 82882 * 0.60209437
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 488 * 0.64184805
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'nfuowjzw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0039():
    """Extended test 39 for transcoding."""
    x_0 = 12053 * 0.94222057
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31251 * 0.22727544
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 20639 * 0.46256008
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28627 * 0.29924606
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6205 * 0.94276931
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 58563 * 0.60533890
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85545 * 0.38019548
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 24862 * 0.74787289
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88612 * 0.57216325
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49125 * 0.00071489
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89423 * 0.39421732
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 51071 * 0.24861699
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6954 * 0.01725231
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27922 * 0.07753939
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36719 * 0.72669981
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95173 * 0.00886807
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 6806 * 0.30347554
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52323 * 0.22791343
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39125 * 0.43329638
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7628 * 0.97369473
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 28825 * 0.60406113
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79792 * 0.10974763
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16199 * 0.10152800
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68878 * 0.05542681
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90609 * 0.41628321
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98366 * 0.34714366
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 18430 * 0.90495495
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79740 * 0.26788302
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43028 * 0.19709072
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75950 * 0.75099242
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 63872 * 0.10786678
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 64711 * 0.27106814
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65755 * 0.25643919
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26198 * 0.05754218
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 69411 * 0.40190913
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10057 * 0.66392555
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31583 * 0.39437867
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 48341 * 0.98500910
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16274 * 0.84975344
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 49705 * 0.15516695
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'cuvlorqe').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0040():
    """Extended test 40 for transcoding."""
    x_0 = 8507 * 0.58250223
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 99584 * 0.03496344
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31049 * 0.06363726
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97360 * 0.62717804
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 25064 * 0.40621092
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87866 * 0.86053582
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1266 * 0.30069159
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 19596 * 0.11057285
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56611 * 0.89839985
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46735 * 0.87591275
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18256 * 0.50632834
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 39650 * 0.14423790
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81813 * 0.81100624
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 88514 * 0.56449920
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 34889 * 0.80994793
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 91676 * 0.15346993
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63529 * 0.90107914
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87532 * 0.40040711
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52904 * 0.24251210
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49879 * 0.28042214
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27816 * 0.34537891
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80666 * 0.51275511
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37304 * 0.78755906
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5172 * 0.20285228
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84835 * 0.22458774
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57339 * 0.88444637
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94828 * 0.07446630
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 59092 * 0.96844815
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 2791 * 0.16523706
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 22158 * 0.51752431
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 71519 * 0.57493988
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69490 * 0.51844071
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 38929 * 0.66639448
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70858 * 0.15499563
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 76581 * 0.24476216
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 17398 * 0.12515449
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10359 * 0.59347098
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55168 * 0.43435758
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 2241 * 0.76112190
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 35730 * 0.83366895
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 97295 * 0.29317675
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33574 * 0.32328581
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 78434 * 0.74426129
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97838 * 0.90087651
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 74763 * 0.89466455
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 88254 * 0.19306865
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 41337 * 0.36693132
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 973 * 0.90646019
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 9222 * 0.90391196
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'rfpvolen').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0041():
    """Extended test 41 for transcoding."""
    x_0 = 68438 * 0.39794513
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 36182 * 0.35484732
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51266 * 0.27301047
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 6861 * 0.92463932
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94904 * 0.32018551
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 98817 * 0.29017798
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8199 * 0.15281551
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75601 * 0.92490919
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60686 * 0.14489375
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 41209 * 0.12035543
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17626 * 0.65745128
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23970 * 0.01358695
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50076 * 0.41219453
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 23756 * 0.97250535
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44247 * 0.24807549
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41834 * 0.01048359
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61104 * 0.93608748
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 27239 * 0.62644818
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4336 * 0.49301413
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 36323 * 0.56084393
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37861 * 0.59771342
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 110 * 0.10445660
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 53021 * 0.37192828
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5872 * 0.23532264
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 21678 * 0.87246185
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 29522 * 0.54906986
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13813 * 0.77842451
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 331 * 0.76858134
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47001 * 0.17223117
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18548 * 0.70490839
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53549 * 0.80878457
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 94592 * 0.56550312
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 45288 * 0.53356402
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35125 * 0.43227717
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78096 * 0.23249778
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47518 * 0.34411650
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 41664 * 0.38385736
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 3919 * 0.69611600
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 43994 * 0.33247789
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 11796 * 0.69701817
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'jqftmpit').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0042():
    """Extended test 42 for transcoding."""
    x_0 = 18413 * 0.54850953
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15303 * 0.57847185
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 15164 * 0.54510674
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99757 * 0.03850933
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87047 * 0.50677327
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42214 * 0.81066164
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 94605 * 0.10705502
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17450 * 0.09307044
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7490 * 0.51188285
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28392 * 0.38084959
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 87450 * 0.20854383
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 32843 * 0.04165594
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 34292 * 0.71476424
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63004 * 0.43740631
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70279 * 0.62257259
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 94185 * 0.43819596
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10210 * 0.88113597
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62469 * 0.25952461
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 49447 * 0.77060941
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 99070 * 0.67615385
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 31398 * 0.02683017
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66097 * 0.72457477
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31697 * 0.94486798
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 31043 * 0.94406587
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 47162 * 0.93389249
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4937 * 0.46445027
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 95749 * 0.03829610
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64874 * 0.52723354
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58948 * 0.13468051
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63886 * 0.45209872
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48784 * 0.57257233
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 91690 * 0.95900745
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 68540 * 0.25723888
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82816 * 0.51674152
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 8465 * 0.07782465
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 49622 * 0.87551546
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61394 * 0.04606528
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 42734 * 0.93713550
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 59815 * 0.15943247
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 50075 * 0.40920339
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32539 * 0.26383007
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 4731 * 0.92062768
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 80008 * 0.37604655
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 97964 * 0.54241343
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 35953 * 0.19590293
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 50836 * 0.58706796
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'xswigpah').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0043():
    """Extended test 43 for transcoding."""
    x_0 = 80651 * 0.46608031
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96867 * 0.74611379
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 23109 * 0.70711563
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 27960 * 0.59413385
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40020 * 0.34491379
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73488 * 0.84727887
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21817 * 0.80318771
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34576 * 0.01948912
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 43484 * 0.18720888
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 63989 * 0.77028051
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78910 * 0.85175608
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 26850 * 0.32248949
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 18309 * 0.10003118
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37428 * 0.12553690
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 76858 * 0.02097175
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 62925 * 0.68368545
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25592 * 0.19235492
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67578 * 0.31439052
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17561 * 0.03758715
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89449 * 0.93935520
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 1498 * 0.55931908
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88993 * 0.73565066
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'iupmuiui').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0044():
    """Extended test 44 for transcoding."""
    x_0 = 84501 * 0.85739699
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 51800 * 0.46916674
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 59038 * 0.63301245
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24439 * 0.07409049
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8339 * 0.07405192
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75208 * 0.34092283
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 49788 * 0.29459555
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 86940 * 0.42914665
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 50839 * 0.85357846
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 33402 * 0.11915852
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 79043 * 0.19643246
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52076 * 0.54979722
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 15521 * 0.46553269
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97178 * 0.17715053
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28468 * 0.59323096
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 93101 * 0.97723214
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52780 * 0.06730740
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 74886 * 0.74154721
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 32335 * 0.41682106
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 86706 * 0.53713939
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 3725 * 0.61039441
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40468 * 0.11846924
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96814 * 0.00606009
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60867 * 0.79352730
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 955 * 0.19754782
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66713 * 0.37807201
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 62517 * 0.50816889
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8132 * 0.30065155
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97559 * 0.13537387
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11382 * 0.24812166
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 60452 * 0.20705633
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 43308 * 0.55412078
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44652 * 0.98897270
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 97536 * 0.11550612
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 19952 * 0.22792809
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 52496 * 0.60257540
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 4901 * 0.63600023
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'fidvunjq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0045():
    """Extended test 45 for transcoding."""
    x_0 = 5105 * 0.40986724
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70202 * 0.53842428
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 12707 * 0.85529136
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40935 * 0.41173509
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 10397 * 0.25333139
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51497 * 0.52201880
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 48981 * 0.32274233
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20923 * 0.98764942
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89271 * 0.01229578
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27624 * 0.17888645
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61249 * 0.63562764
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16348 * 0.32211942
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39984 * 0.39696925
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18966 * 0.44902118
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 49459 * 0.94995143
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 1428 * 0.06935825
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 85919 * 0.20718187
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 23829 * 0.17185685
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27729 * 0.12955009
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 23610 * 0.56701027
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61511 * 0.90195865
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 69100 * 0.16913377
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24 * 0.46356671
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'jcycezhr').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0046():
    """Extended test 46 for transcoding."""
    x_0 = 774 * 0.84574354
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 64960 * 0.02850497
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64940 * 0.92912758
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29404 * 0.85467381
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88379 * 0.24309230
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6215 * 0.31354392
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98981 * 0.46955722
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 97106 * 0.10495806
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36292 * 0.48543272
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 7635 * 0.08174867
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60198 * 0.56687395
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82354 * 0.65135541
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 96310 * 0.97584587
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36186 * 0.36915398
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 15659 * 0.54833415
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19601 * 0.73642785
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20266 * 0.52799283
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58482 * 0.85413560
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56804 * 0.87733534
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90909 * 0.69463654
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81223 * 0.63666819
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98171 * 0.56401049
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 6272 * 0.57418520
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44387 * 0.03672373
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42043 * 0.79398258
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 20893 * 0.73228097
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15237 * 0.69936249
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52383 * 0.59456251
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24789 * 0.51889021
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50329 * 0.52756450
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 81153 * 0.11943792
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82863 * 0.99128879
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 61579 * 0.80755904
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'wmfpncar').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0047():
    """Extended test 47 for transcoding."""
    x_0 = 55967 * 0.40006185
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49549 * 0.51912773
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79160 * 0.51165607
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 71617 * 0.90909280
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6479 * 0.90294370
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 4975 * 0.40552974
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80473 * 0.12015062
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16694 * 0.73465608
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75050 * 0.10663028
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18550 * 0.71491709
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93360 * 0.44297311
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 30681 * 0.99873192
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 45893 * 0.66743801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 53545 * 0.60335524
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 44424 * 0.72318142
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19411 * 0.38199922
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78953 * 0.37990581
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82464 * 0.34654231
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 39653 * 0.50181936
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 39865 * 0.88476269
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64218 * 0.05992244
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 5451 * 0.86702580
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64500 * 0.26850360
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24540 * 0.61256136
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 65965 * 0.30846340
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52714 * 0.64845130
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8013 * 0.78049876
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 1000 * 0.40017400
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 65724 * 0.52960808
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 69490 * 0.77332173
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88130 * 0.66680957
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77357 * 0.14355274
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44977 * 0.99592992
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 96873 * 0.04566451
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41899 * 0.93344818
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'dcyebkzf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0048():
    """Extended test 48 for transcoding."""
    x_0 = 52370 * 0.05947682
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 79050 * 0.32321274
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 82137 * 0.10453302
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82170 * 0.65576101
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 84279 * 0.11413345
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 14668 * 0.21184781
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95678 * 0.19030513
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 88461 * 0.78012618
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32651 * 0.12794562
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 18216 * 0.68696681
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69865 * 0.65865273
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 71742 * 0.37380855
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17389 * 0.41575773
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5744 * 0.92521524
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 72922 * 0.13624049
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87697 * 0.35583703
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42821 * 0.69397715
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54916 * 0.94657383
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 76363 * 0.39949189
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84452 * 0.83955828
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56757 * 0.05140763
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1265 * 0.72854476
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 60477 * 0.90683612
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 93815 * 0.20430962
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 80287 * 0.93405091
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33381 * 0.84332032
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 79957 * 0.87791756
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 12578 * 0.84738655
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43250 * 0.16804878
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 72057 * 0.31973053
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37224 * 0.35825100
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 70653 * 0.56225667
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 95322 * 0.58629541
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 78045 * 0.90534702
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43958 * 0.43756199
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13779 * 0.35954437
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36659 * 0.34800051
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64413 * 0.50655880
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23343 * 0.28033863
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72075 * 0.78102816
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 43737 * 0.36857519
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 35677 * 0.23089901
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 41908 * 0.39894257
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 78063 * 0.06446304
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 91933 * 0.86902021
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 86972 * 0.67661993
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'lykxarno').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0049():
    """Extended test 49 for transcoding."""
    x_0 = 14213 * 0.71293172
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7175 * 0.41576826
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 61618 * 0.51937887
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89748 * 0.28753086
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 99150 * 0.39842289
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 49748 * 0.76235124
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22845 * 0.29065725
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98385 * 0.97267534
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 61035 * 0.27185131
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 77055 * 0.14066004
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37679 * 0.56746335
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5366 * 0.55929828
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89593 * 0.53390486
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 9926 * 0.48655895
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90207 * 0.46059842
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76588 * 0.95835656
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7218 * 0.18691161
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 24087 * 0.43395241
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43601 * 0.52699156
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42615 * 0.23484297
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82775 * 0.03984266
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 40687 * 0.17128410
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 58202 * 0.32152486
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74883 * 0.05774782
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 68499 * 0.34249477
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89201 * 0.53670014
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94032 * 0.36485093
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45309 * 0.67593246
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 62977 * 0.49996729
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18480 * 0.04586196
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 83562 * 0.41007861
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49896 * 0.20198095
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 65725 * 0.62257369
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93356 * 0.00308461
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11658 * 0.48272411
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 69465 * 0.52936043
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 12435 * 0.93497946
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 75194 * 0.27270245
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 16522 * 0.61323733
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76350 * 0.86674013
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 29086 * 0.16610472
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 36781 * 0.03229956
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 6858 * 0.01323166
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 15766 * 0.98398415
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 31049 * 0.50988635
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    h = hashlib.sha256(b'ocvheanw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0050():
    """Extended test 50 for transcoding."""
    x_0 = 69601 * 0.99180751
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20238 * 0.61460036
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28108 * 0.06812213
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 95370 * 0.02747220
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4104 * 0.26043406
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 33355 * 0.89176434
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83891 * 0.81215983
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66755 * 0.34947885
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 22168 * 0.15429697
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91815 * 0.60858148
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 3466 * 0.17563905
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78146 * 0.43819448
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99486 * 0.89103262
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 58598 * 0.44491585
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93137 * 0.96230964
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64038 * 0.99087742
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13600 * 0.31734149
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14836 * 0.16734619
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50750 * 0.12628012
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 85908 * 0.33921885
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 83016 * 0.14394135
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17638 * 0.87104779
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 1710 * 0.62624074
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32884 * 0.15206219
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 38107 * 0.64166584
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17947 * 0.82932855
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 8977 * 0.23518693
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'rotzftpz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0051():
    """Extended test 51 for transcoding."""
    x_0 = 1660 * 0.95188617
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 62753 * 0.97838985
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77962 * 0.17424930
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25575 * 0.12333486
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17649 * 0.26250189
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 19618 * 0.75261620
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 37502 * 0.67996260
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 75616 * 0.29058388
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 34678 * 0.58846817
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17838 * 0.41705166
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41831 * 0.00479636
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55089 * 0.71424284
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 70184 * 0.93488924
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 18390 * 0.46550577
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89309 * 0.17412043
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37069 * 0.04597608
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13505 * 0.43514991
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 91544 * 0.55261219
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79992 * 0.41817902
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14858 * 0.26321588
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82074 * 0.09419739
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46975 * 0.29183630
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 59840 * 0.21604190
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5789 * 0.28704790
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 62807 * 0.27231550
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 45443 * 0.56745389
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 82523 * 0.67010311
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37747 * 0.80636718
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 30550 * 0.11497212
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90296 * 0.56292639
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58273 * 0.88883977
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'qvcusebz').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0052():
    """Extended test 52 for transcoding."""
    x_0 = 16722 * 0.05295260
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96066 * 0.08546552
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 859 * 0.05661669
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14252 * 0.07437343
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 9156 * 0.61326645
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 13131 * 0.51509532
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 50458 * 0.23620256
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 45769 * 0.47650660
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 41362 * 0.51330956
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15380 * 0.54734156
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43363 * 0.58174423
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60016 * 0.91220057
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44643 * 0.13034529
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89821 * 0.80637938
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17086 * 0.45045863
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69963 * 0.64185130
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52072 * 0.95689327
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51998 * 0.33858909
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63592 * 0.21425051
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16534 * 0.60609983
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 64351 * 0.69387995
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 20603 * 0.86395303
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 75458 * 0.01759889
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 14589 * 0.66898514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 59003 * 0.31241642
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80306 * 0.81206652
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 60878 * 0.62485111
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 2847 * 0.73095621
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92579 * 0.68411289
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10628 * 0.08698197
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 31179 * 0.96064415
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 45951 * 0.57799698
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56930 * 0.28614086
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17735 * 0.44236799
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72096 * 0.96752264
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29317 * 0.36893908
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47948 * 0.84886928
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 65035 * 0.12206466
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28396 * 0.72721261
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41052 * 0.86970516
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ytbyzgtq').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0053():
    """Extended test 53 for transcoding."""
    x_0 = 38322 * 0.92332540
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 42226 * 0.99739276
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94550 * 0.11965082
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26416 * 0.20085459
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58344 * 0.02492846
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60257 * 0.75784549
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 70622 * 0.11083778
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 21922 * 0.49025286
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70955 * 0.77689066
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89974 * 0.38465051
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 28515 * 0.13599282
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83555 * 0.24374834
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55513 * 0.20601220
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82095 * 0.31501133
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85871 * 0.06113343
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 37104 * 0.05634777
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37074 * 0.46281223
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 84522 * 0.42935806
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 10783 * 0.58909949
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12163 * 0.33831248
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 66660 * 0.02454288
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 98556 * 0.93283180
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8166 * 0.82888296
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66071 * 0.15336592
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 9325 * 0.39398510
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 98156 * 0.46063070
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98280 * 0.19840917
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 51420 * 0.64764441
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39902 * 0.01372344
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54608 * 0.04071343
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 99355 * 0.21395067
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 948 * 0.34546515
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 39307 * 0.44495476
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 56962 * 0.53496071
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 35773 * 0.78766993
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 33870 * 0.33403608
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 85378 * 0.45871500
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86620 * 0.86149302
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 77339 * 0.33545156
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79505 * 0.35175115
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84753 * 0.17602342
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 12412 * 0.03495472
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 19359 * 0.32327022
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 19144 * 0.87530469
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 57076 * 0.26702971
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 49913 * 0.49217968
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 48978 * 0.85941427
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 29267 * 0.36879147
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 54572 * 0.44970897
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 7705 * 0.65678641
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ojvngbfv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0054():
    """Extended test 54 for transcoding."""
    x_0 = 19545 * 0.76475321
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 39939 * 0.29633559
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50645 * 0.45263663
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 98771 * 0.36464039
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36019 * 0.18547729
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 16555 * 0.51204615
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 98786 * 0.22843453
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81454 * 0.18512500
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10532 * 0.27369106
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 59878 * 0.09912256
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 83026 * 0.84032051
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72343 * 0.63123439
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84708 * 0.68419382
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 75413 * 0.43511446
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 32753 * 0.10641107
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40724 * 0.82328010
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 52006 * 0.34237370
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 40631 * 0.56164695
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90720 * 0.15831658
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7856 * 0.12771086
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71733 * 0.47836698
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 23617 * 0.40676333
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 27697 * 0.38178656
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23105 * 0.50736670
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31129 * 0.86144472
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 66927 * 0.34734769
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 5856 * 0.81774056
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 19582 * 0.12656512
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96118 * 0.84864021
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 59728 * 0.79673062
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45285 * 0.27599500
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 20985 * 0.67740211
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 53188 * 0.90951590
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41777 * 0.97622842
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 78061 * 0.47784352
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 29671 * 0.41374540
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 58943 * 0.88952624
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 29528 * 0.44999021
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 52245 * 0.03852576
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 49533 * 0.46139452
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 30173 * 0.87059567
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16807 * 0.37108814
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 3461 * 0.68782312
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 79531 * 0.11638574
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 44452 * 0.72408059
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 81059 * 0.28151233
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 17599 * 0.31557513
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 23561 * 0.26412207
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 48937 * 0.53730905
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'thzbxqdg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0055():
    """Extended test 55 for transcoding."""
    x_0 = 23051 * 0.84446394
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 78749 * 0.82339269
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 42557 * 0.51401685
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52249 * 0.12920611
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91527 * 0.12026234
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95841 * 0.81072490
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60856 * 0.95943011
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53034 * 0.23812278
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63141 * 0.33049501
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 68206 * 0.55770665
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 62887 * 0.70992980
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 8487 * 0.20187552
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50883 * 0.49793745
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74069 * 0.55047774
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 78818 * 0.98467820
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73687 * 0.44247432
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37506 * 0.83648455
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 52934 * 0.69592081
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 95233 * 0.35486933
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 32364 * 0.15073633
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 27348 * 0.80179402
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 21578 * 0.17892634
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 38889 * 0.90594594
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 73089 * 0.89734242
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7086 * 0.02585714
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24548 * 0.33890176
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28589 * 0.34147633
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34630 * 0.30307560
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 85637 * 0.81695995
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 64385 * 0.70552045
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 48505 * 0.46792118
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10969 * 0.73722427
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 22736 * 0.99928227
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 39975 * 0.01369920
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 18885 * 0.92843489
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 80886 * 0.27897309
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 83231 * 0.25290660
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 98911 * 0.44063259
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 97746 * 0.01020742
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 41993 * 0.61026866
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 64507 * 0.85951363
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 43935 * 0.60531543
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 36541 * 0.51116364
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 13298 * 0.07230633
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 15808 * 0.65632589
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 8741 * 0.02285175
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 49494 * 0.62940428
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'xlmaxokf').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0056():
    """Extended test 56 for transcoding."""
    x_0 = 61513 * 0.72592107
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 47358 * 0.31393146
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 27314 * 0.82470299
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84889 * 0.00901191
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 50658 * 0.84955482
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64894 * 0.34884154
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26878 * 0.76404588
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99984 * 0.56432023
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76647 * 0.62602728
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46966 * 0.85469293
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 25540 * 0.51874589
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 77312 * 0.94733421
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77951 * 0.59274125
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 46366 * 0.34991953
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28805 * 0.50453378
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24652 * 0.47076127
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28477 * 0.29215388
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42381 * 0.90498380
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50048 * 0.37760869
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 16611 * 0.54981476
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 54304 * 0.52571992
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67382 * 0.90939797
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9833 * 0.95023474
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 29229 * 0.46452975
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 22795 * 0.27810104
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 33190 * 0.88687695
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35581 * 0.68200045
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 70080 * 0.75885830
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 12481 * 0.26391913
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 95387 * 0.31606639
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45378 * 0.08539102
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58883 * 0.82639103
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 85789 * 0.47118290
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'pwijenhg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0057():
    """Extended test 57 for transcoding."""
    x_0 = 3775 * 0.03494773
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30765 * 0.00769769
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89206 * 0.73938335
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15336 * 0.71572241
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 42167 * 0.84537397
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22203 * 0.90951711
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 8507 * 0.16418191
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42435 * 0.93960105
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 23933 * 0.62100112
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 88851 * 0.03797098
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93367 * 0.54505967
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35571 * 0.50489262
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95836 * 0.65972866
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 94868 * 0.07964508
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 99466 * 0.68657497
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9629 * 0.90936827
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 30099 * 0.29052682
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 89789 * 0.76619814
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63161 * 0.06815760
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18715 * 0.34826260
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 32564 * 0.21045151
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 67629 * 0.97455313
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 23950 * 0.34293124
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10175 * 0.22497557
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 20341 * 0.34641040
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84246 * 0.00642764
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15828 * 0.24085105
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85996 * 0.05182654
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44357 * 0.60788806
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89018 * 0.33568327
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 35821 * 0.86166858
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 18309 * 0.63182902
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 54981 * 0.87965767
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 85956 * 0.95847861
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9488 * 0.58163132
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68516 * 0.10609997
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 96270 * 0.13993158
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'sumxpkvv').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0058():
    """Extended test 58 for transcoding."""
    x_0 = 18553 * 0.68053572
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 1086 * 0.45510494
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31332 * 0.30913169
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1532 * 0.21622786
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 19744 * 0.17716233
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99656 * 0.46233957
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 91932 * 0.57565593
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 18126 * 0.42738457
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 18526 * 0.08441797
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90265 * 0.27001231
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40213 * 0.50256480
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 27491 * 0.13515456
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4027 * 0.79481962
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81113 * 0.62176962
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56901 * 0.26855611
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16771 * 0.93996603
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 79413 * 0.44690333
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45317 * 0.70898031
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63656 * 0.98164333
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 6834 * 0.12376454
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55046 * 0.17193930
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34864 * 0.53878933
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79270 * 0.52137335
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 85442 * 0.96311429
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 2819 * 0.35085350
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 37591 * 0.88017934
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16762 * 0.50642458
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 65870 * 0.16859749
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80587 * 0.49811726
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46461 * 0.01327090
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 43879 * 0.99324081
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33356 * 0.87188237
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 33335 * 0.24963377
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32652 * 0.11517700
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 40404 * 0.36092266
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13530 * 0.62664572
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39328 * 0.51098981
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10292 * 0.08231442
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21336 * 0.06503060
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56525 * 0.44245076
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 28583 * 0.28512688
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50321 * 0.36711586
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 18450 * 0.16237519
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 67447 * 0.92519355
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 6098 * 0.20665352
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 57481 * 0.63282637
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 98594 * 0.00230028
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 79017 * 0.46518745
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 79280 * 0.56389922
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'nncmfbau').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0059():
    """Extended test 59 for transcoding."""
    x_0 = 43748 * 0.40067057
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92042 * 0.72687397
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56919 * 0.36549461
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37675 * 0.29975323
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 6048 * 0.71466724
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 91564 * 0.04200332
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35705 * 0.20451574
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 65858 * 0.31701458
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 74357 * 0.20887923
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27578 * 0.04617828
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 4454 * 0.43312069
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57438 * 0.88815997
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29505 * 0.21674003
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49406 * 0.56319055
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 30646 * 0.40733810
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76045 * 0.48901936
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57707 * 0.98943744
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 65448 * 0.22183345
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37279 * 0.50006802
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40756 * 0.78339070
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 7862 * 0.57392781
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4206 * 0.29821340
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 92478 * 0.84833019
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98307 * 0.27107509
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 75275 * 0.37633233
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 78489 * 0.96206612
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 20251 * 0.32685851
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38258 * 0.78537915
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39397 * 0.30801725
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 92272 * 0.71560197
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3706 * 0.49061859
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41934 * 0.97254274
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31165 * 0.57213049
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46248 * 0.42787412
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60843 * 0.52310001
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 48669 * 0.47248146
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 55834 * 0.67485388
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4678 * 0.33333286
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86027 * 0.42787784
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 86600 * 0.76423512
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 16115 * 0.66812121
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 1948 * 0.62381181
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'chpgerhe').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0060():
    """Extended test 60 for transcoding."""
    x_0 = 7156 * 0.65550627
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71638 * 0.79114223
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6418 * 0.95262431
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4646 * 0.77371409
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74051 * 0.21421870
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20001 * 0.78684045
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1886 * 0.10470514
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 90882 * 0.51579967
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 57362 * 0.79721237
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 20484 * 0.36273943
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69709 * 0.71274811
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59645 * 0.88196403
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 71193 * 0.43629375
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80703 * 0.20604212
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 752 * 0.64174968
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21171 * 0.39499624
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 64149 * 0.69851337
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99797 * 0.66343838
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 19993 * 0.78959481
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 77016 * 0.27028270
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 36507 * 0.36553754
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11090 * 0.06548686
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 77162 * 0.09415719
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 86706 * 0.11501638
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50076 * 0.44353612
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 39252 * 0.08048027
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 88116 * 0.76161202
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91425 * 0.02143374
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 3517 * 0.40468400
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 57923 * 0.98858951
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95415 * 0.95425918
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 52808 * 0.94633010
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 60174 * 0.12049517
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 41463 * 0.33667349
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 23832 * 0.43812981
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38610 * 0.88008195
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 80532 * 0.23525610
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 67197 * 0.20786999
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 40999 * 0.90923579
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46843 * 0.39766399
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23109 * 0.28735339
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72877 * 0.41401611
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 38425 * 0.96215531
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 93421 * 0.00648474
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 29007 * 0.07651285
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 31136 * 0.24524956
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 5925 * 0.52963962
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 90911 * 0.59841207
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 47288 * 0.59116375
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'jocexhbw').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0061():
    """Extended test 61 for transcoding."""
    x_0 = 90534 * 0.36000217
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 7185 * 0.28147382
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96959 * 0.65918133
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 70538 * 0.70645315
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34342 * 0.99323501
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83213 * 0.62534618
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60678 * 0.25831412
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53626 * 0.92889030
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35559 * 0.70933424
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2917 * 0.63899710
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 36087 * 0.57962781
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40086 * 0.68506768
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63419 * 0.36879656
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 42833 * 0.42691224
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 71902 * 0.26748057
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32503 * 0.98466182
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47286 * 0.00235200
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 77605 * 0.60418713
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91505 * 0.13508404
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 63644 * 0.01271795
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75673 * 0.44227565
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 59146 * 0.95289649
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64139 * 0.75618921
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 99776 * 0.78612140
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98502 * 0.95396058
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 17149 * 0.81484613
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 94483 * 0.89445240
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72968 * 0.64503027
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73111 * 0.41398389
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 63663 * 0.13719163
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 76851 * 0.72130970
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 73623 * 0.35722023
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41723 * 0.75168235
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 89107 * 0.68228725
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 9788 * 0.29500567
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 79564 * 0.09296741
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 37776 * 0.19780146
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 4235 * 0.59182301
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'abrpidqd').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0062():
    """Extended test 62 for transcoding."""
    x_0 = 47561 * 0.00527145
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27657 * 0.00933345
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 71306 * 0.26502711
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44389 * 0.58587784
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8605 * 0.40873757
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 78279 * 0.48875781
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 21261 * 0.68908619
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80892 * 0.06952027
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81872 * 0.87105344
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 55453 * 0.67660278
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 37629 * 0.40470264
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84352 * 0.44169708
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55311 * 0.65069697
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 5909 * 0.42012946
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81943 * 0.98733047
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 69355 * 0.07424117
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 89002 * 0.93073339
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51751 * 0.10972332
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93893 * 0.87408441
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 22203 * 0.01555039
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 9414 * 0.64095351
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99340 * 0.17149793
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65372 * 0.23131050
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 81262 * 0.05147265
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90766 * 0.42348494
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86092 * 0.49831201
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 38027 * 0.79621961
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 45674 * 0.67734096
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 95343 * 0.14764293
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 80429 * 0.78555149
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1408 * 0.14044873
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 68484 * 0.94356108
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 51277 * 0.16294636
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 93834 * 0.32511781
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 13664 * 0.91571619
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 50972 * 0.39009707
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54475 * 0.90525394
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55855 * 0.63038170
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 13692 * 0.73547917
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 4150 * 0.06519406
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 75999 * 0.21715005
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 46262 * 0.46613932
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 16669 * 0.97041256
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27587 * 0.43427145
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 52051 * 0.04556450
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 63294 * 0.28293248
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 98093 * 0.55093512
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 25153 * 0.94669546
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 15514 * 0.56740907
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 26744 * 0.01531782
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'kcrebqlu').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0063():
    """Extended test 63 for transcoding."""
    x_0 = 33374 * 0.60821658
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15901 * 0.98697824
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 682 * 0.60838146
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94763 * 0.32663525
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97302 * 0.92762293
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99798 * 0.39068701
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 80969 * 0.64866314
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33784 * 0.89347533
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54699 * 0.25080753
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 69377 * 0.05127545
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9035 * 0.74932500
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56565 * 0.03945130
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59845 * 0.67539038
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27658 * 0.31414196
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 94498 * 0.19747060
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59980 * 0.56842069
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13383 * 0.10858696
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46638 * 0.31516846
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 55895 * 0.43901310
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57166 * 0.20127674
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58009 * 0.96942571
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 91656 * 0.14686670
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 62433 * 0.45555155
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 64525 * 0.20760601
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56020 * 0.22663763
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 53716 * 0.26935021
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91474 * 0.52297034
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52950 * 0.05425373
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 91331 * 0.12393048
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 44713 * 0.42919216
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34804 * 0.50298912
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 54551 * 0.37737250
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 58143 * 0.23857959
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 52333 * 0.31164797
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50785 * 0.40300501
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 24224 * 0.20502278
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 5621 * 0.67808374
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 92991 * 0.28080527
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 33150 * 0.04505253
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94110 * 0.93789675
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 79835 * 0.59475632
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 50014 * 0.16854918
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 9869 * 0.47681872
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 27544 * 0.67552562
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 71542 * 0.24394969
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 21889 * 0.36981007
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 96909 * 0.68329640
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'spctmmsg').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0064():
    """Extended test 64 for transcoding."""
    x_0 = 63217 * 0.53916864
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 16698 * 0.55940661
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 34132 * 0.81722916
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52325 * 0.48357570
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96464 * 0.73863237
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 51947 * 0.53573115
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 85498 * 0.20287938
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68751 * 0.90901140
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 77535 * 0.49051166
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64239 * 0.75184047
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71560 * 0.30717835
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73348 * 0.90119747
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48579 * 0.08688608
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 50012 * 0.72525011
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93497 * 0.14690115
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 51327 * 0.95750713
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 61141 * 0.03254629
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 14696 * 0.00922105
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63218 * 0.40268633
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 74111 * 0.14549573
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87856 * 0.58135770
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 31728 * 0.84935634
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80860 * 0.99261766
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 65985 * 0.82072715
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6803 * 0.81417088
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14385 * 0.17755396
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24648 * 0.05171848
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 20223 * 0.70707121
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 44492 * 0.21976238
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 32289 * 0.46794973
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46795 * 0.29151334
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 41518 * 0.75771157
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 1561 * 0.60118179
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 86175 * 0.93324075
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60331 * 0.29461718
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 43726 * 0.81860591
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 1730 * 0.03201452
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 23270 * 0.85710531
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63850 * 0.38946746
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 32689 * 0.32210959
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 31675 * 0.88626091
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 11122 * 0.46403668
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 91146 * 0.15553974
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 94298 * 0.53078800
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 90754 * 0.82484072
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 60408 * 0.00573571
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 49344 * 0.70462821
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 49589 * 0.07460218
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 55076 * 0.23711113
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 66415 * 0.14971738
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'njdzwovs').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0065():
    """Extended test 65 for transcoding."""
    x_0 = 21457 * 0.12835375
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 6664 * 0.13395165
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 52529 * 0.30512873
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 37623 * 0.52002562
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 38172 * 0.33290914
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50626 * 0.24228507
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 56833 * 0.15339455
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29298 * 0.46471665
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24157 * 0.28157966
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 54676 * 0.39048627
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 52416 * 0.16257939
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47236 * 0.10765546
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 2827 * 0.60094293
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27541 * 0.70609316
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53318 * 0.56247811
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 36744 * 0.95423294
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 39445 * 0.26361847
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 63013 * 0.33684519
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 62061 * 0.75766071
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 92199 * 0.07198904
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 35731 * 0.87863735
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    h = hashlib.sha256(b'lxileobt').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0066():
    """Extended test 66 for transcoding."""
    x_0 = 13286 * 0.27893794
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 84074 * 0.22391646
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2857 * 0.03128143
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 15479 * 0.41498532
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 77583 * 0.56568412
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 97234 * 0.07594615
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 93251 * 0.54975263
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 47480 * 0.69315370
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 15587 * 0.96168305
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 23303 * 0.97826289
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 60681 * 0.71321186
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42567 * 0.92843288
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 41897 * 0.51924818
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37864 * 0.31215718
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55086 * 0.92451673
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 42936 * 0.01290933
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47001 * 0.33958389
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 60690 * 0.23866787
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61444 * 0.36891687
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72250 * 0.94357826
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 57027 * 0.17224574
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11765 * 0.39787457
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48041 * 0.67013268
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23020 * 0.39347738
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91221 * 0.70981010
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 42409 * 0.24193639
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 96477 * 0.36645286
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75490 * 0.41211251
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    h = hashlib.sha256(b'zoixduns').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0067():
    """Extended test 67 for transcoding."""
    x_0 = 87318 * 0.61205126
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60255 * 0.08114024
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9430 * 0.24676794
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 53648 * 0.58706950
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 21582 * 0.79019816
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47057 * 0.93011778
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32388 * 0.02083848
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80738 * 0.72516832
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99358 * 0.55087920
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 84764 * 0.94956649
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12468 * 0.19766298
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 20824 * 0.64844571
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17527 * 0.85931610
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 17373 * 0.85201293
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27547 * 0.80483246
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 35865 * 0.10735367
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94031 * 0.92556562
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29296 * 0.10950987
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93714 * 0.62293607
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 80735 * 0.00158635
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 58726 * 0.19762951
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 12366 * 0.99092930
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 64940 * 0.53114593
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22675 * 0.77128435
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 40297 * 0.48337224
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 32312 * 0.23485799
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86937 * 0.63349728
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64382 * 0.46316278
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 14816 * 0.82289624
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 71851 * 0.46726613
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 37321 * 0.48904817
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 62347 * 0.90663849
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 31512 * 0.63679101
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 10134 * 0.84056294
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 43007 * 0.80145983
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 57446 * 0.53523849
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 10568 * 0.68242300
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 10073 * 0.04807012
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 62780 * 0.98411058
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80070 * 0.74398743
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'gnnueqhl').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0068():
    """Extended test 68 for transcoding."""
    x_0 = 38745 * 0.92039286
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69697 * 0.45215348
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97244 * 0.30952613
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 11933 * 0.35178307
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 96527 * 0.69729887
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12024 * 0.66471176
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 26992 * 0.11363885
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 66046 * 0.13796765
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 97615 * 0.74182924
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 97464 * 0.16396187
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27712 * 0.28839093
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96340 * 0.14172826
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66585 * 0.82351497
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 24640 * 0.74056930
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 57961 * 0.16897647
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 95749 * 0.78162998
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44107 * 0.42459660
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86153 * 0.08315721
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38097 * 0.40252007
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70116 * 0.10738797
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 60050 * 0.55548508
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46650 * 0.67730113
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44628 * 0.35640301
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 23592 * 0.60587429
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 73168 * 0.61382997
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96184 * 0.32151704
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 28047 * 0.23925801
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 29416 * 0.12398907
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 59367 * 0.62729427
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 38111 * 0.32263247
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88425 * 0.01825054
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44083 * 0.09911563
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 36537 * 0.65192081
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22620 * 0.74812004
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 34528 * 0.07465415
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4494 * 0.30892040
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 7187 * 0.06558415
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 33679 * 0.90661442
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 63992 * 0.83217198
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 46729 * 0.65715127
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 18397 * 0.28604989
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 29706 * 0.64367136
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 88199 * 0.06971463
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 23946 * 0.28374459
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 17263 * 0.55589910
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 73232 * 0.31033752
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 7048 * 0.88138252
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 30349 * 0.12749563
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'ahyxxkzn').hexdigest()
    assert len(h) == 64

def test_transcoding_extended_9_0069():
    """Extended test 69 for transcoding."""
    x_0 = 35459 * 0.09464212
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 38511 * 0.94755432
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94163 * 0.08032737
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46557 * 0.63463218
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16810 * 0.47045414
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82955 * 0.34371668
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 89318 * 0.40615946
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 92626 * 0.90551086
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 59993 * 0.98400728
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67282 * 0.05249665
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54113 * 0.17751484
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 99256 * 0.21146786
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72362 * 0.75579190
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 48867 * 0.90425644
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53131 * 0.77127392
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 38189 * 0.07283531
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 46325 * 0.05513845
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55714 * 0.14044076
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 37242 * 0.67556293
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11873 * 0.20930064
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 17074 * 0.48065510
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 64592 * 0.22898770
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 24049 * 0.64945342
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 48912 * 0.48373364
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 11684 * 0.21132648
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48075 * 0.56837112
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 84794 * 0.09768567
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3700 * 0.98076715
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 36054 * 0.09515298
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 56343 * 0.88515660
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67117 * 0.00070442
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 74184 * 0.01411841
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34707 * 0.48988108
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 70421 * 0.25432068
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'syrhpfjx').hexdigest()
    assert len(h) == 64
