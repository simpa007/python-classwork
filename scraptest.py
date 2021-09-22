

def person(name,age,occupation,sex,level):
    person={'name':name,"age":age,"occupation":occupation,'sex':sex,'level':level}
    return person
user=person('simpa',17,'web developer','male','beginner')
user2=person('femi',49,'full stack developer','female','professional')

print(user)
print(user2)

#passing a list
def greet_user(names):
    for name in names:
        print(f'Hello {name.title()} how are you today?')
greet_user(['john','femi'])

#passing an arbitrary numbers of arguments
def make_pizza(*toppings):
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green',' cheese')

def user(firstname,lastname):
    fullname=f"{firstname} {lastname}"
    return fullname.title()
user1=user('simpa','emmanuel')
print(user1)






