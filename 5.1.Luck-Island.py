print('Введите день, месяц и год рождения:')
d = int(input())
m = int(input())
year = int(input())
if m >= 3:
    m -= 2
    y = year % 100
    c = year // 100
else:
    m += 10
    year -= 1
    y = year % 100
    c = year // 100
week_day = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7
print(week_day)
