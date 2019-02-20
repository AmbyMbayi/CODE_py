"""write a python code that count number of tweets by a given twitter account
"""

from bs4 import BeautifulSoup
import requests

handle = input('Input account name on twitter: ')
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text, 'html.parser')

try:
    tweet_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--tweets is-active'})
    tweets = tweet_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("{} tweets {} number of tweets.".format(handle, tweets.get('data-count')))

except:
    print('account name not found...')
