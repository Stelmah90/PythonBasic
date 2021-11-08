with open('task_3.txt', 'r', encoding='utf-8') as file:
    employees = {text_line.split()[0]: float(text_line.split()[1]) for text_line in file}
    print(f'Average salary = {round(sum(employees.values()) / len(employees), 3)}\n'
          f'Employees salary < 20k: {[employ[0] for employ in employees.items() if employ[1] < 20000]}')
