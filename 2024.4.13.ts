/*
 * @lc app=leetcode.cn id=230 lang=typescript
 *
 * [230] 二叉搜索树中第K小的元素
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function kthSmallest(root: TreeNode | null, k: number): number {
  const res: number[] = [];
  inorder(root, res);
  return res[k - 1];
}

function inorder(root: TreeNode | null, res: number[]) {
  if (!root) {
    return;
  }

  inorder(root.left, res);
  res.push(root.val);
  inorder(root.right, res);
}

// @lc code=end
