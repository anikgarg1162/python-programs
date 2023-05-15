di={"anik garg":"name"," G L A":"student"}
d2={}
for key,value in di.items():
      d2.update({key.replace(" ",""):value})
print(d2)
