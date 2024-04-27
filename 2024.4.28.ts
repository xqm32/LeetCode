/*
 * @lc app=leetcode.cn id=687 lang=typescript
 *
 * [687] 最长同值路径
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

function longestUnivaluePath(root: TreeNode | null): number {
  let ans = 0;
  const dfs = (node: TreeNode | null): number => {
    if (!node) return 0;
    let left = dfs(node.left);
    let right = dfs(node.right);
    let leftPath = 0,
      rightPath = 0;
    if (node.left && node.left.val === node.val) {
      leftPath = left + 1;
    }
    if (node.right && node.right.val === node.val) {
      rightPath = right + 1;
    }
    ans = Math.max(ans, leftPath + rightPath);
    return Math.max(leftPath, rightPath);
  };
  dfs(root);
  return ans;
}
// @lc code=end
