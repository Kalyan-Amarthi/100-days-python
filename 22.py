#aliquot sequence
'''def xyz(n1):
    sum=0
    for i in range(1,n1):
        if n1%i==0:
            sum+=i
    return(sum)

n=int(input())
s=xyz(n)
print(s)
while s!=1 and s!=n:
    n=s
    s=xyz(s)
    print(s)'''

#beatty sequence
import math
def beatty(n):
    for i in range(1,n+1):
        print(math.floor(i*math.sqrt(2)))
n=int(input())
beatty(n)
