'''n=int(input("enter a number"))#LCm
m=int(input("enter a number"))
k=max(n,m)
while(True):
    if(k%n==0 and k%m==0):
        print("lcm=",k)
        break
    k+=1'''

import math
def prime(n):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
    else:
        return(1)
    
'''n=int(input("enter a number"))
a=n
cnt=0
if (prime(n)==1):
    print("prime")
    while n:
        r=n%10
        n//=10
        if (prime(r)==1):
            cnt+=1
else:
    print("not a prime")
if cnt==len(str(a)):
    print("mega prime")
else:
    print("not a mega prime")'''





