import random

caract = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

long = int(input("¿Cuantos caracteres?"))

for i in range(long):
    password += random.choice(caract)

print(password)    
