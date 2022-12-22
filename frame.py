import tkinter as tk
from tkinter import END, Canvas, Entry, Label, StringVar, messagebox
import fetcher

tkWindow =tk.Tk()
tkWindow.geometry('400x150')  
tkWindow.title('BORED!')
tkWindow.config(bg="#c4ffd2")
 
frame_1 = tk.Frame(tkWindow, bg='#c4ffd2', width=400, height=50)
frame_1.pack(pady=20)

get_string = StringVar()

def on_click():
    get_string.set(fetcher.get_data())

button = tk.Button(tkWindow,
	text = 'check',
	command = on_click
)  
val = button.invoke()
button.pack()  
my_label = Label(frame_1, bg='#c4ffd2',font=("Arial", 14),
                 textvariable=get_string).pack(pady=10)

tkWindow.mainloop()