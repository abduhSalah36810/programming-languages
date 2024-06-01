""" Write a Python program to get a single string
from two given strings, separated by a space 
and swap the first two characters of each string."""


str1 = input(str("enter it ? "))  
str2 = input(str("enter inother ? "))
str3 = (f" {str2[:2] + str1[-1] }")
str4 = (f" {str1[:2] + str2[-1] }")
output = str3 + " " + str4
print(output)