"""
46. Permutations
https://leetcode.com/problems/permutations/description/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.func(nums, [], result)
        return result

    def func(self, nums: List[int], path: List[int], result: List[List[int]]):
        if len(path) == len(nums):
            result.append(path.copy())  # Add a copy of the current permutation
            return
        for num in nums:
            if num in path:  # Skip if the number is already in the current permutation
                continue
            path.append(num)  # Add the number to the current permutation
            self.func(nums, path, result)  # Recur to build permutations
            path.pop()  # Backtrack to explore other permutations

# Example of testing the function
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    permutations = solution.permute(nums)
    print(permutations)  # Output: All possible permutations of [1, 2, 3]

"""
Time Complexity: O(n!)
Space Complexity: O(n)
"""