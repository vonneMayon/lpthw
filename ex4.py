cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_compacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven
#assigning/defining variables

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_compacity, "people today.")
print ("We have", passengers, "to carpool today.")
print("We need to put about",average_passengers_per_car, "in each car.")
#printing strings and utilizing the variables that were assigned to be used w/in string
