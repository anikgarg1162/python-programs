n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("this is fibonacci number")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("this is fibonacci number")
    else:
        print("this is not a fibonacci number")