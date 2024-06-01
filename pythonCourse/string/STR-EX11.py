"""Write a Python script that takes input from the user and displays that input back in upper and lower cases."""


input1= input(str("type a word  : "))
check= input1.islower()
check1= input1.isupper()
if check : 
  print(input1.upper())
if check1: 
  print(input1.lower())