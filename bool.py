
# bool логический тип данных, который может принимать одно из двух значений: True или False.

# Логические операторы:

# and - возвращает True, если оба операнда истинны

# or - возвращает True, если хотя бы один из операндов истинный

# not - возвращает True, если операнд ложный

# Примеры:

print("Logische Operatoren:")

print("True and False:", True and False)  # False

print("not True:", not True)  # False

print("False or True:", False or True)  # True

print("\n") # пустая строка для удобства чтения

#================================================================

is_authorized = True

print(is_authorized) # True

print(type(is_authorized)) # <class 'bool'> - тип данных

# bool часто используется при проверке правильности ввода данных пользователем

# Пример результа выражений с использованием bool:

print("\n") # пустая строка для удобства чтения

print(100 > 24) # True - 100 больше 24

print(-5> 0) # False - отрицательное число меньше нуля

print('long string' > 'long') # True - сравнение строк. посимвольное сравнение

print( [1, 2, 3] == [1, 2, 3]) # True - сравнение списков


# ================================================================

# конвертация в логическое значение с помощью bool()

print("\n") # пустая строка для удобства чтения

db_is_available = True

print(db_is_available) # True

db_is_available = False
print(db_is_available)

print(type(db_is_available)) # <class 'bool'> - тип данных

