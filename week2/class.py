
# 1. Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
    
person1 = Person("deepanshu", 87)
print(person1)

# 2. Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, customer_name, account_number, opening_balance):
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = opening_balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"{amount}rs deposited, current balance is {self.balance}rs")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        print(f"{amount}rs withdrawn, current balance is {self.balance}")

    def check_balance(self):
        print(f"current balance is {self.balance}rs") 
account = BankAccount("Alice", "ACC101", 1000)

account.check_balance()
account.deposit(500)
account.withdraw(300)
account.check_balance()
try:
    account.withdraw(2000)
except Exception as e:
    print("Error:", e)

try:
    account.deposit(-100)
except Exception as e:
    print("Error:", e)


# 3. Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def from_string(title_with_author):
        title, author = [item.strip() for item in title_with_author.split(",")]
        return Book(title, author)
    
    def __str__(self):
        return f"{self.title}, {self.author}"
    
book = Book.from_string("Python Programming, John Doe")
print(book)

# 4. Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.
class Animal:
    def sound(self):
        raise NotImplementedError

class Dog(Animal):
    def sound(self):
        return "bhau"

class Cat(Animal):
    def sound(self):
        return "mao"
dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())
# 5. Write a code to perform multiple inheritance.
class Flyer:
    def fly(self):
        return "chidiya ud"

class Swimmer:
    def swim(self):
        return "swim swim swim"

class Duck(Flyer, Swimmer):
    def sound(self):
        return "quack"

duck = Duck()
print(duck.fly())
print(duck.swim())
print(duck.sound())