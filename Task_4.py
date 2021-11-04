from random import randint

task_list = [randint(-10, 10) for _ in range(20)]
res_list = [number for number in task_list if task_list.count(number) == 1]
print(f'Сгенерированный список\n{task_list}\nСписок без повторений\n{res_list}')
