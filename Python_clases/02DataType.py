#A data type describe the type of data 
# All of them is a string which can be identified with a double or single qout like
#this

'Laptop' "Desktop" "Software"

#Data type :string examples
string1="Emeka"
string2="4.5"
string3='0'
string4='true'
string='6'

# Print combined strings
print(string1)
print(string1 + ' '+ string4) #Adding two or more string together is called concatenation to produce new string

#Data types: number 
# Number is basically just number 
# Number is what u see without a quite around it 

number1= 4.5
number2= 0
number3= 5
number4= -4
number5= 139484747748484

# Adding two strings together is called concatenation while adding two number together is called addition 
print(number1+ number2)
print(number1+ number3)

# You can't add a number and a string together which is addition and concatebaion together
#print(number3+ string1)

#Data types: Boolean
#Boolean is a state identifier.Its something that shows you the state of something which is either 
#True or Force 

isStudentActive=True #Yes
print(isStudentActive)

isGraduate=False #No
print(isGraduate)

#It's very hard to write a simple program without using boolean 
age= 55
if age > 35:
    print('Yes')