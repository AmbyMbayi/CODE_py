"""write a python program to extract h1 from example.com
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.example.com/')
bsh = BeautifulSoup(html.read(), 'html.parser')
print(bsh.p)
print(bsh.h1)