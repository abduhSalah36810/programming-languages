# file handling : 

# first we neeed to know the current workig dir
# cuz if we wouldn't find it if we were searching
# for the file to read in the wrong place :

# getting things ready :

import os 


print(os.getcwd()) # current working directory
# getting the abslute path of this file  :
print(os.path.abspath(__file__))
# getting the abslute path of this folder :
print(os.path.dirname(os.path.abspath(__file__)))
# change the current working directory : 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# checking changes:
print(os.getcwd())
# finally opening a file :

file = open("what.txt")

# reading the file : 

print(file) # will print the info of this file
#print(file.read()) #all lines as text
print(file.readline(10))
print(file.readlines()) #list of all lines
# controlling lines : 
for line in file : 
    if line.startswith("03") : 
        print(line)
        break

# writing in the file : 

# if the file exists write in it if not make one
# if the file has any thing it will be replaced
# with what u type using writ() :

file = open("what.txt","w")
file.write("what is up")
listy = ["ss"]
file = open("what'sup.txt" , "w")
file.writelines(listy)


# appending in the file : 

# when we append it won't remove what has been
# written befor . and if the file isn't there
# it makes for u : 

file = open("wasup", "a")
file.write("high five me")


# some methodes : 
 
file = open("hi.txt" , "a")

# truncate : removing charcters :

file.truncate(6)

# tell : where the curser is : 
    
print(file.tell())


# seek : seek the begginng of reading :

file= open("hi.txt","r")
file.seek(2)
print(file.read())


# finally closing the file :

file.close()

# and that was everything peace out ✌


