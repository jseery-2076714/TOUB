# Google sheets API
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import os

worksheet = None
records = pd.DataFrame.from_dict({})
level = 0

# Returns the column names as a list
def get_columns():
    return records.columns.to_list()

# Returns the column with colname
def get_col(colname):
    return records[colname]

# Returns the information and conversions of the unit as a list
def get_data(unit):
    return records.loc[records['unit'] == unit].values.flatten().tolist()

def add_unit(unit, value, dimension):
    row = []
    if(dimension == 1):
        row = [unit, value]
    elif(dimension == 2):
        row = [unit, '', value]
    else:
        row = [unit, '', '', value]
    worksheet.append_row([unit, value])
    records.loc[len(records.index)] = row
    return

def set_up_api():
    global records
    global level
    global worksheet
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.getcwd() +'/src/creds.json', scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open('Conversions')

    # get the first sheet of the Spreadsheet
    worksheet = sheet.get_worksheet(0)

    # get all the records of the data
    records_data = worksheet.get_all_records()
    level = 1
    records = pd.DataFrame.from_dict(records_data)