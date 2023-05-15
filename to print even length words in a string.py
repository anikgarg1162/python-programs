x=input("Enter the String :")
z=x.split()
l=len(z)
for i in range(0,l):
    if(i%2!=0):
        print(z[i],end=",")
