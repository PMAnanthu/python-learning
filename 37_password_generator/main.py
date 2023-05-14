'''Password Generator Code'''
import random

CHARS=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L',
       'l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T',
       't','U','u','V','v','W','w','X','x','Y','y','Z','z']
NUMBERS = ['0','1','2','3','4','5','6','7','8','9']
SYMBOLS=['!','@','#','$','%','^','&','*','(',')','-','+','=','[',']','|']
number_of_char = int(input("How many letters would you like in your password?  "))
number_of_symboles = int(input("How many symbols would you like? "))
number_of_digits = int(input("How many number would you like? "))

PASSWORD = []
for char in range(0,number_of_char):
    PASSWORD.append(random.choice(CHARS))

for symbol in range(0,number_of_symboles):
    PASSWORD.append(random.choice(SYMBOLS))

for digit in range(0,number_of_digits):
    PASSWORD.append(random.choice(NUMBERS))

random.shuffle(PASSWORD)

PWD_STR="".join(PASSWORD)

print(PWD_STR)
