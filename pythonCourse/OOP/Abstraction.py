# WHTA'S ABSTRACTION ? 

"""
Abstraction is used to hide the internal functionality of the function
from the users. The users only interact with the basic implementation 
of the function, but inner working is hidden. User is familiar with 
that "what function does" but they don't know "how it does."

In simple words, we all use the smartphone and very much familiar 
its functions such as camera, voice-recorder, call-dialing, etc., but 
we don't know how these operations are happening in the background. 
Let's take another example - When we use the TV remote to increase the
volume. We don't know how pressing a key increases the volume of the TV.
We only know to press the "+" button to increase the volume.
"""

# technicly speaking  : 

"""
A class that consists of one or more abstract method is called the 
abstract class. Abstract methods do not contain their implementation.
Abstract class can be inherited by the subclass and abstract method 
gets its definition in the subclass. Abstraction classes are meant to
be the blueprint of the other class. An abstract class can be useful
when we are designing large functions. An abstract class is also helpful
to provide the standard interface for different implementations of
components . 

"""

# EAMPLE : 


from abc import ABC,abstractmethod 

class subjects (ABC) : 
    @abstractmethod
    def studystate (self) : 
        pass


class maths (subjects) : 
    def studystate (self) : 
        return("it's going good here 😁")


class physics (subjects) : 
    def studystate (self) : 
        return(" 85 %  👍")


class chemisrty (subjects) : 
    def studystate (self) : 
        return("outstanding 😁")


ch  = chemisrty()
py = physics()
ma = maths()
print(ch.studystate())
print(py.studystate())
print(ma.studystate())