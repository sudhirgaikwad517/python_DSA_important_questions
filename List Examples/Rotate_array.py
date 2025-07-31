# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 22:05:29 2025

@author: Sudhir Gaikwad
"""

def rotate_array(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

# Example:
print(rotate_array([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
