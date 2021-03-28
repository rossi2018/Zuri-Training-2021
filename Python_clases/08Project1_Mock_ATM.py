#A way to receive input from the user is by using input() function
#To star from the next line use \n
name=input('What is your name? \n')
allowedUers=['Rossi','Toria','Ada'] #List of allowed users 
AllowedPassword='Password'#Password is static for ni

if name in allowedUers:
    password=input('Your password? \n')
    if password==AllowedPassword:
        print('Welcome %s' %name)
    else:
        print('Password Incorrect, please try again')

else:
    print('Name not found, please try again')