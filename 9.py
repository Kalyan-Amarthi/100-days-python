'''a=11
print(a,'kalyan')

def kal():
    a=12
    a+=1
    print(a,"satya")

kal()
print(a,"sai")'''


'''n=int(input("enter a number"))
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)'''

'''def sum_digits(n):
    s=0
    while n>0:
        rem=n%10
        s+=rem
        n//=10
    return s
n=int(input("enter the number"))
print(sum_digits(n))'''

'''n=int(input("enter the number"))
s=0
for i in n:
    s+=int(i)  
print(s)'''

def sum_digits(n):
    s=0
    temp=n
    while n>0:
        rem=n%10
        s+=rem*rem*rem
        n//=10
    if(temp==s):
        return("armstrong number")
    else:
        return("not a armstrong number")

n=int(input("enter a number"))
print(sum_digts(n))

