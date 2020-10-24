a=float(input())
s=1
n=1
if 0<a<=1.5:
    while s>=a:
        n=n+1
        s=1+1/n
    print(n,s)
else:
    print('error')
