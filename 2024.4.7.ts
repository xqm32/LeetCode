/*
 * @lc app=leetcode.cn id=447 lang=typescript
 *
 * [447] 回旋镖的数量
 */

// @lc code=start
function numberOfBoomerangs(points: number[][]): number {
  let res = 0;
  for (let i = 0; i < points.length; i++) {
    const map = new Map<number, number>();
    for (let j = 0; j < points.length; j++) {
      if (i === j) continue;
      const distance = getDistance(points[i], points[j]);
      map.set(distance, (map.get(distance) || 0) + 1);
    }
    for (const value of map.values()) {
      res += value * (value - 1);
    }
  }
  return res;

  function getDistance(p1: number[], p2: number[]): number {
    return Math.pow(p1[0] - p2[0], 2) + Math.pow(p1[1] - p2[1], 2);
  }
}
// @lc code=end
