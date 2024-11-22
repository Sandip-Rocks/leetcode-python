"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

Explanation of Examples
Example 1:
s = "())"

( increases balance to 1.
) decreases balance to 0 (matched).
) is unmatched, so add = 1.
Result: add + balance = 1 + 0 = 1.

Example 2:
s = "((("

Each ( increases balance to 3.
No closing ) exists to reduce balance.
Result: add + balance = 0 + 3 = 3.

Example 3:
s = "()"

( increases balance to 1.
) decreases balance to 0 (matched).
Result: add + balance = 0 + 0 = 0.

Example 4:
s = "()))(("

( increases balance to 1.
Each ) reduces balance, but when balance = 0, extra ) increases add to 2.
( adds unmatched balance of 2.
Result: add + balance = 2 + 2 = 4.

"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        add = 0

        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                if balance > 0:
                    balance -= 1
                else:
                    add += 1
        return add + balance
    
if __name__ == '__main__':
    solution = Solution()
    # s = "())"         # Output: 1
    s = "((("           # Output: 3
    result = solution.minAddToMakeValid(s)
    print(result)
