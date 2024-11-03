"""
941. Valid Mountain Array
https://leetcode.com/problems/valid-mountain-array/description/

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
 

Constraints:

3 <= A.length <= 10000
0 <= A[i] <= 10000
"""

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        start = 0
        
        # Ascending part of the mountain
        while start < n - 1 and arr[start] < arr[start + 1]:
            start += 1
        
        # Check if we didn't move or we are at the last element
        if start == 0 or start == n - 1:
            return False

        # Descending part of the mountain
        while start < n - 1 and arr[start] > arr[start + 1]:
            start += 1

        return start == n - 1  # True if we reached the end
    

# Example of testing the function
if __name__ == "__main__":
    solution = Solution()
    print(solution.validMountainArray([2, 1]))  # Output: False
    print(solution.validMountainArray([3, 5, 5]))  # Output: False
    print(solution.validMountainArray([0, 3, 2, 1]))  # Output: True
    print(solution.validMountainArray([0, 2, 3, 4, 5, 2, 1, 0]))  # Output: True

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""