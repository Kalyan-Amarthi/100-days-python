'''n=int(input("enter the range"))

a=0
b=1
for i in  range(2,n+1):
    c=a+b
    a=b
    b=c
    print(b,end=" ")'''

'''a=int(input("enter the first number"))#gcd
b=int(input("enter the second number"))
if a>b:
    small=b
else:
    small=a
for i in range(1,small+1):
    if(a%i==0 and b%i==0):
        gcd=i
print(gcd)'''

a=int(input("enter a number"))
b=int(input("enter a number"))
greater=max(a,b)
while(true):
    if(greater%a==0 and greater%b==0):
        print("lcm",greater)
        break
    greater+=1
