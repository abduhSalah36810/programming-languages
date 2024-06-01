# today's lesson is about Generator : 

# what is generators ? 

# it's actully a function with keyword yield 
# instead of return .and it returns a generator 
# object by using next() method or by a for loop.


# Example :

# suppose we wanted to print all numbers in range
#  one milion squared with a for loop 

x = [i**2 for i in range(1000000)]

# don't use the last code . 

def gen (n): 
    for i in range(n):
    	yield i**2
  
g = gen(1000000) 
#for i in g : 
 #  print(i) 	
   
import sys
#without using a generator :
print(sys.getsizeof(x))
# using a generator:
print(sys.getsizeof(g))








