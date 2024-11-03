"""
1688. Count of Matches in Tournament

You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. 
A total of n / 2 matches are played, and n / 2 teams are eliminated.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest get paired. 
A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams are eliminated.
Return the number of matches played in the tournament until a winner is decided.

Example 1:

Input: n = 7
Output: 6
Explanation: Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 3 teams advance to the next round.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance to the next round.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.
Example 2:

Input: n = 14
Output: 13
Explanation: Details of the tournament:
- 1st Round: Teams = 14, Matches = 7, and 7 teams advance to the next round.
- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance to the next round.
- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance to the next round.
- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 7 + 3 + 2 + 1 = 13.
"""

class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        
        while n > 1:
            if n % 2 == 0:
                matches += n // 2
                n //= 2
            else:
                matches += (n - 1) // 2
                n = (n - 1) // 2 + 1
                
        return matches
    
solution = Solution()
result = solution.numberOfMatches(7)
print(result)  # Output: 6

result = solution.numberOfMatches(14)
print(result)  # Output: 13

        
        # Time Complexity: O(log n)
        # Space Complexity: O(1)