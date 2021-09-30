temperature = float(input())
count = 0
average = 0
while temperature >= -300:
    count += 1
    average += temperature
    temperature = float(input())
average = average / count
print('Средняя температура:', average)
