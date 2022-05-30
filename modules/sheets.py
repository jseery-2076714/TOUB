# Google sheets API
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

worksheet = None
records = pd.DataFrame.from_dict({})
level = 1

def get_records():
    return records

def get_level():
    return level

def set_level(newLevel):
    level = newLevel
    

# Returns the column names as a list
def get_columns():
    return records.columns.to_list()

# Returns the column with colname
def get_col(colname):
    return records[colname]

# Returns the information and conversions of the unit as a list
def get_data(unit):
    if(not worksheet):
        set_up_api()
    return records.loc[(records['unit'] == unit) | (records['short name'] == unit)].values.flatten().tolist()

def get_value(unit):
    row = get_data(unit)
    index = 1
    while(not row[index]):
        index += 1
    return float(row[index])**(1/index), index

def add_unit(unit, value, dimension):
    if(not worksheet):
        set_up_api()
    if(unit in records['unit'].unique()):
        rowNum = records[records['unit'] == unit].index[0]
        records.iloc[[rowNum],[dimension]] = value
        worksheet.update_cell((rowNum+2), dimension+1, value)
    else:
        row = []
        if(dimension == 1):
            row = [unit, value, '', '', '']
        elif(dimension == 2):
            row = [unit, '', value, '', '']
        else:
            row = [unit, '', '', value, '']
        worksheet.append_row(row)
        records.loc[len(records.index)] = row
    return

def set_up_api():
    global records
    global level
    global worksheet
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('./modules/creds.json', scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheetß
    sheet = client.open('Conversions')

    # get the first sheet of the Spreadsheet
    worksheet = sheet.get_worksheet(0)

    # get all the records of the data
    records_data = worksheet.get_all_records()
    level = 1
    records = pd.DataFrame.from_dict(records_data)