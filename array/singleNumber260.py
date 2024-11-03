"""
260. Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
"""

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        y = 0
        xor = 0
        
        # Step 1: Compute the XOR of all numbers
        for num in nums:
            xor ^= num
            
        # Step 2: Get the rightmost set bit
        last_set_bit = xor & -xor
        
        # Step 3: Divide numbers into two groups and find the two unique numbers
        for num in nums:
            if num & last_set_bit == 0:
                x ^= num
            else:
                y ^= num
                
        return [x, y]


solution = Solution()
nums = [1, 2, 1, 3, 2, 5]
result = solution.singleNumber(nums)
print(result)  # Output: [3, 5] or [5, 3] (order may vary)

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""