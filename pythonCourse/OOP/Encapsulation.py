# WHAT'S IS ENCAPSUlation ?

"""
Encapsulation is defined as the wrapping up of data under a single
unit. It is the mechanism that binds together code and the data it
manipulates. Another way to think about encapsulation is, it is a 
protective shield that prevents the data from being accessed by the 
code outside this shield

"""


# Advantages of Encapsulation :  

"""

Data Hiding :

The user will have no idea about the inner implementation 
of the class. It will not be visible to the user how the class is 
storing values in the variables. The user will only know that we are
passing the values to a setter method and variables are getting 
initialized with that value.

Increased Flexibility : 

We can make the variables of the class read-only or write-only 
depending on our requirement.

"""

# access specifiers. : 

"""

1- puplic :

A public member is accessible from anywhere outside the class 
but within a program. You can set and get the value of public
variables without any member function 

2- protected :

A protected member variable or function is very similar to a private
member but it provided one additional benefit that they can be accessed
in child classes which are called derived classes.

3- private :

A private member variable or function cannot be accessed, or even 
viewed from outside the class. Only the class and friend functions 
can access private members.

"""

# setters and getters : 

"""
they help you to get or set the private variable's values
by defining function inside the calss to do this . 

"""

# Example : 


class member  :

    def __init__(self , name , age, id ) :
        self.__name = name # => privat
        self._age = age  # => protected 
        self.id = id # => puplic

    def namegetter (self) : # => Getter
        return self.__name
    
    def namesetter (self , newname) : # => Setter
        self.__name = newname



class member1(member) : 

    def __init__(self) : 
       pass
      


mem = member("ahmed" , 20 , 20202020)
mem1 = member1() 
#print(mem.__name) # => name variable is private so it's an error
print(mem._age) # member1 inherited from member so age as protected works 
print(mem.id) # it's already puplic so it will print the value
print(mem.namegetter()) # getting a privte value
(mem.namesetter("amanda")) # modifing the private value
print(mem.namegetter()) # getting the new one . 




""" after all, you can always edit the source of the class itself to 
achieve the same effect. Python drops that pretence of security and
encourages programmers to be responsible. In practice, this works very
nicely. """