 # callback function - это функция, которая передается в качестве аргумента другой функции и вызывается внутри этой функции.

def other_fn():
     pass

def fn_with_callback(callback_fn):
     callback_fn()

fn_with_callback(other_fn)

# коллбэк

# В приведенном коде реализована функция обратного вызова (callback function), которая передается в качестве аргумента
#  другой функции и вызывается внутри этой функции.
#  Функция print_number_info принимает один параметр num и проверяет, является ли это число четным или нечетным.
#  В зависимости от результата проверки, функция выводит соответствующее сообщение:
def print_number_info(num):
    if (num % 2) == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

# Функция process_numbers принимает два параметра: число num и функцию обратного вызова callback_fn.
#  Внутри этой функции вызывается переданная функция обратного вызова с аргументом num:

def process_numbers(num, callback_fn):
    callback_fn(num)

 # основной части кода пользователь вводит число с помощью функции input, преобразует его в целое число и передает в
 # функцию process_numbers вместе с функцией обратного вызова print_number_info:
def print_square_number(num):
    print(f'{num} in square is {num**2}')

entered_num = int(input('Enter a number: '))
process_numbers(entered_num, print_number_info)
process_numbers(entered_num, print_square_number)

# Таким образом, когда пользователь вводит число, функция process_numbers вызывает функцию print_number_info,
#  которая определяет, является ли введенное число четным или нечетным, и выводит соответствующее сообщение.


def send_data(data):
    pass

def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()

    send_data_fn(updated_data)

process_data({'name': 'John', 'age': 25}, send_data)

# В приведенном коде определены две функции: send_data и process_data.
#  Функция send_data принимает один параметр data и выполняет какие-то действия с этими данными.
#  Функция process_data принимает два параметра: input_data и функцию обратного вызова send_data_fn.
#  Внутри функции process_data создается копия входных данных input_data, которая затем передается в функцию обратного вызова send_data_fn.




