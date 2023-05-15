import random
x = int(input("enter no.:"))
c = random.randint(1, 100)
if x < c:
     print("Number is low")
elif x > c:
     print("Number is high")
elif x == c:
     print("correct")
print("no. is :",c)