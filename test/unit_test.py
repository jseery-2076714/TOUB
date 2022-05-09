# Database/Google Sheets API/backend processing tests
# testInsert
#import sys
#import os
from ..src.convert import *
from ..src.sheets import *
#sys.path.append(os.path.abspath("/home/runner/work/TOUB/TOUB/src"))
#from convert import convertUnit, unitSelect, parseMessage
#from sheets import retrieveData


def test_retrieve():
    assert retrieveData('cm') == "Centimeter, 1, 1, 1"


def test_convert():
    assert convertUnit('1', 'inch', 'cm') == '2.54 cm'


def test_select():
    assert unitSelect('cm', 1) == 'Randomly selected new unit'


def test_parse():
    assert parseMessage('Message 1 cm') == 'Converted message'
