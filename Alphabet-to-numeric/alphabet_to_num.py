#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:41:06 2020

@author: atharva
"""

"""Replace With Alphabet Position

Given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.
"""

def alpha_to_num(string_input):
    result=[]
    string_input= string_input.lower()
    alpha_num_dict= dict(zip([chr(i) for i in range(97,123)],[i for i in range(1,27)]))
    for alphabet in string_input:
        if alphabet in [chr(i) for i in range(97,123)]:
            result.append(alpha_num_dict[alphabet])
        else:
            continue
    return ' '.join([str(elem) for elem in result])
    
print(alpha_to_num("The sunset sets at twelve o' clock."))