from sheet1 import a_dict


class Car:
    """
    To create instance of car class
    """
    def __init__(self, registration, color):
        self.registration = registration
        self.color = color

    def get_appraisal(self):
        all_dict_items = [item for item in a_dict() if item['Reg']
                          == self.registration]
        dates = [item['Date'] for item in all_dict_items]
        appraisals = [item['Appraisal Details'] for item in all_dict_items]
        return dates, appraisals

    def describe(self):
        print(f"This car has the registration {self.registration} ")
        print(f"and is {self.color} in color")


class ETronic(Car):
    """Creates an instance of 'Etronic' vehicle object"""
    def __init__(self, registration, color, heated):
        super().__init__(registration, color)
        self.model = "Etronic"
        self.powertrain = "Battery"
        self.massage = "No"
        self.heated = heated
        self.type = "Estate"

    def description(self):
        print(f"{self.registration} is the {self.model} model and ")
        print(f"is a {self.type} vehicle with a {self.powertrain} powertrain.")
        print(f"Heated seats: {self.heated}")
        print(f"Massage seats: {self.massage}")


class Trojan(Car):
    """Creates an instance of 'Trojan' vehicle object"""
    def __init__(self, registration, color, heated, massage):
        super().__init__(registration, color)
        self.model = "Trojan"
        self.powertrain = "Combustion"
        self.massage = massage
        self.heated = heated
        self.type = "Pickup"

    def description(self):
        print(f"{self.registration} is the {self.model} model and ")
        print(f"is a {self.type} vehicle with a {self.powertrain} powertrain.")
        print(f"Heated seats: {self.heated}")
        print(f"Massage seats: {self.massage}")
        print(f"Color: {self.color}")
