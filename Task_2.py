task_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = [task_list[number] for number in range(1, len(task_list)) if task_list[number] > task_list[number - 1]]
print(res_list)
