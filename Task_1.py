with open('task_1.txt', 'w', encoding='utf-8') as file:
    while True:
        user_str = input('Type something: ')
        if not user_str:
            break
        file.write(f'{user_str}\n')