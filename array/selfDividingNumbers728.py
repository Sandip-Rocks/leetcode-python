"""
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

Example 1:

Input: left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]

"""

from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_numbers = []
        
        for i in range(left, right + 1):
            n = i
            is_self_dividing = True
            
            while n > 0:
                r = n % 10
                if r == 0 or i % r != 0:
                    is_self_dividing = False
                    break
                n //= 10  # Use integer division
            
            if is_self_dividing:
                self_dividing_numbers.append(i)
        
        return self_dividing_numbers

solution = Solution()
result = solution.selfDividingNumbers(1, 22)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""