phonebook = {}

while True:
    choice = int(input("____________________________________\n<<<<Welcome To The Contacts>>>>\n\n1. Add Contact -> \n\n2. Search Contact -> \n\n3. Show All Contacts -> \n\n4. Exit -> \n____________________________________\nEnter Your Choice -> "))
    if choice == 1:
        name = input("\nEnter The Name -> ")
        ph = int(input("\nEnter The Phone Number -> "))
        phonebook[name] = ph
        print("\n\n***Contact Saved Successfully***")
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
       
        
    

    
