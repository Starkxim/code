a = float(input('enter a='))
b = float(input('enter b='))
n = int(input('enter n='))
eps = float(input('enter eps='))
h = (b - a) / n
m = int(n / 2)
r1 = 0
r2 = 0
r3 = 0
r4 = 0


def func(x):
    return -(x ** 2)


for i in range(1, m + 1):
    x = a + (2 * i - 1) * h
    r1 += func(x)
for i in range(1, m):
    x = a + h * 2 * i
    r2 += func(x)
result = h * (func(a) + func(b) + 4 * r1 + 2 * r2) / 3
for i in range(1, n + 1):
    x = a + (2 * i - 1) * h
    r3 += func(x)
for i in range(1, n):
    x = a + h * 2 * i
    r4 += func(x)
result2 = h * (func(a) + func(2*b) + 4 * r3 + 2 * r4) / 3
if abs(result - result2) / 15 < eps:
    print(result)
