/*
 * @lc app=leetcode.cn id=131 lang=typescript
 *
 * [131] 分割回文串
 */

// @lc code=start
function partition(s: string): string[][] {
  const res: string[][] = [];
  const path: string[] = [];
  backtracking(s, 0, path, res);
  return res;
}

function backtracking(
  s: string,
  start: number,
  path: string[],
  res: string[][]
) {
  if (start === s.length) {
    res.push([...path]);
    return;
  }

  for (let i = start; i < s.length; i++) {
    if (isPalindrome(s, start, i)) {
      path.push(s.substring(start, i + 1));
      backtracking(s, i + 1, path, res);
      path.pop();
    }
  }
}

function isPalindrome(s: string, left: number, right: number): boolean {
  while (left < right) {
    if (s[left] !== s[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}
// @lc code=end
