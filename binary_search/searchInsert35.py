"""
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

 

Constraints:

1 <= nums.length <= 10^4
-104 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low

solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))  # Output: 2
print(solution.searchInsert([1, 3, 5, 6], 2))  # Output: 1
print(solution.searchInsert([1, 3, 5, 6], 7))  # Output: 4
print(solution.searchInsert([1, 3, 5, 6], 0))  # Output: 0


"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""