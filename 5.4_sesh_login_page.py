import tkinter as tk

window = tk.Tk()
window.title("Login Page")
window.geometry("500x500")

my_username = tk.Label(window, text = "Username -> ",font = ("Arial",24))
my_username.grid(row=0,column=0)

my_un_entry = tk.Entry(window, text = "", font = ("Arial",24))
my_un_entry.grid(row=0,column=1)

my_password = tk.Label(window, text = "Password -> ", font  = ("Arial",24))
my_password.grid(row=1,column=0)

my_password_entry = tk.Entry(window, text = "", font = ("Arial",24),show = "*")
my_password_entry.grid(row=1,column=1)

my_button = tk.Button(window, text = "Login", command = "")
my_button.grid(row=2,column=1)


window.mainloop()
