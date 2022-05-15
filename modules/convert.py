# Parsing and conversion
import random as rd
import importlib, importlib.util
 
def module_directory(name_module, path):
    P = importlib.util.spec_from_file_location(name_module, path)
    import_module = importlib.util.module_from_spec(P)
    P.loader.exec_module(import_module)
    return import_module

sheets = module_directory("sheets", "./modules/sheets.py")
sheets.set_up_api()

# Given a message from Discord
# Return converted message
def parse_message(message):
    # error checking
    # ensuring message contains a value and a unit to convert
    # check what level of chaos the bot is set to
    # selectedNewUnit = unitSelect(parsedUnit, chaosLevel)
    # newMessage = convert(parsedValue, parsedUnit, selectedNewUnit)
    words = message.split(' ')
    for i in range(len(words)):
        if(words[i].isnumeric()):
            if(i == len(words)-1):
                break
            value = words[i]
            for unit in sheets.get_col('unit'):
                if(unit in words[i+1].lower()):
                    (resValue, resUnit) = convert_unit(float(value), unit, unit_select(unit, sheets.get_level())).split(' ')
                    words[i] = resValue
                    words[i+1] = resUnit
                    i+=1    
                    break;      
    return ' '.join(words)


## Given the value of current, current, and target
### Return the value in terms of target
def convert_unit(value, current, target):
    ### retrieved rows from sheets
    cv = float(sheets.get_data(current)[1])
    tv = float(sheets.get_data(target)[1])
    return str(value * cv/tv) + " " + str(target)


# Given the current unit and bot level of chaos
# Return randomly selected unit from sheet
def unit_select(unit, level):
    # get possible units
    units = sheets.get_col('unit')
    # pick one
    newUnit = rd.choice(units)
    # if it is the same unit, pick a new one
    while (newUnit == unit):
        newUnit = rd.choice(units)
    return newUnit
