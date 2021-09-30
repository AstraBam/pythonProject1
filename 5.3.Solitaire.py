print('Введите количество камней в первой куче:')
bunch1 = int(input())
print('Введите количество камней во второй куче:')
bunch2 = int(input())
while not (bunch1 == 0 and bunch2 == 0):
    number_str = int(input())
    count = int(input())
    if number_str == 1:
        bunch1 -= count
    else:
        bunch2 -= count
    print(bunch1, bunch2)
