"""
154. Find Minimum in Rotated Sorted Array II

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[high]:
                high -= 1  # Reduce the search range if nums[mid] == nums[high]
            elif nums[mid] > nums[high]:
                low = mid + 1  # Minimum is in the right half
            else:
                high = mid  # Minimum is in the left half including mid

        return nums[low]

solution = Solution()
result = solution.findMin([3, 4, 5, 1, 2])
print(result)  # Output: 1

result = solution.findMin([2, 2, 2, 0, 1])
print(result)  # Output: 0

"""
Time Complexity: O(log n)
Space Complexity: O(1)

"""