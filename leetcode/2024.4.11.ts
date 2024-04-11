/*
 * @lc app=leetcode.cn id=324 lang=typescript
 *
 * [324] 摆动排序 II
 */

// @lc code=start
/**
 Do not return anything, modify nums in-place instead.
 */
function wiggleSort(nums: number[]): void {
  const n = nums.length;
  const mid = Math.floor((n + 1) / 2);
  nums.sort((a, b) => a - b);
  const small = nums.slice(0, mid);
  const large = nums.slice(mid);
  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) {
      nums[i] = small.pop()!;
    } else {
      nums[i] = large.pop()!;
    }
  }
}
// @lc code=end
