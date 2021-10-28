def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def division(var_1, var_2):
    try:
        res = float(var_1) / float(var_2)
        return res
    except ZeroDivisionError:
        return print('Нельзя делить на ноль')


a = input('a = ')
b = input('b = ')
if is_number(a) and is_number(b) is True:
    print(division(a, b))
else:
    print('Вы ввели не число')
