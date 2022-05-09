import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import os

### Returns the row of the given unit
def retrieveData(unit):
    # Set 'Name' column as index 
    # on a Dataframe

    # Using the operator .loc[]
    # to select single row
    result = records.loc[records['Unit'] == unit]
    return result


def setUpAPI():
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
    global records
    records = pd.DataFrame.from_dict(records_data)
    print(records)