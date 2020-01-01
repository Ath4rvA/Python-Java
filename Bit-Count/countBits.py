#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 15:33:27 2020

@author: atharva
"""

"""
Given an integer, convert to binary and count the number of ones
"""

def countBits(n):
    return (bin(n).replace("0b","")).count('1')