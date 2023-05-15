n=input("enter any character:")
if(n>='a' and n<='z')or(n>='A' and n<='Z'):
    print("character is alphabet.")
elif(n>='0'and n<='9'):
    print("character is digit.")
else:
    print("character is special character.")