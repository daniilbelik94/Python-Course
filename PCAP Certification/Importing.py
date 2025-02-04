# Importing a module: continued
# Look at the snippet below, this is the way in which you qualify the names of pi and sin with the name of its
# originating module:
#
# math.pi
# math.sin

import math
print(math.sin(math.pi/2))

# It's simple, you put:

# the name of the module (e.g., math)
# a dot (i.e., .)
# the name of the entity (e.g., pi)
# Such a form clearly indicates the namespace in which the name exists.
#
# Note: using this qualification is compulsory if a module has been imported by the import module instruction.
# It doesn't matter if any of the names from your code and from the module's namespace are in conflict or not.


# This first example won't be very advanced - we just want to print the value of sin(½π).
#
# Look at the code in the editor. This is how we test it.
#
# The code outputs the expected value: 1.0.
#
# Note: removing any of the two qualifications will make the code erroneous. There is no other way to enter math's
# namespace if you did the following:
#
# import math

# В приведенном коде демонстрируется использование модуля `math` для выполнения математических операций в Python.
#
# Сначала импортируется модуль `math`, что позволяет использовать его функции и константы:
# ```python
# import math
# ```
#
# Затем используется функция `math.sin` для вычисления синуса угла, заданного в радианах.
# В данном случае вычисляется синус угла \(\frac{\pi}{2}\):
# ```python
# print(math.sin(math.pi/2))
# ```
#
# Результат выполнения этого кода будет равен 1.0, так как синус угла \(\frac{\pi}{2}\) равен 1.
#
# Важно отметить, что для доступа к функциям и константам модуля `math` необходимо использовать полное имя,
# включающее имя модуля и имя функции или константы, разделенные точкой. Например, `math.pi` и `math.sin`.
# Это позволяет явно указать пространство имен, в котором находится данная функция или константа, и избежать
# конфликтов имен.
#
# Если убрать любое из этих квалификаций, код станет ошибочным, так как не будет другого способа войти в
# пространство имен модуля `math`:
# ```python
# # Неправильно:
# print(sin(pi/2))  # вызовет ошибку
# ```
#
# Таким образом, использование полного имени модуля и его функций или констант является обязательным
# при импорте модуля с помощью инструкции `import module`.


# ==================================================================================================



# Importing a module: continued
# Now we're going to show you how the two namespaces (yours and the module's one) can coexist.
#
# Take a look at the example in the editor window.
#
# We've defined our own pi and sin here.
#
# Run the program. The code should produce the following output:
#
# 0.99999999
# 1.0
# output
#
# As you can see, the entities don't affect each other.

import math


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))


# В приведенном коде демонстрируется использование модуля `math` для выполнения математических операций в Python.
#
# Сначала импортируется модуль `math`, что позволяет использовать его функции и константы:
# ```python
# import math
# ```
#
# Затем используется функция `math.sin` для вычисления синуса угла, заданного в радианах.
# В данном случае вычисляется синус угла \(\frac{\pi}{2}\):
# ```python
# print(math.sin(math.pi/2))
# ```
#
# Результат выполнения этого кода будет равен 1.0, так как синус угла \(\frac{\pi}{2}\) равен 1.
#
# Важно отметить, что для доступа к функциям и константам модуля `math` необходимо использовать полное имя,
# включающее имя модуля и имя функции или константы, разделенные точкой. Например, `math.pi` и `math.sin`.
# Это позволяет явно указать пространство имен, в котором находится данная функция или константа,
# и избежать конфликтов имен.
#
# Если убрать любое из этих квалификаций, код станет ошибочным, так как не будет другого способа
# войти в пространство имен модуля `math`:
# ```python
# # Неправильно:
# print(sin(pi/2))  # вызовет ошибку
# ```
#
# Таким образом, использование полного имени модуля и его функций или констант является
# обязательным при импорте модуля с помощью инструкции `import module`.


# ========================================================================================================

from math import sin, pi

print(sin(pi / 2))




