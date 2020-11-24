a=0
for i in range (1,10000):
    if i%2!=0:
        a+=1/i
    else:
        a-=1/i
print(a)
    
