# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.

    перевод:
    Создайте функцию с именем merge_lists, которая принимает 2 списка.
    Функция должна объединить оба этих списка вместе
    и вернуть результат.
    
"""

# your code below:

def merge_list(list1,list2):
    return list1 + list2


list1 = ['a', 'bc', 2, True]
list2 = [ 1.23, False, 'danil']

print(merge_list(list1,list2))









































# solution Below:

def merge_lists(list_a, list_b):
    return list_a + list_b

my_list = merge_lists([1,2,3],['a', 'b', 'c'])
print(my_list)