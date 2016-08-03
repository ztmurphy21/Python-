#declarations of variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars-drivers #calc
cars_driven = drivers #calc
carpool_capacity = cars_driven * space_in_a_car #calc
average_passengers_per_car = passengers / cars_driven #calc

#output
print ("There are ", cars, " cars available.")
print ("There are only ", drivers, " drivers available.")
print ("There will be ", cars_not_driven, " empty cars today.")
print ("We can transport ", carpool_capacity, " people today.")
print ("We have ", passengers, " to carpool today.")
print ("We need to put about ", average_passengers_per_car, " in each car.")