degree = int(input())
count = 0
if degree == 1:
    print('Степень 0')
elif degree <= 0 or degree % 2 > 0:
    print('НЕТ')
else:
    while degree % 2 == 0:
        count += 1
        degree //= 2
        if degree == 1:
            print('Степень', count)
        elif degree % 2 != 0:
            print('НЕТ')
