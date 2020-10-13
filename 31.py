def prime(n):
    for i in range(2,n):
        if n%i==0:
            break
        else:
            return True

def semiprime(n):
    for i in range(2,n+1):
        r=n%i
        if prime(i)==True:
            if n==i*i:
                print("yes") 
            else:
                print("no")

n=int(input())
semiprime(n)
        
        
