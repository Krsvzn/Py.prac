import json
import os

filename = "contacts.json"
if os.path.exists(filename):
   with open(filename,"r") as f:
     phonebook = json.load(f)
else:
   phonebook = {}
while True:
 try:
    choice = int(input("____________________________________\n<<<<Welcome To The Contacts>>>>\n\n1. Add Contact -> \n\n2. Search Contact -> \n\n3. Show All Contacts -> \n\n4. Exit -> \n____________________________________\nEnter Your Choice -> "))   
    if choice == 1:
        name = input("\nEnter The Name -> ")
        ph = int(input("\nEnter The Phone Number -> "))
        phonebook[name] = ph
        print("\n\n***Contact Saved Successfully***")
        with open(filename,"w") as f:
           json.dump(phonebook,f)
    elif choice == 2:
        f_name = input("\nEnter The Name Of The Contact To Search -> ")
        if f_name in phonebook:
         print("\n",phonebook[f_name])
        else:
           print("\nContact Not Found")
    elif choice == 3:
       print("***All Contacts In The Phone Book***\n",phonebook)
       
    elif choice == 4:
       print("\nSuccessfully Exited\n____________________________________")
       break
    else:
       print("\n:::::Sorry, Only Enter Values From (1-4)\nTry Again :D")
 except ValueError:
    print("\n:::::::Sorry, Only Integers Allowed As Input :D::::::::\nTry Again :D\n")  

    
