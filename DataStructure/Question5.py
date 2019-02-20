"""write a python program to count the most common words in a dictionary

Expected output
[('pink',6),('black',5), ('white',5),('red', 4)]

"""
word = ['red','yellow','black','black','black','black','pink','white', 'red', 'red', 'red', 'red', 'red']

from collections import Counter

word_counts = Counter(word)
top_four = word_counts.most_common(5)
print(top_four)