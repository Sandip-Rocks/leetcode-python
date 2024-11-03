"""
1281. Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:

Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_digits = 1
        sum_of_digits = 0
        
        while n > 0:
            digit = n % 10
            product_of_digits *= digit
            sum_of_digits += digit
            n //= 10  # Use integer division
            
        return product_of_digits - sum_of_digits

solution = Solution()
result = solution.subtractProductAndSum(234)
print(result)  # Output: 15 (Product: 24, Sum: 9, Difference: 15)

result = solution.subtractProductAndSum(4421)
print(result)  # Output: 21 (Product: 32, Sum: 10, Difference: 22)
