
def is_leap(year):
    if year % 4 == 0:
     if year % 100 != 0:
          leap = True 
    elif year % 400 == 0:
        leap = True
    else :
        leap = False 
year = int(input( "enter a year"))
print(is_leap(year))

