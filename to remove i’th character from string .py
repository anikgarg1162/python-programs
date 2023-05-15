x=input("Enter something: ")
l=len(x)
nx=''
n=int(input("Enter the position of element which you want to remove :"))
for i in range (0,l):
    if(i!=n-1):
        nx=nx+x[i]
print(nx)