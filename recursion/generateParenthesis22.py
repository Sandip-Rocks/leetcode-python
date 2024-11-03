"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []  # Initialize the list
        self._backtrack(ans, n, 0, 0, "")
        return ans
    
    def _backtrack(self, ans: List[str], n: int, open_count: int, close_count: int, current: str) -> None:
        # Condition to check if the combination is valid
        if open_count == n and close_count == n:
            ans.append(current)  # Add the valid combination to the list
            return
        
        if open_count < n:  # Add an open parenthesis if possible
            self._backtrack(ans, n, open_count + 1, close_count, current + "(")
        
        if close_count < open_count:  # Add a close parenthesis if valid
            self._backtrack(ans, n, open_count, close_count + 1, current + ")")

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 3  # Example input
    result = solution.generateParenthesis(n)
    print(f"Generated parentheses for n={n}: {result}")

"""
Time complexity: O(2^n)
Space complexity: O(2^n)
"""