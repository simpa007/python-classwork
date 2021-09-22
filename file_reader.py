#Files Path
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
print(contents.rstrip())
#Reading lind by line
filename="pi_digits.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
#making a lists of lines from a file
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line)
#working with a field contents
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

#Large Files:one million Digits
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

#Exercise
with open('learning_python.txt') as file_object:
    content=file_object.read()
print(content)
filename='learning_python.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
text=''
for line in lines:
    text += line.lstrip()
print(text)
print(len(text))

#Writing to an Empty File
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write('I love programming\n')

#Writing mutiple lines
    file_object.write('I love creating new games\n')
    
#Appending to a file
with open(filename,'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')
