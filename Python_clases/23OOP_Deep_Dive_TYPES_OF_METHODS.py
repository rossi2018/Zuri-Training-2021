#Object oriented deep dive class
class Animal:
    # Class attribute
    animal_type='insects'
    # instance(object) attribute
    def __init__ (self,name,number_of_legs):
        self.name=name
        self.number_of_legs=number_of_legs
    #This a method (an instance method)
    def can_run(self):
        print(f'Animal {self.name} runs with {self.number_of_legs} legs')

animal_one= Animal ('hen',2)
animal_two= Animal ('Cat',4)

#Calling the method can_run on the instance of the animal_one and animal_two
animal_one.can_run()
animal_two.can_run()

print('='* 40)

print(animal_one.animal_type)
print(animal_two.animal_type)

#We have three type of method in python 
#1. Instance method 
#2. class method 
#3.Static method 

print('1. Insatance method=======================================================')
#Instance method: This is a very basic and easy method that we use regularly when we create classes in python.
#  If we want to print an instance variable or instance method we must create an object of that required class.

#If we are using self as a function parameter or in front of a variable, that is nothing but the calling 
# instance itself.
#As we are working with instance variables we use self keyword.

#Look at the code below

#Instance Method Example in Python 
class Student:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    #This an instance method
    def avg(self):
        return (self.a + self.b)/2

s1=Student(10,20)
print(s1.avg())
#In the above program, a and b are instance variables and these get initialized when we create an object 
# for the Student class. If we want to call avg() function which is an instance method, we must create an
#  object for the class.

#If we clearly look at the program, the self keyword is used so that we can easily say that those are 
# instance variables and methods.

print('2. Class method ============================================================================')
#The purpose of the class methods is to set or get the details (status) of the class. That is why they
#  are known as class methods. They can’t access or modify specific instance data. They are bound to the 
# class instead of their objects.
# class method  modify the general state of the class specific details.

#  Two important things about class methods:

# In order to define a class method, you have to specify that it is a class method with the help of the 
# @classmethod decorator

#Class methods also take one default parameter- cls, which points to the class. Again, this not mandatory
#  to name the default parameter “cls”. But it is always better to go with the conventions

class ANIMAL:
    # Class attribute
    animal_type='INSECTS'
    # instance(object) attribute
    def __init__ (self,name,number_of_legs):
        self.name=name
        self.number_of_legs=number_of_legs
    #This a class method 
    @classmethod
    def can_see(cls):
        print(f'Animal can see')

animal_one= ANIMAL ('hen',2)
animal_two= ANIMAL ('Cat',4)

#calling the class method in animal_one and animal_two 
animal_one.can_see()
animal_two.can_see() #it displays animal can see in but state of animal_one and animal_two 

print('3. Static method ==================================================================================')
#static method:Static methods cannot access the class data. In other words, they do not need to access the 
# class data. They are self-sufficient and can work on their own.  Since they are not attached to any class 
# attribute, they cannot get or set the instance state or class state.
#static methd Cannot access anything else in the class.They are totally self-contained code.

#In order to define a static method, we can use the @staticmethod decorator (in a similar way we used  
# @classmethod decorator). Unlike instance methods and class methods, we do not need to pass any special 
# or default parameters.

# Static Method Implementation in python
class STUDENT:
    name = 'STUDENT'
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    @staticmethod
    def info():
        return "This is a student class"

print(STUDENT.info())

#Check when to use each of the method 