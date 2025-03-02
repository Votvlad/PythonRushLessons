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


