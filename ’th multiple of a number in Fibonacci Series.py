n1=int(input('Enter the number:'))
n2=int(input('Enter the nth:'))
f1 = 0
f2 = 1
i =2
while i!=0:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    if f2%n1 == 0:
        print(n2*i)
    i+=1
