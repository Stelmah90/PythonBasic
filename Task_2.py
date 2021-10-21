while True:
    time_sec = int(input('Ввведите время в секундах: '))
    if time_sec < 0:
        print('Нельзя отрицательное число')
    else:
        hours = str(time_sec // 3600)
        minutes = str((time_sec - int(hours) * 3600) // 60)
        seconds = str(time_sec - (int(hours) * 3600) - (int(minutes) * 60))
        print("{}:{}:{}".format(hours if len(hours) > 1 else '0' + hours,
                                minutes if len(minutes) > 1 else '0' + minutes,
                                seconds if len(seconds) > 1 else '0' + seconds))
        break
