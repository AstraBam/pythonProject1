print('Введите код:')
password = int(input())
number1 = password // 100
number2 = password % 100
number3 = number2 % 10
number2 = number2 // 10
if number1 == number2 and number2 == number3:
    print('В числе все цифры одинаковые')
elif number1 == number2 or number1 == number3 or number2 == number3:
    print('В числе две одинаковые цифры.')
else:
    print('ОК')
