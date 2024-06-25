#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(x, y, val):
            for i in range(9):
                if board[x][i] == val:
                    return False
                if board[i][y] == val:
                    return False
                if board[(x // 3) * 3 + i // 3][(y // 3) * 3 + i % 3] == val:
                    return False
            return True

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] != ".":
                        continue
                    for val in range(1, 10):
                        if not is_valid(i, j, str(val)):
                            continue
                        board[i][j] = str(val)
                        if backtrack():
                            return True
                        board[i][j] = "."
                    return False
            return True

        backtrack()


# @lc code=end
