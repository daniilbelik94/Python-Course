  # значения параметров по умолчанию


def mult_by_factor(value, multiplayer=1):
    return value * multiplayer

print(mult_by_factor(10,2)) # 20
print(mult_by_factor(10))# 10 наличие значения по умолчанию для параметра функции делает его необязательным

from datetime import date

def get_weekday():
  return date.today().strftime('%A') # возвращает текущий день недели, а ('%A') - это формат даты

def create_new_post(post,weekday=get_weekday()):
  post_copy = post.copy()
  post_copy['create_on_weekday'] = weekday
  return post_copy

initial_post = {
  'id': 2533,
    'title': 'Python functions',
    'content': 'Python functions are amazing',
    'author': 'Daniil Belik'
}

post_with_weekday = create_new_post(initial_post)

print(post_with_weekday) # {'id': 2533, 'title': 'Python functions', 'content': 'Python functions are amazing',
  # 'author': 'Daniil Belik', 'create_on_weekday': 'Tuesday'}






