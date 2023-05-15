p=int(input("enter number of physics :"))
c=int(input("enter number of chemistry :"))
b=int(input("enter number of biology:"))
m=int(input("enter number of mathematics:"))
com=int(input("enter number of computer:"))
percentage=(p+c+b+m+com)*0.2
print("percentage is",percentage)
if(percentage>=90):
    print("grade A")
elif(percentage>=80 and percentage<90):
    print("grade B")
    if(percentage>=70 and percentage<80):
        print("grade C")
    if(percentage>=60 and percentage<70):
        print("grade D")    
    if(percentage>=40 and percentage<60):
        print("grade E")  
else:
    print("grade F")

    










