#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def is_leaf(x, y, length):
            for i in range(x, x + length):
                for j in range(y, y + length):
                    if grid[i][j] != grid[x][y]:
                        return False
            return True

        def construct_tree(x, y, length):
            if is_leaf(x, y, length):
                return Node(grid[x][y] == 1, True, None, None, None, None)
            else:
                half = length // 2
                return Node(
                    "*",
                    False,
                    construct_tree(x, y, half),
                    construct_tree(x, y + half, half),
                    construct_tree(x + half, y, half),
                    construct_tree(x + half, y + half, half),
                )

        return construct_tree(0, 0, len(grid))


# @lc code=end
