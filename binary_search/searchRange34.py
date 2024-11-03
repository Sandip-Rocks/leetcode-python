"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

from typing import List

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        result[0] = self.findFirstOccurrence(nums, target)
        result[1] = self.findLastOccurrence(nums, target)
        return result

    def findFirstOccurrence(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                ans = mid
                high = mid - 1  # Narrow down to the left side
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def findLastOccurrence(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                ans = mid
                low = mid + 1  # Narrow down to the right side
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans
