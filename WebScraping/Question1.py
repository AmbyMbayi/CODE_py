"""write a python program to test if a given page is found or not on the server
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("http://abcxyz.com")
except HTTPError as e:
    print("Http error")
except URLError as e:
    print("server not found")
else:
    print(html.read())

try:
    html= urlopen("http://www.google.com/")
except HTTPError as e:
    print("Http error")

except URLError as e:
    print("server not found")
else:
    print("Html details")
    print(html.read())

