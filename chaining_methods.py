class User:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.account_balance=0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)

tom = User("Tom", "35")
sam = User("Sam", "25")
jim = User("jim", "30")

tom.make_deposit(200).make_deposit(300).make_deposit(500).make_withdrawal(800).display_user_balance()
sam.make_deposit(300).make_deposit(500).make_deposit(1000).make_withdrawal(1000).display_user_balance()
jim.make_deposit(400).make_deposit(1200).make_deposit(400).make_withdrawal(1800).display_user_balance()
