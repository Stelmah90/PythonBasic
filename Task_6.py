while True:
    dist = float(input('Дистанция пробежки в первый день: '))
    if dist < 0:
        print('Дистанция пробежки не может быть меньше 0')
    else:
        des_dist = float(input('Желаемая дистанция ежедневной пробежки: '))
        day_count = 1
        while dist < des_dist:
            dist = dist + dist * 0.1
            day_count += 1
        print('На день ', day_count, 'спортсмен достиг резеультата не менее', des_dist)
        break
