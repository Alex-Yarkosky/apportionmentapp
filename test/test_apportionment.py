import pytest
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
