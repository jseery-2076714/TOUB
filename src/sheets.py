import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import os

records = pd.DataFrame.from_dict({})
level = 0

### Returns the conversions to SI of the given unit
def retrieveData(unit):
    return records.loc[records['Unit'] == unit]


def setUpAPI():
    global records
    global level
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.getcwd() +'/src/creds.json', scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open('Conversions')

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)

    # get all the records of the data
    records_data = sheet_instance.get_all_records()

    level = 1
    records = pd.DataFrame.from_dict(records_data)