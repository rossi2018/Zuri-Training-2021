import datetime
e=datetime.datetime.now()

name=input('What is your name\n')
print(e.strftime('Date %Y-%m-%d  Time %H:%M:%S'))
allowedUser=['Rossi','Toria','Emma']
allowedPassword=['passwordRay','passwordRay','passwordRay']

if name in allowedUser:
    password=input('Your password \n')
    userId=allowedUser.index(name)

    if password==allowedPassword[userId]:
        print('Welcome %s' % name)
        print('1. Withdrawal')
        print('2. Cash Deposite')
        print('3. Complaint')

        selectionOption=int(input('Please select an option:'))
        if selectionOption==1:
            print('How much would you like to withdraw?')
            int(input('Amount:'))
            print('Take cash')
        elif selectionOption==2:
            print('How much would you like to deposit?')
            int(input('Amount in Number:'))
            print('Current balance')
        elif selectionOption==3:
            print('What issue will you like to report?')
            str(input('Complaint:'))
            print('Thank you for contacting us')

    else:
        print('Password option selected, please try again')

else:
    print('Name not found,please try again')

