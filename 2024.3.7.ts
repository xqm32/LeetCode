/*
 * @lc app=leetcode.cn id=316 lang=typescript
 *
 * [316] 去除重复字母
 */

// @lc code=start
function removeDuplicateLetters(s: string): string {
  const stack: string[] = [];
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (stack.includes(c)) continue;
    while (
      stack.length > 0 &&
      stack[stack.length - 1] > c &&
      s.indexOf(stack[stack.length - 1], i) > i
    ) {
      stack.pop();
    }
    stack.push(c);
  }
  return stack.join("");
}
// @lc code=end
