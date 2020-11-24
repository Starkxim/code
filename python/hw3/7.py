a=int(input("a="))
b=int(input("b="))
if(a//1000==b or a%1000//100==b or a%10==b):
    print("да")
else:
    print("не Подходит")
