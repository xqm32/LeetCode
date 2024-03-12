/*
 * @lc app=leetcode.cn id=413 lang=typescript
 *
 * [413] 等差数列划分
 */

// @lc code=start
function numberOfArithmeticSlices(nums: number[]): number {
  const n = nums.length;
  if (n < 3) {
    return 0;
  }
  let dp = new Array(n).fill(0);
  for (let i = 2; i < n; i++) {
    if (nums[i] - nums[i - 1] === nums[i - 1] - nums[i - 2]) {
      dp[i] = dp[i - 1] + 1;
    }
  }
  return dp.reduce((prev, curr) => prev + curr, 0);
}
// @lc code=end
