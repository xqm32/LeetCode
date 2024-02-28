/*
 * @lc app=leetcode.cn id=830 lang=typescript
 *
 * [830] 较大分组的位置
 */

// @lc code=start
function largeGroupPositions(s: string): number[][] {
  const res: number[][] = [];
  let i = 0;
  let j = 0;
  while (i < s.length) {
    while (j < s.length && s[i] === s[j]) {
      j++;
    }
    if (j - i >= 3) {
      res.push([i, j - 1]);
    }
    i = j;
  }
  return res;
}
// @lc code=end
