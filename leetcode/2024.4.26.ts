/*
 * @lc app=leetcode.cn id=451 lang=typescript
 *
 * [451] 根据字符出现频率排序
 */

// @lc code=start
function frequencySort(s: string): string {
  const map = new Map<string, number>();
  for (const c of s) {
    map.set(c, (map.get(c) || 0) + 1);
  }
  const list = Array.from(map.entries());
  list.sort((a, b) => b[1] - a[1]);
  return list.map(([c, count]) => c.repeat(count)).join("");
}
// @lc code=end
