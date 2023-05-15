n= int(input(" Please Enter any No: "))
print("all prime factor of no. :") 
for j in range(1, n + 1):
   if j> 1:
       for i in range(2, j):
           if (j % i) == 0:
               break
       else:
           if(n%j==0):
               print(j,end=",")