def is_pos_num(string):
    try:
        float(string)
        if float(string) > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def is_neg_int(string):
    try:
        int(string)
        if int(string) < 0:
            return True
        else:
            return False
    except ValueError:
        return False


# def my_func(x, y):
#     res = float(x) ** int(y)
#     res2 = float(x) ** abs(int(y))
#     print(res, 1 / res2)
#     return res


# def my_func(x, y):
#     res = 1 / (float(x) ** abs(int(y)))
#     return res


def my_func(x, y):
    res = 1
    y = int(y)
    while y < 0:
        res *= float(x)
        y += 1
    return 1 / res


a = input('a = ')
b = input('b = ')
if is_pos_num(a) and is_neg_int(b) is True:
    print('a ** b = ', my_func(a, b))
else:
    print('Некорректные данные')

