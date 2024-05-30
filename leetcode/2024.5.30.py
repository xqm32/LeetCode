#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            if node.val > high:
                return dfs(node.left)
            if node.val < low:
                return dfs(node.right)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)


# @lc code=end
