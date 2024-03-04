/*
 * @lc app=leetcode.cn id=275 lang=typescript
 *
 * [275] H 指数 II
 */

// @lc code=start
function hIndex(citations: number[]): number {
  let left = 0;
  let right = citations.length - 1;
  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);
    if (citations[mid] === citations.length - mid) {
      return citations.length - mid;
    } else if (citations[mid] < citations.length - mid) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return citations.length - left;
}
// @lc code=end
