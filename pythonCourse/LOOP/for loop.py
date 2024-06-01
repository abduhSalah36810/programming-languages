"""today's lesoon is about loops"""

""" basiclly what we use loop when we want to 
loop through data type to do spcifice operations 
on each item or a group of them . """


# how do we write a loop  : 
# for (item) in (items) :
#   ( a block of code ) .

#example to find number 2 in a list if it exists 
#we will print it if not we print (not around 😁):

def find_number (numbers) :

    for number in numbers :
        if number == 2 :
            print(f"i got the {number}")
        else :
            ("not around 😁")

    

print(find_number([1, 2 ,3, 4]))


# looping through a dictionary  :

sports = {"football": 1, 
         "Cricket" : 2, 
         "Hockey" : 3 , 
         "Tennis" : 4  } 
for sport in sports : 
    print(f'{sport } is the sport number {sports.get(sport)} in the world ')


# nestes loop : 
"""let's take the dictionary to another level
   to explain nested by nested  🤷‍♂️😁"""

sports_pro ={"football":{"rate" : 1 , 
            "Estimated Fans": " 3.5 Billion" } ,
         "Cricket" :{"rate" : 2 ,
            "Estimated Fans": "	2.5 Billion" },
         "Hockey" :{ "rate" : 3 ,
            "Estimated Fans" : " 2.2 Billion"},
         "Tennis" :{"rate" : 4, 
            "Estimated Fans": " 2 Billion" }
             }


print("Most popular sports in the world : ")
for sport in sports_pro :   
    print(f"the {sport} is : ")
    for thing in sports_pro[sport] :
      print(f"{thing} => {sports_pro[sport][thing]}" )


"""let me tell you that there is a better
and easiear way to do  nested looping
throught nested dectionary  🤷‍♂️"""   

# the other way :
  

for main_sport , main_props in sports_pro.items() : 
  print(f"{main_sport} is : ") 
  for main_key , main_valus in main_props.items() :
    print(f'{main_key} => ({main_valus})')

# that's it 🤷‍♂️

