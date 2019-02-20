"""write a python program to get the number of post on twitter liked by a given account
"""
from bs4 import BeautifulSoup
import requests

handle = input('input your twitter account name: ')
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text, 'html.parser')

try:
    favorite_box = bs.find('li', {'class': 'ProfileNav-item ProfileNav-item--favorites'})
    favorite = favorite_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("Number of post {} liked are {} : ". format(handle,favorite.get('data-count')))

except:
    print('account name cannot be found...')