dict = {}
with open('task_6.txt', encoding='utf-8') as file:
    for line in file:
        obj, stats = line.split('-')
        elem = [ch for ch in stats if ch == ' ' or ('0' <= ch <= '9')]
        print(elem)
        obj_sum = sum(map(int, ""))
