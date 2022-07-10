from ctypes import alignment
from tkinter import *
from tkinter.ttk import * # The tkinter.ttk module provides access to the Tk-themed widget set, introduced in Tk 8.5


root=Tk() # creates the GUI Instance Object which we are gin to use in the programming which is called the main window

root.title("MpxOne All Programming Tool")
root.geometry("800x600")

btn1=Button(root,text="Exit",command=root.destroy)
btn2=Button(root,text="Exit")

btn1.pack(side="bottom")
btn2.pack(side="top")



root.mainloop()