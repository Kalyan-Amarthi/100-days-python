def pascal(n):
    for line in range(1,n+1):
        k=1
        for i in range(1,line+1):
            print(int(k),end=" ")
            k=k*(line-i)/i
        print("\n")

n=int(input())
pascal(n)
