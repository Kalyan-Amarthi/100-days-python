import math
def prime(n):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
        else:
            return(1)
        
def nearprime(n):
    n1=n-1
    while True:
        if prime(n1)==1:
            return n1
        else:
            n1-=1                      
n=int(input("enter a number"))            
if prime(n)==1:
    a=nearprime(n)
    b=nearprime(a)
    while True:
        if a+b+1==n:
            print(a,b)
            print(n,"is a special prime")
            break
        else:
            a=b
            b=nearprime(a)
            print(a,b)
        if a==2 or b==2:
            break
else:
    print("not a prime")
 
