/*
 * @lc app=leetcode.cn id=583 lang=typescript
 *
 * [583] 两个字符串的删除操作
 */

// @lc code=start
function minDistance(word1: string, word2: string): number {
	const m = word1.length;
	const n = word2.length;
	const dp: number[][] = Array.from(new Array(m + 1), () =>
		new Array(n + 1).fill(0),
	);
	for (let i = 1; i <= m; i++) {
		dp[i][0] = i;
	}
	for (let j = 1; j <= n; j++) {
		dp[0][j] = j;
	}
	for (let i = 1; i <= m; i++) {
		for (let j = 1; j <= n; j++) {
			if (word1[i - 1] === word2[j - 1]) {
				dp[i][j] = dp[i - 1][j - 1];
			} else {
				dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + 1;
			}
		}
	}
	return dp[m][n];
}
// @lc code=end
