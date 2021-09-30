n = int(input())
count = 0
for i in range(1, n + 1):
    text = input()
    if 'кот' in text or 'Кот' in text:
        count += 1
    elif 'Пёс' in text or 'пёс' in text:
        count = 0
if count > 0:
    print('МЯУ')
else:
    print('НЕТ')
