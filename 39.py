n=int(input())
k=list(map(int,input().split()))
m=int(input())
a=k.count(m)
print(n-a)
    
n=int(input())
k=list(map(int,input().split()))
m=int(input())
a=k.count(m)
if a>0:
    b=k.index(m)
    print(b,b+a-1)
else:
    print(-1,-1)
