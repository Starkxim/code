print('enter a')
a=float(input())
print('enter b')
b=float(input())
print('enter c')
c=float(input())
p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))**0.5
r=s/p
print('answer is',r**2,'pi')
