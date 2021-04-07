# Things needed for registeration are
#-username,passwprd,email
#-generate user account 

#Things needed for login
#- (username or email) and password

#Then finally bank operations

#Inializing the system 
database={}

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
    print('this is the login function')

def register():
    print('this is register function')

def bankOperation():
    print('some operations')

def generationAccountNumber():
    print('Account number generator')

### ACTUAL BANKING SYSTEM ###

init()