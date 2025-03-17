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