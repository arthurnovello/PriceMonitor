import httplib2
import os

from apiclient import discovery
from google.oauth2 import service_account

try:
    scopes = ["https://www.googleapis.com/auth/drive",
              "https://www.googleapis.com/auth/drive.file",
              "https://www.googleapis.com/auth/spreadsheets"]
    secret_file = os.path.join(os.getcwd(), 'client_secret.json')

    spreadsheet_id = '1Jgsf-5wtsCdyDiIp-P_EZbnoT6Ya_0URC3I8s1-5GeM'
    range_name = 'Sheet1!A1:D2'

    credentials = service_account.Credentials.from_service_account_file(
        secret_file, scopes=scopes)
    service = discovery.build('sheets', 'v4', credentials=credentials)

    values = [
        ['a1', 'b1', 'c1', 123],
        ['a2', 'b2', 'c2', 456],
    ]

    data = {
        'values': values
    }

    service.spreadsheets().values().update(
                                           spreadsheetId=spreadsheet_id,
                                           body=data, range=range_name,
                                           valueInputOption='USER_ENTERED'
                                           ).execute()

except OSError as e:
    print(e)
