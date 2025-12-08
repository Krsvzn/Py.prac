import tkinter as tk
import random
import os
import json
window = tk.Tk()
window.title("No Guessing Game")
window.geometry("570x560")

secret_number = random.randint(1,100)
guess_count = 0
filename = "score.json"

my_highscore_label = tk.Label(window, text = "", font = ("Arial",24))
my_highscore_label.grid(row=4,column=0)

if os.path.exists(filename):
   with open(filename, "r") as f:
      high_score = json.load(f)
      actual_highscore = "Highscore : " + str(high_score)
      my_highscore_label.config(text = actual_highscore)

else:
   high_score = 0
   
def checker():
    try:
        guess = my_entry.get()
        actual_guess = int(guess)
        global guess_count
        guess_count += 1
        actual_guess_count = "Guess Count : " + str(guess_count)
        my_count_label.config(text = actual_guess_count)     
       
        if actual_guess == secret_number:
            my_label.config(text = "You Win")
        
        elif actual_guess < secret_number:
            my_label.config(text = "Too Low, Guess Higher")
            
        elif actual_guess > secret_number:
            my_label.config(text = "Too High, Guess Lower")
        global high_score
        if guess_count < high_score:
           high_score =  int(1000/guess_count) 
           actual_highscore = "Score : " + str(high_score)
           my_highscore_label.config(text = actual_highscore)
        else:
           my_label.config(text = "You Lose! :( ")
        if actual_guess == secret_number:
         with open(filename,"w") as f:
           json.dump(high_score,f)   
    except ValueError:
         my_label.config(text = "Only Integers Please!")
                             
my_label = tk.Label(window, text = "Welcome!", font = ("Arial",24))
my_label.grid(row=0,column=0)

my_count_label = tk.Label(window, text = "Guess Count : 0", font = ("Arial",24))
my_count_label.grid(row=3,column=0)

my_entry = tk.Entry(window, text = "", font = ("Arial",24))
my_entry.grid(row=1,column=0)

my_button = tk.Button(window, text = "Check", command = checker)
my_button.grid(row=2,column=0)

my_rules = tk.Label(window, text = "\nRules : Below\n\n1. The Computer Will Guess A Number.\n\n2. You Will Have To Guess A Number .\n\n3. You Will Get Hints If You Are Close .\n\n4. If You Guess The Number, You Win. ", font = ("Arial",24))
my_rules.grid(row=5,column=0)

window.mainloop()

