#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#

# @lc code=start
import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get(s):
            quot, rem = divmod(s-1, n)
            row = n - 1 - quot
            col = rem if row%2 != n%2 else n - 1 - rem
            return row, col

        dist = {1: 0}
        queue = collections.deque([1])
        while queue:
            s = queue.popleft()
            if s == n*n: return dist[s]
            for s2 in range(s+1, min(s+6, n*n) + 1):
                r, c = get(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in dist:
                    dist[s2] = dist[s] + 1
                    queue.append(s2)
        return -1
# @lc code=end

