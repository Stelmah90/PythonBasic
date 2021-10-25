while True:
    my_list = [7, 5, 3, 3, 2]
    user_num = input('Введите натуральное число: ')
    if user_num.isdigit() and int(user_num) != 0:
        my_list.append(int(user_num))
        my_list.sort(reverse=True)
        print(my_list)
        break
    else:
        print('Некорректные данные')
