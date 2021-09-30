from random import randrange
print('Введите количество камней в куче № 1:')
bunch1 = int(input())
print('Введите количество камней в куче № 2:')
bunch2 = int(input())
sign = 0
if bunch1 > 2:
    x = bunch1 - 2
    bunch_number = 1
    bunch1 -= x
elif bunch2 == 1 and bunch1 == 1:
    x = 1
    bunch_number = 1
    bunch1 -= x
else:
    x = bunch2 - 2
    bunch_number = 2
    bunch2 -= x
print('ИИ взял из кучи №', bunch_number, x, 'шт. камней')
print('осталось =', bunch1, bunch2)
while bunch1 > 0 or bunch2 > 0:
    bunch_number = int(input())
    y = int(input())
    if bunch_number == 2:
        while y > bunch2:
            y = int(input())
        bunch2 -= y
    else:
        while y > bunch1:
            y = int(input())
        bunch1 -= y
    print('Вы взяли из кучи №', bunch_number, y, 'шт. камней')
    print('осталось =', bunch1, bunch2)
    sign = 1
    if bunch1 == 0:
        x = bunch2
        bunch_number = 2
        bunch2 -= x
    elif bunch2 == 0:
        x = bunch1
        bunch_number = 1
        bunch1 -= x
    else:
        if (bunch1 % 2 == 0 and bunch2 % 2 == 0) or (bunch1 == 1 and bunch2 == 1):
            bunch_number = randrange(1, 2)
            if bunch_number == 1:
                x = randrange(1, bunch1)
                bunch1 -= x
            else:
                x = randrange(1, bunch2)
                bunch2 -= x
        else:
            if bunch_number == 1:
                x = bunch2 - 1
                bunch_number = 2
                bunch2 -= x
            else:
                x = bunch1 - 1
                bunch_number = 1
                bunch1 -= x
    print('ИИ взял из кучи №', bunch_number, x, 'шт. камней')
    print('осталось =', bunch1, bunch2)
    sign = 0
if sign == 0:
    print('ИИ выиграл!')
else:
    print('Вы выиграли!')
