#
# @lc app=leetcode.cn id=794 lang=python3
#
# [794] 有效的井字游戏
#

# @lc code=start
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count = sum(row.count("X") for row in board)
        o_count = sum(row.count("O") for row in board)
        if o_count not in {x_count - 1, x_count}:
            return False
        if self.win(board, "X") and x_count - 1 != o_count:
            return False
        if self.win(board, "O") and x_count != o_count:
            return False
        return True

    def win(self, board: List[str], player: str) -> bool:
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
            if all(board[j][i] == player for j in range(3)):
                return True
        if board[1][1] == player:
            if board[0][0] == board[2][2] == player:
                return True
            if board[0][2] == board[2][0] == player:
                return True
        return False


# @lc code=end
