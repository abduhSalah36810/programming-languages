"""Write a Python program to convert temperatures
 to and from celsius, fahrenheit."""


input1 = int(input("enter the degree : "))
input2 = input ("enter the unit  c or f: " ).lower()
if input2 == "c" :
    degree = 1.8 * input1 + 32 
    print(f"that equels {degree} F ")
elif input2 == "f" : 
    degree = 1.8 * input1 - 32
    print(f"that equels {degree} C ")