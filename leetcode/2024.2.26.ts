/*
 * @lc app=leetcode.cn id=508 lang=typescript
 *
 * [508] 出现次数最多的子树元素和
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

function findFrequentTreeSum(root: TreeNode | null): number[] {
  const map = new Map<number, number>();
  let maxCount = 0;

  function dfs(node: TreeNode | null): number {
    if (!node) {
      return 0;
    }
    const sum = dfs(node.left) + dfs(node.right) + node.val;
    const count = (map.get(sum) || 0) + 1;
    map.set(sum, count);
    maxCount = Math.max(maxCount, count);
    return sum;
  }

  dfs(root);
  const res: number[] = [];
  for (const [key, value] of map) {
    if (value === maxCount) {
      res.push(key);
    }
  }
  return res;
}
// @lc code=end
