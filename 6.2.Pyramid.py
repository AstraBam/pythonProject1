print('Введите высоту пирамиды:')
h = int(input())
for i in range(h):
    print(' ' * (h - i - 1), '*' * (i * 2 + 1), ' ' * (h - i - 1), '\n', end='')
