import tkinter as tk

window = tk.Tk()
window.title("my first gui")
window.geometry("300x200")

count = 0

def on_click():
    global count
    count += 1
    my_label.config(text = count)
    pass

my_label =  tk.Label(window, text = "click = 0", font = ("Arial",24))
my_label.pack()

my_button = tk.Button(window, text = "CLick me", command = on_click)
my_button.pack()
window.mainloop()

