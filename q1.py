# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:03:34 2024

@author: User
"""

def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap values
    x, y = y, x
    return x,y


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
swap("Apple", 10)
swap(9, 17)