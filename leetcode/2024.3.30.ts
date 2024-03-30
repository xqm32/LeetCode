/*
 * @lc app=leetcode.cn id=788 lang=typescript
 *
 * [788] 旋转数字
 */

// @lc code=start
function rotatedDigits(n: number): number {
	let res = 0;
	for (let i = 1; i <= n; i++) {
		if (isGood(i)) {
			res++;
		}
	}
	return res;
}

function isGood(n: number): boolean {
	let flag = false;
	while (n) {
		let t = n % 10;
		if (t === 3 || t === 4 || t === 7) {
			return false;
		}
		if (t === 2 || t === 5 || t === 6 || t === 9) {
			flag = true;
		}
		n = Math.floor(n / 10);
	}
	return flag;
}
// @lc code=end
