
# importing important modules

from importlib.resources import path
from msilib.schema import tables
from pickle import NONE, TRUE
import requests 
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

MovieNames = []
MovieRating = []
Links = []
forbden = ["المدة" , "الترجمة", "التقييم" , "النوع", "الجودة", "التصنيف", "اللغة • البلد"]
duration=[]
page_num=1

# getting the main page

while page_num <= 23:

    page_counter = "https://seen.egybest.vin/movies/top?page="+str(page_num)
    main_page = requests.get(page_counter)

    # getting the maing page content
    page_content = main_page.content

    # creating a soup object to handle page content
    soup = BeautifulSoup(page_content , "lxml") 

    # we are collecting the (movie name , the rate )
    movies_names = soup.find_all("span" , {"class" : "title"}) 
    movies_ratings = soup.find_all("i" , {"class":"i-fav rating"})
    movies_links = soup.find_all("a" , {"class":"movie"})
   
    # extracting the text 
    for i in range(len(movies_names)):
        MovieNames.append(movies_names[i].text) 
        MovieRating.append(movies_ratings[i].text)
        Links.append(movies_links[i].attrs['href']) 
        
    page_num +=1
    print(f"page {page_num}")

#looping throw each page like 

for link in Links:
    movie_page = requests.get(link)
    movie_content = movie_page.content
    soup1 = BeautifulSoup(movie_content , "lxml")
    # looping throw the table to fet the duration. 
    movies_tables = soup1.find("div", {"class":"td vat"})
    table = movies_tables.find('table')
    for row in table.find_all('tr'):
      for data in row.find_all('td'):
         if (data.string) not in forbden and (data.string) != None:
              duration.append(data.string)
                        
# isializing the csv file 
file_list = [MovieNames,MovieRating,duration,Links]
exported = zip_longest(*file_list)
with open("EgyBest1.csv" , "w", encoding="utf-8", errors='ignore') as file :
    wr = csv.writer(file)
    wr.writerow(["Movie Name" , "Rating" ,"Duration" , "Link"])
    wr.writerows(exported)


      