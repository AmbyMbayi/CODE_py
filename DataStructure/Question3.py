"""write a program that displays all member nam of en enum cla ordered by their values

expected output:
city ordered by city code


Alego
Kisumu
Nairobi
Usenge 
"""

import enum
class City(enum.IntEnum):
    Kisumu = 45
    Nairobi = 67
    Alego = 56
    Usenge =4

print('city name ordered by city code')
print('\n'.join(' '+ c.name for c in sorted(City)))