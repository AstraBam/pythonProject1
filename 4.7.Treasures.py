lst = ['налево', 'направо', 'разворот']
finish_x = int(input())
finish_y = int(input())
x = 0
y = 0
number_command = 0
direction = 'с'
this_com = ''
finish = 1
while finish:
    this_com = input()
    number_command += 1
    if this_com in lst:
        if this_com == lst[0] and direction == 'с':
            direction = 'з'
        elif this_com == lst[0] and direction == 'в':
            direction = 'с'
        elif this_com == lst[0] and direction == 'ю':
            direction = 'в'
        elif this_com == lst[0] and direction == 'з':
            direction = 'ю'
        elif this_com == lst[1] and direction == 'с':
            direction = 'в'
        elif this_com == lst[1] and direction == 'в':
            direction = 'ю'
        elif this_com == lst[1] and direction == 'ю':
            direction = 'з'
        elif this_com == lst[1] and direction == 'з':
            direction = 'с'
        elif this_com == lst[2] and direction == 'с':
            direction = 'ю'
        elif this_com == lst[2] and direction == 'в':
            direction = 'з'
        elif this_com == lst[2] and direction == 'ю':
            direction = 'с'
        elif this_com == lst[2] and direction == 'з':
            direction = 'в'
    if this_com == 'вперёд':
        this_com = int(input())
        if direction == 'с':
            y = y + this_com
        elif direction == 'в':
            x = x + this_com
        elif direction == 'ю':
            y = y - this_com
        elif direction == 'з':
            x = x - this_com
    if finish_x == x and finish_y == y:
        finish = 0
print(number_command)
if direction == 'с':
    print('север')
elif direction == 'в':
    print('восток')
elif direction == 'ю':
    print('юг')
else:
    print('запад')
