/*
 * @lc app=leetcode.cn id=306 lang=typescript
 *
 * [306] 累加数
 */

// @lc code=start
function isAdditiveNumber(num: string): boolean {
  const len = num.length;
  if (len < 3) {
    return false;
  }
  const dfs = (index: number, num1: string, num2: string): boolean => {
    if (index === len) {
      return true;
    }
    if (
      (num1[0] === "0" && num1.length > 1) ||
      (num2[0] === "0" && num2.length > 1)
    ) {
      return false;
    }
    const sum = addStrings(num1, num2);
    const sumLen = sum.length;
    if (index + sumLen > len) {
      return false;
    }
    const next = num.substring(index, index + sumLen);
    if (sum !== next) {
      return false;
    }
    return dfs(index + sumLen, num2, sum);
  };
  for (let i = 1; i <= len / 2; i++) {
    for (let j = 1; j <= (len - i) / 2; j++) {
      if (dfs(i + j, num.substring(0, i), num.substring(i, i + j))) {
        return true;
      }
    }
  }
  return false;
}

function addStrings(num1: string, num2: string): string {
  let i = num1.length - 1,
    j = num2.length - 1,
    add = 0;
  const res: string[] = [];
  while (i >= 0 || j >= 0 || add !== 0) {
    let x = i >= 0 ? num1.charCodeAt(i) - "0".charCodeAt(0) : 0;
    let y = j >= 0 ? num2.charCodeAt(j) - "0".charCodeAt(0) : 0;
    let sum = x + y + add;
    res.push(String.fromCharCode((sum % 10) + "0".charCodeAt(0)));
    add = Math.floor(sum / 10);
    i--;
    j--;
  }
  return res.reverse().join("");
}
// @lc code=end
