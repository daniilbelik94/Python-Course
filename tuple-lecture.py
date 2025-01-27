# кортежи - неизменяемые списки

# кортежи нельзя изменять

# структура и синтаксис кортежа

my_fruits = ('apple', 'banana', 'cherry', 'date')

posts_ids = (151, 245, 762, 167)

user_inputs = (True, 'hi!', 5, 5.5)

# индикатором кортежа являются круглые скобки и запятые

# порядок в кортежах важен и два одинаковых списка с разным порядком элементов не равны друг другу

other_fruits = ('apple', 'cherry','banana', 'date')

print(my_fruits == other_fruits) # False

# изменить элементы кортежа нельзя
# удалять элементы кортежа нельзя


# my_fruits[0] = 'orange' # ошибка

# кортежи словарей и списков


users = (
    {'user-name': 'John',
     'age': 25,
     'users-id': 213},
    {'user-name': 'Jane',
     'age': 30,
     'users-id': 22},
    {'user-name': 'Jake',
     'age': 35,
     'users-id': 343}
)

print(users[2]['user-name']) # Jake

users[1]['age'] = 31 # изменение значения в словаре

print(users[1]['age']) # 31 - значение изменилось у Jane



print('\n') # пустая строка для удобства чтения

# использование переменных для кортежей


my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'cherry'

all_fruits = (my_fruit, other_fruit, new_fruit)

print(all_fruits) # ('apple', 'banana', 'cherry')


# методы кортежей их всего два
# count() - возвращает количество элементов в кортеже и ведет подсчет
# index() - возвращает индекс элемента в кортеже


# конвертация кортежа в список и наоборот

posts_ids = (151, 245, 762, 167)

posts_ids_list = list(posts_ids) # конвертация кортежа в список
posts_ids_list.append(100) # добавление элемента в список с помощью append() метода добавление в конец списка

print(posts_ids_list) # [151, 245, 762, 167, 100] - список

posts_ids_tuple = tuple(posts_ids_list) # конвертация списка в кортеж обратно

print(posts_ids_tuple) # (151, 245, 762, 167, 100) - кортеж
