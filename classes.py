class Dog:
	"""A simple attempt to model a dog"""
	def __init__(self,name,age):
		"""initialize name and age attributes"""
		self.name=name
		self.age=age
	def sit(self):
		"""stimulate a dog sitting in respect to the command"""
		print(f"{self.name} is now sitting")
	def roll_over(self):
		"""stimulate roll over in respond to the command"""
		print(f"{self.name} rolled over!")
my_dog= Dog('bigo',12)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

#calling methods
my_dog.sit()
my_dog.roll_over()

#creating multiple instances
my_dog=Dog('willie',6)
your_dog=Dog('lucy',3)

print(f"\nMy dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old ")
my_dog.sit()
print(f"\nMy dog's name is {your_dog.name}")
print(f"my dog age is {your_dog.age} years old")
your_dog.sit()
 #Exercise
class Restaurant:
 	def __init__(self,restaurant_name,cuisine_type):
 		self.restaurant_name=restaurant_name
 		self.cuisine_type=cuisine_type
 	def open_restaurant(self):
 		print(f"{self.restaurant_name} is now opened")
describe_restaurant=Restaurant('Good Food','nigerian jollof')
print(f'\nThe name of my restaurant is {describe_restaurant.restaurant_name} restaurant')
print(f"Makes {describe_restaurant.cuisine_type}")
describe_restaurant.open_restaurant()

describe_restaurant=Restaurant('madam Edo','italian food')
print(f'\nThe name of my restaurant is {describe_restaurant.restaurant_name} restaurant')
print(f"Makes {describe_restaurant.cuisine_type}")
describe_restaurant.open_restaurant()
class User:
 	def __init__(self,first_name,last_name):
 		self.first_name=first_name
 		self.last_name=last_name
 	def walk(self):
 		print(f'{self.first_name} love to walk home')
describe_user=User('lebron','james')
print(f'\nMy name is {describe_user.first_name} {describe_user.last_name}')
describe_user.walk()
greet_user=User('Simpa','Emmanuel')
print(f"\nHello {greet_user.first_name} {greet_user.last_name}")

#The car class
class Car:
	def __init__(self,make,model,year):
		"""initialize attribute to describe a car"""
		self.make=make
		self.model=model
		self.year=year
	def get_describtive_name(self):
		"""Return a neatly formatted describtive name"""
		long_name=f"{self.year} {self.make} {self.model}"
		return long_name.title()
my_car=Car('audi','a4',2019)
print(my_car.get_describtive_name())
#setting a default value for an attribute
class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
	def get_describtive_name(self):
		long_name=f"{self.year} {self.make} {self.model}"
		return long_name.title()
	def read_odometer(self):
		"""print a statement showing the car's miliege"""
		print(f"This car has {self.odometer_reading} miles on it")
my_car=Car('audi','a4',2019)
print(my_car.get_describtive_name())
my_car.read_odometer()
#modifying an attribute's value through a method
class Car:
	def __init__(self,brand,model):
		self.brand=brand
		self.model=model
		self.odometer_reading=0
	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it")
	def update_odometer(self,mileage):
		self.odometer_reading=mileage
		
my_new_car=Car('toyota','s280')
print(f"i have {my_new_car.brand} and is {my_new_car.model} model")
my_new_car.update_odometer(23)
my_new_car.read_odometer()
#Incrementing an attribute's value through a method

#Execrise
class Restaurant:
	def __init__(self,name,location):
		self.name=name
		self.location=location
		self.number_served=0
	def get_details(self):
		food=f"\n{self.name} is located in {self.location}"
		return food
	def served_food(self):
		print(f'number of food served {self.number_served}')
	def update_served_food(self,food):
		self.number_served=food
	def increment_food(self,food):
		self.number_served +=food

call_restaurant=Restaurant('king delight','gwarimpa')
print(call_restaurant.get_details())
call_restaurant.served_food()
#modifying an attribute value directly
call_restaurant.number_served=23
call_restaurant.served_food()
#modifying an attribute value through a method
call_restaurant.update_served_food(42)
call_restaurant.served_food()
#Incrementing an Attribute’s Value Through a Method
call_restaurant.increment_food(100)
call_restaurant.served_food()

#inheritance
class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
	def get_descriptive_name(self):
		long_name=f"{self.year} {self.make} {self.model}"
		return long_name.title()
	def read_odometer(self):
		print(f"This car has a {self.odometer_reading} miles on it")
	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print('youcant roll back an odometer')
	def increment_odometer(self,miles):
		self.odometer_reading=miles
class ElectricCar(Car):
	"""Represent aspect of car specific to electric vehicles"""
	def __init__(self,make,model,year):
		"""Initialize attributes of the parent class"""
		super().__init__(make,model,year)
mytelsa=ElectricCar('telsa','model s',2019)
print(mytelsa.get_descriptive_name())

#Defining attributes and methods for the child class
class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
	def get_describtive_name(self):
		long_name=f"{self.year} {self.make} {self.model}"
		return long_name.title()
	def read_odometer(self):
		print(f"This car has a {self.odometer_reading} miles on it")
	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print('you cant roll back an odometer')
	def increment_odometer(self,miles):
		self.odometer_reading=miles
class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery_size=75
	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kwh battery")
my_telsa=ElectricCar('telsa','model s',2019)
print(my_telsa.get_describtive_name())
my_telsa.describe_battery()

#instance as an attribute
class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
	def get_descriptive_name(self):
		long_name=f"{self.year} {self.make} {self.model}"
		return long_name.title()
class Battery:
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size
	def describe_battery(self):

		print(f"This car has a {self.battery_size}-kWh battery.")
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):

		super().__init__(make, model, year)
		self.battery = Battery()
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


users={
'aeinstern':{
'first':'albert',
'last':'einstern',
'location':'princeton',
},
'mcurie':{
'first':'marie',
'last':'curie',
'location':'paris',
},	
}	
for username,user_info in users.items():
	print(f"\nusername :{username}")
	full_name=f"{user_info['first']} {user_info['last']}"
	location=f"{user_info['location']}"
	print(f"\tFullname :{full_name.title()}")
	print(f"\tLocation :{location.title()}")
responses={}
polling_active =True

















