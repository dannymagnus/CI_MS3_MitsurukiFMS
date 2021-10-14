from pprint import pprint
from sheet1 import a_data
from sheet1 import c_dict

from vehicles import Car
from vehicles import ETronic


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
                pass
            else:
                pass
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
                    'Please enter the vehicle registration or <enter> to exit: ')
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
                elif vehicle_validation(reg, c_dict):
                    cell = catalogue.find(reg)
                    row_number = cell.row
                    catalogue.delete_rows(row_number)
                    print('\nVehicle was successfully deleted.......')
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
        print(f"Invalid selection: {e} ")
        return False
    return True


main_menu()
