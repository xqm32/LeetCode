/*
 * @lc app=leetcode.cn id=3 lang=typescript
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
function lengthOfLongestSubstring(s: string): number {
  let charSet = new Set<string>();
  let [left, maxLength, currentLength] = [0, 0, 0];
  for (let i = 0; i < s.length; i += 1) {
    while (charSet.has(s[i])) {
      charSet.delete(s[left++]);
      currentLength -= 1;
    }
    charSet.add(s[i]);
    currentLength += 1;
    if (currentLength > maxLength) maxLength = currentLength;
  }
  return maxLength;
}
// @lc code=end

console.log(lengthOfLongestSubstring("abcabcbb"));
console.log(lengthOfLongestSubstring("bbbbb"));
console.log(lengthOfLongestSubstring("pwwkew"));
console.log(lengthOfLongestSubstring("aab"));
