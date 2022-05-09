import sheets


### Parsing and conversion code will be written here

# Given a message from Discord
# Return converted message
def parse(message):
    # error checking
    # ensuring message contains a value and a unit to convert
    # check what level of chaos the bot is set to
    # selectedNewUnit = unitSelect(parsedUnit, chaosLevel)
    # newMessage = convert(parsedValue, parsedUnit, selectedNewUnit)
    return "Converted message"


## Given the value of current, current, and target
### Return the value in terms of target
def convert(value, current, target):
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
    return "Randomly selected new unit"
