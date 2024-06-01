# LET'S BE AWESOME AND PLAY WITH TIME 🕰

from datetime import*

s = "," 
yourbirthday = int(input("enter your birth day : "))
yourbithmoths = int(input("enter your birth month :"))
yourbithyear = int(input("enter your birth year : "))
borndate= datetime(yourbithyear,yourbithmoths,yourbirthday)
bornday= borndate.strftime("%A")
print(f" you was born in {bornday}")
