"""
485. Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current_consecutive = 0
        
        for num in nums:
            if num == 1:
                current_consecutive += 1
                max_consecutive = max(max_consecutive, current_consecutive)
            else:
                current_consecutive = 0
        
        return max_consecutive

solution = Solution()
result = solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
print(result)  # Output: 3

result = solution.findMaxConsecutiveOnes([0, 0, 0, 0])
print(result)  # Output: 0


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""