def int_func(string):
    return string.title()


us_str = input('Введите латинские слова через пробел: ')
if us_str.isascii() and us_str.isascii() and us_str.islower() is False:
    print('Неверные данные')
else:
    print(int_func(us_str))
