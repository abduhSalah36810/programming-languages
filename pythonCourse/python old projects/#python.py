
from tkinter import *
from PIL import ImageTk,Image
root = Tk()
from tkinter import messagebox
fram = LabelFrame(root ,text= "password" , border = 2 , bg= "black"  , fg= "white")
fram.pack(padx = 30 , pady = 50)
e = Entry(fram , border =5)
e.pack(padx= 10 , pady = 10 )
def open (): 
    password = "123"
    code = e.get()
    if code == password:
      new_window = Toplevel()
      new_window.title("just a window")

    if code != password :
      bel=  Label(fram, text= "invalid password" ).pack()
button = Button(fram, text = "submite",  command = open).pack()
root.mainloop()