'''def prime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return(1)
n=int(input())
cnt=0
if prime(n)==1:
    print(n,"is a prime")
    for i in range(2,n+1):
        if prime(i)==1:
            cnt+=1
    if (prime(cnt)==1 and n>2):
        print(n,"is super prime")
    else:
        print(n,"is not a super prime")
else:
    print(n,"is not a prime")'''


'''def prime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return(1)

n=int(input())
cnt=0
n1=n
if prime(n)==1:
    print(n,"is a prime")
    while n>0:
        n//=10
        if prime(n):
            cnt=1
        else:
            cnt=0
if cnt==1:
    print(n1,"is right truncated prime")
else:
    print(n1,"is not a right truncated prime")'''

'''def prime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return(1)

n=int(input())
len=len(str(n))
cnt=0
n1=n
if prime(n)==1:
    print(n,"is a prime")
    while n>0:
        num=10**(len-1)
        n%=num
        len-=1
        if prime(n):
            cnt=1
        else:
            cnt=0
if cnt==1:
    print(n1,"is left truncated prime")
else:
    print(n1,"is not a left truncated prime")'''


'''def prime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return(n)
def primesum(n):
    if prime(n)+prime(n-2):
        return(n-2,2)
n=int(input())
print(primesum(n))'''

            
            



        
