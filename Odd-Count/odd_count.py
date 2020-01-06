#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:03:18 2020

@author: atharva
"""

"""
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""


def find_it(seq):
    x= set(seq)
    for i in x:
        if seq.count(i) % 2 != 0:
            return i


find_it([1,1,1,2,2])