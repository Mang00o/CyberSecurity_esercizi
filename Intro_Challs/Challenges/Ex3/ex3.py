import random
import string

vocabulary = list(string.ascii_letters) + list(string.digits)

password = ''

password_size = 10

for i in range(password_size):
    password += random.choice(vocabulary)

#print(f"Password generated = {password}")
print("Password generated =",password)