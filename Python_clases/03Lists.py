#A list contain different item while a variable single item
crate=['sand','water',7,5.9,True] #List, array 

print(crate) 

#If you want to select the first item in a list ,do it like this 
print(crate[0]) # Use 0 because list is an index starting from 0 to 1 e,g 0,1,2,3,4,5 etc

# You can add more value to this crate like this
crate.append('James')
print(crate)

#------------------Continuation of list from another python class--------------------------
#In python programming , a list is created by placing all the items (elements) inside square
#brackets [], separated by commas. It can have any bumber of items and they may be of different
#  types (integer, float,string etc.). A list can also have another list as an item. This is 
# nested list.

Zuri_Mentors=['Xylus','Motun','Prometheus','Bigdaddy','Tomisilalude','Toonie','Abbie',['John','James']]
print(Zuri_Mentors)

#-----------List operations---------------------

#append()- Adds an element at the of the list
Zuri_Mentors.append('Jovialcore')
print(Zuri_Mentors)

Zuri_Mentors.append(4)
print(Zuri_Mentors)
# Append() fucton accept only one argument like the above example

#clear() - Removes all the element from the list
Zuri_Mentors.clear()
print(Zuri_Mentors)

#copy()- Returns a copy of the list
Zuri_Mentors2=['Xylus','Motun','Prometheus','Bigdaddy','Tomisilalude','Toonie','Abbie',['John','James']]
Zuri_Mentors2.copy()
print(Zuri_Mentors2)

#count() - Returns the number of elements with the specified value

print(Zuri_Mentors2.count('Bigdaddy'))
print(Zuri_Mentors2.count('B'))  # It will not show any thing except an exact word match
print(Zuri_Mentors2.count('bigdaddy'))

# index()- Returns the index of the first element with the specified value
print(Zuri_Mentors2.index('Motun'))
print(Zuri_Mentors2.index('Bigdaddy'))

#insert() - Adds an element at the specified position
#Insert use index number to add an element like this 

Zuri_Mentors2.insert(0, 'Rossi')
print(Zuri_Mentors2)

Zuri_Mentors2.insert(1,'Alex')
print(Zuri_Mentors2)

#pop() - Removes the element at the specified position using the index number
Zuri_Mentors3=['Xylus','Motun','Prometheus','Bigdaddy','Tomisilalude','Toonie','Abbie',['John','James']]
print(Zuri_Mentors3.pop(1))
print(Zuri_Mentors3) # Printed the list out and Motun is removed from the list

#reverse - Reverses the order of the list
Zuri_Mentors4=['Xylus','Motun','Prometheus','Bigdaddy','Tomisilalude','Toonie','Abbie',['John','James']]
Zuri_Mentors4.reverse()
print(Zuri_Mentors4)

#sort()- sorts the list 
Zuri_Mentors5=['Xylus','Motun','Prometheus','Bigdaddy','Tomisilalude','Toonie','Abbie','John','James']

Zuri_Mentors5.sort()
print(Zuri_Mentors5)

Zuri_Mentors6=['Xylus','Motun','Prometheus','Bigdaddy','Tomisilalude','Toonie','Abbie','56','87','80','90']
Zuri_Mentors6.sort()
print(Zuri_Mentors6)




