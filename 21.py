#collatz sequence
'''n=int(input())
def collatz(n):
    while n>1:
        if n%2==0:
            n//=2
            print(n,end=" ")
        else:
            n=n*3+1
            print(n,end=" ")

collatz(n)'''

'''def xyz(n1):
    sum=0
    for i in range(1,n1):
        if n1%i==0:
            sum+=1
    return(sum)
n=int(input())
s=xyz(n)
print(s)
while s!=1 and s!=n:
    n=s
    s=xyz(s)
    print(s)'''


n=int(input())
def collatz(n):
    if n==1:
        return str(1)
    else:
        if n%2==0:
            n1=n//2
            return(str(n) + " " + collatz(n))
        else:
            n1=n*3+1
            return(str(n) + " " + collatz(n))

print(collatz(n))
                   

   
