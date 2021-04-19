def account_number_validation(accountNumber):
    #check if account number is not empty
    #check if account number is 10 digits
    #check if the accountNunber is an integer
    if accountNumber:

        
        try:
            int(accountNumber)
            if len(str(accountNumber))==10:
                
                return True
        
            
        except ValueError:
                       
            return False
            
        except TypeError:
                   
            return False
      
        
    return False

