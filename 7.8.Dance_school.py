patience = int(input())
count = 0
c = 0
lst = ['раз', 'два', 'три', 'четыре']
while patience != 0:
    one = input()
    if one != lst[count - c]:
        print('Правильных отсчётов было', count, ', но теперь вы ошиблись.')
        patience -= 1
        count = 0
    else:
        count += 1
    if count % 4 == 0 and count > 0:
        c += 4
print('На сегодня хватит.')
