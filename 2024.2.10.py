#
# @lc app=leetcode.cn id=1379 lang=python3
#
# [1379] 找出克隆二叉树中的相同节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        def dfs(node, target):
            if not node:
                return
            if node.val == target.val:
                return node
            return dfs(node.left, target) or dfs(node.right, target)

        return dfs(cloned, target)


# @lc code=end
