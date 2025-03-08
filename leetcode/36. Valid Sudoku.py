from typing import List

# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not validate_row(board, i):
                return False

            if not validate_column(board, i):
                return False
        
        for (i, j) in [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]:
            if not validate_box(board, i, j):
                return False
        return True

def validate_row(board: List[List[str]], row: int) -> bool:
    numbers = list(map(int, filter(lambda cell: cell != ".", board[row])))
    if len(numbers) == 0:
        return True
    return max(numbers) <= 9 and min(numbers) >= 1 and len(numbers) == len(set(numbers))

def validate_column(board: List[List[str]], col: int) -> bool:
    numbers = []
    for i in range(9):
        cell = board[i][col]
        if cell != ".":
            numbers.append(int(cell))
    if len(numbers) == 0:
        return True
    return max(numbers) <= 9 and min(numbers) >= 1 and len(numbers) == len(set(numbers))


def validate_box(board: List[List[str]], box_center_x: int, box_center_y: int) -> bool:
    numbers = []
    for i in range(box_center_x - 1, box_center_x + 2):
        for j in range(box_center_y - 1, box_center_y + 2):
            cell = board[i][j] 
            if cell != ".":
                numbers.append(int(cell))

    if len(numbers) == 0:
        return True
    return max(numbers) <= 9 and min(numbers) >= 1 and len(numbers) == len(set(numbers))