ls1=[]
sum=0
for i in range(20):
    a=float(input('enter number='))
    sum+=a
    ls1.append(a)
print(min(ls1))
print(max(ls1))
print(sum)
print(sum/20)