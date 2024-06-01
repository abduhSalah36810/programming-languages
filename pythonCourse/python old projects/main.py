from tkinter import *

root = Tk() 
root.title ("simple calculator")

e = Entry( root, width = 35  , borderwidth = 5)
e.grid(row = 0 , column = 0 , columnspan = 4,   padx=10 , pady = 5)


def button_click (number) : 
  crunnet = e.get()   
  
  e.delete(0, END)

  e.insert(0 , str(crunnet ) + str(number))


def button_clear () : 
    e.delete(0, END)

def button_add () :
  first_number = e.get()
  e.delete(0,END)
  global f_num
  global math
  math = "addition"
  f_num = int(first_number)
  


def button_divide () :


  first_number = e.get()
  e.delete(0,END)
  global f_num
  global math
  math = "division"
  f_num = int(first_number)
  


def button_subrtact () :

  first_number = e.get()
  e.delete(0,END)
  global f_num
  global math
  math = "subtraction"
  f_num = int(first_number)
  

def button_multiplay() :

  first_number = e.get()
  e.delete(0,END)
  global f_num
  global math
  math = "multiplication"
  f_num = int(first_number)
  

def  button_return () :
  first_number = e.get()
  e.delete(0,END)
  global f_num
  global math
  math = "return"
  f_num = int(first_number)
    
    
def  button_equal () : 
  second_number = e.get ()
  e.delete(0,END)
  
  if math == "addition" :
     e.insert(0 , f_num  + int(second_number)) 
  if math == "division" : 
     e.insert(0 , f_num  / int(second_number)) 
  if math == "multiplication" : 
     e.insert(0 , f_num  * int(second_number)) 
  if math == "subtraction" :
     e.insert(0 , f_num  - int(second_number)) 
  if math == "return" :
     e.insert(0 , f_num  % int(second_number)) 



button_clear = Button( text = " clear " , width = 22 , command = button_clear ) 
button1 = Button( text= " 1 " , padx = 10, pady = 5,command= lambda :  button_click (1)) 
button2 = Button( text= " 2 " , padx = 10, pady = 5, command= lambda :  button_click (2)) 
button3 = Button( text= " 3 " , padx = 10, pady = 5 ,command= lambda :  button_click (3)) 
button4 = Button( text= " 4 " , padx = 10, pady = 5 ,command= lambda :  button_click (4)) 
button5 = Button( text= " 5 " , padx = 10, pady = 5 ,command= lambda :  button_click (5)) 
button6 = Button( text= " 6 " , padx = 10, pady = 5 ,command= lambda :  button_click (6)) 
button7 = Button( text= " 7 " , padx = 10, pady = 5 ,command= lambda :  button_click (7)) 
button8 = Button( text= " 8 " , padx = 10, pady = 5 ,command= lambda :  button_click (8)) 
button9 = Button( text= " 9 " , padx = 10, pady = 5 ,command= lambda :  button_click (9)) 
button0= Button( text= " 0 " , padx = 10, pady = 5 ,command= lambda :  button_click (0))
button_add= Button( text= " + " , padx = 10, pady = 5 , command = button_add) 
button_multiplay = Button( text= " *  " , padx = 10, pady = 5 , command =  button_multiplay ) 
button_equal= Button( text= " = " , padx = 10, pady = 5 , command = button_equal) 
button_divide= Button( text= " /  " , padx = 10, pady = 5 , command = button_divide)  
button_Decimal_point= Button( text= " .  " , padx = 10, pady = 5 , command= lambda :  button_click (.0 ) )
button_subtract= Button( text= " -  " , padx = 10, pady = 5  ,  command = button_subrtact) 
button_presntage= Button( text=  " % " , padx = 8, pady = 4 , command = button_return ) 


 
button_clear.grid(row= 1, column = 0 , columnspan = 3)

button1.grid( row =4  , column = 0)
button2.grid( row =4  , column = 1)
button3.grid( row =4  , column = 2)

button4.grid( row = 3, column =0 )
button5.grid( row = 3, column =1)
button6.grid( row = 3, column =2 )

button7.grid( row = 2 , column = 0)
button8.grid( row = 2 , column = 1)
button9.grid( row = 2 , column = 2)
button0.grid( row = 5, column = 1)

button_add.grid( row = 3 , column = 3)
button_multiplay.grid( row = 1 , column = 3)
button_equal.grid( row = 5 , column = 3)
button_divide.grid( row =2 , column =  3)
button_Decimal_point.grid( row =5 , column =  2)
button_subtract.grid( row = 4, column =  3)
button_presntage.grid(row = 5 ,column = 0  )







root.mainloop()
