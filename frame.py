import tkinter as tk
from tkinter import END, Entry, Label, messagebox
import fetcher

tkWindow =tk.Tk()
tkWindow.geometry('400x150')  
tkWindow.title('BORED!')


frame_1 = tk.Frame(tkWindow, bg='#c4ffd2', width=400, height=50)
frame_1.pack()
frame_1.pack_propagate(0)

my_label = Label(tkWindow,
                 text = "nothing yet!")
my_label.pack()

def on_click(val):
    my_label.config(text=val)

button = tk.Button(tkWindow,
	text = 'check',
	command = on_click(fetcher.get_data())
)  
button.pack()  
val = button.invoke()
  
tkWindow.mainloop()