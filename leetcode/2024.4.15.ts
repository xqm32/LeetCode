/*
 * @lc app=leetcode.cn id=481 lang=typescript
 *
 * [481] 神奇字符串
 */

// @lc code=start
function magicalString(n: number): number {
  if (n === 0) return 0;
  if (n <= 3) return 1;
  const s = [1, 2, 2];
  let head = 2;
  let tail = 3;
  let num = 1;
  let res = 1;
  while (tail < n) {
    for (let i = 0; i < s[head]; i++) {
      s[tail] = num;
      if (num === 1 && tail < n) res++;
      tail++;
    }
    num = num ^ 3;
    head++;
  }
  return res;
}
// @lc code=end
