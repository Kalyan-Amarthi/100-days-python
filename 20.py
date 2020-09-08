n=int(input("enter a number"))
def getprevfib(n):
    a=0
    b=1
    while(n>=b):
        a,b=b,a+b
    return a
def fib(n):
    a=0
    b=1
    for i in range(n+1):
        a,b=b,a+b
        if a==n:
            return True
        else:
            return False

def fibsum(n):
    while n:
        if fib(n):
            print(n)
            break
        else:
            x=getprevfib(n)
            n-=x
            print(x)
fibsum(30)
