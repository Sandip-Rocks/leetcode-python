"""
532. K-diff Pairs in an Array

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
nums[i] - nums[j] == k
Notice that |val| denotes the absolute value of val.

 
Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).


Constraints:

1 <= nums.length <= 10^4
-107 <= nums[i] <= 10^7
0 <= k <= 10^7
"""

from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0  # k cannot be negative for k-diff pairs
        
        count = 0
        num_counter = Counter(nums)  # Count occurrences of each number

        if k == 0:
            # For k = 0, count how many numbers have at least 2 occurrences
            for num in num_counter:
                if num_counter[num] > 1:
                    count += 1
        else:
            # For k > 0, check for each number if num + k exists
            for num in num_counter:
                if num + k in num_counter:
                    count += 1
        
        return count

# Example of testing the function
if __name__ == "__main__":
    solution = Solution()
    nums1 = [3, 1, 4, 1, 5]
    k1 = 2
    result1 = solution.findPairs(nums1, k1)
    print(result1)  # Output: 2

    # Edge case test
    nums2 = [1, 1, 1, 1, 1]
    k2 = 0
    result2 = solution.findPairs(nums2, k2)
    print(result2)  # Output: 1
