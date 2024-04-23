/*
 * @lc app=leetcode.cn id=494 lang=typescript
 *
 * [494] 目标和
 */

// @lc code=start
function findTargetSumWays(nums: number[], target: number): number {
  let sum = nums.reduce((acc, cur) => acc + cur, 0);
  let diff = sum - target;
  if (diff < 0 || diff % 2 !== 0) {
    return 0;
  }
  let neg = diff / 2;
  let dp = new Array(neg + 1).fill(0);
  dp[0] = 1;
  for (let num of nums) {
    for (let j = neg; j >= num; j--) {
      dp[j] += dp[j - num];
    }
  }
  return dp[neg];
}
// @lc code=end
