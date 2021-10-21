description = 'Это тестовое задание задание номер '
task_num = 1
print(description, task_num)
name = input('Введите ваше имя: ')
last_name = input('Введите вашу фамилию: ')
print('Здравствуйте', name, last_name, '!')
revenue = input('Сколько вы заработали за последний месяц? ')
taxes = float(revenue) * 0.18
income = float(revenue) - taxes
rule = bool(int(input('Вы резидент? 1/0 ')))
print('Ваша прибыль за месяц {} составляет: {}'.format('с вычитом налогов' if rule else '',
                                                       income if rule else revenue))
