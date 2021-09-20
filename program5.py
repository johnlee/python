#!/usr/bin/env python3
import math
from typing import List

# Tuples
t = ("abc", 4.9, 3)
t += (3231, 353e5)
t += ((123,455),(333),444)
print(t) # ('abc', 4.9, 3, 3231, 35300000.0, (123, 455), 333, 444)

# single tuple
st1 = ("abc")
print(st1)
print(type(st1)) # <class 'str'>
st2 = ("abc",)
print(st2)
print(type(st2)) # <class 'tuple'>

# unpacking tuples
lower, upper = (1,(3,4))
print(lower) # 1
print(upper) # (3,4)

# Strings
str1 = ','.join(['a','b','c'])
print(str1) # a,b,c
str2 = ''.join(['a','b','c'])
print(str2) # abc

# String partitions
origin, _, destination = "Seattle-Boston".partition('-')
print(origin) # Seattle
print(destination) # Boston

# String formatting
print("Values are {} and {}".format('val1', 2)) # Values are val1 and 2
print("Values are x={vals[0]} and y={vals[1]}".format(vals=(1,2))) # Values are x=1 and y=2
vals2 = (1, (3,4))
print("Values are {v[0]} and {v[1]}".format(v=vals2)) # Values are 1 and (3, 4)

# Literal String Interpolation, f-strings
print(f'Values are {vals2[0]} and {vals2[1]}') # Values are 1 and (3, 4)
print(f'Values are {math.pi:.3f} and {math.e:.3f}') # Values are 3.142 and 2.718

# Ranges = range(start, stop, step)
for i in range(5,10): print(i) # 5 6 7 8 9
print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8]

# enumerate
tuple2 = [1,'b',3,'d',5]
for i, v in enumerate(tuple2):
    print(f"i={i}, v={v}") # i=0, v=1 ...

# Lists, Slice and Copy
list1 = [1,2,3,4]
print(f"last={list1[-1]} 2ndlast={list1[-2]} first={list1[0]} firstzero={list1[-0]}") # last=4 2ndlast=3 first=1 firstzero=1
list2 = [5, 6, 'h', 'i', 'j', 9]
print(list2[1:3]) # [6, 'h']
print(list2[:3]) # [5, 6, 'h'] 
print(list2[:]) # [5, 6, 'h', 'i', 'j', 9]
list2c = list2.copy() # shallow copy
list2d = list(list2) # shallow copy
list2e = list2[:] # new list object but values all point to same memory reference
print(f'2c={list2 is list2c} 2d={list2 is list2d} 2e={list2 is list2e}') # False but 2c 2d copies not referencing same memory values
# Shallow copies
l1 = [[1,2],['a','b']]
l2 = l1.copy()
print(l1[0] is l2[0]) # True both are pointing to same memory
l1[0].append(3)
print(f'l1={l1}, l2={l2}') # l1=[[1, 2, 0], ['a', 'b']], l2=[[1, 2, 0], ['a', 'b']] # l2 references l1
print(list2.index('h')) # will throw error if not found


# Dictionaries
dict1 = {'name': 'john', 'id': 12345, 'location':'denver'}
dict2 = dict(name='john',id=12345,location='denver')
dict3 = dict1.copy() # shallow copy
print(dict1 == dict2) # True
dict3.update({'name':'jane','age':12})
print(dict1) # {'name': 'john', 'id': 12345, 'location': 'denver'}
print(dict3) # {'name': 'jane', 'id': 12345, 'location': 'denver', 'age': 12}
for dictKey, dictValue in dict3.items():
    print(f'{dictKey}={dictValue}') # name=jane
print('name' in dict3) # True
print('jane' in dict3) # False

from pprint import pprint as pp
pp(dict3) # {'age': 12, 'id': 12345, 'location': 'denver', 'name': 'jane'}


# Sets
set1 = {'adam','bob','chuck','don','ellie'}
set2 = {'bob','frank'}
set3 = {'chuck','don','ellie','frank','sam'}
set4 = {'adam','bob','chuck','ralph'}
print(set1.union(set2)) # {'bob', 'don', 'adam', 'chuck', 'frank', 'ellie'}
print(set1.intersection(set3)) # {'chuck', 'don', 'ellie'}
print(set1.difference(set3)) # {'bob', 'adam'}
print(set1.symmetric_difference(set4)) # {'don', 'ralph', 'ellie'}
print(set2.issubset(set1)) # False
print(set2.isdisjoint(set3)) # False


# Protocols

