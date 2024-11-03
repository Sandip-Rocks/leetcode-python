"""
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is like: 
3 + 8 = 11,
1 + 1 = 2. 

Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

"""

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        # Sum the digits by taking the last digit and recursively calling addDigits
        sum_digits = num % 10 + self.addDigits(num // 10)
        return self.addDigits(sum_digits)

if __name__ == "__main__":
    solution = Solution()
    test_num = 38
    result = solution.addDigits(test_num)
    print(f"The result of addDigits({test_num}) is: {result}")