# waht is a list looks like :

list = ["waht ? " , 1 , 1.5 , 5+4j ,  True , (5, 6)  ]
print (f"list can have all types of data look! {list})")
print(list[:3:2])
list[0:3] = ["what" , 2 , 2.4]
print (list)

#now we are going to show you list methods :

list2 = ["mohammed" , 3 , 'marwan' , 4]

#appending
list2.append(5)
print(list2)
list3 = ['hi','bye']
list2.append(list3)
print(list2[5][1])

#extending
(list2.extend(list3))
print(list2)

#remove
list2.remove('mohammed')
print(list2)

#sort
list4 = [120 , 213, -212 , 10]
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)

#reverse
z= ['i', 'e' , '100']
z.reverse()
print(z)

#clear
x = [1,2]
x.clear()
print(x)

#copy
x= z.copy()
print(x)

#count
print(x.count(1))

#index 
y = [3, 4]
print(y.index(3))

#insert 
e =[4,6,7]
e.insert(1,4)
print(e)

#pop
print(e.pop(2))

# and that was all u need to know about list