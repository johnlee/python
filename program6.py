#!/usr/bin/env python3
from exceptional import convert, string_log

# Exceptions
print(convert("one three seven".split())) # Success
print(convert("one three bad".split())) # Fail key error
print(convert(1)) # Fail type error

#print(string_log('blah'))