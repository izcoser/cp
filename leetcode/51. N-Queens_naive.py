from typing import List

# https://leetcode.com/problems/n-queens/description/
# My naive solution that takes way too long and is ineficient.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        b = Board(n)
        results = set()

        def backtrack(board: Board):
            if board.count("Q") == n:
                results.add(board.as_tuple())
                return
            
            if board.count(".") == 0:
                return # dead end

            for i in range(n):
                for j in range(n):
                    if board.can_place_queen(i, j):
                        board_backup = [x[:] for x in board.board]
                        board.place_queen(i, j)

                        backtrack(board)

                        board.board = board_backup
        

        backtrack(b)

        results_as_matrix = []
        for r in results:
            a = [["." for _ in range(n)] for _ in range(n)]
            for (i, j) in r:
                a[i][j] = "Q"
            results_as_matrix.append(a)
        return results_as_matrix

class Board:
    def __init__(self, n: int):
        self.board = []
        self.size = n
        for i in range(n):
            self.board.append([])
            for j in range(n):
                self.board[i].append(".")
    
    def place_queen(self, i: int, j: int):
        # mark attacking squares
        for row in range(self.size):
            self.board[row][j] = '*'

        for col in range(self.size):
            self.board[i][col] = '*'

        # diagonals

        # stepping forward
        for n in range(1, self.size):
            if i - n >= 0 and j + n < self.size:
                self.board[i - n][j + n] = '*'
            if i + n < self.size and j + n < self.size:
                self.board[i + n][j + n] = '*'

        # stepping back
        for n in range(1, self.size):
            if i - n >= 0 and j - n >= 0:
                self.board[i - n][j - n] = '*'
            if i + n < self.size and j - n >= 0:
                self.board[i + n][j - n] = '*'

        self.board[i][j] = "Q"

    def can_place_queen(self, i: int, j: int) -> bool:
        if self.board[i][j] in ('Q', '*'):
            return False

        # check attacking squares
        for row in range(self.size):
            if self.board[row][j] == 'Q':
                return False

        for col in range(self.size):
            if self.board[i][col] == 'Q':
                return False

        # stepping forward
        for n in range(1, self.size):
            if i - n >= 0 and j + n < self.size and self.board[i - n][j + n] == 'Q':
                return False
            if i + n < self.size and j + n < self.size and self.board[i + n][j + n] == 'Q':
                return False
        
        # stepping back
        for n in range(1, self.size):
            if i - n >= 0 and j - n >= 0 and self.board[i - n][j - n] == 'Q':
                return False
            if i + n < self.size and j - n >= 0 and self.board[i + n][j - n] == 'Q':
                return False
        
        return True

    def count(self, c: str) -> int:
        count = 0
        for i in self.board:
            for j in i:
                if j == c:
                    count += 1
        return count

    def as_tuple(self):
        pos = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 'Q':
                    pos.append((i, j))
        return tuple(pos)

    def print(self):
        for i in range(self.size):
            for j in range(self.size):
                print(f" {self.board[i][j]} ", end="")
            print("")

a = Solution()
n = 5
res = a.solveNQueens(n)

for r in res:
    for i in range(n):
        for j in range(n):
            print(f" {r[i][j]} ", end="")
        print("")
    print("===========")