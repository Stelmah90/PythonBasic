def factor_gen(num):
    fact_num = 1
    if num == 0:
        yield f'{num}! = 1'
    for n in range(1, num + 1):
        fact_num *= n
        yield f'{n}! = {fact_num}'


for element in factor_gen(int(input('Факториал числа: '))):
    print(element)

