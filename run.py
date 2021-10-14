from pprint import pprint
from sheet1 import a_data

from vehicles import Car
from vehicles import ETronic


def main_menu():
    """
    Function to get user input on what they want to do with the system
    """
    choices = 2
    print('Welcome to the test vehicle appraisal system')
    data = a_data()
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


main_menu()
