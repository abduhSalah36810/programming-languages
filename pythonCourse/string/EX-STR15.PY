"""Write a Python function to convert
 a given string to all uppercase if it contains
 at least 2 uppercase characters in the first 4 
 characters."""


input1 = input("write somthing :")
appers_num = 0
for i in input1[:5] : 
    if i.isupper() : 
        appers_num +=1 
    if appers_num ==  2 : 
     print(input1.upper())   