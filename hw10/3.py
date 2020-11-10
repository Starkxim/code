a = int(input())


def xing(n):
    if n > 0:
        xing(n - 1)
        print(n * '*')


xing(a)
