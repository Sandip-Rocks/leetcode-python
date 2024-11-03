"""
287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        
        # Cyclic sort to place each number in its correct position
        while i < n:
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                # Swap nums[i] with nums[correct_index]
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        # Find the duplicate number
        for i in range(n):
            if nums[i] != i + 1:
                return nums[i]
        
        return -1

solution = Solution()
nums = [3, 1, 3, 4, 2]
result = solution.findDuplicate(nums)
print(result)  # Output: 3

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""