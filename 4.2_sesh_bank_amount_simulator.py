class Account:

    def __init__(self,owner,balance):

        self.owner = owner

        self.balance = balance



    def deposit(self,money):

        self.balance += money

   

    def withdraw(self,money):

        self.balance -= money

   

    def show_balance(self):

        print(self.balance)



my_account = Account("batman", 1000)



my_account.deposit(500)



my_account.withdraw(200)



my_account.show_balance()
