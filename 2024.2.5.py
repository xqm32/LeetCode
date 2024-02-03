#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent, depth, x, y):
            if not node:
                return
            if node.val == x:
                self.x_parent = parent
                self.x_depth = depth
            elif node.val == y:
                self.y_parent = parent
                self.y_depth = depth
            dfs(node.left, node, depth + 1, x, y)
            dfs(node.right, node, depth + 1, x, y)

        self.x_parent = None
        self.y_parent = None
        self.x_depth = -1
        self.y_depth = -1
        dfs(root, None, 0, x, y)
        return self.x_depth == self.y_depth and self.x_parent != self.y_parent


# @lc code=end
