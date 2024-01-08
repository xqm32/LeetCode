#
# @lc app=leetcode.cn id=419 lang=python3
#
# [419] 甲板上的战舰
#

# @lc code=start
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "X":
                    continue
                if i > 0 and board[i - 1][j] == "X":
                    continue
                if j > 0 and board[i][j - 1] == "X":
                    continue
                res += 1
        return res


# @lc code=end
