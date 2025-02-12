# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

перевод: Дан список целых чисел, верните True, если последовательность чисел 1, 2, 3
появляется в списке где-либо, в противном случае - false.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""



# Your Code Below:

def sequence(num_list):
    # Проверяем, что список содержит хотя бы 3 элемента
    if len(num_list) < 3:
        return False
    for i in range(len(num_list) - 2):
        # Ищем последовательность [1, 2, 3]
        if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
            return True
    return False

sequence([1, 1, 2, 3, 1])
sequence([1, 1, 2, 4, 1])
sequence([1, 1, 2, 1, 2, 3])
sequence([1, 2])
sequence([])

# Тестовые случаи
print(sequence([1, 1, 2, 3, 1]))  # True, потому что есть [1, 2, 3]
print(sequence([1, 1, 2, 4, 1]))  # False, нет [1, 2, 3]
print(sequence([1, 1, 2, 1, 2, 3]))  # True, потому что есть [1, 2, 3]
print(sequence([1, 2]))  # False, список слишком короткий
print(sequence([]))  # False, список пустой





































# Solution:

# def sequence(num_list):
#     # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False
