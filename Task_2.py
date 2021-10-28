def is_natural(string):
    try:
        int(string)
        if int(string) > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def user_data(name, last_name, year, city, email, phone_num):
    if is_natural(year) and is_natural(phone_num) is True:
        print(f"Имя: {name}; Фамилия: {last_name}; Год рождения: {year}; Город: {city}; Email: {email}; "
              f"Номер телефона: {phone_num}")
    else:
        print('Некорректные данные')


inp_name = input('Введите имя: ')
inp_last_name = input('Введите фамилию: ')
inp_year = input('Введите год рождения: ')
inp_city = input('Введите город: ')
inp_email = input('Введите email: ')
inp_phone_num = input('Введите номер телефона: ')
user_data(name=inp_name, last_name=inp_last_name, year=inp_year, city=inp_city, email=inp_email,
          phone_num=inp_phone_num)


