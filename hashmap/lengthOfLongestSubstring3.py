"""

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

https://www.youtube.com/watch?v=FCbOzdHKW18

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        hash_set = set()
        n = len(s)

        for r in range(n):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
            
            w = (r - l) + 1
            longest = max(longest,w)
            hash_set.add(s[r])

        return longest
        # Time: O(n)
        # Space: O(n)

s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
sol = Solution()
result = sol.lengthOfLongestSubstring(s)
print(result)