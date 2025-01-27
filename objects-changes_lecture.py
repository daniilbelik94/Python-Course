# неизменяемые объекты в памяти

# создание объекта
my_number = 100
print(id(my_number)) # адрес объекта в памяти

other_number = 100
print(id(other_number))  # адрес объекта в памяти

print(id(100))  # тот же адрес, так как small integer интернируется

print('\n')  # пустая строка для удобства чтения

# в случае использования неизменяемых объектов, которые уже существуют в памяти, Python не создает новый объект,
# а использует уже существующий

# еще пример
first_number = 100
second_number = first_number

print(id(first_number))  # адрес объекта в памяти
print(id(second_number))  # тот же адрес

second_number += 5  # изменение переменной

print(first_number)  # 100
print(second_number)  # 105

print(id(first_number))  # адрес объекта в памяти остался без изменений
print(id(second_number))  # адрес объекта в памяти изменился после изменения переменной

print('\n')  # пустая строка для удобства чтения

# изменяемые объекты в памяти

# создание объекта
my_list = [1, 2, 3]
print(my_list)  # [1, 2, 3]
print(id(my_list))  # адрес объекта в памяти

other_list = [1, 2, 3]  # создание нового объекта

other_list.append(4)  # изменение объекта
print(other_list)  # [1, 2, 3, 4]

print(id(other_list))  # адрес объекта в памяти изменился

print(id([1, 2, 3]))  # каждый раз создается новый объект/список

print('\n')  # пустая строка для удобства чтения

# изменение словаря
info = {'name': 'Daniil', 'is_instructor': True}
info_copy = info
info['reviews_qty'] = 10

print(info['reviews_qty'])  # 10

info_copy['reviews_qty'] = 15  # изменение объекта
print(info_copy['reviews_qty'])  # 15

print(info)  # {'name': 'Daniil', 'is_instructor': True, 'reviews_qty': 15}
print(info_copy)  # {'name': 'Daniil', 'is_instructor': True, 'reviews_qty': 15}

print(id(info))  # адрес объекта в памяти
print(id(info_copy))  # адрес объекта в памяти не изменился

# после копирования изменяемых объектов изменения отражаются на всех копиях

print('\n')  # пустая строка для удобства чтения

# как избежать изменения объектов через другие переменные

# через метод copy()
info = {'name': 'Daniil', 'is_instructor': True, 'reviews': []}
info_copy = info.copy()  # копирование словаря

info['reviews'].append('Great course!')  # изменение объекта

print(info)  # {'name': 'Daniil', 'is_instructor': True, 'reviews': ['Great course!']}
print(info_copy)  # {'name': 'Daniil', 'is_instructor': True, 'reviews': []}

# создание глубокой копии объекта
from copy import deepcopy  # импорт функции deepcopy

info = {'name': 'Daniil', 'is_instructor': True, 'reviews': []}  # создание объекта

info_deepcopy = deepcopy(info)  # создание глубокой копии объекта info

info_deepcopy['reviews'].append('Great course!')  # изменение объекта в глубокой копии

print(info)  # {'name': 'Daniil', 'is_instructor': True, 'reviews': []}
print(info_deepcopy)  # {'name': 'Daniil', 'is_instructor': True, 'reviews': ['Great course!']}



