class BankAccount:

	def __init__(self, int_rate = 0.01, balance = 0):
            self.int_rate = int_rate
            self.balance = balance

	def deposit(self, amount):
            self.balance += amount
            return self
		
	def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
            else:
                print('Fondos insuficientes: cobrar una tarifa de $5')
                self.balance -= 5
            return self

	def display_account_info(self):
            print(f'Saldo de: $ {self.balance}')

	def yield_interest(self):
            if self.balance > 0:
                self.balance += (self.balance * self.int_rate)
            return self
