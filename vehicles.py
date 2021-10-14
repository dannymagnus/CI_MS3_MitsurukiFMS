class Car:
    """
    To create instance of car class
    """
    def __init__(self, registration, color):
        self.registration = registration
        self.color = color

    def get_appraisal(self):
        all_dict_items = [item for item in a_dict if item['Reg'] 
                          == self.registration]
        dates = [item['Date'] for item in all_dict_items]
        appraisals = [item['Appraisal Details'] for item in all_dict_items]
        return dates, appraisals

    def describe(self):
        print(f"This car has the registration {self.registration} and\
              is {self.color} in color")