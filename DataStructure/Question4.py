"""write a python program to get all values from an enum class

Expected output
[92,23,42,539,34,53]

"""
from enum import IntEnum
class City(IntEnum):
    Kisumu = 45
    Nairobi = 67
    Alego = 56
    Usenge =4
city_code_list = list(map(int, City))
print(city_code_list)