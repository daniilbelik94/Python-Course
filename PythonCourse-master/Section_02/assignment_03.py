# Assignment 3:
"""
There is a list shown below titled original_list.

Using only what you've learned so far in the course,
write code to create a new list that contains the tuple sorted.

IMPORTANT: you must do this programmatically! Don't just
      hard code a new list with the values rearranged.

      перевод:
        Есть список original_list.
        Используя только то, что вы узнали в курсе,
        напишите код для создания нового списка, содержащего отсортированный кортеж.

        ВАЖНО: вы должны сделать это программно! Не просто
        жестко закодируйте новый список с переупорядоченными значениями.

"""

original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]
print(original_list)

# your code below:

sorted_list = tuple(sorted(original_list[3]))
print(sorted_list)
new_list = original_list[:3] + [sorted_list]

print(new_list)

















































# Solution
# num1 = original_list[3][0]
# num2 = original_list[3][1]
# num3 = original_list[3][2]
# new_list = [num1, num2, num3]
# new_list.sort()
# new_tuple = (new_list[0], new_list[1], new_list[2])
# new_list = [original_list[0], original_list[1], original_list[2], new_tuple]
#
# print(new_list)