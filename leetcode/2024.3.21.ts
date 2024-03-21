/*
 * @lc app=leetcode.cn id=56 lang=typescript
 *
 * [56] 合并区间
 */

// @lc code=start
function merge(intervals: number[][]): number[][] {
	if (intervals.length === 0) return [];
	intervals.sort((a, b) => a[0] - b[0]);
	let res: number[][] = [intervals[0]];
	for (let i = 1; i < intervals.length; i++) {
		if (intervals[i][0] <= res[res.length - 1][1]) {
			res[res.length - 1][1] = Math.max(
				intervals[i][1],
				res[res.length - 1][1],
			);
		} else {
			res.push(intervals[i]);
		}
	}
	return res;
}
// @lc code=end
