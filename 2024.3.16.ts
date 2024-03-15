/*
 * @lc app=leetcode.cn id=453 lang=typescript
 *
 * [453] 最小操作次数使数组元素相等
 */

// @lc code=start
function minMoves(nums: number[]): number {
  const min = Math.min(...nums);
  return nums.reduce((acc, cur) => acc + cur - min, 0);
}
// @lc code=end
