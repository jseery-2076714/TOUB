# Database/Google Sheets API/backend processing tests
# testInsert
from src.convert import convert, unitSelect, parse
from src.sheets import retrieveData


def test_retrieve():
    assert retrieveData('cm') == "Centimeter, 1, 1, 1"


def test_convert():
    assert convert('1', 'inch', 'cm') == '2.54 cm'


def test_select():
    assert unitSelect('cm', 1) == 'Randomly selected new unit'


def test_parse():
    assert parse('Message 1 cm') == 'Converted message'
