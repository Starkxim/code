import re
a=input('输入一串字符：')
char=re.findall(r'[a-z]',a)
print(len(char))