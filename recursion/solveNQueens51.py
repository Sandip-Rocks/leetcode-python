"""
51. N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]

Constraints:

1 <= n <= 9
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []  # List to store the final solutions
        board = [[False] * n for _ in range(n)]  # Board to track the queens' positions
        self.func(board, n, 0, ans)  # Start recursion from row 0
        return ans  # Return the list of solutions

    def isValid(self, board: List[List[bool]], n: int, row: int, col: int) -> bool:
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

    def func(self, board: List[List[bool]], n: int, row: int, ans: List[List[str]]):
        if row == n:  # If all queens are placed
            ans.append(self.createCopy(board, n))  # Add a valid configuration
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            if self.isValid(board, n, row, col):  # Check if placing queen at (row, col) is valid
                board[row][col] = True  # Place the queen
                self.func(board, n, row + 1, ans)  # Recur to place queen in next row
                board[row][col] = False  # Backtrack and remove the queen

    def createCopy(self, board: List[List[bool]], n: int) -> List[str]:
        copy = []
        for i in range(n):
            row = ''.join('Q' if board[i][j] else '.' for j in range(n))
            copy.append(row)
        return copy

# To test the code
if __name__ == "__main__":
    n = 4  # Change this value to test with different sizes
    solution = Solution()
    result = solution.solveNQueens(n)
    for r in result:
        print(r)
