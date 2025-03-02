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