import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation


all_characters = letters + digits + symbols
n = int(input("<<<<<Welcome To Password Generator>>>>>\n\nEnter The Length Of Your Password -> "))

for i in range (0,n):
    random_password = random.choice(all_characters)
    print(random_password,end='')
    i+1
