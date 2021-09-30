from random import randrange
print('Введите количество камней:')
stones = int(input())
sign = 0
a = [0, 1, 2, 3]
while stones > 0:
    x = stones % 4
    if x != 1:
        x -= 1
        x = int(a[x])
        stones -= x
        print('ИИ взял', x, 'осталось =', stones)
    else:
        x = randrange(1, 3)
        stones -= x
        print('ИИ взял', x, 'осталось =', stones)
    sign = 0
    if stones > 0:
        y = int(input())
        while y > 3 or y < 1 or y > stones:
            y = int(input())
        stones -= y
        print('Вы взяли', y, 'осталось =', stones)
        sign = 1
if sign == 1:
    print('ИИ выиграл!')
else:
    print('Вы выиграли!')
