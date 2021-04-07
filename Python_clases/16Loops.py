# In computer science, a loop is a programming structure that repeats a sequence of instructions until a 
# specific condition is met. Programmers use loops to cycle through values, add sums of numbers, 
# repeat functions, and many other things. ... Two of the most common types of loops are the while loop 
# and the for loop.

#For loop - The for loop happen for a given period of time in the sense that they terminate 
#The for loop in Python is used to iterate over a sequence (list, tuple, string,dictionary,set) or other 
# iterable objects. 
# For loop is used when you have no idea how long the program will keep running 

#A way to print out all the names in the list using for loops
names=['xylux','Toonie','Big daddy']

if isinstance(names,list):
    for name in names:
        print(name)

print('using for loop to alterate character -----------------------------------------')
#A way to print out all character in a string
for char in 'Mosquitoes':
    print(char)

print('Another loop examples .........................................................')
alist=[1,2,3,4,5,6,7]
for item in alist:
    print(item)

print('Additional for loop example ---------------------------------------------------')
for x in range(5):
    print(x)

print('Using if statement and for loops to elimite zero from range function -----------')
for x in range(6):
    if(not(x==0)):
        print(x)
#in for loop,we can use statements like break,continue and pass
print('Using break statment -----------------------------------------------------------')
#break - the break statement provides you with the opportunity to exit out of a loop when an external
#  condition is triggered. You’ll put the break statement within the block of code under your loop statement,
# usually after a conditional if statement.

for char in 'Mosquitoes':
    if char == 'u':
        break
    print(char)

#break statement-
print('Exaple of break statement --------------------------------------------------------')
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter', letter)

#Another example of break statement
print('Another examle of break statement-------------------------------------------------')
var=10
while var>0:
    print('Current variable value:',var)
    var=var-1
    if var==5:
        break

    print('Good byr!')

print('Using the pass statement ------------------------------------------------------')
#pass  statement - Python pass is a null statement. When the Python interpreter comes across the statement, 
# it does nothing and is ignored.

for char in 'Mosquitoes':
    if char == 'u':
        pass
    print(char) # The full character of 'Mosquitoes' including the u is printed out ignoring the equality sign (==)

print('Another exaplme of pass statement-----------------------------------------------')
#Another example of pass statement inside the loop

test='Guru'
for i in test:
    if i=='r':
        print('pass executed')
        pass
    print(i)

print('Example of continue statement---------------------------------------------------------')
# continue statement- The continue statement rejects all the remaining statements in the current iteration 
# of the loop and moves the control back to the top of the loop


for letter in 'Python':     
   if letter == 'h':
      continue
   print ('Current Letter :',letter)

print('Another example to demonstrate how continue statement work-----------------------------')
var=10
while var>0:
    var=var-1
    if var ==5:
        continue
    print('current variable value:',var)
print('Good bye')

print('Python looping through a range--------------------------------------------------------------')
#range() function -To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
#  and ends at a specified number.

for x in range(6):
    print(x) #Note that range(6) is not the values of 0 to 6, but the values 0 to 5

print('Another example of range specifying the start point--------------------------------------------')
#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by
#  adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2,6):
    print(x)


print('Example of range specifying the increment value------------------------------------------------')
#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment
#  value by adding a third parameter: range(2, 30, 3):

for x in range(2,30,3):
    print(x)

print('adding else statment to for loop ----------------------------------------------------------------')
# You can add else statement to for loop like this
for r in range(5,500,100):
    print(r)
else:
    print('Processing done')


print('Nested for loop===================================================================================')
#Nested for loop-A nested loop is a loop that occurs within another loop.
# The program first encounters the outer loop, executing its first iteration. This first iteration triggers 
# the inner, nested loop, which then runs to completion. Then the program returns back to the top of the 
# outer loop, completing the second iteration and again triggering the nested loop. Again, the nested loop
#  runs to completion, and the program returns back to the top of the outer loop until the sequence is complete 
# or a break or other statement disrupts the process.

food_1=['White_rice','Spaghetty','Beans']
food_complement=['stem','egg','bread']

for food in food_1:
    for completement in food_complement:
        print(food,completement)
        # You can add other for loop here like 3 or 4 or more but its a bad practice as it will make your 
        # code slow

else:
    print('Loop processing done!')


print('Enumeration function ----------------------------------------------------------------------------')
#enumeration() function - The enumerate() function takes a collection (e.g. a tuple) and returns it as 
# an enumerate object.The enumerate() function adds a counter as the key of the enumerate object

food_2=['white_rice','spaghetti','beans']

for index, food in enumerate(food_2):
    print('Index-> {}, Value {}' .format(index,food))

print('while loop --------------------------------------------------------------------------------------')
#while loop - With the while loop we can execute a set of statements as long as a condition is true.
count=5

while count > 0:
    print(count)
    count-=1