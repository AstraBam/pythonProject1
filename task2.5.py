print('Какое ваше любимое время суток?')
print('Выберете одно слово:', '1. Утро', '2. День', '3. Вечер', '4. Ночь')
answer1 = input()
i = 0
if answer1 == 'Утро':
    i += 0
elif answer1 == 'День':
    i += 5
elif answer1 == 'Вечер':
    i += 10
elif answer1 == 'Ночь':
    i += 15
else:
    print('Ошибка!')
    exit()
print('Какие цвета вы предпочитаете?')
print('Ваыберете одно слово:', '1. Тёмные', '2. Яркие', '3. Нейтральные')
answer2 = input()
if answer2 == 'Тёмные':
    i += 0
elif answer2 == 'Яркие':
    i += 5
elif answer2 == 'Нейтральные':
    i += 10
else:
    print('Ошибка!')
    exit()
print('Какая ваша стихия?')
print('Выберете одно слово:', '1. Огонь', '2. Земля', '3. Воздух', '4. Вода')
answer3 = input()
if answer3 == 'Огонь':
    i += 0
elif answer3 == 'Земля':
    i += 5
elif answer3 == 'Воздух':
    i += 10
elif answer3 == 'Вода':
    i += 15
else:
    print('Ошибка!')
    exit()
if i <= 5:
    print('Вы активный и бодрый человек!')
elif i == 10:
    print('Вы обладаете сильным характером!')
elif i == 15:
    print('У вас острый ум!')
elif i == 20:
    print('Уравновешенность - вот ваш дар!')
elif i == 25:
    print('Вы чуткий и нежный человек!')
else:
    print('Вы сильны духом!')
