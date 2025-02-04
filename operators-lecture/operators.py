

# операторы - это специальные символы, которые выполняют операции над операндами

# арифметические операторы

# сложение +
print(5 + 3)  # 8

# вычитание -
print(5 - 3)  # 2

# умножение *
print(5 * 3)  # 15

# деление /
print(5 / 3)  # 1.6666666666666667

# целочисленное деление //
print(5 // 3)  # 1

# остаток от деления %
print(5 % 3)  # 2

# возведение в степень **
print(5 ** 3)  # 125

# операторы сравнения
print(5 == 3)  # False
print(5 != 3)  # True
print(5 > 3)  # True

# операторы присваивания
x = 5
print(x)  # 5

x += 3
print(x)  # 8 # x = x + 3

x -= 3 # x = x - 3

# логические операторы

# and - логическое умножение
print(True and True)  # True

# or - логическое сложение
print(True or False)  # True

# not - логическое отрицание
print(not True)  # False

# операторы принадлежности

# in - проверяет, содержится ли элемент в последовательности
print(5 in [1, 2, 3, 4, 5])  # True

# not in - проверяет, не содержится ли элемент в последовательности
print(5 not in [1, 2, 3, 4, 5])  # False

# операторы тождественности

# is - проверяет, являются ли два объекта одним и тем же объектом
x = [1, 2, 3] # создаем список
y = [1, 2, 3] # создаем список
print(x is y)  # False

# is not - проверяет, являются ли два объекта разными объектами
print(x is not y)  # True

# операторы приоритета
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. <, <=, >, >=, !=, ==
# 6. not
# 7. and
# 8. or

print('\n')

# задача

my_set = {"apple", "banana", "cherry"}

my_second_set = {"apple", "banana", "cherry"}

print(my_set == my_second_set) # true
print(my_set is my_second_set) # false
# print(id(my_second_set))# false
# print(id(my_set))
print('apple' in my_set) # true

# 1.два набора идентичны так как в них находятся одинковые уникальные элементы. пайтон сравнивает значения находящиеся в них
# 2. выводит false так как имеет другое название и место в памяти
# 3 true так как этот уникальный эжлемент есть в наборе



