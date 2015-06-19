from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

base_url = ("http://vancouver.craigslist.ca/search/roo")

soup = BeautifulSoup(urlopen(base_url).read())
posts = soup.find_all("p", "row")
post_urls = [p.a["href"] for p in posts]


for url in post_urls:
    url = url.replace("http://vancouver.craigslist.ca", "")  # inconsistent URL
    page = urlopen("http://vancouver.craigslist.ca{0}".format(url))
    soup = BeautifulSoup(page.read()).find("section", "body")
    address = soup.find_all("div", {"id": "map"})
    print address
