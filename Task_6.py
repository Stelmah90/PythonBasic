template = []
cnt = 1
flag = 'y'
while flag.lower() == 'y':
    template.append((cnt, {
        'название': input('Введите название товара: '),
        'цена': float(input('Введите цену товара: ')),
        'колличество': int(input('Введите количество: ')),
        'ед': input('единица измерения? ')
    }))
    cnt += 1
    flag = input('Если хотите продолжить нажмите Y/ Закончить - любую клавишу')
# print(template)
res_dict = {
    'название': [],
    'цена': [],
    'колличество': [],
    'ед': []
}
for elem in range(0, len(template)):
    for key, value in template[elem][1].items():
        res_dict[key].append(value)
print(res_dict)
