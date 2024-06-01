"""tody's lesson is about the most important 
cuz it's like genral use in programming """

# function is somthing that does specific orderes
# we define it by keyword (def) and we give it a name
# you give it inputs as arguments. 
# it's does whatver the block of code was . 
# return the value of the prossecc . 
# but firt u call it . 
# the name of the inputs in the fuction definition
# is prameters  .

# example : 


def math (input1 , input2) : # defining the function
    
  return input1*input2  # the funcionality 


print(math(3,3)) # calling it and printing the result 

# exercise : how to muliply list items ? 

def func (list) :
    result = 1
    for i in list :       
         result = result * i
         print(result)
    return result  

print(func([1,2,4,5,6,7]))


# this was in case we know the number of the inputs
# if we don't know we use (*) to unpack 


# unpaking  :
# in this case we want to sum all the numbers 
# in every list but we don't know the number 
# of them so we use * to unpack them . 

def list_sum (*lists) :
    list2  = []
    for i in lists : 
        for x in i  :
            list2.append(x)
    return sum(list2)


print(list_sum( [1,2,3],[4,5,6],[7,8,9] ))


# unpacking dictionaries : 

# We use (**) to unpack the keys and values

def func2 ( name = "unkown", **dash ) : 
    print(name)
    for i , o in dash.items() : 
      print(f"{i} => {o}")   
    
func2(name = "abduh" , age = 17)



# function scope : 

"""it means the type of variable inside 
or out the fuction"""


# 1- globle : out of the function 

x = 3 
print(x)

# 2- local : inside the function

def func3 () : 
    x = 5 
    print(x) 
 
func3()

# in short what happens in the function 
# stays in teh function 😂 unless we 
# wanted to globel the varialble :

def func3 () : 
  global  x 
  x = 5 
  print(x) 
 
func3()

# consequently if we print the value of
# x now will have five printed cuz now 
# it is the last definition of that variale


# function recursion : 
''' the fuction is reapeted inside it self 
over and over again until the task is done '''

# for example if wated to make a function 
# that returns the given word with no repeaterd
# letters => wwwwwwwwooooooowwwww => wow

def func4 (theword) : 
    
    if len(theword) == 1  : 
        return theword 
    if theword[0] == theword[1] :
        return func4(theword[1:])
    return theword[0] + func4(theword[1:])


print(func4("wwwwwwwwooooooowwwww"))


# lambda function : 

""" In Python, an anonymous function is a
function that is defined without a name.
While normal functions are defined using the
def keyword in Python, anonymous functions 
are defined using the lambda keyword.
"""  

# example : 

# Here is an example of lambda function 
# that doubles the input value.

# => variable = keyword (lambda) (argument) : (expression) 

double = lambda x : x *2
print(double(3))

# why do we use it :

""" In Python, we generally use it as an 
argument to a higher-order function
(a function that takes in other functions as 
arguments). Lambda functions are used along with
built-in functions like filter(), map() etc.
"""

# example with filter()  :

# filter  takes in a function and a list 
# as arguments and it's used to filter out a 
# all the items in the list  : 

mylist= [1,2,3,4,5,7,8,9,10,11,12]
newlist= list(filter(lambda  x : (x%2==0),mylist ))
print(newlist)

# that's all of it 🤷‍♂️