from flight import Flight
from airport import Airport
from flights_database import Flights_Database

def display_menu():
    print("1. Add a flight")
    print("2. Remove a flight")
    print("3. Display all flights")
    print("4. Exit")
    
def handle_option(option):
    if option == 1:
        flight = Flight()
        flight.get_flight()
        air = Airport()
        air.get_airport()
        flight_db.add_flight(flight, air)
    elif option == 2:
        a_code = input("Enter the aircode: ")
        f = input("Enter the flight: ")
        if flight_db.remove_flight(a_code, f):
            print("Flight was successfully removed.")
        else:
            print("Flight was not found.")
    elif option == 3:
        flight_db.display_flights()
        
EXIT_OPTION = 4

flight_db = Flights_Database()
print("Welcome to the airport")
print("--------------------------------")
display_menu()
option = int(input("Choose an option: "))
while option != EXIT_OPTION:
    handle_option(option)
    display_menu()
    option = int(input("Choose an option: "))