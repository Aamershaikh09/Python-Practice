#static method

# class hello():
#     @staticmethod
#     def college():
#         print("hello world")

# s1=hello()
# s1.college()
'''
create account class with 2 attributes - balance & account no. 
create methods for debit ,
creadit & printing the banalnce
'''
class Account():
    def __init__(self,Balance,Account_no):
        self.Balance=Balance
        self.Account_no=Account_no

    def debit(self,amount):
        self.Balance-=amount
        print("rs",amount, "debited")
        print("your current balance: ",self.check_balance())

    def credit(self,amount):
        self.Balance+=amount
        print("rs",amount, "creadited")
        print("your current balance: ",self.check_balance())

    def check_balance(self):
        return self.Balance

s1=Account(1000,11235)
s1.debit(500)
s1.credit(100)
s1.check_balance()

