"""
### 448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

"""
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
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

        # Find all missing numbers
        result = []
        for j in range(n):
            if nums[j] != j + 1:
                result.append(j + 1)
        
        return result

solution = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
result = solution.findDisappearedNumbers(nums)
print(result)  # Output: [5, 6]


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""