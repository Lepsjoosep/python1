
def calculate_average(numbers):

    return sum(numbers) / len(numbers) if numbers else 0


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance

students = [
    {"name": "Alice", "age": 22, "grade": 85},
    {"name": "Bob", "age": 20, "grade": 92},
    {"name": "Charlie", "age": 21, "grade": 78}
]


high_performers = [student for student in students if student['grade'] >= 80]


print("Average grade:", calculate_average([s['grade'] for s in students]))


account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(f"{account.account_holder}'s balance: ${account.get_balance()}")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

for student in high_performers:
    print(f"{student['name']} is a high performer with grade {student['grade']}")
