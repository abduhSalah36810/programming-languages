from tkinter import *
from PIL import ImageTk, Image

root = Tk()


cool = IntVar()
Radiobutton(root, text = "answer 1 " , variable = cool , value = 1).pack()
Radiobutton(root, text = "answer 2 " , variable = cool , value = 2).pack()









root.mainloop()