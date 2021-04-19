#What is a module in python: A module is a Python object with arbitrarily named attributes that you can bind 
# and reference. ... Simply, a module is a file consisting of Python code. A module can define functions, 
# classes and variables.

#Consider a module to be the same as a code library.A file containing a set of functions you want to include 
# in your application or other codes to be used.

#-------------Create a module--------------------------------------
#To create a module just save the code you want in a file with the file extension .py:

#-------------use the module--------------------------------------
#Now we can use the module we just created, by using the import statement:

import Validation
import random
import database

# database={
#     8087466639:['Rossi','Otali','rotali77@gmail.com','password',0]
# } #Dictionary 

def init():
    print('Welcome to bankPHP')
  
    haveAccount=int(input('Do you have account with us: 1 (yes) 2(No)\n'))

    if haveAccount==1:

        login()

    elif haveAccount==2:
        
        register()

    else:
        print('You have selected invalid option')
        init()


def login():
    print('***********Login*************')

   
    accountNumberFromUser=input('What is your account number?\n')

    is_valid_account_number= Validation.account_number_validation(accountNumberFromUser)

    if is_valid_account_number: 

        password=input('What is your password \n')

        for accountNumber,userDetails in database.items():
            if accountNumber==int(accountNumberFromUser):
                if userDetails[3]==password:
                    bankOperation(userDetails)
        
        print('Invalid account or password')
        login()
    else:
        init()


def register():
    print('**************Register****************')
    
    email=input('What is your email address?\n')
    first_name=input('What is your first name?\n')
    last_name=input('What is your last name?\n')
    password=input('Create password for yourself \n')

    
    accountNumber=generationAccountNumber()
        
     
    # database[accountNumber]=[first_name,last_name,email,password]
    is_user_created=database.create(accountNumber,[first_name,last_name,email,password])

    #Using database module to create new user record 
    if is_user_created:
        print('Your account has been created ')
        print('------------------------------')
        print('Your account number is: %d . Keep it safe'%accountNumber)
        print('===============================')
        # return database (used this piece of code to test my database)

        login()
    else:
        print('Something went wrong, please try again')
        register()

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
    #get current balance
    #get amount to withdraw
    #check if current balance > withdraw balance 
    #deduct withdraw amount from current balance
    #display current balance 



def depositOperation():
    print('Deposite Operations')
    #get current balance
    #get amount to deposite
    #add deposited  amount to current balance
    #display current balance 

def generationAccountNumber():
    return random.randrange(1111111111,9999999999)


def set_current_balance(userDetails,balance):
    user_details[4]=balance


def get_current_balance(userDetails):
    return userDetails[4]


def logout():
    login()


### ACTUAL BANKING SYSTEM ###

init()