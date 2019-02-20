"""write a python program that retrieves an arbitrary wikipedia pages of pyathon and creates a list od links on that page
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Python')
bsObj = BeautifulSoup(html)

for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])