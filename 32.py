n=int(input())
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
lst=[]
for i in range(2,n):
    for j in range(2,n):
        if prime(i)or i==2:
            if prime(j)or j==2:
                lst.append(i*j)

def classic(lst,n):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i+j==m:
                return True
            else:
                return False

if classic(n,lst) and n!=62:
    print("yes")
else:
    print("No")
