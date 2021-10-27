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
CATALOGUE = SHEET.worksheet('catalogue')
APPRAISALS = SHEET.worksheet('appraisals')
LOGINS = SHEET.worksheet('logins')


def get_logins() -> list:
    """
    Pull all values from logins work sheet and return as list
    of lists
    """
    login_data = LOGINS.get_all_records()
    return login_data


def a_data() -> list:
    """
    Pull all values from appraisals work sheet and return as list
    of lists
    """
    a_data = APPRAISALS.get_all_values()
    return a_data


def a_dict() -> list:
    """
    Pull all values from appraisals work sheet and return as
    list of dictionaries
    """
    a_dict = APPRAISALS.get_all_records()
    return a_dict


def c_dict() -> list:
    """
    Pull all values from catalogue work sheet and return as
    list of dictionaries
    """
    c_dict = CATALOGUE.get_all_records()
    return c_dict


def append_car(worksheet, car: list) -> bool:
    """
    Adds vehicle list to google sheet
    @param worksheet(object): variable containing gsheet worksheet
    @param car(list): list with values from vehicle object
    """
    print('..adding vehicle to the database..')
    worksheet.append_row(car)
    return True


def delete_vehicle(reg: str):
    """
    Locates reg values in gsheet (catalogue) and removes the row
    @param reg(string): car registration as inputted by the user
    """
    cell = CATALOGUE.find(reg)
    row_number = cell.row
    CATALOGUE.delete_rows(row_number)
    print('\nVehicle was successfully deleted.......')


def search(reg: str, vehicles: list) -> list:
    """
    Function to search for vehicle reg in gsheet vehicle catalogue returns a
    dictionary
    @param reg(string): Vehicle registration as entered by user input
    @param vehciles(object): vehicle catalogue worksheet
    returns list of dictionaries for matching values
    """
    locatedcar = [x for x in vehicles if x['Reg'] == reg]
    return locatedcar


def appraisals_list() -> list:
    """
    Gets and returns a list of lists from gsheet
    """
    appraisals_list = SHEET.worksheet('appraisals')
    return appraisals_list
