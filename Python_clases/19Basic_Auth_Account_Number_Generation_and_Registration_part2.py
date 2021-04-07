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

    isValidOptionSelected=False
    print('Welcome to bankPHP')

    while isValidOptionSelected==False:

        haveAccount=int(input('Do you have account with us: 1 (yes) 2(No)\n'))

        if haveAccount==1:
            isValidOptionSelected=True
            login()
        elif haveAccount==2:
            isValidOptionSelected=True
            register()
        else:
            print('You have selected invalid option')



def login():
    print('Login to your account')

    bankOperation()

def register():
    print('**************Register****************')
    email=input('What is youremail address?\n')
    first_name=input('What is your first name?\n')
    last_name=input('What is your last name?\n')
    password=input('Create password for yourself \n')

    accountNumber=generationAccountNumber()

    database[accountNumber]=[first_name,last_name,email,password]

    print('Your account has been created ')

    # return database (used this piece of code to test my database)

    login()


def bankOperation():
    print('some operations')

def generationAccountNumber():

    
    return random.randrange(1111111111,9999999999)

### ACTUAL BANKING SYSTEM ###

init()