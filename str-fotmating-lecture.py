 # форматирование строк в Python

# пример форматирования строк:
import string

name = 'John'
age = 25
info = f'My name is {name}, I am {age} years old'
# info = info.title() # My Name Is John, I Am 25 Years Old

info = ' '.join(word.capitalize() for word in info.split()) # My Name Is John, I Am 25 Years Old
print(info) # My name is John, I am 25 years old

# в f строка можно использовать значения других типов


my_name = 'Danil'
my_age = 30
my_height = 186.5
my_weight = 87.6
my_eyes = 'brown'

info = f'My name is {my_name}, I am {my_age} years old, my height is {my_height} cm, my weight is {my_weight} kg, my eyes are {my_eyes}'

print(info) # My name is Danil, I am 30 years old, my height is 186.5 cm, my weight is 87.6 kg, my eyes are blue