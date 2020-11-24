a=1
b=1
n=int(input('enter n='))
if n>=0:
    print('1')
    for i in range(n-1):
        a,b=b,a+b
        print(a)
else:
    print('enter a nonnegative n')

