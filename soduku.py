from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        line = [[] for _ in range(9)]
        column = [[] for _ in range(9)]
        square = [[] for _ in range(9)]

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                # print(f"Sudoku at position ({i}, {j}): {val}")
                
                if val == ".":
                    continue
                
                # if exist in line
                if val in line[i]:
                    return False
                line[i].append(val)
                
                # if exist in column
                if val in column[j]:
                    return False
                column[j].append(val)

                # if exist in square
                square_index = (i // 3) * 3 + (j // 3)
                if val in square[square_index]:
                    return False
                square[square_index].append(val)

        return True

s = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(s.isValidSudoku(board))