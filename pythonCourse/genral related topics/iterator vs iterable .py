# iterable  :

# an object has data that can be iterated upon 
# like => {set , string ,tuple , dict , list}

# EXSMPLE : 

mylist = [1,2,3]
number = 10 
for number in mylist :
    print(number) # iterable 

# for degit in number :
#   print(number)  !!! not iterable
 
print("*"*50)

# ITERATOR : 

# genrates an iterable using iter() and next()

# EXAPLE : 
# if we eanter to iterate over a string 
mystring = "abduh"
myiterator = iter(mystring)
print(next(myiterator)) # a
print(next(myiterator)) # b
print(next(myiterator)) # d
print(next(myiterator)) # u
print(next(myiterator)) # h

print("*"*50)

# that's exactly what we use for loops for
# it does the same thing . 

for letter in iter(mystring) : 
   print(letter)

# what for loops do is generating an iterable 
# with iter() and give u the result with next 
# and break it by break()


