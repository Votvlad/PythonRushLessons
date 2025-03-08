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
from logging import exception

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

# Инициализация иерархии

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

# Полиморфизм

"""
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method!")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * pow(self.radius, 2)






def process_input(string):
    try:
        result = int(string)
        if int(result):
            print(result ** 2)
    except (ValueError, IndexError) as e:
         print(f"Произошла ошибка: {e}")

# Примеры вызова функции
print(process_input("5"))         # Вывод: 25
print(process_input("abc"))       # Вывод: Ошибка: введенная строка не является числом.
print(process_input(""))
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
areas = [shape.area() for shape in shapes]

for area in areas:
    print(f"{area:.2f}")
"""

"""
class Animal:
    def make_sound(self):
        return "Ууууууу!"

class Dog(Animal):
    def make_sound(self):
        parent_bark = super().make_sound()
        return f"{parent_bark} Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        parent_bark = super().make_sound()
        return f"{parent_bark} Мяу-мяу!"

# Примеры использования:

dog = Dog()
cat = Cat()

print(dog.make_sound())  # Ууууууу! Гав-гав!
print(cat.make_sound())  # Ууууууу! Мяу-мяу!

#animals = [dog, cat]
#for animal in animals:
    #print(animal.make_sound())
"""

# Проверка типов

"""
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

def check_type(obj):
    return isinstance(obj, Animal)

dog = Dog()
cat = Cat()
not_animal = "Not an animal"

print(check_type(dog))  # True
print(check_type(cat))  # True
print(check_type(not_animal))  # False
"""

"""
def check_subclass(class_name1, class_name2):
    return issubclass(class_name1, class_name2)

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass


print(check_subclass(Vehicle, Car))
print(check_subclass(Bicycle, Vehicle))
"""

# Множественное наследование

"""
class Base1:
    def describe(self):
        print('Метод Base1')


class Base2:
    def describe(self):
        # super().describe()
        print('Метод Base2')


class Combined(Base1, Base2):
    def describe(self):
        super().describe()
        Base2.describe(self)
        print('Метод Combined')


comb = Combined()
comb.describe()
"""


"""
class BaseA:
    def action(self):
        print("Питонь!")
        super().action()

class BaseB:
    def action(self):
        print("Кому говорю?!")
        #super().action()

class Derived(BaseA, BaseB):
    def action(self):
        print(f"Сильно питонь!!")
        super().action()

d = Derived()
d.action()
"""

# Method Resolution Order

"""
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")
        super().method()

class C(A):
    def method(self):
        print("C")
        super().method()

class D(B, C):
    def method(self):
        print("D")
        super().method()


d = D()
d.method()
"""

"""
class M:
    def action(self):
        print("This is a class M")


class N(M):
    def action(self):
        print("This is a class N")
        super().action()


class O(M):
    def action(self):
        print("This is a class O")
        super().action()


n = N()
n.action()
"""


# Ошибки во время работы программы

"""
def division(a, b):
    if b == 0:
        raise ZeroDivisionError('деление на ноль')
    return a / b

print(division(6, 3))
print(division(5, 0))
"""

"""
def square(number):
    try:
        return pow(number, 2)
    except TypeError:
        return "Ошибка: несовместимые типы данных"

print(square('5'))

#def cause_type_error():
    #result = "string" + 5

#cause_type_error()
"""

# Популярные исключения

"""
#Напиши программу, которая создает исключение IndentationError
def error_func():
return "Hello!"

error_func()
"""


"""
# Напиши программу, которая создает исключение SyntaxError
raise SyntaxError("Это синтаксическая ошибка")
"""

# Обработка исключений

"""
def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль."
    except TypeError:
        return "Некорректный ввод данных"
    return result

print(safe_division('6', 3))
"""

"""
def convert_and_sum(a, b):
    try:
        result = int(a) + int(b)
    except ValueError:
        return "Ошибка: невозможно преобразовать аргумент в число."
    return result

print(convert_and_sum('a', '10'))
"""

# Обработка нескольких исключений


"""
def process_input(string):
    try:
        if not string:
            raise IndexError("Введена пустая строка.")
        num = int(string)
        return num ** 2
    except ValueError:
        return "Ошибка: введенная строка не является числом."
    except IndexError:
        return "Ошибка: введена пустая строка."

# Примеры вызова функции
print(process_input("5"))         # Вывод: 25
print(process_input("abc"))       # Вывод: Ошибка: введенная строка не является числом.
print(process_input(""))          # Вывод: Ошибка: введена пустая строка.
"""

"""
def read_integer(string):
    try:
        num = int(string)
    except ValueError as e:
        print(f"Тип ошибки: {type(e)}")
        print(f"Аргументы ошибки: {e.args}")
        return e

exception = read_integer("hola")
print(exception)
"""


"""
# вариант решения предыдущей задачи ментором
def read_integer(input_string):
    exception_instance = None
    try:
        return int(input_string)
    except ValueError as e:
        exception_instance = e
        print(f"Error arguments: {e.args}")
        print(f"Error type: {type(e)}")
    print(f"Exception instance: {exception_instance}")

read_integer("abc")
"""

# Стек-трейс

"""
import traceback

def divide_numbers(a, b):
    try:
        return a/ b
    except ZeroDivisionError as e:
        print("Произошло исключение:")
        traceback.print_exc()

divide_numbers(1, 0)
"""

"""
import traceback

def complex_operation():
    def inner_function_1():
        def inner_function_2():
            def inner_function_3():
                # Здесь генерируем исключение
                raise ValueError("An error occurred")
            inner_function_3()
        inner_function_2()
    try:
        inner_function_1()
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        for frame in tb:
            print(f"File: {frame.filename}, Line: {frame.lineno}, Function: {frame.name}, Code: {frame.line}")

complex_operation()
"""


