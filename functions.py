def greet_user():
	"""Display a simple greeting"""
	print('Hello!')
greet_user()
#Passing Information to a Function
def greet_user(username):
	"""Display a simple greeeting"""
	print(f'Hello, {username.title()}')
greet_user('jesse!')
greet_user('sarah!')
#Exercise
def display_message():
	print('I am learning about functions')
display_message()
def favourite_book(book):
	print(f"One of my favourite book is {book.title()}")
favourite_book('think and grow rich')
favourite_book('the richest man in bablyon')
#Positional Arguments
def describe_pet(animal_type,pet_name):
	"""Describe information about a pet"""
	print(f"\nI have a {animal_type.title()}")
	print(f"My {animal_type}'s name is {pet_name}")
describe_pet('hamster','harry')
#multiple function calls
def describe_pet(animal_type,pet_name):
	"""Describe information about a pet"""
	print(f"\nI have a {animal_type.title()}")
	print(f"my {animal_type}'s name is {pet_name}")
describe_pet('hamster','harry')
describe_pet('dog','willie')
#Order Matter in Positional Arguments
#Keyword Arguments
def describe_pet(animal_type,pet_name):
	"""Display information about a pet"""
	print(f"\nI have a {animal_type.title()}")
	print(f"my {animal_type}'s name is {pet_name}")
describe_pet(animal_type='dog',pet_name='bigo')
describe_pet(pet_name='jack',animal_type='lion')
#Default values
def describe_pet(pet_name,animal_type='dog'):
	print(f"\nI have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name}")
describe_pet(pet_name='willie')

def describe_pet(pet_name,pet_size,animal_type='dog',):
	print(f"\nI have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name} with a {pet_size} size")
describe_pet(pet_name='willie',pet_size='medium',animal_type='mster')
#Exercise
def describe_city(city,country='france'):
	print(f"{city.title()} is in {country.title()}")
describe_city('paris')
describe_city('lagos','nigeria')
describe_city('kampala','ugandan')
#Returning a simple value
def get_formatted_name(first_name,last_name):
	full_name=f"{first_name} {last_name}"
	return full_name.title()
name=get_formatted_name('simpa','emmanuel')
musician=get_formatted_name('peter','parker')
print(name)
print(musician)
def name(first_name,last_name):
	full_name= f"{first_name} {last_name}"
	return full_name.title()
name=name('kim','oparah')
print(name)

#Making an Argument Optional
def get_formatted_name(first_name,middle_name,last_name):
	full_name=f"{first_name} {middle_name} {last_name}"
	return full_name.title()
musician=get_formatted_name('simpa','gift','emmanuel')
print(musician)
def your_name(first_name,middle_name,last_name):
	full_name=f"{first_name} {middle_name} {last_name}"
	return full_name.title()
name=your_name('john','kelvin','great')
print(name)

#Making middle name optional
def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)
#Returning a Dictionary
def build_person(first_name,last_name):
	"""Return a dictionary of information about a person"""
	person={'first':first_name,'last':last_name}
	return person
musician=build_person('Dada','Esther')
print(musician)

def build_person(first_name,last_name,age=None):
	person={'first':first_name,'last':last_name}
	if age:
		person['age']=age
	return person
musician=build_person('jimi','bernado',age=27)
print(musician)
#Exercise
def city_country(city,country):
	place=f"{city},{country}"
	return place.title()
city=city_country('lagos', 'nigeria')
places=city_country('paris', 'france')
print(city)
print(places)
def make_album(artist_name,album_title):
	album={'artist':artist_name,'title':album_title}
	return album
musician=make_album('wizkid','starboy')
print(musician)
musician=make_album('davido','good time')
print(musician)
musician=make_album('chris brown','love')
print(musician)

def make_album(artist_name,album_title,songs=None):
	album={'artist':artist_name,'title':album_title}
	if songs:
		album['songs']=songs
	return album
musician=make_album('davido','eya',10)
print(musician)

#Passing a List
def greet_user(names):
	for name in names:
		print(f"Hello, {name.title()}!")
usernames=['hannah','ty','margot']
greet_user(usernames)
#modifying a list in a function
def print_models(unprinted_design,completed_models):
	while unprinted_design:
		current_design=unprinted_design.pop()
		print(f"printing model: {current_design}")
		completed_models.append(current_design)
def show_completed_model(completed_models):
	print('\nThe following models have been printed')
	for completed_model in completed_models:
		print(completed_model)
unprinted_design=['phone case','robot pendant','dodecahedron']
completed_models=[]
print_models(unprinted_design,completed_models)
show_completed_model(completed_models)
#Exercise
def show_messages(messages):
	for message in messages:
		print(message)
msg=['how ar you doing?','i love you!']
show_messages(msg)
#passing an arbitrary numbers of arguments
def make_pizza(*toppings):
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green',' cheese')
def make_pizza(*toppings):
	"""summarize the pizza we are about to make"""
	print("\nMaking the pizza with the followin toppings:")
	for topping in toppings:
		print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','green pepper','extra cheese') 
#mixing positional and arbitrary arguments
def make_pizza(size,*toppings):
	print(f"\nmaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f'- {topping}')
make_pizza(16,'pepperoni')
make_pizza(12,'murooms','green pepper','extra cheese')
def build_profile(first,last,**user_info):
	"""Build a dictionry containing everything we know about a user"""
	user_info['first_name']=first
	user_info['last_name']=last
	return user_info
user_profile=build_profile('simpa','emmanuel',location='paris',field='physics')
print(user_profile)
#Exercise
def sand_wiches(*toppings):
	print("\nMaking different type of sandwich ordered:")
	for topping in toppings:
		print(f"-{topping}")
sand_wiches('bacon','beef')
sand_wiches('chicken','cheese')
sand_wiches('pork')

def build_profile(first,last,**user_info):
	user_info['first']=first
	user_info['last']=last
	return user_info
user_profile=build_profile('john','edet',age=22,occupation='student')
print(user_profile)
#storing your function in modules

