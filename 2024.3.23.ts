/*
 * @lc app=leetcode.cn id=452 lang=typescript
 *
 * [452] 用最少数量的箭引爆气球
 */

// @lc code=start
function findMinArrowShots(points: number[][]): number {
	points.sort((a, b) => a[1] - b[1]);
	let ans = 1;
	let end = points[0][1];
	for (let i = 1; i < points.length; i++) {
		if (points[i][0] > end) {
			ans++;
			end = points[i][1];
		}
	}
	return ans;
}
// @lc code=end
