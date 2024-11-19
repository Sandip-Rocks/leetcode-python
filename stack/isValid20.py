"""
https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

"""
class Solution:
    def isValid(self, s: str) -> bool:
        # Map to match closing brackets with their respective opening brackets
        map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in map:
                # Pop the top element from the stack if available; otherwise, use a dummy value
                top_element = stack.pop() if stack else "#"
                # Check if the popped element matches the corresponding opening bracket
                if map[char] != top_element:
                    return False
            else:
                # Push the opening bracket onto the stack
                stack.append(char)

        # If the stack is empty, all brackets are balanced
        return not stack
    
if __name__ == '__main__':
    solution = Solution()
    s = "()[]{}"
    result = solution.isValid(s)
    print(result)
