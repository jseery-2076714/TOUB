import sheets

### Coversion code will be written here

def convert(value, unit1, unit2):
    print("Converting " + str(value) + " " + str(unit1) + " to " + str(unit2))
    return str(float(sheets.retrieveData(unit1)) * value) + " " + str(unit2)
    ### get row associated to unit1 from Google Sheets API
    ### convert based on retreived value
    ### return conversion

    