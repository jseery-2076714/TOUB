from random import Random
from src import sheets



### Parsing and conversion code will be written here

# Given a message from Discord
# Return converted message
def parseMessage(message):
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
            for unit in sheets.records['Unit'].tolist():
                if(unit in words[i+1].lower()):
                    (resValue, resUnit) = convertUnit(float(value), unit, unitSelect(unit, sheets.level)).split(' ')
                    words[i] = resValue
                    words[i+1] = resUnit
                    i+=1    
                    break;      
    return ' '.join(words)


## Given the value of current, current, and target
### Return the value in terms of target
def convertUnit(value, current, target):
    print("Converting " + str(value) + " " + str(current) + " to " + str(target))
    ### retrieved rows from sheets
    currentRow = sheets.retrieveData(current)
    targetRow = sheets.retrieveData(target)
    ### convert current value to centimeters
    centimeters = float(currentRow['cm']) * value
    ### get value in terms of target
    resultValue = centimeters / float(targetRow['cm'])
    return str(resultValue) + " " + str(target)


# Given the current unit and bot level of chaos
# Return randomly selected unit from sheet
def unitSelect(unit, level):
    # Randomly select new unit from sheet depending on level of chaos
    rand = Random()
    units = sheets.records['Unit'].tolist()
    foundUnit = True
    while(foundUnit):
        index = rand.randint(0, 8)
        if(unit != units[index]):
            return units[index]
        else:
            break

    return "centimeter"
