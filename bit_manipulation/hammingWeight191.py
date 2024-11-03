"""
191. Number of 1 Bits

Given a positive integer n, write a function that returns the number of 
set bits in its binary representation (also known as the Hamming weight).
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            n &= (n - 1)  # Clear the least significant 1-bit
            ans += 1
        return ans

solution = Solution()
result = solution.hammingWeight(11)  # Binary representation of 11 is 1011
print(result)  # Output: 3

result = solution.hammingWeight(128)  # Binary representation of 128 is 10000000
print(result)  # Output: 1


"""
Time Complexity: O(1)
Space Complexity: O(1)
"""