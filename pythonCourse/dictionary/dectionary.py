""" today's lesson is all about dectionaries 
let's go ahead and see what it is 😁 :  """

# what a dectionary looks like :

dec = {"islam" : "muslim"}

# nested dectionary :

dec2 = {"hobbies" : {
    "writing" : "poetry" , 
    "reading" : ["economy" , "pscycology" ] } }


#dectionary properties :

# 1-DECT = {key : value} 
# 2-it's not indexed so we access the value by 
# its key.
# 3-key can not be modified .
# 4-key can not be a list .
 

# so now how to access an item :

print(dec.keys())
print (dec.values())    #or
print(dec["islam"])     #or
print(dec2["hobbies"]["reading"]) #or
allitems= dec2.items()
print(allitems)

# so we can also define a name of a dect as 
# a value of a key of another dect : 

dect3 = {"personal" : dec2 }
print(dect3)

# finally dectionary methods :

# clear :
are= {"R" : "r"}
are.clear()
print(are)

# adding items :
dect3["age"] =  16
print(dect3)
dect3.update({"m" : "M"})
print(dect3)

# copy :
dect4 = dect3.copy()
print(dect4)

# setdefult
dec5 = {"name" : 'abdo'}
dec5.setdefault("name" )
print(dec5)

# popitem
dec5.update({"X" :"x"})
print(dec5.popitem())

# fromkeys

a = "s" , "d" 
b = "d" , "s"
c =  (dec.fromkeys(a,b))
print(c)

# والحمدلله ده كان كل حاجة انهاردة 😊🤲