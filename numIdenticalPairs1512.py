"""
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

"""
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        count = {}
        
        # Count occurrences of each number
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Calculate the number of good pairs using the counts
        for freq in count.values():
            good_pairs += (freq * (freq - 1)) // 2
            
        return good_pairs

solution = Solution()
nums = [1, 2, 3, 1, 1, 3]
result = solution.numIdenticalPairs(nums)
print(result)  # Output: 4

nums = [1, 1, 1, 1]
result = solution.numIdenticalPairs(nums)
print(result)  # Output: 6

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""