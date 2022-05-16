# Database/Google Sheets API/backend processing tests
import importlib, importlib.util


def module_directory(name_module, path):
    P = importlib.util.spec_from_file_location(name_module, path)
    import_module = importlib.util.module_from_spec(P)
    P.loader.exec_module(import_module)
    return import_module


sheets = module_directory("sheets", "./modules/sheets.py")
convert = module_directory("convert", "./modules/convert.py")
sheets.set_up_api()


def test_retrieve():
    assert sheets.get_data('feet') == ['feet', 30.48, 929.0304, 28316.84659, 'ft']


def test_convert():
    assert convert.convert_unit(1, 'feet', 'yard') == '0.33333333333333337 yard'
    assert convert.convert_unit(2, 'feet', 'yard') == '0.66666666666666674 yard'


def test_select():
    assert convert.unit_select('feet', 1) != 'feet'


# def test_parse():
#     assert convert.parse_message('1 feet') == 'Converted message'
