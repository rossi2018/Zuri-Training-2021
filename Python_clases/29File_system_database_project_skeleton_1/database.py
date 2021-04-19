#In data base we are able to perform CRUD operations which are:
#Create record
#Read record
#Update record
#Delete record

#In the databse operation ,add find user to enable search for user

def create(accountNumber,userDetails):

    completion_state=False

    try:
        f=open('data/user_record/'+ str(accountNumber)+ '.txt','x')
        
    except FileExistsError:
        print('User already exist')
        #delete the already created file, and print out error, then return false
        return completion_state

    else: 
        f.write(str(userDetails))
        completion_state=True

    finally:
        f.close()

    return completion_state

    # create a file
    #name of the file would be account.txt
    #add the user details to the file
    #return true 
    #if saving to file fails, then delete created file

def read(user_account_number):
    print('Read user account number')
    #find user with account number
    #fetch content of the file 

def update(user_account_number):
    print('update user record')
    #find user with account number 
    #fetch the content of the file
    #update the content of the file
    #save the file 
    #return true


def delete(user_account_number):
    print('delete user record')
    #find user with account number 
    #delete the user recod (file)
    #return true 

def find(user_account_number):
    print('find user')
    # find user record in the data folder 


