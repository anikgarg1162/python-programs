di={1:"anik",2:"garg",3:[10,20,50,30],5:[3,8]}
count=0
for keys,val in di.items():
     if type(val)==list:
       count+=1
print(count)