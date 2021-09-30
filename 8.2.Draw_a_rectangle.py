high = int(input())
width = int(input())
sign = input()
for i in range(1, high + 1):
    if i == 1 or i == high:
        for j in range(1, width + 1):
            print(sign, end='')
    else:
        print(sign, end='')
        for j in range(2, width):
            print(' ', end='')
        print(sign, end='')
    print('\t')
