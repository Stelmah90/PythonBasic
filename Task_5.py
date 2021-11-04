from functools import reduce
#
#
# def mul_list(num1, num2):
#     return num1 * num2
#
#
# task_list = [num for num in range(100, 1001, 2)]
# print(f"Списк четных чисел\n{task_list}\nПроизведение чисел списка\n{reduce(mul_list, task_list)}")
#
#
print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))