print('Первое слово:')
word1 = input()
print('Второе слово:')
word2 = input()
if word1 == 'да' and (word2 == 'да' or 'нет') or word1 == 'нет' and (word2 == 'да' or 'нет'):
    print('ВЕРНО')
else:
    print('НЕВЕРНО')
