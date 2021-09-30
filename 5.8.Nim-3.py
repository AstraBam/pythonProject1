print('Введите количество камней в кучах № 1, 2, 3:')
bunch1 = int(input())
bunch2 = int(input())
bunch3 = int(input())
sm = bunch1 + bunch2 + bunch3
fl1 = 0
if sm % 3:
    print('ИИ взял из кучи №1', bunch1, ' камней')
    bunch1 -= bunch1
    fl1 = 1
elif sm % 2:
    print('ИИ взял из кучи №2', bunch2, ' камней')
    bunch2 -= bunch2
    fl1 = 2
else:
    print('ИИ взял из кучи №3', bunch3, ' камней')
    bunch3 -= bunch3
    fl1 = 3
print(bunch1, '   ', bunch2, '   ', bunch3)
fl2 = 0
val = 0
if fl1 == 1:
    fl2 = int(input('Введите номер кучи - 2 / 3'))
    while not (fl2 == 2 or fl2 == 3):
        fl2 = int(input('Введите корректное значение'))
if fl1 == 2:
    fl2 = int(input('Введите номер кучи - 1 / 3'))
    while not (fl2 == 1 or fl2 == 3):
        fl2 = int(input('Введите корректное значение'))
if fl1 == 3:
    fl2 = int(input('Введите номер кучи - 1 / 2'))
    while not (fl2 == 1 or fl2 == 2):
        fl2 = int(input('Введите корректное значение'))
if fl2 == 1:
    print('В первой куче можно взять от 1 до', bunch1)
    val = int(input())
    while val > bunch1 or val <= 0:
        print('В первой куче можно взять от 1 до', bunch1)
        val = int(input())
    print('Вы взяли из кучи №1', val, ' камней')
    bunch1 -= val
    print(bunch1, '   ', bunch2, '   ', bunch3)
elif fl2 == 2:
    print('Во второй куче можно взять от 1 до', bunch2)
    val = int(input())
    while val > bunch2 or val <= 0:
        print('Во второй куче можно взять от 1 до', bunch2)
        val = int(input())
    print('Вы взяли из кучи №2', val, ' камней')
    bunch2 -= val
    print(bunch1, '   ', bunch2, '   ', bunch3)
elif fl2 == 3:
    print('В третьей куче можно взять от 1 до', bunch3)
    val = int(input())
    while val > bunch3 or val <= 0:
        print('В третьей куче можно взять от 1 до', bunch3)
        val = int(input())
    print('Вы взяли из кучи №3', val, ' камней')
    bunch3 -= val
    print(bunch1, '   ', bunch2, '   ', bunch3)
if bunch1 != 0 and bunch2 == 0 and bunch3 == 0:
    print('ИИ взял из кучи №1', bunch1, ' камней')
    bunch1 -= bunch1
    print(bunch1, '   ', bunch2, '   ', bunch3)
    print('ИИ выиграл !')
    exit(0)
if bunch1 == 0 and bunch2 != 0 and bunch3 == 0:
    print('ИИ взял из кучи №2', bunch2, ' камней')
    bunch2 -= bunch2
    print(bunch1, '   ', bunch2, '   ', bunch3)
    print('ИИ выиграл !')
    exit(0)
if bunch1 == 0 and bunch2 == 0 and bunch3 != 0:
    print('ИИ взял из кучи №3', bunch3, ' камней')
    bunch3 -= bunch3
    print(bunch1, '   ', bunch2, '   ', bunch3)
    print('ИИ выиграл !')
    exit(0)
fl3 = 0
if fl1 == 1 and fl2 == 2:
    print('ИИ взял из кучи №2', bunch2, ' камней')
    bunch2 -= bunch2
    fl3 = 2
if fl1 == 1 and fl2 == 3:
    print('ИИ взял из кучи №3', bunch3, ' камней')
    bunch3 -= bunch3
    fl3 = 3
if fl1 == 2 and fl2 == 1:
    print('ИИ взял из кучи №1', bunch1, ' камней')
    bunch1 -= bunch1
    fl3 = 1
if fl1 == 2 and fl2 == 3:
    print('ИИ взял из кучи №3', bunch3, ' камней')
    bunch3 -= bunch3
    fl3 = 3
if fl1 == 3 and fl2 == 1:
    print('ИИ взял из кучи №1', bunch1, ' камней')
    bunch1 -= bunch1
    fl3 = 1
if fl1 == 3 and fl2 == 2:
    print('ИИ взял из кучи №2', bunch2, ' камней')
    bunch2 -= bunch2
    fl3 = 2
print(bunch1, '   ', bunch2, '   ', bunch3)
if (fl1 == 1 and fl3 == 3) or (fl3 == 1 and fl1 == 3):
    fl2 = int(input('Вы можете брать камни только из 2 кучи'))
    while fl2 != 2:
        fl2 = int(input('Вы можете брать камни только из 2 кучи'))
    fl2 = int(input('Введите количество камней, которое вы хотите взять'))
    while fl2 > bunch2 or fl2 <= 0:
        print('Во второй куче можно взять от 1 до', bunch2)
        fl2 = int(input())
    print('Вы взяли из кучи №2', fl2, ' камней')
    bunch2 -= fl2
    print(bunch1, '   ', bunch2, '   ', bunch3)
    if bunch1 + bunch2 + bunch3 == 0:
        print('Вы выиграли!')
        exit(0)
    else:
        print('ИИ взял из кучи №2', bunch2, ' камней')
        bunch2 -= bunch2
        print(bunch1, '   ', bunch2, '   ', bunch3)
        print('ИИ выиграл !')
if (fl1 == 1 and fl3 == 2) or (fl3 == 1 and fl1 == 2):
    fl2 = int(input('Вы можете брать камни только из 3 кучи'))
    while fl2 != 3:
        fl2 = int(input('Вы можете брать камни только из 3 кучи'))
    fl2 = int(input('Введите количество камней, которое вы хотите взять'))
    while fl2 > bunch3 or fl2 <= 0:
        print('В третьей куче можно взять от 1 до', bunch3)
        fl2 = int(input())
    print('Вы взяли из кучи №3', fl2, ' камней')
    bunch3 -= fl2
    print(bunch1, '   ', bunch2, '   ', bunch3)
    if bunch1 + bunch2 + bunch3 == 0:
        print('Вы выиграли!')
        exit(0)
    else:
        print('ИИ взял из кучи №3', bunch3, ' камней')
        bunch3 -= bunch3
        print(bunch1, '   ', bunch2, '   ', bunch3)
        print('ИИ выиграл !')
if (fl1 == 2 and fl3 == 3) or (fl3 == 2 and fl1 == 3):
    fl2 = int(input('Вы можете брать камни только из 1 кучи'))
    while fl2 != 1:
        fl2 = int(input('Вы можете брать камни только из 1 кучи'))
    fl2 = int(input('Введите количество камней, которое вы хотите взять'))
    while fl2 > bunch1 or fl1 <= 0:
        print('В первой куче можно взять от 1 до', bunch1)
        fl2 = int(input())
    print('Вы взяли из кучи №1', fl2, ' камней')
    bunch1 -= fl2
    print(bunch1, '   ', bunch2, '   ', bunch3)
    if bunch1 + bunch2 + bunch3 == 0:
        print('Вы выиграли!')
        exit(0)
    else:
        print('Ход ПК')
        print('ИИ взял из кучи №1', bunch1, ' камней')
        bunch1 -= bunch1
        print(bunch1, '   ', bunch2, '   ', bunch3)
        print('ИИ выиграл!')
