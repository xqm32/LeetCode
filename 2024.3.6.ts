/*
 * @lc app=leetcode.cn id=567 lang=typescript
 *
 * [567] 字符串的排列
 */

// @lc code=start
function compareMap(
  map1: Map<string, number>,
  map2: Map<string, number>
): boolean {
  if (map1.size !== map2.size) {
    return false;
  }
  for (const [key, value] of map1) {
    if (map2.get(key) !== value) {
      return false;
    }
  }
  return true;
}

function checkInclusion(s1: string, s2: string): boolean {
  const s1Len = s1.length;
  const s2Len = s2.length;
  if (s1Len > s2Len) {
    return false;
  }
  const s1Map = new Map<string, number>();
  const s2Map = new Map<string, number>();
  for (let i = 0; i < s1Len; i++) {
    s1Map.set(s1[i], (s1Map.get(s1[i]) || 0) + 1);
    s2Map.set(s2[i], (s2Map.get(s2[i]) || 0) + 1);
  }
  for (let i = 0; i < s2Len - s1Len; i++) {
    if (compareMap(s1Map, s2Map)) {
      return true;
    }
    s2Map.set(s2[i + s1Len], (s2Map.get(s2[i + s1Len]) || 0) + 1);
    s2Map.set(s2[i], s2Map.get(s2[i]) - 1);
    if (s2Map.get(s2[i]) === 0) {
      s2Map.delete(s2[i]);
    }
  }
  return compareMap(s1Map, s2Map);
}
// @lc code=end
