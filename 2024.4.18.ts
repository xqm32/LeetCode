/*
 * @lc app=leetcode.cn id=647 lang=typescript
 *
 * [647] 回文子串
 */

// @lc code=start
function countSubstrings(s: string): number {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    count += countPalindrome(s, i, i);
    count += countPalindrome(s, i, i + 1);
  }
  return count;
}

function countPalindrome(s: string, left: number, right: number): number {
  let count = 0;
  while (left >= 0 && right < s.length && s[left] === s[right]) {
    count++;
    left--;
    right++;
  }
  return count;
}
// @lc code=end
