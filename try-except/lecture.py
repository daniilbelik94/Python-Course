

# получение ошибки в try/except блоке

try:
    print(2 ** 3 ** 2 ** 1)
except ZeroDivisionError as e: # обработка ошибки деления на ноль
    print(type(e)) # <class 'ZeroDivisionError'>
    print(e) # division by zero

print('continue...') # continue

2 ** 3 ** 2 ** 1  # здесь будет выполнено возведение в степень справа налево, т.е. 2 ** 3 = 8, 8 ** 2 = 64, 64 ** 1 = 64