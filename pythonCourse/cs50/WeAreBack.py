import csv 

titles = {}
 

with  open("username.csv" , "r") as file:

    reader = csv.DictReader(file)
    for row in reader :
         title = row["title"].strip().upper()
         if not title in titles:
            titles[title] = 0
         titles[title] += 1

for title in titles : 
    print[title , titles[title]]

