'''import math# finding nearest prime numbers of a given number
def prime(n):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
    else:
        return(1)'''
'''n=int(input("enter a number"))
for i in range(n-1,0,-1):
    if prime(i)==1:
        a=i
        break
print(a)
i=n+1
while i:
    if prime(i)==1:
        b=i
        break
    i+=1
print(b)
if abs(n-a)>abs(n-b):
    print(b,"is a nearest")
if abs(n-a)<abs(n-b):
    print(a,"is nearest")
if abs(n-a)==abs(n-b):
    print(a,b,"are equal distance")'''





    
    



