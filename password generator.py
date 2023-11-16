import random
uper_letter = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower_letter = uper_letter.lower()
digits = "0123456789"
symbols =" ,./;'[]-=<>?:{}+_()*&^%$#@!~'|"

uper,lower,number,symbol = True ,True, True,True
add=""
if uper:
    add+=uper_letter
if lower:
    add+=lower_letter
if number:
    add+=digits
if symbol:
    add+=symbols
length = 15
amount = 10

for x in range (amount):
    password ="".join(random.sample(add,length))
    print(password)