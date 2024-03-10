/*
 * @lc app=leetcode.cn id=764 lang=typescript
 *
 * [764] 最大加号标志
 */

// @lc code=start
function orderOfLargestPlusSign(n: number, mines: number[][]): number {
  const dp: number[][] = Array(n)
    .fill(0)
    .map(() => Array(n).fill(1));
  for (const [x, y] of mines) {
    dp[x][y] = 0;
  }
  const left = Array(n)
    .fill(0)
    .map(() => Array(n).fill(0));
  const right = Array(n)
    .fill(0)
    .map(() => Array(n).fill(0));
  const top = Array(n)
    .fill(0)
    .map(() => Array(n).fill(0));
  const bottom = Array(n)
    .fill(0)
    .map(() => Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    left[i][0] = dp[i][0];
    right[i][n - 1] = dp[i][n - 1];
    top[0][i] = dp[0][i];
    bottom[n - 1][i] = dp[n - 1][i];
  }
  for (let i = 0; i < n; i++) {
    for (let j = 1; j < n; j++) {
      left[i][j] = dp[i][j] === 0 ? 0 : left[i][j - 1] + 1;
      top[j][i] = dp[j][i] === 0 ? 0 : top[j - 1][i] + 1;
      right[i][n - j - 1] = dp[i][n - j - 1] === 0 ? 0 : right[i][n - j] + 1;
      bottom[n - j - 1][i] = dp[n - j - 1][i] === 0 ? 0 : bottom[n - j][i] + 1;
    }
  }
  let max = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      max = Math.max(
        max,
        Math.min(left[i][j], right[i][j], top[i][j], bottom[i][j])
      );
    }
  }
  return max;
}
// @lc code=end
