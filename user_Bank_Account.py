class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        # your code here
        self.balance+=amount
        return self
    def withdraw(self, amount):
        # your code here
        if(self.balance<amount):
            print("Insufficient Funds: Charging a $5 fee")
            self.balance-=5
        else:
            self.balance+=amount
        return self
    def display_account_info(self):
        # your code here
        print('Balance: '+str(self.balance))
        return self
    def yield_interest(self):
        # your code here
        if(self.balance>0):
            self.balance*=self.int_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)
    # other methods
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    # your code here
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        self.account.display_account_info()

user1=User('jimmy','test')
user1.make_deposit(80)
user1.display_user_balance()