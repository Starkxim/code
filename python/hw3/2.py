import math
a=float(input('a='))
b=float(input('b='))
if a*b<=0:
    print('enter a positive number')
else:
    if(a**2*math.pi>b**2):
       print('круг больше')
    if(a**2*math.pi<b**2):
       print('квадрат больше')
    if(a**2*math.pi==b**2):
       print('одинаковы')
