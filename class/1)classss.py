class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # fixed typo

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

s1 = Student('Zunaisha', 21, 'A+')
s1.display_info()  # added ()





import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius
c1 = Circle(5)
print("Area:", c1.area())                  # Output: ~78.54
print("Circumference:", c1.circumference())  # Output: ~31.42




class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully.")
        else:
            print("Enter a valid amount to deposit.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount} successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")
acc1 = BankAccount("Zunaisha")
acc1.deposit(1000)
acc1.withdraw(300)
acc1.display_balance()
