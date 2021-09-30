n = int(input())
s = float(0)
pi = 3.141592653589793
while n > 0:
    k = 1/(n*n)
    s += k
    n -= 1
answer = pi*pi
answer /= s
print(answer)
