#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 08:46:48 2020

@author: atharva
"""

"""
In 10 mins you have to check if your starting and ending position is same.
Each step accounts for 1 min.
"""


def is_valid_walk(walk):
    #determine if walk is valid
    counter=0
    dir_dict={'n':1, 's':-1, 'w':2, 'e':-2}
    if len(walk)!=10:
        return False
    else:
        for direction in walk:
            counter+= dir_dict.get(direction)
    if counter==0:
        return True
    else:
        return False

is_valid_walk(['n','s','n','s','w','w','e','e','s','n'])