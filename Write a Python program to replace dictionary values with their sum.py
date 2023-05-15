li=[{"term1":100,"term2":70},{"term1":200,"term2":85},{"term1":700,"term2":65}]
for d in li:
    d["total"]=d.pop("term1")+d.pop("term2")
print(li)