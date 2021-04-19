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
