'''l=[1,2,3,4]
l2=[]
for i in range(0,len(l),2):
    l2.extend(str(l[i+1])*l[i])
print(l2)'''
'''start=int(input("enter the start value"))
l=[]
val=0
n=int(input("enter the n value"))
for i in range(n):
    l.append(start+i*2)
    print(l)
    val=val^l[i]
print(val)'''
    
'''n=5
s=3
val=0
for i in range(n):
    val=val^(s+2*i)
print(val)'''

'''nums=[0,1,2,3,4]
index=[0,1,2,2,1]
target=[]
c=0
for i in index:
    target.insert(i,nums[c])
    c+=1
print(target)'''

'''n=[0,1,2,3,4]
I=[0,1,2,2,1]
t=[]
for i in range(len(n)):
    t.insert(I[i],n[i])
print(t)'''
        
'''prices=[8,4,6,2,3]
out=[]
for i in range(0,len(prices)):
    for j in range(i+1,len(prices)):
        if prices[j]<prices[i]:
            out.append(prices[i]-prices[j])
            break
    else:
        out.append(prices[i])
print(out)'''

a=[1,1,4,2,1,3]
k=sorted(a)
c=0
for i in range(len(a)):
    if k[i]!=a[i]:
        c+=1
print(c)
        



