""" Write a Python program to get a string from
a given string where all occurrences of its
first char have been changed to '$',except 
the first char itself. """


input2 = input(str("ur word ?"))
sa = input2[0]
for i in input2 :
   if sa == i :
      input2 = input2.replace(i, "$")
      output = sa + input2[1:]
print(output)    
      










