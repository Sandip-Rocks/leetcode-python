"""
## 283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        length = len(nums)
        
        # Move non-zero elements to the front of the array
        for i in range(length):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        
        # Fill the remaining elements with zeroes
        while index < length:
            nums[index] = 0
            index += 1

solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""