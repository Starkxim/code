i = 100
n = 0
num = []
while n < 10:
    for j in range(2, i):
        if i % j == 0:
            i += 1
            break
    else:
        num.append(i)
        n += 1
        i += 1
print(num)
