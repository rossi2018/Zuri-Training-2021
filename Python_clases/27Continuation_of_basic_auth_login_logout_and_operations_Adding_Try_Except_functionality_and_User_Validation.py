# Things needed for registeration are
#-first name,last name,passwprd,email
#-generate user account 

#Things needed for login
#- account number & password

#Then finally bank operations

#Inializing the system 
import random
database={
    8087466639:['Rossi','Otali','rotali77@gmail.com','password',0]
} #Dictionary 

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

   
    accountNumberFromUser=input('What is your account number?\n')

    is_valid_account_number= account_number_validation(accountNumberFromUser)

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



    
def account_number_validation(accountNumber):
    #check if account number is not empty
    #check if account number is 10 digits
    #check if the accountNunber is an integer
    if accountNumber:

        if len(str(accountNumber))==10:

            try:
                int(accountNumber)
                return True
            except ValueError:
                print("Invalide Account number,account number should be integer")
                return False
            except TypeError:
                print("Invalid account type")
                return False
            

        else:
            print('Account Number cannot be less than or more than 10 digits')
            return False

    else:
        print('Account Number is a required field')
        return False



def register():
    print('**************Register****************')
    email=input('What is your email address?\n')
    first_name=input('What is your first name?\n')
    last_name=input('What is your last name?\n')
    password=input('Create password for yourself \n')


    try:
        accountNumber=generationAccountNumber()
        
    except ValueError:
        print('Account generation failed due to internet connection failure')
        init()

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
