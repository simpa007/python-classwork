from car import Car
my_new_car=Car('audi','model s',2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=21
my_new_car.read_odometer()
my_new_car.update_odometer(30)
my_new_car.read_odometer()
my_new_car.increment_odometer(10)
my_new_car.read_odometer()
