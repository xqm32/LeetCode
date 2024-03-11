/*
 * @lc app=leetcode.cn id=784 lang=typescript
 *
 * [784] 字母大小写全排列
 */

// @lc code=start
function letterCasePermutation(s: string): string[] {
  const res: string[] = [];
  const dfs = (str: string, index: number) => {
    if (index === s.length) {
      res.push(str);
      return;
    }
    if (s[index] >= "0" && s[index] <= "9") {
      dfs(str + s[index], index + 1);
    } else {
      dfs(str + s[index].toLowerCase(), index + 1);
      dfs(str + s[index].toUpperCase(), index + 1);
    }
  };
  dfs("", 0);
  return res;
}
// @lc code=end
