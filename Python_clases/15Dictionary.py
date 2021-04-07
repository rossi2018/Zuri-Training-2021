#Dictionary - Dictionary in Python is an unordered collection of data values, used to store data values
#  like a map, which unlike other Data Types that hold only single value as an element.

# Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized
#Dictionary is a collection of item which can be ordered or unordered 
#The benefit of using dictionary lets you get a value from a key at constant time i nthe sense that you 
# dont need to loop through a list of items for you to see a particular item you are looking for.
#We use  two curly braces {} to signify a dictionary

#We have two ways of representing dictionary
first_variable={}
second_variable=dict()
#Both are the same in that the second one you use dict() datatype 

#We can check the data type of both method
print(type(first_variable)) 
print(type(second_variable)) #Both have same data type

#How to get item in a dictionary 
fruit_basket={'mango':40,'oranges':30,'pawpaw':3}
print(len(fruit_basket))

#Its import to note that we dont have duplicate key in dictionary 
# fruit_basket2={'mango':40,'oranges':30,'pawpaw':40,'mango': 50} #Duplicate key like mango here is 
# not allowed in a dictionary

print('How to manually add value to a dictionary -----------------------------------------------------------')
dictionaryTwo={}

dictionaryTwo['key4']='value4'
dictionaryTwo['key5']='value5'
dictionaryTwo['key6']='value6'
print(dictionaryTwo)

print('How to delete from dictionary -----------------------------------------------------------------------')
dictionaryThree={'key1':'value1',
                  'key2':'value2',
                  'key3':'value3'}

del dictionaryThree['key1']
print(dictionaryThree)
print('Another way to delete from dictionary is by using pop===============================================')

dictionaryFour={'Data1':'Value1',
                'Data2':'Value2',
                'Data3':'Value3',
                'Data4':'Value4'}

dictionaryFour.pop('Data1')
print(dictionaryFour)

print('How to loop through the item in a dictionary=========================================================')
dictionaryFive={'Data1':'Value1',
                'Data2':'Value2',
                'Data3':'Value3',
                'Data4':'Value4'}

for key,value in dictionaryFour.items():
    print('I have ' + key + ' relating with ' + value)


#You can also include a list as value to a key like this
fruit_basket={
    'mango':40,
    'orange':30,
    'pawpaw':3,
    'banana':[40,50.60,70]
}

print(fruit_basket['mango'])

#To know if a variable is a dictionary ,you use isinstance() function like this
print(isinstance(fruit_basket,dict)) #True

#You check too if its an instance of a list like this
print(isinstance(fruit_basket,list)) #False 

#You can access dictionary values by using their key
mangoes=fruit_basket['mango']
print('we have {} mangoes'.format(mangoes))

#In dictionary you must specify the key to access the value.Normally if the key is not available ,
# it  returns a error.They is a way to make it not to display the error using get() method in python 

#This is the syntax using get() method
#dict.get(key,default=None)
#Example
dic={'A':1,'B':2}

print(dic.get('A'))
print(dic.get('B'))
print(dic.get('c'))
print(dic.get('c','Not Found !'))

#Another example of using get

fruit_basket2={
    'mango':40,
    'orange':30,
    'pawpaw':3,
    'banana':[40,50.60,70]
}
mangoes=fruit_basket2.get('apple',None)
print('We have {} mangoes'.format(mangoes))

#How to see all the keys in a dictionary?
all_fruit_keys=fruit_basket2.keys()
print(all_fruit_keys)

#We can update the value for a particular key like this 
new_fruit_basket=fruit_basket2['mango']-1
print(new_fruit_basket)

#Or we can update it like this
print('original fruit basket',fruit_basket2) #Original fruit_basket2

fruit_basket2['mango']=fruit_basket2['mango']-1
print(fruit_basket2) #updated fruit_basket2 by removing 1 from mango making it 49

#We can update our dictionary to add new object like this 
fruit_basket2.update({'oragne':100})
print(fruit_basket2) #orange has been addded to the fruit_basket2

#We can decide to get item of a dictionary whic returns the key and values
print(fruit_basket2.items()) #It list out all the item of frui_basket2

#We can check if a key exist in a particular dictionary using if statement
if 'mango' in fruit_basket2:
    print('Mango is key value in fruit basket2')
    

#How to remove an itmen from dictionary using pop() 
fruit_basket.pop('banana')
print(fruit_basket) #banana has been removed from the item

#Using delete(del) and clear
# del fruit_basket2['orange']  #What del does is removing item in dictioanry permanently without 
# any refernce to the deleted item. In this case it deleted orange permanently from fruit_basket

#Using clear()- is better option compared to del in the sense that you can have reference to cleared 
#item
fruit_b=fruit_basket2.clear()
print(fruit_b) #It returns None but the fruit_basket2 can be acess

#Copying and referencing dictionary dictionary have similarity and differences 

#Using assignment = operator  simply serve as a pointer and not copy because it a reference 

fruit_basket3={
    'mango':40,
    'orange':30,
    'pawpaw':3,
    'banana':{'bad':10,'good':44}
}

new_fruit_basket=fruit_basket3 #Using only assignmet operator = reference the dictionary 
print('New fruit Basket:',new_fruit_basket)
print('Fruit Basket', fruit_basket3) 

#To check memory address using Id to see if it copied or made reference to original file
print(id(fruit_basket3))
print(id(new_fruit_basket)) #Both printout have the same address meaning that the     
#new_fruit_basket is referencing fruit_basket3 which did not copy but referencing 
#the number displayed is the memory reference in the RAM
print('-------------------------------------------------------------')

#Shallow vs Deep Copying of Python Objects

#Shallow copy - A shallow copy means constructing a new collection object and then populating it with 
# references to the child objects found in the original. In essence, a shallow copy is only one level deep. 
# The copying process does not recurse and therefore won’t create copies of the child objects themselves.
#Example of shallow copy using copy() function 
new_fruit_basket=fruit_basket3.copy()
print('New fruit Basket:',new_fruit_basket)
print('Fruit Basket', fruit_basket3) #Both print out contain the same dictionary item

#To check memory address using Id to see if it copied or made reference to original file
print(id(fruit_basket3))
print(id(new_fruit_basket)) #Its has different memory addresse 

print('=============================================================')
#Adding/changing item in fruit_basket3 will still affect new_fruit_basket  because its 
#  a referenc to fruit_basket3
fruit_basket3['banana']['bad']=0
print('New fruit Basket:',fruit_basket3)
print('Fruit Basket', new_fruit_basket)

# Deep copying - A deep copy makes the copying process recursive. It means first
# constructing a new collection object and then recursively populating it with 
# copies of the child objects found in the original. Copying an object this way 
# walks the whole object tree to create a fully independent clone of the original
#  object and all of its children.

print('Deep-copy example ...........................................................')
#To use deep copy you need the copy module which is import copy
import copy

fruit_basket4={
    'mango':40,
    'orange':30,
    'pawpaw':3,
    'banana':{'bad':10,'good':44}
}

new_fruit_basket=copy.deepcopy(fruit_basket4)
print('New fruit Basket:',new_fruit_basket)
print('Fruit Basket', fruit_basket4)

print(id(fruit_basket4))
print(id(new_fruit_basket)) 

fruit_basket4['banana']['bad']=0
print('New fruit Basket:',fruit_basket3)
print('Fruit Basket', new_fruit_basket) #you will notice that the new_fruit_basket have the original 10
# while the fruit_basket have the added value.
