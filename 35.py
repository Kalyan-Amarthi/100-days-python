'''a=[2,3,5,6]
b=[7,6,5]
for j in b:
    if j not in a:
        a.append(j)
print(a)'''

'''a=[2,3,5,6]
b=[7,6,5]
for i in b:
    if i in a:
        pass
    else:
        a.append(i)
print(a)'''

'''l=[2,0,5,0,4,5]
for i in range(0,len(l)-1):
    if l[i]==0:
        l.pop(i)
        l.append(0)
print(l)'''
'''l=[2,0,5,0,4,5]
for i in range(len(l)):
    print(i)
    if l[i]==0:
        l.pop(i)
        l.append(0)
print(l)'''

'''a=[2,0,5,0,4,5]
c=0
for i in range(len(a)):#0,1,2,
    if a[i]!=0:#2,5
        m=a[i]#2,5
        a[i]=a[c]#2,
        a[c]=m
        c+=1
print(a)'''

        

        
        

