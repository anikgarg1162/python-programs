m= input("enter 1st string :")
n = input("enter 2nd string")
m=m.split()
n=n.split()
x=[]
for i in m:
    if i not in n:
        x.append(i)
for i in n:
    if i not in m:
        x.append(i)
x=list(set(x))
print("uncomman words are :",x)
