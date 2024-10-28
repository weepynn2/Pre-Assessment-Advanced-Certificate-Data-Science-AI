# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:47:37 2024

@author: User
"""

def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    return s[::-1]
    
# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
string_reverse("Hello World")
string_reverse("Python") 
