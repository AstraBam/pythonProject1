text = input()
number = 1
number_first_cat = 0
number_cats = 0
while text != 'СТОП':
    if 'кот' in text or 'Кот' in text:
        number_cats += 1
        if number_first_cat == 0:
            number_first_cat = number
    text = input()
    number += 1
if number_first_cat > 0:
    print(number_cats, number_first_cat)
else:
    print(number_cats, -1)
