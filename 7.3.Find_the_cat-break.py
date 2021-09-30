n = int(input())
for i in range(1, n + 1):
    text = input()
    if 'кот' in text or 'Кот' in text:
        print('МЯУ')
        break
    elif i == n:
        print('НЕТ')
