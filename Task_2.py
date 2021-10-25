user_list = input('Введите список слов через пробел: ').split(' ')
# print(user_list)
for element in range(0, len(user_list) if len(user_list) % 2 == 0 else len(user_list) - 1, 2):
    user_list[element], user_list[element + 1] = user_list[element + 1], user_list[element]
print(user_list)
