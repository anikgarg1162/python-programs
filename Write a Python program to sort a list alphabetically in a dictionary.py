# di={1:["aman","leo"],2:["itsz","kevin"],3:["mj","saumyajeet"]}
# for i,j in di.items():
#    d2={i:sorted(j)}
# print(d2)
# Python program to sort the list
# alphabetically in a dictionary
dict={
	"L1":[5,28,15,1],
	"L2":[2,00,3,20],
	"L3":[1,78,2,9],
	"L4":[40,4,14,7]
}

print("\nBefore Sorting: ")
for x in dict.items():
	print(x)

sorted_dict = {i: sorted(j) for i, j in dict.items()}
print("\nAfter Sorting: ", sorted_dict)
