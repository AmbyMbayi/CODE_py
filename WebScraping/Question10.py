"""write a python code that gets the number of following on a tiwtter account

"""

from bs4 import BeautifulSoup
import requests

handle = input('input your account name on twitter: ')
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text, 'html.parser')

try: 
    following_box = bs.find('li', {'class': 'ProfileNav-item ProfileNav-item--following'})
    following = following_box.find('a').find('span', {'class':'ProfileNav-value'})
    print("{} is following {} people.".format(handle,following.get('data-count')))

except:
    print('Account name not found...')