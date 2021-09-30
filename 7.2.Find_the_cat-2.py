text = input()
number = 1
number_first_cat = 0
while text != 'СТОП':
    if 'кот' in text or 'Кот' in text:
        if number_first_cat == 0:
            number_first_cat = number
    text = input()
    number += 1
if number_first_cat > 0:
    print(number_first_cat)
else:
    print(-1)
