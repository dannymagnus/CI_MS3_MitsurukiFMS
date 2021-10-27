from sheet1 import a_dict

valid_models = ['Slicker', 'Trojan', 'Slider', 'Etronic']


class Car:
    """
    To create instance of car class
    @param registration(string): Registration as entered by the user
    @param color(string): Color of the car as entered by user input
    """
    def __init__(self, registration, color):
        self.registration = registration
        self.color = color

    def get_appraisal(self):
        """
        Pulls all appraisals from gsheet which match intance created
        """
        all_dict_items = [item for item in a_dict() if item['Reg'] ==
                          self.registration]
        dates = [item['Date'] for item in all_dict_items]
        appraisals = [item['Appraisal Details'] for item in all_dict_items]
        return dates, appraisals

    def describe(self):
        """
        Prints description of car instance
        """
        print(f"This car has the registration {self.registration} ")
        print(f"and is {self.color} in color")


class ETronic(Car):
    """
    Creates an instance of 'Etronic' vehicle object
    @param registration(string): Registration as entered by user input
    @param color(color): Color of car instance as entered by user input
    @param heated(string): Y or N value as entered by user input
    """
    def __init__(self, registration, color, heated):
        super().__init__(registration, color)
        self.model = "Etronic"
        self.powertrain = "Battery"
        self.massage = "No"
        self.heated = heated
        self.type = "Estate"

    """Prints description of car instance"""
    def description(self):
        print(f"{self.registration} is the {self.model} model and ")
        print(f"is a {self.type} vehicle with a {self.powertrain} powertrain.")
        print(f"Heated seats: {self.heated}")
        print(f"Massage seats: {self.massage}")


class Trojan(Car):
    """
    Creates an instance of 'Trojan' vehicle object
    @param registration(string): Registration as entered by user input
    @param color(color): Color of car instance as entered by user input
    @param heated(string): Y or N value as entered by user input
    @param massage(string): Y or N value as entered by user input
    """
    def __init__(self, registration, color, heated, massage):
        super().__init__(registration, color)
        self.model = "Trojan"
        self.powertrain = "Combustion"
        self.massage = massage
        self.heated = heated
        self.type = "Pickup"

    """Prints description of car instance"""
    def description(self):
        print(f"{self.registration} is the {self.model} model and ")
        print(f"is a {self.type} vehicle with a {self.powertrain} powertrain.")
        print(f"Heated seats: {self.heated}")
        print(f"Massage seats: {self.massage}")
        print(f"Color: {self.color}")


class Slicker(Car):
    """
    Creates an instance of 'Slicker' vehicle object
    @param registration(string): Registration as entered by user input
    @param color(color): Color of car instance as entered by user input
    @param heated(string): Y or N value as entered by user input
    @param massage(string): Y or N value as entered by user input
    """
    def __init__(self, registration: str, color, heated, massage):
        """
        """
        super().__init__(registration, color)
        self.model = "Slicker"
        self.powertrain = "Hybrid"
        self.massage = massage
        self.heated = heated
        self.type = "SUV"

    def description(self):
        """Prints description of car instance"""
        print(f"{self.registration} is the {self.model} model and ")
        print(f"is a {self.type} vehicle with a {self.powertrain} powertrain.")
        print(f"Heated seats: {self.heated}")
        print(f"Massage seats: {self.massage}")
        print(f"Color: {self.color}")


class Slider(Car):
    """
    Creates an instance of 'Slider' vehicle object
    @param registration(string): Registration as entered by user input
    @param color(color): Color of car instance as entered by user input
    @param heated(string): Y or N value as entered by user input
    @param massage(string): Y or N value as entered by user input
    """
    def __init__(self, registration, color, heated, massage):
        super().__init__(registration, color)
        self.model = "Slicker"
        self.powertrain = "Combustion"
        self.massage = massage
        self.heated = heated
        self.type = "Saloon"

    """Prints description of car instance"""
    def description(self):
        print(f"{self.registration} is the {self.model} model and ")
        print(f"is a {self.type} vehicle with a {self.powertrain} powertrain.")
        print(f"Heated seats: {self.heated}")
        print(f"Massage seats: {self.massage}")
        print(f"Color: {self.color}")


def catalogue_deconstruct(car: list) -> object:
    """
    Function to take gspread data and conditionallly create vehicle instance,
    used with search_car_reg()
    @param car(object): list taken from gsheet and returns class instance
    """
    car = car[0]
    if car['Model'] == 'Trojan':
        thiscar = Trojan(
            car['Reg'], car['Color'], car['Heated'], car['Massage'])
        return thiscar
    elif car['Model'] == 'Slicker':
        thiscar = Slicker(
            car['Reg'], car['Color'], car['Heated'], car['Massage'])
        return thiscar
    elif car['Model'] == 'Slider':
        thiscar = Slicker(
            car['Reg'], car['Color'], car['Heated'], car['Massage'])
        return thiscar
    else:
        thiscar = ETronic(car['Reg'], car['Color'], car['Heated'])
        return thiscar


def create_vehicle_list(obj: object) -> list:
    """
    Function to convert car instance list
    @param obj(object): class instance object vehicle
    """
    print('\n..preparing to add vehicle to database...')
    car = [
        obj.registration, obj.model,
        obj.powertrain, obj.color, obj.heated,
        obj.massage]
    return car
