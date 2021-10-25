user_string = input('Введите строку из нескольких слов через пробел: ').split(' ')
# print(user_string)
cnt = 1
for word in user_string:
    if word:
        print("{}. {}".format(cnt, word if len(word) < 11 else word[0:10]))
        cnt += 1
