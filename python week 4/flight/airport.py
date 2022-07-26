class Airport:
    """This class represents an airport
    """
    def __init__(self):
        """Initializes airport
        """
    
    def get_airport(self):
        self.air_code = input("Enter the airport code: ")
        self.country = input("Enter the country: ")
        self.city = input("Enter the city: ")

    def __str__(self):
        s = ""
        s += f'Airport code: {self.air_code} \n'
        s += f'Country: {self.country} \n'
        s += f'City: {self.city}'

        return s