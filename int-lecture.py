# =======================================================================

# целые числа - int

# структура и синтаксис

# friends_quantity = 50
#
# print(friends_quantity) # 50
#
# print(type(friends_quantity)) # <class 'int'> - тип данных
#
# #каждое целое число - это экземпляр класса int
#
# # числа и пользовательский ввод
#
# any_number = input('Enter any number: ')
#
# print(any_number) # 5 - ввод пользователя
#
# print(type(any_number)) # <class 'str'> - тип данных
#
# # тип данных получены от пользователя всегда строка по-этому print(type(any_number)) выводит строку после input а не число
#
# # ================================================================
#
# # концертация строк в числа
#
# user_input = input('Enter any number: ')
#
# any_number = int(user_input) # конвертация строки в число с помощью int()
#
# print(any_number)
#
# print(type(any_number)) # <class 'int'> - тип данных после конвертации
#
# #так же можно конвертировать в целое число без использования дополнительной переменной
#
# any_num = int(input('Enter any number: ')) # конвертация строки в число с помощью int()
#
# print(any_num) # 5 - ввод пользователя
#
# print(type(any_num)) # <class 'int'> - тип данных после конвертации

# ================================================================

# арифметические операции с целыми числами (возведение в степень)

# base = 2
# power = 3
#
# print(pow(base, power)) # 8 - 2 в степени 3 (2*2*2)
#
# #================================================================
#
# # длинные числа
#
# # длинные числа - это числа, которые не помещаются в стандартный размер int
#
# one_million = 1_000_000 # 1000000 разделение с помощью _ для удобства чтения
#
# print(one_million) # 1000000
#
# my_number = 3_553
#
# print(my_number) # 3553
#
# # ================================================================
#
# # практика
#
#
# input_str = input('Enter any number: ')
# input_int = int(input_str)
#
# print(input_str)
# print(input_int)
#
# print(type(input_str)) # <class 'str'> - тип данных
# print(type(input_int)) # <class 'int'> - тип данных

# ================================================================

#pow() - возведение в степень
#
# base = 42.4
# power = 2
#
# print(pow(base, power)) # 2025 - 45 в степени 2 (45*45) - результат float
# print(type(pow(base, power))) # <class 'float'> - тип данных
#
# #float - это числа с плавающей точкой, поэтому результат float
#
# # потому что base - float. Если base - int, то результат будет int
#
# base = 42
# power = 2
#
# print(pow(base, power)) # 1764 - 42 в степени 2 (42*42) - результат int
# print(type(pow(base, power))) # <class 'int'> - тип данных
# # ================================================================
#
# long_int = 1_000_000_000
#
# print(long_int) # 1000000000   - длинное число
#
#
# # ================================================================
#
# # конвертаця в float с помощью float()
#
# avarage_price = 5.43 # при конвертации в int, дробная часть отбрасывается
# price = int(avarage_price)
#
# print(price) #  результат int 5, при конвертации в int, дробная часть отбрасывается\
# print(type(price)) # <class 'int'> - тип данных
#
# str_temperature = '15.4' # строка
# temperature = float(str_temperature) # конвертация строки в float. также можно конвертировать между str, int, float
#
# print(temperature) # 15.4 - результат float
# print(type(temperature)) # <class 'float'> - тип данных



# ================================================================

# практика

# int_temp = 5.43 # float
# print(int(int_temp)) # 5 - результат int
# print(type(int_temp)) # <class 'float'> - тип данных
#
# temperatures = str(5.43) # str
#
# print(type(temperatures)) # <class 'str'> - тип данных
# temperatures = float(5.43) # float
#
# print(str(temperatures)) # 5 - результат int
# print(type(temperatures)) # <class 'float'> - тип данных

# ================================================================

# операции с комлпексными числами

complex_a = 10 + 7j # комплексное число
complex_b = 3 + 3j # комплексное число

print(complex_a - complex_b) # 13 + 10j - результат сложения комплексных чисел

print(complex_a * complex_b) # 9 + 51j - результат умножения комплексных чисел (10*3 + 10*3j + 7j*3 + 7j*3j)

