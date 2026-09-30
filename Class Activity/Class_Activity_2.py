class BankAccount:
    def __init__(self, acc_num, name, balance=0.0):
        # Private attributes (Encapsulation)
        self.__acc_num = acc_num
        self.__name = name
        self.__balance = 0.0
        self.set_balance(balance)  # Validate initial balance

    # Getter and Setter methods
    def get_acc_num(self):
        return self.__acc_num

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Error: Balance cannot be negative.")

    # Method overloading using *args (deposit single or multiple amounts)
    def deposit(self, *amounts):
        total = sum(a for a in amounts if a > 0)
        self.__balance += total
        print(f"Deposited: {total}. New Balance: {self.__balance}")

    # Withdraw method with balance validation
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. Remaining Balance: {self.__balance}")
        else:
            print("Error: Insufficient balance or invalid amount.")

    # Operator Overloading: + to combine balances
    def __add__(self, other):
        return self.__balance + other.__balance

    # Operator Overloading: == to compare account numbers
    def __eq__(self, other):
        return self.__acc_num == other.__acc_num

    # Operator Overloading: > to compare balances
    def __gt__(self, other):
        return self.__balance > other.__balance

    # Operator Overloading: __str__ to display account details
    def __str__(self):
        return f"Account[{self.__acc_num}] - Holder: {self.__name}, Balance: {self.__balance}"


# --- Demonstration ---

# 1. Create two BankAccount objects
acc1 = BankAccount(101, "Alice", 500)
acc2 = BankAccount(102, "Bob", 1000)

# Display initial details (__str__)
print(acc1)
print(acc2)

# 2. Method Overloading demonstration (deposit single vs multiple values)
acc1.deposit(200)           # Single amount
acc1.deposit(50, 100, 25)   # Multiple amounts via *args

# 3. Withdrawal demonstration with validation
acc1.withdraw(100)          # Valid
acc1.withdraw(2000)         # Invalid (exceeds balance)

# 4. Negative balance validation via setter
acc1.set_balance(-50)

# 5. Operator Overloading: + (combined balance)
total_funds = acc1 + acc2
print(f"Combined Balance (acc1 + acc2): {total_funds}")

# 6. Operator Overloading: == (compare account numbers)
print(f"Are acc1 and acc2 the same account? {acc1 == acc2}")

# 7. Operator Overloading: > (compare balances)
print(f"Does acc1 have more balance than acc2? {acc1 > acc2}")
print(f"Does acc2 have more balance than acc1? {acc2 > acc1}")
