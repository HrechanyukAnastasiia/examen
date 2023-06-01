#11
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Гроші успішно додано. Новий баланс:", self.balance)
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Гроші успішно знято. Новий баланс:", self.balance)
        else:
            print("Недостатньо коштів на рахунку!")

account1 = BankAccount("1506856570", 2000)
account1.deposit(50)
account1.withdraw(50)