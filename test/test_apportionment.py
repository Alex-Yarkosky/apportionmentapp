import pytest
from csv import reader
from src import apportionment

''' Testing that state populations from 2010 Census are successfully retrieved from the text file '''
def test_get_state_populations():
    expected = ['4779736','710231','6392017','2915918','37253956','5029196','3574097','897934','18801310','9687653','1360301','1567582','12830632','6483802','3046355','2853118','4339367','4533372','1328361','5773552','6547629','9883640','5303925','2967297','5988927','989415','1826341','2700551','1316470','8791894','2059179','19378102','9535483','672591','11536504','3751351','3821074','12702379','1052567','4625364','814180','6346105','25145561','2763885','625741','8001024','6724540','1852994','5686986','563626',]
    output = apportionment.get_state_populations('2010')
    assert expected == output

''' Testing that the national population is found by combining all of the state populations from the 2010 Census '''
def test_find_nationational_pop():
    expected = 308133815
    output = apportionment.find_national_pop('2010')
    assert expected == output

''' Testing Hamilton Method apportions correctly for 435 seats with the 2010 Census '''
def test_hamilton_method():
    expected = [7,1,9,4,53,7,5,1,27,14,2,2,18,9,4,4,6,6,2,8,9,14,8,4,8,1,3,4,2,12,3,27,13,1,16,5,5,18,2,7,1,9,36,4,1,11,10,3,8,1,]
    output = apportionment.hamilton_method(435, '2010')
    assert expected == output

''' Testing Jefferson Method apportions correctly for 435 seats with the 2010 Census '''
def test_jefferson_method():
    expected = [7,1,9,4,55,7,5,1,27,14,2,2,19,9,4,4,6,6,1,8,9,14,7,4,8,1,2,4,1,13,3,28,14,1,17,5,5,18,1,6,1,9,37,4,1,11,9,2,8,1,]
    output = apportionment.jefferson_method(435, '2010')
    assert expected == output

''' Testing Lowndes Method apportions correctly for 435 seats with the 2010 Census '''
def test_lowndes_method():
    expected = [6,2,10,5,52,8,6,2,26,13,1,3,19,10,5,5,7,6,1,9,10,13,7,5,8,1,2,3,1,12,2,27,13,1,17,6,5,17,1,6,2,8,35,3,1,12,9,2,9,1,]
    output = apportionment.lowndes_method(435, '2010')
    assert expected == output

''' Testing Adams Method apportions correctly for 435 seats with the 2010 Census '''
def test_adams_method():
    expected = [7,1,9,4,50,7,5,2,26,13,2,3,18,9,5,4,6,7,2,8,9,14,8,4,9,2,3,4,2,12,3,26,13,1,16,6,6,18,2,7,2,9,34,4,1,11,9,3,8,1,]
    output = apportionment.adams_method(435, '2010')
    assert expected == output

''' Testing Webster Method apportions correctly for 435 seats with the 2010 Census '''
def test_webster_method():
    expected = [7,1,9,4,53,7,5,1,27,14,2,2,18,9,4,4,6,6,2,8,9,14,8,4,8,1,3,4,2,12,3,27,14,1,16,5,5,18,1,7,1,9,36,4,1,11,10,3,8,1,]
    output = apportionment.webster_method(435, '2010')
    assert expected == output

''' Testing Huntington-Hill Method apportions correctly for 435 seats with the 2010 Census '''
def test_huntington_hill_method():
    expected = [7,1,9,4,53,7,5,1,27,14,2,2,18,9,4,4,6,6,2,8,9,14,8,4,8,1,3,4,2,12,3,27,13,1,16,5,5,18,2,7,1,9,36,4,1,11,10,3,8,1,]
    output = apportionment.huntington_hill_method(435, '2010')
    assert expected == output

''' Testing Dean Method apportions correctly for 435 seats with the 2010 Census '''
def test_dean_method():
    expected = [7,1,9,4,53,7,5,1,27,14,2,2,18,9,4,4,6,6,2,8,9,14,8,4,8,2,3,4,2,12,3,27,13,1,16,5,5,18,2,7,1,9,35,4,1,11,10,3,8,1,]
    output = apportionment.dean_method(435, '2010')
    assert expected == output

''' Testing Hamilton Method apportions correctly for 135 seats with the 1900 Census '''
def test_hamilton_method_few_seats():
    expected = [3,1,1,3,2,1,1,1,1,4,1,1,8,4,4,2,4,2,1,2,5,4,3,2,5,1,2,1,1,3,1,13,3,1,7,1,1,11,1,2,1,3,5,1,1,3,1,1,3,1,]
    output = apportionment.hamilton_method(135, '1900')
    assert expected == output

''' Testing Jefferson Method apportions correctly for 135 seats with the 1900 Census '''
def test_jefferson_method_few_seats():
    expected = [3,1,1,3,2,1,1,1,1,4,1,1,9,4,4,2,4,2,1,2,5,4,3,2,5,1,1,1,1,3,1,13,3,1,7,1,1,11,1,2,1,3,5,1,1,3,1,1,3,1,]
    output = apportionment.jefferson_method(135, '1900')
    assert expected == output

''' Testing Lowndes Method apportions correctly for 135 seats with the 1900 Census '''
def test_lowndes_method_few_seats():
    expected = [4,1,1,4,2,1,1,1,1,3,1,1,8,4,3,2,3,2,2,3,4,4,4,2,5,1,1,1,1,3,1,12,3,1,7,1,1,12,1,2,1,3,5,1,1,3,1,1,3,1,]
    output = apportionment.lowndes_method(135, '1900')
    assert expected == output

''' Testing Adams Method apportions correctly for 135 seats with the 1900 Census '''
def test_adams_method_few_seats():
    expected = [3,1,1,3,3,1,2,1,1,4,1,1,7,4,4,3,4,2,1,2,5,4,3,3,5,1,2,1,1,3,1,11,3,1,6,2,1,9,1,2,1,3,5,1,1,3,1,2,3,1,]
    output = apportionment.adams_method(135, '1900')
    assert expected == output

''' Testing Webster Method apportions correctly for 135 seats with the 1900 Census '''
def test_webster_method_few_seats():
    expected = [3,1,1,3,2,1,1,1,1,4,1,1,8,4,4,2,4,2,1,2,5,4,3,3,5,1,2,1,1,3,1,12,3,1,7,1,1,10,1,2,1,3,5,1,1,3,1,2,3,1,]
    output = apportionment.webster_method(135, '1900')
    assert expected == output

''' Testing Huntington-Hill Method apportions correctly for 135 seats with the 1900 Census '''
def test_huntington_hill_method_few_seats():
    expected = [3,1,1,3,2,1,2,1,1,4,1,1,8,4,4,2,3,2,1,2,5,4,3,3,5,1,2,1,1,3,1,12,3,1,7,1,1,10,1,2,1,3,5,1,1,3,1,2,3,1,]
    output = apportionment.huntington_hill_method(135, '1900')
    assert expected == output

''' Testing Dean Method apportions correctly for 135 seats with the 1900 Census '''
def test_dean_method_few_seats():
    expected = [3,1,1,3,2,1,2,1,1,4,1,1,8,4,4,2,3,2,1,2,5,4,3,3,5,1,2,1,1,3,1,12,3,1,7,1,1,10,1,2,1,3,5,1,1,3,1,2,3,1,]
    output = apportionment.dean_method(135, '1900')
    assert expected == output

''' Testing average constiuencies number is calculated correctly for Huntington-Hill apportionment for 435 seats with the 2010 Census '''
def test_average_constituencies():
    expected = 710149.4864537753
    app = [7,1,9,4,53,7,5,1,27,14,2,2,18,9,4,4,6,6,2,8,9,14,8,4,8,1,3,4,2,12,3,27,13,1,16,5,5,18,2,7,1,9,36,4,1,11,10,3,8,1]
    output = apportionment.average_constituencies(app, 2010)
    assert expected == output

''' Testing multiple runs for varying house size '''
def test_multiple_runs_variable_house_size():
    expected = [['hamilton', '2010', '430', '714743.2213626188'],[],['lowndes', '2010', '430', '763505.6330012811'],[],['jefferson', '2010', '430', '767281.5906495652'],[],['adams', '2010', '430', '677715.6511431522'],[],['webster', '2010', '430', '724998.5433510079'],[],['dean', '2010', '430', '707051.6256483331'],[],['huntington-hill', '2010', '430', '714743.2213626188'],[],['hamilton', '2010', '431', '712848.9624340474'],[],['lowndes', '2010', '431', '765501.7177619174'],[],['jefferson', '2010', '431', '766433.3182966241'],[],['adams', '2010', '431', '676877.0477444595'],[],['webster', '2010', '431', '724462.8934934579'],[],['dean', '2010', '431', '704849.0713626188'],[],['huntington-hill', '2010', '431', '714472.8733510077'],[],['hamilton', '2010', '432', '711354.6202118252'],[],['lowndes', '2010', '432', '755678.828465621'],[],['jefferson', '2010', '432', '766182.4499060517'],[],['adams', '2010', '432', '676298.5458983055'],[],['webster', '2010', '432', '724063.7576045691'],[],['dean', '2010', '432', '702954.8124340475'],[],['huntington-hill', '2010', '432', '713937.2234934579'],[],['hamilton', '2010', '433', '710818.9703542753'],[],['lowndes', '2010', '433', '755217.0616076388'],[],['jefferson', '2010', '433', '765055.2840086159'],[],['adams', '2010', '433', '673797.6452316388'],[],['webster', '2010', '433', '722569.4153823468'],[],['dean', '2010', '433', '701460.4702118252'],[],['huntington-hill', '2010', '433', '712442.8812712356'],[],['hamilton', '2010', '434', '710548.6223426643'],[],['lowndes', '2010', '434', '745536.4454472923'],[],['jefferson', '2010', '434', '764304.9546518907'],[],['adams', '2010', '434', '672134.0543983056'],[],['webster', '2010', '434', '720675.1564537754'],[],['dean', '2010', '434', '700924.8203542753'],[],['huntington-hill', '2010', '434', '710548.6223426643'],[],['hamilton', '2010', '435', '710149.4864537753'],[],['lowndes', '2010', '435', '742490.0904472923'],[],['jefferson', '2010', '435', '759804.0363185572'],[],['adams', '2010', '435', '671303.8335486325'],[],['webster', '2010', '435', '719627.30117905'],[],['dean', '2010', '435', '700654.4723426643'],[],['huntington-hill', '2010', '435', '710149.4864537753'],[],['hamilton', '2010', '436', '709101.6311790501'],[],['lowndes', '2010', '436', '732595.9404472923'],[],['jefferson', '2010', '436', '758309.694096335'],[],['adams', '2010', '436', '669809.4913264102'],[],['webster', '2010', '436', '719114.6529779918'],[],['dean', '2010', '436', '700255.3364537754'],[],['huntington-hill', '2010', '436', '709101.6311790501'],[],['hamilton', '2010', '437', '707438.0403457168'],[],['lowndes', '2010', '437', '743324.3789662435'],[],['jefferson', '2010', '437', '757812.3049428959'],[],['adams', '2010', '437', '669257.4086483475'],[],['webster', '2010', '437', '717451.0621446585'],[],['dean', '2010', '437', '699207.4811790502'],[],['huntington-hill', '2010', '437', '707438.0403457168'],[],['hamilton', '2010', '438', '716323.8962472227'],[],['lowndes', '2010', '438', '740278.0239662433'],[],['jefferson', '2010', '438', '757069.4757616093'],[],['adams', '2010', '438', '668192.8313956003'],[],['webster', '2010', '438', '716323.8962472227'],[],['dean', '2010', '438', '697543.8903457167'],[],['huntington-hill', '2010', '438', '706925.3921446586'],[],['hamilton', '2010', '439', '705798.2262472227'],[],['lowndes', '2010', '439', '742793.6958323402'],[],['jefferson', '2010', '439', '756592.1826088999'],[],['adams', '2010', '439', '667900.6435054042'],[],['webster', '2010', '439', '705798.2262472227'],[],['dean', '2010', '439', '697031.2421446586'],[],['huntington-hill', '2010', '439', '705798.2262472227'],[],['hamilton', '2010', '440', '704949.9538942815'],[],['lowndes', '2010', '440', '739747.3408323401'],[],['jefferson', '2010', '440', '755379.9062452635'],[],['adams', '2010', '440', '664933.3465054042'],[],['webster', '2010', '440', '704949.9538942815'],[],['dean', '2010', '440', '695904.0762472227'],[],['huntington-hill', '2010', '440', '695904.0762472227'],[],]
    apportionment.multiple_runs_variable_house_size(430, 440, 2010)
    output = []
    with open('apportionments.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            output.append(row)
    assert expected == output

''' Testing multiple runs for varying census year '''
def test_multiple_runs_varible_year():
    expected = [['Hamilton', '1900', '435', '171461.34579717205'],[],['Lowndes', '1900', '435', '171266.79465830847'],[],['Jefferson', '1900', '435', '177730.23791488245'],[],['Adams', '1900', '435', '161534.4556680634'],[],['Webster', '1900', '435', '171461.34579717205'],[],['Dean', '1900', '435', '167499.6280518286'],[],['Huntington-Hill', '1900', '435', '171461.34579717205'],[],['Hamilton', '1910', '435', '207038.90285103107'],[],['Lowndes', '1910', '435', '221675.5572292543'],[],['Jefferson', '1910', '435', '225314.52225272555'],[],['Adams', '1910', '435', '197560.52982178662'],[],['Webster', '1910', '435', '200972.8211893051'],[],['Dean', '1910', '435', '199896.17980753872'],[],['Huntington-Hill', '1910', '435', '207038.90285103107'],[],['Hamilton', '1920', '435', '241528.39096789074'],[],['Lowndes', '1920', '435', '243326.12973594517'],[],['Jefferson', '1920', '435', '259133.6770224385'],[],['Adams', '1920', '435', '226279.8712687014'],[],['Webster', '1920', '435', '241528.39096789074'],[],['Dean', '1920', '435', '229691.19482803735'],[],['Huntington-Hill', '1920', '435', '241528.39096789074'],[],['Hamilton', '1930', '435', '277868.9940796861'],[],['Lowndes', '1930', '435', '297758.800386097'],[],['Jefferson', '1930', '435', '300651.9686532415'],[],['Adams', '1930', '435', '258751.55808224657'],[],['Webster', '1930', '435', '277868.9940796861'],[],['Dean', '1930', '435', '269680.0126641958'],[],['Huntington-Hill', '1930', '435', '277868.9940796861'],[],['Hamilton', '1940', '435', '293981.08409297606'],[],['Lowndes', '1940', '435', '314841.6671414882'],[],['Jefferson', '1940', '435', '330530.8869274366'],[],['Adams', '1940', '435', '278710.93573120545'],[],['Webster', '1940', '435', '293981.08409297606'],[],['Dean', '1940', '435', '289889.537042471'],[],['Huntington-Hill', '1940', '435', '293981.08409297606'],[],['Hamilton', '1950', '435', '342752.28274964285'],[],['Lowndes', '1950', '435', '364171.62807676883'],[],['Jefferson', '1950', '435', '369638.736133379'],[],['Adams', '1950', '435', '320880.720802837'],[],['Webster', '1950', '435', '337647.5234593203'],[],['Dean', '1950', '435', '332056.24969443405'],[],['Huntington-Hill', '1950', '435', '342752.28274964285'],[],['Hamilton', '1960', '435', '412998.2729870068'],[],['Lowndes', '1960', '435', '419180.289908478'],[],['Jefferson', '1960', '435', '440057.5068501055'],[],['Adams', '1960', '435', '381277.48174236924'],[],['Webster', '1960', '435', '405448.8847139909'],[],['Dean', '1960', '435', '400039.7488165551'],[],['Huntington-Hill', '1960', '435', '412998.2729870068'],[],['Hamilton', '1970', '435', '468517.6852536904'],[],['Lowndes', '1970', '435', '474140.49297161296'],[],['Jefferson', '1970', '435', '501599.2373004071'],[],['Adams', '1970', '435', '433511.99597179616'],[],['Webster', '1970', '435', '469627.4802536904'],[],['Dean', '1970', '435', '457264.1356346427'],[],['Huntington-Hill', '1970', '435', '468517.6852536904'],[],['Hamilton', '1980', '435', '525407.6642583612'],[],['Lowndes', '1980', '435', '543311.7267567306'],[],['Jefferson', '1980', '435', '580293.3387418694'],[],['Adams', '1980', '435', '489826.0555111902'],[],['Webster', '1980', '435', '517769.4396400037'],[],['Dean', '1980', '435', '514423.3221854583'],[],['Huntington-Hill', '1980', '435', '525407.6642583612'],[],['Hamilton', '1990', '435', '578031.6990385669'],[],['Lowndes', '1990', '435', '589565.6720170501'],[],['Jefferson', '1990', '435', '608801.1870758996'],[],['Adams', '1990', '435', '539289.9141058848'],[],['Webster', '1990', '435', '577042.5509359684'],[],['Dean', '1990', '435', '567676.8538215272'],[],['Huntington-Hill', '1990', '435', '578031.6990385669'],[],['Hamilton', '2000', '435', '649658.7363957916'],[],['Lowndes', '2000', '435', '678305.7555981469'],[],['Jefferson', '2000', '435', '691757.7814987'],[],['Adams', '2000', '435', '615795.4444149333'],[],['Webster', '2000', '435', '649658.7363957916'],[],['Dean', '2000', '435', '638192.6042283992'],[],['Huntington-Hill', '2000', '435', '649658.7363957916'],[],['Hamilton', '2010', '435', '710149.4864537753'],[],['Lowndes', '2010', '435', '742490.0904472923'],[],['Jefferson', '2010', '435', '759804.0363185572'],[],['Adams', '2010', '435', '671303.8335486325'],[],['Webster', '2010', '435', '719627.30117905'],[],['Dean', '2010', '435', '700654.4723426643'],[],['Huntington-Hill', '2010', '435', '710149.4864537753'],[],]
    apportionment.multiple_runs_varible_year(435)
    output = []
    with open('apportionments.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            output.append(row)
    assert expected == output
