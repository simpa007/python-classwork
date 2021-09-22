#Importing classes
#Importing a single class
"""A class that can be used to represent a car"""
class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
	def get_descriptive_name(self):
		long_name=f"{self.year} {self.model} {self.make}"
		return long_name.title()
	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it")
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles

#storing mutiple classes in a module
class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
	def get_describtive_name(self):
		long_name=f"{self.year} {self.model} {self.make}"
		return long_name.title()
class Battery:
	def __init__(self,battery_size=75):
		self.battery_size=battery_size
	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kwh battery")
	def range(self):
		if self.battery_size ==75:
			range =260
		elif self.battery_size ==100:
			range =315
		print(f"This car can go about {range} miles on a full charge")
class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery_size=Battery()
class Dice:
	def __init__(self,slides=6):
		self.slides=slides
	def roll_dice(self):
		for random import randint(1,6):





