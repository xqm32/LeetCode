/*
 * @lc app=leetcode.cn id=655 lang=typescript
 *
 * [655] 输出二叉树
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

function printTree(root: TreeNode | null): string[][] {
  const height = getHeight(root);
  const width = Math.pow(2, height) - 1;
  const res: string[][] = Array.from({ length: height }, () =>
    Array(width).fill("")
  );
  fill(root, 0, 0, width - 1, res);
  return res;
}

function getHeight(root: TreeNode | null): number {
  if (!root) return 0;
  return 1 + Math.max(getHeight(root.left), getHeight(root.right));
}

function fill(
  root: TreeNode | null,
  row: number,
  left: number,
  right: number,
  res: string[][]
): void {
  if (!root) return;
  const mid = left + Math.floor((right - left) / 2);
  res[row][mid] = root.val.toString();
  fill(root.left, row + 1, left, mid - 1, res);
  fill(root.right, row + 1, mid + 1, right, res);
}
// @lc code=end
