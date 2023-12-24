#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
            if not root:
                return None
            if root == p or root == q:
                return root
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right
            else:
                return None

        return dfs(root, p, q)


# @lc code=end
