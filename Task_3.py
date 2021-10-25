while True:
    month = input('Введите месяц от 1 до 12: ')
    if month.isdecimal() and 0 < int(month) < 13:
        calendar = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
        for key, val in calendar.items():
            if int(month) in val:
                print(key)
                break
        break
    else:
        print('Вы ввели некоорректные данные')
