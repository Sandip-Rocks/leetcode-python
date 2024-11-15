"""
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: Insert all numbers into a hash set
        num_set = set(nums)
        print(num_set)
        longest_streak = 0
        
        # Step 2: Find the start of each sequence
        for num in num_set:
            if num - 1 not in num_set:  # Start of a sequence
                current_num = num
                current_streak = 1

                # Step 3: Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2, 100, 4]
    # nums = [5,4,3,2,1]
    print(solution.longestConsecutive(nums))

"""
Dry Run: Example Input [100, 4, 200, 1, 3, 2]

Insert into Set: {1, 2, 3, 4, 100, 200}
Iterate over each number in the set:
100: No predecessor (99 not in set). Streak = 1.
4: Has predecessor (3 in set). Skip.
200: No predecessor (199 not in set). Streak = 1.
1: No predecessor (0 not in set). Count consecutive numbers:
1 → 2 → 3 → 4 (Streak = 4).
2, 3: Skip (predecessors exist).

Longest streak = 4.
"""

"""
Time Complexity: O(n)
Each element is processed at most twice:
once to check if it's the start of a sequence, and once to expand the sequence.


Space Complexity: O(n)
For the hash set storing the numbers.
"""