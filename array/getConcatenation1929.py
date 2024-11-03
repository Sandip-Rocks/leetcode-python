"""
1929. Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)  # Initialize the result list with double the size

        for i in range(n):
            ans[i] = nums[i]          # Copy elements from nums
            ans[i + n] = nums[i]      # Concatenate the same elements
        
        return ans

solution = Solution()
result = solution.getConcatenation([1, 2, 1])
print(result)  # Output: [1, 2, 1, 1, 2, 1]

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""