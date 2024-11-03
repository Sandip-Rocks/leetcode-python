"""
645. Set Mismatch

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

"""

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        
        # Cyclic sort to place each number at its correct index
        while i < n:
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                # Swap nums[i] with nums[correct_index]
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        # Find the duplicate and missing numbers
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
        
        return []

solution = Solution()
nums = [1, 2, 2, 4]
result = solution.findErrorNums(nums)
print(result)  # Output: [2, 3]


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""