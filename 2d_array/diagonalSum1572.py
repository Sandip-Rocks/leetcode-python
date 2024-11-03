"""
1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
"""
from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total_sum = 0
        
        for i in range(n):
            total_sum += mat[i][i]  # Sum for the primary diagonal
            total_sum += mat[i][n - 1 - i]  # Sum for the secondary diagonal
            
        # If the matrix has odd length, subtract the middle element (counted twice)
        if n % 2 == 1:
            total_sum -= mat[n // 2][n // 2]
        
        return total_sum

solution = Solution()
result = solution.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)  # Output: 25 (1 + 5 + 9 + 3 + 7 = 25)

result = solution.diagonalSum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
print(result)  # Output: 8 (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 8)

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""