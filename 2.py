a="technical hub"
b="python123"
for i in range(4):
    li=input("Enter a login id")
    pw=input("Enter a password")
    if li==a and pw==b:
        print("Logged in successfully")
        break
    else:
        print("failure")
else:
    print("blocked for 24 hours")
