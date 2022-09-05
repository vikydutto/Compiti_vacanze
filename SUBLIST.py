"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.

SUBLIST = 1
SUPERLIST = 10
EQUAL = 20
UNEQUAL = 30

def sublist(list_one, list_two):
    len1 = len(list_one)
    len2 = len(list_two)
    
    if len1 > 0 and len2 == 0:
        return SUPERLIST
        
    if len1 == 0 and len2 > 0:
        return SUBLIST
        
    if list_one == list_two:
        return EQUAL
        
    if len1 < len2:
        for i in range(0, len2 - len1 + 1):
            if list_one == list_two[i:i + len1]:
                return SUBLIST
                
    if len1 > len2:
        for i in range(0, len1 - len2 + 1):
            if list_two == list_one[i:i + len2]:
                return SUPERLIST
    return UNEQUAL

