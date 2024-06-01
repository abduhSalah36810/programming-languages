# What's Polymorphisim ? 

"""
What is Polymorphism: The word polymorphism means having many forms.
In programming, polymorphism means the same function name
(but different signatures) being used for different types.
"""

# method overriding :


"""
Polymorphism lets us define methods in the child class that have the
same name as the methods in the parent class. In inheritance, the child
class inherits the methods from the parent class. However, it is
possible to modify a method in a child class that it has inherited from
the parent class. This is particularly useful in cases where the method
inherited from the parent class doesn’t quite fit the child class.
In such cases, we re-implement the method in the child class
"""


# Method overridding : 

"""
deffirent functions have the same name but the fucntionality is 
deffirent and this is un unluckly not available in python .
"""

# a way to overcome this problem : 

# @dispatch :

from multipledispatch import dispatch


#passing one parameter
@dispatch(int,int)
def product(first,second):
    result = first*second
    print(result)
  
#passing two parameters
@dispatch(int,int,int)
def product(first,second,third):
    result  = first * second * third
    print(result)
  
#you can also pass data type of any value as per requirement
@dispatch(float,float,float)
def product(first,second,third):
    result  = first * second * third
    print(result)
  