# Parsing and conversion
import random as rd
import sheets

# Given a message from Discord
# Return converted message
def parseMessage(message):
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
            for unit in sheets.records['Unit'].tolist():
                # convert to different unit based on level of bot and update message
                if(unit in words[i+1].lower()):
                    (resValue, resUnit) = convertUnit(float(value), unit, unitSelect(unit, sheets.level)).split(' ')
                    words[i] = resValue
                    words[i+1] = resUnit
                    i+=1    
                    break;      
    # combine message back with newly converted unites
    return ' '.join(words)


## Given the value of current, current, and target
### Return the value in terms of target
def convertUnit(value, current, target):
    ### retrieved rows from sheets
    cv = float(sheets.get_data(current)[1])
    tv = float(sheets.get_data(target)[1])
    return str(value * cv/tv) + " " + str(target)


# Given the current unit and bot level of chaos
# Return randomly selected unit from sheet
def unitSelect(unit, level):
    if(level == 1):
        return "centimeter"
    # get possible units
    units = sheets.get_col('unit')
    # pick one
    newUnit = rd.choice(units)
    # if it is the same unit, pick a new one
    while (newUnit == unit):
        newUnit = rd.choice(units)
    return newUnit
