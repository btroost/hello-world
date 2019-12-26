#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
#import cgitb
#cgitb.enable()

print ("Content-type: text/html\n\n")

#print("Content-Type: text/plain;charset=utf-8")
#print()

print("Hello World!")
print("<button type=""button"" onclick=""document.getElementById('demo').innerHTML = Date()"">Click me to display Date and Time.</button>")
  #<button type="button" onclick="document.getElementById('demo').innerHTML = Date()">Click me to display Date and Time.</button>

print("<p id=""demo"">xx</p>")
  
