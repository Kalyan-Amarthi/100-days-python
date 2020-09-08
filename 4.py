start=int(input("enter the value of starting range"))
end=int(input("Enter the value of ending range"))
while True:
    if(start%3==0):
        print(start,end=" ")
    start+=1
    if start>end:
        break
