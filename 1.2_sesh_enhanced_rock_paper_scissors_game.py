import random

options = ["rock","scissors","paper"]

computer_choice = random.choice(options)
print("\n<<<<<ROCK>>>>>     <<<<<PAPER>>>>>     <<<<<SCISSORS>>>>>\n")
my_choice = int(input("Enter Your Choice ... 0(Rock) 1(Scissors) 2(Paper) -> "))
user_choice = options[my_choice]

if computer_choice == user_choice:
    print("You Picked = ",user_choice,"\nComputer Picked = ",computer_choice,"\n\nIts A (Draw)")

elif computer_choice == "rock" and user_choice == "scissors" or\
 computer_choice == "paper" and user_choice == "rock" or\
 computer_choice == "scissors" and user_choice == "paper":
    print("You Picked = ",user_choice,"\nComputer Picked = ",computer_choice,"\n\nYou Loose (COMPUTER WINS)")
else:
    print("You Picked = ",user_choice,"\nComputer Picked = ",computer_choice,"\n\nYou WIN <3")
  
