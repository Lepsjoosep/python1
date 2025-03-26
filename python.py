# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    Returns 0 if the list is empty to avoid division by zero.
    """
    return sum(numbers) / len(numbers) if numbers else 0

# Class representing a simple bank account
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        """Get the current account balance"""
        return self.balance

# List of dictionaries representing students
students = [
    {"name": "Alice", "age": 22, "grade": 85},
    {"name": "Bob", "age": 20, "grade": 92},
    {"name": "Charlie", "age": 21, "grade": 78}
]

# Demonstrating list comprehension and filtering
high_performers = [student for student in students if student['grade'] >= 80]

# Using the function and class
print("Average grade:", calculate_average([s['grade'] for s in students]))

# Create a bank account and demonstrate its methods
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(f"{account.account_holder}'s balance: ${account.get_balance()}")

# Simple error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Using f-strings and formatting
for student in high_performers:
    print(f"{student['name']} is a high performer with grade {student['grade']}")
