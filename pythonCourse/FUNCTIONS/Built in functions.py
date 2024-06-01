# HI there 🤞

''' we're gonna learn some new cool functions '''

# Ready ? 🤔😉

# let's gooooo 🏃‍♂️


# first one is (any) : 

# - it returns true if there's at least one true 
# element . if not returns false .

print(any(["true " , 2 , 0  ]))
print(any([ False ]))


# second one is (all) :

# returns true if all the items were true .

print(all(["true " , 2 , 0  ]))
print(all([ True , False ]))


# Third one is (bin) : 

# returns any number in the binary form (0101011)

print(bin(64))


# fourth one is (id) : 

# returns the serial number of the element in the
# memory . 

print(id(11111)) 


# fifth one is (sum) : 

# returns the sum of all items in tuple , list etc

print(sum([1,2,4,5]))


# sixth one is (round) : 

# returns a floating point number that is
# a rounded version of the specified number,
# with the specified number of decimals. 
# round (number,digits) . 

print(round(150.32))
print(round(127.0923 , 2 ))

# seventh one is (range) : 


# The range() function returns a sequence 
# of numbers, starting from 0 by default,
# and increments by 1 (by default), and
# stops before a specified number.
# range (start , end , steps)
 

for u in range(0,20,2) :
  print(u)


# 8th one is (print) :

# we use like alote and it's obvios that it 
# prints stuff on the screen but we get a 
# little deep into it 

# -seperating the messages :

print("we are good " , " we are muslims" , sep= "______")

# - between the prints : 
print("hi" , end= "\n")
print("bye")


# the 9th one is (abs) : 

# returns a positive number as the destance
# between zero and the given negative nubmer .

print(abs(-33))


# 10th one is (max) : 

# retuns the maximum item 

print(max([10 , 3 , 483 , 32432]))
print(max("a", "w"))


# 11th one is (min) : 

# retuns the minimum item 

print(min([10 , 3 , 483 , 32432]))
print(min("a", "w"))


# 12th one is (pow) : 

# return the numer to the given power . 
# pow(base, exponent)

print(pow(2,6))


# 13th one is (slice) :

# slices of the data returned 
# slice(start , end , steps)  

s = [1,2,3,4,5,5,6,7]
print(s[slice(2,5,2)])


# 14th one is (map) :

# returns a map object(which is an iterator)
# of the results after applying the given
# function to each item of a given iterable (list, tuple etc.)

def add_me_to_me (number) : 

    return number + number


numbers  = [2, 19 , 23 , 22]

result = map(add_me_to_me,numbers)
print(list(result))

# using map with lambda :

print(list(map(lambda x : x + x , numbers )))


# 15th one is (filter) : 

# filter takes in a function and an iterator
# as arguments and it's used to filter out a 
# all the items in the iterator . and it just 
# return the true value only . 

# example  : 

def names (name) : 
  return name.startswith("w")


hername= ["wesam" , "wesamy" , "wesa" , "soma" ]
result = filter(names,hername)
for i in result : 
  print(i)

# or with filter : 

for i in filter(lambda x : x.startswith("w"),hername) :
  print(i)


# 16th one is (reduse) : 

# The reduce(fun,seq) function is used to 
# apply a particular function passed in its
# argument to all of the list elements mentioned 
# in the sequence passed along.This function is
# defined in “functools” module.

# Working :  

# At first step, first two elements of sequence
# are picked and the result is obtained.
# Next step is to apply the same function to
# the previously attained result and the
# number just succeeding the second element and 
# the result is again stored.This process
# continues till no more elements are left in the
# container.The final returned result is returned and printed on console.

# example : 

from functools import reduce

# initializing list
lis = [1, 3, 5, 6, 2, ]
 
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(reduce(lambda a, b: a+b, lis))
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))

# 17th one is (enumerate) : 


# retuns any thing witha counter (iterator , start)

# example :

list =  ["Arabic" , "french" , "english" , "physics"   , "chimestry"  , "math"]

for number, subject in enumerate(list , 0 ) : 
  print (f"{number} => {subject}")


# 18th one is (help) : 

# IF wanted to learn somthing without going online
# u can use help to get some help 😉😂

print(help(reduce))


# 19th one is (reversed) :

# reverces whatever 

for i in reversed(list) : 
  print(i)


# الحمدلله خلصنا 😂


