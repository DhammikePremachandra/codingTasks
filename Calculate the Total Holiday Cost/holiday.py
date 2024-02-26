"""
Calculate the user's total holiday cost, which includes the 
plane cost, hotel cost, and car-rental cost.
"""

"""
Function to display the options that user could select according to 
his flying destination.
"""
def options():
    """# Displaying the options for flying city."""
    print("Welcome to the options:")
    print("A - If you will be flying East Midland to Aberdeen")
    print("E - If you will be flying East Midland to Edinburgh")
    print("L - If you will be flying East Midland to London")

def destination():
    """
    #Function to get the city that the user will be flying to.
    """
    city_flight = " "
    # Getting valid input using loop.
    while city_flight not in ["A", "E", "L"]:
        options() # Output the options.
        # Getting the flying city as a user input or "Q" to quit.
        city_flight = input("Please enter the character related to the city you will be flying to: ").upper().strip()
        # Returning the city corresponding on user input.
        if city_flight == "A":
            return "Aberdeen"
        elif city_flight == "E":
            return "Edinburgh"
        elif city_flight == "L":
            return "London"
        else:
            print("Invalid option, Please try again")

# Getting the flying destination from the user.
city_flight = destination()
# Displaying the flying city.
print(f"You will be flying to {city_flight}")

"""
Get the num_nights the user will be staying at a hotel.
"""
while True:
    try: # Error handling.
        # Getting num_nights stay at the hotel as an user input and 
        # convert it into integer.
        num_nights = int(input("Please enter number of nights you will be staying at a hotel: "))
        break # when the valid input recieved need to be break this.
    except ValueError: # Error handling.
        print("Invalid input, Please enter a valid number")

while True:
    try:# Error handling.
        # Getting rental_days for hiring a car as an user input and 
        # convert it into integer.
        rental_days = int(input("Please enter number of days you will be hiring a car:"))
        break # when the valid input recieved need to be break this.
    except ValueError:# Error handling.
        print("Invalid input, Please enter a valid number")

def hotel_cost(num_nights):
    """#Function to calculate the total cost of hotel stay."""
    return 50 * num_nights # hotel rent for a night = 50.
   
def plane_cost(city_flight):
    """#Function to calculate the cost of the plane cost."""
    if city_flight == "Aberdeen":
        return 360 # EastMidland to aberdeen plane cost = 360.
    elif city_flight == "Edinburgh":
        return 290 # EastMidland to edinburgh plane cost = 290. 
    else:
       return 100 # EastMidland to london plane cost = 100.
    
"""Function to calculate the total cost of car rental"""
def car_rental(rental_days):
    return 30 * rental_days # car rental for a day = 30.

def holiday_cost(hotel_cost, plane_cost, car_rental):
    """Function to calculate the total holiday cost."""
    # Calculating the total cost for the holiday.
    total_cost_for_holiday = hotel_cost(num_nights) + plane_cost(city_flight) 
    + car_rental(rental_days)
    # Output the total cost for the holiday.
    print(f"Total cost for your holiday in {city_flight} for {num_nights} nights and car rental for {rental_days} days: {total_cost_for_holiday}")

# Calling the function to calculate the total holiday cost .
holiday_cost(hotel_cost, plane_cost, car_rental)
