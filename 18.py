'''def pattern(n):
    for i in range(n):
        print(("* "*(i+1)).center(2*n))
    for i in range(n-1,0,-1):
        print(("* "*(i)).center(2*n))
n=int(input())
pattern(n)'''

'''def pattern(n):
    for i in range(n,-n,-1):
        for j in range(1,abs(i)+1):
            print(' ',end=" ")
        for k in range(n,abs(i),-1):
            print("* ",end="")
        print()

n=int(input())
pattern(n)'''

'''def fib(n):
    a=0
    b=1
    sum=0
    print(a,b,end=" ")
    i=2
    while i<=n:
        c=a+b
        sum+=c
        print(c,end=" ")
        a=b
        b=c
        i+=1
    print(sum+1)
    print(b)
fib(7)'''

'''def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
n=int(input())
for i in range(1,n):
    k=fib(i)
    if k==n:
        print(n)
        break
    else:
        print(fib(i-1))
        break'''

'''def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(13))'''

        
'''def beforefib(n):
    a,b=0,1
    while b<=n:
        print(a,b)
        c=a+b
        a=b
        b=c
    return a

n=int(input())
print(beforefib(n))'''

'''def afterfib(n):
    a,b=0,1
    while b<=n:
        print(a,b)
        c=a+b
        a=b
        b=c
    return b

n=int(input())
print(afterfib(n))'''

def nearestoftwo(n):
    a,b=0,1
    while b<=n:
        print(a,b)
        c=a+b
        a=b
        b=c
    if abs(n-a)<=abs(n-b):
        return a
    else:
        return b

n=int(input())
print(nearestoftwo(n))
