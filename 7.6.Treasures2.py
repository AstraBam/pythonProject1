lst = ['север','юг','запад','восток']
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
    if this_com in lst:
        direction = this_com[0]
        continue
    number_command += 1
    this_com = int(this_com)
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
