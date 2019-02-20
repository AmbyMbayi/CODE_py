"""write a python program to create an Enum object and display a member name and
value.
Sample data:
Kisumu = 45
Nairobi = 67
Alego = 56
Usenge =45

Expected output:
Member name: Usenge
Member Value: 45

"""
from enum import Enum

class City(Enum):
    Kisumu = 45
    Nairobi = 67
    Alego = 56
    Usenge =45

print('\n Member name: {}'.format(City.Alego.name))
print('\nMember Value: {}'.format(City.Alego.value))