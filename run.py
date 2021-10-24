import datetime

from sheet1 import c_dict
from sheet1 import append_car
from sheet1 import catalogue
from sheet1 import delete_vehicle
from sheet1 import search
from sheet1 import appraisals_list

from vehicles import Car
from vehicles import ETronic
from vehicles import Slider
from vehicles import Trojan
from vehicles import Slicker
from vehicles import valid_models
from vehicles import catalogue_deconstruct
from vehicles import create_vehicle_list

divider = '-' * 20
vehicle_return = "\nPress <enter> to return the vehicle menu..."


def main_menu():
    """
    Function to get user input on what they want to do with the system
    """
    choices = 2
    print(('\n\nWelcome to the test vehicle appraisal system\n').upper())
    while True:
        print(divider)
        print(('Main menu').upper())
        print(divider)
        print('\n1:Search vehicle catalogue')
        print('\n2:Appraisals\n')
        selection = input("\nWhat would you like to do?: ")
        if validateselection(selection, choices):
            print('Accepted')
            selected = int(selection)
            if selected == 1:
                vehicle_menu()
            else:
                appraisals_menu()
            break


def validateselection(selection: int, choices: int) -> bool:
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
        print(f"Invalid selection: {e}")
        input('Press <enter> to continue')
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
        print(divider)
        print(('Vehicle Menu').upper())
        print(divider)
        print('\nYou can search vehciles in the current engineering fleet.')
        print('You can also add and remove vehicles.')
        print('\n1: Search for a vehicle')
        print('\n2: Add a vehicle')
        print('\n3: Remove a vehicle')
        print('\n4: Return to main menu')
        vm_selection = input('\nWhat would you like to do?:  ')
        if vm_selection not in ['1', '2', '3', '4']:
            print('\nPlease select a valid option (1), (2), (3) or (4)')
        else:
            print('\nLoading your choice')
        if vm_selection == '1':
            while True:
                reg_input = input(
                    '\nEnter the vehicle registration or <enter> to exit: '
                    )
                reg = reg_input.upper()
                if vehicle_validation(reg, c_dict()):
                    search_car_reg(reg)
                elif reg == '':
                    print('\nReturning to vehicle menu....)')
                    vehicle_menu()
                else:
                    print('\nPlease check the registration and try again...')
        elif vm_selection == '2':
            create_vehicle()
        elif vm_selection == '3':
            while True:
                print('\nTo return to the vehicle menu press enter...')
                reg_input = input('\nPlease input the vehicle registration: ')
                reg = reg_input.upper()
                if reg == "":
                    vehicle_menu()
                elif vehicle_validation(reg, c_dict()):
                    print(f'\nThis will delete vehicle {reg}')
                    print('\nThe following action cannot be reversed')
                    delete_input = input('\nDo you wish to proceed?: ')
                    proceed = delete_input[0].upper()
                    if proceed == 'Y':
                        delete_vehicle(reg)
                        input(vehicle_return)
                        vehicle_menu()
                        break
                    else:
                        print('\nVehicle not deleted...')
                        input('\nPress <enter> to return to vehicle menu')
        elif vm_selection == '4':
            main_menu()
        else:
            input('\nPress <enter> to try again...')


def vehicle_validation(reg, vehicles):
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
        print(f"Invalid selection: {e}")
        return False
    return True


def search_car_reg(reg):
    """
    Function to search car in gsheet vehicle catalogue, uses deconstruct
    function to create vehicle instance and print description
    @param reg(string): Vehicle registration as entered by user input
    """
    locatedcar = [x for x in c_dict() if x['Reg'] == reg]
    print("\nThe car has been located........")
    while True:
        option = input("\nWould you like to view vehicle specification?: ")
        choice = option[0].upper()
        if choice == "Y":
            car_details = catalogue_deconstruct(locatedcar)
            print('\n')
            print(divider)
            print(car_details.description())
            print(divider)
            input(
                '\nPress <enter> to return to the vehicle menu....'
                )
            vehicle_menu()
            break
        elif choice == 'N':
            print('\nReturning to the vehicle menu...')
            vehicle_menu()
            break
        else:
            print('\nPlease enter a valid choice')


def validate_create(reg, model, color, heated):
    """
    Validates the input from the user that the vehicle is of valid type(s)
    @param reg(string): Vehicle registration as entered by user input
    @param model(string): Vehicle model as entered by user input
    @param color(string): Vehicle color as entered by user input
    @param heated(string): Vehicle heated (y/n) as entered by user input
    """
    try:
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
        print(f"Invalid selection: {e}.  Please try again..")
        return False
    return True


def create_vehicle():
    """
    To create a vehicle from user input and append call to
    append it to the gsheet (database)
    Returns user to previous menu once complete
    """
    while True:
        reg = input('\nEnter vehicle registration: ').upper()
        model = input('Model: ').capitalize()
        color = input('Color: ').capitalize()
        heated = input('Are heated seats fitted?(y/n): ').capitalize()
        massage = ""
        if validate_create(reg, model, color, heated):
            model = model.capitalize()
            if model == 'Trojan' or model == 'Slicker' or model == 'Slider':
                while True:
                    massage = (
                        input('Are massage seats fitted? (y/n): ').upper()
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
            print("The data inputted is invalid")
    print('\nYou have inputted the following details...')
    print(vehicle.description())
    choice = input('Would you like to add this to the fleet database?:  ')
    if choice.capitalize()[0] == 'Y':
        car_list = create_vehicle_list(vehicle)
        if append_car(catalogue, car_list):
            print('\nVehicle successfully added...')
            print('\nReturning to the vehicle menu...')
            input('Press <enter> to continue...')
            vehicle_menu()
        else:
            print("Sorry an error has occurred")
            print("Please try again later")
            input('Press <enter> to continue...')
            vehicle_menu()
    else:
        print('\nYour choice was to not add to the vehicle database')
        print('\nReturning to the vehicle menu.....')
        input('Press <enter> to continue....')
        vehicle_menu()


def appraisals_menu():
    """
    Appraisals sub menu, options to create or view appraisals
    """
    am_selection = ''
    while am_selection not in ['1', '2', '3']:
        print('\n')
        print(divider)
        print(('Appraisals menu').upper())
        print(divider)
        print('\nHere you can search for or add appraisals')
        print('\n1: Add vehicle appraisal')
        print('\n2: Search vehicle appraisal')
        print('\n3: Return to the main menu')
        am_selection = input('\nWhat do you want to do?: ')
        if am_selection not in ['1', '2', '3', '4']:
            print('\nPlease select a valid option (1), (2), (3) or (4)')
            input('Press enter to continue')
        else:
            print('\nLoading your choice')
        if am_selection == '1':
            while True:
                reg = input('\nPlease enter the vehicle registration: ')
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
                            '\nWould you like to add this to the database?: '
                            )
                        if add_appraisal_input == 'n':
                            print('\nReturning to appraisals menu....')
                            appraisals_menu()
                        elif add_appraisal_input == 'y':
                            append_car(appraisals_list(), car_list_values)
                            print('\nAdded to appraisals database')
                            print('\nReturning to appraisals menu,')
                            input('\nPress enter to continue....')
                            appraisals_menu()
                        else:
                            print('That is not a valid selection.')
                            print('Please enter y or n only')
                elif input('\n"Would you like to try again (y/n)?') == 'n':
                    print('\nReturning to appraisals menu....)')
                    appraisals_menu()
                else:
                    print('\nPlease try again...')
        elif am_selection == '2':
            while True:
                reg = input('\nPlease enter vehicle registration: ')
                if vehicle_validation(reg, c_dict()):
                    print('\n Your vehicle has been located...\n')
                    car = search(reg, c_dict())[0]
                    print(f"Vehicle: {car['Reg']}")
                    print(f"Model: {car['Model']}")
                    car_list_values = list(car.values())
                    car_instance = Car(car_list_values[0], car_list_values[3])
                    dates, appraisals = car_instance.get_appraisal()
                    print('\nPress enter to print all appraisals')
                    input('for this vehicle...')
                    for d, a in zip(dates, appraisals):
                        print(f"\nDate: {d}")
                        print(f"\nDetails: {a}\n")
                        print(divider)
                    print('\nReport complete.')
                    input('\nPress enter to return to appraisals menu...')
                    appraisals_menu()
        else:
            main_menu()


def create_appraisal_details():
    """
    Function to create an appraisal, takes user input, parses data and returns
    2 variables, date(string) and appraisal(string)
    """
    while True:
        date = input('\nWhat is the date of appraisal? (dd/mm/yy): ')
        day, month, year = date.split('/')
        appraisal = input('\nPlease enter the vehicle appraisal: ')
        if validate_app_input(day, month, year):
            return date, appraisal
        elif input('\n"Would you like to try again (y/n)?') == 'n':
            print('\nReturning to appraisals menu....)')
            appraisals_menu()
        else:
            print('\nPlease try again...')


def validate_app_input(day, month, year):
    """
    Data validation for date format input
    @param day(string): parsed date from user input
    @param month(string): parsed month from user input
    @param year(string): parsed year from user input
    """
    try:
        if not datetime.datetime(int(year), int(month), int(day)):
            raise ValueError("Please enter a valid date format")
    except ValueError as e:
        print(f'Entry invalid: {e}')
        return False
    return True


main_menu()
