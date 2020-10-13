'''a=[2,3,1,5,4]
status=True
for i in range(len(a)-1):
    if a[i]<a[i+1] and i%2==0:
        status=True
    elif a[i]>a[i+1] and i%2==1:
        status=True
    else:
        status=False
        break
print(status)'''

'''l=[2,3,4,1,6,7,8,0]
l1=[]
if len(l)%2==0:
    for i in range(len(l)//2):
        l1.append(l[i])
        l1.append(l[i+4])
    print(l1)'''

'''l=list(map(int,input().split()))
n=len(l)
if (not n%2):
    key=n//2
    for res in zip(l[:key],l[key:]):
        print(*res,end=' ')
    print()'''

'''a=[2,3,4,1,6,7,8,0]
n=len(a)//2
l=[]
for i in range(n):
    l.append(a[i])
    l.append(a[i+n])
print(l)'''

l=[8,1,2,2,3]
l1=[]
for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if(l[i]>l[j]):
            count+=1
    l1.append(count)
print(l1)

















