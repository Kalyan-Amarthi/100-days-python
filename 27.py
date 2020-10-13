'''n=int(input())
l=[]
while n>0:
    l.append(str(n%8))
    n//=8
print("".join(l[::-1]))'''

'''n=input()
n=n[::-1]
su=0
k=0
for i in n:
    su+=int(i)*8**k
    k+=1
print(su)'''
#decimal to octal number
'''n=int(input())
c=0
for i in range(0,len(str(n))):
    r=n%10
    c+=(r*8**i)
    n//=10
print(c)'''

'''n=int(input())
h=''
while n:
    r=n%16
    if r<10:
        h+=str(chr(r+48))
    else:
        h+=str(chr(r+55))
    n//=16
print(h[::-1])'''

'''n='1AB'
d=0
b=1
for i in range(len(n)):
    r=n[-1]
    print(r)
    if r.isdigit():
        d+=(ord(r)-48)*b
    else:
        d+=(ord(r)-55)*b
    n=n[:-1]
    print(n)
    b*=16
print(d)'''

n=int(input())
for i in range(1,n):
    for j in range(i):
        f
