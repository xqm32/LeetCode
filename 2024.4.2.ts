/*
 * @lc app=leetcode.cn id=983 lang=typescript
 *
 * [983] 最低票价
 */

// @lc code=start
function mincostTickets(days: number[], costs: number[]): number {
	let dp: number[] = new Array(days[days.length - 1] + 1).fill(0);
	let set = new Set(days);
	for (let i = 1; i < dp.length; i++) {
		if (!set.has(i)) {
			dp[i] = dp[i - 1];
		} else {
			dp[i] = Math.min(
				dp[i - 1] + costs[0],
				dp[Math.max(0, i - 7)] + costs[1],
				dp[Math.max(0, i - 30)] + costs[2],
			);
		}
	}
	return dp[dp.length - 1];
}
// @lc code=end
