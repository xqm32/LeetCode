#
# @lc app=leetcode.cn id=1339 lang=python3
#
# [1339] 分裂二叉树的最大乘积
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            node.val += dfs(node.left) + dfs(node.right)
            return node.val

        total = dfs(root)
        res = 0

        def dfs(node):
            if not node:
                return
            nonlocal res
            res = max(res, node.val * (total - node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res % (10**9 + 7)


# @lc code=end
