import random
min = 1
max = 7
x = random.randint(min, max)
for i in range(1,7):
     if x == 6:
        print("It's 6 games end")
        break
     else:
        print("Not six , roll it again.")