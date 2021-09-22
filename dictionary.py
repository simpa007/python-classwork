# A simple dictionary
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
#Accessing value in a dictionary
alien_0={'color':'green'}
print(alien_0['color'])
alien_0={'color':'green','points':5}
new_points=alien_0['points']
print(f"you just earned {new_points} points!")
#Adding new key-value pairs
alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
#Starting with an empty dictionary
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)
#Modifying values in a dictionary
alien_0={'color':'green'}
print(f"The alien color is now {alien_0['color']}")
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")
if alien_0['speed']=='slow':
	alien_0['x_position'] += 1
elif alien_0['speed']=='medium':
	alien_0['x_position'] += 2
else:
	#This must be a fast alien
	alien_0['x_position'] += 3
print(f"New position: {alien_0['x_position']}")
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
alien_0['speed']='fast'
print(f"\nOriginal position: {alien_0['x_position']}")
if alien_0['speed']=='slow':
	x_increment=1
elif alien_0['speed']=='medium':
	x_increment=2
else:
	#This must be a fast alien
	x_increment=3
#The new position is the old position plus the increment
alien_0['x_position']=alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
#Removing key-value pairs
alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)
#A dictionary of similar objects
favourite_languages={'jen':'python',
'sarah':'c','edward':'ruby','phil':'python'}
language=favourite_languages['sarah']
print(f"Sarah's favourite language is {language.title()}")
#Using get() to access value
alien_0={'color':'green','speed':'slow'}
point_value=alien_0.get('points','No point assigned')
print(point_value)
#Looping through a Dictionary
#Looping through all key-value pairs

user_0={
'username':'simpa_sol',
'first':'Simpa',
'last':'Emmanuel'
}
for key,value in user_0.items():
	print(f'\nkey :{key}')
	print(f'value :{value}')
favourite_languages={
'jen':'python',
'sarah':'c',
'edward':'ruby',
'phil':'python'
}
for name,language in favourite_languages.items():
	print(f"{name.title()}'s favourite language is {language.title()}")
#Looping through all keys in a Dictionary
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys():
	print(name.title())
for name in favourite_languages:
	print(name.title())
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(f'Hi {name.title()}')
	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
if 'eric' not in favourite_languages.keys():
	print('Eric,please take our poll!')
#Looping through a Dictionary's key in a particular order
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favourite_languages.keys()):
	print(f'\t{name.title()}, thank you for taking the poll.')
#Looping through all values in Dictionary
favourite_languages={
'jen':'python',
'sarah':'c',
'edward':'ruby',
'phil':'python'
}
print('The following languages has been mentioned:')
for language in favourite_languages.values():
	print(language.title())
#A set is a collection in which each items must be unique
favourite_languages={
'jen':'python',
'sarah':'c',
'edward':'ruby',
'phil':'python'
}
print('The following languages has been mentioned:')
for language in set(favourite_languages.values()):
	print(language)
rivers={'nile':'egypt','benue':'nigeria','zazo':'south africa'}
for river,country in rivers.items():
	print(f'The {river.title()} runs through {country.title()}')
for river in rivers.keys():
	print(river.title())
for country in rivers.values():
	print(country.title())
favourite_languages={
'jen':'python',
'sarah':'c',
'edward':'ruby',
'phil':'python'
}
persons=['sarah','edward','john']
for names in favourite_languages.keys():
	if names in persons:
		print(f'{names.title()}, thank you for taking the poll.')
	else:
		print(f'{names.title()}, please register for the poll.')
#Nesting
#A list of Dictionary
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)
#Make an empty list for storing aliens
aliens=[]
for alien_number in range(30):
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
for alien in aliens[:3]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['points']=10
		alien['speed']='medium'
	elif alien['color']=='yellow':
		alien['color']='red'
		alien['points']=15
		alien['speed']="fast"

#show the first 5 aliens
for alien in aliens[:5]:
	print(alien)

#show how many aliens have been created.
print(f"Total number of aliens is {len(aliens)}")
#A list in a Dictionary
pizza={'crust':'thick',
'toppings':['mushrooms','extra cheese']
}
print(f"you ordered a {pizza['crust']}-crust pizza " 
	"with the following pizza:")
for topping in pizza['toppings']:
	print('\t'+topping)
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")
#A Dictionary in a Dictionary
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
pet_0={'animal':'cat','owner':'simpa'}
pet_1={'animal':'dog','owner':'peter'}
pet_2={'animal':'rabbit','owner':'mike'}
pets=[pet_0,pet_1,pet_2]
for pet in pets:
	print(pet)







