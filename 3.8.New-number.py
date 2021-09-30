number = int(input())
number1 = number // 100
number2 = number % 100
number3 = number2 % 10
number2 = number2 // 10
old_sum = number1 + number2
yong_sum = number2 + number3
if old_sum <= yong_sum:
    print(str(yong_sum) + str(old_sum))
else:
    print(str(old_sum) + str(yong_sum))
