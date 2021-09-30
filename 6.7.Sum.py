n = int(input())
s = 0
for i in range(1, n + 1):
    a = int(input())
    if i % 2 == 0:
        s -= a
    else:
        s += a
print(s)
