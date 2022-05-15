# Database/Google Sheets API/backend processing tests
import importlib, importlib.util
 
def module_directory(name_module, path):
    P = importlib.util.spec_from_file_location(name_module, path)
    import_module = importlib.util.module_from_spec(P)
    P.loader.exec_module(import_module)
    return import_module
 
sheets = module_directory("result", "./modules/sheets.py")
convert = module_directory("result", "./modules/convert.py")

def test_retrieve():
    assert sheets.get_data('cm') == "Centimeter, 1, 1, 1"


def test_convert():
    assert convert.convertUnit('1', 'inch', 'cm') == '2.54 cm'


def test_select():
    assert convert.unitSelect('cm', 1) == 'Randomly selected new unit'


def test_parse():
    assert convert.parseMessage('Message 1 cm') == 'Converted message'
