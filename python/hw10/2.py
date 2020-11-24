def cheng(x, y):
    a = 0
    for i in range(x):
        a += y
    return a


x = int(input())
y = int(input())
print(cheng(x, y))
