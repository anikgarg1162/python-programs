n=int(input("enter any no. :"))
count=0
b=n
while(b>0):
    c=b%10
    count=count+c**3
    b=b//10
if (count==n):
    print("no. is armstrong")
else:
    print("no. is not armstrong")         