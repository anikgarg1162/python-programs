x=int(input("Enter the number"))
sum=0
l=len(str(x))
z=x
for j in range(0,l):
    mul=1
    rem=x%10
    for i in range(1,rem+1):
        mul=mul*i
    sum=sum+mul
    x=x//10   
if(z==sum):
    print("no. is Strong Number")
else:
    print("no. is Not a Strong Number") 
