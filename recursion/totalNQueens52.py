"""
52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.sol = 0  # Variable to count the number of solutions
        board = [[False] * n for _ in range(n)]  # Board to track queens' positions
        self._placeQueens(board, n, 0)  # Start recursion from row 0
        return self.sol  # Return the number of solutions
    
    def _isValid(self, board: list, n: int, row: int, col: int) -> bool:
        # Check the column above
        for i in range(row):
            if board[i][col]:
                return False
        
        # Check upper-left diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j]:
                return False
        
        # Check upper-right diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j]:
                return False
        
        return True  # It's valid to place the queen here

    def _placeQueens(self, board: list, n: int, row: int) -> None:
        if row == n:  # If all queens are placed
            self.sol += 1  # Increment solution count
            return
        
        # Try placing a queen in each column of the current row
        for col in range(n):
            if self._isValid(board, n, row, col):  # Check if placing queen at (row, col) is valid
                board[row][col] = True  # Place the queen
                self._placeQueens(board, n, row + 1)  # Recur to place queen in next row
                board[row][col] = False  # Backtrack and remove the queen

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 4  # Example input
    result = solution.totalNQueens(n)
    print(f"Total solutions for {n}-Queens: {result}")

"""
Time complexity: O(n!)
Total space complexity: O(n^2) + O(n) ~ O(n^2)
Space complexity: O(n^2)
"""