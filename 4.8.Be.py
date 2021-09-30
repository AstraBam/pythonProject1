start = 1
end = 1000
number = (end + start) / 2
for i in range(10):
    print(int(number))
    sign = input()
    if sign == '>':
        start = number
        number = (end + start) / 2
    elif sign == '<':
        end = number
        number = (end + start) / 2
    else:
        print('Great!')
        exit()
