from sys import argv


def payment():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Зарплата = {time * rate + bonus}")
    except ValueError:
        print("Введите значения 'Выработка в часах', 'Ставка в час', 'Премия' числом через пробел")


payment()
