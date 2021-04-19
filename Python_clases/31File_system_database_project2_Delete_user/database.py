#In data base we are able to perform CRUD operations which are:
#Create record
#Read record
#Update record
#Delete record

#In the databse operation ,add find user to enable search for user
import os #os allows us to delete a file in the os

user_db_path='data/user_record/'


def create(accountNumber,userDetails):

    completion_state=False

    try:
        f=open(user_db_path + str(accountNumber)+ '.txt','x')
        
    except FileExistsError:
        print('User already exist')
        #delete the already created file, and print out error, then return false
        #check content of file before deleting

        # delete(accountNumber)

    else: 
        f.write(str(userDetails))
        completion_state=True

    finally:
        f.close()
        return completion_state


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
    
    is_delete_successful=False

    if os.path.exists(user_db_path + str(user_account_number)+'.txt'):

        try:

            os.remove(user_db_path+ str(user_account_number)+'.txt')
            is_delete_successful=True

        except FileNotFoundError:
            print('User not found')

        finally:
                
            return is_delete_successful

    #find user with account number 
    #delete the user recod (file)
    #return true 

def find(user_account_number):
    print('find user')
    # find user record in the data folder 

print(delete(3652386601))

