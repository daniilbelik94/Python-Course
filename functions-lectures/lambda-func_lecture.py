
# лямпда функции - это анонимные функции, которые могут содержать только одно выражение

# lambda arguments: expression

# def square(x):
#     return x ** 2

# square = lambda x: x ** 2

# print(square(5))  # 25 потому что 5 в квадрате равно 25

# замыкание - это функция, которая сохраняет значение переменной из внешней области видимости, даже если эта переменная
#
# уже не существует в этой области видимости.

def greeting(greet):
    return lambda name: f'{greet}, {name}'

morning_greet = greeting('Good morning')

print(morning_greet('John'))  # Good morning, 'John' - указание имени лямбда функции

evening_greet = greeting('Good evening') # Good evening, John

print(evening_greet('John'))  # Good evening, John

