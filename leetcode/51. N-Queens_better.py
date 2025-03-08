from typing import List

# https://leetcode.com/problems/n-queens/description/
# My better solution.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        positions = [-1] * n  # Index is the row, value is the column where the queen will be. positions[row] = col (placement of queen in row)
        cols_used = set()
        diag_used = set()      # store (row - col)
        anti_diag_used = set() # store (row + col)

        def backtrack(row):
            if row == n:
                results.append(make_board_from_positions(positions))
                return
            
            for col in range(n):
                if col not in cols_used and (row - col) not in diag_used and (row + col) not in anti_diag_used:
                    positions[row] = col
                    cols_used.add(col)
                    diag_used.add(row - col)
                    anti_diag_used.add(row + col)
                    
                    backtrack(row + 1)
                    
                    positions[row] = -1
                    cols_used.remove(col)
                    diag_used.remove(row - col)
                    anti_diag_used.remove(row + col)

        backtrack(0)
        return results

def make_board_from_positions(positions: List[int]) -> List[str]:
    size = len(positions)
    board = []
    for p in positions:
        row_as_list = ["."] * size
        row_as_list[p] = "Q"
        row = ''.join(row_as_list)
        board.append(row)
    return board


if __name__ == "__main__":
    a = Solution()
    n = 9
    res = a.solveNQueens(n)

    for r in res:
        for i in r:
            print(i)
        print("=====")
        