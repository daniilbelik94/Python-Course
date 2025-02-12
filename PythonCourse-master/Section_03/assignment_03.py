# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

перевод:
Создайте функцию с именем multi_merge, которая принимает список и строку
в качестве аргументов.

Функция должна вернуть объединенный список
содержащий исходный аргумент списка, а также каждое из слов, которые есть в
аргументе строки, в дополнение к каждому из символов в строке
аргумент как отдельные элементы в списке.



"""
# Your Code Below:

def multi_merge(list_a, str):
    return list_a + str.split() + list(str) # Разбиваем строку на слова и символы

print(multi_merge([1,2,3,4], "Hello My name is imtiaz"))

print(multi_merge("Hello My name is imtiaz",[1,2,3,4]))

# [1, 2, 3, 4, 'Hello', 'My', 'name', 'is', 'imtiaz', 'H', 'e', 'l', 'l', 'o',
# ' ', 'M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'i', 'm', 't', 'i', 'a', 'z']

def multi_merge(stroke,list_a):
        return list_a + stroke.split() + list(stroke)







































# Solution:

def multi_merge(list_a, str):
    return list_a + str.split() + list(str)

print(multi_merge([1,2,3,4], "Hello My name is imtiaz"))
