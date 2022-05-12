# Database/Google Sheets API/backend processing tests
import sys

from src import sheets
from src import convert


def test_retrieve():
    assert sys.path == ''
    assert sheets.get_data('cm') == "Centimeter, 1, 1, 1"


def test_convert():
    assert convert.convertUnit('1', 'inch', 'cm') == '2.54 cm'


def test_select():
    assert convert.unitSelect('cm', 1) == 'Randomly selected new unit'


def test_parse():
    assert convert.parseMessage('Message 1 cm') == 'Converted message'
