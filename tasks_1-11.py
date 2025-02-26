"""
while True:
    response = input("Введите 'exit' для выхода: ")
    if response == 'exit':
        break
"""
import math

"""
elements = [1, 2, 3, -99, 5]
# Поиск первого отрицательного элемента
for element in elements:
    if element < 0:
        print("Найден отрицательный элемент: ", element)
        break
"""

"""
i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
"""

"""
sum = 0
num = 0
while num >= 0:
    num = int(input("Введите число: "))
    if num < 0:
        break
    sum += num
    print(sum)
"""

"""
name = input("Введите Ваше имя: ")
age = input("Введите Ваш возраст: ")
city = input("Введите Ваш город: ")
greetings = f"Привет, {name}! Тебе {age} лет, и ты живешь в городе {city}."
print(greetings)
"""

"""
print(1, 2, 3, 4, 5, sep = "*", end = " ")
print("Конец программы.")
"""

"""
num = int(input("Введите число: "))
print("Число четное") if num % 2 == 0 else print("Число нечетное")
"""

"""
num = int(input("Введите число : ")) # Таблица Пифагора
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(i * j, end='\t')
    print()
"""

"""
x = 1
print(type(x))
"""

"""
integer = int(input("Введите целое число: ")) # преобразование типов
flt = float(input("Введите вещественное число: "))
string = str(input("Введите строку: "))

in_float = float(integer)
in_str = str(flt)
in_int = int(string)

print(in_float)
print(in_str)
print(in_int)
"""

"""
import random
summ = 0
for i in range(0, 10):
    ran = random.randint(1, 100)
    summ += ran
print("Среднее значение: ", summ / 10)
"""

"""
num = float(input())
down = math.floor(num)
up = math.ceil(num)
near = round(num)
print(down)
print(up)
print(near)
"""

"""
import random  #функция генерации случайного целого числа в заданном диапазоне
def generate_random_number(a, b):
    x = random.randint(a, b)
    print(x)
generate_random_number(-200, 0)
"""
"""
import random
def print_random(a, b, c):
    x = random.choice([a, b, c])
    print(x)
print_random(10, 7, 4)
"""

"""
a = int(input("Первое число: "))
b = int(input("Второе число: "))

def find_max(a, b):
    if a > b or a == b:
        return a
    else:
        return b
print(find_max(a, b))
"""

"""
n = int(input("Введите число: "))
def factorial(n):
    summ = 1
    for i in range(1, n + 1):
        if n == 0:
            return 1
        summ *= i
    return summ
print(factorial(n))
"""

"""
def calculate_total_cost(price, tax = 0.2):
    print(price * (1 + tax))
calculate_total_cost(55)
calculate_total_cost(100, tax = 0.3)
"""
"""
def create_cat_profile(name, age, breed = "Неизвестно"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Breed: {breed}")
create_cat_profile("Барсик", "7")
"""

"""
counter = 0
def increment_counter():
    global counter
    counter += 1
    return counter
increment_counter()
increment_counter()
print(counter)
"""

"""
def sum_numbers(*args: int) -> int:
    #summ = 0
    #summ += args
    return sum(args)
print(sum_numbers(5, 5, 5))
print(sum_numbers(123, 456, 789, 101112))
"""

"""
def create_cat_profile(name: str, age: int, **kwargs: str) -> None:
    print(f"имя: {name}")
    print(f"возраст: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_cat_profile("Мурзик", 3, порода="Сиамский", цвет="Черный")
create_cat_profile("Барсик", 5, страна="Китай", хобби="Ловить мышей")
"""

"""
list = []
for i in range(-100, 101):
    x = i * i
    list.append(x)
print(list)
"""

"""
list = []
elem = ''
while elem != "стоп":
    elem = input()
    if elem == "стоп":
        break
    list.append(elem)
print(list)
"""

"""
elem_list = [12, True, "64", [0,7], 3.14]
print(len(elem_list))
print(type(elem_list))
print(elem_list[0])
print(elem_list[-1])
"""

"""
my_list = []
for i in range(5):
    elem = input("Введите значение: ")
    my_list.append(elem)
print(my_list)
print(my_list[int(input("Введите индекс: "))])
"""

"""
my_list = ["cat", "dog", "bird", "ant", "elephant", 6, 7, 8, 9, 10]
print(my_list[2:7])
print(my_list[-3:])
"""

"""
my_list = ["cat", "dog", "bird", "ant", "elephant","Barsik", "Sharik", "Kesha", "Anansi", "Mamont" ]
string = input("Запрос строки: ")
is_string = string in my_list
print(is_string)
"""

"""
my_list = []
for _ in range(5):
    elem = input("Введите элемент: ")
    my_list.append(elem)
print(my_list)
"""

"""
my_list = ["cat", "dog", "bird", "ant", "elephant","Barsik", "Sharik", "Kesha", "Anansi", "Mamont"]
replace = input("Заменить на: ")
my_list[2:5] = [replace]
print(my_list)
"""

"""
my_list = []
for _ in range(5):
    elem = input("Элемент списка: ")
    my_list.append(elem)
print(my_list)
purge = input("Элемент для удаления: ")
my_list.remove(purge)
print(my_list)
"""

"""
my_list = []
for _ in range(5):
    elem = input("Элемент списка: ")
    my_list.append(elem)
print(my_list)
index = int(input("Индекс для удаления: "))
if 0 <= index < len(my_list):
    removed_element = my_list.pop(index)
    print("Обновленный список:", my_list)
    print("Удаленный элемент:", removed_element)
else:
    print("Индекс не существует.")
print(my_list)
"""

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = "четное"
print(numbers)
"""

"""
n = 10
alist = [i ** 2 for i in range(1, n)]
print(alist)
"""

"""
from random import randrange

n = 20
alist = [randrange(1, 100) for i in range(n)]
print(alist)
new_alist = [alist[i] for i in range(len(alist)) if alist[i] % 2 == 0] #с использованием List Comprehension и выводом только четных чисел из списка alist
print(new_alist)
"""

"""
from random import randrange
my_list = [randrange(1, 101) for i in range(10)]
print(my_list)

sorted_num_up = sorted(my_list)
print(sorted_num_up)

sorted_num_up.sort(reverse=True)
print(sorted_num_up)
"""

"""
my_list = []
for i in range(5):
    string = input("Введите строку: ")
    my_list.append(string)
my_list = sorted(my_list, key=len) # можно указать 3-й параметр reverse=True , тогда список будет идти по убыванию длины строк
print(my_list)
"""

"""
from random import randrange
my_list = [randrange(1, 101) for i in range(10)]
import copy
my_list_copy = copy.deepcopy(my_list)
my_list_copy = sorted(my_list_copy)
print(my_list)
print(my_list_copy)
"""

"""
from random import randrange
my_list = [randrange(1, 21) for i in range(10)]
print(my_list)
for list in my_list.copy():
    if list % 2 == 0:
        my_list.remove(list)
print(my_list)
"""

"""
tuple1 = ()
tuple2 = (1,)
tuple3 = 1, 2, 3, 4, 5
tuple4 = ([i for i in range(1, 101)])
list_to_tuple4 = tuple(tuple4)
tuple5 = ([i for i in range(1, 1001)])
list_to_tuple5 = tuple(tuple5)
print(tuple1)
print(tuple2)
print(tuple3)
print(list_to_tuple4)
print(list_to_tuple5)
"""

"""
values = ('Alice', 25, 'Moscow')
name, age, city = values # распаковка элементов кортежа в переменные
print(name)
print(age)
print(city)
"""

"""
my_list= [input("Cтроки: ") for i in range(int(input("Кол-во строк: ")))]
tuple = tuple(my_list)
if len(tuple) > 0:
    print(tuple[-1])
else:
    print("Пустой кортеж")
print(type(tuple))
"""


"""
#РЕШЕНИЕ ВЕРХНЕЙ ЗАДАЧИ МЕНТОРОМ:
elements = []
print("Введите элементы кортежа (для окончания ввода просто нажмите Enter):")
while True:
    element = input()
    if element == "":
        break
    elements.append(element)

tuple_elements = tuple(elements)

if tuple_elements:
    print(f"Последний элемент кортежа: {tuple_elements[-1]}")
else:
    print("Кортеж пустой")
"""

"""
elements = []
for i in range(5):
    elem = input("Введите строку: ")
    elements.append(elem)
tuple = tuple(elements)
index = int(input('Введите индекс: '))
if index >= 0 and index <= len(tuple) - 1:
        print(tuple[index])
else:
        print("Индекс за пределами котрежа")
"""

"""
elems = []
while True:
    string = input('Введите элемент: ')
    if string == '':
        break
    elems.append(string)
elems = tuple(elems)
reversed_tuple = elems[::-1]
print(reversed_tuple)
"""

"""
my_tuple = [input('Введите элемент: ')for i in range(7)]
my_tuple = tuple(my_tuple)
print(my_tuple[-3:-1])
"""


"""
my_list = [input('Введите элемент: ') for i in range(5)]
my_tuple = tuple(my_list)
#print(my_tuple)
#print(type(my_tuple))
new_list = list(my_tuple)
new_list.append(input('Добавить элемент: '))
#print(new_list)
new_tuple = tuple(new_list)
print(new_tuple)
#print(type(new_tuple))
"""

"""
#РЕШЕНИЕ ВЕРХНЕЙ ЗАДАЧИ МЕНТОРОМ
# Создаем кортеж из 5 элементов, запрашиваемых у пользователя
elements = tuple(input(f"Введите элемент {i+1}: ") for i in range(5))

# Запрашиваем у пользователя новый элемент
new_element = input("Введите новый элемент для добавления в конец кортежа: ")

# Создаем новый кортеж, добавляя новый элемент к существующему кортежу
updated_tuple = elements + (new_element,)

# Выводим обновленный кортеж
print("Обновленный кортеж:", updated_tuple)
"""

"""
elements = tuple(input(f"Введите элемент {i+1}: ") for i in range(6))
elements1 = (elements[0],) + (elements[1],) 
#elements1 = elements[:2]
elements2 = (elements[2],) + (elements[3],) 
#elements2 = elements[2:4]
elements3 = (elements[4],) + (elements[5],) 
#elements3 = elements[4:]
sum_elements = elements1 + elements3
print(sum_elements)
"""

"""
my_tuple = ((50, 30), (20, 40, 50), (10,))
total = 0
for inner_tuple in my_tuple:
    for number in inner_tuple:
        total += number
print(total)
"""


"""
def find_max(tup):      #"найти максимальный элемент в_кортеже"
    max_num = float('-inf')

    for sub_tup in tup:
        for elem in sub_tup:
            if elem > max_num:
                max_num = elem

    return max_num
tup = ((50, 30), (20, 40, 60), (10,))
print(find_max(tup))
"""

"""
empty_set = set()
one_set = {1}
five_set = {1, 2, 3, 4, 5}
hundred_set = set(x for x in range(1, 101))
thousand_set = set(x for x in range(1, 1001))
"""

"""
alist = [input('Введите элемент: ') for i in range(10)]
uniq_set = set(alist)
print(uniq_set)
"""

"""
color_set = {'red', 'blue', 'yellow', 'green', 'white', 'black', 'orange'}
print(color_set)
"""

"""
def set_detector(*args):
  for arg in args:
    if isinstance(arg, set):
      return True
  return False

color_set = {'red', 'blue', 'yellow', 'green', 'white', 'black', 'orange'}
num_set = [1, 2, 3]
my_tuple = (4, 5, 6)
print(set_detector(color_set, num_set, my_tuple))
"""

"""
from random import randrange
my_set = set(randrange(1, 101) for i in range(10))
even_set = {x for x in my_set if x % 2 == 0}
print(even_set)
"""

"""
square_set = set(pow(x, 2)  for x in range(1, 11))
print(square_set)
"""

"""
import random
n = 10
list1 = [random.randint(0, 99) for _ in range(n)]
list2 = [random.randint(50, 125) for _ in range(n)]
my_set1 = set(list1)
my_set2 = set(list2)
combined_set = my_set1 | my_set2
print(combined_set)
print(len(combined_set))
"""

"""
empty_set = set()
for i in range(5):
    request = int(input('Input number: '))
    new_set = {request}
    empty_set.update(new_set) # empty_set = empty_set.union(new_set)
print(empty_set)
"""

"""
cat_set = {'Мурзик', 'Барсик', 'Васька', 'Бегемот', 'Мурка'}
counter = 0
while cat_set:
    name = input("Угадайте имя кота: ")
    if name in cat_set:
        cat_set.discard(name)
        print(f"Верно! Осталось угадать: {len(cat_set)} имен.")
    else:
        print("Неверно. Попробуйте снова.")
    counter += 1
print(f"Вы угадали всех котов за {counter} попыток!")
"""

"""
import random
n = 10
random_set = {random.randint(1, 50) for _ in range(n)}
for index, element in enumerate(random_set):
    print(f"Индекс: {index}, Элемент: {element}")
"""

"""
fruits = {'banana', 'grapes', 'apple', 'orange'}
print(fruits)
new_fruits = list(fruits)
number = int(input('Введите номер: '))
elem = input('Введите новое название: ')
for index, element in enumerate(new_fruits):
    if index == number:
        new_fruits[index] = elem
fruits = set(new_fruits)
print(fruits)
"""

"""
set1 = set(input('Введите элемент: ') for x in range(int(input('Введите кол-во элементов: '))))
set2 = set(input('Введите элемент: ') for x in range(int(input('Введите кол-во элементов: '))))
set3 = set1.union(set2) # set3 = set1 | set2
print(set3)
intersection_set = set1.intersection(set2) # union_set = set1 & set2
print(intersection_set)
"""

"""
import random
random_set1 = {random.randint(1, 20) for _ in range(10)}
random_set2 = {random.randint(10, 30) for _ in range(10)}
difference_set = random_set1.difference(random_set2) # difference_set = random_set1 - random_set2
symmetric_difference_set = random_set1.symmetric_difference(random_set2) # difference_set = random_set1 ^ random_set2
print(random_set1)
print(random_set2)
print(difference_set)
print(symmetric_difference_set)
"""

"""
text = input('Введите строку: ')
substring = input('Подстрока: ')
print(substring in text)
find_meth = text.find(substring)
counter = text.count(substring)
print(find_meth)
print(counter)
"""

"""
text = input('Введите строку: ')
print(len(text))
try:
    text_index = int(input('Введите индекс: '))
    print(text[text_index])
except IndexError:
    print("Индекс выходит за пределы строки.")
"""

"""
string = input('Введите строку: ')
sub_str1 = string[3:9]
sub_str2 = string[5:]
print(sub_str1)
print(sub_str2)
"""

"""
string = input('Введите строку: ')
last_three = string[-3:]
except_last = string[:-1]
reversed_string = string[::-1]
print(last_three)
print(except_last)
print(reversed_string)
"""

"""
text = input()
gap_del = text.strip()
print(gap_del)
lower_text = text.lower()
print(lower_text)
upper_text = text.upper()
print(upper_text)
"""

"""
string = input("Введите несколько слов, разделенных запятыми: ")
split_string = string.split(',')
print(split_string)
joined_string = ' '.join(split_string)
print(joined_string)
"""

"""
print(u'\U0001F600')
print(u'\U0001F923')
print(u'\U0001F602')
"""

"""
alist = [1,2,3,4,5]
frset1 = frozenset(alist)
print(frset1)
string = input('Введите строку: ')
frset2= frozenset(string)
print(frset2)
union_set = frset1 | frset2
print(union_set)
intersection_set  = frset1 & frset2
print(intersection_set)
difference_set = frset1 - frset2
print(difference_set)
symmetric_set = frset1 ^ frset2
print(symmetric_set)
"""

"""
list1 = ['name', 'city', 'age']
list2 = ['new_name', 'new_city', 'new_age']

frset1 = frozenset(list1)
frset2 = frozenset(list2)

string1 = ", ".join(map(str, ['Saul', 'Denver', 33]))
string2 = ", ".join(map(str, ['Mike', 'LA', 58]))

dic = {frset1: string1, frset2: string2}
print(dic)
"""

"""
dic1 = {"name" : "Vlad", "age" : 45, "city" : "Zhukovsky"}
print(dic1)
dic2 = dict([("name", "Saul"), ("age", 33), ("city", "Phenix")])
print(dic2)
dic3 = dict(name="John", age=30, city="New York")
print(dic3)
"""

"""
students = {
    "Группа": [
        {
            "Иванов": [
                "Математика",
                "Физика",
                "Информатика"
            ]
        },
        {
            "Петрова": [
                "Русский язык",
                "Литература",
                "История"
            ]
        }
    ]
}
print(students)
"""

"""
person1 = {"name" : "Saul", "age" : 47, "city" : "Albuquerque"}
person2 = {"name" : "Mike", "age" : 61, "city" : "New-York", "country" : "America"}
person3 = {}
print(len(person1))
print(len(person2))

def check_empty(dic):
    if len(dic) > 0:
        print("Словарь не пустой")
    else:
        print("Словарь пустой")
check_empty(person1)
check_empty(person2)
check_empty(person3)
"""

"""
person_dict = {"name" : "Saul", "age" : 47, "city" : "Albuquerque"}
city = person_dict["city"]
print(city)
print(person_dict.get("name"))
print(person_dict.get("country"))
print(person_dict.setdefault("country", "America"))
print(person_dict)
"""

"""
book = {"name" : "Generation 'P'", "author" : "V. Pelevin", "year" : 1999}
keys = book.keys()
print(keys)

for key in book.keys():
    print(key)
"""

"""
product = {'name' : 'coffee', 'price' : 775, 'quantity' : 1}
for key, value in product.items():
    print(f"{key}: {value}")
product["brand"] = "Ruanda Kigali"
print(product)
"""

"""
book = {"title" : "Generation 'P'", "author" : "V. Pelevin", "publisher" : 1999}

if "author" in book:
    print("Ключ 'author' присутствует в словаре.")
else:
    print("Ключ 'author' отсутствует в словаре.")

value = book.get("publisher")
if value is not None:
    print("Ключ 'publisher' присутствует в словаре.")
else:
    print("Ключ 'publisher' отсутствует в словаре.")

if "title" in book.keys():
    print("Ключ 'title' присутствует в словаре.")
else:
    print("Ключ 'title' отсутствует в словаре.")
"""

"""
student = {'name' : "Anton", 'age' : 22, 'university': "MIT"}
if "MIT" in student.values():
    print("Значение 'MIT' присутствует в словаре.")
else:
    print("Значение 'MIT' отсутствует в словаре.")

values_set = set(student.values())
if 'Harvard' in values_set:
    print("Значение 'Harvard' присутствует в словаре.")
else:
    print("Значение 'Harvard' отсутствует в словаре.")

value_to_find = 22

if any(value == value_to_find for value in student.values()):
    print(f"Значение {value_to_find} присутствует в словаре.")
else:
    print(f"Значение {value_to_find} отсутствует в словаре.")
"""

"""
student = {"имя" : "Саул", "возраст" : 23}
student["университет"] = "МГУ"
print(student)
if "город" not in student:
    student["город"] = "Москва"
print(student)
new_elements = {"страна" : "Россия", "планета" : "Земля"}
student.update(new_elements)
print(student)
"""

"""
book = {"название" :
"Три товарища",
"автор" :
"Эрих Мария Ремарк",
"год издания" :
1926}
print(book)

book["год издания"] = 1936
print(book)

if "издательство" not in book:
    publishing = book.setdefault("издательство", "Kammerater")
print(book)


book.update({"автор" : "Э.М. Ремарк", "country" : "Германия"})
print(book)

for key, value in enumerate(book.items()):
    print(f"Ключ: {key}, Значение: {value}")
"""

"""
#Словарь с данными о человеке
student = {"name": "Jessie", "age": 25, "university": "Cambridge"}

# Перебор ключей и значений словаря с индексами
for index, (key, value) in enumerate(student.items()):
    print(f"Индекс: {index}, Ключ: {key}, Значение: {value}")
"""

"""
employees = [("Иванова", "директор"), ("Петрова", "бухгалтер"), ("Сидорова", "секретарь")]
employees = {name: position for name, position in employees}
print(employees)
"""

"""
# Обход словаря.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Перебрать все элементы словаря, включая вложенные словари, с использованием циклов.
# Реализовать функцию для обхода всех уровней вложенности и вывода ключей и значений.

person = {
    "name": "Saul",
    "details": {
        "age": 25,
        "contact": {
            "phone": "127-07-08"
         }
    }
}
def print_dict(d, indent=0):
    for key, value in d.items():
        print("  " * indent + str(key) + ": ", end="")
        if isinstance(value, dict):
            print()
            print_dict(value, indent + 1)
        else:
            print(value)

print_dict(person)
"""

"""
person = {
    "name": "Saul",
    "details": {
        "age": 25,
        "contact": {
            "phone": "127-07-08"
        },
       "address": {
             "city" : "Albuquerque"
        }
    }
}

print(person)
"""

"""
person = {
    "name": "Saul",
    "details": {
        "age": 25,
        "contact": {
            "phone": "127-07-08"
        },
       "location": {
             "city" : "Albuquerque"
        }
    }
}

print(person)
person["name"] = "Mike"
print(person)
print(person)
person["details"]["age"] = 61
print(person)
person["details"]["contact"]["phone"] = "111-11-11"
print(person)
person["details"]["location"]["street"] = "Main St."
print(person)
del person["name"]
print(person)
del person["details"]["location"]["street"]
print(person)
"""