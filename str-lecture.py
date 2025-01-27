#=======================================================================

str - строки

greeting = 'Hello, World!'
print(greeting) #  Hello, World!

print(type(greeting)) # <class 'str'> - тип строки
print(id(greeting)) # 2772370586736 - айди строки

#многострочные строки

info_msg = '''Hello, World!
This is a multi-line string.
It can span multiple lines.
'''

print(info_msg) # Hello, World! This is a multi-line string. It can span multiple lines. - выводит текст в несколько строках


long_str = 'This is a very long string. It can span multiple lines. '

print(long_str) # This is a very long string. It can span multiple lines. - выводит текст в одну строку

print(type(long_str)) # <class 'str'> - тип строки
print(type(str)) # <class 'type'> - тип строки встроенный тип данных
print(type(int)) # <class 'type'> - тип числа встроенный тип данных
print(id(long_str)) # 2772370586736 - айди строки

#=======================================================================
# встроенные функции и строки
#
# len() - длина строки
# str() - преобразует в строку
# int() - преобразует в число
# float() - преобразует в число с плавающей точкой
# bool() - преобразует в булевый тип
# type() - возвращает тип данных
#
#
#
# [] - можно использовать для всех упорядоченных последовательностей