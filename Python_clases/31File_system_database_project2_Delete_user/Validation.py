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

