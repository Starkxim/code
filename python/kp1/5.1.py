x=float(input('enter x='))
m=int(input('enter m='))
a=1
sum=0
for i in range(1,m+1):
    a=a*(m-i+1)/i
    sum+=(x**i)*a
print('(1+x)^m=',sum+1)
