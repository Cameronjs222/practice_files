num1 = 42 #variable declaration, number
num2 = 2.3 #variable declaration, number
boolean = True #variable declaration
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, string, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, string, list
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, strings, tuples
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms')
print(person['name']) #log statement
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2]) #log statement

if num1 > 45: #conditional, if statement
    print("It's greater") #log statement
else: #conditional, else statement
    print("It's lower") #log statement

if len(string) < 5: #length check, conditional, if statement
    print("It's a short word!") #log statement
elif len(string) > 15: #length check, conditional else if statement
    print("It's a long word!") #log statement
else: #conditional, else statement
    print("Just right!") #log statement

for x in range(5):

    print(x) #log statement
for x in range(2,5):
    print(x) #log statement
for x in range(2,10,3):
    print(x) #log statement
x = 0
while(x < 5):
    print(x)#log statement
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person) #log statement
person.pop('eye_color')
print(person) #log statement

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement') #log statement
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello') #log statement

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello') #log statement

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') #log statement

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section (multiline comment)
"""
print(num3) #log statement
num3 = 72 #number
fruit[0] = 'cranberry' #string
print(person['favorite_team']) #log statement
print(pizza_toppings[7]) #log statement
print(boolean)#log statement, boolean
fruit.append('raspberry') #sting
fruit.pop(1) #function, argument