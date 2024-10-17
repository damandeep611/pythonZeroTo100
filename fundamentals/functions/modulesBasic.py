# a module is simply a file that contains functions, classes and variables that other programs can use easily by just using import function 

# it provides reuseability , better organization

# example 

import moduleExample

moduleExample.hello("red john")

moduleExample.flash("Reset timeline story starts ")
# this moduleExample is a file that we have made to store a function that we may want to use over and over again in our program, and .hello is a funcition that is inside that file, and the main function due to which we made moduleExample.py file so that we don't clutter our current code and use external local defined funciton to maintain clean structure and easy to manage codebase

# there are basically three types of modules 
# 1- built in , within python, 2- third party - imported/installed using pip. 3.- user defined - the one we just used now - moduleExmple.py 

#? ---------- built in imports 
import math

# to import all math modules we can also import math in this way 
from math import *

print(math.pi)
print(math.sqrt(25))

# date time module 
from datetime import datetime

current_time = datetime.now()
print(current_time)



