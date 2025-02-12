# Assignment 5:

"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return
the second_folder to last item in the specific list specified by the user of the function.

Определите функцию с именем key_list_items, которая может принимать неограниченное
количество списков вместе с другим аргументом.
Функция должна возвращать предпоследний элемент в конкретном списке,
 указанном пользователем функции.

Example:

    For example, the below function call should return: jan

    key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])

"""
from operator import index


# Your Code Below:

def key_list_items(item,**kwargs):

    '''
    Объяснение:
    key — это ключ, который указывает, из какого списка нужно взять второй с конца элемент.
    **kwargs — позволяет передавать неограниченное количество именованных аргументов, каждый
    из которых может быть списком.
    Проверка if key in kwargs: — проверяет, существует ли указанный ключ в переданных аргументах.
    if isinstance(target_list, list) and len(target_list) >= 2: — проверяем,
    что значение под ключом — это список и что в нем минимум 2 элемента.
    return target_list[-2] — возвращаем второй с конца элемент.
    '''

    # Проверяем, существует ли указанный список
    if  item in kwargs:
        second_folder = kwargs[item]
        # Проверяем, что это список и в нем достаточно элементов
        if isinstance(second_folder, list) and len(second_folder) >= 2:
            return second_folder[-2] # Возвращаем второй с конца элемент
    return None # Если ключ не найден или список не соответствует условиям

result = key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])

print(result) # Вывод: 'jan'













































# Solution:

def key_list_items(key, **kwargs):
    keys = kwargs[key]
    return keys[-2]

result = key_list_items("people", things=['book', 'tv', 'shoes'], people=['pete', 'mike', 'jan', 'tom'],
                ages=[20, 30, 40])
print(result)