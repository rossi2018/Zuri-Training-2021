#Build a list,check the name on the list, check against another list and get the index of the particular list 
name=input('What is your name? \n')
allowedUsers=['Rossi','James','Sandra']
allowedPassword=['passwordRossi','passwordJames','passwordSandra']

if name in allowedUsers:
    password=input('Your password? \n')
    userId=allowedUsers.index(name)
    if password==allowedPassword[userId]:
        print('Welcome %s'%name)
    else:
        print('Password Incorrect, please try again')

else:
    print('Name not found, please try again')