/*
 * @lc app=leetcode.cn id=2729 lang=typescript
 *
 * [2729] 判断一个数是否迷人
 */

// @lc code=start
function isFascinating(n: number): boolean {
  const nString = n.toString() + (2 * n).toString() + (3 * n).toString();

  if (nString.includes("0")) return false;

  const set = new Set(nString);
  const good = Array.from(set).join("");
  if (nString.length === good.length && good.length === 9) return true;
  return false;
}
// @lc code=end
