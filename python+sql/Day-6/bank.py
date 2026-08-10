class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Withdrawn: ${amount}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")


class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > self.get_balance():
            print("Insufficient funds in savings account.")
        else:
            super().withdraw(amount)

    def add_interest(self, rate):
        interest = self.get_balance() * rate / 100
        self.deposit(interest)
        print(f"Interest added: ${interest}")


account = SavingsAccount("Varun", 10000)

print(f"Account holder: {account.account_holder}")
print(f"Initial balance: ${account.get_balance()}")

account.deposit(5000)
print(f"Balance after deposit: ${account.get_balance()}")

account.withdraw(3000)
print(f"Balance after withdrawal: ${account.get_balance()}")

account.add_interest(5)
print(f"Balance after adding interest: ${account.get_balance()}")