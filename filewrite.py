#!/usr/bin/python

try:
    f = open("test.txt", "w")
    f.write("asdf is a test")

except IOError:
   print ( "Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")