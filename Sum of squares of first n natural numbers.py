n=int(input ("enter last no. of natural no. series:"))
sum=0
for i in range(1,n+1):
    sum = sum + i**2
print("Sum of squares of first %d natural numbers is %d"%(n,sum))    