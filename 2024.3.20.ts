/*
 * @lc app=leetcode.cn id=368 lang=typescript
 *
 * [368] 最大整除子集
 */

// @lc code=start
function largestDivisibleSubset(nums: number[]): number[] {
	nums.sort((a, b) => a - b);
	const n = nums.length;
	const dp: number[] = new Array(n).fill(1);
	let maxSize = 1;
	let maxVal = dp[0];
	for (let i = 1; i < n; i++) {
		for (let j = 0; j < i; j++) {
			if (nums[i] % nums[j] === 0) {
				dp[i] = Math.max(dp[i], dp[j] + 1);
			}
		}
		if (dp[i] > maxSize) {
			maxSize = dp[i];
			maxVal = nums[i];
		}
	}
	const res: number[] = [];
	if (maxSize === 1) {
		res.push(nums[0]);
		return res;
	}
	for (let i = n - 1; i >= 0 && maxSize > 0; i--) {
		if (dp[i] === maxSize && maxVal % nums[i] === 0) {
			res.push(nums[i]);
			maxVal = nums[i];
			maxSize--;
		}
	}
	return res;
}
// @lc code=end
