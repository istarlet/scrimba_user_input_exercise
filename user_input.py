# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input("Please enter your first name: ")
distance_km = float(input("Please enter the distance in km: "))
distance_in_miles = distance_km * 1.609

print("Hi " + name.capitalize() + "," + " you walked " + str(distance_in_miles) + " miles.")