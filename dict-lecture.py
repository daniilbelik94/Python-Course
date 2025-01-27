# словари -dict
from types import new_class

# словари это обекты

# словарь - набор элементов {ключ:значение}

# ключи - уникальные, неизменяемые объекты (числа, строки, кортежи)

# структура и синтаксис словарей

my_motorbike = {
    'brand': 'Honda',
    'price': 1000,
    'engine+vol': 1.200,
    'color': 'red',
    }

# порядок элементов в словаре не имеет никакого значения

other_motorbike = {
    'color': 'red',
    'brand': 'Honda',
    'price': 10000,
    'engine+vol': 1.200,
    }

print(my_motorbike == other_motorbike) # True - словари равны, порядок элементов не имеет значения

print('\n') # пустая строка для удобства чтения


# изменения и удаление значений в словарях

print(my_motorbike['price']) # 1000 - получение значения по ключу
print(my_motorbike['brand']) # Honda - получение значения по ключу

# чтобы изменений значение в словаре -

my_motorbike['price'] = 20000 # таким образом я меняю значение ключа price на 2000

print(my_motorbike['price']) # 2000 - получение значения по ключу

# для словарей ключи не являются атрибутами я не могу вызывать их через точку.
# Будет ошибка AttributeError: 'dict' object has no attribute 'price'

# print(dir(my_motorbike)) # список методов словаря

# добавление новых элементов в словарь

my_motorbike['year'] = 2020 # добавление нового элемента в словарь
my_motorbike['max-speed'] = 250 # добавление нового элемента в словарь
my_motorbike['is-new'] = True # добавление нового элемента в словарь

print(my_motorbike) # {'brand': 'Honda', 'price': 2000, 'engine+vol': 1.2, 'color': 'red', 'year': 2020, 'max-speed': 250}


print('\n') # пустая строка для удобства чтения

# удаление элементов из словаря

del my_motorbike['is-new'] # удаление элемента из словаря
print(my_motorbike) # {'brand': 'Honda', 'price': 2000, 'engine+vol': 1.2, 'color': 'red', 'year': 2020, 'max-speed': 250}

print('\n') # пустая строка для удобства чтения

# доступ к значению элемента с помощью переменной

key = 'brand' # ключ для доступа к значению бренда дя последующего изменения

my_motorbike[key] = 'Yamaha'

print(my_motorbike) # {'brand': 'Yamaha', 'price': 2000, 'engine+vol': 1.2, 'color': 'red', 'year': 2020, 'max-speed': 250}

print('\n') # пустая строка для удобства чтения


# вложенные словари

my_motorbike = {
    'brand': 'Honda',
    'price': 15000,
    'engine+vol': 1.200,
    'info': {
        'year': 2020,
        'max-speed': 250,
        'is-new': False,
        'is-available': True,
        }
    }

print(my_motorbike['info'] ['max-speed']) # 250 - доступ к значению вложенного словаря

# длинна словаря

print(len(my_motorbike)) # 4 - длинна словаря

del my_motorbike['info'] # удаление вложенного словаря

print(len(my_motorbike)) # 3 - длинна словаря

print('\n') # пустая строка для удобства чтения


# несуществующие ключи и метод get()

# print(my_motorbike['color']) # KeyError: 'color' - ошибка, так как ключа color нет в словаре

# метод get() - возвращает значение по ключу, если ключа нет, то возвращает None

print(my_motorbike.get('color')) # None - ключа color нет в словаре

# также можно задать значение методу get() по умолчанию

print(my_motorbike.get('color', 'black')) # black - ключа color нет в словаре, поэтому возвращается значение по умолчанию

print('\n') # пустая строка для удобства чтения

# атрибут __doc__

# my_dict = {}
#
# print(my_dict.__doc__) # dict() -> new empty dictionary - описание словаря

# dict() -> new empty dictionary
# dict(mapping) -> new dictionary initialized from a mapping object's
#     (key, value) pairs
# dict(iterable) -> new dictionary initialized as if via:
#     d = {}
#     for k, v in iterable:
#         d[k] = v
# dict(**kwargs) -> new dictionary initialized with the name=value pairs
#     in the keyword argument list.  For example:  dict(one=1, two=2)


# Пустой словарь
# Создается без аргументов:
d = dict()
print(d)  # Вывод: {}


# Словарь из объекта типа "mapping"
# Используем уже существующий объект с парами ключ-значение, например, другой словарь:
existing_dict = {'a': 1, 'b': 2}
d = dict(existing_dict)
print(d)  # Вывод: {'a': 1, 'b': 2}


# Словарь из итератора с парами
# Итератор или список кортежей вида (key, value):
pairs = [('x', 10), ('y', 20)]
d = dict(pairs)
print(d)  # Вывод: {'x': 10, 'y': 20}

# Словарь из именованных аргументов
# Создаeтся с помощью ключевых слов:
d = dict(one=1, two=2, three=3)
print(d)  # Вывод: {'one': 1, 'two': 2, 'three': 3}

print('\n') # пустая строка для удобства чтения


# практика по словарям


my_disk = {}

# print(id(my_disk)) # 2638620835648
# print(type(my_disk)) # <class 'dict'>

my_disk['brand'] = 'Seagate'
my_disk['price'] = 87.5
my_disk['capacity'] = 1.0

# print(my_disk) # {'brand': 'Seagate', 'price': 87.5, 'capacity': 1.0}
# print(id(my_disk)) # 2638620835648


print(my_disk.items())

print(type(my_disk.items())) # <class 'dict_items
print(my_disk.keys()) # dict_keys(['brand', 'price', 'capacity']) - список ключей
print(my_disk.popitem()) # ('capacity', 1.0) - удаляет последний элемент и возвращает его - для использования не рекомендуется

print('\n') # пустая строка для удобства чтения

new_disk = my_disk.copy() # копирование словаря

new_disk['type'] = 'ssd'
new_disk['capacity'] = 2.0

print(len(my_disk)) # 2 - длинна словаря
print(len(new_disk))  # 4 - длинна словаря


# конвертация в словарь с помощью dict()

my_list = [['first', 0], ['second', True], ['third', 'abc']]
my_dict = dict(my_list)

print(my_dict) # {0: 0, 1: True, 2: 'abc'} - конвертация списка в словарь


# практика по словарям


# 1. Создать пустой словарь

my_empty_dict = {}

# 2. Трижды попросите пользователя сначала ввести название ключа, а потом ввести значение для этого ключа.
# Всего должно быть 6

key_1 = input('Please enter key 1:')
value_1 = input('Please enter value 1:')

key_2 = input('Please enter key 2:')
value_2 = input('Please enter value 2:')

key_3 = input('Please enter key 3:')
value_3 = input('Please enter value 3:')


# 3. Во время получения данных от пользователя, добавляйте в словарь ключи с значениями согласно тому, что ввел пользователь

my_empty_dict[key_1] = value_1
my_empty_dict[key_2] = value_2
my_empty_dict[key_3] = value_3

# 4. Выводите результирующий словарь в терминал

print(my_empty_dict)
