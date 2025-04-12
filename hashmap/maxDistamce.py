"""
https://www.geeksforgeeks.org/maximum-distance-two-occurrences-element-array/

Given an array arr[], the task is to find the maximum distance between two occurrences of any element. If no element occurs twice, return 0.
Input: arr = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is: 4-2 = 2, So max distance is 5.


Input : arr[] = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Output: 10
Explanation : Max distance for 2 is 11-1 = 10, max distance for 1 is 4-2 = 2 and max distance for 4 is 10-5 = 5  


Input: arr[] = [1, 2, 3, 6, 5, 4]
Output: 0
Explanation: No element has two occurrence, so maximum distance = 0.
"""
from typing import List
def maxDistance(arr: List) -> int:
    hash_map = {}
    result = 0
    size = len(arr)

    for i in range(size):
        if arr[i] not in hash_map:
            hash_map[arr[i]] = i
        else:
            result = max(result, i - hash_map[arr[i]])
    return result

arr = [1, 1, 2, 2, 2, 1]

sol = maxDistance(arr)
print(sol)