/*
 * @lc app=leetcode.cn id=113 lang=typescript
 *
 * [113] 路径总和 II
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

function pathSum(root: TreeNode | null, targetSum: number): number[][] {
  const res: number[][] = [];
  const path: number[] = [];
  dfs(root, targetSum, path, res);
  return res;
}

function dfs(
  root: TreeNode | null,
  targetSum: number,
  path: number[],
  res: number[][]
) {
  if (!root) {
    return;
  }
  path.push(root.val);
  targetSum -= root.val;
  if (!root.left && !root.right && targetSum === 0) {
    res.push([...path]);
  }
  dfs(root.left, targetSum, path, res);
  dfs(root.right, targetSum, path, res);
  path.pop();
}
// @lc code=end
