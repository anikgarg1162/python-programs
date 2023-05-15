x=int(input("Enter the Salary of user"))
if(x>=20000):
    hra=x*0.2
    da=x*0.8
elif(x>=10000 and x<=20000):
    hra=x*0.25
    da=x*0.9
else:
    hra=x*0.3
    da=x*0.95
gross=x+hra+da
print("The total gross of User is ",gross)