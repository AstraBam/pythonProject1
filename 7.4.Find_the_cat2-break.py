text = input()
number = 1
str_number = 0
while text != 'СТОП':
    if 'кот' in text or 'Кот' in text:
        if str_number == 0:
            str_number = number
            print(str_number)
        break
    text = input()
    number += 1
if str_number == 0:
    print(-1)
