cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "there are", cars, "cars available."
print "there are only", drivers, "drivers available."
print "there will be", cars_not_driven, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."

# første print blir regna ut enkelt ved hva variable er car = 100, samme for drivers = 30, cars_not_driven blir regna ut ved cars 100 - driver 30 = 70, carpool_capacity blir regnet ut ved cars_driven 30 * space_in_a_car 4.0 = 120, passengers blir regnet ut ved hva  som står 90, og average blir regnet ut ved passengers 90 / cars_driven 30 = 3.
