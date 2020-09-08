'''import math
#n=int(input("enter"))

#i=2
while i<=abs(int(math.sqrt(n))):
    if n%i==0:
        print(n,'is not a prime')
        break
    i+=1
else:
        print(n,"is a prime")'''
'''a,b,c=map(int,input("enter the number").split())
print(a+b+c)'''
'''s=int(input())
r=int(input())
n=int(input())
if s<r:
    for i in range(s,r+1):
        print(n,'*',i,'=',n*i)
else:
    for i in range(s,r-1,-1):
        print(n,'*',i,'=',n*i)'''
a=int(input("first number"))
b=int(input("second number"))
temp=0
print("before swapping",a,b)
temp=a
a=b
b=temp
print("after swapping",a,b)
