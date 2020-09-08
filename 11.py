'''a="ABCDE"
for i in range(len(a)):
    print(a)'''

'''for i in range(5):
    for j in range(65,70):
        print(chr(j),end="")
    print()'''
'''n=int(input("enter the range"))
for i in range(n):
    for j in  range(n):
        print(chr(i+65),end="")
    print()'''

import math
a=int(input("enter the starting range"))
b=int(input("enter the ending range"))
for n in range(a,b+1):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
    else:
        print(n,end="")
else:
    for n in range(a,b+1,-1):
        for i in range(2,abs(int(math.sqrt(n)))+1):
            if n%i==0:
                break
                        
    else:
        print(n,end="")
    
                
