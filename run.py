import datetime

from pprint import pprint
from sheet1 import a_data
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


def main_menu():
    """
    Function to get user input on what they want to do with the system
    """
    choices = 2
    print('Welcome to the test vehicle appraisal system')
    while True:
        selection = input("What would you like to do?\n\n1:Search vehicle \
        catalogue\n2:Appraisals\n\n")
        if validateselection(selection, choices):
            print('Accepted')
            selected = int(selection)
            if selected == 1:
                vehicle_menu()
            else:
                appraisals_menu()
            break


def validateselection(selection, choices):
    """
    Tries values to see if they are numbers and within the value range
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
        return False
    return True


def vehicle_menu():
    """Vehicle sub menu, gives options for search, add and remove vehicles"""
    vm_selection = ''
    while vm_selection not in ['1', '2', '3', '4']:
        print('\nVehicle Menu')
        print('Welcome to the vehicle menu\n')
        print('Here you can search vehciles in the current engineering fleet')
        print('You can also add and remove vehicles')
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
                reg = input(
                    'Enter the vehicle registration or <enter> to exit: '
                    )
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
                reg = input('\nPlease input the vehicle registration: ')
                if reg == "":
                    vehicle_menu()
                elif vehicle_validation(reg, c_dict()):
                    delete_vehicle(reg)
        else:
            main_menu()


def vehicle_validation(reg, vehicles):
    """
    Data validation function to check vehicle exists in the database
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
    """
    locatedcar = [x for x in c_dict() if x['Reg'] == reg]
    print("\nThe car has been located........")
    while True:
        option = input("\nWould you like to view vehicle specification?:")
        choice = option.upper()
        if choice in ["YES", "Y"]:
            car_details = catalogue_deconstruct(locatedcar)
            print(car_details.description())
            input('\n Press <enter> to the vehicle menu....')
            vehicle_menu()
            break
        elif choice in ['N', 'No']:
            print('\nReturning to the vehicle menu...')
            vehicle_menu()
            break
        else:
            print('\nPlease enter a valid choice')


def validate_create(reg, model, color, heated):
    try:
        if not len(reg) == 7:
            raise ValueError(
                "Registration character length should be 7")
        if model.isdigit() is True:
            raise ValueError("Model should contain letters only.")
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
    To create a vehicle from user input and append
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
    """Appraisals sub menu, options to create or view appraisals"""
    am_selection = ''
    while am_selection not in ['1', '2', '3']:
        print('\n\nAppraisals menu')
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
                reg = input('Please enter the vehicle registration: ')
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


def create_appraisal_details():
    """Function to create an appraisal"""
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
    """Data validation for date format input"""
    try:
        if not datetime.datetime(int(year), int(month), int(day)):
            raise ValueError("Please enter a valid date format")
    except ValueError as e:
        print(f'Entry invalid: {e}')
        return False
    return True


main_menu()
