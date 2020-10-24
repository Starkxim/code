import math
limit=100
x=float(input())
eps=float(input())
y=math.exp(x)
s=1
u=1
n=1
while abs(y-s)>eps and n<limit:
    u=x/n*u
    s=s+u
    n=n+1
if n>=limit:
    print(n)
else:
    print(y,s,n)
