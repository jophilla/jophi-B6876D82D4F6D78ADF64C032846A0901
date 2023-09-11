# BankAccount class
class Bankaccount:
	def __init__(self):
# Function to deposit amount
def deposit(self):
		amount = float(input("Enter amount to be deposited: "))
		self.balance += amount
		print("\n Amount Deposited:", amount)
# Function to withdraw the amount
def withdraw(self):
		amount = float(input("Enter amount to be withdrawn: "))
		if self.balance >= amount:
			self.balance -= amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")
