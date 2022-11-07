#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:28:27 2022
@author: MargheritaP
"""
# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#
def triple(x):
    y = x*3
    return print(y)

#test if function works
triple(4)

# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def subtract(x,y):
    return x-y

#test if function works
subtract(12,8)


# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}

def dictionary_maker(a):  #a should be a list of 2-tuples
    d = dict((k, l) for k, l in a)
    return print(d)

#test if function works
dictionary_maker([(1,"a"),(2,"b"),(3,"c")])
