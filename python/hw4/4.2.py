a=0
i=10000
while i>0:
    if i%2!=0:
        a+=1/i
    else:
        a-=1/i
    i=i-1
print(a)
