from tkinter import Tk
from tkinter import Label
from tkinter import Button

root = Tk()
mylabel = Label(root,text="I am a label widget")
mybutton = Button(root,text="I am a button")
mylabel.pack()
mybutton.pack()
root.mainloop()

