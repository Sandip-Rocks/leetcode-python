"""
https://www.geeksforgeeks.org/find-whether-an-array-is-subset-of-another-array-set-1/

Given two arrays arr1[] and arr2[] of size m and n respectively,
the task is to determine whether arr2[] is a subset of arr1[].
Both arrays are not sorted, and elements are distinct.

Examples: 

Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1} 
Output: Yes


Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4} 
Output: Yes


Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3} 
Output: No
"""

def is_subset(arr1,arr2):
    hash_map = {}

    for element in arr1:
        hash_map[element] = True
    
    for element in arr2:
        if element not in hash_map:
            return "No"
    return "Yes"

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]
print(is_subset(arr1, arr2))  # Output: Yes

arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [1, 2, 4]
print(is_subset(arr1, arr2))  # Output: Yes

arr1 = [10, 5, 2, 23, 19]
arr2 = [19, 5, 3]
print(is_subset(arr1, arr2))  # Output: No