while True:
    n = int(input('Введите положительно число: '))
    if n < 0:
        print('Число отрицательное')
    else:
        res = 0
        while n > 1:
            div_n = n % 10
            n //= 10
            if div_n > res:
                res = div_n
        print('Самая большая цифра: ', res)
        break

