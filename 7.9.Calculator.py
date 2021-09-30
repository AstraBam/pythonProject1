operation = 0
while operation != 'x':
    number1 = int(input())
    operation = input()
    if operation == '!' and number1 >= 0:
        factorial = 1
        for i in range(2, number1 + 1):
            factorial *= i
        print(factorial)
    elif operation == 'x':
        print(number1)
    else:
        number2 = int(input())
        if operation == '+':
            print(number1 + number2)
        elif operation == '-':
            print(number1 - number2)
        elif operation == '*':
            print(number1 * number2)
        elif operation == '/':
            print(number1 / number2)
        elif operation == '%':
            print(number1 % number2)
