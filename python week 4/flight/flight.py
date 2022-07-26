class Flight:
    """This class represents a flight and its information 
    """
    def __init__(self):
        """Initializes flight
        """

    def get_flight(self):
        self.f_number = input("Enter the flight number: ")
        self.d_time = input("Enter the departure time: ")
        self.d_airport = input("Enter the departure airport: ")
        self.a_time = input("Enter the arrival time: ")
        self.a_airport = input("Enter the arrival airport: ")

    def __str__(self):
        s = ""
        s += f'Flight Number: {self.f_number} \n'
        s += f'Departure Time: {self.d_time} \n'
        s += f'Departure Airport: {self.d_airport} \n'
        s += f'Arrival Time: {self.a_time} \n'
        s += f'Arrival Airport: {self.a_airport}'

        return s 