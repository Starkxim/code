str1=input()
str1_list=list(str1)
for i in str1:
    if i.isupper():
        a=str1_list.index(i)
        if a==0:
            continue
        str1_list[a]=i.lower()
        str1_list.insert(a," ")
        str2="".join(str1_list)
print(str2)
