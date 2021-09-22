from car import ElectricCar
telsa=ElectricCar('telsa','model s',2019)
print(telsa.get_describtive_name())
telsa.battery_size.describe_battery()
telsa.battery_size.range()

#Importing multiple classes from a module
from car import Car,ElectricCar
my_car =Car('mecedes benz','S series',2013)
print(my_car.get_describtive_name())

my_telsa = ElectricCar('telsa','v24',2020)
print(my_telsa.get_describtive_name())
my_telsa.battery_size.describe_battery()
#Importing an Entire module
import car
my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_describtive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_describtive_name())