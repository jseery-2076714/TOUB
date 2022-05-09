import sheets

### Coversion code will be written here

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
    resultValue = centimeters/float(targetRow['cm'])

    return str(resultValue) + " " + str(target)

    