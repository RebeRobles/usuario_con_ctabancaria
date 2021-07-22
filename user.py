from bankAccount import BankAccount

class User:
    def __init__(self, username, email_address, accounts):
        self.name = username			
        self.email = email_address		
        self.accounts = accounts

    def make_deposit(self, indice, amount):	
        self.accounts[indice].deposit(amount)
        return self

    def make_withdrawal(self, indice, amount):
        self.accounts[indice].withdraw(amount)
        return self

    def display_user_balance(self):
        print(f'Usuario: {self.name}')
        for i in self.accounts:
            i.display_account_info()


    def transfer_money (self, other_user, indice, amount):
        if amount > self.accounts[indice].balance:
            print('No existe saldo suficiente para su retiro')
        else:
    	#    self.account.balance -= amount
        #    other_user.account.balance += amount 
            self.accounts[indice].balance -= amount
            other_user.accounts[indice].balance += amount
        return self 

    # dado por defecto la cuenta de transferencia
    # def transfer_money (self, other_user, amount):
    #     if amount > self.accounts[0].balance:
    #         print('No existe saldo suficiente para su retiro')
    #     else:
    #         self.accounts[0].balance -= amount
    #         other_user.accounts[0].balance += amount
    #     return self

     
user1 = User('Bruce', 'bruce@example.com', [BankAccount(0.01, 100000), BankAccount(0.002, 80000)])
user2 = User('Chris', 'chris@coldplay.uk', [BankAccount(0.01, 1000), BankAccount(0.002, 80000)] )
user1.make_deposit(0, 1000).make_deposit(1, 10000).transfer_money(user2, 1, 10000).display_user_balance()
user2.display_user_balance()