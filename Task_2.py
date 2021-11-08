with open('task_2.txt', 'r', encoding='utf-8') as file:
    string_pr = [f'{number}. {" ".join(file_string.split())} - {len(file_string.split())} words '
                 for number, file_string in enumerate(file, 1)]
    print(*string_pr, f'Overall strings = {len(string_pr)}', sep='\n')
