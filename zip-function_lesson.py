# встроенная функция zip() объединяет два списка в список кортежей
from statistics import quantiles

# пример

fruits = ['apple', 'banana', 'cherry'] # фрукты

quantities = [0.25, 0.5, 0.75] # кг

availability = [True, False, True] # True - в наличии, False - нет в наличии

fruits_qty_zip = zip(fruits, quantities, availability)

print(type(fruits_qty_zip)) # <class 'zip'>

print(fruits_qty_zip) # <zip object at 0x7f9f1a9c8b40>

fruits_qty_zip = list(fruits_qty_zip) # преобразование zip object в список кортежей

print(fruits_qty_zip) # [('apple', 0.25), ('banana', 0.5), ('cherry', 0.75)] - список кортежей

print('\n') # пустая строка

 # если список заменить на набор, то он будет не упорядоченным
 # со строкой можно работать как с набором, но не наоборот

 # конвертация zip object в dict

fruits = ['apple', 'banana', 'cherry'] # фрукты

quantities = [0.25, 0.5, 0.75] # кг

fruits_qty_zip = zip(fruits, quantities) # объединение двух списков в zip object

fruits_qty_dict = dict(fruits_qty_zip) # конвертация zip object в dict. при конвертации zip object в dict,
# допускается только два аргумента в вызванной функции zip()

print(type(fruits_qty_dict)) # <class 'dict'>

print(fruits_qty_dict) # {'apple': 0.25, 'banana': 0.5, 'cherry': 0.75}


# практика

list_practice = ['apple', 'banana', 'cherry', 'date', 'elderberry'] # список фруктов

prices = [0.25, 0.5, 0.75, 1.0, 1.25] # цены

list = list(zip(list_practice, prices))

dict_arc = dict(list)

print(list) # [('apple', 0.25), ('banana', 0.5), ('cherry', 0.75), ('date', 1.0), ('elderberry', 1.25)]

print(dict_arc) # {'apple': 0.25, 'banana': 0.5, 'cherry': 0.75, 'date': 1.0, 'elderberry': 1.25}



