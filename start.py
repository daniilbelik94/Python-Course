import sys
sys.stdin = open(0)


print("Hello world!")  # print это функция,
# вызов функции происходит с помощью скобок, 
# пример print("Hello world"), а внктри есть значение типа строка (string)

# функции вызываются с помощью def/ функция имеет имя и параметры

def my_function(a, b):
 a = a + 1 # тело функции
 b = 5
 c = a + b
 return c # возвращаемый результат


# input 

name = input("Enter your name: ")
print("Hello " + name)
# name you enter is a string



