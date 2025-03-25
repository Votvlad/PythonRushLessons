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

# Работа с JSON посредством json

"""
import json
from datetime import datetime

class ExampleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {
    "city" : "London",
    "time_now" : datetime.now()
}

result = json.dumps(data, cls=ExampleEncoder, indent=2)
print(result)
"""

"""
import json
from datetime import datetime


def user_decoder(dct):
    if 'date_now' in dct:
        dct['date_now'] = datetime.fromisoformat(dct['date_now'])
    return dct


json_string = '''
{
    "city": "London",
    "date_now": "2023-05-15T14:30:00"
}
'''
data = json.loads(json_string, object_hook=user_decoder)
print(data)
"""

# Работа с сетью

"""
import requests

url = "https://jsonplaceholder.typicode.com/users"

params = {
    "username": "Samantha"
}


response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")
"""

"""
import requests

url = "https://httpbin.org/post"


form_data = {
    "username": "alice123",
    "password": "qwerty",
    "email": "alice@example.com"
}

response = requests.post(url, json=form_data)

print("Статус код:", response.status_code)
print("Ответ сервера:", response.json())
"""

# Работа с сетью на практике

"""
import requests

response = requests.get('https://vk.com')
print(response.status_code)
print(response.headers)
print(response.text)
"""

"""
import requests

try:
    response = requests.get('https://vkont.com')
    response.raise_for_status()  # Генерирует исключение для статус-кодов 4xx и 5xx
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")
else:
    print("Success!")
"""

# Используем HttpClient

"""
import http.client

try:
    # Создание подключения
    conn = http.client.HTTPSConnection("vk.com")

    # Отправка GET-запроса
    conn.request("GET", "/friends/")

    # Получение ответа
    response = conn.getresponse()
    print(response.status, response.reason)

    # Чтение и декодирование данных ответа
    data = response.read().decode('utf-8')
    print(data)

except http.client.HTTPException as e:
    print("HTTP error occurred:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    # Закрытие подключения
    conn.close()
"""


"""
import http.client

headers = {
    'Content-Type': 'application/json'
}

try:
    conn = http.client.HTTPSConnection("vk.com")
    conn.request("POST", "/friends", headers=headers)

    # Получение ответа
    response = conn.getresponse()
    print(response.status, response.reason)

    # Чтение и декодирование данных ответа
    data = response.read().decode('utf-8')
    print(data)

except http.client.HTTPException as e:
    print("HTTP error occurred:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    conn.close()
"""

# Используем Proxy

"""
import requests

url = 'http://vk.com'
proxies = {'http': 'http://79.117.21.113:8080', 'https': 'http://79.117.21.113:4321'}

response = requests.get(url, proxies=proxies)

try:
    response = requests.get(url, proxies=proxies)
    print(response.status_code)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
"""

"""
import http.client

proxy_host = '68.183.122.221'
proxy_port = 32890
dest_url = 'rutracker.org'
dest_path = '/get'

# Создание соединения с прокси-сервером
conn = http.client.HTTPConnection(proxy_host, proxy_port)

headers = {
    "Host": dest_url,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Формирование и отправка запроса
conn.set_tunnel(dest_url)
conn.request('GET', dest_path, headers=headers)

# Получение ответа
response = conn.getresponse()
print(response.status, response.reason)
print(response.read().decode('utf-8'))

# Закрытие соединения
conn.close()
"""

# Модуль socket

"""
import socket  # Импортируем модуль для работы с сокетами

server_socket = socket.socket(
    socket.AF_INET,      # Используем IPv4
    socket.SOCK_STREAM   # TCP-сокет (для UDP — SOCK_DGRAM)
)

host = '127.0.0.1'  # Локальный адрес (localhost)
port = 65432


# Привязываем сокет к адресу и порту
server_socket.bind((host, port))

# Начинаем слушать входящие подключения
server_socket.listen(1)  # Аргумент — максимальное количество подключений в очереди
print(f"Сервер запущен на {host}:{port}. Ожидание подключений...")

# Принимаем подключение
client_socket, client_address = server_socket.accept()  # Блокируется, пока не подключится клиент
print(f"Подключился клиент: {client_address}")

# Работаем с клиентом
with client_socket:  # Автоматически закроет сокет при выходе из блока
    while True:
        # Получаем данные от клиента (макс. 1024 байта)
        data = client_socket.recv(1024)
        if not data:  # Если данные пустые — клиент отключился
            break
        print(f"Получено от клиента: {data.decode('utf-8')}")

        # Отправляем ответ
        client_socket.sendall(b"Hello, client!")

# Закрываем серверный сокет (выполнится после выхода из with)
server_socket.close()
"""

"""
import socket

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Установка соединения с сервером
client_socket.connect(('127.0.0.1', 65432))

# Отправка данных на сервер
client_socket.sendall(b'Hello, server!')

# Получение данных от сервера
data = client_socket.recv(1024)
print(f"Получено от сервера: {data.decode('utf-8')}")

# Закрытие сокета
client_socket.close()
"""







