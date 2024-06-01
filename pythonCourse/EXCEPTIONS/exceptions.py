# IT's been along time since the last time 😅

"""  ERRORS - EXCEPTIONS RAISING  """

# WHAT're EXXCEPTIONS  ? 

"""
it's a runtime error reporting mechanisim 
giving you a messege to understand the problem 
according to some types such as (syntaxerror)

"""


# WE CAN RAIS OR OWN EXEPTIONS :

"""if u asked the user through ur app to 
type a a positive number and he typed a negtive 
one that's an error accornding to ur own rules
so we gotta rais an exeption"""

x = int(input("a positive number  :"))
if x < 0 : 
    raise Exception ("this is not positve")


# to have a full controle on ur exceotions :
# we use {try , except , else , finally }

"""
that's an exapmle a funny one to say 
we wanna make the user to read a file 
so he must write a path if he missed 
the program countinues cuz we are in 
control and we would give him 5 tries..

"""

file = None
numtry = 5

while numtry > 0 : 

    try : 

      input1 = input("enter a path  : ").strip()
      file = open(input1 , "r")
      print(file.read())

      break

    except FileNotFoundError:
      print("this is not the one")
      numtry -= 1
      print(f"you still have {numtry} tryies left ")

    finally : 
        if file is not None  :
            file.close()
else : 
    print("tries are over")


















