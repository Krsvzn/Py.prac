class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,money):
        if money > 0:
         self.balance += money
        else:
         print("\nNegative or Zero Amount Is Not Permitted.")
    
    def withdraw(self,money):
        if self.balance >= money:
         self.balance -= money
        else:
         print("\nNot Enough Balance To Withdraw.\nTransaction Failed.")
    
    def show_balance(self):
        print(self.balance)

my_account = Account("batman", 1000)

my_account.deposit(500)

my_account.withdraw(200)

my_account.show_balance()


