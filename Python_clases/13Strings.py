#Strings are sequence of character data.The string type in python is called str

#Strings literals may be delimited using either single or double quotes.
#All the characters between the opening delimiter and matching closing delimiter
#are part of the strings

#Strings are words

Rossi='rossi is learning python programming language'
Rossi2='Rossi Is Learning Python'
print(Rossi)

#String operations

#capitalize() - converts the first character to upper case
print(Rossi.capitalize())

#casefold() - convert string into lower case
print(Rossi2.casefold()) 

#count() - Returns the number of times a specified value occurs in a string
print(Rossi.count('o'))
print(Rossi.count('r'))

#endswith() - Returns true if the string ends with the specified value
print(Rossi.endswith('e'))
print(Rossi.endswith('g'))

#find() - Searches the string for a specified value and returns the position of when it was found
print(Rossi.find('rossi'))

#isalpha() - Returns True if all characters in the strings are in the alphabet
Zuri= 'python'
print(Zuri.isalpha()) #True - because all the character in python are alphabet without space
print(Rossi.isalpha()) #False - because it contains character with space 

#isalnum() - Returns True if all characters in the strings are alphanumeric 
three='3'
print(three.isalnum()) #True because all the character in three are numbers

#isdecimal() - Returns True if all character in the string are decimal 
decimal='2.6'
decimal2='34568'
print(decimal.isdecimal()) # False - one character is not decimal 
print(decimal2.isdecimal()) # True- all character in the string are decimal character 

#isdigit()- Returns True if all characters in the string are digits
digit='34'
digit2='3r'
print(digit.isdigit()) #True
print(digit2.isdigit()) #False

#replace()- Returns a string where a specified value is replaced with a special value
name='rossi'
print(name.replace('r','R'))
print(name.replace('i','e'))

#upper()- Converts a string into upper case
justString='ray'
justString2='what is your name'
print(justString.upper())
print(justString2.upper())

#lower() - Converts a string into lower case 
justString3='WHATS YOUR NAME?'
print(justString3.lower())

#split() - splits the string at the specified separator, and returns a list
justString4='I am learning pythond which after will take a deep delve into django frame work'
print(justString4.split())
print(justString3.split())

print('Isinstance-----------------------------------------------------------------------')
#isinstance
# isinstance(object,classinfo) - Python has a built-in function called isinstance() that compares the value 
# with the type given. If the value and type given matches it will return true otherwise false.
#  The return value is a Boolean i.e true or false.

#isinstance(object,classinfo) parameters- instance takes two parameter 
#object-object to be checked
#classinfo - class, type, or tuple of classes and types
numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers,'instance of list?', result)

result = isinstance(numbers, dict)
print(numbers,'instance of dict?', result)

result = isinstance(numbers, (dict, list))
print(numbers,'instance of dict or list?', result)

number = 5

result = isinstance(number, list)
print(number,'instance of list?', result)

result = isinstance(number, int)
print(number,'instance of int?', result)