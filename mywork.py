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

#INTRODUCTION TO WHILE LOOP
#The while loop in action
current_number=1
while current_number <=5:
    print(current_number)
    current_number +=1
#letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
#Using a Flag
prompt="Tell me something,and i will repeat it back to you"
prompt +="\nEnter 'quit' to end program: "
active=True
while active:
    message=input(prompt)
    if message =='quit':
        active=False
    else:
        print(message)
#Using break to Exit a loop
prompt='Plese enter the name of the city you have visited:'
prompt +="\n(Enter 'quit' when you are finished.)"
while True:
    city=input(prompt)
    if city=='quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")
#Using continue in a Loop
current_number=0
while current_number <10:
    current_number +=1
    if current_number % 2==0:
        continue
    print(current_number)
age=input('how old are you: ')
age=int(age)
if age <3:
    price=0
elif age <=12:
    price=10
elif age > 12:
    price=15
print(f'The cost of your movie ticket ${price}')
prompt="please enter requested topping"
prompt+="\nEnter 'quit' to end the program: "
requested_topping=''
while requested_topping !='quit':
    requested_topping=input(prompt)
    if requested_topping !='quit':
        print(requested_topping)
        
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(f"verified users :{current_user.title()}")
    confirmed_users.append(current_user)
#Display confirmed users
print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#Removing All Instances of Specific Values fron a List
pets=['dog','cat','goldfish','dog','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
#Filling a Dictionary with user input
responses={}
#set a flag to indicate polling is active
polling_active=True
while polling_active:
#prompt for person's name and response
    name=input('what is your name? ')
    response=input('which mountain would you like to climb today? ')
    #store the response in the dictionary
    responses[name]=response
    #find out if anyone else is willing to take the poll
    repeat=input('would you like to let another person respond (yes/no):')
    if repeat =="no":
        polling_active=False
    #polling is complete show the result
print("\n...polling result...")
for name,response in responses.items():
    print(f"{name} would like to climb {response}")




