# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 22:20:49 2025

@author: Sudhir Gaikwad
"""

# find missing number

def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example:
print(find_missing_number([1, 2, 3, 5, 6], 6))
