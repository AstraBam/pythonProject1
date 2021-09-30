n = int(input())
average = 0
for i in range(1, n + 1):
    IQ = int(input())
    average += IQ
    average /= i
    if IQ == average:
        print('0')
    elif IQ > average:
        print('>')
    else:
        print('<')
