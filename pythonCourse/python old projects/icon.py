from  tkinter import *
from PIL import ImageTk,Image

root = Tk ()
root.title("image viewer")
root.iconbitmap('C:/Users/Abdulrahman/Downloads/python/img/unnamed.png')

my_image1 = ImageTk.PhotoImage(Image.open("C:/Users/Abdulrahman/Downloads/python/img/images (27).jpeg"))
my_image2 = ImageTk.PhotoImage(Image.open("C:/Users/Abdulrahman/Downloads/python/img/images (31).jpeg"))
my_image3 = ImageTk.PhotoImage(Image.open("C:/Users/Abdulrahman/Downloads/python/img/images (33).jpeg"))
my_image4 = ImageTk.PhotoImage(Image.open("C:/Users/Abdulrahman/Downloads/python/img/images (34).jpeg"))
my_image5 = ImageTk.PhotoImage(Image.open("C:/Users/Abdulrahman/Downloads/python/img/images (35).jpeg"))
my_image6 = ImageTk.PhotoImage(Image.open("C:/Users/Abdulrahman/Downloads/python/img/images (36).jpeg"))
my_image7 = ImageTk.PhotoImage(Image.open("C:/Users/Abdulrahman/Downloads/python/img/images (24).jpeg"))
my_image8 = ImageTk.PhotoImage(Image.open("C:/Users/Abdulrahman/Downloads/python/img/images (23).jpeg"))
my_image9 = ImageTk.PhotoImage(Image.open("C:/Users/Abdulrahman/Downloads/python/img/images (25).jpeg"))



my_label= Label(image= my_image1)


image_list =[my_image1 ,my_image2, my_image3,my_image4, my_image5, my_image5 , my_image6, my_image7,my_image8 , my_image9]

def forward (image_number) : 
    global my_label
    global button_next
    global button_back


    my_label.grid_forget() 
    my_label = Label(image = image_list[image_number -1])
    my_label.grid(row= 0, column = 0 , columnspan= 3)
    button_next= Button(root , text = ">>" ,  command =  lambda : forward(image_number+1))
    button_back= Button(root , text = ">>" ,  command =  lambda : forward(image_number-1))
    button_back.grid(row =1 , column =0 )
    button_next.grid(row = 1, column = 2)

    if image_number == 9 : 
        button_next= Button(root , text = ">>" ,  state = DISABLED)
        
def back () :

    global my_label
    global button_next
    global button_back




button_back= Button(root , text = "<<" ,command = back)
button_next= Button(root , text = ">>" ,  command =  lambda : forward(2))
button_quit= Button(root, text = " exite" , command = root.quit)




my_label.grid(row= 0, column = 0 , columnspan= 3)
button_back.grid(row =1 , column =0 )
button_next.grid(row = 1, column = 2)
button_quit.grid(row = 1, column = 1)




root.mainloop () 
