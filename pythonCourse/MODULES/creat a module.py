# how to creat a module :

# first we need to know the system pathes 
# that we can import form to creart our 
# modules there: 


import sys 

print(sys.path)

# u also can append a new path :

sys.path.append(r"F:\try")

# so i have created a module and imma import it :

from my_module import*

print(reverse_string("racecar"))

# we can also refer to my module with any name :

# import my_module as moduly






