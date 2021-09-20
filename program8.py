#!/usr/bin/env python3
from math import atan2, factorial
from pprint import pprint as pp
from classes import Aircraft, Charter, Flight

# Classes
f1 = Flight("SN100")
print(f1.number())
print(f1._number) # no access modifiers

#f2 = Flight("FAIL") # ValueError: Invalid route number 'FAIL'

a1 = Aircraft("G-ERO", "Boeing 737", 22, 6)
print(a1.model()) # Boeing 737
print(a1.seatingPlan()) # (range(1, 23), 'ABCDEF')

f3 = Flight("AF222", a1)
print(f3.aircraftModel()) # Boeing 737
pp(f3._seating) # [None, {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}, ...
pp(f3.allocateSeat("12A","John"))
#pp(f3.allocateSeat("12A","Jane")) # ValueError: Seat 12A already occupied
#pp(f3.allocateSeat("12J","Jane")) # ValueError: Invalid seat letter J
#pp(f3.allocateSeat("99A","Jane")) # ValueError: Invalid row number 99
pp(f3.allocateSeat("15F","Jack"))

a2 = Charter("CH-US", "Charter 1000", 10, 4)
f4 = Flight("CH100", a2)
pp(f4.aircraftModel())
pp(f4.allocateSeat("1A","John"))
pp(f4._seating) # [None, {'A': 'John', 'B': None, 'C': None, 'D': None}, ...
#pp(f4.allocateSeat("20A","Jane")) # ValueError: Invalid row number 20
