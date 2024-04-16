/*
 * @lc app=leetcode.cn id=686 lang=typescript
 *
 * [686] 重复叠加字符串匹配
 */

// @lc code=start
function repeatedStringMatch(a: string, b: string): number {
  const n = Math.ceil(b.length / a.length);
  let s = "";
  for (let i = 0; i < n; i++) {
    s += a;
    if (s.includes(b)) {
      return i + 1;
    }
  }
  s += a;
  if (s.includes(b)) {
    return n + 1;
  }
  return -1;
}
// @lc code=end
