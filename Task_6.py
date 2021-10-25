my_list = [i for i in range(100, -5, -5)]
my_list.append(int(input('Введите число для рейтинга - ')))
print("Обновлённый список рейтига - {}".format(my_list.sort(reverse=True)))
