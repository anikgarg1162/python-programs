n=input("Enter string in snake case :")

res = n.replace("_", " ").title().replace(" ", "")

print("The String after changing in pascal case : " + str(res))
