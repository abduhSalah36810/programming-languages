#  the idea is all about operators let's see :

# first, Arithmetic operators:
''' 
Arithmetic operators are used to perform mathematical 
operations like addition, subtraction, multiplication, etc.
like -> (+,-,*,/,%,//,**)
'''
# second, assignment operatores :

''' 
we use them to assign values to variables.
(x)->"variable",(=)->"operator",(10)->"value"
x = 10  
print(x)  # i think u got it 😁
'''

'''
in case we wanted to perform any sort of
operations on a variable like adding it to other
or even itself so instead of typing it this way
-> x = x + y we type it like this x += y :
'''

#addition
y = 4
z = 2 
z += y
print(z) 

#subtraction
w = 5 
r = 1
w -= r
print(w)

#multiplication
q = 6 
e = 7
q *= e
print(q)


#division
t = 80 
i = 10 
t /= i
print(t)



# ood or even
v= 20
b = 30
n= 8
o = 3
v %= o #even
b %= n #odd
print(v)
print(b)

# c to the power of m
c= 3 
m = 2 
c**= m
print(c)

# how many fours 15 has 
k = 15
d = 4
k //= d
print(k) 


# third , comparision operators :

"""
we use them to compare between to conditions
"""

# greater than and greater than or equal 
h = 4 
a = 10
u = 10 
print(a<b)
print(10 <= b)

# smaller than and smaller than or equel :
ad = 220
az = 229
aw = 229
print(az > ad)
print(az >= aw)

# equelity and unequelity :
ae = "shit"
aq = 'shit'
print(ae == aq)
print(1!=2)

# fourth, Special operators :
 
# 1- Identity operators :

'''
they are used to check if two values
(or variables) are located on the same part
of the memory. Two variables that are equal does
not imply that they are identical.
'''
# is and is not  
x1 = 4 
x2 = "abdoh"
y1= 4 
y2= "abdoh"
print(x1 is y1)
print(x2 is not y2)


# 2- Membership operators:

'''
They are used to test whether a value or
variable is found in a sequence 
(string, list, tuple, set and dictionary),but
In a dictionary we can only test for presence 
of key, not the value.
'''
# in and not in :
name = "abdoh" 
face = [ 'nose', 'ear' , 'eye' ]
years = (2004 , 2005)
info = { 
"name" : "abdoh" ,
"face" : [ 'nose', 'ear' , 'eye' ] ,
"years" : (2004 , 2005)  }

print("a" in name)
print("leg"  not in face  )
print(2006 in years)
print("name" in info )






