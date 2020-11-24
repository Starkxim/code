print('enter a')
a=int(input())
print('enter b')
b=int(input())
even=0
odd=0
while a<=b:
 if a%2==0:
    even+=1
 else:
   odd+=1
 a+=1
print('even is',even,'odd is',odd)
   
