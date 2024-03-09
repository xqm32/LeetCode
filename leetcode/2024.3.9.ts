/*
 * @lc app=leetcode.cn id=763 lang=typescript
 *
 * [763] 划分字母区间
 */

// @lc code=start
function partitionLabels(s: string): number[] {
  const last = Array(26).fill(0);
  const length = s.length;
  const codePointA = "a".codePointAt(0)!;
  for (let i = 0; i < length; i++) {
    last[s.codePointAt(i)! - codePointA] = i;
  }
  const partition: number[] = [];
  let start = 0;
  let end = 0;
  for (let i = 0; i < length; i++) {
    end = Math.max(end, last[s.codePointAt(i)! - codePointA]);
    if (i === end) {
      partition.push(end - start + 1);
      start = end + 1;
    }
  }
  return partition;
}
// @lc code=end
