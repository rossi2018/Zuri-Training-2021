#Turples - Turples are used to store multiple items in a single variable. A tuple is a 
# collection which is order and unchangeable. A tuple is similar to a list but immutable

#Tuples are written with round brackets ()
Zuri_Interns=('Jack','John','Jane') #Example of turples
print(Zuri_Interns)

#Difference between string and turple
#A string is a sequence of values which can be characters, intergers or even another list
string='Am interested in python backend programming using django'
print(string)

#A turple is a sequence of values (any type) which makes them similar to list,but the 
#difference is they immutable
Turples=('Matriculation','Wednesday','DSPG','Mummy')
print(Turples)

#You can get the length of turples,list and string using len() function
print(len(Turples))

print(len(string))

#The difference between turple and list is that list are mutable that means that you can 
#change the order of list like this
currency=['Naira','Cedis','Dollars']
currency[0]='Pounds'
print(currency) #Change Naira to pounds which means that list mutable 

#Example to see that turples are immutable
currency2=('Naira','Cedis','Dollars')
currency2[2]='Euros'
print(currency2) #You get an error saying object does not support item assignment 
