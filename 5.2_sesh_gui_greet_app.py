import tkinter as tk

window = tk.Tk()
window.title("Greet Application")
window.geometry("300x300")

def show_name():
    user_text = my_entry.get()
    my_label.config(text = "hello " + user_text)
    
my_entry = tk.Entry(window, text = "",font = ("Arial",24))
my_entry.pack()

my_label = tk.Label(window, text = "", font = ("Arial",24))
my_label.pack()

my_button = tk.Button(window, text = "Greet me", command = show_name)
my_button.pack()

window.mainloop()                    
