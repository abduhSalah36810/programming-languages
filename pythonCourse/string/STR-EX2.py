""" Write a Python program to get a string made 
the first 2 and the last 2 chars from a given
a string. If the string length is less than 2,
return instead of the empty string. """

input1 = input(str("what's the ur word ?").strip())
if len(input1) >= 2 :
   word= input1[:2] + input1[-2:] 
   print (word)
elif len(input1) < 2  : 
   word = "legnth problem"
   print(word) 