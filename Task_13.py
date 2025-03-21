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

# Запуск исключения

""" 
def check_positive(num):
    if num <= 0:
        raise ValueError("Number must be positive")
    print(num)
try:
    check_positive(-3)
except ValueError as e:
    print('Ошибка: число отрицательное, либо равно нулю.')
"""

"""
class InputValidationError(Exception):
    def __init__(self, message, original_exception=None):
        super().__init__(message)  # Инициализируем родительский класс
        self.original_exception = original_exception  # Сохраняем исходное исключение

# 2. Функция validate_input
def validate_input(string):
    try:
        # Проверка на пустую строку
        if string == "":
            raise ValueError("Input cannot be empty")
        # Проверка на длину строки
        if len(string) > 10:
            raise ValueError("Input is too long")
        # Если проверки пройдены, возвращаем строку
        return string
    except ValueError as e:
        # Переупаковываем ValueError в InputValidationError
        raise InputValidationError("Validation failed", original_exception=e) from e

# 3. Пример использования
try:
    result = validate_input("")  # Вызов функции с пустой строкой
    print(f"Validation successful: {result}")
except InputValidationError as e:
    print(f"Caught custom exception: {e}")
    print(f"Original exception: {e.original_exception}")
"""

# Создание своего исключения

"""
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(f"Invalid age: {age}")

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer for age.")
"""

"""
class ApplicationError(Exception):
    pass

class NegativeValueError(ApplicationError):
    pass

class ValueTooLargeError(ApplicationError):
     pass

def check_number(num) :
    if num < 0:
        raise NegativeValueError("Введено отрицательное число",  num)
    if num > 100:
        raise ValueTooLargeError("Значение превышает максимум", num)

try:
    check_number(101)
except NegativeValueError as e:
    print("Введено отрицательное число")

except ValueTooLargeError as e:
    print("Значение превышает максимум")
"""

# Импорт модулей

"""
#with open ("geometry.py", "w") as geometry:
    # geometry.write(import math

#def circle_area(radius):
    #return math.pi * pow(radius, 2)

#def rectangle_area(length, width):
    #return length * width)

#with open ("import_geometry.py", "w") as import_geometry:
    #import_geometry.write(from geometry import circle_area
#print(f"Площадь круга: {circle_area(5):.2f}")
"""


"""
module_name = input("Введите название модуля: ")
func_name = input("Введите название функции: ")

module = __import__(module_name)
import_result = getattr(module, func_name)
print(f"{import_result(100):.1f}")
"""

#Создание своего пакета


#import os

#os.makedirs("mypackage", exist_ok=True)

#with open("mypackage/module1.py", "w") as f:
    #f.write("""import math
    #def circle_area(radius):
        #return math.pi * pow(radius, 2)
    #""")

#with open("mypackage/module2.py", "w") as f:
    #f.write("""import math
    #def rectangle_area(length, width):
        #return length * width
#""")

#with open("test.py", "w") as f:
    #f.write("""from mypackage import module1, module2

#print(f"{module1.circle_area(4):.1f}")
#print(module2.rectangle_area(5, 7))
#""")


"""
#with open("mymodule.py", "w") as f:
    #f.write(#import math      # запись кода в файл должна быть в тройных кавычках
    #def circle_area(radius):
        #return math.pi * pow(radius, 2)
    #radius = 5)

with open("task04.py", "w") as f:
    #f.write(import mymodule
    #print(dir(mymodule)))
"""


# Пакетные менеджеры

"""
pip --version

pip install requests

pip install numpy==1.21.0

pip install --upgrade requests

pip uninstall -y requests

pip list
"""

"""
conda create --name myenv

conda activate myenv

conda install numpy

conda list

conda deactivate
"""


# Установка пакетов

"""
import requests
response = requests.get("https://jsonplaceholder.typicode.com")
print(response)
"""


"""
# Установка пакета cowsay
#pip install cowsay

# Использование пакета cowsay для отображения сообщения
import cowsay
cowsay.cow("Нужно было учить Python...")

# Удаление пакета cowsay
#pip uninstall -y cowsay
"""


# Итераторы

"""
class SimpleIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current


iterator = SimpleIterator(5, 11)

for num in iterator:
    print(num)
"""

"""
class CollectionIterator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyIterator(self.data)


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item


iterator = CollectionIterator([1, 3, 5, 7, 9])

for num in iterator:
    print(num)
"""


# Перегрузка операторов

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

p = Person("Petr", 75)
p2 = Person("Mikhail", 35)
print(p == p2)
print(p > p2)
"""

"""
class Matrix:
    def __init__(self, rows, cols=None):
        if cols is None:
            # Если передан один аргумент, это готовая матрица
            self.data = rows
        else:
            # Если переданы два аргумента, создаём матрицу, заполненную нулями
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, index):
        if isinstance(index, tuple):
            row, col = index
            if row < len(self.data) and col < len(self.data[row]):
                return self.data[row][col]
            else:
                raise IndexError("Индекс за пределами матрицы")
        else:
            if index < len(self.data):
                return self.data[index]
            else:
                raise IndexError("Индекс строки за пределами матрицы")

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            row, col = index
            if row < len(self.data) and col < len(self.data[row]):
                self.data[row][col] = value
            else:
                raise IndexError("Индекс за пределами матрицы")
        else:
            if index < len(self.data):
                self.data[index] = value
            else:
                raise IndexError("Индекс строки за пределами матрицы")


matrix = Matrix(3, 3)
matrix[0, 0] = 1
print(matrix[0, 0])  # Вывод: 1
"""

# Стандартные ошибки

"""
def foo(bar=[]):
    bar.append("baz")
    return bar


def foo_correct(bar=None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar


print(foo())
print(foo())
print(foo())
# Проверка исправленной функции
print(foo_correct())  # Выводит: ['baz']
print(foo_correct())  # Выводит: ['baz']
print(foo_correct())  # Выводит: ['baz']

# Проверка с передачей списка
lst = [1, 2, 3]
print(foo_correct(lst))  # Выводит: [1, 2, 3, "baz"]
print(foo_correct(lst))  # Выводит: [1, 2, 3, "baz", "baz"]
"""

"""
# Неправильный вариант: несколько исключений перехватываются неправильно
try:
    number = int(input("Введите число: "))
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Произошла ошибка: вводите только числа кроме нуля.")

# Исправленный вариант:

try:
    number = int(input("Введите число: "))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print("Произошла ошибка: вводите только числа кроме нуля.")
"""

# Стандартные ошибки, часть 2

"""
x = 10

def foo_correct():
    global x
    x += 1
    print(x)

foo_correct()  # Вывод: 11
"""

"""
# Исправьте код замыкания:
def create_multipliers_correct():
    return [lambda x, i=i : i * x for i in range(5)]

for multiplier in create_multipliers_correct():
    print(multiplier(2))  # Вывод: 0 2 4 6 8
"""


# Стандартные ошибки, часть 3

"""
# Импортируем встроенный модуль math
import math as std_math

# Вызов функции sqrt стандартного модуля math
print(std_math.sqrt(9))

# Импортируем пользовательский модуль math
import importlib.util

# Путь к пользовательскому модулю
# custom_math_path = './math.py'
custom_math_path = '/home/votvlad/PythonRush/mypackage/math.py'

# Загрузите пользовательский модуль math
spec = importlib.util.spec_from_file_location("custom_math", custom_math_path)
custom_math = importlib.util.module_from_spec(spec)
spec.loader.exec_module(custom_math)

# Вызов функции sqrt из пользовательского модуля math
custom_math.sqrt(9)
"""

"""
def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)

def bad():
    exception = None
    try:
        bar(1)
    except KeyError as e:
        exception = e
        print('key error')
    except ValueError as e:
        exception = e
        print('value error')
    print(exception)

bad()
"""











