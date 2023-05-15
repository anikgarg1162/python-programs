n=input("Enter the string :")
z=n.split()
l=len(z)
f=input("Enter the find String :")
for i in range(0,l):
    if(z[i]==f):
        print("The Element is found")
        break
else:
    print("Element is not found")
