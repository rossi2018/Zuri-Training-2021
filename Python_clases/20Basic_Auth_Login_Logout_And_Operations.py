# Things needed for registeration are
#-first name,last name,passwprd,email
#-generate user account 

#Things needed for login
#- account number & password

#Then finally bank operations

#Inializing the system 
import random
database={} #Dictionary 

def init():
    print('Welcome to bankPHP')
  
    haveAccount=int(input('Do you have account with us: 1 (yes) 2(No)\n'))

    if haveAccount==1:
        
        login()
    elif haveAccount==2:
        
        register()
    else:
        print('You have selected invalid option')



def login():
    print('***********Login*************')

   
    accountNumberFromUser=int(input('What is your account number?\n'))
    password=input('What is your password \n')

    for accountNumber,userDetails in database.items():
        if accountNumber==accountNumberFromUser:
            if userDetails[3]==password:
               bankOperation(userDetails)
    
    print('Invalid account or password')
    login()

def register():
    print('**************Register****************')
    email=input('What is your email address?\n')
    first_name=input('What is your first name?\n')
    last_name=input('What is your last name?\n')
    password=input('Create password for yourself \n')

    accountNumber=generationAccountNumber()

    database[accountNumber]=[first_name,last_name,email,password]

    print('Your account has been created ')
    print('------------------------------')
    print('Your account number is: %d . Keep it safe'%accountNumber)
    print('===============================')
    # return database (used this piece of code to test my database)

    login()


def bankOperation(user):

    print('Welcome %s %s'% (user[0],user[1])) 

    selectedOption=int(input('What would you like to do? (1) Deposite (2) WIthdrawal (3) Logout (4) Exit\n'))

    if selectedOption==1:
            
        depositOperation()

    elif selectedOption==2:
            
        withdrawalOperation()

    elif selectedOption==3:
           
        logout()

    elif selectedOption==4:
            
        exit()

    else:
        
        print('Invalid option selected')
        bankOperation(user)


def withdrawalOperation():
    print('WIthdrawal')

def depositOperation():
    print('Deposite Operations')


def generationAccountNumber():
    return random.randrange(1111111111,9999999999)

def logout():
    login()


### ACTUAL BANKING SYSTEM ###

init()