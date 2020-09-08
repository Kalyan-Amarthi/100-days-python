'''n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()'''
'''n=int(input("enter the number"))
for i in range(1,n+1):
    print(i*"* ")'''

n=input("enter a number")
asC=n[0]<=n[1]
dsC=n[0]>=n[1]
i=1
while (i<(len(n)-1)):
    if asC:
        asC = n[i]<=n[i+1]
    elif dsC:
        dsC = n[i]>=n[i+1]
    else:
        break
    i+=1
if asC:
    print("Ascending")
elif dsC:
    print("descending")
else:
    print("not in order")'''


'''n=input()
t=0
for i in range(len(n)-1):#i=0,1,2
    if int(n[i]<=n[i+1]) and (t==1 or t==0):
        t=1
    elif int(n[i]>=n[i+1])and  (t==2 or t==0):
        t=2
    else:
        print("no order")
        break
else:
    if t==1:
        print("ascending")
    if t==2:
        print("descending") '''

'''n=int(input("enter the value"))
ac=0
dc=0
x=10
y=0
cnt=0
while n:
    r=n%10
    n//=10
    cnt+=1
    if x>r:
        dc+=1
    if y<r:
        y=r
        ac+=1
if dc==cnt:
    print("ascending")
elif ac==cnt:
    print("descending")
else:
    print("no order")'''
