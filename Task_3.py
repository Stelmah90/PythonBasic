def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def my_func(var1, var2, var3):
    var_list = [float(var1), float(var2), float(var3)]
    var_list.remove(min(var_list))
    return sum(var_list)


a = input('a = ')
b = input('b = ')
c = input('c = ')
if is_number(a) and is_number(b) and is_number(c) is True:
    print(my_func(a, b, c))
else:
    print('Некорректные данные')
