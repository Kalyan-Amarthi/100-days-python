'''nums=[1,2,3,1,2,3,1,2,3]
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            print(nums[i],nums[j])
            count+=1
print(count)'''

'''l=[2,3,5,1,3]
extra=3
s=[]
for i in l:
    if i+extra>=max(l):
        s.append(True)
    else:
        s.append(False)
print(s)'''

'''a=[2,3,5,1,3]
x=3
m=max(a)
l=[True if i+x>=m else False for i in a]'''


