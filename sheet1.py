import gspread

from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('vehiclebookings')
catalogue = SHEET.worksheet('catalogue')
c_data = catalogue.get_all_values()
appraisals = SHEET.worksheet('appraisals')
dan = "dan"


def a_data():
    a_data = appraisals.get_all_values()
    return a_data


def a_dict():
    a_dict = appraisals.get_all_records()
    return a_dict


def c_dict():
    c_dict = catalogue.get_all_records()
    return c_dict
