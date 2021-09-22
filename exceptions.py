#Using try-except Blocks
"""try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")

#using exceptions to prevent crashes

print("Give me two numbers and I'll divide it")
print("Enter 'q' to end program")
while True:
    first_number=input('\nfirst number:')
    if first_number == 'q':
        break
    second_number=input('\nSecond number:')
    if second_number == 'q':
        break
    try:
        result= int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("\nyou can't divide by 0")
    else:
        print(result)

#Handling the FileNotFoundError Exception

filename="alice.txt"
try:
    with open(filename) as f:
        contents=f.read()
except FileNotFoundError:
    print(f"sorry this {filename} does not exist")
    
#Analyzing Text
filename="learning_python.txt"
try:
    with open(filename) as f:
        content=f.read()
except FileNotFoundError:
    print(f"This {filename} does not exist")
else:
    words=content.split()
    num_words=len(words)
    print(f"\nThis file has {num_words} number of words")

#Working with multiple files
def count_word(filename):
    try:
        with open(filename,encoding="utf-8") as f:
            content=f.read()
    except FileNotFoundError:
        print(f"This file {filename} does not exist")
    else:
        words=filename.split()
        num_words=len(words)
        print(f"The {filename} has about {num_words} number of words")
#filename="programming.txt"
#count_word(filename)
filenames=['learning_python.txt','programming.txt']
for filename in filenames:
    count_word(filename)

#Exercise
print("\nEnter two numbers")
while True:
    num1 = input('Enter first number:')
    num2 = input('Enter second number:')
    try:
        sum = int (num1) + int (num2)
        print(sum)
    except ValueError:
        print('you cannot add alpablet')
        break

def read_files(filename):
    try:
        with open(filename) as file_object:
            content=file_object.read()
            print(content)
    except FileNotFoundError:
        pass
filenames =['cats.txt','dogs.txt','gbp.txt']
for filename in filenames:
    read_files(filename)
    

#STORING DATA
#json.dump()
import json
numbers = [2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)
#json.load()
with open(filename) as f:
    numbers=json.load(f)
print(numbers)"""

#Saving and Reading User-Generated Data
#Saving
"""import json
user =input("What is your name:")
filename ='username.json'
with open(filename, 'w') as f:
        json.dump(user,f)
        print(f"we'll remeber you when you come back, {user}")
#Reading
with open(filename) as f:   
    user=json.load(f)
    print(f"welcome back, {user}")
"""
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
"""filename = "numbers.json"
try:
    with open(filename) as f:
        num=json.load(f)
except FileNotFoundError:
    num = input("Enter a number:")
    with open(filename,'w') as f:
        json.dump(num,f)
        print(f"That is my favourite {num}")
else:
    print(f"List of numbers {num}")       

#Refactoring"""
#making your code cleaner, easier to understand and easy to extend.
"""import json
def greet_user():
    Greet the user by name
    filename = "username.json"
    try:
        with open(filename) as f:
            username=json.load(f)
    except FileNotFoundError:
        username = input("Enter your name:")
        with open(filename,'w') as f:
            json.dump(username,f)
            print(f"Hello {username}")
    else:
        print(f"\nwelcome back {username}")
greet_user()"""

#Refactoring
"""import json
def get_stored_username():
    Get stored username if available
    filename = "text.json"
    try:
        with open(filename) as f:
            txt = json.load(f)
    except FileNotFoundError:
        return None 
    else:
        return txt
def greet_user():
    Greet the user by name
    txt = get_stored_username()
    if txt:
        print(f"welcome back from {txt}")
    else:
        txt = input("Where are you from:")
        filename = "text.json"
        with open(filename,'w') as f:
            json.dump(txt,f)
            print(f"will love to visit {txt} some day")
greet_user()"""


import json
def get_stored_username():
    """Get stored username if available"""
    filename = "text.json"
    try:
        with open(filename) as f:
            text = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return text
def get_new_user():
    """prompt for a new username"""
    text = input("Enter your full name:")
    filename = "text.json"
    with open(filename,'w') as f:
        json.dump(text,f)
    return text
def greet_user():
    """Greet user by name"""
    text=get_stored_username()
    if text:
        print(f"welcome back {text}")
    else:
        text = get_new_user()
        print(f"we'll remeber you when you come back, {text}")
greet_user()
#EXERCISE
filename = "username.json"
try:
    with open (filename) as f:
        user=json.load(f)
except FileNotFoundError:
    user=input("Enter your name:")
    filename = "username.json"
    with open(filename,'w') as f:
        json.dump(user,f)
        print(f"welcome back {user}")
else:
    print(f"This file already existed {user}")



