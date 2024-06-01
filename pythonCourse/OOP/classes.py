# what's a class ?  

"""
it's the constructor of the instance which is
the object . the class has its own attributes 
behaviors and methods so the object .
"""

# class syntax : 

# (class ) name of it : 
#   (def ) __init__ (self) : 
#        the attributes snd the methods


# what's init  ? 

"""it's a must be called method every time you
creat an object from a class to initailize the
data"""


# what is self  : 

"""it refers to the current inctance u can name
it any anything and must be the first parammeter """



class members : 
    
    # class attributes : 
    
    allowed_age = range(18, 50)
    users_number = 0

    # class methodes : 

    @classmethod
    def users_counter (cls) : 
        print(f"the users number is {cls.users_number}")
    
    # static method : 

    """ we use it when don't need acess to both of the class
    or the instance to make it  . it's just related to the 
    class """

    def company_name(): # no need for args 

        print("welcome to creartors".upper())


    # instance :

    def __init__ (member , member_name , member_salary, age, gender ) : 
            
            # istance attributes :    

            member.name =  member_name
            member.salary = member_salary
            member.age = age
            member.gender = gender
            members.users_number += 1 

    # method :

    def greeting(member) :

            if member.gender == "male" : 
             return f"welcome mr {member.name} we hope you're ok"
            else : 
             return f"welcome madame {member.name} we  hope your ok"

    def age_checker(member) :

            if member.age in members.allowed_age : 
                return(members.greeting(member))
            else : 
                print("ur underage")

    @property # no need for prameter so we convet it to a property
    def sayhi (member) : 
        return "hi"


members.company_name()
memberone = members("ali" , 4400 , 18 , "male")
member2 = members("mona" , 5000 , 20 , "female")
print(member2.age_checker())
members.users_counter()
