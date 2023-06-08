num1 = 42   #variable declaration, numbers
num2 = 2.3  #variable declaration, numbers
boolean = True #variable declaration, boolean
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #varriable declaration, dictionary, initialize
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple, initialize
print(type(fruit)) #log, type check
print(pizza_toppings[1]) #log, access value
pizza_toppings.append('Mushrooms') #list, add value
print(person['name']) #log, dictionary, accesss value
person['name'] = 'George' #dictionary, change value
person['eye_color'] = 'blue' #dictionary, add value
print(fruit[2]) #log, tuple, access value

if num1 > 45: #conditional, if statement
    print("It's greater") #log
else: #conditional, else
    print("It's lower") #log

if len(string) < 5: #conditional, if statement
    print("It's a short word!") #log
elif len(string) > 15: #elif statement
    print("It's a long word!") #log
else: #elif statement
    print("Just right!") #log

for x in range(5): #for loop, start
    print(x) #log
for x in range(2,5): #for loop, start
    print(x) #log
for x in range(2,10,3): #for loop, start
    print(x) #log
x = 0 #variable declaration, number
while(x < 5): #while loop, start
    print(x) #log
    x += 1 #increment

pizza_toppings.pop() #list, delete value
pizza_toppings.pop(1) #list, delete value

print(person)   #log statement
person.pop('eye_color') #dictionarry, remove value
print(person)   #log statement

for topping in pizza_toppings: #for loop, start
    if topping == 'Pepperoni': #conditional, if
        continue    #continue
    print('After 1st if statement') #log
    if topping == 'Olives':#conditional, if
        break #break

def print_hello_ten_times(): #function
    for num in range(10): #for loop, argument
        print('Hello') #log

print_hello_ten_times() #function call

def print_hello_x_times(x): #function, parameter
    for num in range(x): #for loop
        print('Hello') #log

print_hello_x_times(4) #function call, parameter

def print_hello_x_or_ten_times(x = 10): #function, parameter
    for num in range(x): #for loop
        print('Hello') #log

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) #function call, parameter


"""
Bonus section
"""

# print(num3)                       #log
# num3 = 72                         #variable declaration
# fruit[0] = 'cranberry'            #KeyError: 'tuple' object does not support item reassignment
# print(person['favorite_team'])    #KeyError: 'favorite_team'
# print(pizza_toppings[7])          #IndexError: list index ouut of range
#   print(boolean)                  #IndentationError: unexpected indent
# fruit.append('raspberry')         #AttributeError: 'tuple' has no attribute 'append'
# fruit.pop(1)                      #AttributeError: 'tupl' has no attribute 'pop'