import random
options = ["rock","scissors","paper"]

computer_choice = random.choice(options)

my_choice = int(input("Enter 0 for (Rock)\nEnter 1 for (Scissors)\nEnter 2 for(paper)\n\nEnter Your Choice - "))
if computer_choice == options[0] and my_choice == options[0]:
    print("You both choose Rock.\nDRAW")
elif computer_choice == options[0] and my_choice == 1:
    print("Computer Picked Rock and you picked Scissors.\nComputer Wins")
elif computer_choice == options[0] and my_choice == 2:
    print("Computer Picked Rock and You picked Paper.\n You WIN")
elif computer_choice == options[1] and my_choice == 0:
    print("the computer picked scissors and you picked Rock.\n YOU WIN")
elif computer_choice == options[1] and my_choice == 1:
    print("Computer Picked Scissors and you also picked Scissors.\nDRAW")
elif computer_choice == options[1] and my_choice == 2:
    print("Computer picked scissors and you picked paper.\nComputer Wins")
elif computer_choice == options[2] and my_choice == 0:
    print("the computer picked Paper and you picked Rock.\n Computer WINS")
elif computer_choice == options[2] and my_choice == 1:
    print("Computer Picked Paper and you also picked Scissors.\nYOU WIN")
elif computer_choice == options[2] and my_choice == 2:
    print("Computer picked Paper and you picked paper.\nDraw")
