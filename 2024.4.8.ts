/*
 * @lc app=leetcode.cn id=467 lang=typescript
 *
 * [467] 环绕字符串中唯一的子字符串
 */

// @lc code=start
function findSubstringInWraproundString(s: string): number {
  const dp = Array(26).fill(0);
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (
      i > 0 &&
      (s.charCodeAt(i) - s.charCodeAt(i - 1) === 1 ||
        s.charCodeAt(i - 1) - s.charCodeAt(i) === 25)
    ) {
      count++;
    } else {
      count = 1;
    }
    const index = s.charCodeAt(i) - 97;
    dp[index] = Math.max(dp[index], count);
  }
  return dp.reduce((prev, curr) => prev + curr, 0);
}
// @lc code=end
