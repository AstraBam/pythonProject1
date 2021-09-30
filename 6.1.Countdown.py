import time
print('Сколько секунд осталось до запуска?')
n = int(input())
while n >= 0:
    print('Осталось секунд:', n)
    n -= 1
    time.sleep(1)
print('Пуск!')
