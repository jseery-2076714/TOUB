# Google sheets API
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

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

def set_up_api():
    global records
    global level
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('./modules/creds.json', scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheetß
    sheet = client.open('Conversions')

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)

    # get all the records of the data
    records_data = sheet_instance.get_all_records()
    level = 1
    records = pd.DataFrame.from_dict(records_data)