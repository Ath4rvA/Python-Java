#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:42:59 2020

@author: atharva
"""

"""Translate morse to text and vice-versa
"""


morse_code = {'A': '.-',     'B': '-...',   'C': '-.-.',  
   'D': '-..',    'E': '.',      'F': '..-.', 
   'G': '--.',    'H': '....',   'I': '..', 
   'J': '.---',   'K': '-.-',    'L': '.-..', 
   'M': '--',     'N': '-.',     'O': '---', 
   'P': '.--.',   'Q': '--.-',   'R': '.-.', 
   'S': '...',    'T': '-',      'U': '..-', 
   'V': '...-',   'W': '.--',    'X': '-..-', 
   'Y': '-.--',   'Z': '--..',   '0': '-----',
   '1': '.----',  '2': '..---',  '3': '...--',  
   '4': '....-',  '5': '.....',  '6': '-....',  
   '7': '--...',  '8': '---..',  '9': '----.'  
   }

reverse_morse_code={value:key for key,value in morse_code.items()}            

def text_to_morse(text): 
   text= text.upper() 
   alphabets= list(text) 
   result="" 
   for element in alphabets: 
       if element.isalpha(): 
           result+= morse_code[element]
           result+=" "
       elif element in [str(i) for i in range(0,10)]: 
           result+= morse_code[element] 
       elif element==" ":
           result+="  "
       else: 
           result+=element 
   return result

def morse_to_text(morse):
    result=""
    new_text= morse.split("  ")
    for text in new_text:
        words= text.split(" ")
        for word in words:
            if word=='':
                result+=" "
            try:
                result+=reverse_morse_code[word]
                
            except:
                print(word)
    return result

inp=text_to_morse("Atharva is a good boy")
res= morse_to_text(inp)
print("Input: ",inp)
print("Output: ", res)
