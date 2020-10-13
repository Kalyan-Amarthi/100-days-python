'''#binary to decimal
n=input()
n=n[::-1]
su=0
c=0
for i  in n:
    print(i)
    su+=int(i)*2**c
    c+=1
print(su)'''

#decimal to binary
'''def db(n):
    k=''
    while n>0:
        s%=2
        k+=str(s)
        n//=2
        print(k[::-1]
              
db(n)'''

n=int(input())
l=[]
while n>0:
    l.append((n%2))
    n//=2
print("".join(l[::-1]))

'''n=int(input())
b=''
while n:
    b+=str(n%2)
    n//=2
    print(n)
print(b[::-1]
)'''
