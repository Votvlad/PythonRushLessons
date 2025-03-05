"""
string = 'brothers'
number = 123
my_tuple = ('18', 24, 'Gustavo')

print(id(string))
print(id(number))
print(id(my_tuple))
print()
print(hash(string))
print(hash(number))
print(hash(my_tuple))
print()
print(dir(string))
print(dir(number))
print(dir(my_tuple))
"""

"""
list_1 = [1, 2, 3]
list_2 = ['Mike', 'Todd', 'Gus']
list_combo = zip(list_1, list_2)  #list_combo = list(zip(list_1, list_2))
print(list(list_combo))

list_num = [12, 567, 81, 9, -45]
print(max(list_num))
print(min(list_num))
print(sum(list_num))
"""

"""
numbs = [1, 2, 3, 4, 5]
squares = list(map(lambda x: pow(x, 2), numbs))
print(squares)
"""

"""
strings = ['better', 'call', 'saul']
sorted_strings = sorted(strings, key=lambda x: len(x))
print(sorted_strings)
"""

"""
def make_counter():
    count = 0
    count2 = 5
    def counter():
        nonlocal count
        count += 1
        return count
    def counter2():
        nonlocal count2
        count2 += 2
        return count2
    return counter, counter2

counter1, counter2 = make_counter()

print(counter1())
print(counter1())
print(counter2())
print(counter2())
"""

"""
def make_filter(threshold):
    def filter_func(value):
        return value > threshold
    return filter_func
   
filter_above_10 = make_filter(10)
filter_above_15 = make_filter(15)
data = [5, 10, 15, 20]
filtered_data = list(filter(filter_above_10, data))
filtered_data2 = list(filter(filter_above_15, data))
print(filtered_data)
print(filtered_data2)
"""

"""
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))
"""


"""
square_num = (pow(x, 2) for x in range(1, 11))
for value in square_num:
    print(value)
"""

#ДЕКОРАТОРЫ

"""
def log_decorator(func):
    def wrapper():
        print("Сообщение до выполнения функции")
        func()
        print("Сообщение после выполнения функции")
    return wrapper

@log_decorator
def greet():
    print('Hello, friend!')

greet()
"""

"""
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)

        return wrapper

    return decorator_repeat


@repeat(3)
def say_hello(name):
    print(f'Hello, {name}!')


say_hello('Kim')
"""

"""
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Before function call")
        result = func(*args, **kwargs)
        print("Decorator 1: After function call")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: Before function call")
        result = func(*args, **kwargs)
        print("Decorator 2: After function call")
        return result
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello, world!")
say_hello()
"""

"""
import time

def time_decorator(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time:.4f} секунд")
        return result
    return wrapper

@time_decorator
def compute_square(n):
    time.sleep(0.5)  # Имитация задержки
    return n * n

result = compute_square(5)
print(f"Результат вычисления: {result}")
"""


#Продвинутая работа с параметрами функций
"""
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(1, 2, 3)) 
# numbers = [1, 2, 3, 4, 5]
# print(sum_numbers(*numbers))
"""

"""
def print_person_info(**kwargs):
    for key, kwarg in kwargs.items():
        print(f"{key} : {kwarg}")
print_person_info(name = "Saul", age = "47", city = "Albuquerque")
"""

# Встроенные библиотеки

"""
import os
os.mkdir('test_directory')
os.chdir('test_directory')
with open("test_file.txt", "w") as f:
    f.write("Hello, World!")
with open("test_file.txt", "r") as f:
    content = f.read()
    print(content)
os.chdir("..")
os.remove("test_directory/test_file.txt")
os.rmdir("test_directory")
"""

"""
import platform

print("Operating System:", platform.system())
print("Node Name:", platform.node())
print("OS Version:", platform.version())
print("Architecture:", platform.architecture())
print("Python Version:", platform.python_version())
"""

# Библиотека datetime
"""
import datetime
#from datetime import date
year = int(input('Год рождения: '))
month = int(input('Месяц рождения: '))
day = int(input('День рождения: '))

birthday = datetime.date(year, month, day)

today = datetime.date.today()

days_since_birth = today - birthday
print(days_since_birth.days)
"""

"""
import datetime
utc_dt = datetime.datetime(2025, 3, 3, 3, 29,00, tzinfo=datetime.timezone.utc)
difference = int(input("Введите разницу в часах: "))
user_tz = datetime.timezone(datetime.timedelta(hours = difference))
user_dt = utc_dt.astimezone(user_tz)
print(utc_dt)
print(user_dt)
"""

# Создание классов и объектов
"""
class Car:
   def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
   def display_info(self):
       print(f"Автомобиль: {self.make} {self.model}, год выпуска {self.year}")

my_car = Car("Mercedes", "Maybach-S", 2025)
my_car.display_info()
"""

#Создание классов и объектов
"""
class Car:
   def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
   def display_info(self):
       print(f"Автомобиль: {self.make} {self.model}, год выпуска {self.year}")

my_car = Car("Mercedes", "Maybach-S", 2025)
my_car.display_info()
"""

"""
class Library:
    def __init__(self, books = None):
        self. books = books if books is not None else []
    #def __init__(self):
    #self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(self.books)
        #for book in self.books:
        #print(book)

my_book = Library()

my_book.add_book("Bible")
my_book.add_book("Alice in the Wonderland")
my_book.display_books()
"""

"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rectangle = Rectangle(17, 22)

print(rectangle.area())
"""

"""
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Сумма на счёте: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Сумма на счёте:{self.balance}")
        else:
            print("На счёте не достаточно средств")
            print(f"Сумма на счёте: {self.balance}")

account = BankAccount('12345', 1000)

account.deposit(500)
account.withdraw(2000)
"""

"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model

    def get_model(self):
        return self._model

    def set_model(self, new_model):
        self._model = new_model

car = Car('Toyota', 'Corolla')

print(car.get_model())
car.set_model("Camry")
print(car.get_model())
print(car.brand)
car.brand = 'Mercedes'
print(car.brand)
"""

"""
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return str(self.books)

    def __len__(self):
        return len(self.books)

# Создаем объект библиотеки
library = Library()

# Добавляем книги в библиотеку
library.add_book("Harry Potter and the Philosopher's Stone")
library.add_book("The Great Gatsby")
library.add_book("1984")

# Выводим информацию о библиотеке с перечнем книг и количество книг
print(library)
print(f"Number of books in library: {len(library)}")
"""

# Наследование
"""
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return f"{self.brand} {self.model} is driving."

class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def ride(self):
        return f"{self.brand} {self.model} is riding."

# Примеры использования классов:
car = Car("Toyota", "Corolla")
print(car.drive())  # Output: Toyota Corolla is driving.

motorcycle = Motorcycle("Yamaha", "R1")
print(motorcycle.ride())  # Output: Yamaha R1 is riding.
"""

"""
import math

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return  self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * pow(self.radius, 2)


# Пример использования
rect = Rectangle(3, 4)
print(f"Area of rectangle: {rect.area()}")

circle = Circle(5)
print(f"Area of circle: {circle.area():.2f}")
"""



"""
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

car = Car("Lada", "Sedan", 95)
print(f"Brand: {car.brand}, Model: {car.model}, Fuel Type: {car.fuel_type}")
"""


"""
class Animal:
    def speak(self):
        return "Ррррр!"


class Dog(Animal):
    def speak(self):
        parent_bark = super().speak()
        return f"{parent_bark} Гав!"

dog = Dog()
print(dog.speak())
"""