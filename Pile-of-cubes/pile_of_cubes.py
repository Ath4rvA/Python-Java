#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:30:19 2020

@author: atharva
"""

"""
Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

findNb(1071225) --> 45
findNb(91716553919377) --> -1
"""


def find_nb(m):
    counter = 0
    result = 0
    while True:
        if result == m:
            return counter
        else:
            counter += 1
            result += counter**3
        if result > m:
            return -1


print(find_nb(1071225))
print(find_nb(91716553919377))
print(find_nb(10252519345963644753025))
