from tkinter import *
from tkinter.ttk import *

# creation of the main window
main=Tk()
#set the geometry of the window
main.geometry("800x600")
# create a label for user name
user_name=Label(main,text="User Name").place(x=40,y=60) # use the place geometry specifier for positions
#create a area for input using Entry
user_name_input_area = Entry(main,width = 30).place(x = 110,y = 60)# use the place geometry specifier for positions
user_password=Label(main,text="Password").place(x=40,y=100)# use the place geometry specifier for positions
user_password_entry_area = Entry(main,width = 30).place(x = 110,y = 100)  # use the place geometry specifier for positions

submit_button = Button(main, text = "Submit",command=main.destroy).place(x = 40,y = 130)# use the place geometry specifier for positions


main.mainloop()