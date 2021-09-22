print("Hello Python World")
#varaible
message="Hello World"
print(message)
#changing cases in a string with methods
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
#using variables in strings
first_name="simpa"
last_name="emmanuel"
full_name=f"{first_name} {last_name}"
print(full_name.title())
print(f"Hello {full_name.title()}")
#Adding whitespaces to strings with tabs and newlines
print("Languages:\n\tPython\n\tJava\n\tJavascript")
#stripping whitespace
#underscores in numbers
universa_age=14_000_000
print(universa_age)
#multiple Assignments
x,y,z=30,0,10
print(x,y,z)
#constants
MAX_CONNECTIONS=5000
#Lists
bicycles=['treks','cannondale','redline','specilized']
print(bicycles)
#Accessing elements in a lists
bicycles=['treks','cannondale','redline','specilized']
print(bicycles[0].title())
bicycles=['treks','cannondale','redline','specilized']
print(bicycles[-1].title())
#Using individual value from a list
bicycles=['treks','cannondale','redline','specilized']
message=f"my first bicycle was a {bicycles[0].title()}."
print(message)
#changing Adding and Removing elements
#modifying elements in a list
motocycles=['honda','yamaha','suzuki']
print(motocycles)
motocycles[0]='ducati'
print(motocycles)
#Adding elements to a list
#Appending Elements to the End of a lists
motocycles=['honda','yamaha','suzuki']
motocycles.append('ducati')
print(motocycles)
motocycles=[]
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')
print(motocycles)
#inserting Elements into a list
motocycles=['honda','yamaha','suzuki']
motocycles.insert(0,'ducati')
print(motocycles)
#Removing Elements from a list
#Removing an item using the del statement
motocycles=['honda','yamaha','suzuki']
del motocycles[0]
print(motocycles)
#Removing an item using the pop()method
subjects=['maths','english','physic','biology']
print(subjects)
popped_subjects=subjects.pop()
print(subjects)
print(popped_subjects)
#popping items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned=motorcycles.pop(0)
print(f"My first motorcycle was a {first_owned.title()}")
#Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
expensive='ducati'
motorcycles.remove(expensive)
print(motorcycles)
print(f"\nA {expensive.title()} is too expensive for me")
#Organizing a list
#sorting a list permanently with the sort()method
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars) 
#Reverse
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
#sorting a list temporarily with the sorted() function
cars=['bmw','audi','toyota','subaru']
print('\nHere is the original list')
print(cars)
print('\nHere is the sorted list')
print(sorted(cars))
print('\nHere is the original list again')
print(cars)
#printing a list in reverse order
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)
#finding the length of a lists
cars=['bmw','audi','toyota','subaru']
len(cars)
#Working with Lists
#Looping Through an Entire List
magicians=['david','alice','caroline']
for magician in magicians:
	print(magician)
#Doing more work within a for loop
magicians=['david','alice','caroline']
for magician in magicians:
	print(f"{magician.title()},that was a great trick!")
	print(f"I can't wait to see your next trick {magician.title()}\n")
#Doing something after a for loop
magicians=['david','alice','caroline']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick {magician.title()}\n ")
print("Thank you, everyone. that was a great magic show!")
#Making Numerical Lists
#using the range() function
for value in range(1,5):
	print(value)
for value in range(1,6):
	print(value)
for value in range(6):
	print(value)
#Using range() to make a List of Numbers
numbers=list(range(1,6))
print(numbers)
even_numbers=list(range(2,11,2))
print(even_numbers)
odd_numbers=list(range(1,20,2))
print(odd_numbers)
squares=[]
for value in range(1,11):
	square=value ** 2
	squares.append(square)
print(squares)
squares=[]
for value in range(1,11):
	squares.append(value **2)
print(squares)
#simple statistics with a list of numbers
digits=[0,1,2,3,4,5,6,7,8,9]
min(digits)
max(digits)
sum(digits)
#list comprehension
squares=[value**2 for value in range(1,11)]
print(squares)
cubes=[value**3 for value in range(1,11)]
print(cubes)
#working with part of a list
#slicing a list
players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])
#Looping through a Loop
players=['charles','martina','michael','florence','eli']
print('Here are the first three players on my team: ')
for player in players[:3]:
	print(player.title())
#Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favourite food are:")
print(my_foods)
print("\nMy friend's favourite food are:")
print(friend_foods)

my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('\nMy favourite food are:')
print(my_foods)
print("\nMy friend's favourite food are:")
print(friend_foods)
#Tuples
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#Looping through all values in a Tuple
dimensions=(200,50)
for dimension in dimensions:
	print(dimension)
#Writing over a Tuple
dimensions=(200,50)
print("Original dimension:")
for dimension in dimensions:
	print(dimension)
dimensions=(400,100)
print("\nModified dimension:")
for dimension in dimensions:
	print(dimension)

#IF STATEMENTS
cars=['audi','bmw','subaru','toyota']
for car in cars:
	if car=='bmw':
		print(car.upper())
	else:
		print(car.title())
#checking for Equality
car='audi'
car=='audi'
#Ignoring case when checking for Equality
car='Audi'
car.lower()=='audi'
#checking for Inequality
requested_topping='mushrooms'
if requested_topping!='anchovies':
	print('Hold the anchovies!')
#Numerical comparisons
answer=17
if answer!=42:
	print('That is not the correct answer. please try again!')
#checking multiple condition
#Using and to check multiple condition
#The use of and & or
#Checking whether a value is in a List
requested_topping=['mushrooms','onions','pineapple']
'onions'in requested_topping
#Checking whether a value is not in a list
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.  ")
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#IF STATEMENTS
age=19
if age >=18:
	print('you are eligible to vote')
	print('Have you registered to vote yet?')
#IF ELSE STATEMENTS
age=11
if age >=18:
	print('you are eligible to vote')
	print('Have you registered to vote yet?')
else:
	print('\nsorry,you are too young to vote')
	print('please register to vote as soon as you turn 18!')
#The if-elif-else chain
age=12
if age < 4:
	print('Your admission cost is $0')
elif age <= 18:
	print('\nYour admission cost is $25')
else:
	print('Your admission is $40')
age=12
if age < 4:
	price=0
elif age <=18:
	price=25
else:
	price=40
print(f"your admission cost is ${price}")
#Using multiple elif blocks
age=12
if age < 4:
	price=0
elif age < 18:
	price=25
elif age < 65:
	price=40
else:
	price=20
print(f"your admission cost is ${price}")
#omitting the else block
age=42
if age < 4:
	price=0
elif age < 18:
	price=25
elif age < 65:
	price=40
elif age >= 65:
	price=20
print(f"your admission cost is ${price}")
#Testing multiple condition
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
	print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
	print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
	print('Adding extra cheeese')
print('\nFinished making your pizza')
cars=['bmw','subaru','audi']
#checking for special items
requested_toppings=['mushrooms','green pepper','extra cheese']
for requested_topping in requested_toppings:
	print(f'Adding {requested_topping}')
print('\nFinished making pizza')
requested_toppings=['mushrooms','green pepper','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping=='green pepper':
		print('Sorry, we are out of green pepper right now.')
	else:
		print(f'Adding {requested_topping}')
print('\nFinished making your pizza')
#Checking that a list is not empty
requested_toppings=[]
if requested_toppings:
	for requested_topping in reqeusted_toppings:
		print(f'Adding {requested_topping}')
		print('\nFinished making your pizza')
else:
	print('Are you sure you want a plain pizza?')
#Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f'Adding {requested_topping}')
	else:
		print(f'sorry we dont have {requested_topping}')
print('\nFinished making your pizza')


		

print('hello world')
#Writing clear prompt
name=input('pleae enter your name:')
print(f"\nHello {name}!")
print('hello world')
#How the input() function works
message=input('Tell me something and i will repeat it back to you:')
print(message)
#Writing clear prompt
name=input('pleae enter your name: ')
print(f"\nHello {name}!")
prompt='if you tell us who you are we can personalize the message you see.'
prompt+='\nwhat is your first name? '
name=input(prompt)
print(f"\nHello,{name}!")
#using int() to accept numerical input
age=input('How old are you? ')
print(age)
age=int(age)
if age >=18:
    print('you are eligible to vote')
else:
    print('Not eligible')
height=input('How tall are you, in inches? ')
height=int(height)
if height >= 48:
    print('\nYou are tall enough to ride')
else:
    print("\nYou'll be able to ride when you are a little older")
#The modulo operator
number=input('\nEnter a number i will tell you if it even or odd: ')
number=int(number)
if number % 2 == 0:
    print('This is an even number')
else:
    print('This is an odd number')
rental_car=input('what kind of rental car would you like? ')
print(f"Let me see if i can find you a {rental_car}")



