import tkinter as tk

window = tk.Tk()
window.title("From Miles To Km")
window.geometry("300x300")

def conversion():
    data = my_entry.get()
    number = float(data)
    c = number * 1.6
    my_label.config(text = str("%.2f"%c) + " Km")
    
my_entry = tk.Entry(window, text = "", font = ("Arial",24))
my_entry.pack()

my_label = tk.Label(window, text = "Miles to Km", font = ("Arial",24))
my_label.pack()

my_button = tk.Button(window, text = "Convert", command = conversion)
my_button.pack()

window.mainloop()
