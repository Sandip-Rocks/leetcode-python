"""
## 53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

"""

from typing import List

class Solution:
    def maxSubArray(self, nums):
        """
        This method takes a list of integers as input and returns the maximum sum of a contiguous subarray.
        
        The algorithm uses a dynamic programming approach, keeping track of the maximum sum seen so far and the current sum.
        It iterates through the list, updating the current sum and maximum sum as it goes.
        """
        
        # Initialize the maximum sum and current sum to the first element of the list
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Iterate through the rest of the list
        for i in range(1, len(nums)):
            # Update the current sum to be the maximum of the current element and the sum of the current element and the previous current sum
            current_sum = max(nums[i], nums[i] + current_sum)
            
            # Update the maximum sum to be the maximum of the current maximum sum and the current sum
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum sum
        return max_sum

# Create an instance of the Solution class
solution = Solution()

# Define a list of integers to test the method
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Call the maxSubArray method and print the result
result = solution.maxSubArray(nums)
print(result)

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""