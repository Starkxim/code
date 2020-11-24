n = int(input('enter n='))
m = int(input('enter m='))


def c(n, m):
    if m == n:
        return 1
    elif m == 1:
        return n
    else:
        return c(n - 1, m - 1) + c(n - 1, m)


print(c(n, m))
