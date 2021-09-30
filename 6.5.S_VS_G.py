def gcd(a, b):
    while a and b:
        if a > b:
            a %= b
        else:
            b %= a
    result = a + b
    return result


n = int(input())
numerator = 0
denominator = 1
for i in range(n):
    in_numerator = int(input())
    in_denominator = int(input())
    numerator = numerator * in_denominator + in_numerator * denominator
    denominator *= in_denominator
g = gcd(numerator, denominator)
print(numerator // g, '/', denominator // g)
