# Работа с файлами

"""
file = open('mypackage/example.txt', 'r')
content = file.read()
print(content)
file.close()
"""

"""
file = open('mypackage/example.txt', 'w')
file.write("Hello, World!")
file.close()

file = open('mypackage/example.txt', 'a')
file.write("\nAppended text.")
file.close()
"""

# Чтение данных из файла

"""
file = open('mypackage/example.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()
"""

"""
file = open('mypackage/example.txt', 'r')
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()
file.close()
"""

# Запись данных в файл

"""
file = open('mypackage/example.txt', 'w')
file.write("This is a new file.\n")
file.close()
"""

"""
file = open('mypackage/example.txt', 'a')
file.write("Мы добавили эту линию.\n")
file.write("И эту тоже.\n")
file.close()
"""


# Оператор with

"""
file = None
try:
    file = open('example.txt', 'a')
    file.write("Новая линия.")
except FileNotFoundError:
    print("Файл не найден.")
finally:
    if file:
        file.close()
"""

"""
try:
    with open('example.txt', 'a') as file:
        file.write("Новая линия.\n")
except FileNotFoundError as e:
    print(f"Caught an exception: {e}")
"""


