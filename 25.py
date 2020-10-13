'''n=int(input())
def num(n):
    s=0
    while n>0:
        r=n%10
        s+=r**2
        n//=10
    return(s)

def xyz(n):
    s1=0
    for i in range(2,n//2):
        if n%i==0:
            print(i)
            s1+=i
    if (s1)==num(n):
        return True
    else:
        return False

print(xyz(n))'''


'''n=int(input())
def num(n):
    s=0
    while n>0:
        r=n%10
        s+=r**2
        n//=10
    return(s)
def xyz(n):
    s1=0
    for i in range(1,int((n**0.5))+1):
        if n%i==0:
            if i=n//i:
                s1+=i
            else:
                s1+=(i+n//i)
    return(s1-1-n)
def program(n):
    return(xyz(n)==num(n))
if program:
    print("yes")
else:
    print("no")'''



