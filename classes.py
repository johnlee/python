#!/usr/bin/env python3
from math import factorial
from pprint import pprint as pp

# Classes

class EmptyClass:
    pass

class Flight:
    """A flight by number and aircraft"""

    def __init__(self, number, aircraft=None): # default argument
        # validate flight number AA####
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}")
        
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")
        
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number

        if not aircraft is None:
            self._aircraft = aircraft # dynamic typing
            rows, seats = self._aircraft.seatingPlan()
            self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
        else:
            self._aircraft = Aircraft("Unknown","Unknown",20,6)
            
        
    def number(self): 
        return self._number

    def aircraftModel(self):
        return self._aircraft.model() # dynamic typing

    def allocateSeat(self, seat, passenger):
        """Allocate seat to passenger"""
        rows, seatletters = self._aircraft.seatingPlan()
        
        letter = seat[-1]
        if letter not in seatletters:
            raise ValueError(f"Invalid seat letter {letter}")
        
        rowtext = seat[:-1]
        try:
            row = int(rowtext)
        except ValueError:
            raise ValueError(f"Invalid seat row {rowtext}")
        
        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger

class Aircraft:

    def __init__(self, registration, model, numRows, numSeatsPerRow):
        self._registration = registration
        self._model = model
        self._numRows = numRows
        self._numSeatsPerRow = numSeatsPerRow

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seatingPlan(self):
        return (range(1, self._numRows + 1), "ABCDEF"[:self._numSeatsPerRow])

class Charter(Aircraft): # inheritance

    def seatingPlan(self):
        return (range(1, self._numRows + 1), "ABCD"[:self._numSeatsPerRow])