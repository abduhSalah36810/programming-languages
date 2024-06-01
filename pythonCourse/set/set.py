""" today's lesson is set which is a data type let's 
jump right into it : """

# what a set looks like :

our_set = {1 , 2  , 3}
print(our_set)

# set properties :
# 1- Sets are unordered.
# 2- Set elements are unique. Duplicate elements are not allowed.
# 3- A set itself may be modified,but the elements 
#    contained in the set must be of an immutable type.
 
# now let's get to the set methods :


#clear 
s ={1.30 , 22 , "woah" }
s.clear()
print(s)

#add 
e = {9,8,7}
e.add(6)
print(e)

# dicared and remove 
w = {5, 4.4 }
#w.remove(4)
#print(w)

#that gives us an error cuz 4 is noy in the set but 
#if we used discared ineasted we won't get an error :

w.discard(4)
print (w)


#union and update 
q = {"dd" , "ff"}
print(w.union(q))
t = {"true" , True}
t.update([2, 3 , 4])
print(t)

#copy
x = t.copy()
print(x)

#pop 
print(w.pop())



