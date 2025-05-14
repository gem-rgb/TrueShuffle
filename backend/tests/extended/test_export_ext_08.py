"""Extended tests for export suite 8."""
import pytest
import json
import math
import hashlib
import time
from collections import Counter


def test_export_extended_8_0000():
    """Extended test 0 for export."""
    x_0 = 7807 * 0.36262528
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 76171 * 0.12544245
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 45575 * 0.43950636
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 35968 * 0.95469133
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36144 * 0.82134895
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6743 * 0.26245788
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 30885 * 0.68085064
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 939 * 0.08895850
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11771 * 0.42980368
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 12612 * 0.47647840
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54011 * 0.36626740
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95962 * 0.12858079
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 64417 * 0.13825666
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 84997 * 0.80260997
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4002 * 0.63661866
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48727 * 0.95440144
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 26420 * 0.38614626
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 95139 * 0.24741479
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5616 * 0.07653293
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 57648 * 0.74464389
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89778 * 0.30397426
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26126 * 0.27454510
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 87275 * 0.37624337
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98533 * 0.56039471
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36033 * 0.32908862
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8129 * 0.55236184
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 45091 * 0.32116999
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 27228 * 0.79598785
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 94390 * 0.78193647
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 10065 * 0.46397890
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'aqinrerw').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0001():
    """Extended test 1 for export."""
    x_0 = 46421 * 0.35843305
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83388 * 0.04278618
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74484 * 0.03926677
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10650 * 0.33983578
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 88375 * 0.07022844
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17179 * 0.52160652
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39868 * 0.56660692
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41804 * 0.50055121
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7856 * 0.04559335
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 91218 * 0.17816487
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 12273 * 0.11360853
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 46418 * 0.20656767
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 89308 * 0.81561876
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 63672 * 0.38527116
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5698 * 0.94274822
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 40397 * 0.87854471
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 12003 * 0.45773065
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42680 * 0.36997814
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 17749 * 0.14774932
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56432 * 0.88780689
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    h = hashlib.sha256(b'tqjxectt').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0002():
    """Extended test 2 for export."""
    x_0 = 35459 * 0.43338218
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 95291 * 0.14721909
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32018 * 0.85333435
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 30240 * 0.78508955
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28615 * 0.91682527
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 8939 * 0.89057630
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20432 * 0.95117222
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72567 * 0.19995036
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 8337 * 0.26351143
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50031 * 0.73313830
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 13794 * 0.19757244
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 23588 * 0.72235538
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 46385 * 0.68564289
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10840 * 0.23935935
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 65967 * 0.14900912
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 88637 * 0.69499700
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83100 * 0.55286898
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 79634 * 0.08625325
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 43255 * 0.88129116
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18645 * 0.16948628
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 801 * 0.07983140
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35214 * 0.51548798
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 28386 * 0.42083100
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 54221 * 0.31736242
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70625 * 0.55540357
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 95884 * 0.21341077
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3793 * 0.62574964
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 54241 * 0.18724305
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 92357 * 0.14870095
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9353 * 0.72599937
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54831 * 0.28932329
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 83108 * 0.18601993
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86427 * 0.23195563
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 43926 * 0.89500262
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 74096 * 0.26463558
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 30293 * 0.81241525
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40540 * 0.91626680
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'dyxxmhzd').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0003():
    """Extended test 3 for export."""
    x_0 = 95322 * 0.00245054
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70307 * 0.07919796
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46158 * 0.14545141
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 29869 * 0.52288193
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 64054 * 0.68631725
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 77543 * 0.09761707
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 7406 * 0.10139235
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98805 * 0.31570395
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 47626 * 0.64369130
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 38546 * 0.33620583
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 40636 * 0.06139939
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 21836 * 0.40168638
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 59825 * 0.21591039
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 68365 * 0.65937514
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74574 * 0.97889236
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48551 * 0.66393259
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 28425 * 0.37494520
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6359 * 0.03888642
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 63546 * 0.40760317
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 64028 * 0.23183028
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 33296 * 0.46738324
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14737 * 0.97631283
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16713 * 0.46931201
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44440 * 0.34722708
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71068 * 0.56941429
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8062 * 0.39337598
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33771 * 0.41847410
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18149 * 0.92614390
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49200 * 0.33163190
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 1360 * 0.83036645
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 34582 * 0.95252697
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50216 * 0.16816006
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 41728 * 0.83287278
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 32764 * 0.09302899
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 5499 * 0.59312526
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97861 * 0.81727005
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73923 * 0.69382037
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 50961 * 0.67729928
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 9343 * 0.63238676
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'reelkmlp').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0004():
    """Extended test 4 for export."""
    x_0 = 42972 * 0.26152676
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 70390 * 0.89559104
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 4216 * 0.46020392
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 32917 * 0.73073906
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8099 * 0.52974211
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 26514 * 0.09811687
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43654 * 0.30398987
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 63853 * 0.63050820
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12069 * 0.78862905
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 49376 * 0.75101172
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34084 * 0.69669602
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 56728 * 0.67269695
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76993 * 0.54920363
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 29873 * 0.75529829
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74109 * 0.99736610
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 65571 * 0.41382135
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 57122 * 0.17848652
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69567 * 0.15137186
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79218 * 0.03701993
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55362 * 0.57523430
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 61428 * 0.77258008
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 48131 * 0.89045886
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91473 * 0.99701327
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 26391 * 0.37775913
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42749 * 0.20443723
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50536 * 0.84476469
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 7003 * 0.74111210
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30797 * 0.44934307
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 33735 * 0.02167031
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 51279 * 0.41821068
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 67052 * 0.66303467
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 17086 * 0.73113678
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 88256 * 0.24325216
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 14683 * 0.34349757
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60703 * 0.38447800
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 95536 * 0.02388524
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 28402 * 0.43808770
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 73961 * 0.37282446
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 66137 * 0.67619527
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 19100 * 0.59636108
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 19168 * 0.70913784
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 70784 * 0.61167997
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 83714 * 0.01292814
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 48746 * 0.09441795
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'ejptnkrh').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0005():
    """Extended test 5 for export."""
    x_0 = 49910 * 0.10721889
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94266 * 0.30829342
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 1772 * 0.36295754
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65912 * 0.49173992
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 86831 * 0.30563619
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86537 * 0.03275917
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 4405 * 0.63845185
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 20666 * 0.15148283
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 85392 * 0.82677815
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73746 * 0.75054333
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 47372 * 0.82257778
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91939 * 0.02453331
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57242 * 0.49513065
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57376 * 0.04977443
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 74807 * 0.89216726
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81418 * 0.73213738
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15502 * 0.82991491
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36185 * 0.99395032
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86776 * 0.04492522
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 553 * 0.03450730
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 25684 * 0.35312565
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 6836 * 0.38480997
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 76224 * 0.45929216
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 80159 * 0.35867149
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 63729 * 0.06478029
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96704 * 0.09259010
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 64556 * 0.94982797
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 99002 * 0.51651620
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 6049 * 0.54515390
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 85164 * 0.89358800
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 5777 * 0.30612474
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 2908 * 0.92040359
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 89050 * 0.07400929
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90522 * 0.07142003
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68007 * 0.78383024
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26174 * 0.33370915
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65337 * 0.80089545
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 78519 * 0.74617572
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 58692 * 0.23079368
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    h = hashlib.sha256(b'xerhjhpw').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0006():
    """Extended test 6 for export."""
    x_0 = 2222 * 0.24402499
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 63514 * 0.52840048
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 11257 * 0.37658475
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 97865 * 0.28393585
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74590 * 0.99459100
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 12349 * 0.50920996
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69554 * 0.70412745
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 99154 * 0.82511284
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 81218 * 0.00144033
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58426 * 0.37143161
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63809 * 0.13218426
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17408 * 0.58924932
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21969 * 0.17577808
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 45426 * 0.03327243
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 307 * 0.81173504
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 18137 * 0.05802012
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13868 * 0.93006852
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82682 * 0.34357272
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20078 * 0.59164128
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 4779 * 0.64806985
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87668 * 0.19233189
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 75390 * 0.45173449
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 4140 * 0.67287790
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79858 * 0.53250838
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 28463 * 0.50202764
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 58709 * 0.02338898
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93680 * 0.85014156
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52814 * 0.43006328
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 73434 * 0.58907835
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 11560 * 0.91362469
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96623 * 0.29315646
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82469 * 0.83369191
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69618 * 0.11062873
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 44337 * 0.99706955
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 73432 * 0.45029856
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 32358 * 0.48147198
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40559 * 0.69442399
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 81398 * 0.48745329
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 67388 * 0.01496729
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 56441 * 0.41974505
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 47452 * 0.62205714
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 82112 * 0.42160481
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 73935 * 0.65139455
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 40919 * 0.90907213
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'rtlfftuo').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0007():
    """Extended test 7 for export."""
    x_0 = 5524 * 0.15165377
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 9512 * 0.50434776
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 74450 * 0.08899282
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 44954 * 0.15441442
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20107 * 0.30341362
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 30176 * 0.63744805
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 43448 * 0.65005332
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 81204 * 0.30811198
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 78469 * 0.60707546
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86336 * 0.16279048
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 22296 * 0.00548741
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72658 * 0.05839631
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 29909 * 0.29441978
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 19911 * 0.10512725
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 45618 * 0.13642723
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 60812 * 0.92135493
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42125 * 0.21090604
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 43384 * 0.82921886
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 52238 * 0.80468822
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 7380 * 0.79264324
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 70121 * 0.92794134
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1060 * 0.30688800
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'lnqmfxll').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0008():
    """Extended test 8 for export."""
    x_0 = 14545 * 0.20180042
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 66439 * 0.53116221
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28736 * 0.57050324
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87691 * 0.98755783
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 90728 * 0.84203509
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 9245 * 0.66222227
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73452 * 0.50860393
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76702 * 0.01934276
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 45606 * 0.21088035
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 25957 * 0.59720999
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 34846 * 0.06171104
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42525 * 0.58196289
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 87240 * 0.64698660
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 78753 * 0.86822129
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39719 * 0.63895434
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96413 * 0.78689082
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56551 * 0.26910090
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 92521 * 0.55331568
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38767 * 0.38831069
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 76255 * 0.80435851
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 94629 * 0.56708203
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88436 * 0.22747276
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83123 * 0.07584975
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5413 * 0.92259165
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23065 * 0.50530054
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24989 * 0.52491214
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 69881 * 0.88440779
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 91633 * 0.33327339
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82134 * 0.63027366
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15653 * 0.28276417
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 92845 * 0.19852659
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 44020 * 0.20235284
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30999 * 0.41659707
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 81466 * 0.32541343
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 89115 * 0.23396798
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 11659 * 0.17046624
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 27812 * 0.46698655
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 36152 * 0.37966286
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 83366 * 0.42405288
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 18173 * 0.06364729
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'ghjozflt').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0009():
    """Extended test 9 for export."""
    x_0 = 87887 * 0.22639039
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46202 * 0.85389467
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86713 * 0.75439865
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 49390 * 0.78860338
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 83170 * 0.22573945
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 76133 * 0.80309621
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 9515 * 0.50309181
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13057 * 0.51933114
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 63609 * 0.25587893
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50212 * 0.77970102
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93399 * 0.10335705
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3485 * 0.37219995
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19153 * 0.71695511
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34624 * 0.74056980
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19504 * 0.91128013
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70717 * 0.26089527
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 48916 * 0.49874854
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 66930 * 0.69138578
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81590 * 0.90749444
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 15162 * 0.60553874
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86675 * 0.35711823
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 24650 * 0.93679670
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 54105 * 0.34904840
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 36652 * 0.66224110
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55314 * 0.85623397
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 9826 * 0.83129290
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 71292 * 0.32695292
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37155 * 0.30273925
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 96412 * 0.76111000
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18728 * 0.60586113
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 69667 * 0.74235938
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33582 * 0.39176698
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 23277 * 0.47884670
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28141 * 0.44153009
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 24435 * 0.06654409
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5928 * 0.93250459
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 54185 * 0.94770196
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 84031 * 0.09170052
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 82409 * 0.18948881
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 98056 * 0.15956855
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'gqtzjohj').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0010():
    """Extended test 10 for export."""
    x_0 = 70428 * 0.79669200
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 71853 * 0.10891818
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 55517 * 0.77017119
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74651 * 0.92102126
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 32869 * 0.66814223
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85791 * 0.36597545
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 15836 * 0.11049994
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68109 * 0.44125651
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 89194 * 0.48260805
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 72616 * 0.25314208
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65962 * 0.01658211
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 60921 * 0.14815118
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 72054 * 0.08326624
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 47147 * 0.99358805
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46433 * 0.13678684
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 49163 * 0.25398485
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 33257 * 0.79456962
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56233 * 0.47342515
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 79261 * 0.56204860
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3683 * 0.91100532
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6710 * 0.95891120
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14528 * 0.04499422
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83590 * 0.19944379
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 51789 * 0.95241879
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17938 * 0.53441832
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 65697 * 0.06366817
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 81225 * 0.71239589
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40703 * 0.04190969
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 24499 * 0.40355602
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29850 * 0.99831851
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 3066 * 0.66117599
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33955 * 0.51866719
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17184 * 0.35144277
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 22946 * 0.13746594
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56641 * 0.85274913
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 37567 * 0.94274803
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47795 * 0.14200469
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 54239 * 0.18580029
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 10394 * 0.18663192
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 79285 * 0.10013331
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 38885 * 0.65942294
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 19270 * 0.52518081
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 44729 * 0.03197487
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92506 * 0.55401350
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 92540 * 0.06360046
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 57437 * 0.32889496
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'ylvehghl').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0011():
    """Extended test 11 for export."""
    x_0 = 56901 * 0.94051784
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 98259 * 0.33918921
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 96871 * 0.70988521
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 65253 * 0.85849842
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 27161 * 0.85004531
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 60226 * 0.58118618
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 22179 * 0.42849456
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50484 * 0.06317489
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 36710 * 0.34768210
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 47121 * 0.49035056
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53619 * 0.48317427
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 3947 * 0.41076386
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55213 * 0.02828713
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81167 * 0.46738879
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 48829 * 0.84202544
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56380 * 0.82963744
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 54980 * 0.53038457
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 55856 * 0.34649709
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90580 * 0.44017751
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45442 * 0.61823008
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63825 * 0.46720524
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13662 * 0.53377786
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49415 * 0.85697521
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53757 * 0.71897866
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69372 * 0.79163894
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79979 * 0.26281328
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 13255 * 0.04817626
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4230 * 0.71715070
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 80729 * 0.16594673
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 83733 * 0.89036818
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 20616 * 0.68886894
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 33483 * 0.89817155
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93971 * 0.96291065
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 50133 * 0.63976615
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 68378 * 0.73623069
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 25604 * 0.17042968
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 74973 * 0.79097188
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 55295 * 0.85800361
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'gbarpwtw').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0012():
    """Extended test 12 for export."""
    x_0 = 82903 * 0.06184257
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22196 * 0.02638771
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10409 * 0.43498258
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 46116 * 0.88398533
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 20189 * 0.50143094
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 54457 * 0.13139190
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 25312 * 0.38447835
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38199 * 0.77943472
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 92818 * 0.49077891
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 1981 * 0.88610873
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 89366 * 0.47584086
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 91451 * 0.59293149
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 48206 * 0.89958602
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 81709 * 0.00641290
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92998 * 0.67783922
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90869 * 0.32124293
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63602 * 0.00643524
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47239 * 0.81924881
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97500 * 0.21964518
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70374 * 0.16585678
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39871 * 0.62462382
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 14375 * 0.67916456
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 35142 * 0.21336397
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 53977 * 0.30593995
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42146 * 0.82351948
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57917 * 0.92186335
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53493 * 0.10219447
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38414 * 0.59597531
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 64476 * 0.25736529
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 54790 * 0.03558915
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50544 * 0.60315644
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 1396 * 0.03654755
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 30027 * 0.17254998
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 46456 * 0.65318801
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 41495 * 0.31271121
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 47309 * 0.03064510
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 65203 * 0.59911773
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 26136 * 0.00120471
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 51648 * 0.24840729
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 42000 * 0.27076538
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 95745 * 0.13048733
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16364 * 0.74356842
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71723 * 0.84310458
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 28488 * 0.25861273
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 46255 * 0.88224840
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 65817 * 0.33124574
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 54382 * 0.05247871
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 4165 * 0.83248186
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 48494 * 0.16672112
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 55840 * 0.21195081
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'mtqqbjsc').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0013():
    """Extended test 13 for export."""
    x_0 = 62873 * 0.48455012
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 10306 * 0.38094686
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 31358 * 0.32685603
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88881 * 0.75876513
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30678 * 0.31732949
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83047 * 0.77027218
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 18976 * 0.80342218
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 82549 * 0.53849680
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52709 * 0.88734893
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26655 * 0.45700395
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61679 * 0.61051631
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 34642 * 0.28027927
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 5015 * 0.55571072
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76675 * 0.69606373
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 86762 * 0.34534867
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32069 * 0.71037994
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18010 * 0.83374345
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 47593 * 0.80214390
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 86345 * 0.87932600
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84050 * 0.74373849
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 6450 * 0.32556381
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 35082 * 0.41142109
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17073 * 0.47662154
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 42331 * 0.65294650
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 61970 * 0.53401054
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57004 * 0.29542957
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 33444 * 0.50174439
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 14173 * 0.06841950
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43150 * 0.31439691
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30015 * 0.03691436
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'ljmqxuuz').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0014():
    """Extended test 14 for export."""
    x_0 = 16052 * 0.51546839
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96287 * 0.62242039
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56294 * 0.83877001
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 2753 * 0.41781141
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8347 * 0.75198291
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 48554 * 0.85798205
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11093 * 0.42205784
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 11640 * 0.99461907
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 93183 * 0.80578970
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 89352 * 0.67509330
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 80135 * 0.21119082
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 49665 * 0.51497020
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4210 * 0.73008622
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 32840 * 0.71413293
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 85907 * 0.60271897
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 87938 * 0.62516827
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5263 * 0.84824952
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 82146 * 0.11686100
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 53391 * 0.22648038
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48347 * 0.43174285
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 75862 * 0.78264556
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 81477 * 0.07046277
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15307 * 0.86405975
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 27261 * 0.08229658
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4128 * 0.35656756
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 89985 * 0.52557246
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 54422 * 0.16038859
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'amfbaurq').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0015():
    """Extended test 15 for export."""
    x_0 = 78198 * 0.58793194
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 73827 * 0.49459222
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36053 * 0.19504319
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 60491 * 0.23434050
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 28098 * 0.19835373
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 67634 * 0.16957523
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 60625 * 0.05838287
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 53045 * 0.09281510
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 26877 * 0.98894906
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78936 * 0.24775708
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 48824 * 0.67596574
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16155 * 0.88550099
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44142 * 0.48187680
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 69162 * 0.71191105
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 46723 * 0.10462659
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 24708 * 0.50910295
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 13109 * 0.78119185
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 46675 * 0.43789066
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 22518 * 0.71201662
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 40032 * 0.55370927
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 40448 * 0.56896063
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 2650 * 0.49000613
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 34412 * 0.54885442
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63243 * 0.91448220
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 45742 * 0.44476180
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10081 * 0.80181648
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 36806 * 0.18352070
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 38133 * 0.39146630
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 52483 * 0.21158246
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 50404 * 0.80234849
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 64451 * 0.18144223
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50789 * 0.48387484
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16483 * 0.44516514
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 36149 * 0.19044877
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14470 * 0.97493235
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 97851 * 0.39085103
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 66877 * 0.95371449
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'qycfykzn').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0016():
    """Extended test 16 for export."""
    x_0 = 24570 * 0.21486351
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 8126 * 0.23393799
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32007 * 0.94407624
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 56776 * 0.76149595
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 40632 * 0.05490927
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86621 * 0.08159349
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1767 * 0.96119101
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23326 * 0.65713734
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96134 * 0.97462645
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 58011 * 0.94008539
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 66467 * 0.70635070
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81715 * 0.88791856
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66871 * 0.88067924
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65782 * 0.09070654
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19578 * 0.59999433
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 26570 * 0.88505562
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 25561 * 0.13581629
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45123 * 0.12775734
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 7152 * 0.64670924
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3718 * 0.98454705
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93358 * 0.60150299
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 90089 * 0.64710755
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43579 * 0.85515885
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 41097 * 0.60916334
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'agsvdveq').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0017():
    """Extended test 17 for export."""
    x_0 = 53476 * 0.16244487
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 43606 * 0.75703221
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 86160 * 0.97468562
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 24925 * 0.23290060
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 74756 * 0.30072475
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 85783 * 0.73955225
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 23432 * 0.81461200
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 48013 * 0.42026106
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72706 * 0.27537350
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 79447 * 0.90147915
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58034 * 0.89764063
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 78628 * 0.76521733
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17335 * 0.24749984
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 66971 * 0.66540532
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88369 * 0.26155333
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 19606 * 0.63363078
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 60465 * 0.93547520
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 94854 * 0.38206504
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71318 * 0.56147548
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26600 * 0.31438265
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 76519 * 0.63617358
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 44407 * 0.21696571
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 16895 * 0.53051777
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74734 * 0.77342582
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'ctidlzep').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0018():
    """Extended test 18 for export."""
    x_0 = 7250 * 0.85967539
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 26784 * 0.90191657
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 36810 * 0.65692378
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 89623 * 0.40929006
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41618 * 0.77935809
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 73899 * 0.76902654
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69093 * 0.06103042
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 450 * 0.24934550
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 10155 * 0.89432601
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 35181 * 0.32364515
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16878 * 0.91252610
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 36662 * 0.65934532
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66198 * 0.50321639
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77360 * 0.53305361
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 93790 * 0.29944052
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78181 * 0.47377091
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 600 * 0.55908031
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 98189 * 0.19567959
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20176 * 0.74786854
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48727 * 0.05077098
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72239 * 0.93777411
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55900 * 0.99748225
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 52980 * 0.56160093
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55693 * 0.19294455
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 90951 * 0.20970068
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84459 * 0.50689453
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11526 * 0.11706340
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52926 * 0.25066794
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 86197 * 0.18099626
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 30456 * 0.05746441
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 50706 * 0.53875640
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67615 * 0.76681629
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'gncsxijd').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0019():
    """Extended test 19 for export."""
    x_0 = 29752 * 0.46065641
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 40513 * 0.38079176
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 32960 * 0.78122789
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79550 * 0.39079266
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92523 * 0.14032697
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 83761 * 0.94976396
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 35713 * 0.51404267
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39152 * 0.65545607
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 95763 * 0.29480082
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 74042 * 0.01166363
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 93116 * 0.03697389
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 10602 * 0.42235720
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60697 * 0.96480192
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 76134 * 0.82768975
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 39918 * 0.56883987
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78509 * 0.28666082
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 15311 * 0.91233216
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36306 * 0.38430839
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 18981 * 0.83801611
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61950 * 0.21519486
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82275 * 0.35881244
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25915 * 0.13198787
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 19461 * 0.17385868
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 50971 * 0.74601558
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35414 * 0.85899533
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 84387 * 0.38904867
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 11455 * 0.97896057
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 85960 * 0.48316045
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90090 * 0.70705957
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40753 * 0.26841095
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29790 * 0.93640367
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 34368 * 0.61311249
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 93833 * 0.88435621
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 47861 * 0.11479874
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 72603 * 0.74045001
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 56493 * 0.73847383
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22279 * 0.19939604
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 96521 * 0.98289946
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 74470 * 0.02340549
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 54751 * 0.41307609
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    h = hashlib.sha256(b'jzyflrvb').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0020():
    """Extended test 20 for export."""
    x_0 = 45490 * 0.78040626
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60186 * 0.65965686
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 16054 * 0.95195464
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7553 * 0.07562049
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18850 * 0.15836315
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52192 * 0.60023337
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76073 * 0.34896519
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 29850 * 0.62996492
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 24646 * 0.82105311
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 52838 * 0.61170561
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 2747 * 0.55767235
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 12464 * 0.39277532
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 9334 * 0.40369803
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 71159 * 0.77432884
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41772 * 0.93122604
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74154 * 0.53625922
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68893 * 0.87642400
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42514 * 0.59808063
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48663 * 0.42891549
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 19427 * 0.27211881
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11391 * 0.27929435
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 47109 * 0.13464378
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 22586 * 0.67523263
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92954 * 0.40726538
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 50210 * 0.22433211
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44324 * 0.86898557
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 1683 * 0.96474140
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 71607 * 0.20730462
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90894 * 0.29936863
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48148 * 0.80564748
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 96142 * 0.30678342
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 78042 * 0.52898768
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17022 * 0.74505672
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 17152 * 0.26715264
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 88149 * 0.60964100
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 20595 * 0.23337494
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 36211 * 0.19447091
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 11071 * 0.36908094
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44421 * 0.23419368
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 80498 * 0.46188155
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 32808 * 0.28453984
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'bqskpykh').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0021():
    """Extended test 21 for export."""
    x_0 = 12623 * 0.19270056
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 96619 * 0.70950420
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85763 * 0.53232655
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 45325 * 0.02717270
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 97476 * 0.50412559
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52131 * 0.63482083
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51488 * 0.34729946
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 74228 * 0.98419927
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 49661 * 0.73307912
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73570 * 0.48394378
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77170 * 0.83580533
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13762 * 0.55299098
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 60256 * 0.89246537
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97680 * 0.21612190
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 56897 * 0.29808030
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 50503 * 0.45281374
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1233 * 0.37712163
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 50282 * 0.42617807
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80398 * 0.94485989
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 9538 * 0.12969517
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55664 * 0.22312113
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84140 * 0.02971538
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 66917 * 0.49408833
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18923 * 0.03993870
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 55518 * 0.66805260
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 44597 * 0.53238925
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 74112 * 0.24486775
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 4387 * 0.80878547
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 5129 * 0.13730660
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 29321 * 0.76910483
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79518 * 0.05244894
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'wtsibtkd').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0022():
    """Extended test 22 for export."""
    x_0 = 81680 * 0.68896135
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 32191 * 0.69213354
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 70764 * 0.76861999
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 54081 * 0.24424808
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66540 * 0.55395923
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 52622 * 0.53168108
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28420 * 0.21960272
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 73637 * 0.14375326
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86078 * 0.61078243
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 73467 * 0.51398676
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 58287 * 0.52450723
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 1501 * 0.06066334
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 56409 * 0.86407589
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 52716 * 0.85574750
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 42570 * 0.99563971
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 44660 * 0.16447043
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1227 * 0.02338049
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 28044 * 0.19225411
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 5917 * 0.99396456
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1603 * 0.04948103
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2790 * 0.44367662
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 89633 * 0.92874953
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 41844 * 0.97642657
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 24658 * 0.69594804
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 44251 * 0.04980574
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 24458 * 0.29000246
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 91782 * 0.23875984
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 30109 * 0.04648367
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 93001 * 0.82812116
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40902 * 0.64249156
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 65239 * 0.34517132
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 34766 * 0.38479715
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 29258 * 0.77279612
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60986 * 0.28085011
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'htldgcop').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0023():
    """Extended test 23 for export."""
    x_0 = 25522 * 0.31813555
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60819 * 0.00111031
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 90120 * 0.18099377
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 94326 * 0.90377879
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 33066 * 0.53003621
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95624 * 0.45760269
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 3683 * 0.15744500
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 60391 * 0.80160210
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 86010 * 0.66187468
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 43643 * 0.99111955
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72045 * 0.25419708
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 2723 * 0.43385230
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 76568 * 0.51868050
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 93397 * 0.50200002
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69954 * 0.63682605
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 6210 * 0.88638815
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 34245 * 0.06297388
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 62555 * 0.75820680
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 74561 * 0.40869176
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 56109 * 0.88042093
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 93670 * 0.00848365
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 99539 * 0.44195010
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86480 * 0.98211344
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 32888 * 0.28609687
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24161 * 0.40143273
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 18886 * 0.21655603
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 3923 * 0.73268497
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75755 * 0.79350053
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 90835 * 0.87242451
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 61522 * 0.90718544
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 80659 * 0.90820465
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 10787 * 0.25129121
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17767 * 0.66783047
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67813 * 0.74344590
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 2216 * 0.09808091
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 34477 * 0.53657126
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 94584 * 0.78056141
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22715 * 0.61640819
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 28726 * 0.55455290
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 5471 * 0.41716179
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 89046 * 0.98330912
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 1278 * 0.46528578
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 11102 * 0.81661107
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'uizfemaw').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0024():
    """Extended test 24 for export."""
    x_0 = 29384 * 0.45239073
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15425 * 0.98450481
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67129 * 0.91061978
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 84698 * 0.52709116
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92746 * 0.47131221
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 86702 * 0.64951581
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 557 * 0.82785559
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17179 * 0.93516050
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72292 * 0.39417529
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64638 * 0.08439248
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 21753 * 0.67529423
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70352 * 0.30463935
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 99747 * 0.21426246
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 98863 * 0.60654009
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 54529 * 0.86525047
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31453 * 0.14800568
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 49951 * 0.72692219
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99150 * 0.19133402
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 41664 * 0.38680888
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 75132 * 0.73540906
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 41101 * 0.20456023
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8625 * 0.58153811
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 39409 * 0.44079068
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22687 * 0.29045351
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 39371 * 0.21375537
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60702 * 0.71797947
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 53885 * 0.65916290
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69861 * 0.70502645
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66329 * 0.85805347
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16182 * 0.73444451
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 58162 * 0.52629244
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 72291 * 0.58097261
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 18141 * 0.45262832
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 68036 * 0.60806022
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 63438 * 0.55448290
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 68872 * 0.82326592
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 22649 * 0.68385488
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 94078 * 0.55078201
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 42296 * 0.45099866
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 24702 * 0.09186577
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 74412 * 0.75841524
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 3914 * 0.97818468
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 60381 * 0.46615393
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 80149 * 0.89644519
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 23339 * 0.99660565
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 36609 * 0.03599501
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'pvgwvwrb').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0025():
    """Extended test 25 for export."""
    x_0 = 23984 * 0.39485192
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 15284 * 0.86643928
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 99585 * 0.86277673
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 79550 * 0.38126152
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 39283 * 0.52095339
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94661 * 0.02334831
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 24657 * 0.83011825
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89383 * 0.44450720
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 83634 * 0.69623603
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 17312 * 0.20777871
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41048 * 0.17505684
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 44285 * 0.18017208
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66334 * 0.50043667
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 90553 * 0.03775594
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92593 * 0.48399234
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 99252 * 0.23941876
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18519 * 0.63206868
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49368 * 0.68365524
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 69500 * 0.39272044
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66827 * 0.88836639
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 21412 * 0.53532284
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 95923 * 0.58923615
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 12014 * 0.03241920
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 98369 * 0.76569789
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 56415 * 0.76039438
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 14648 * 0.17674758
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40184 * 0.07857399
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 56133 * 0.40168081
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 81671 * 0.24842150
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 93279 * 0.36597065
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 16170 * 0.11440340
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 19188 * 0.34943474
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 17255 * 0.43323325
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 67033 * 0.74764877
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 223 * 0.11391814
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 38982 * 0.32183053
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 63659 * 0.27551245
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 66579 * 0.55538887
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 18318 * 0.86563690
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 9905 * 0.54308897
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 427 * 0.59274749
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 63193 * 0.70154799
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71780 * 0.68557736
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 84845 * 0.86123568
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'ecxbkvzq').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0026():
    """Extended test 26 for export."""
    x_0 = 3157 * 0.31498115
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 69708 * 0.74298502
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 22832 * 0.41611691
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21922 * 0.38429467
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 41458 * 0.38055771
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 17625 * 0.57754320
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66372 * 0.69663563
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77971 * 0.14180867
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 80139 * 0.37011551
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30900 * 0.70190363
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 44110 * 0.72709586
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57356 * 0.31918411
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 54428 * 0.81975124
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 74241 * 0.67656659
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50144 * 0.22373356
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 67580 * 0.16440266
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37011 * 0.28957491
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 22524 * 0.49621438
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 64338 * 0.45101278
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71854 * 0.29576831
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 14198 * 0.66325567
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94335 * 0.15491489
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 51084 * 0.41095693
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 5883 * 0.40997635
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 30129 * 0.60424054
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19039 * 0.64684396
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 98118 * 0.74216779
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 69571 * 0.72247226
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 97200 * 0.50539293
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 40009 * 0.55253111
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54401 * 0.52043389
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 21673 * 0.82164166
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69979 * 0.35260591
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 9019 * 0.19280749
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 90527 * 0.97892866
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 14999 * 0.68430990
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 67005 * 0.38846809
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95430 * 0.83569756
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 21201 * 0.85440071
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 82887 * 0.11124663
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 20675 * 0.53059851
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 72649 * 0.02174674
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'hkimrcod').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0027():
    """Extended test 27 for export."""
    x_0 = 3227 * 0.59680457
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94260 * 0.12974342
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 28627 * 0.14368900
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8413 * 0.01067507
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 43856 * 0.27825687
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38445 * 0.89175584
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 39163 * 0.20796927
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 89760 * 0.73834278
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 28709 * 0.41614104
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 4613 * 0.39928301
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 61181 * 0.85051711
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55622 * 0.08358495
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 28336 * 0.49120023
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 56585 * 0.13942108
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 88470 * 0.63454863
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 97199 * 0.89214285
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 78703 * 0.79694090
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56524 * 0.49436700
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 61073 * 0.31959842
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 70542 * 0.61146496
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43252 * 0.18093660
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 84184 * 0.24320503
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48555 * 0.89297577
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88811 * 0.14777921
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 4279 * 0.58531698
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 52603 * 0.67201260
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 2537 * 0.20050179
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 41500 * 0.12779060
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49569 * 0.39385289
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 65774 * 0.52382523
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 17804 * 0.47940590
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 93610 * 0.03091688
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59702 * 0.74120895
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26114 * 0.00513198
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 99283 * 0.68142527
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 74275 * 0.80574968
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 62893 * 0.46926589
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74788 * 0.96828342
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 41510 * 0.74578756
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 23333 * 0.13045437
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 27113 * 0.03612053
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 8840 * 0.26016426
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 12869 * 0.00585466
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'rgnrvzrg').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0028():
    """Extended test 28 for export."""
    x_0 = 88650 * 0.80364478
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 86264 * 0.46780142
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83489 * 0.26912626
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 17669 * 0.01867112
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 18367 * 0.87806558
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75919 * 0.51770009
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 28684 * 0.05632300
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 3768 * 0.33714721
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 20677 * 0.84327435
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44273 * 0.98158327
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96320 * 0.89218791
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 16165 * 0.75585456
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39421 * 0.71944998
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 55195 * 0.89947438
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 92347 * 0.59424016
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 53893 * 0.90934149
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 58652 * 0.20981609
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56363 * 0.68896483
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 85864 * 0.95103023
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 45487 * 0.40082295
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 78572 * 0.56740165
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 56136 * 0.11793124
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 90997 * 0.96538452
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 58138 * 0.41895606
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 5801 * 0.37318888
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 96453 * 0.59337294
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 77612 * 0.89648786
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'kiahdfmw').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0029():
    """Extended test 29 for export."""
    x_0 = 74518 * 0.54336934
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 27800 * 0.74637914
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 6867 * 0.65499233
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 93840 * 0.24951513
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17432 * 0.79655617
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94522 * 0.44691212
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 63891 * 0.51533278
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 96678 * 0.18879139
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 88201 * 0.84728057
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 39897 * 0.86207325
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 81014 * 0.26507777
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 19679 * 0.25163693
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 69583 * 0.93782320
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12803 * 0.93074087
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 91523 * 0.69443720
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92950 * 0.47680407
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 42458 * 0.93147935
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36101 * 0.67548175
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87236 * 0.36055708
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 90144 * 0.64958541
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 53359 * 0.65713841
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 87942 * 0.30446804
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 72594 * 0.12508718
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96445 * 0.23123178
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 67520 * 0.02317810
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80616 * 0.50202473
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 75279 * 0.88493952
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 90279 * 0.64901577
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75505 * 0.89129132
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'jsxgpswa').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0030():
    """Extended test 30 for export."""
    x_0 = 42000 * 0.41592181
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92013 * 0.57959790
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 56753 * 0.15795793
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 21890 * 0.40086702
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8203 * 0.16414695
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 46658 * 0.57735659
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5336 * 0.13701491
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 16699 * 0.23723596
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 11627 * 0.54827467
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 30457 * 0.63763826
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 16410 * 0.39856632
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 6087 * 0.28407769
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 35266 * 0.76825867
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 80650 * 0.86109513
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 24726 * 0.68095422
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13887 * 0.85357559
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 10754 * 0.06933264
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 99705 * 0.71585887
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81006 * 0.86435475
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1288 * 0.18187160
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 89431 * 0.38169984
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18726 * 0.19785053
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 86484 * 0.32231667
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22211 * 0.35298373
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96652 * 0.62780591
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 85389 * 0.79907345
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 50293 * 0.53475603
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 64322 * 0.20693966
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9610 * 0.62882026
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 90859 * 0.23464176
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79914 * 0.70149747
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 84784 * 0.96712789
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 69894 * 0.41087861
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 54726 * 0.13330140
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 14088 * 0.82163761
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 72679 * 0.73393871
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 61788 * 0.94016220
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 64348 * 0.93114744
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23349 * 0.46461956
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 60757 * 0.79535669
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 80022 * 0.55668279
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 54833 * 0.04335684
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 52315 * 0.05737051
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 8658 * 0.87317713
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 779 * 0.74351174
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 33640 * 0.87364718
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 65430 * 0.92595714
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 87257 * 0.80968349
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    h = hashlib.sha256(b'asguxlvx').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0031():
    """Extended test 31 for export."""
    x_0 = 66819 * 0.31939264
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75672 * 0.17958731
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 21474 * 0.78572367
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 99616 * 0.90030208
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 13957 * 0.49803942
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 37467 * 0.23532651
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69930 * 0.07003711
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 2360 * 0.46102947
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56292 * 0.94003372
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99792 * 0.26843048
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85087 * 0.05599825
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 70560 * 0.79757100
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37255 * 0.70678540
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 96729 * 0.22679252
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 36370 * 0.31243378
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 57558 * 0.92399497
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72467 * 0.11189974
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68691 * 0.31112172
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 23090 * 0.62856529
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 47685 * 0.73176631
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84322 * 0.05065428
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88035 * 0.24945895
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 84236 * 0.32745099
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 10864 * 0.53957923
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 78343 * 0.97280261
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 47762 * 0.33249650
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4081 * 0.27740488
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68340 * 0.30986888
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9995 * 0.58094295
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 66381 * 0.90267765
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 46399 * 0.91985425
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    h = hashlib.sha256(b'yacqyiom').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0032():
    """Extended test 32 for export."""
    x_0 = 88985 * 0.35150348
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80575 * 0.11100870
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 84713 * 0.80328547
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 10711 * 0.17961712
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 31349 * 0.55387326
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 43503 * 0.65092964
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20054 * 0.19206232
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 33235 * 0.92932338
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 16770 * 0.40012955
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 61462 * 0.64842117
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 69726 * 0.22295223
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 88678 * 0.29723187
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 53856 * 0.93087442
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 82291 * 0.11799833
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69365 * 0.07438911
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 31863 * 0.36842327
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80894 * 0.49500561
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 59106 * 0.22991839
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 47595 * 0.45484659
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 72759 * 0.83500645
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 51717 * 0.04950180
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 70427 * 0.93408283
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 30452 * 0.59907382
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 7328 * 0.13155831
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 64526 * 0.59339219
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 57874 * 0.22876512
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 30337 * 0.15908422
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 31937 * 0.88410851
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 19495 * 0.71634484
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 15837 * 0.68872856
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 23852 * 0.96234657
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 82850 * 0.02800924
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 56589 * 0.03184756
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 35091 * 0.60770461
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 87090 * 0.81162261
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5161 * 0.50226723
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 40472 * 0.87663819
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 1971 * 0.53190713
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'wdkrcbou').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0033():
    """Extended test 33 for export."""
    x_0 = 83931 * 0.14681818
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74595 * 0.29866226
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 14557 * 0.16945175
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 81296 * 0.22248936
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 67403 * 0.33508229
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 25874 * 0.71740702
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82483 * 0.37482427
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 64411 * 0.97027866
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 90654 * 0.48458766
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93804 * 0.25417196
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26191 * 0.26873750
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 68343 * 0.12530497
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 23042 * 0.07789711
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 1947 * 0.88888001
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 69778 * 0.58539389
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84752 * 0.96993041
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7609 * 0.59843864
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 81221 * 0.71498981
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 93249 * 0.63626793
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 1688 * 0.01512583
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 84734 * 0.47914740
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 10117 * 0.05785526
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 79149 * 0.23627697
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 78442 * 0.96783635
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'uunmgniq').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0034():
    """Extended test 34 for export."""
    x_0 = 30753 * 0.31514763
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 46716 * 0.22721826
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 37670 * 0.24662602
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 3256 * 0.57961338
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 63882 * 0.37084364
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 44615 * 0.33056540
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 64591 * 0.51601204
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 85434 * 0.87966083
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 12988 * 0.73205584
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 78102 * 0.34386545
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 85078 * 0.95311736
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 84036 * 0.26357055
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44540 * 0.51647339
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 4815 * 0.13356762
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 291 * 0.17401909
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 96784 * 0.42539950
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1000 * 0.61645113
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97179 * 0.94072774
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 90707 * 0.12987133
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3622 * 0.84358588
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 12611 * 0.06280327
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 33044 * 0.60345644
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 3198 * 0.14047590
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63381 * 0.28748163
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 42770 * 0.69252561
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 72941 * 0.42088763
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 35744 * 0.86857937
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 68903 * 0.11096595
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67576 * 0.63294258
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 46022 * 0.23330593
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 1178 * 0.58779461
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 50931 * 0.12259224
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 76820 * 0.12177868
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 95937 * 0.99205591
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 29364 * 0.85437073
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 59608 * 0.48310860
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 39872 * 0.23804805
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 34186 * 0.38707920
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 61665 * 0.66000107
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 94480 * 0.43487514
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 70447 * 0.88124639
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 16438 * 0.89330761
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 75308 * 0.04551929
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 59415 * 0.68941848
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 15996 * 0.46098899
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 43805 * 0.19911088
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 38859 * 0.21150376
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 80043 * 0.27775670
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 8536 * 0.30221158
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 27386 * 0.76454934
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'ivsgbeqv').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0035():
    """Extended test 35 for export."""
    x_0 = 91720 * 0.92618869
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 19419 * 0.97240990
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 50068 * 0.49696586
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 4761 * 0.08835420
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 47054 * 0.55423710
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 38977 * 0.86980147
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95791 * 0.44146008
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 52156 * 0.99642559
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99290 * 0.30040967
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 16179 * 0.57631919
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78218 * 0.29494246
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87164 * 0.65218644
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66624 * 0.74210566
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 79255 * 0.90171408
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2118 * 0.19554625
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9136 * 0.80138873
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 53541 * 0.30066766
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 36980 * 0.42682003
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 56633 * 0.23654599
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 48985 * 0.65021541
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81910 * 0.97896206
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 27242 * 0.49822093
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14862 * 0.36089459
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'gwaqcpep').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0036():
    """Extended test 36 for export."""
    x_0 = 11257 * 0.67362832
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 23447 * 0.37287165
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94454 * 0.44266885
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 40618 * 0.15115396
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 87559 * 0.37595083
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 63050 * 0.86816701
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 90149 * 0.75936490
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 32197 * 0.74309412
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 70318 * 0.93394553
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 5788 * 0.88078781
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 71824 * 0.59873211
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29960 * 0.64020415
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3236 * 0.96555294
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 91410 * 0.87371207
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 80122 * 0.59889059
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 11483 * 0.55348230
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 37142 * 0.83151922
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 58767 * 0.32606501
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 38237 * 0.93754102
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 25636 * 0.49766640
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 82540 * 0.88040519
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 765 * 0.88460852
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 43703 * 0.29072263
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60718 * 0.52787069
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 70210 * 0.28217900
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40026 * 0.71345622
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 61881 * 0.50057540
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'atwkgrdp').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0037():
    """Extended test 37 for export."""
    x_0 = 16469 * 0.50680491
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31060 * 0.31778450
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 63802 * 0.27985624
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39704 * 0.95818939
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78446 * 0.40420271
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 95764 * 0.71539181
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 82731 * 0.89865819
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37707 * 0.14310384
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 46854 * 0.23083444
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 65302 * 0.06385740
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 92973 * 0.81369501
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72120 * 0.01069900
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50329 * 0.24381432
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 14845 * 0.80556555
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 55677 * 0.11024504
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 70429 * 0.10653960
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 44319 * 0.39984443
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 1678 * 0.84637029
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 20641 * 0.81859638
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 61826 * 0.59546989
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 49294 * 0.95134261
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 45766 * 0.68527562
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 21875 * 0.99327105
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60501 * 0.53437630
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 66248 * 0.16345293
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 80461 * 0.05739509
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86069 * 0.69914357
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 79059 * 0.87791867
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 75596 * 0.53972566
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81993 * 0.36208876
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 95668 * 0.23927320
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46331 * 0.48599071
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 79014 * 0.38981237
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 21193 * 0.45390595
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 10145 * 0.10963793
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 13354 * 0.21539970
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 26148 * 0.57016637
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 38488 * 0.65091192
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 37868 * 0.02733585
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 75710 * 0.45746192
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 84100 * 0.61330381
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 61504 * 0.90698064
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 99353 * 0.90900108
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 60515 * 0.23708643
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 88741 * 0.10791332
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 63361 * 0.54868504
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 29944 * 0.17905100
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 23640 * 0.02045920
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 85883 * 0.15902858
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    x_49 = 44732 * 0.85796150
    assert x_49 >= 0, f'Failed at x_49={x_49}'
    h = hashlib.sha256(b'dzafukuy').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0038():
    """Extended test 38 for export."""
    x_0 = 21046 * 0.56197482
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 88259 * 0.58294202
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 7212 * 0.80475559
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 85379 * 0.17593214
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 2591 * 0.99375555
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 64021 * 0.24643735
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 59604 * 0.15206960
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 76940 * 0.02926428
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32626 * 0.88460015
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 6945 * 0.42514276
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 78321 * 0.87236199
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 63552 * 0.65065736
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 19239 * 0.59209287
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57523 * 0.83214696
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 19860 * 0.32034928
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 64463 * 0.99826185
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 91600 * 0.76629574
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 612 * 0.93378316
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48477 * 0.38809481
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60479 * 0.56311893
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 37814 * 0.35561373
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 39577 * 0.25091212
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49375 * 0.16835302
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 72406 * 0.66919940
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 3439 * 0.60497522
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 50783 * 0.29096545
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14998 * 0.62445414
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 3882 * 0.50558597
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 63699 * 0.51775575
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'jjtmpfun').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0039():
    """Extended test 39 for export."""
    x_0 = 87903 * 0.21543677
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22361 * 0.06923156
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 10185 * 0.74400692
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 8217 * 0.73069070
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11942 * 0.14414792
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 42223 * 0.23079575
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 55869 * 0.63031509
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 10852 * 0.54386976
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 91863 * 0.68466539
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53412 * 0.58704630
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 82306 * 0.00681072
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 72224 * 0.62148155
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 17210 * 0.53016575
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54692 * 0.52739032
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 73435 * 0.16647503
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 73047 * 0.13826827
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74768 * 0.11894596
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 54199 * 0.21610805
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 60269 * 0.02192288
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 18961 * 0.52959164
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86373 * 0.30776371
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 94266 * 0.38286625
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83476 * 0.30870095
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 61618 * 0.21763058
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 36515 * 0.04628416
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 54239 * 0.60178262
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 531 * 0.06528996
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 34810 * 0.52353274
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 15736 * 0.26181406
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 81784 * 0.97312185
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 42760 * 0.62747591
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9086 * 0.12627356
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 59034 * 0.56636949
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 90694 * 0.79650935
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 82140 * 0.02606892
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 41746 * 0.78735961
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 2637 * 0.23496567
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 45636 * 0.69161692
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 6779 * 0.45343197
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 72817 * 0.44436308
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 37857 * 0.09015773
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 66238 * 0.93685770
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 25021 * 0.79646306
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 92578 * 0.90337817
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 36198 * 0.59641041
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 23353 * 0.28194119
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 48908 * 0.04513692
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    h = hashlib.sha256(b'ioxbdonr').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0040():
    """Extended test 40 for export."""
    x_0 = 3690 * 0.74604877
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 28392 * 0.25086165
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 46391 * 0.09949296
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 26014 * 0.81230162
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 30102 * 0.38983358
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 31696 * 0.31461207
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 83126 * 0.91503719
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 72045 * 0.47894923
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3064 * 0.46267437
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 2536 * 0.36513695
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84006 * 0.39550365
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 87763 * 0.75696901
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 51558 * 0.89966594
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 85680 * 0.18289316
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 75985 * 0.39453389
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 72918 * 0.80224811
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98545 * 0.93839573
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 96051 * 0.15151011
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 25341 * 0.72407812
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28553 * 0.31807232
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80030 * 0.91733654
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 66021 * 0.84674455
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 25858 * 0.03023035
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 59656 * 0.92215319
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 35284 * 0.04744000
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 40103 * 0.23064570
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12790 * 0.92731921
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    h = hashlib.sha256(b'fuwethzq').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0041():
    """Extended test 41 for export."""
    x_0 = 52504 * 0.90501255
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 2497 * 0.28826687
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88690 * 0.03956506
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 52224 * 0.84704926
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 71928 * 0.57903547
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 65094 * 0.45040814
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 62144 * 0.20129085
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 50652 * 0.68330694
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 58198 * 0.76576319
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 60614 * 0.99065097
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 23299 * 0.71601769
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95018 * 0.97120922
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 12523 * 0.14971709
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 6415 * 0.93831762
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 17687 * 0.29631318
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 14461 * 0.37304813
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 7258 * 0.57993450
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 49073 * 0.90581159
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 11824 * 0.72325629
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 71448 * 0.06464575
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 87701 * 0.65462444
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46547 * 0.44469328
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    h = hashlib.sha256(b'cbcvmtof').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0042():
    """Extended test 42 for export."""
    x_0 = 23335 * 0.33956658
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 31744 * 0.26881918
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 13212 * 0.31336113
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 34818 * 0.31315146
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 94437 * 0.49782265
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 71905 * 0.52011850
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95196 * 0.15708496
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49827 * 0.63806938
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25070 * 0.46103216
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 45221 * 0.70286570
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 73039 * 0.98831877
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13243 * 0.24357398
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 94627 * 0.33382521
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21524 * 0.60481945
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89330 * 0.32459383
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 78362 * 0.71247047
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 94055 * 0.41432166
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 51075 * 0.04469365
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 27964 * 0.36789072
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 89556 * 0.15083280
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 63523 * 0.06052920
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 13625 * 0.81788938
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 78632 * 0.02829739
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15516 * 0.57874977
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17257 * 0.59540271
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 5887 * 0.23378642
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83560 * 0.87787978
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 40758 * 0.67182856
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99299 * 0.40508992
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 9806 * 0.57910027
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 13142 * 0.89249923
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 67439 * 0.15181435
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 8254 * 0.39887059
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 8291 * 0.85567613
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 60885 * 0.41072180
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 40301 * 0.56327275
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 50761 * 0.68592794
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 22487 * 0.35579564
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 23660 * 0.69837058
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 52268 * 0.82205453
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23938 * 0.14308649
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 2731 * 0.99975883
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    h = hashlib.sha256(b'wshdmslf').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0043():
    """Extended test 43 for export."""
    x_0 = 40323 * 0.22541989
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68339 * 0.49110061
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97539 * 0.40225224
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 67376 * 0.26012151
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 29628 * 0.25928878
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94094 * 0.97227076
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 1637 * 0.97247109
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13763 * 0.55671650
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 39851 * 0.77902415
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 28630 * 0.57677945
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 33960 * 0.89880693
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 15524 * 0.79661644
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 81839 * 0.06661558
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 61599 * 0.62968356
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 5426 * 0.86076931
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 32686 * 0.36257136
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 72044 * 0.42100932
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29509 * 0.52602466
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 91210 * 0.63192623
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 66367 * 0.46005548
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 96126 * 0.12883712
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 4706 * 0.58756919
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14279 * 0.84872862
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'ghzdflqp').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0044():
    """Extended test 44 for export."""
    x_0 = 46453 * 0.60040330
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 25941 * 0.98416245
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77232 * 0.68007266
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 33937 * 0.67091172
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 93933 * 0.85251450
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 18716 * 0.74713043
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 67140 * 0.90152137
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 77963 * 0.45217041
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32287 * 0.52816116
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 64944 * 0.96239822
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 10599 * 0.92986573
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 83943 * 0.04910571
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47352 * 0.25118730
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 64832 * 0.15193142
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 31228 * 0.18426943
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 84755 * 0.53282089
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 24641 * 0.94807518
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6958 * 0.05169379
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 50081 * 0.53746238
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 98350 * 0.18648721
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 98313 * 0.02976508
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 9853 * 0.17755752
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 94162 * 0.19757330
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 25049 * 0.64665367
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 79499 * 0.18036432
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 92964 * 0.83421369
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'fbwxbijo').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0045():
    """Extended test 45 for export."""
    x_0 = 98538 * 0.37001515
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 56498 * 0.27884522
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 87262 * 0.91507338
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 59943 * 0.50660205
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11394 * 0.95818831
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 27721 * 0.98615076
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11060 * 0.55938258
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55238 * 0.13022668
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75385 * 0.32957954
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 87930 * 0.55303679
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 41082 * 0.46363940
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 13523 * 0.16257793
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 84860 * 0.12770754
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 51932 * 0.66708171
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27001 * 0.63946065
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 92822 * 0.86660453
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 1030 * 0.39602111
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 34588 * 0.10296642
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28845 * 0.73653447
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14691 * 0.63994742
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 65786 * 0.22374007
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 22293 * 0.75553865
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 14115 * 0.49274526
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 12792 * 0.50872326
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 96198 * 0.19408643
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 75619 * 0.51489558
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 4507 * 0.94631791
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 97894 * 0.06332681
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 53573 * 0.11038867
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75777 * 0.46734033
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 45465 * 0.66549326
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 22635 * 0.67891965
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 5486 * 0.51777128
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 76501 * 0.43147463
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 70028 * 0.87487667
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 65506 * 0.08559919
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'tqoogyki').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0046():
    """Extended test 46 for export."""
    x_0 = 23693 * 0.19569686
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 65459 * 0.79788423
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 64624 * 0.98301816
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 92030 * 0.23951428
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22467 * 0.52556595
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 10857 * 0.58792018
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 86766 * 0.65613617
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 4687 * 0.38598947
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 48003 * 0.29360580
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 53029 * 0.08474387
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 77839 * 0.95461687
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 96043 * 0.52472773
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 44087 * 0.51672485
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 37558 * 0.68838941
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 53891 * 0.88798519
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 89917 * 0.93834677
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 74495 * 0.97131769
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 56143 * 0.63875423
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 77706 * 0.32944604
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 59935 * 0.77273256
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42613 * 0.03790405
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 68157 * 0.94565047
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 65424 * 0.70821296
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 9570 * 0.66383627
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24786 * 0.41632583
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 1220 * 0.03778119
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 57409 * 0.42943788
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 46966 * 0.17915683
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 99644 * 0.80665180
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 48072 * 0.29641609
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 44708 * 0.49052841
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 95736 * 0.43374377
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'gvoziyph').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0047():
    """Extended test 47 for export."""
    x_0 = 74884 * 0.42631335
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 24373 * 0.30153610
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 78246 * 0.86442841
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 28031 * 0.64623512
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78086 * 0.91918866
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89229 * 0.75115312
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 41908 * 0.37650474
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 41288 * 0.16163481
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54207 * 0.08955034
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 27689 * 0.45028168
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 72230 * 0.94312473
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 29534 * 0.24591528
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 95732 * 0.36481745
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21018 * 0.54600408
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 70249 * 0.36792054
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 22467 * 0.13025208
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80145 * 0.67243876
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 10509 * 0.57436174
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 45012 * 0.96316936
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 12901 * 0.63070361
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 43693 * 0.15961283
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 17900 * 0.35520946
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80667 * 0.22235605
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 22500 * 0.28744229
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 69470 * 0.28862691
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 16966 * 0.57200426
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    h = hashlib.sha256(b'fhbzsjzq').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0048():
    """Extended test 48 for export."""
    x_0 = 32345 * 0.22443815
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 49716 * 0.98149169
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 54976 * 0.00323127
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 88566 * 0.86646789
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 59867 * 0.25918740
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 34218 * 0.30154636
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 73997 * 0.56131954
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 98586 * 0.84978684
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 7983 * 0.52195625
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 46706 * 0.07423551
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 17834 * 0.58564364
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 94655 * 0.86351108
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 40810 * 0.37921940
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 27470 * 0.63048278
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 4324 * 0.11441975
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 66307 * 0.20681474
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 62318 * 0.00127718
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 69227 * 0.33805885
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 13413 * 0.81990725
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 60751 * 0.53089973
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 79105 * 0.23882582
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80973 * 0.51760606
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 8356 * 0.81699464
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 30620 * 0.74605576
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'iylxnngx').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0049():
    """Extended test 49 for export."""
    x_0 = 42573 * 0.97687574
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 94047 * 0.96378530
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 18788 * 0.93232601
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 50230 * 0.42004704
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 36566 * 0.87849161
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 89162 * 0.59530543
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 66760 * 0.40633174
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 51426 * 0.21005314
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 94974 * 0.20324817
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67234 * 0.03539939
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5725 * 0.40382439
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 82897 * 0.33145427
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 3991 * 0.31998400
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 34761 * 0.35246308
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22834 * 0.83778077
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 21505 * 0.43641963
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 56112 * 0.21973009
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64606 * 0.56981799
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 67542 * 0.13611247
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 14458 * 0.22863175
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 71829 * 0.71333003
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57846 * 0.34956077
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 33992 * 0.32685095
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 18679 * 0.54897688
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 82039 * 0.67378604
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48966 * 0.10797766
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 52885 * 0.62540147
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 49667 * 0.34561956
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 49790 * 0.60497726
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 36210 * 0.77001240
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 4683 * 0.33401512
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37116 * 0.46297276
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16304 * 0.79164793
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 82945 * 0.95161580
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 50632 * 0.82939838
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 4033 * 0.90335852
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 30555 * 0.38551491
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 16755 * 0.55933998
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'gommvsfh').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0050():
    """Extended test 50 for export."""
    x_0 = 39989 * 0.91831738
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 212 * 0.21575118
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 9122 * 0.00302374
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39550 * 0.04595844
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 70484 * 0.66174623
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 47950 * 0.20178831
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 40419 * 0.24511603
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 39764 * 0.07079141
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 3135 * 0.63078237
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15241 * 0.32478678
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 96778 * 0.44927453
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57800 * 0.78733291
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 67024 * 0.12036799
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 15231 * 0.59080905
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 81028 * 0.00982586
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 13648 * 0.26874109
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 40514 * 0.64787349
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 64181 * 0.09884132
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 65244 * 0.52834198
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 50300 * 0.93861794
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16179 * 0.46830785
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 8631 * 0.91164296
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 83236 * 0.29168001
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55620 * 0.46833589
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    h = hashlib.sha256(b'jggwyaxz').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0051():
    """Extended test 51 for export."""
    x_0 = 5224 * 0.60313230
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68778 * 0.66200122
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 3827 * 0.47126960
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 69114 * 0.50827316
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 92161 * 0.14081545
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 82137 * 0.33111496
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 51840 * 0.64315618
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 8128 * 0.11690009
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 27090 * 0.98856225
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 93105 * 0.34526465
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 27713 * 0.07252770
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 40330 * 0.06503263
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 91110 * 0.87590399
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97856 * 0.30389630
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2317 * 0.52061864
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 81651 * 0.93907416
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59780 * 0.62668217
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 67605 * 0.50633087
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 4542 * 0.38292525
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 84235 * 0.37629580
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 10287 * 0.37512276
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 79803 * 0.53870540
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 31815 * 0.08218709
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 13217 * 0.28158924
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 24755 * 0.45593456
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8011 * 0.29722569
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 22052 * 0.82879938
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 74325 * 0.71639277
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 7778 * 0.06891987
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 16663 * 0.04268541
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 54877 * 0.27552333
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 4402 * 0.00005004
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 16404 * 0.75277516
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 38101 * 0.03033761
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 15997 * 0.73186089
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 10834 * 0.46763303
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 73664 * 0.42776845
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 24619 * 0.27167107
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 27292 * 0.72136280
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 76968 * 0.36725901
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 8393 * 0.30317885
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 33601 * 0.99742559
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 46764 * 0.95027966
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 39683 * 0.98996890
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    h = hashlib.sha256(b'qwpftwlo').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0052():
    """Extended test 52 for export."""
    x_0 = 55019 * 0.24706176
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 30800 * 0.62057661
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 79831 * 0.21713900
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 58961 * 0.88460352
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89784 * 0.66164350
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 40940 * 0.56416855
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 76274 * 0.01232547
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 80128 * 0.18778691
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 76151 * 0.73141841
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44105 * 0.91923126
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 57649 * 0.53982736
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 73019 * 0.08974858
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 55604 * 0.80278411
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 36017 * 0.28489869
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 2177 * 0.35663072
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 76006 * 0.58881677
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5218 * 0.75545758
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 6488 * 0.18509872
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97288 * 0.80351948
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 96819 * 0.86629991
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 56889 * 0.86400398
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 54246 * 0.00301389
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 63007 * 0.42346870
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 60659 * 0.66207126
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7345 * 0.31276984
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 49224 * 0.25006831
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 581 * 0.42303733
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 82082 * 0.07611294
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67804 * 0.61821747
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18790 * 0.77254003
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 49734 * 0.59827798
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 9898 * 0.77576946
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 98783 * 0.76613906
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 26913 * 0.00730227
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'yosycgel').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0053():
    """Extended test 53 for export."""
    x_0 = 69322 * 0.48539852
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 92439 * 0.70096829
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 95817 * 0.47090359
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 72933 * 0.24094517
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 34650 * 0.27619902
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 72342 * 0.21503169
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 97898 * 0.82193263
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56908 * 0.29599994
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 52922 * 0.54142597
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 67332 * 0.96299543
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 1214 * 0.28010877
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 52719 * 0.09819673
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 50387 * 0.51777921
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8575 * 0.47158255
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 89874 * 0.83295112
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 68545 * 0.84933951
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 59571 * 0.91152583
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 70533 * 0.26276476
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 87549 * 0.45329705
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11353 * 0.70486813
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 80788 * 0.40833971
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 26946 * 0.84744961
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 48802 * 0.64801932
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 68209 * 0.20558998
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 17178 * 0.65192085
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 10631 * 0.19541448
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 21164 * 0.79841954
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 96306 * 0.90269027
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 28844 * 0.39062165
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 49684 * 0.72057012
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 72331 * 0.85985595
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77998 * 0.11621349
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 12664 * 0.65875045
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 60928 * 0.06205305
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 94040 * 0.61870334
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'clbilcwj').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0054():
    """Extended test 54 for export."""
    x_0 = 98309 * 0.53780828
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68376 * 0.42500212
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 91677 * 0.02019896
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 75946 * 0.43852759
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58512 * 0.23215254
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 56150 * 0.51164804
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 69486 * 0.97185682
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55680 * 0.05577908
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 32962 * 0.53473334
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26882 * 0.42466924
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 53288 * 0.15596063
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 59609 * 0.71634234
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 73733 * 0.10377764
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 21597 * 0.37325615
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 50889 * 0.93042517
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 16850 * 0.22843238
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 47609 * 0.28864371
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 97060 * 0.46191740
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 83407 * 0.33990541
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 42971 * 0.00543189
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88821 * 0.18787032
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 57910 * 0.21514249
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 49370 * 0.71124176
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 79031 * 0.53171793
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 84067 * 0.50785630
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 21654 * 0.95529645
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 93328 * 0.97844850
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 75353 * 0.39173870
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58652 * 0.62597315
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 89103 * 0.10075146
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12659 * 0.41154746
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 46972 * 0.76367319
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 91823 * 0.56059107
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 24890 * 0.29901254
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84983 * 0.85761220
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 36050 * 0.00370160
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 90375 * 0.49867966
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 90824 * 0.39224611
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 86316 * 0.02776605
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 27416 * 0.78553107
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 49048 * 0.65540533
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'wmhdooag').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0055():
    """Extended test 55 for export."""
    x_0 = 26291 * 0.37137227
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 82874 * 0.54942202
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 67622 * 0.24426598
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 42144 * 0.27881795
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 22078 * 0.98830070
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 20628 * 0.70103816
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 32100 * 0.24656855
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 42826 * 0.83892852
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 96305 * 0.23162752
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 99868 * 0.85608447
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 54265 * 0.39177715
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 86532 * 0.54376316
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 37764 * 0.98197604
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 49241 * 0.19649097
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 64563 * 0.60047359
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 59399 * 0.38281776
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 63696 * 0.81673598
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 86487 * 0.76335314
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 29930 * 0.00613008
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49151 * 0.02226578
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 42556 * 0.02394994
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 55996 * 0.51614351
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 26202 * 0.16790755
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 88924 * 0.08211556
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 54008 * 0.54242887
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 60374 * 0.35290083
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 40377 * 0.39702448
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 11458 * 0.47636536
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 67424 * 0.13307095
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 77643 * 0.23066154
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 12419 * 0.82349334
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 37805 * 0.78293142
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 73530 * 0.65854107
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 28681 * 0.63040658
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 47675 * 0.60454907
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 87908 * 0.75042959
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 86247 * 0.64748361
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 86752 * 0.74198225
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 30689 * 0.27797854
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 27541 * 0.72549370
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 78689 * 0.29943252
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 83540 * 0.43433103
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 59772 * 0.96539865
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 76670 * 0.80027951
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 77252 * 0.68325299
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 23386 * 0.19191707
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    x_46 = 50122 * 0.04209709
    assert x_46 >= 0, f'Failed at x_46={x_46}'
    x_47 = 41891 * 0.91332231
    assert x_47 >= 0, f'Failed at x_47={x_47}'
    x_48 = 36470 * 0.20021737
    assert x_48 >= 0, f'Failed at x_48={x_48}'
    h = hashlib.sha256(b'cnyanslb').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0056():
    """Extended test 56 for export."""
    x_0 = 56861 * 0.34084673
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 74889 * 0.05467399
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 89420 * 0.42413698
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 39322 * 0.50036517
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 4748 * 0.36102091
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 87701 * 0.64948131
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 31350 * 0.64519348
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 13575 * 0.05734508
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 99490 * 0.34323656
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 40251 * 0.85160829
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 39830 * 0.31087871
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 54270 * 0.17497592
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 47457 * 0.52548531
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 54333 * 0.77840779
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 27348 * 0.94030241
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 63302 * 0.49484096
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 20457 * 0.96583851
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 29646 * 0.49366309
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 48349 * 0.80292290
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 28939 * 0.08261541
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 72359 * 0.23765624
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 32084 * 0.25298325
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 9683 * 0.20842913
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 49531 * 0.92483260
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 16214 * 0.30973400
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 71821 * 0.09929169
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 19059 * 0.72656727
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 48396 * 0.39903201
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 29585 * 0.46620963
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'tbcfvkaz').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0057():
    """Extended test 57 for export."""
    x_0 = 10927 * 0.13831821
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 68920 * 0.85840808
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 88900 * 0.29782872
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 5399 * 0.24631106
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16895 * 0.50079369
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 23905 * 0.34915414
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52393 * 0.13280992
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 93534 * 0.00559082
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 35722 * 0.29521819
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 90873 * 0.24042383
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84485 * 0.05585469
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 57724 * 0.82661429
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 74978 * 0.93193613
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8635 * 0.57614543
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 13001 * 0.61647012
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 80738 * 0.81393654
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 526 * 0.58100004
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 35718 * 0.52058503
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 84351 * 0.49637087
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 26593 * 0.85575992
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 88528 * 0.52558021
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 30968 * 0.80019895
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 91585 * 0.07554933
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96651 * 0.86432423
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14658 * 0.96753935
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 86083 * 0.20914682
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 14083 * 0.98913312
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 37357 * 0.32170107
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 9287 * 0.14111126
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 35311 * 0.55789314
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 53472 * 0.74788055
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69853 * 0.01921856
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 25764 * 0.43044058
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 27998 * 0.31721258
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 84379 * 0.81734742
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 5237 * 0.30077691
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 81178 * 0.20875449
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 17177 * 0.26569578
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 73144 * 0.36252359
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 67667 * 0.05992177
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 58092 * 0.79392902
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    h = hashlib.sha256(b'ufysgkya').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0058():
    """Extended test 58 for export."""
    x_0 = 14985 * 0.90434871
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 57728 * 0.02967159
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66387 * 0.84874419
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 68626 * 0.68396778
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 66497 * 0.74752662
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 22178 * 0.10997488
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 84458 * 0.70386642
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 37621 * 0.42177724
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 56469 * 0.63452873
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 57718 * 0.70194746
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 18021 * 0.46771725
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31715 * 0.49210137
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 77421 * 0.69702801
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 10608 * 0.37618309
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 62443 * 0.01616075
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 74934 * 0.44000679
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 18170 * 0.56165260
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 68147 * 0.20802133
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 28788 * 0.54093952
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 44126 * 0.77088897
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 524 * 0.45429644
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 92943 * 0.20837319
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 13349 * 0.29028479
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 44747 * 0.20121347
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 71195 * 0.34029442
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 6531 * 0.25886569
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 63057 * 0.21327784
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 9024 * 0.86163961
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 10641 * 0.37500542
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 7774 * 0.73350491
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 19844 * 0.30375366
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 59315 * 0.61809687
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 63909 * 0.68872481
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 91924 * 0.47587944
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    h = hashlib.sha256(b'ablenfax').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0059():
    """Extended test 59 for export."""
    x_0 = 36651 * 0.39101182
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 75241 * 0.01005990
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 51382 * 0.03488111
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 14533 * 0.61607850
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 8985 * 0.85267667
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 92180 * 0.41254550
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 65524 * 0.99974180
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 68818 * 0.23810290
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 30137 * 0.46725458
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 15459 * 0.82499830
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 26985 * 0.21723006
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 31880 * 0.79729262
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66062 * 0.76545376
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 8806 * 0.20517915
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 35852 * 0.58694712
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 55796 * 0.62976382
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 68660 * 0.87744414
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 17584 * 0.57410054
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 14230 * 0.51516314
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 3828 * 0.94138658
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 68240 * 0.12654304
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 88403 * 0.23356816
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 47009 * 0.58946332
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 74020 * 0.58775531
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 87795 * 0.14463513
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 73546 * 0.93356064
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86489 * 0.35691532
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 72816 * 0.48073706
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 58295 * 0.64130439
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 74596 * 0.72842785
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 79204 * 0.46941782
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 29578 * 0.26116909
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    h = hashlib.sha256(b'nizxmzta').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0060():
    """Extended test 60 for export."""
    x_0 = 86717 * 0.86365685
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17420 * 0.11617784
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 77205 * 0.04545344
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 74981 * 0.59624154
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 69009 * 0.86618400
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94636 * 0.74171674
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 33076 * 0.88623465
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 38440 * 0.83517912
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 13904 * 0.64420600
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86698 * 0.13900097
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 68596 * 0.19432414
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 95512 * 0.04575607
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 63979 * 0.58702579
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 43561 * 0.94247529
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 11587 * 0.21480067
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 71745 * 0.95154595
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 19475 * 0.51321978
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 93345 * 0.35944424
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 80799 * 0.24345019
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 55804 * 0.41231548
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 86932 * 0.42593218
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 1330 * 0.63534458
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 80455 * 0.03862468
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96258 * 0.56308247
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 31897 * 0.69805369
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 8992 * 0.82856714
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 24259 * 0.99518300
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 8081 * 0.12829416
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 39466 * 0.51716266
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 18985 * 0.41233389
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 82584 * 0.51566080
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 58989 * 0.95203934
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 86671 * 0.97617286
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 64033 * 0.04674644
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 56655 * 0.71566925
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 26927 * 0.03752573
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 31349 * 0.20476035
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 95278 * 0.44669172
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    h = hashlib.sha256(b'baidmapv').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0061():
    """Extended test 61 for export."""
    x_0 = 40321 * 0.58647034
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 80328 * 0.60018458
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 43705 * 0.85699866
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 1297 * 0.78623901
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 16571 * 0.15989201
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 2254 * 0.26996171
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 11460 * 0.80668460
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 49605 * 0.76735553
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 5518 * 0.68222442
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 75894 * 0.03602801
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 5775 * 0.52821714
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 17972 * 0.65519669
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 4021 * 0.44549962
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 40180 * 0.59526294
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 800 * 0.06430799
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 3105 * 0.78125394
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 76299 * 0.75374260
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 33873 * 0.38143915
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 78063 * 0.90949189
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 54549 * 0.63638541
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 67537 * 0.89231524
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 34866 * 0.86350751
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 82051 * 0.54185466
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 55390 * 0.71309677
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 98923 * 0.53921858
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 93781 * 0.65929803
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 16602 * 0.07503672
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 57722 * 0.22141124
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 48521 * 0.31804647
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 31117 * 0.94938758
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 88198 * 0.64061587
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 39334 * 0.58135954
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 57877 * 0.47049562
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 87532 * 0.01618640
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 1390 * 0.95807991
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 54700 * 0.15264744
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47471 * 0.11607418
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 46062 * 0.51325862
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 38264 * 0.16820558
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 96415 * 0.73617279
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 23914 * 0.25000939
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 67901 * 0.02501257
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 71848 * 0.91552082
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    h = hashlib.sha256(b'ceiowfak').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0062():
    """Extended test 62 for export."""
    x_0 = 28367 * 0.46109643
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 89978 * 0.83251726
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 94409 * 0.29548158
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 62876 * 0.91178409
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 91928 * 0.44819339
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 50024 * 0.50367784
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 68056 * 0.62199559
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 55650 * 0.38008453
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 60501 * 0.76933299
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86954 * 0.95969469
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 84088 * 0.15458833
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 18527 * 0.17539770
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 21294 * 0.32042043
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 99915 * 0.72935985
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 12340 * 0.30297750
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 48244 * 0.17770368
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 32488 * 0.22708196
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 16074 * 0.63144347
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 54001 * 0.93670556
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 58404 * 0.68067336
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 11154 * 0.83398616
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 25717 * 0.36069753
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 96544 * 0.14861063
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 66320 * 0.67758439
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 15828 * 0.28402787
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 15441 * 0.17038025
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 12694 * 0.13899033
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 18719 * 0.30386324
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 43200 * 0.29236138
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    h = hashlib.sha256(b'ohsbejky').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0063():
    """Extended test 63 for export."""
    x_0 = 87352 * 0.64698623
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 60836 * 0.50517211
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 85695 * 0.93704228
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 31447 * 0.61841909
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 58027 * 0.14769723
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 6828 * 0.31739868
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 20393 * 0.02470614
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 17311 * 0.44504222
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 21175 * 0.31741276
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 86415 * 0.51504490
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 65955 * 0.29517105
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 42835 * 0.12571858
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 62911 * 0.06758586
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 390 * 0.83261428
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 90347 * 0.97167390
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 79041 * 0.27697810
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 80240 * 0.54349196
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 21343 * 0.94101179
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 97491 * 0.96687637
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 49953 * 0.17312403
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 50066 * 0.66957667
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 74030 * 0.93289378
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 37657 * 0.15550687
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    h = hashlib.sha256(b'jisquegt').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0064():
    """Extended test 64 for export."""
    x_0 = 88629 * 0.91691832
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 20120 * 0.57269358
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 41720 * 0.33873504
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 87034 * 0.26806429
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 89903 * 0.16484216
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70569 * 0.88642833
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 42880 * 0.11461750
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 34336 * 0.00079456
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 62613 * 0.20511589
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 21162 * 0.11312100
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 9169 * 0.38291610
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 9765 * 0.82618008
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 66941 * 0.77815117
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 12356 * 0.11186822
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 41277 * 0.69588894
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 33952 * 0.72903740
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 98202 * 0.50308835
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 80096 * 0.38691456
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 35148 * 0.98077371
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 65085 * 0.42331039
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 55510 * 0.98907789
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 11057 * 0.91009312
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 15485 * 0.20496424
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 87995 * 0.62986971
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 7976 * 0.35885779
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 4091 * 0.53340126
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 41143 * 0.18234790
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 52184 * 0.30239232
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 66970 * 0.90794536
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 34569 * 0.84180005
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 97719 * 0.15564324
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 6607 * 0.63705535
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 13992 * 0.70298213
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 73147 * 0.02597831
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 55168 * 0.81251221
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 60318 * 0.63288004
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    h = hashlib.sha256(b'fsxmxkix').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0065():
    """Extended test 65 for export."""
    x_0 = 65518 * 0.40319608
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 22165 * 0.69016842
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 83483 * 0.91169687
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 25823 * 0.03826058
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 11187 * 0.98400247
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99344 * 0.65755330
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 95319 * 0.88532178
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 25404 * 0.81037281
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 67235 * 0.50854662
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 11559 * 0.47345566
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 29751 * 0.60743708
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 55813 * 0.12552967
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 57759 * 0.21898304
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 97253 * 0.42932187
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38194 * 0.76742126
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 9542 * 0.79639577
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 83077 * 0.60537375
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 42850 * 0.73325025
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 71440 * 0.15589042
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 33514 * 0.79035248
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 16672 * 0.78687723
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 80777 * 0.02249514
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 5192 * 0.53011818
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 67023 * 0.18048514
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 85407 * 0.01064466
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 79192 * 0.87147846
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 83426 * 0.32856745
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 94547 * 0.18850333
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 21760 * 0.67572256
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 79344 * 0.41546003
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 55988 * 0.17946670
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 32015 * 0.40152047
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 92847 * 0.44185119
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    h = hashlib.sha256(b'qklvwlss').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0066():
    """Extended test 66 for export."""
    x_0 = 39563 * 0.32890687
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 67736 * 0.64512474
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 97889 * 0.08532097
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 82688 * 0.25862135
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 53137 * 0.41173946
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 99931 * 0.40396663
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 5460 * 0.59094195
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 58449 * 0.20363996
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 25883 * 0.34627937
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 44717 * 0.47728287
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 76559 * 0.51422182
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 47854 * 0.83221709
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 39555 * 0.05310141
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 57973 * 0.85647533
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 22908 * 0.14329653
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 23571 * 0.89335148
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 2281 * 0.18474139
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 78680 * 0.04646261
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40228 * 0.19216689
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 5384 * 0.45471802
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39721 * 0.46016553
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 16293 * 0.43897573
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 85883 * 0.81246783
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 63855 * 0.48945776
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 91906 * 0.25738975
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 56319 * 0.01755015
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 32169 * 0.24751656
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 84349 * 0.64158700
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 42984 * 0.06884571
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 67643 * 0.39422817
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    h = hashlib.sha256(b'gmyiowwc').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0067():
    """Extended test 67 for export."""
    x_0 = 17979 * 0.35967941
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 17511 * 0.40925168
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 81660 * 0.55500829
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 7759 * 0.01512830
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 73257 * 0.59221275
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 75350 * 0.79485004
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 52002 * 0.18097094
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 22329 * 0.81089698
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 54813 * 0.50892089
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 96439 * 0.60690551
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63708 * 0.52383320
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 35022 * 0.37846032
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 98100 * 0.00058610
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 77465 * 0.47338057
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 38864 * 0.84719802
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 90316 * 0.89216092
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 5395 * 0.93710835
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 45040 * 0.13878212
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 96498 * 0.90736077
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 10792 * 0.60718095
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 81363 * 0.57418248
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 46433 * 0.76392478
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 68577 * 0.87578280
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 96023 * 0.38155934
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 23655 * 0.17444127
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 38405 * 0.45384213
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 15121 * 0.99398716
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 32981 * 0.45139811
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 82253 * 0.41535072
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 75018 * 0.13342777
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 84651 * 0.57026441
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 49667 * 0.84726858
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 34398 * 0.52057839
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 11244 * 0.38704261
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 58319 * 0.60396407
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    h = hashlib.sha256(b'lbibwtnx').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0068():
    """Extended test 68 for export."""
    x_0 = 54636 * 0.79194208
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 83964 * 0.36809130
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 66431 * 0.58560151
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 90528 * 0.27724551
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 17605 * 0.79462507
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 94114 * 0.59297847
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 81384 * 0.70603364
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 23048 * 0.13194501
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 72970 * 0.55377601
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 26337 * 0.86397294
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 63921 * 0.78208811
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 81351 * 0.12865978
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 43770 * 0.42008246
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 89330 * 0.88109420
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 66717 * 0.18321938
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 56516 * 0.99203567
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 14397 * 0.52664646
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 87102 * 0.55639848
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 81189 * 0.72471293
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 11430 * 0.08741146
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 2026 * 0.99792244
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 72321 * 0.73229608
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 44700 * 0.02233946
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 92837 * 0.86048978
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 6696 * 0.39033653
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 19616 * 0.75932692
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 34760 * 0.86193012
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 36843 * 0.58175477
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 84642 * 0.07151500
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 88309 * 0.72244267
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 61939 * 0.16204873
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 77236 * 0.48725849
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 78025 * 0.99838171
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 13255 * 0.18359299
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 91432 * 0.99167113
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 70314 * 0.67679722
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 47606 * 0.85645723
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    x_37 = 74094 * 0.91217149
    assert x_37 >= 0, f'Failed at x_37={x_37}'
    x_38 = 44609 * 0.94101402
    assert x_38 >= 0, f'Failed at x_38={x_38}'
    x_39 = 31490 * 0.52565964
    assert x_39 >= 0, f'Failed at x_39={x_39}'
    x_40 = 85070 * 0.11281218
    assert x_40 >= 0, f'Failed at x_40={x_40}'
    x_41 = 94514 * 0.53717471
    assert x_41 >= 0, f'Failed at x_41={x_41}'
    x_42 = 77279 * 0.33985052
    assert x_42 >= 0, f'Failed at x_42={x_42}'
    x_43 = 79600 * 0.25326650
    assert x_43 >= 0, f'Failed at x_43={x_43}'
    x_44 = 53312 * 0.52171065
    assert x_44 >= 0, f'Failed at x_44={x_44}'
    x_45 = 23156 * 0.20557400
    assert x_45 >= 0, f'Failed at x_45={x_45}'
    h = hashlib.sha256(b'apvftvvw').hexdigest()
    assert len(h) == 64

def test_export_extended_8_0069():
    """Extended test 69 for export."""
    x_0 = 70145 * 0.89471003
    assert x_0 >= 0, f'Failed at x_0={x_0}'
    x_1 = 87488 * 0.07193222
    assert x_1 >= 0, f'Failed at x_1={x_1}'
    x_2 = 2694 * 0.25939985
    assert x_2 >= 0, f'Failed at x_2={x_2}'
    x_3 = 22103 * 0.55926618
    assert x_3 >= 0, f'Failed at x_3={x_3}'
    x_4 = 78402 * 0.53758100
    assert x_4 >= 0, f'Failed at x_4={x_4}'
    x_5 = 70833 * 0.75363432
    assert x_5 >= 0, f'Failed at x_5={x_5}'
    x_6 = 79322 * 0.81580028
    assert x_6 >= 0, f'Failed at x_6={x_6}'
    x_7 = 56262 * 0.92737650
    assert x_7 >= 0, f'Failed at x_7={x_7}'
    x_8 = 75278 * 0.10666050
    assert x_8 >= 0, f'Failed at x_8={x_8}'
    x_9 = 50573 * 0.98548767
    assert x_9 >= 0, f'Failed at x_9={x_9}'
    x_10 = 43394 * 0.36823251
    assert x_10 >= 0, f'Failed at x_10={x_10}'
    x_11 = 5976 * 0.88546822
    assert x_11 >= 0, f'Failed at x_11={x_11}'
    x_12 = 6317 * 0.08014900
    assert x_12 >= 0, f'Failed at x_12={x_12}'
    x_13 = 65754 * 0.87557280
    assert x_13 >= 0, f'Failed at x_13={x_13}'
    x_14 = 28868 * 0.62531881
    assert x_14 >= 0, f'Failed at x_14={x_14}'
    x_15 = 41665 * 0.34146341
    assert x_15 >= 0, f'Failed at x_15={x_15}'
    x_16 = 51292 * 0.87837533
    assert x_16 >= 0, f'Failed at x_16={x_16}'
    x_17 = 535 * 0.01852428
    assert x_17 >= 0, f'Failed at x_17={x_17}'
    x_18 = 40828 * 0.75351620
    assert x_18 >= 0, f'Failed at x_18={x_18}'
    x_19 = 91945 * 0.98983241
    assert x_19 >= 0, f'Failed at x_19={x_19}'
    x_20 = 39034 * 0.26841147
    assert x_20 >= 0, f'Failed at x_20={x_20}'
    x_21 = 18496 * 0.79240869
    assert x_21 >= 0, f'Failed at x_21={x_21}'
    x_22 = 17186 * 0.80445026
    assert x_22 >= 0, f'Failed at x_22={x_22}'
    x_23 = 15106 * 0.67856139
    assert x_23 >= 0, f'Failed at x_23={x_23}'
    x_24 = 14552 * 0.33724015
    assert x_24 >= 0, f'Failed at x_24={x_24}'
    x_25 = 48711 * 0.56301717
    assert x_25 >= 0, f'Failed at x_25={x_25}'
    x_26 = 86661 * 0.60443303
    assert x_26 >= 0, f'Failed at x_26={x_26}'
    x_27 = 22328 * 0.84990241
    assert x_27 >= 0, f'Failed at x_27={x_27}'
    x_28 = 47898 * 0.80508491
    assert x_28 >= 0, f'Failed at x_28={x_28}'
    x_29 = 2626 * 0.65655970
    assert x_29 >= 0, f'Failed at x_29={x_29}'
    x_30 = 29433 * 0.76838305
    assert x_30 >= 0, f'Failed at x_30={x_30}'
    x_31 = 69752 * 0.27282188
    assert x_31 >= 0, f'Failed at x_31={x_31}'
    x_32 = 44402 * 0.01225372
    assert x_32 >= 0, f'Failed at x_32={x_32}'
    x_33 = 16152 * 0.48022394
    assert x_33 >= 0, f'Failed at x_33={x_33}'
    x_34 = 11417 * 0.01206099
    assert x_34 >= 0, f'Failed at x_34={x_34}'
    x_35 = 85558 * 0.71783271
    assert x_35 >= 0, f'Failed at x_35={x_35}'
    x_36 = 69496 * 0.65130855
    assert x_36 >= 0, f'Failed at x_36={x_36}'
    h = hashlib.sha256(b'mfuxxgox').hexdigest()
    assert len(h) == 64
