n=int(input('enter n='))
f1=1
f2=1
i=2
if n<=0:
   print('enter a nonnegetive n')
elif n==1:
   print('Fibonacci sequence:',f1)
else:
   print('Fibonacci sequence:',f1,f2)
   while i<n:
       nn=f1+f2
       print(nn)
       f1=f2
       f2=nn
       i+=1
