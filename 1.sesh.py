import random

secret_number = random.randint(1,100)
print("A Number Has Been Chosen, Now Its your time to choose :D")
num = secret_number
guess = int(input("Enter Your choice - "))

while num != guess:
    if guess < num:
        print("Too low pick higher")
        guess = int(input("Enter Your choice - "))
    elif guess > num:
        print("Too High pick lower")
        guess = int(input("Enter Your choice - "))
    if guess == num:
        print("We Have A winner")
        
