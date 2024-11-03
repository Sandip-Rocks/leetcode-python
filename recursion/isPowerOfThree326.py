"""
326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3^x = (-1).
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)

"""
Explanation:
• Base Case: If n is 1, it returns True since 3^0 = 1.
• Edge Cases: If n is less than or equal to 0, or if n is not divisible by 3, it returns False .
• Recursive Case: The function recursively divides n by 3 until it reaches the base case.
Time and Space Complexity:
• Time Complexity: O(log₃ n) because the input n is divided by 3 in each recursive call.
• Space Complexity: O(log₃ n) due to the recursion stack.
"""