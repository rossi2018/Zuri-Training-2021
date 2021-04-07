#A function is a block of code which only runs when it is called.You can pass data, known as parameters,
#  into a function.A function can return data as a result.

#Creating a function- In python a function is defined using the def keyword:
def simple_function(): #This a function definition 
    print('Yay!!! First function') #If you rn this function like this nothing will happen because you 
                                   #have not you have not creat the function

#How do you call a function: you have to call the function signature and 'simple_function()' is the function 
#signature 
simple_function() #this line is function call

print('Argument of a function and paremeter of a function ---------------------------------------------------------')
#The terms parameter and argument can be used for the same thing: information that are passed into a function.

#From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.

def simple_function2(name):
    print(f'Hello {name}')

#Expected 2 blank lines after end of function or class (E305)
name_inpute=input('Enter your name:')
simple_function2(name_inpute)
#Note: name is the parameter while name_inpute is the argument
print('Another argument of a function and paremeter of a function example-----------------------------')
def nameofFunction(count):
    print('This is a function %d' % count)


nameofFunction(4)

print('Number of Arguments of a function ============================================================')
#By default, a function must be called with the correct number of arguments. Meaning that if your function 
# expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

def simple_function3(FirstName,LastName):
    print(f'Hello {FirstName}, are you sure your last name is {LastName}')


first_name=input('Enter your first name:')
last_name=input('Enter your last name:')
simple_function3(first_name,last_name)
#This function expects 2 arguments, and gets 2 arguments

print('Arbitrary Arguments, *args---------------------------------------------------------------------')
#If you do not know how many arguments that will be passed into your function, add a * before the parameter 
# name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
print('First Arbitrary Argument demostrating it can take multiple arguments+++++++++++++++++++++++++++')
def people_names(*args):
    print(args)


first_name1='Manny'
last_name1='Johson'
people_names(first_name1,last_name1)

print('How args take the remaining argument and save it in turple--------------------------------------')

def people_names2(firstname,*args):
    print(firstname)
    print(args)
    

first_Name2='Manny'
last_Name2='Johson'
middleName2='Devs'
people_names2(first_Name2,last_Name2,middleName2)

print('Unpacking tuple from args------------------------------------------------------------------------')
def people_names3(firstname3,*args):
    print(firstname3)
    last_Name3,middleName3=args 
    print(last_Name3)
    print(middleName3)


firstname3='Manny'
middleName3='Johnson'
lastname3='Devs'
people_names3(firstname3,middleName3,lastname3)

print('To verify args as tuple--------------------------------------------------------------------------')
def name(Nick_name,*args):
    print(Nick_name)
    print(args)
    print(type(args))


Nick_name='Beeple'
country='America'
state='New york'
name(Nick_name,country,state)

print('Key word argument..................................................................................')
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
def people_names4(firstname4,LastName4,middleName4):
    print(firstname4)
    print(LastName4)
    print(middleName4)


first_Name4='Tommy'
last_Name4='Johson'
middleName4='Devs'

people_names4(middleName4=middleName4,LastName4=last_Name4,firstname4=first_Name4)

print('Arbitrary Keyword Arguments, **kwargs===============================================================')
#Arbitrary Keyword Arguments, **kwargs- If you do not know how many keyword arguments that will be passed 
# into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:

def people_name_new(*args,**kwargs):
    print(args)
    print(kwargs)


first_Name5='Manny'
last_name5='Johson'
middleName5='Dev'
people_name_new(middleName5=middleName5,LastName5=last_name5,firstname5=first_Name5)
people_name_new('chioma') #This line of code is an argument meaning chioma is added in a tuple 

print('Return Values-------------------------------------------------------------------------------')
# To let a function return a value, use the return statement:
def square_function(value):
    return value **2


square_value=square_function(10)
print(square_value)

print('Lambda function=============================================================================')
#Lambda function-A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

square_value2=lambda x:x**2 #The lambda returns a function and not a value that has been processed
print(square_value2(10))

print('To demostrate that function can be used many times as you want--------------------------------')
def nameofFunction2(name2,count2):
    print('%s called function with count %d' %(name2,count2))


nameofFunction2('Seyi',4)
nameofFunction2('Love',9)
nameofFunction2('Mike',8)

print('Another example to demostrate function cab be used many times ---------------------------------')
def nameofFunction3(name,count):
    print(name * count)


nameofFunction3('seyi ',4)
nameofFunction3('Mike ',10)