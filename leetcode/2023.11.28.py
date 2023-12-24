#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def count(i, j):
            c = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                        continue
                    if x == i and y == j:
                        continue
                    if board[x][y] == 1 or board[x][y] == 2:
                        c += 1
            return c

        for i in range(len(board)):
            for j in range(len(board[0])):
                c = count(i, j)
                if board[i][j] == 0:
                    if c == 3:
                        board[i][j] = 3
                else:
                    if c < 2 or c > 3:
                        board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1


# @lc code=end
