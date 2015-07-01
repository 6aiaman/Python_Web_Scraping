from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

base_url = ("http://vancouver.craigslist.ca/search/apa?s=000")


soup = BeautifulSoup(urlopen(base_url).read())
posts = soup.find_all("p", "row")
post_urls = [p.a["href"] for p in posts]

with open("rent.csv", "w") as f:
    fieldnames = ("lng", "lat", "price", "number of rooms")
    output = csv.writer(f)
    output.writerow(fieldnames)
    for url in post_urls:
        url = url.replace("http://vancouver.craigslist.ca", "")  # inconsistent URL
        page = urlopen("http://vancouver.craigslist.ca{0}".format(url))
        soup = BeautifulSoup(page.read()).find("section", "body")

#description        
        #for hit in soup.find_all(attrs={'class' : 'postingtitletext'}):
        #    description = hit.contents[3].strip()
        #    print description

#address        
        #for hit in soup.find_all(attrs={'class' : 'mapaddress'}):
        #    address = hit.contents[0].strip()
        #    print address

#Lng   
        lng = soup.find_all("div", {"id": "map"})

#Lat   
        lat = soup.find_all("div", {"id": "map"})
        
#price
        for hit in soup.find_all(attrs={'class' : 'price'}):
            price = hit.contents[0].strip()
            print price

#rooms
        for hit in soup.find_all(attrs={'class' : 'housing'}):
            rooms = hit.contents[0].strip()
            print rooms

#white in csv
        output.writerow([lng, lat, price, rooms ])
          
       
