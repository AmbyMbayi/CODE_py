"""write a python program to extract and display all the headers tags from en.wikipedia.org/wiki/Main_Page
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1','h2','h3', 'h4', 'h5', 'h6'])
print('List of all header tags: ', *titles, sep='\n\n')