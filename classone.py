#ClassOne.py

class Calculator(object):

    #define class to simulate a simple calculator

    def __init__ (self):

        #start with zero

        self.current = 4

    def add(self, amount):

        #add number to current

        self.current += amount

    def getCurrent(self):

        return self.current