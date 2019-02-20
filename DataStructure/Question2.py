"""writer a python program to iterate over an enum class and
display individual members and their vvalue.

Expected output:

Kisumu = 45
Nairobi = 67
Alego = 56
Usenge =45

"""
from enum import Enum
class City(Enum):
    Kisumu = 45
    Nairobi = 67
    Alego = 56
    Usenge =45

for city in City:
    print('{:10}= {}'.format(city.name, city.value))