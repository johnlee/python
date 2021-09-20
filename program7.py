#!/usr/bin/env python3
from math import factorial
from pprint import pprint as pp

# Interations Iterables

# Comprehensions - lists, sets, dictionaries
cWords = "How do you do today".split()
print([len(cw) for cw in cWords]) # [3, 2, 3, 2, 5]
sFact = {len(str(factorial(x))) for x in range(20)}
print(type(sFact)) # <class 'set'>
print(sFact) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18}
dCountryCapitol = {
    'England':'London',
    'USA':'Washington',
    'South Korea':'Seoul',
    'Sweden':'Stockholm'
}
dCaptiolCountry = {capitol: country for country, capitol in dCountryCapitol.items()}
pp(dCaptiolCountry) # {'London': 'England', 'Seoul': 'South Korea', ...

# Iterator
iterable1 = ['apple','candy','donut']
iterator1 = iter(iterable1)
print(next(iterator1)) # apple
print(next(iterator1)) # candy
print(next(iterator1)) # donut
# print(next(iterator1)) # Exceoption StopIteration

# Generator Functions
def generator1():
    print('yielding to 2')
    yield 2
    print('yielding to 5')
    yield 5
    print('yielding to 8')
    yield 8
g1 = generator1()
print(next(g1)) # yielding to 2
print(next(g1)) # yielding to 5
print(next(g1)) # yielding to 8
# print(next(g1)) # Exception StopIteration

