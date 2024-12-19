# import sys
# sys.stdin = open(0)
#
#
# print("Hello world!")  # print это функция,
# # вызов функции происходит с помощью скобок,
# # пример print("Hello world"), а внктри есть значение типа строка (string)

# функции вызываются с помощью def/ функция имеет имя и параметры

# def my_function(a, b):
#  a = a + 1 # тело функции
#  b = 5
#  c = a + b
#  return c # возвращаемый результат


# input 

# name = input("Enter your name: ")
# print("Hello " + name)
# name you enter is a string

# встроенная функция dir

# name = 'Danii Belik'
# print(name.upper()) # функция dir отображает имена всех атрибутов обьекта

# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


# practice

# print (input)
# print (print)
# print (dir())
# <built-in function input>
# <built-in function print>
# <built-in function dir>

# name = input("Enter your name: ")
# ages = input("Enter your age: ")
# print(name.capitalize())
# print("Hello my dear " + name)
# print("Your age is " + ages)



# def my_name(name):
#     print("Hello my dear " + name)
#
# my_name("Daniil")
#
#
# my_list = [1, 2, 3, 4, 5]
#
# print(my_list)


# function

# def hello(name):
#     print("Hello,", name)
#     print("Hello world!")
#     print("Hello again!")
#
# # print("Hello there from outside of function!")
#
# hello('Daniel')


# def sum_nums(a, b):
#     sum = a + b
#     return sum
#
# first_sum = sum_nums(76, 7)
# print(first_sum) # 83
#
# print(sum_nums(1, 2)) # 3
#
# print(sum_nums(sum_nums(54,23),301)) # 77 + 379, добавляю в функцию ту же функцию с другим числом,таким образом
# # прибавляя её

