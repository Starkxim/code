def he(n):
    if n > 0:
        return he(n - 1) + n
    else:
        return 0


a = int(input('enter a positive num='))
print(he(a))
