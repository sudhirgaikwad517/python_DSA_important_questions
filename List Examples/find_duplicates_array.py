# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 21:30:52 2025

@author: Sudhir Gaikwad
"""

def find_duplicates(arr):
    
    seen = set() #initialing empty set
    duplicates = set() #initslizzing the empty set
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
            
    return list(duplicates)

print(find_duplicates([1,1,2,3,4,4]))