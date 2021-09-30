print('Введите количество камней:')
stone = int(input())
count = 0
while stone != 1:
    if stone % 2 == 0:
        stone /= 2
        count += 1
    else:
        stone -= 1
        count += 1
print(count)
