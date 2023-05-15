n=input("enter any string :")
print(n) 

word= {key: n.count(key) for key in n.split()}

print("Words in the string")
print(word)