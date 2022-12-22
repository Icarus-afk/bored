import tkinter as tk
from tkinter import END, Entry, messagebox
import fetcher

tkWindow =tk.Tk()
tkWindow.geometry('400x150')  
tkWindow.title('BORED!')

entry=Entry(tkWindow, width= 70)
entry.pack()

frame_1 = tk.Frame(tkWindow, bg='#c4ffd2', width=400, height=50)
frame_1.pack()
frame_1.pack_propagate(0)

def on_click(text):
   entry.delete(0, END)
   entry.insert(0,text)

button = tk.Button(tkWindow,
	text = 'check',
	command = on_click(fetcher.get_data()))  
button.pack()  


  
tkWindow.mainloop()