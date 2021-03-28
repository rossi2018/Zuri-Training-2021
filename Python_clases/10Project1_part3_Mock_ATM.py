# Extending the application to a typical ATM style  option after they have log in 
#The options will include : Withdrawal,Deposite and complaint
name=input('What is your name? \n')
allowedUsers=['Rossi','James','Sandra']
allowedPassword=['passwordRossi','passwordJames','passwordSandra']

if name in allowedUsers:
    password=input('Your password \n')
    userId=allowedUsers.index(name)

    if password==allowedPassword[userId]:
        print('Welcome %s'% name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposite')
        print('3. Complaint')

        selectedOption=int(input('Please select an option:'))

        if selectedOption==1:
            print('You selected %s'% selectedOption)
        elif selectedOption==2:
            print('You selected %s' % selectedOption)
        elif selectedOption==3:
            print('You selected %s' % selectedOption)
        else:
            print('Invalide option selected,please try again ')
    
    else:
        print('Password option selected, please try again')

else:
    print('Name not found,please try again')
