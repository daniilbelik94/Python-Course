# range - диапазон чисел

# диапазон - упорядоченная неизменяемая последовательность элементов(чисел)

# диапазоны обычно используются в циклах  for

# стуктура и синтаксис range

my_range = range(7)

print(type(my_range)) # <class 'range'>

print(my_range) # range(0, 7)

print(list(my_range)) # [0, 1, 2, 3, 4, 5, 6]

print('\n') # пустая строка

# таким образом я могу создать диапазон чисел от 0 до 7 не включительно

# добавление шага в диапазон

my_range = range(10, 20, 3) # диапазон от 10 до 20 не включительно с шагом 3

print(type(my_range)) # <class 'range'>

print(my_range) # range(10, 20, 3)

print(list(my_range)) # [10, 13, 16, 19]

print('\n') # пустая строка

# индексы элементов в диапазонах

my_range = range(10, 20, 3) # диапазон от 10 до 20 не включительно с шагом 3

print(my_range[0]) # 10
print(my_range[1]) # 13
print(my_range[2]) # 16
print(my_range[3]) # 19
# print(my_range[4]) # IndexError: range object index out of range

print('\n') # пустая строка

# использование диапазонов в циклах
my_range = range(10, 20, 3) # диапазон от 10 до 20 не включительно с шагом 3

for i in my_range:
    print(i) # 10 13 16 19


# практика

my_range = range(5)

print(type(my_range)) # <class 'range'>
print(my_range) # range(0, 5) - от 0 до 5 не включительно
print(my_range[0]) # 0 - индексация начинается с 0

print('\n') # пустая строка

for i in my_range:
    print(i) # 0 1 2 3 4

print('\n') # пустая строка

# в словари конвертировать диапазон нельзя

my_range = range(10, 30, 3)

print(my_range.start) # 10
print(my_range.stop) # 30
print(my_range.step) # 3

print('\n') # пустая строка

print(my_range.count(13)) # 1 - количество элементов 13
print(my_range.index(19)) # 3 - индекс элемента 19

print('\n') # пустая строка

# задание

practice_range = range(10, 100, 4)
print(practice_range.start) # 10
print(practice_range.stop) # 100
print(practice_range.step) # 4

print('\n') # пустая строка

practice_list = list(practice_range)

for i in practice_list:
    print(i) # 10 14 18 22 26 30 34 38 42 46 50 54 58 62 66 70 74 78 82 86 90 94 98

print(practice_list)



