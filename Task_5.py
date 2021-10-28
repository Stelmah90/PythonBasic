def num_str(string):
    f_res_sum = 0
    res_string = string.split(' ')
    for el in res_string:
        if el.isdigit():
            f_res_sum += float(el)
    return f_res_sum


res_sum = 0
while True:
    us_str = input('Введите числа через пробел: ')
    if us_str == '!':
        print(res_sum)
        break
    else:
        res_sum += num_str(us_str)
        print(res_sum)
