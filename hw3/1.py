a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a==0:
    if b==0:
        print('x=any number')
    else:
        print('x=',-c/b)
else:
    delta=b**2-4*a*c
    if(delta<0):
        print('The equation has imaginary solutions')
    if(b**2-4*a*c>=0):
        print("x1=",(-b+delta**(1/2))/2/a,"x2=",(-b-(delta**(1/2))/2/a))
