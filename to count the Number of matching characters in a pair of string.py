x=input("Enter the first string :")
y=input("Enter the second string :")
x1=set(x)
y1=set(y)
match= (x1 & y1)
print("total matching characters : ",len(match))
