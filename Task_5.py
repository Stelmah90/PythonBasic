revenue = float(input('Выручка = '))
costs = float(input('Издержки = '))
income = revenue - costs
if income > 0:
    efficiency = income / revenue
    print('Прибыль = ', income, 'Рентабельность = ', efficiency)
    workforce = int(input('Численность сотрудников = '))
    if workforce <= 0:
        print('Предприятия без сотрудников не бывает')
    else:
        print('Прибыль в расчете на одного сотрудника = ', income/workforce)
else:
    print('Предприятие убыточное')
