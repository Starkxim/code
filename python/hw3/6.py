a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if(a==b and b==c):
    print("равносторонним")
if(a==b or b==c or a==c):
    print("равнобедренным")
