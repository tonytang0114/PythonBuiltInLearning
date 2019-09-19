# Sort a list of words by length
def SortAListOfWords(words):
    sorted(words, key=len)

# 'testing' --> 'gnitset'
def reverse(word):
    return word[::-1]

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=reverse)) # sorted a list of words by their reversed spelling
print(sorted(fruits, key=lambda word: word[::-1]))
def factorial(n):
    """return n!"""
    return 1 if n < 2 else n*factorial(n-1)

# map, filter, reduce
print(list(map(factorial,range(6))))
print([factorial(n) for n in range(6)])
print(list(map(factorial, filter(lambda n: n%2, range(6)))))
print([factorial(n) for n in range(6) if n%2])

# Reduce
from functools import reduce
from operator import add
from datetime import datetime


print(reduce(add, range(100)))
print(sum(range(100)))


