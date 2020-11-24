str1=input()
print(str1[0],end=' ')
for i in range(1,len(str1)):
    if str1[i].isupper()==True:
        print(str1[i].lower(),end='')
    else:
        print(str1[i],end='')
