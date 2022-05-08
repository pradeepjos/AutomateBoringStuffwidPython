# all python program can call a basic set of functions called the built in functions
# print(), len(), round(), abs(), input()
# python also comes with a set of modules called the standard library.. each module contains a group of python programs that can be used.
# you will need to first import the module.

# random module to generate random numbers

from copy import copy
import random as rd
print(rd.randint(1,10))


# we can also include specific functions in the module
from random import * # * means import all the functions
print(randint(1,10)) # no need to mention random.randint()

# more modules sys, os, math
from sys import *
print("hello")
#exit() # uncomment this while running
print("Goodbye")

# third party modules pyperclip --like clipboard copy and past
#from pyperclip import *
#copy("Hello there how are you")
#paste()


## Summary
#   You can import modules and get access to new functions 
# the modules that come with pythin are called standard library, but you can also install thid-party modules using the pip tool
# the sys.exit() function will immediately quit your program
# The pyperclip third-party module has copy() and paste () functions for reading and writing text to the clipboard.
