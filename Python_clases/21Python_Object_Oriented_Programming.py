#---------------Python Object Oriented Programming------------------------
#Object-oriented programming (OOP) is a method of structuring a program by bundling related 
# properties and behaviors into individual objects. 

#Python is a multi-paradigm programming language. It supports different programming approaches.
#One of the popular approaches to solve a programming problem is by creating objects. This is 
# known as Object-Oriented Programming (OOP).
#An object has two characteristics:
#--attributes
#--behavior
#Let's take an example:A dog  can be an object,as it has the following properties:
#--name, age, color as attributes
#--bark, howl as behavior
# The concept of OOP in Python focuses on creating reusable code. This concept is also known 
# as DRY (Don't Repeat Yourself).
#In Python, the concept of OOP follows some basic principles:

#---------Classs-----------------------

#What are CLasses? Classes provides means by which we bundle related data and functionalities
# together. It is a core aspect of object oriented programming,which is a programming          
#paradigm that is based on the concept of 'objects'.

#A class is a blueprint for the object.
# We can think of class as a sketch of a dog with labels. It contains all the details about the
#  name, colors, size etc. Based on these descriptions, we can study about the dog. Here, a dog
#  is an object.
# The example for class of dog can be :

class dog:
    pass 

#Here, we use the class keyword to define an empty class dog. From class, we construct instances. 
# An instance is a specific object created from a particular class.
# pass is often used as a placeholder indicating where code will eventually go. It allows you to run 
# this code without Python throwing an error.

#------------Object--------------------
#An object (instance) is an instantiation of a class. When class is defined, only the description 
# for the object is defined. Therefore, no memory or storage is allocated.
#The properties of dog we use are name and age.


#The properties that all Dog objects must have are defined in a method called .__init__(). 
# Every time a new Dog object is created, .__init__() sets the initial state of the object by 
# assigning the values of the object’s properties. That is, .__init__() initializes each new 
# instance of the class.

# You can give .__init__() any number of parameters, but the first parameter will always be a variable 
# called self. When a new class instance is created, the instance is automatically passed to the self
#  parameter in .__init__() so that new attributes can be defined on the object.

#Let’s update the Dog class with an .__init__() method that creates .name and .age attributes:

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Notice that the .__init__() method’s signature is indented four spaces. The body of the method 
# is indented by eight spaces. This indentation is vitally important. It tells Python that the 
# .__init__() method belongs to the Dog class.
#in the body of .__init__(), there are two statements using the self variable:

#1. self.name = name creates an attribute called name and assigns to it the value of the name parameter.
#2.self.age = age creates an attribute called age and assigns to it the value of the age parameter.

#------------ instance attributes--------------------
#Attributes created in .__init__() are called instance attributes. An instance attribute’s value is 
# specific to a particular instance of the class. All Dog objects have a name and an age, but the values 
# for the name and age attributes will vary depending on the Dog instance.

#-------------class attributes ----------------------
#On the other hand, class attributes are attributes that have the same value for all class instances.
#  You can define a class attribute by assigning a value to a variable name outside of .__init__().

#For example, the following Dog class has a class attribute called species with the value "Canis familiaris":

class DOG:
    # Class attribute
    species = "Canis familiaris"
    # instance(object) attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Class attributes are defined directly beneath the first line of the class name and are indented by four spaces. 
# They must always be assigned an initial value. When an instance of the class is created, class attributes are
#  automatically created and assigned to their initial values.

#Use class attributes to define properties that should have the same value for every class instance. 
# Use instance attributes for properties that vary from one instance to another.

#Now that we have a Dog class, let’s create some dogs!

class DOGG:
    # Class attribute
    species = "Canis familiaris"
    # instance(object) attribute
    def __init__(self, name, age):
        self.name = name 
        self.age = age

# instantiate the DOGG class
buddy = DOGG("Blu", 10)
miles = DOGG("Woo", 15)

# access the class attributes
print("Buddy is a {}".format(buddy.__class__.species))
print("Miles is also a {}".format(miles.__class__.species))

# access the instance attributes
print("{} is {} years old".format( buddy.name, buddy.age))
print("{} is {} years old".format( miles.name, miles.age))


print('Create an instance(object) of a class--------------------------------------------------------------------')
#Creat an instance of a class
class car:
    pass

car_1=car() #created an instance of class car() using car_1 as variable name
print(type(car_1)) 
print('This signify that (car_1) is an object of the class because it depandent on the main function of car') 

print('Understanding attribute and parameter by adding  and calling them -------------------------------------------')
#adding attribute  name and adding the value to the name parameter.
class CAR:
    def __init__(self,name,color):
        self.car_name=name #car_name is the attribute name while name is the parameter name
                           #You can just use name instead of car_name.Its just demonstrating attribute name and 
                           #parameter
        self.color=color
CAR_1=CAR('Mercedez','Silver')
CAR_2=CAR('Bmw','Blue')

print(f'{CAR_1.car_name} is has a beautify design with {CAR_2.color} color')
print(CAR_2.car_name)

print(' Method for class------------------------------------------------------------------------------------')
# Methods: These are functions affiliated with some class
#Note: A function is a block of code which only runs when it is called.

#A method is a function which describe an action the object can carry out 

class Auto():
    def __init__(self,manufacture,milage):
        self.manufacture=manufacture
        self.milage=milage
    
    #This a method 
    def accel(self): #You can do any thing in this code block here like calculations of lenght etc  
        print(f'{self.manufacture} {self.milage} acceleration is the top in EV market')

dealer1=Auto('Tesla','100Mph')
dealer2=Auto('GM','60Mph')


print(dealer1.manufacture)
dealer1.accel() #This demonstrate how you can call a method in a class
dealer2.accel() #This call will show the property of dealer2 

print('Doc strings =========================================================================================')
# Doc strings: Python documentation strings (or docstrings) provide a convenient way of associating 
# documentation with Python modules, functions, classes, and methods. It's specified in source code that is 
# used, like a comment, to document a specific segment of code.

#Most of the classes in python have built in doc string related to them like dict() class 
# Like this example below. Uncomment to see how it works
#print(help(dict())) # The output gives you explanation of the dictionary class 

#When you are building your own class, doc strings are very import as you put them as an explanation 

#Python docstrings are the string literals that appear right after the definition of a function, 
# method, class, or module.
class AUTO():
    '''
    This is a car class
    '''
    #Inside the triple quotation marks is the docstring of the function
    def __init__(self,manufacture,milage):
        self.manufacture=manufacture
        self.milage=milage

    def ACCEL(self): 
        print(f'{self.manufacture} {self.milage} acceleration is the top in EV market')

dealer01=AUTO('Tesla','100Mph')
dealer02=AUTO('GM','60Mph')


print(dealer01.manufacture)
dealer01.ACCEL() 
dealer02.ACCEL() 
print(help(AUTO)) # This will print out the docstring documentation 