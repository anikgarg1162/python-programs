n=input("enter string :")
d=int(input("enter no. to rotate :"))
Lfirst = n[0 : d]
Lsecond = n[d :]
Rfirst = n[0 : len(n)-d]
Rsecond = n[len(n)-d : ]
print ("Left Rotation : ", (Lsecond + Lfirst) )
print ("Right Rotation : ", (Rsecond + Rfirst))
