from tkinter import * 
from tkinter import messagebox
import fetcher

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('BORED!')

frame_1 = tkWindow.Frame(tkWindow, bg='#c4ffd2', width=400, height=50)
frame_1.pack()
frame_1.pack_propagate(0)


def showMsg():  
    messagebox.showinfo('Message', 'You clicked the Submit button!')

button = Button(tkWindow,
	text = 'Submit',
	command = fetcher.get_data())  
button.pack()  
  
tkWindow.mainloop()