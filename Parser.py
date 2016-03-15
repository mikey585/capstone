#! usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request
import urllib.response
import urllib.error

url = 'http://www.nytimes.com/2000/01/01/opinion/l-on-this-first-day-a-fanfare-for-the-new-era-an-asian-century-165670.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)
text = soup.find_all("div", class_="articleBody")

positive = ["freedom", "increase", "reduce"]
negative = ["China"]
score = 0

for i in positive:
    if i in text:
        score += 1

print (score)
