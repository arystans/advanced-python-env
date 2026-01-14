class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def dep(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("No funds")
        self.__balance -= amount

    def balance(self):
        return self.__balance


account = BankAccount("Alice", 1000)
d = int(input("Enter your deposit amount: "))
account.dep(d)
w = int(input("Enter your withdrawal amount: "))
account.withdraw(w)
print(account.balance())
