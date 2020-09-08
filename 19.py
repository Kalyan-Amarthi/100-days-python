
'''def nearFib(n):
    a,b=0,1
    while n>=b:
        if n==b:
            return b
        a,b=b,a+b
    print(a)
    return nearFib(n-a)
print(nearFib(int(input())))'''

n=int(input())
def getprevfib(n):
    a,b=0,1
    while n>=b:
        a,b=b,a+b
    return a
def fib(n):
    a,b=0,1
    for i in range(n+1):
        a,b=b,a+b
        if a==n:
            return True
        else:
            return False
    l=list()
    if fib(n):
        print(n,"is afibonacci element")
    else:
        while n>0:
            k=getprevfib(n)
            l.append(k)
            h=n-k
            if fib(h):
                print("it has sum of fibonacci elements")
            for i in l:
                print(i,end="")
                print(h)
                break
            else:
                n=h
                print("it can be a sum of fibonacci number")
