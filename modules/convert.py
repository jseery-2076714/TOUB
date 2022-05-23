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
    
    # Split message up
    words = message.split(' ')
    # find units of measurement in message
    for i in range(len(words)):
        # if number found, check if unit follows after
        if(words[i].isnumeric()):
            if(i == len(words)-1):
                break
            value = words[i]

            # find unit
            unitsCheck = sheets.get_col('unit')
            if(sheets.level == 1):
                unitsCheck = unitsCheck[:8]
            for unit in unitsCheck:
                # convert to different unit based on level of bot and update message
                if(unit in words[i+1].lower() or sheets.get_data(unit)[4] in words[i+1].lower()):
                    newUnit = unit_select(unit, sheets.get_level())
                    result = convert_unit(float(value), unit, newUnit)
                    while(result == ''):
                        newUnit = unit_select(unit, sheets.get_level())
                        result = convert_unit(float(value), unit, newUnit)
                    (resValue, resUnit) = result.split(' ')
                    words[i] = resValue
                    words[i+1] = resUnit
                    i+=1    
                    break;      
    # combine message back with newly converted unites
    return ' '.join(words)


## Given the value of current, current, and target
### Return the value in terms of target
def convert_unit(value, current, target):
    ### retrieved rows from sheets
    currentValue, currentIndex = sheets.get_value(current)
    targetValue = sheets.get_data(target)[currentIndex]
    if(not targetValue):
        return ''
    return str(value * currentValue/targetValue) + " " + str(target)


# Given the current unit and bot level of chaos
# Return randomly selected unit from sheet
def unit_select(unit, level):
    if(level == 1):
        return "centimeter"
    # get possible units
    units = sheets.get_col('unit')
    # Level 3, Crazy Units Only
    if(sheets.level == 3):
        units = units[10:]
    # pick one
    newUnit = rd.choice(units)
    # if it is the same unit, pick a new one
    while (newUnit == unit):
        newUnit = rd.choice(units)
    return newUnit
