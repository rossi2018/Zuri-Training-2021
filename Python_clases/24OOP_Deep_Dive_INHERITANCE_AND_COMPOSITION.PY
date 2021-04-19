#Inheritance 
#Inheritance is a powerful feature in object oriented programming.

#Inheritance  refers to defining a new class with little or no modification to an existing class. 
# The new class is called derived (or child) class and the one from which it inherits is called the 
# base (or parent) class.

class Animal:
    
    def can_breathe(self):
        return 'can breath'

class birds(Animal):
    pass

class Mammals(Animal): #Another inheritance 
    pass

    def body_size(self):
        return 'mammals have body size of 40kg and above'

mammal_one=Mammals().can_breathe()
mammal_two=Mammals().body_size() 
print(mammal_one) #This demonstrate that mammals is is inheriting from Animal and also have access to the 
                  #can_breath method 

print(mammal_two)

print('Another example of inheritance==============================================================')

class Car:          #parent class

    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

class BMW(Car):     #child class
    pass

class Audi(Car):     #child class
    def audi_desc(self):
        return "This is the description method of class Audi."


obj1 = BMW("BMW 7-series",39.53)
print(obj1.description())

obj2 = Audi("Audi A8 L",14)
print(obj2.description())
print(obj2.audi_desc())

print('Third example of inheritance using custom exception(custom error)==================================')
class customException(Exception):
    pass

class ValueTooSmallException(customException):
    pass

class ValueTooBigException(customException):
    pass

number_value=20

while True:
    try:
        input_number=int(input('Enter a number:'))
        if input_number<number_value:
            raise ValueTooSmallException
        elif input_number>number_value:
            raise ValueTooBigException
        break
        
    except ValueTooSmallException as _:
        print('Value to small')

    except ValueTooBigException as _:
        print('Value too big')

    except Exception as _ :
        print(_.__str__())

print('Hey you got it correctly')



print('Fourth example of  User-Defined Exception in Python demostrating inheritance=======================')
#In this example, we will illustrate how user-defined exceptions can be used in a program to raise and catch
#  errors.
#This program will ask the user to enter a number until they guess a stored number correctly. To help them 
# figure it out, a hint is provided whether their guess is greater than or less than the stored number.

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")

#We have defined a base class called Error.
#The other two exceptions (ValueTooSmallError and ValueTooLargeError) that are actually raised by our program 
# are derived from this class. This is the standard way to define user-defined exceptions in Python programming,
#  but you are not limited to this way only.

print('Composition=========================================================================================')
#composition-In this concept, we will describe a class that references to one or more objects of other classes 
# as an Instance variable. Here, by using the class name or by creating the object we can access the members 
# of one class inside another class. It enables creating complex types by combining objects of different classes.
#  It means that a class Composite can contain an object of another class Component. This type of relationship
# is known as Has-A Relation.

#Note
#inheritance --------> is a relationship
#composition --------> has a relationship 


class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary

    def check_salary(self):
        return self.salary.check_salary()


class salary:

    def __init__(self,amount,bonus):
        self.amount=amount
        self.bonus=bonus

    def check_salary(self):
        return   f'Marketers salary is {self.amount+(self.amount * self.bonus)} with a bonus of {self.bonus}'


marketer_salary=salary(400000,5)
marketer_employee=Employee('Jones','Maketing',marketer_salary)

print(marketer_employee.check_salary())