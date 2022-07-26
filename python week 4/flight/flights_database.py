from flight import Flight
from airport import Airport

class Flights_Database:
    """This class represents the flight database and stores all flights in the system 
    """

    def __init__(self):
        """Initializes flight database attributes
        """
        self.db = {}    #key = airport code, value = Flight object

    def add_flight(self, flight:Flight, air: Airport):
        self.db[air.air_code] += [flight]
    
    def remove_flight(self, air_code, flight):
        for air_code in self.db.items():
            if flight in air_code:
                del self.db.values[flight]
                return True
            else:
                return False

    def display_flights(self):
        for airport in self.db.items():
            print(airport)
            print("*" * 40)

