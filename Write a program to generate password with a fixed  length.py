import random
import string
length=int(input("Enter the desired length of the password:"))
characters=string.ascii_letters+string.digits
password=""
for i in range(length):
    password+=random.choice(characters)
print("Generated password:",password)