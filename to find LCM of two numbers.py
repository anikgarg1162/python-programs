n1=int(input("enter any no. :"))
n2=int(input("enter any no. :"))
if(n1>n2):
    small=n2
else:
    small=n1
for i in range (1,small+1,1):
    if(n1%i==0) and (n2%i==0):
        gcd=i

LCM=(n1*n2)//gcd
print("LCM of number :",LCM)