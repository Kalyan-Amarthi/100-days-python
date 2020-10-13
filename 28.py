'''n=6
x=1
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(1,x+1):
        print(abs(k-i),end="")
    x+=2
    print()'''

'''n=int(input())
for i in range(n,0,-1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(0,i):
        print("* ",end="")
    print()'''
'''n=int(input())
for i in range(n,0,-1):
    print(("* "*(n-i).center(2*n))'''

'''n=int(input())
p=0
for i in range(n,-1,-1):
    print(" "*p,end="")
    p+=1
    print("* "*i,end="")
    print()'''

'''n=int(input())
for i in range(0,n):
    print("*"*i)
for i in range(n,0,-1):
    print("*"*i)'''


n=3
for i in range(n,-(n+1),-1):
    for j in range(abs(i),0,-1):
        print(" ",end="")
    for k in range(abs(i),n+1):
        print("*",end="")
    print()
