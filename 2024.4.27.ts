/*
 * @lc app=leetcode.cn id=1552 lang=typescript
 *
 * [1552] 两球之间的磁力
 */

// @lc code=start
function maxDistance(position: number[], m: number): number {
  position.sort((a, b) => a - b);
  let left = 1;
  let right = position[position.length - 1] - position[0];
  let res = 0;
  while (left <= right) {
    let mid = left + Math.floor((right - left) / 2);
    if (check(position, mid, m)) {
      res = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return res;
}

function check(position: number[], mid: number, m: number): boolean {
  let count = 1;
  let pre = position[0];
  for (let i = 1; i < position.length; i++) {
    if (position[i] - pre >= mid) {
      count++;
      pre = position[i];
    }
  }
  return count >= m;
}
// @lc code=end
