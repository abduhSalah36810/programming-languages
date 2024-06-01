

"""Write a Python program to count the occurrences of each word in a given sentence."""


input1= input(str("type a sentnce please  :   "))
dictionary= dict()
words= input1.split()
for word in words : 
   if word in dictionary: 
      dictionary[word]+= 1
   else: 
      dictionary[word]= 1
print(dictionary)