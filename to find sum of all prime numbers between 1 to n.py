n= int(input(" Enter  the No. you want : "))
count=0  
for j in range(1, n + 1):
   if j> 1:
       for i in range(2, j):
           if (j % i) == 0:
               break
       else:
           count=count + j
print("sum of all prime numbers between 1 to",n,"is",count)     