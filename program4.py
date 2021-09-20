#!/usr/bin/env python3
import time

# Object and Argument references
def f1(x):
    return x

y = 1
z = f1(y)
print(y is z) # True

# Default arguments
def f2(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

f2("helloworld") # ------ \n helloworld \n --------
f2("helloworld",border="*") # ******* \n helloworld \n ********
f2(border=".", message="helloworld") # ...... \n helloworld \n .......
