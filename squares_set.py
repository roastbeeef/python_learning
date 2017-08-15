#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 17:29:57 2017
In a similar way to building an empty list with my_list = [], 
you can create an empty set with my_set = set(). Using this technique, 
and the add method, build a set of all of the square numbers greater than 0 and less than 2,000. 
For reference, I included my implementation of nearest_square function from an earlier quiz. 
You may call the function in your code, integrate it into your code, or ignore it altogether.
@author: matt
"""



squares = set()

# todo: populate "squares" with the set of all of the integers less 
# than 2000 that are square numbers


# Note: If you want to call the nearest_square function, you must define
# the function on a line before you call it. Feel free to move this code up!
def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2


        
# =============================================================================
# build a function that starts with an empty set and fills it up with square numbers until you hit 2000
# 1) build function    
# 2) build empty set
# =============================================================================

def square_set(limit):
    squares = set()
    counter = 0
    while (counter+1)**2 < limit:
        counter += 1
        squares.add(counter**2)
    return(squares)
    
    
# solution - this way the function does not have to iterate through the loop 2000 times.
# it is simply a while loop   
n = 1
while n**2 < 2000:
    squares.add(n**2)
    n += 1