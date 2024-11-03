"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low, mid, high = 0, 0, n - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]  # Swap nums[low] and nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]  # Swap nums[mid] and nums[high]
                high -= 1

# Example of testing the function
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    print(nums)  # Output: [0, 0, 1, 1, 2, 2]

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""