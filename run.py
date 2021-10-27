from datetime import datetime

from sheet1 import c_dict
from sheet1 import append_car
from sheet1 import catalogue
from sheet1 import delete_vehicle
from sheet1 import search
from sheet1 import appraisals_list
from sheet1 import get_logins

from vehicles import Car
from vehicles import ETronic
from vehicles import Slider
from vehicles import Trojan
from vehicles import Slicker
from vehicles import valid_models
from vehicles import catalogue_deconstruct
from vehicles import create_vehicle_list

DIVIDER = '-' * 30
VEHICLE_RETURN = "\nPress <enter> to return the vehicle menu...\n"


def login():
    """
    Function to take user input (uid and password) and compare
    to gsheet data record
    """
    print(DIVIDER)
    print(('Mitsuruki Automotive Systems').upper())
    print(('Fleet management user login').upper())
    print(DIVIDER)
    uid = input('\nEnter username: \n')
    pwd = input('\nPassword: \n')
    logins = get_logins()
    if not [x for x in logins if x['username'] == uid]:
        print('\nNo such user found')
        print('\nPlease check and try again.')
        login()
    else:
        matched_uid = [x for x in logins if x['username'] == uid][0]
    if pwd == matched_uid['password']:
        print('\nLogin successful')
        main_menu()
    else:
        print('\nLogin failed')
        print('\n Password did not match.')
        print('\n Please try again.')
        login()


def main_menu():
    """
    Function to get user input on what they want to do with the system
    """
    choices = 3
    print(('\n\nWelcome to the test vehicle appraisal system\n').upper())
    while True:
        print(DIVIDER)
        print(('Main menu').upper())
        print(DIVIDER)
        print('\n1: Search vehicle catalogue')
        print('\n2: Appraisals')
        print('\n3: Logout\n')
        selection = input("\nWhat would you like to do?: \n")
        if validate_selection(selection, choices):
            print('Accepted')
            selected = int(selection)
            if selected == 1:
                vehicle_menu()
                break
            elif selected == 2:
                appraisals_menu()
                break
            else:
                login()
            break


def validate_selection(selection: int, choices: int) -> bool:
    """
    Tries values to see if they are numbers and within the value range
    @param selection(int): Selected menu option from user input on what
    they want to do with the system
    @param choices(int): Number of menu items that exist in range
    """
    try:
        if not selection.isdigit():
            raise ValueError(
                "Please use a number value"
            )
        if int(selection) > choices or int(selection) <= 0:
            raise ValueError(
                "Please use a number within range"
                )
    except ValueError as e:
        print(f"\nInvalid selection: {e}")
        input('Press <enter> to continue\n')
        return False
    return True


def vehicle_menu():
    """
    Vehicle sub menu, gives options for search, add and remove vehicles
    and calls relevent functions to execute request
    """
    vm_selection = ''
    while vm_selection not in ['1', '2', '3', '4']:
        print('\n')
        print(DIVIDER)
        print(('Vehicle Menu').upper())
        print(DIVIDER)
        print('\nYou can search vehciles in the current engineering fleet.')
        print('You can also add and remove vehicles.')
        print('\n1: Search for a vehicle')
        print('\n2: Add a vehicle')
        print('\n3: Remove a vehicle')
        print('\n4: Return to main menu')
        vm_selection = input('\nWhat would you like to do?:  \n')
        if vm_selection not in ['1', '2', '3', '4']:
            print('\nPlease select a valid option (1), (2), (3) or (4)')
        else:
            print('\nLoading your choice')
        if vm_selection == '1':
            while True:
                reg_input = input(
                    '\nEnter the vehicle registration or <enter> to exit: \n\n'
                    )
                reg = reg_input.upper()
                if reg == '':
                    print('\nReturning to vehicle menu....')
                    vehicle_menu()
                elif vehicle_validation(reg, c_dict()):
                    search_car_reg(reg)
                else:
                    print('\nPlease check the registration and try again...')
        elif vm_selection == '2':
            create_vehicle()
        elif vm_selection == '3':
            while True:
                print('\nTo return to the vehicle menu press enter...')
                reg_input = input(
                    '\nPlease input the vehicle registration: \n'
                        )
                reg = reg_input.upper()
                if reg == "":
                    vehicle_menu()
                elif vehicle_validation(reg, c_dict()):
                    print(f'\nThis will delete vehicle {reg}')
                    print('\nThe following action cannot be reversed')
                    delete_input = input('\nDo you wish to proceed?: \n')
                    proceed = delete_input[0].upper()
                    if proceed == 'Y':
                        delete_vehicle(reg)
                        input(VEHICLE_RETURN)
                        vehicle_menu()
                        break
                    else:
                        print('\nVehicle not deleted...')
                        input('\nPress <enter> to return to vehicle menu\n')
                        vehicle_menu()
                        break
        elif vm_selection == '4':
            main_menu()
        else:
            input('\nPress <enter> to try again...\n')


def vehicle_validation(reg: str, vehicles: object) -> bool:
    """
    Data validation function to check vehicle exists in the database
    and that the character length is valid
    @param reg(string): Vehicle registration as entered by user input
    @param vehicles(object): List of vehicles derived from gsheet
    """
    try:
        if len(reg) != 7:
            raise ValueError("Too many / too few characters")
        if not [element for element in vehicles if element['Reg'] == reg]:
            raise ValueError("No such vehicle in fleet management database")
    except ValueError as e:
        print(f"\nInvalid selection: {e}")
        return False
    return True


def search_car_reg(reg: str):
    """
    Function to search car in gsheet vehicle catalogue, uses deconstruct
    function to create vehicle instance and print description
    @param reg(string): Vehicle registration as entered by user input
    """
    locatedcar = [x for x in c_dict() if x['Reg'] == reg]
    print("\nThe car has been located........")
    while True:
        while True:
            option = input(
                "\nWould you like to view vehicle specification?: \n"
                    )
            if option == '':
                print('\nPlease enter y or n only')
            else:
                choice = option[0].upper()
                break
        if choice == "Y":
            car_details = catalogue_deconstruct(locatedcar)
            print('\n')
            print(DIVIDER)
            car_details.description()
            print(DIVIDER)
            input(
                '\nPress <enter> to return to the vehicle menu....\n'
                )
            vehicle_menu()
            break
        elif choice == 'N':
            print('\nReturning to the vehicle menu...')
            vehicle_menu()
            break
        else:
            print('\nPlease enter y or n only')


def validate_create(reg: str, model: str, color: str, heated: str) -> bool:
    """
    Validates the input from the user that the vehicle is of valid type(s)
    @param reg(string): Vehicle registration as entered by user input
    @param model(string): Vehicle model as entered by user input
    @param color(string): Vehicle color as entered by user input
    @param heated(string): Vehicle heated (y/n) as entered by user input
    """
    try:
        if [element for element in c_dict() if element['Reg'] == reg]:
            raise ValueError("Vehicle registration already exists.")
        if not len(reg) == 7:
            raise ValueError(
                "Registration character length should be 7")
        if model.capitalize() not in valid_models:
            raise ValueError(f"No such model exists. Your model was {model}")
        if color.capitalize().isdigit() is True:
            raise ValueError("Color should be letters only")
        if heated.upper() not in ['Y', 'N']:
            raise ValueError("Please enter the letters Y or N only")
    except ValueError as e:
        print(f"\nInvalid selection: {e}.")
        return False
    return True


def create_vehicle():
    """
    To create a vehicle from user input and append call to
    append it to the gsheet (database)
    Returns user to previous menu once complete
    """
    while True:
        reg = input(
            '\nEnter vehicle registration or <enter> to exit: \n'
            ).upper()
        if reg == '':
            vehicle_menu()
            break
        model = input('\nModel: \n').capitalize()
        color = input('\nColor: \n').capitalize()
        heated = input('\nAre heated seats fitted?(y/n): \n').capitalize()
        massage = ""
        if validate_create(reg, model, color, heated):
            model = model.capitalize()
            if model == 'Trojan' or model == 'Slicker' or model == 'Slider':
                while True:
                    massage = (
                        input('\nAre massage seats fitted? (y/n): \n').upper()
                        )
                    if massage in ['Y', 'N']:
                        break
                    else:
                        print("\nEnter Y or N only")
            if model == 'Slider':
                vehicle = Slider(reg, color, heated, massage)
            elif model == 'Trojan':
                vehicle = Trojan(reg, color, heated, massage)
            elif model == 'Slicker':
                vehicle = Slicker(reg, color, heated, massage)
            else:
                vehicle = ETronic(reg, color, heated)
            break
        else:
            print("\nPlease try again...")
    print('\nYou have inputted the following details...')
    (vehicle.description())
    while True:
        choice = input(
            '\nWould you like to add this to the fleet database?:  \n'
            )
        if choice == '':
            print('\nPlease enter and valid choice (y) or (n)')
        elif choice.capitalize()[0] not in ['Y', 'N']:
            print('\nPlease enter and valid choice (y) or (n)')
        elif choice.capitalize()[0] == 'Y':
            car_list = create_vehicle_list(vehicle)
            if append_car(catalogue, car_list):
                print('\nVehicle successfully added...')
                print('\nReturning to the vehicle menu...')
                input('\nPress <enter> to continue...\n')
                vehicle_menu()
                break
            else:
                print("\nSorry an error has occurred")
                print("\nPlease try again later")
                input('\nPress <enter> to continue...\n')
                vehicle_menu()
                break
        else:
            print('\nYour choice was to not add to the vehicle database')
            print('\nReturning to the vehicle menu.....')
            input('\nPress <enter> to continue....\n')
            vehicle_menu()
            break


def appraisals_menu():
    """
    Appraisals sub menu, options to create or view appraisals
    """
    am_selection = ''
    while am_selection not in ['1', '2', '3']:
        print('\n')
        print(DIVIDER)
        print(('Appraisals menu').upper())
        print(DIVIDER)
        print('\nHere you can search for or add appraisals')
        print('\n1: Add vehicle appraisal')
        print('\n2: Search vehicle appraisal')
        print('\n3: Return to the main menu')
        am_selection = input('\nWhat do you want to do?: \n')
        if am_selection not in ['1', '2', '3', '4']:
            print('\nPlease select a valid option (1), (2), (3) or (4)')
            input('\nPress <enter> to continue\n')
        else:
            print('\nLoading your choice\n')
        if am_selection == '1':
            while True:
                reg_input = input(
                    '\nPlease enter the vehicle registration: \n'
                        )
                reg = reg_input.upper()
                if vehicle_validation(reg, c_dict()):
                    print('\n Your vehicle has been located...\n')
                    car = search(reg, c_dict())[0]
                    print(f"Vehicle: {car['Reg']}")
                    print(f"Model: {car['Model']}")
                    car_list_values = list(car.values())
                    date, appraisal = create_appraisal_details()
                    car_list_values.append(date)
                    car_list_values.append(appraisal)
                    add_appraisal_input = ""
                    while add_appraisal_input not in ['y', 'n']:
                        add_appraisal_input = input(
                            '\nWould you like to add this to the database?: \n'
                            )
                        if add_appraisal_input == 'n':
                            print('\nReturning to appraisals menu....')
                            appraisals_menu()
                        elif add_appraisal_input == 'y':
                            append_car(appraisals_list(), car_list_values)
                            print('\nAdded to appraisals database')
                            print('\nReturning to appraisals menu,')
                            input('\nPress <enter> to continue....\n')
                            appraisals_menu()
                        else:
                            print('\nThat is not a valid selection.')
                            print('\nPlease enter y or n only')
                elif input('\n"Would you like to try again (y/n)?\n') == 'n':
                    print('\nReturning to appraisals menu....)')
                    appraisals_menu()
                else:
                    print('\nPlease try again...')
        elif am_selection == '2':
            while True:
                reg = input('\nPlease enter vehicle registration: \n')
                if vehicle_validation(reg, c_dict()):
                    print('\n Your vehicle has been located...\n')
                    car = search(reg, c_dict())[0]
                    print(f"Vehicle: {car['Reg']}")
                    print(f"Model: {car['Model']}")
                    car_list_values = list(car.values())
                    car_instance = Car(car_list_values[0], car_list_values[3])
                    dates, appraisals = car_instance.get_appraisal()
                    print('\nPress enter to print all appraisals')
                    input('for this vehicle...\n')
                    for d, a in zip(dates, appraisals):
                        print(f"\nDate: {d}")
                        print(f"\nDetails: {a}\n")
                        print(DIVIDER)
                    print('\nReport complete.')
                    input('\nPress enter to return to appraisals menu...\n')
                    appraisals_menu()
        else:
            main_menu()


def create_appraisal_details():
    """
    Function to create an appraisal, takes user input, parses data and returns
    2 variables, date(string) and appraisal(string)
    """
    while True:
        date = input('\nWhat is the date of appraisal? (dd/mm/yy): \n')
        if validate_date_type(date):
            appraisal = input('\nPlease enter the vehicle appraisal: \n')
            return date, appraisal
        elif input('\nWould you like to try again (y/n)?: \n') == 'n':
            print('\nReturning to appraisals menu....)')
            appraisals_menu()
        else:
            print('\nPlease try again...')


def validate_date_type(date_input: str) -> bool:
    """
    Validates if date can be split by '/'
    @param date(str): date entered by user
    """
    date_today_grab = datetime.today().strftime('%d/%m/%y')
    date_today = datetime.strptime(date_today_grab, '%d/%m/%y')
    try:
        datetime.strptime(date_input, '%d/%m/%y')
    except ValueError:
        print('\nInvalid date or format')
        return False
    try:
        if datetime.strptime(date_input, '%d/%m/%y') > date_today:
            raise ValueError('\nDate cannot be in the future')
    except ValueError as e:
        print(f'\nError: {e}')
        return False
    return True


login()
