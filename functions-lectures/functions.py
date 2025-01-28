import json

# функции - function

# функция это блок кода который можно выполнять многократно

a = 10
b = 4

c = a + b # 14
print(c)    # 14

a = 15
b = 5

c = a + b # 20
print(c)    # 20

# функция это блок кода который можно выполнять многократно

def sum(a, b):
    c = a + b
    print(c)

a = 10
b = 4

sum(a, b)   # 14

a = 15 
b = 5

sum(a, b)   # 20

print('\n')  # пустая строка для удобства чтения


# функция это обьект который можно присвоить переменной
# функция состоит из 2 частей: определение и вызов
# определение - это создание функции
# вызов - это выполнение функции

def sum(a, b): # определение функции
    a = a + 1 # тело функции
    c = a + b # тело функции
    return c # тело функции

result = sum(10, 4) # вызов функции

print(result)   # 15

print('\n')  # пустая строка для удобства чтения

# функцию нужно вызвать для выполнения кода внутри неё

# функция может принимать аргументы и возвращать значения

def my_fn(a, b): # объявление функции
    a = a + 1
    c = a + b
    return c # сдесь функция прекращает выполнение и возвращает значение

res = my_fn(10, 23) # вызов функции


print(res) # 34 - результат выполнения функции

# как это работает:
# 1. вызов функции my_fn(10, 23)
# 2. параметры a и b присваивается значения 10 и 23
# 3. a увеличивается на 1 и становится равным 11
# 4. c = 11 + 23 = 34
# 5. возвращаем значение c с помощью return
# 6. результат выполнения функции равен 34


print('\n')  # пустая строка для удобства чтения

# передача неизменяемых объектов в функцию

def my_fn(a, b):
    a = a + 1
    c = a + b
    return c

num_one = 10 # int
num_two = 5 # int

result = my_fn(num_one, num_two) # вызов функции
print(result)   # 16 - результат выполнения функции
print(num_one)  # 10 - переменная num_one не изменилась так как int неизменяемый объект


print('\n')  # пустая строка для удобства чтения

# передача изменяемых объектов в функцию

def increase_person_age(person):
    person['age'] += 1
    return person

person_one = {'name': 'John',
          'age': 25 # int
          } # dict

increase_person_age(person_one) # вызов функции
print(person_one['age'])   # 26 - результат выполнения функции

# как это работает:
# 1. вызов функции increase_person_age(person_one)
# 2. в функцию передается словарь person_one
# 3. в словаре изменяется значение ключа 'age' на 26
# 4. возвращаем словарь person_one с измененным значением ключа 'age'
# 5. результат выполнения функции равен 26


print('\n')  # пустая строка для удобства чтения

# внутри функции не рекомендуется изменять внешние объекты
# как избежать изменения внешних объектов внутри функции

# создание копии обьекта

def increase_person_age(person):
    person_copy = person.copy() # создание копии словаря
    person_copy['age'] += 1 # изменение копии словаря
    return person_copy # возвращение копии словаря

person_one = {'name': 'John',
            'age': 25
            } # dict

new_person = increase_person_age(person_one) # вызов функции копии словаря
print(person_one['age'])   # 25 - оригинальный словарь не изменился
print(new_person['age'])   # 26 - результат выполнения функции

print('\n')  # пустая строка для удобства чтения
# практическая задача

# 1. создать функцию
# 2. у функции должно быть два параметра
# 3. функция должна обьединять два списка,используя встроенную функцию zip
# 4. конвертировать обьект зип в словарь и верните его из функции
# 5. вызовите функцию, передав ей два списка в качестве аргументов

# решение

def merge_list_to_dict(fruits, prices): # создаю функцию и дую ей два аргумента
    dictionary = dict(zip(fruits,prices)) # конвертирую функцию в словарь
    return dictionary # возвращаю его

fruits = ['banana', 'orange', 'coconut', 'apple'] # создаю список из хуйни
prices = [0.25, 0.50, 1.0, 0.10] # еще список из цифер,типо цены

result = merge_list_to_dict(fruits,prices) # чтобы вывести результат даю констатну для вывода функции с ее параметрами
print(result) # имеем ключ/значение {'banana': 0.25, 'orange': 0.5, 'coconut': 1.0, 'apple': 0.1}


# Задача 1:
# Создайте функцию.
# У функции должно быть два параметра.
# Функция должна обьединять два списка, используя встроенную функцию zip.
# Конвертировать объект zip в список кортежей и вернуть его из функции.
# Вызовите функцию, передав ей два списка в качестве аргументов.


def tr_fn1(fruits,prices):
    tuple_dict = tuple(zip(fruits,prices))
    return tuple_dict

fruits = ['banana', 'orange', 'coconut', 'apple'] # создаю список из хуйни
prices = [0.25, 0.50, 1.0, 0.10] # еще список из цифер,типо цены

result = tr_fn1(fruits,prices)
print(result) # (('banana', 0.25), ('orange', 0.5), ('coconut', 1.0), ('apple', 0.1))


# Задача 2:
# Создайте функцию.
# У функции должно быть три параметра.
# Функция должна обьединять три списка, используя встроенную функцию zip.
# Конвертировать объект zip в список словарей, где ключи – элементы первого списка, значения – элементы второго
# и третьего списков, и вернуть его из функции.
# Вызовите функцию, передав ей три списка в качестве аргументов.

def fn_tr2(fruits,prices,kilo):
    return {fruit: (price, kilo) for fruit,price, kilo in zip(fruits,prices,kilo)}

fruits = ['banana', 'orange', 'coconut', 'apple'] # создаю список из хуйни
prices = [0.25, 0.50, 1.0, 0.10] # еще список из цифер,типо цены
kilo = [1.2, 4.1, 5,2]
# тут я задаю ключ фрукту и определяю его значения через фор где разбиваю списки на элементы и спаковываю все в зип

result = fn_tr2(fruits,prices,kilo)
print(result)


# Задача 3:
# Создайте функцию.
# У функции должно быть два параметра.
# Функция должна обьединять два списка, используя встроенную функцию zip.
# Конвертировать объект zip в строку формата JSON и вернуть её из функции.
# Вызовите функцию, передав ей два списка в качестве аргументов.


def fn_tr3(stroke,qty):
    list_dict = dict(zip(stroke,qty)) # чтобы вызывать джсон нужно сначало списки перевести в словарь
    return json.dumps(list_dict,indent=4)
# для улучшения и оптимизации кода можно в result передать сразу return json.dumps(list_dict,indent=4)

stroke = ['avc', 'a', 'fdg', '34', 'vb', 'c']
qty = [21, 50, 4.1, 76, 4.2, 98,3]



result = fn_tr3(qty,stroke)
# json_data = json.dumps(result) # json.dumps конвертация в json
print(result)

# Задание (усложнённая версия):
# Напиши функцию, которая принимает три списка:
#
# Первый список содержит названия продуктов.
# Второй список содержит цены этих продуктов.
# Третий список содержит количество доступных единиц каждого продукта.
# Функция должна:
#
# Объединить три списка с помощью zip().
# Преобразовать результат в список словарей, где:
# Ключ "name" — это элемент из первого списка (название продукта).
# Ключ "price" — элемент из второго списка (цена).
# Ключ "quantity" — элемент из третьего списка (количество).
# Отфильтровать список так, чтобы включить только товары, у которых количество больше 0.
# Вернуть результат.
# Дополнительно:
#
# Добавь проверку: если списки разной длины, выбрось исключение ValueError.
# Сделай так, чтобы результат был отсортирован по цене (от дешёвого к дорогому).




def lists(names,prices,quantities):
    result = [] # для начала нужно создать пустой словарь куда все будет выводится
    for fruit, price,quantity  in zip(names, prices, quantities): # проводим итерацию по спискам
        if quantity > 0: # ищем где больше 0 - клво
            result.append({"name": fruit, "price": price, "quantity": quantity})
    return result

names = ["Apple", "Banana", "Cherry", "Date"]
prices = [1.2, 0.5, 2.5, 3.0]
quantities = [10, 0, 5, 2]

result = lists(names,prices,quantities)
print(result) # [
#     {"name": "Apple", "price": 1.2, "quantity": 10},
#     {"name": "Cherry", "price": 2.5, "quantity": 5},
#     {"name": "Date", "price": 3.0, "quantity": 2}
# ]


# Задача:
# Напиши функцию, которая принимает три списка:
#
# names — названия товаров.
# prices — цены этих товаров.
# categories — категория каждого товара (например, "фрукты", "овощи", "напитки").
# Функция должна:
#
# Объединить три списка с помощью zip().
# Вернуть словарь, где ключами будут названия товаров из списка names, а значениями будут словари с двумя ключами:
# "price" — цена товара из списка prices.
# "category" — категория товара из списка categories.
# Вернуть только те товары, которые принадлежат категории "фрукты" (если категория не "фрукты", товар не включается
# в результат).



# Ожидаемый результат:
# {
#     "Apple": {"price": 1.2, "category": "fruits"},
#     "Banana": {"price": 0.5, "category": "fruits"},
#     "Orange": {"price": 0.8, "category": "fruits"}
# }

def true_category(names,prices,categories):
    result = {} # created DICT for print
    for name, price, category in zip(names,prices,categories):
        if category == 'fruits':
            result[name] = {'price': price, 'category': category}
    return result


# Пример входных данных:
names = ["Apple", "Banana", "Carrot", "Orange", "Milk"]
prices = [1.2, 0.5, 2.0, 0.8, 1.5]
categories = ["fruits", "fruits", "vegetables", "fruits", "dairy"]

result = true_category(names,prices,categories)
print(result)



# У тебя есть список продуктов с их ценами и количествами. Напиши функцию, которая будет принимать три списка:
#
# products — список с названиями продуктов.
# prices — список с ценами продуктов.
# quantities — список с количеством каждого продукта на складе.
# Твоя задача:
#
# Посчитать стоимость каждого продукта на складе (цена * количество).
# Если общая стоимость продукта на складе превышает определённую сумму (например, 10), этот продукт должен
# попасть в итоговый результат.
# Итоговый результат должен быть словарем, где ключом является название продукта, а значением — словарь,
# содержащий цену, количество и общую стоимость.

# Пример:
# Входные данные:

def totalPrice(products,prices,quantities):
    result = {}
    for product,price, quantity in zip(products,prices,quantities):
        if price * quantity >= 10:
            result[product] = {'quantity': quantity, 'total_cost': price * quantity}
    return result

products = ["Apple", "Banana", "Carrot", "Milk", "Cheese"]
prices = [2.0, 1.5, 0.8, 3.0, 5.0]
quantities = [5, 10, 8, 3, 2]


result = totalPrice(products,prices,quantities)
print(result)

# Выход:
# {
#     "Apple": {"price": 2.0, "quantity": 5, "total_cost": 10.0},
#     "Banana": {"price": 1.5, "quantity": 10, "total_cost": 15.0},
#     "Cheese": {"price": 5.0, "quantity": 2, "total_cost": 10.0}
# }
# Подсказки:
# Используй цикл zip для объединения продуктов, цен и количеств.
# Рассчитай общую стоимость как price * quantity.
# Применяй условие для фильтрации продуктов, где общая стоимость больше 10.





# Хорошо, вот задача чуть сложнее, которая потребует работы с фильтрацией и дополнительными операциями:
#
# Задача:
# Ты получаешь список продуктов с их ценами, количеством и категориями. Напиши функцию, которая будет
# принимать эти три списка:
#
# products — список с названиями продуктов.
# prices — список с ценами продуктов.
# quantities — список с количеством каждого продукта на складе.
# categories — список с категориями для каждого продукта.
# Твоя задача:
#
# Посчитать стоимость каждого продукта на складе (цена * количество).
# Если общая стоимость продукта на складе больше 20, этот продукт должен попасть в итоговый результат.
# Итоговый результат должен быть разделен на две части:
# Продукты, которые принадлежат категории "fruits" (фрукты).
# Продукты, которые принадлежат категории "vegetables" (овощи).
# Результат должен быть словарем, в котором два ключа: "fruits" и "vegetables". Значением для каждого ключа должен быть
# список продуктов, где каждый продукт представлен как словарь с ключами: "name", "price", "quantity" и "total_cost".

def totalPrice(products, prices, quantities, categories):
    result = {'fruits': [], 'vegetables': []} # помимо пустого словаря я так же добавил списки
    for product, price, quantity, categorie in zip(products, prices, quantities, categories):
        total_cost = price * quantity # изначально сделал полную сумму из цены и клва
        if total_cost >= 20: # определил что цена должна быть больше 20
            if categorie == 'fruits': # сортировка по категориям
                result['fruits'].append({
                    'name': product,
                    'price': price,
                    'quantity': quantity,
                    'total_cost': total_cost
                })
            elif categorie == "vegetables":
                result['vegetables'].append({
                    'name': product,
                    'price': price,
                    'quantity': quantity,
                    'total_cost': total_cost
                })
    return result

products = ["Apple", "Banana", "Carrot", "Milk", "Cheese"]
prices = [2.0, 1.5, 0.8, 3.0, 5.0]
quantities = [15, 10, 25, 3, 2]
categories = ["fruits", "fruits", "vegetables", "dairy", "dairy"]

result = totalPrice(products, prices, quantities, categories)
print(result)
# {
#     "fruits": [
#         {"name": "Apple", "price": 2.0, "quantity": 15, "total_cost": 30.0},
#         {"name": "Banana", "price": 1.5, "quantity": 10, "total_cost": 15.0}
#     ],
#     "vegetables": [
#         {"name": "Carrot", "price": 0.8, "quantity": 25, "total_cost": 20.0}
#     ]
# }
