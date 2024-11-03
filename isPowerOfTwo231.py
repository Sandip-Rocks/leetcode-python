"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 2^0 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 2^4 = 16

Example 3:

Input: n = 3
Output: false

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

solution = Solution()
result = solution.isPowerOfTwo(16)
print(result)  # Output: True

result = solution.isPowerOfTwo(18)
print(result)  # Output: False

"""
Time Complexity: O(1)
Space Complexity: O(1)
"""
