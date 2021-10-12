import sheet
import pprint


def main_menu():
    """
    Function to get user input on what they want to do with the system
    """
    choices = 2
    print('/nWelcome to the Mitsuruki Fleet Management System/n').upper()
    print('The purpose of this system is to be able to select')
    print('and view vehicles to appraise.')
    a_data = a_data()
    pprint(c_dict)
    while True:
        print('')
        selection = input("What would you like to do?\n\n1:Search vehicle catalogue\n2:Appraisals\n\n")
        if validateselection(selection, choices):
            print('Accepted')
            selected = int(selection)
            if selected == 1:
                catalogue_menu()
            else:
                appraisals_menu()
            break


main_menu()
