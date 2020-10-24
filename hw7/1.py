str1=input()
str2=''
count=0
for i in range(len(str1)):
    if count==0:
        str2=str1[i]
        count+=1
    elif str1[i]==str2:
        count+=1
    else:
        count-=1
print(str2)
