# Область видимости — это часть программы, в которой можно обращаться к определённой переменной или функции.
#
# В Python области видимости определяют, где и как можно использовать переменные.
#
# Понимание областей видимости помогает избежать очень серьезных проблем. Например,
# случайное переопределение
# глобальных переменных внутри функций или использование переменных до их объявления
# могут привести к трудноуловимым багам.
#
# Для определения последовательности, в которой Python ищет значение переменной, используется правило LEGB.
# Это правило представляет собой порядок поиска переменных в следующих областях видимости: Local (локальная),
# Enclosing (вложенная), Global (глобальная) и Built-in (встроенная).
#
# Сразу про встроенную область
# Встроенная область видимости в Python содержит предопределенные функции, типы и исключения, которые доступны
# в любой части программы. Эта область видимости загружается автоматом при запуске интерпретатора Python и доступна
# в любом месте программы.
#
# Python предоставляет множество встроенных функций и атрибутов. Некоторые из них:
#
# print() - используется для вывода данных на экран.
#
# len() - возвращает длину объекта (списка, строки и т.д.).
#
# type() - возвращает тип объекта.
#
# input() - считывает строку ввода от пользователя.
#
# int(), float(), str() - функции для преобразования типов данных.
#
# range() - генерирует последовательность чисел.
#
# sum() - возвращает сумму элементов последовательности.
#
# min(), max() - возвращают минимальный и максимальный элементы в последовательности.
#
# sorted() - возвращает отсортированный список.
#
# Локальная область видимости
# Локальная область видимости касается переменных, которые объявлены внутри функции или лямбда-выражения.
# Эти переменные доступны только в пределах функции, в которой они объявлены, и уничтожаются после завершения
# выполнения этой функции.
#
# Локальные переменные объявляются внутри функции и доступны только в рамках этой функции. Их область видимости
# ограничена телом функции, и они недоступны за ее пределами.

def greet():
    message = "Hello, World!"  # локальная переменная
    print(message)

greet()  # выведет: Hello, World!
 # print(message)  # ошибка: NameError, так как 'message' недоступна за пределами функции
# Лямбда-выражения также могут содержать локальные переменные, которые существуют только в контексте выполнения этой лямбды.

square = lambda x: x ** 2
print(square(5))  # выведет: 25
# Локальные переменные создаются при каждом вызове функции и уничтожаются после завершения ее выполнения.
# Т.е при каждом вызове функции создаются новые экземпляры локальных переменных, независимо от предыдущих вызовов.

def counter():
    count = 0  # локальная переменная
    count += 1
    print(count)

counter()  # выведет: 1
counter()  # выведет: 1 (новая переменная 'count' создается при каждом вызове функции)
# Примеры применения
# Локальные переменные отлично подходят для временного хранения промежуточных результатов, необходимых
# только в пределах одной функции:

def process_data(data):
    temp_result = []  # локальная переменная для временного хранения
    for item in data:
        temp_result.append(item * 2)
    return temp_result

data = [10, 20, 30]
print(process_data(data))  # выведет: [20, 40, 60]
# Лямбда-выражения часто используются в качестве аргументов функций, таких как map, filter и reduce:

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # выведет: [1, 4, 9, 16, 25]
# Закрытия позволяют внутренним функциям запоминать состояние их окружения:

def outer_function():
    message = "Hello"

    def inner_function():
        print(message)

    return inner_function

my_function = outer_function()
my_function()  # выведет: Hello
# Локальные переменные могут использоваться для управления состоянием внутри функции:

def search_item(data, target):
    found = False  # локальная переменная для отслеживания состояния
    for item in data:
        if item == target:
            found = True
            break
    return found

data = [1, 2, 3, 4, 5]
print(search_item(data, 3))  # выведет: True
print(search_item(data, 6))  # выведет: False

# Глобальная область видимости
# Глобальная область видимости в Python охватывает все переменные,
# определенные на самом верхнем уровне скрипта или модуля.
#
# Глобальные переменные объявляются вне всех функций и доступны для использования в любом месте программы.
# Их жизненный цикл продолжается на протяжении всего выполнения программы. Например:

global_var = "I am a global variable"

def print_global():
    print(global_var)

print_global()  # выведет: I am a global variable

# Для чтения глобальных переменных внутри функции никаких специальных действий не требуется.
# Однако для их изменения необходимо использовать ключевое слово global. Без этого ключевого слова Python создаст
# новую локальную переменную с тем же именем, что и глобальная, но не изменит глобальную переменную.
#
# Чтение глобальной переменной внутри функции:

count = 10

def print_count():
    print(count)  # использует глобальную переменную count

print_count()  # выведет: 10
# Модификация глобальной переменной внутри функции:

 # count = 10

def increment_count():
    global count
    count += 1

increment_count()
print(count)  # выведет: 11

# Примеры использования
# Использование глобальных переменных для хранения конфигурации:

config = {
    "host": "localhost",
    "port": 8080
}

def print_config():
    print(f"Host: {config['host']}, Port: {config['port']}")

print_config()
# Выведет: Host: localhost, Port: 8080
# Управление состоянием через глобальные переменные:

is_logged_in = False

def log_in():
    global is_logged_in
    is_logged_in = True

def log_out():
    global is_logged_in
    is_logged_in = False

def check_login_status():
    return "Logged in" if is_logged_in else "Logged out"

print(check_login_status())  # Выведет: Logged out
log_in()
print(check_login_status())  # Выведет: Logged in


# Глобальные переменные и многопоточность:

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        for _ in range(10000):
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(counter)  # ожидаемый результат: 100000

# Область видимости в пределах функции
# Вложенные функции — это функции, определенные внутри других функций. Вложенные функции могут обращаться к переменным,
# определенным в их внешних функциях. Эта способность делает возможным создание замыканий, где внутренняя функция
# запоминает контекст, в котором она была создана, даже после завершения выполнения внешней функции.
#
# nonlocal — это ключевое слово, используемое для объявления переменной, находящейся во внешней функции, но не в
# глобальной области видимости. Оно позволяет внутренней функции изменять значение этой переменной.

def outer_function():
    message = "Hello, World!"

    def inner_function():
        nonlocal message
        message = "Hello, Python!"

    inner_function()
    print(message)

outer_function()  # выведет: Hello, Python!


# nonlocal используется для указания, что переменная, находящаяся в локальной области видимости внутренней функции,
# должна быть связана с переменной, определенной во внешней функции. Так можно изменять переменные, которые находятся
# в области видимости между локальной и глобальной.

def outer_function():
    outer_var = "outer"

    def middle_function():
        middle_var = "middle"

        def inner_function():
            nonlocal outer_var, middle_var
            outer_var = "modified outer"
            middle_var = "modified middle"

        inner_function()
        print(middle_var)

    middle_function()
    print(outer_var)

outer_function()
# выведет:
# modified middle
# modified outer


# Примеры
# Фабричная функция возвращает вложенную функцию, которая использует переменные из внешней функции для выполнения своих задач:

def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # выведет: 10
print(triple(5))  # выведет: 15


# Счетчик вызовов функции, который отслеживает количество вызовов функции:

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

counter = make_counter()
print(counter())  # выведет: 1
print(counter())  # выведет: 2
print(counter())  # выведет: 3


# Декораторы часто используют вложенные функции для изменения поведения других функций:

def my_decorator(func):
    def wrapper():
        print("Что-то происходит перед функцией.")
        func()
        print("Что-то происходит после функции.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Выведет:
# Что-то происходит перед функцией.
# Hello!
# Что-то происходит после функции.
# Области видимости и встроенных функций позволяют создавать более структурированные программы без багов.