class Customer:
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance
        self.penalty = 0

    def total_balance(self):
        """Print the balance left in the bank account"""
        print("The current balance is:", self.balance)

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            self.widthdraw_with_penalty(amount)
        else:
            self.balance -= amount
        return self.balance

    def widthdraw_with_penalty(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        fixed_penalty = 5
        self.balance -= (amount + fixed_penalty)
        self.penalty += 5
        print("The balance of your account is negative!")

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

def main():
    customer1 = Customer("marcello", 1500)
    customer1.deposit(600)
    customer1.withdraw(500)
    customer1.withdraw(1800)
    customer1.total_balance()

#just execute if this is the main file (where the play button was pressed)
if __name__ == "__main__":
    main()


