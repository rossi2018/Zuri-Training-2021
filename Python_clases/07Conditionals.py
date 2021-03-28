#Conditional 
#Conditional represent an expression that would only be executed when a certain condition is met 
# If acondition is not met you can alson set it to do other thing

#sample of movie theatre allowing only 18 years of age to watch movie

age=17 #You can change the age to 18 and above to see different output
movie= 'Avengers End Game'
if age > 18:
    print('Customer can purchase ticket for movie:' + movie)

#Return a message if the first condition of 18 above is not met 
if age < 18:
    print('customer is not allowed to watch ' + movie) # True


# and conditional
#and: The and condition is when two conditions must be true for the test to pass
#or: The or condition require only one condition to be true for the test to pass

age2= 18
height=5

if age2 >=18 and height >= 5:
    print('Person can get on this rie')

elif age2 < 18 or height < 5:
    print('Person cannot get on this ride') #True

else:
    print('Error, something went wrong with your inputs')

# With all the conditional(if,elif and else) the program goes from the top to bottom
