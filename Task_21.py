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


# Работа с бинарными файлами

"""
#with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)
"""

"""
#with open('input_image.jpg', 'rb') as infile:
    image_data = infile.read()

#with open('output_image.jpg', 'wb') as outfile:
    outfile.write(image_data)
"""


# Работа с файлами на диске

"""
#with open('source.txt', 'r') as file:
    source = file.read()

#with open('destination.txt', 'w') as file:
    file.write(source)
"""

"""
import os

if os.path.exists('example.txt'):
    os.remove('example.txt')
else:
    print("File does not exist")
"""

# Работа с директориями

"""
import os
import shutil

os.mkdir('new_directory')

os.makedirs('parent_directory/child_directory')

os.rmdir('new_directory')

shutil.rmtree('parent_directory')
"""

"""
import os

current_directory = os.getcwd()
print(f"Текущая рабочая директория: {current_directory}")

contents = os.listdir('.')
print(f"Содержимое текущей директории: {contents}")

with os.scandir('.') as entries:
    for entry in entries:
        print(f"Имя: {entry.name}, Это директория: {entry.is_dir()}, Это файл: {entry.is_file()}")
"""


# Сериализация

"""
import pickle

# Объект для сериализации
student_info = {
    'name': 'John Doe',
    'age': 20,
    'status': 'student'
}
# Сериализация объекта
with open('student_info.pkl', 'wb') as file:
    pickle.dump(student_info, file)

# Десериализация объекта из файла
with open('student_info.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
"""

"""
import yaml

# Пример словаря с информацией о фильме
film_info = {
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'year': 2010
}

# Сериализация объекта в строку YAML
yaml_string = yaml.dump(film_info)
print(yaml_string)

# Десериализация объекта из строки YAML
loaded_data = yaml.load(yaml_string, Loader=yaml.FullLoader)
print(loaded_data)
"""


# Работа с pickle

"""
import pickle

data = [1, 2, 3, 'a', 'b', 'c']

with open('example.pkl', 'wb') as file:
    pickle.dump(data, file)

with open('example.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
"""

"""
import pickle

data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}

serialized_data = pickle.dumps(data)

loaded_data = pickle.loads(serialized_data)

print(loaded_data)
"""

# Управление сериализацией

"""
import pickle

class CustomClass:
    def __init__(self, name, age, city=None):
        self.name = name
        self.age = age
        self.city = city

    def __reduce__(self):
        # Возвращаем кортеж: (функция, аргументы, состояние)
        return (self.__class__, (self.name, self.age))

    def __repr__(self):
        return f"CustomClass(name={self.name}, age={self.age}, city={self.city})"

obj = CustomClass('Alice', 23, 'Wonderland')
print("Оригинальный объект:", obj)

# Сериализация объекта
serialized_obj = pickle.dumps(obj)
print("Сериализованный объект:", serialized_obj)

# Десериализация объекта
deserialized_obj = pickle.loads(serialized_obj)
print("Десериализованный объект:", deserialized_obj)
"""

"""
import pickle

class NotSerializedFields:
    def __init__(self, name, file_path, db_connection):
        self.name = name
        self.file = open(file_path, 'r')
        self.connection = db_connection

    def __getstate__(self):
        # Сохраняем только сериализуемые поля
        state = self.__dict__.copy()
        del state['file']  # Исключаем открытый файл
        del state['connection']  # Исключаем подключение к БД
        return state

    def __setstate__(self, state):
        # Восстанавливаем сериализуемые поля
        self.__dict__.update(state)
        # Восстанавливаем несериализуемые поля
        self.file = None  # Файл будет закрыт, нужно открыть заново
        self.connection = None  # Подключение нужно установить заново

    def close_resources(self):
        # Метод для закрытия ресурсов
        if self.file:
            self.file.close()
        if self.connection:
            self.connection.close()

    def __repr__(self):
        return (f"NotSerializedFields(name={self.name}, "
                f"file={'open' if self.file else 'closed'}, "
                f"connection={'active' if self.connection else 'closed'})")


obj = NotSerializedFields("Alice", "example.txt", "db_connection")
print("Оригинальный объект:", obj)

# Сериализация объекта
serialized_obj = pickle.dumps(obj)
print("Сериализованный объект:", serialized_obj)

# Десериализация объекта
deserialized_obj = pickle.loads(serialized_obj)
print("Десериализованный объект:", deserialized_obj)

# Закрываем ресурсы (если они были открыты)
obj.close_resources()
"""




