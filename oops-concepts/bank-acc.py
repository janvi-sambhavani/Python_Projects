class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
        else:
            print("Not enough balance!")

    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    acc_number = input("Enter account number: ")
    owner = input("Enter account owner name: ")
    acc = BankAccount(acc_number, owner, 0)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. View Transactions\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            amt = float(input("Enter amount to deposit: "))
            acc.deposit(amt)
        elif choice == "2":
            amt = float(input("Enter amount to withdraw: "))
            acc.withdraw(amt)
        elif choice == "3":
            print("Balance:", acc.get_balance())
        elif choice == "4":
            print("Transactions:", acc.transactions)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

