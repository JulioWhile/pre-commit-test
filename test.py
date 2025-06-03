import os, sys # E401: multiple imports on one line
import math
import json

def foo( a,  b ):
    c =  1
    d=2
    unused_var = 123
    print('The result is: ',a+b) # E225: missing whitespace around operator

def bar():
    _temp = 42  # allowed, underscore-prefixed
    not_used = 5 # F841: assigned but never used
    print(  "something" ) # bad spacing, single->double quote

foo( 1 ,2)