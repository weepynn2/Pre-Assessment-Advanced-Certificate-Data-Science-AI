# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:25:44 2024

@author: User
"""
def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:    
        print(f"{dct[key]}")
        dct[key] = value
    else:
        dct = {key: value}
    
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
update_dictionary({}, "name", "Alice")
update_dictionary({"age": 25}, "age", 26)