#In data base we are able to perform CRUD operations which are:
#Create record
#Read record
#Update record
#Delete record

#In the databse operation ,add find user to enable search for user
import os #os allows us to delete a file in the os
import Validation


user_db_path='data/user_record/'


def create(user_account_number,first_name,last_name, email, password):

    # create a file
    #name of the file would be account.txt
    #add the user details to the file
    #return true 
    #if saving to file fails, then delete created file
    userData=first_name + ','+ last_name+ ',' +email+ ',' + password + ',' +str(0) 

    if does_account_number_exist(user_account_number):
        return False

    
    if does_account_number_exist(email):
        print('User already exists')
        return False 
    
    completion_state=False

    try:
        f=open(user_db_path + str(user_account_number)+ '.txt','x')
        
    except FileExistsError:
        
        does_file_contain_data=read(user_db_path + str(user_account_number)+ '.txt')
        if not does_file_contain_data:
            delete(user_account_number)

        #delete the already created file, and print out error, then return false
        #check content of file before deleting

        # delete(accountNumber)

    else: 
        f.write(str(userData))

        completion_state=True

    finally:
        f.close()
        return completion_state


    return completion_state



def read(user_account_number):
    
    #find user with account number
    #fetch content of the file 
    is_valid_account_number=Validation.account_number_validation(user_account_number)

    try:
        if is_valid_account_number:
            f=open(user_db_path + str(user_account_number)+ '.txt','r')
        else:
            f=open(user_db_path + user_account_number, 'r')


    except FileNotFoundError:

        print('User not found ')

    except FileExistsError:

        print('User doesnt exist')
    
    except TypeError:
        print('Invalide account number format ')

    else:

        return f.readline()

    return False 

def update(user_account_number):
    print('update user record')
    #find user with account number 
    #fetch the content of the file
    #update the content of the file
    #save the file 
    #return true


def delete(user_account_number):

    #find user with account number 
    #delete the user recod (file)
    #return true 
    
    is_delete_successful=False

    if os.path.exists(user_db_path + str(user_account_number)+'.txt'):

        try:

            os.remove(user_db_path+ str(user_account_number)+'.txt')
            is_delete_successful=True

        except FileNotFoundError:
            print('User not found')

        finally:
                
            return is_delete_successful

  
def does_email_exist(email):

    all_users = os.listdir(user_db_path)

    for user in all_users:

        user_list=str.split(read(user), ',')

        if email in user_list:

            return True

    return False


def does_account_number_exist(accountNumber):

    all_users = os.listdir(user_db_path)

    for user in all_users:
    

        if user == str(accountNumber)+ '.txt':

            return True

    return False

def authenticated_user(accountNumber,password):
    if does_account_number_exist(accountNumber):
        
        user=str.split(read(accountNumber), ',')
        
        if password == user[3]:
            return user 

    return False


# print(does_account_number_exist(5640311350))
# print(read(3614552875))
# print(read(6240930363))

# print(read({'roo':'too'}))