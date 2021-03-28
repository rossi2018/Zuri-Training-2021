#String formating allow us to decide how the string is printed out 
name= 'Mike' #string -s
age= 55 # Digits - d

print('His name is %s and he is %d years old'%(name,age))

# You can also used the string formating to print out items in list 
sampleList=['Mike','Love','Dove',55]

print('some text %s'% sampleList)

#You can still select items from the sampleList like this 
print('Lists %s ' %sampleList)

#To no the length of string use len
string= 'I am a string'
string2='Mike b'
string3='UPPERCASE STRING'

print(len(string))
print(len(string2))

# To get the position of a particular letter in a string use index() function
print(string2.index('k'))

# To get the count of a letter in a string use count() function 
print(string2.count('e'))
print(string.count('a'))
print(string2.count('Mike'))
print(string2.count('o')) # o doesnt exist so it returns 0
print(string2.count(' ')) # It returns 1 which is the space i string2 

# To print sub string 
print(string[1:8])

#To convert string to upper case 
print(string.upper())

#You can also convert string to lower
print(string3.lower())

#You might revers a string like this 
print(string3[::-1])

#You can check if a string start with a particular term like this
print(string.startswith('I')) # True
print(string.startswith('p')) #False 

#And also check if a string ends with a particuar letter like this
print(string.endswith('string')) #True
print(string.endswith('shifrtr')) # False