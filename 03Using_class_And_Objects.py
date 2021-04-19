#Task Title: Python: Classes and Objects
#Budget App

#Create a Budget class that can instantiate objects based on different budget categories like food, clothing, 
#and entertainment. These objects should allow for
#1.  Depositing funds to each of the categories
#2.  Withdrawing funds from each category
#3.  Computing category balances
#4.  Transferring balance amounts between categories

class budget:
    def __init__(self,food,clothing,entertainment):
        self.food=food
        self.clothing=clothing
        self.entertainment=entertainment

    @classmethod
    def from_input(cls):
        return cls(
            int(input('food budget:')),
            int(input('clothing budget:')),
            int(input('entertainment budget:')),
            
                  )
    #Add  error exception handling              
            

    @classmethod
    def with_draw_funds(cls):
        return cls(
            int(input('Food: ')),
            int(input('Clothing: ')),
            int(input('Entertainment: '))
        )


    @classmethod
    def compute_balance(cls):
        pass 
        
budget.from_input()
print('Withdraw Funds from ------------------------------------------')
budget.with_draw_funds()