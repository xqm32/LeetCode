#
# @lc app=leetcode.cn id=894 lang=python3
#
# [894] 所有可能的真二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1, n, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(n - i - 1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res


# @lc code=end
