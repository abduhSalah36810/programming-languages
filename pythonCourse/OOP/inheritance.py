# WAHT'S INHERITANCE ? 

"""
Inheritance is the capability of one class to derive or inherit the
properties from another class. 

"""

# The benefits of inheritance : 

"""
1- It represents real-world relationships well.

2- It provides reusability of a code. We don’t have to write the same
code again and again. Also, it allows us to add more features to a class
without modifying it.

3- It is transitive in nature, which means that if class B inherits from
another class A, then all the subclasses of B would automatically 
inherit from class A. (MULTIPLE INHERITANCE)
"""

# EXASMPLE :

class person () : 
    def __init__ (self, name , age , weight ) :
        self.name =name
        self.age = age
        self.weight = weight 
    def isstudent (self): 
        return False
    def isemployee  (self) : 
        return False


class student (person) : 
    def isstudent (self): 
        return False

class Employee (person) :
    def isemployee  (self) : 
        return False


student1 = student("mohammed" , 20 , 74)
Employee1 = Employee("wesam" , 25 , 70) 


