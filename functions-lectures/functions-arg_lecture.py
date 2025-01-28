#
# # аргументы функции
# #
# # аргументы изменяются внутри функции, если они изменяемые
# #
# # ошибка отсутствия аргумента
# #
# # def sum_nums(a, b):
# #     return a + b
# #
# # print(sum_nums(1)) # TypeError: sum_nums() missing 1 required positional argument: 'b'
# # print(sum_nums(1, 2)) # 3
# # print(sum_nums() # TypeError: sum_nums() missing 2 required positional arguments: 'a' and 'b'
# # print(sum_nums(1, 2, 3)) # TypeError: sum_nums() takes 2 positional arguments but 3 were given
#
# # обьеденение аргументов в tuple
#
# def sum_nums(*args): # *args - это tuple с аргументами(кортеж)
#     print(args) # (1, 2, 3)
#     print(type(args)) # <class 'tuple'>
#
#     print(args[0]) # 1
#     return sum(args)
#
# print(sum_nums(1, 2, 3)) # 6
#
# # позиционные аргументы
#
# def get_posts_info(name,post_qty):
#     info = f'{name} wrote {post_qty} posts' # f-string - форматирование строк
#     return info
#
# info = get_posts_info('John', 5) # позиционные аргументы
# print(info) # John wrote 5 posts
#
#
# # форматирование строк - это способ форматирования строк в Python,
# # который позволяет встраивать значения переменных в строки.
# #
# # пример форматирования строк:
#
# name = 'John'
# age = 25
# info = f'My name is {name}, I am {age} years old'
# print(info) # My name is John, I am 25 years old
#
# # аргументы с ключевыми словами
#
# def get_posts_info(name, post_qty):
#     info = f'{name} wrote {post_qty} posts'
#     return info
#
# info = get_posts_info(name='John', post_qty=5) # аргументы с ключевыми словами
# print(info) # John wrote 5 posts
#
# # использование аргументов с ключевыми словами делает код более читаемым и понятным
#
# print('\n') # печать пустой строки
#
# # обьеденение аргументов в словарь - dict
#
# def get_posts_info(**person): # **person - это словарь с аргументами
#     print(person) # {'name': 'John', 'post_qty': 5}
#     print(type(person)) # <class 'dict'>
#     info = (
#         f"{person['name']} wrote "
#         f"{person['post_qty']} posts" # если не ставить запятую то pyton будет считать что это одна строка
#     )
#     print(person['name']) # John
#     return info
#
# info = get_posts_info(name='John', post_qty=5) # аргументы с ключевыми словами
# print(info) # John wrote 5 posts
#
# print('\n')

# задачи - именнованые аргументы функции

# 1. создать функцию
# 2. у функции должно быть два параметра
# 3. функция должна обьединять два списка, используя встроенную функцию zip
# 4. конвертировать обьект зип в словарь и верните его из функции
# 5. вызовите функцию, передав ей два списка в качестве аргументов


# 6. переписать вызов функции чтобы в нем использовались аргументы с ключевыми словами
# 7. Добавить еще один вызов функции, в котором будет один позиционированный аргумент, а второй -
# аргументом с ключевым значением

# def merge_list_to_dict(fruits,prices): # создаю функцию и даю ей два аргумента
#     return dict(zip(fruits,prices))
#
# fruits = ['banana', 'orange', 'coconut', 'apple'] # создаю список из хуйни
# prices = [0.25, 0.50, 1.0, 0.10] # еще список из цифер, типа цены
#
# result = merge_list_to_dict(fruits,prices) # чтобы вывести результат даю константу для вывода функции с ее параметрами
# print(result) # имеем ключ/значение {'banana': 0.25, 'orange': 0.5, 'coconut': 1.0, 'apple': 0.1}
#
#
# def merge_list_to_dict(fruits,prices, **kwargs):
#     result = dict(zip(fruits,prices))
#
#     if kwargs:
#         for fruit,price in kwargs.items():
#             result[fruit] = price
#
#     return result
# fruits = ['banana', 'orange', 'coconut', 'apple'] # создаю список из хуйни
# prices = [0.25, 0.50, 1.0, 0.10] # еще список из цифер, типа цены
#
# added_fruits = 'cherry'
# added_price = 0.8
#
# result = merge_list_to_dict(fruits,prices, **{added_fruits:added_price})
# print(result)

# улучшенная версия кода

# Функция для объединения двух списков в словарь с возможностью добавления дополнительных элементов
# def merge_list_to_dict(fruits, prices, **kwargs):
#     # Создаем словарь из двух списков с помощью zip
#     result = dict(zip(fruits, prices))
#
#     # Если есть дополнительные элементы в kwargs, добавляем их в результат
#     result.update(kwargs)
#
#     return result  # Возвращаем итоговый словарь
#
# # Списки фруктов и их цен
# fruits = ['banana', 'orange', 'coconut', 'apple']
# prices = [0.25, 0.50, 1.0, 0.10]
#
# # Дополнительный фрукт и его цена
# added_fruits = 'cherry'
# added_price = 0.8
#
# # Вызов функции с передачей дополнительных аргументов через **kwargs
# result = merge_list_to_dict(fruits, prices, **{added_fruits: added_price})
# print(result)


# Задача:
# Напишите функцию, которая будет принимать два списка и дополнительный словарь,
# который может содержать значения для некоторых продуктов.
# Функция должна объединить два списка в словарь, где первый список будет ключами, а второй — значениями.
# Затем функция должна пройтись по ключам словаря и, если значение по ключу больше определённого
# порога (например, 1.0), заменить его на значение из дополнительного словаря.
# Вернуть итоговый словарь с обновлёнными значениями.


def upd_price(fruits, prices, **kwargs):
    # Создаем словарь из двух списков
    price_dict = dict(zip(fruits, prices))

    # Обновляем значения, если они есть в kwargs и больше 1.0
    for fruit, price in price_dict.items():
        if price > 1.0 and fruit in kwargs:
            price_dict[fruit] = kwargs[fruit]

    return price_dict


# Пример:
fruits = ['apple', 'banana', 'orange', 'grape']
prices = [0.8, 1.2, 0.5, 1.5]
updated_prices = {'banana': 1.3, 'grape': 1.6}

result = upd_price(fruits, prices, **updated_prices)
print(result)


# Если цена на «banana» больше 1.0, она должна быть обновлена до 1.3.
# Если цена на «grape» больше 1.0, она должна быть обновлена до 1.6.
# Результат должен содержать все продукты и их обновлённые цены.

# {
#     'apple': 0.8,
#     'banana': 1.3,  # обновлено, так как больше 1.0
#     'orange': 0.5,
#     'grape': 1.6   # обновлено, так как больше 1.0
# }

def  actual_prices(items, costs,**kwargs):
    dict_price = dict(zip(items,costs))
    for item,cost in dict_price.items():
        if cost >= 1.5 and item in kwargs:
            dict_price[item] = kwargs[item]
    return dict_price


items = ['bread', 'milk', 'butter', 'cheese', 'yogurt', 'honey']
costs = [1.0, 1.5, 2.0, 3.0, 0.8, 5.0]
new_prices = {'butter': 2.5, 'cheese': 3.5, 'honey': 4.8}

result = actual_prices(items,costs, **new_prices)
print(result)


def qty_upd(products,quantities,categories, **kwargs):
    list_zip = [{'product': product, 'quantity': quantity, 'category': category}
                for product,quantity,category in zip(products,quantities,categories)]
    for item in list_zip:
        product = item['product']
        quantity = item['quantity']

        if quantity > 10 and product in kwargs:
            item['quantity'] = kwargs[product]

    return list_zip


products = ['apple', 'banana', 'orange', 'milk', 'cheese', 'honey']
quantities = [5, 12, 8, 15, 7, 20]
categories = ['fruit', 'fruit', 'fruit', 'dairy', 'dairy', 'sweets']
updated_quantities = {'banana': 14, 'honey': 25}

result = qty_upd(products,quantities,categories, **updated_quantities)
print(result)

# Логика кода:
# Создание списка словарей:
#
# Функция zip объединяет три списка: products, quantities и categories в кортежи, которые потом
# конвертируются в словари.
# Каждый словарь содержит ключи 'product', 'quantity', и 'category', соответствующие продуктам,
# их количествам и категориям.
# Перебор списка словарей:
#
# Вы перебираете каждый элемент в list_zip, получая доступ к продукту, количеству и категории.
# Проверка и обновление количества:
#
# Если количество продукта больше 10 и продукт присутствует в словаре kwargs, то вы обновляете количество
# данного продукта в item['quantity'] значением из kwargs[product].
# Возвращение обновленного списка:
#
# Функция возвращает список словарей, где для продуктов, соответствующих условиям,
# обновлены значения количества.


def modify_prices(products,prices, **kwargs):
    result = dict(zip(products, prices))

    result.update(kwargs)

    return result


products = ['apple', 'banana', 'orange', 'grape']
prices = [1.2, 0.8, 1.5, 2.0]
updated_prices = {'banana': 1.0, 'grape': 1.8}
result = modify_prices(products, prices, **updated_prices)
print(result)


def update_car_info(brands, prices, **kwargs):
    # Создаем список с основными данными
    cars = [{'brand': brand, 'price': price}
            for brand, price in zip(brands, prices)]

    # Добавляем информацию из kwargs, обновляя список словарей
    for car in cars:
        brand = car['brand']
        if brand in kwargs:  # Проверяем, если в kwargs есть данный бренд
            car['is_available'] = kwargs[brand]  # Добавляем информацию о наличии

    return cars


brands = ['bmw', 'opel', 'audi', 'mercedes']
prices = [10000, 5000, 15000, 20000]
is_available = {'bmw': True, 'opel': True, 'audi': False, 'mercedes': False}

# Передаем is_available как словарь
car = update_car_info(brands, prices, **is_available)

# Выводим результат
print(car)




