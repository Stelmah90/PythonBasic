from itertools import count, cycle


print('Генерим целые числа, начиная с указанного с каждым нажатием Enter. Для выхода жми "!"')
for number in count(int(input('Введи первое число: '))):
    print(number, end='')
    ext = input()
    if ext == '!':
        break

print('Повторяем элементы списка. Генерим каждое повторение кнокпой "Enter". Для выхода жми"!"')
user_list = input('Введи список чего-нибудь через пробел: ').split()
iter_ = cycle(user_list)
ext = None

while ext != '!':
    print(next(iter_), end='')
    ext = input()
