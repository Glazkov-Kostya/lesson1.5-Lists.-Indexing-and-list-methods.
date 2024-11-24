# чтобы добавить эл. в конец списка используем команду .append
# .extend перебирает каждый символ
# .remove удаляет введенное значение
# in = проверка на наличие эл. в списке
# not in = проверка на отсутствие эл. в списке
food = ['apple', 'coconut', 'banana']
print(food[0])
food[0] = 'peach'
print(food)
food.append(True)
print(food)
food.extend('string')
print(food)
food.extend(['string', 2])
print(food)
food.remove('s')
print(food)
print('coconut' in food)
print('coconut' not in food)
print(food[0:2])
print(food[0:2:2])